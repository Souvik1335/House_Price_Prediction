🏠 House Price Prediction --- End-to-End Data Science Application

An end-to-end House Price Prediction application built todemonstrate how a Machine Learning model can be transformed into acomplete, production-style Data Science application.

The project goes beyond training a model by integrating:
1) Machine Learning
2) FastAPI backend
3) Streamlit frontend
4) PostgreSQL database through Supabase
5) JWT-based authentication
6) User registration and login
7) Password reset
8) User profile
9) Prediction history
10) Docker
11) REST API
12) Cloud deployment using Render

🚀 Live Application

Frontend
Users should use the Streamlit frontend to interact with theapplication:

House Price Prediction App:https://house-price-prediction-1-4we3.onrender.com

Backend API
The FastAPI backend is deployed separately:

Backend API:https://house-price-prediction-vsnv.onrender.com

API Documentation
Interactive Swagger documentation is available at:

Swagger UI:https://house-price-prediction-vsnv.onrender.com/docs

✨ Features

1) 👤 Authentication & User Management
2) User registration
3) Email-based login
4) Password confirmation during registration
5) JWT authentication
6) Secure protected API routes
7) User profile
8) Password reset
9) Logout
10) 🏠 House Price Prediction
11) Accepts house-related input features
12) Sends prediction requests to the FastAPI backend
13) Uses the trained Machine Learning model
14) Returns the predicted house price through the Streamlit interface

📊 Prediction History

Authenticated users can:

1) View previous predictions
2) Store prediction results in the database
3) Retrieve their own prediction history

🗄️ Database

1) The application uses Supabase PostgreSQL for persistent storage.
2)The database stores application data such as:

2.1) User information
2.2) Authentication-related information
2.3) Prediction records

🐳 Docker

The backend is containerized using Docker to provide a reproducibledeployment environment.

☁️ Deployment

The application is deployed as separate frontend and backend services:

Streamlit Frontend
        │
        ▼
FastAPI Backend
        │
        ├── Machine Learning Model
        │
        └── Supabase PostgreSQL

🧠 Machine Learning Workflow

The Machine Learning component follows a standard supervised learningworkflow:

Dataset
   ↓
Data Preprocessing
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
Train/Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Selection
   ↓
Model Serialization
   ↓
FastAPI Prediction Endpoint
   ↓
Streamlit Application

The trained model is integrated into the backend so that predictions canbe generated through an API instead of running the training process forevery request.

🏗️ System Architecture

                         ┌─────────────────────┐
                         │       User          │
                         └──────────┬──────────┘
                                    │
                                    ▼
                    ┌────────────────────────────┐
                    │   Streamlit Frontend       │
                    │                            │
                    │ • Register                 │
                    │ • Login                    │
                    │ • Profile                  │
                    │ • Prediction               │
                    │ • Prediction History       │
                    │ • Logout                   │
                    └────────────┬───────────────┘
                                 │
                                 │ HTTP Requests
                                 ▼
                    ┌────────────────────────────┐
                    │       FastAPI Backend      │
                    │                            │
                    │ • Authentication           │
                    │ • JWT Verification         │
                    │ • User Management          │
                    │ • Prediction API           │
                    │ • History API              │
                    └───────┬───────────┬────────┘
                            │           │
                            │           │
                            ▼           ▼
                 ┌──────────────┐  ┌──────────────┐
                 │ ML Prediction│  │   Supabase   │
                 │    Model     │  │ PostgreSQL   │
                 └──────────────┘  └──────────────┘

🔐 Authentication Flow

The application uses JWT-based authentication.

User
 │
 ├── Register
 │      ↓
 │   FastAPI
 │      ↓
 │   Database
 │
 └── Login
        ↓
   FastAPI Authentication
        ↓
   JWT Access Token
        ↓
   Streamlit Session
        ↓
   Protected API Requests

Protected requests include the JWT token in the Authorization header:

Authorization: Bearer <access_token>

🔌 API Endpoints

Authentication

Method   Endpoint                  Description

POST     /register               Register a new userPOST     /auth/login             Authenticate user and obtain JWTPOST     /auth/forgot-password   Reset user passwordPOST     /auth/logout            Logout authenticated user

User

Method   Endpoint     Description

GET      /user/me   Get authenticated user's profile

Prediction

Method                  Endpoint                Description

POST                    /prediction/predict   Generate a house priceprediction

For complete request/response schemas, use the interactive Swaggerdocumentation:

https://house-price-prediction-vsnv.onrender.com/docs

🖥️ Frontend Pages

The Streamlit frontend provides a complete user-facing workflow.

📝 Register

Users can create an account by providing:

1) Full name
2) Email
3) Personal phone number
4) Alternate phone number
5) Date of birth
6) Password
7) Password confirmation
8) 🔐 Login
9) Registered users can authenticate and access protected applicationfeatures.

👤 Profile

Authenticated users can view their profile information.

🏠 House Price Prediction

Users provide the required house information and receive a predictedprice from the Machine Learning model.

📜 Prediction History

Users can view their previous house price predictions.

🔑 Forgot Password

Users can reset their password through the password reset workflow.

🚪 Logout

Users can securely end their authenticated session.

🛠️ Technology Stack

Programming Language

Python

Machine Learning

1) Pandas
2) NumPy
3) Scikit-learn

Joblib / model serialization

Backend

1) FastAPI
2) Pydantic
3) Uvicorn

Python Requests / HTTP client integration

Frontend

Streamlit

Database

1) Supabase
2) PostgreSQL
3) SQLAlchemy

Authentication

1) JWT
2) OAuth2 password flow
3) Password hashing

Deployment & DevOps

1) Docker
2) Render
3) Git
4) GitHub

📁 Project Structure

A simplified representation of the project architecture:

HOUSE_PRICE_PREDICTION/
│
├── Backend/
│   ├── API / Routers
│   ├── Authentication
│   ├── JWT Verification
│   ├── Database Models
│   ├── Prediction Logic
│   ├── ML Model
│   └── FastAPI Application
│
├── Frontend/
│   ├── Streamlit Pages
│   │   ├── Register
│   │   ├── Login
│   │   ├── Profile
│   │   ├── Prediction
│   │   ├── Prediction History
│   │   ├── Forgot Password
│   │   └── Logout
│   │
│   └── API Utility Functions
│
├── Model/
│   └── Trained ML Model
│
├── requirements.txt
├── Dockerfile
└── README.md

The exact folder and filename structure may vary depending on thelocal development version of the project.

⚙️ Local Setup

1. Clone the repository

git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_DIRECTORY>

2. Create a virtual environment

Windows

python -m venv .venv
.venv\Scripts\activate

Linux / macOS

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

🔐 Environment Variables

Do not hard-code sensitive credentials inside the source code.

Create a .env file for local development and configure the requiredenvironment variables.

Example:

DATABASE_URL=your_database_connection_string
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

If additional Supabase or application-specific credentials are requiredby the backend, configure them through environment variables as well.

⚠️ Important

Never commit:

.env

or any file containing:

Database passwords

JWT secret keys

Supabase secret credentials

API keys

Other private credentials

Add them to .gitignore.

▶️ Run the Backend Locally

Start the FastAPI server using Uvicorn:

uvicorn main:app --reload

Depending on the project's entry-point location, the command may need tobe adjusted.

The local API will normally be available at:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs

▶️ Run the Frontend Locally

Start Streamlit:

streamlit run <frontend_entry_file>.py

The frontend will normally open at:

http://localhost:8501

Make sure the frontend's BASE_URL points to the correct backend.

For local development:

BASE_URL = "http://127.0.0.1:8000"

For the deployed application:

BASE_URL = "https://house-price-prediction-vsnv.onrender.com"

🐳 Running with Docker

Build the backend image:

docker build -t house-price-prediction .

Run the container:

docker run -p 8000:8000 house-price-prediction

The API can then be accessed through:

http://localhost:8000

Swagger:

http://localhost:8000/docs

🧪 Testing the Application

A complete test flow can be performed as follows:

1) Open the frontend
        ↓
2) Register a new account
        ↓
3) Login
        ↓
4) Open Profile
        ↓
5) Enter house information
        ↓
6) Generate prediction
        ↓
7) Check Prediction History
        ↓
8) Test Forgot Password
        ↓
9) Logout

The backend APIs can also be tested independently through Swagger UI.

📌 Error Handling

The frontend handles unsuccessful API responses without assuming thatevery backend response is JSON.

For example:

try:
    detail = response.json().get(
        "detail",
        "Request failed."
    )
except ValueError:
    detail = response.text or "Request failed."

This prevents the Streamlit application from crashing when an unexpectednon-JSON response is returned by the server.

🔒 Security Considerations

This project implements several security-oriented practices:

JWT-based authentication

Protected backend routes

Password hashing

Authorization headers for authenticated requests

Environment variables for sensitive configuration

User-specific prediction history

For a production system, additional security hardening should beconsidered, including HTTPS enforcement, secure cookie/sessionconfiguration where applicable, rate limiting, stronger passwordpolicies, secret rotation, input sanitization, logging, monitoring, andcomprehensive automated testing.

☁️ Deployment Architecture

The deployed application separates the frontend and backend:

                 Internet
                    │
                    ▼
       ┌─────────────────────────┐
       │ Streamlit Frontend      │
       │       Render            │
       └────────────┬────────────┘
                    │
                    │ HTTPS API Requests
                    ▼
       ┌─────────────────────────┐
       │ FastAPI Backend         │
       │       Render            │
       └────────────┬────────────┘
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
   ┌──────────────┐   ┌───────────────┐
   │ ML Model     │   │ Supabase      │
   │ Prediction   │   │ PostgreSQL    │
   └──────────────┘   └───────────────┘

This architecture keeps the user interface and API layer separated andallows each service to be deployed independently.

🎯 Project Goals

The primary goal of this project is not only to build a Machine Learningmodel, but to demonstrate the complete journey from:

Raw Data
   ↓
Machine Learning
   ↓
Model Serialization
   ↓
REST API
   ↓
Authentication
   ↓
Database
   ↓
Frontend
   ↓
Docker
   ↓
Cloud Deployment

This makes the project a practical example of an end-to-end DataScience / Machine Learning application.

📚 What This Project Demonstrates

Through this project, the following concepts are demonstrated:

1) Data preprocessing
2) Supervised Machine Learning
3) Model evaluation
4) Model deployment
5) REST API development
6) FastAPI
7) Pydantic validation
8) JWT authentication
9) OAuth2 authentication flow
10) Password hashing
11) PostgreSQL
12) Supabase
13) Streamlit
14) Docker
15) Git & GitHub
16) Cloud deployment
17) Frontend-backend communication
18) API error handling
19) Persistent prediction history

👨‍💻 Author

Souvik Banerjee
GitHub - https://github.com/Souvik1335
LinkedIn - linkedin.com/in/souvik-banerjee-71a406378
Built as an end-to-end Data Science / Machine Learning application witha focus on practical deployment and backend integration.

⭐ Project Status

Status: Completed & Deployed 🚀

The application currently includes:

✅ Machine Learning model
✅ FastAPI backend
✅ Streamlit frontend
✅ Supabase PostgreSQL database
✅ JWT authentication
✅ User registration
✅ Login
✅ Profile
✅ Password reset
✅ Prediction
✅ Prediction history
✅ Logout
✅ Docker
✅ Cloud deployment

🔗 Live Links

Frontend:- https://house-price-prediction-1-4we3.onrender.com

Backend:- https://house-price-prediction-vsnv.onrender.com

Swagger API Documentation:- https://house-price-prediction-vsnv.onrender.com/docs
