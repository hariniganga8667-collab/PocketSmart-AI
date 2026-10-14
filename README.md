# PocketSmart AI

## AI-Powered Budget & Recommendation Assistant

PocketSmart AI is a GenAI-powered recommendation system that helps users make smart purchasing and planning decisions according to their budget and personal preferences.

The application provides personalized recommendations for three major planning areas:

- Home Interior
- Party Planning
- Jewelry Planning

The system uses Google's Gemini API to generate recommendations based on the user's requirements.

---

## Features

### 🏠 Home Interior Planner

Users can enter:

- Budget
- Room type
- Required items
- Preferred interior style

PocketSmart AI generates a personalized interior planning suggestion with budget allocation, recommendations and money-saving tips.

### 🎉 Party Planner

Users can enter:

- Budget
- Number of guests
- Event type
- Venue
- Requirements

The system generates a party plan including food, decoration, cake, entertainment and other expenses.

### 💎 Jewelry Planner

Users can enter:

- Budget
- Occasion
- Preferred style
- Jewelry requirements

The system recommends suitable jewelry options and provides a budget allocation.

---

## Technology Stack

### Frontend
- HTML5
- CSS3
- JavaScript
- Jinja2 Templates

### Backend
- Python
- FastAPI
- Uvicorn

### AI
- Google Gemini API
- Google GenAI SDK

### Other
- Python-dotenv
- Python Multipart
- Git & GitHub

---

## Project Structure

```text
PocketSmart-AI/
│
├── app/
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── js/
│   │
│   ├── templates/
│   │   ├── index.html
│   │   ├── home_planner.html
│   │   ├── party_planner.html
│   │   └── jewelry_planner.html
│   │
│   ├── database.py
│   ├── gemini_utils.py
│   ├── main.py
│   ├── routes.py
│   └── schemas.py
│
├── tests/
├── .env
├── .gitignore
├── README.md
└── requirements.txt