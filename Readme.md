FAST API
FastAPI-based backend for managing events and users. This API provides endpoints for creating, retrieving, updating, and deleting events and user data. It is designed to be scalable, efficient, and easy to integrate with your frontend application.

Features

User Management:
Create, retrieve, update, and delete user details.
Event Management:
Create, retrieve, update, and delete events.
Link events to their respective organizers (users).
Database Relationships:
One-to-many relationship between users and events.
Interactive API Docs:
Automatically generated documentation using FastAPI's Swagger UI.

Project Structure

.
├── app.py            # Main FastAPI application
├── README.md         # Project documentation
├── requirements.txt  # List of dependencies
└── event_nest.db     # SQLite database (auto-created on first run)


Getting Started
Prerequisites
Python 3.8 or later
Pip for managing dependencies


Installation
Clone this repository:


git clone https://github.com/your-username/eventnest.git
cd eventnest
Install dependencies:


pip install -r requirements.txt
Run the application:


uvicorn app:app --reload
Access the API documentation at:


http://127.0.0.1:8000/docs


Database Configuration
This project uses SQLite as the default database. If you want to switch to a different database (e.g., PostgreSQL, MySQL), update the DATABASE_URL in the app.py file with the appropriate connection string.

Endpoints
User Endpoints
Method	Endpoint	Description
POST	/users/	Create a new user
GET	/users/{id}	Get user details
PUT	/users/{id}	Update user information
DELETE	/users/{id}	Delete a user


Event Endpoints
Method	Endpoint	Description
POST	/events/	Create a new event
GET	/events/	Retrieve all events
GET	/events/{id}	Get event details
PUT	/events/{id}	Update event information
DELETE	/events/{id}	Delete an event


Technologies Used
Framework: FastAPI
Database: SQLite (default, but can be switched)
ORM: SQLAlchemy
Web Server: Uvicorn


Future Enhancements
Add authentication and authorization (e.g., JWT tokens).
Include event registration and participant tracking.
Implement real-time chat rooms using WebSockets.
Add multilingual support.

Contributing
Contributions are welcome! To contribute to EventNest:

Fork this repository.
Create a new branch for your feature/bugfix.
Submit a pull request with detailed explanations.

License
This project is licensed under the MIT License