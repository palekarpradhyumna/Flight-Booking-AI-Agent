from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_BASE_URL = "https://euphonic-springlike-braxton.ngrok-free.dev/searchFlights" 

@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json(silent=True, force=True)

    parameters = req.get("queryResult", {}).get("parameters", {})
    origin = parameters.get("departure_city")
    destination = parameters.get("destination_city")
    date = parameters.get("travel_date")
    payload = {
        "origin": origin,
        "destination": destination,
        "date": date
    }

    try:
        response = requests.post(API_BASE_URL, json=payload, timeout=10)
        response.raise_for_status()
        flight_data = response.json()
        
        if flight_data.get("flights"):
            first_flight = flight_data["flights"][0]
            message = (
                f"Flight {first_flight['flight_number']} from {origin} to {destination} "
                f"departs at {first_flight['departure_time']} and costs {first_flight['price']}."
            )
        else:
            message = f"Sorry, no flights found from {origin} to {destination} on {date}."

    except requests.exceptions.RequestException as e:
        message = f"Unable to connect to flight service: {str(e)}"
    except Exception as e:
        message = f"An unexpected error occurred: {str(e)}"

    return jsonify({
        "fulfillmentMessages": [
            {"text": {"text": [message]}}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)