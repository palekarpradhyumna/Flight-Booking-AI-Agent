<h1 align="center">✈️ FlightMate – AI-Powered Flight Booking Assistant</h1>

<p align="center">
  <b>Your smart travel companion for effortless flight booking.</b><br>
  Powered by AI • Built for Conversational Travel Experiences
</p>

---

## 🚀 Overview

FlightMate is an intelligent **Flight Booking AI Agent** that allows users to search, compare, and book flights through natural language chats.  
It connects with a backend API that provides flight data and automates the full booking experience.
Project Video Link : https://www.loom.com/share/04efbe2196b54fb19e543333633868c3

---

## ✨ Features

- 🗣️ Natural language-based search & booking  
- 📍 Search by location, dates, budget & timings  
- 📊 Side-by-side flight comparison  
- 🧾 Complete booking process with validations  
- 🤖 Designed for Google Vertex AI Agents / Playbooks  
- 🔌 Flexible API-first architecture  

---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| AI Agent | Google Vertex AI Playbooks / Agents |
| Backend | Python + FastAPI / Flask |
| Tunneling | Ngrok |
| Data Format | JSON |
| Tool Invocation | OpenAPI-based function calling |

---

## 📂 Repository Structure
FlightMate/
│
├── backend/
│ ├── Flight_api.py # Backend logic & flight search tool
│ ├── webhook_rest_api.json # Demo flight dataset
│ └── 
│
├── agent/
│ ├── tool_schema.json # Tool definition (OpenAPI)
│ └── Google Cloud Conversational AI  # Conversation flows
│
└── README.md

