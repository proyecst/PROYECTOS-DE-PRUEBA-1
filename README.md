
Order Management Dashboard
Project Description
This project is an order management platform with a user interface (frontend) and a backend API. The application allows you to view key metrics such as total revenue, products sold, and pending orders, and is designed to simulate a scalable cloud architecture using AWS services.

Features
Interactive Dashboard: Displays key metrics in real time.

Flask Backend: A simple RESTful API for serving dashboard data.

HTML/CSS/JS Frontend: Intuitive and adaptable user interface.

AWS Simulation: Demonstration of how services such as AWS Lambda and S3 would be integrated for robust event handling.

API Documentation: Documentation.yaml file for a clear understanding of the endpoints.

Architecture
The project is divided into two main components:

Frontend: A static web interface built with HTML, CSS, and JavaScript that connects to the backend API to retrieve and display data.

Backend: A RESTful API developed with Python and Flask that simulates data processing and integration with cloud services.

AWS Integration (Simulation)
We simulated a flow of order events using two key AWS services:

AWS Lambda: A serverless function that would be triggered upon receiving a new order through the /api/orders/event endpoint. This function would process the order data.

Amazon S3: The event storage location. The Lambda function would save the details of each order as a JSON file in an S3 bucket, creating a durable and immutable event record.

Installation
Requirements
Make sure you have Python 3.x and pip installed.

Steps
Clone the repository:

Bash

git clone [REPOSITORY_URL]
cd [project_name]
Set up the virtual environment and install the backend dependencies:

Bash

python -m venv venv
source venv/bin/activate # On macOS/Linux
# or venv\Scripts\activate # On Windows

pip install Flask flask_cors
Run the backend:

Bash

python app.py
The server will start at http://127.0.0.1:5000.

Open the frontend:
Simply open the index.html file in your web browser. The JavaScript in the file will automatically connect to the backend to load the data.

Project Structure

├── app.py # API backend (Python/Flask)
├── documentation.yaml # API documentation (OpenAPI)
├── index.html # UI frontend
└── style.css # Styles for the frontend
API Endpoints
The backend API exposes the following endpoints:

Method Endpoint Description
GET /api/dashboard Gets metrics and data for the dashboard.
POST /api/orders/event Simulates processing a new order event.
