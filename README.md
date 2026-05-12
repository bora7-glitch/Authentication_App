# Auth App 🔐

A simple web-based authentication app built with Python. Supports user registration, login, and logout with secure password hashing.

## Features
- User Signup with password confirmation
- Secure Login with SHA-256 password hashing
- Cookie-based session management
- Logout functionality
- SQLite database for user storage

## Tech Stack
- **Python** — core language
- **Bottle** — lightweight web framework
- **SQLite** — local database
- **Hashlib** — SHA-256 password hashing

## How to Run

### 1. Install Bottle
pip install bottle

### 2. Run the app
python app.py

### 3. Open in browser
http://localhost:4050

## Routes
| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET/POST | Login page |
| `/signup` | GET/POST | Signup page |
| `/home` | GET/POST | Home page (after login) |

## Requirements
- Python 3.x
- Bottle (`pip install bottle`)
