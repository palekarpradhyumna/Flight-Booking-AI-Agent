from flask import Flask, request, jsonify

app = Flask(__name__)

FLIGHT_DATA = [
  {"origin": "Nagpur", "destination": "Pune", "date": "20/11/2025", "flight_number": "AI-851", "departure_time": "10:30 AM", "price": "₹4500"},
  {"origin": "Nagpur", "destination": "Pune", "date": "20/11/2025", "flight_number": "6E-432", "departure_time": "02:15 PM", "price": "₹3900"},
  {"origin": "Nagpur", "destination": "Mumbai", "date": "21/11/2025", "flight_number": "G8-219", "departure_time": "08:45 AM", "price": "₹3200"},
  {"origin": "Pune", "destination": "Delhi", "date": "22/11/2025", "flight_number": "AI-203", "departure_time": "06:00 AM", "price": "₹6200"},
  {"origin": "Pune", "destination": "Delhi", "date": "22/11/2025", "flight_number": "6E-701", "departure_time": "11:20 AM", "price": "₹5700"},
  {"origin": "Pune", "destination": "Delhi", "date": "22/11/2025", "flight_number": "UK-889", "departure_time": "07:45 PM", "price": "₹6900"},
  {"origin": "Mumbai", "destination": "Bangalore", "date": "23/11/2025", "flight_number": "AI-543", "departure_time": "09:40 AM", "price": "₹4800"},
  {"origin": "Mumbai", "destination": "Bangalore", "date": "23/11/2025", "flight_number": "6E-919", "departure_time": "01:10 PM", "price": "₹4300"},
  {"origin": "Mumbai", "destination": "Bangalore", "date": "23/11/2025", "flight_number": "G8-554", "departure_time": "05:25 PM", "price": "₹4700"},
  {"origin": "Delhi", "destination": "Nagpur", "date": "24/11/2025", "flight_number": "AI-789", "departure_time": "08:00 AM", "price": "₹5200"},
  {"origin": "Delhi", "destination": "Nagpur", "date": "24/11/2025", "flight_number": "6E-522", "departure_time": "12:35 PM", "price": "₹4800"},
  {"origin": "Delhi", "destination": "Nagpur", "date": "24/11/2025", "flight_number": "V-312", "departure_time": "06:45 PM", "price": "₹5400"},
  {"origin": "Bangalore", "destination": "Pune", "date": "25/11/2025", "flight_number": "6E-112", "departure_time": "07:00 AM", "price": "₹3500"},
  {"origin": "Bangalore", "destination": "Pune", "date": "25/11/2025", "flight_number": "AI-404", "departure_time": "03:15 PM", "price": "₹4200"},
  {"origin": "Bangalore", "destination": "Pune", "date": "25/11/2025", "flight_number": "G8-901", "departure_time": "09:30 PM", "price": "₹3900"},
  {"origin": "Mumbai", "destination": "Chennai", "date": "26/11/2025", "flight_number": "AI-602", "departure_time": "06:40 AM", "price": "₹4500"},
  {"origin": "Mumbai", "destination": "Chennai", "date": "26/11/2025", "flight_number": "6E-903", "departure_time": "12:10 PM", "price": "₹4100"},
  {"origin": "Mumbai", "destination": "Chennai", "date": "26/11/2025", "flight_number": "V-882", "departure_time": "08:25 PM", "price": "₹4600"},
  {"origin": "Chennai", "destination": "Delhi", "date": "27/11/2025", "flight_number": "AI-108", "departure_time": "05:55 AM", "price": "₹7200"},
  {"origin": "Chennai", "destination": "Delhi", "date": "27/11/2025", "flight_number": "6E-887", "departure_time": "02:45 PM", "price": "₹6900"},
  {"origin": "Chennai", "destination": "Delhi", "date": "27/11/2025", "flight_number": "UK-450", "departure_time": "10:20 PM", "price": "₹7600"},
  {"origin": "Nagpur", "destination": "Bangalore", "date": "28/11/2025", "flight_number": "AI-311", "departure_time": "09:00 AM", "price": "₹5400"},
  {"origin": "Nagpur", "destination": "Bangalore", "date": "28/11/2025", "flight_number": "6E-111", "departure_time": "04:10 PM", "price": "₹5000"},
  {"origin": "Nagpur", "destination": "Bangalore", "date": "28/11/2025", "flight_number": "G8-703", "departure_time": "08:20 PM", "price": "₹5300"}
]


@app.route("/searchFlights", methods=["POST"])
def search_flights():
    data = request.get_json()
    origin = data.get("origin")
    destination = data.get("destination")
    date = data.get("date")

    results = [
        flight for flight in FLIGHT_DATA
        if flight["origin"].lower() == origin.lower()
        and flight["destination"].lower() == destination.lower()
        and flight["date"] == date
    ]

    return jsonify({"flights": results})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
