# 🚀 AI-Powered SaaS Ticketing API

![Python](https://img.shields.io/badge/Python-3.14-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![JWT](https://img.shields.io/badge/JWT-Authentication-orange)
![Groq AI](https://img.shields.io/badge/Groq-LLM-purple)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED)
![Render](https://img.shields.io/badge/Render-Deployed-success)

> Production-ready AI-powered SaaS backend built with FastAPI, PostgreSQL, JWT Authentication, Background Tasks, and Groq LLM integration.

## 📖 Overview

AI-Powered SaaS Support API is a production-ready backend application built with **FastAPI** that enables secure user authentication, role-based ticket management, and intelligent AI-powered ticket triage.
When a user creates a support ticket, the API instantly stores it in PostgreSQL and returns a response without delay. In the background, an AI service powered by **Groq's Llama 3.1** analyzes the ticket, automatically predicts its category and priority, and updates the database asynchronously using FastAPI Background Tasks.

The project demonstrates modern backend engineering practices including secure JWT authentication, SQLAlchemy ORM, asynchronous programming, Docker-based development, cloud deployment on Render, and AI integration through external APIs.

---

## 🌐 Live Project

**Live API**

`https://saas-ticketing-api.onrender.com`

**Interactive API Documentation**

`https://saas-ticketing-api.onrender.com/docs`

**GitHub Repository**

`https://github.com/sanjaykumarmugada18/saas-ticketing-api.git`

## 📸 API Preview

The application exposes an interactive Swagger UI for exploring and testing all available REST API endpoints.

![Swagger UI](docs/swagger-preview.png)

## ✨ Features

### Authentication & Authorization

- Email-based user registration
- JWT authentication
- Secure password hashing with bcrypt
- Role-based access control (Customer, Agent, Admin)
- Protected API endpoints using FastAPI dependency injection

### Ticket Management

- Create support tickets
- View customer-specific tickets
- Agent and administrator access to all tickets
- Update ticket status
- Automatic timestamp generation
- Multi-tenant data isolation

### AI Ticket Processing

- Automatic ticket categorization
- Automatic priority prediction
- Asynchronous AI processing using FastAPI Background Tasks
- Groq Llama 3.1 integration
- Structured JSON responses from the LLM
- Prompt injection mitigation through system prompts
- Graceful fallback handling when AI services are unavailable

### Production Ready

- PostgreSQL database
- SQLAlchemy ORM
- Docker-based local development
- Environment variable configuration
- CORS middleware
- Health check endpoint
- Cloud deployment on Render
- Production-ready project structure

---

# 🏗️ System Architecture

The application follows a layered backend architecture that separates responsibilities into independent modules, making the project scalable, maintainable, and easy to extend.

```
                    Client
                       │
                       ▼
              FastAPI REST API
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
 Authentication                 Ticket Routes
        │                             │
        └──────────────┬──────────────┘
                       ▼
                Business Logic
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
        AI Service              Database Layer
     (Groq Llama 3.1)          (SQLAlchemy ORM)
        │                             │
        └──────────────┬──────────────┘
                       ▼
                  PostgreSQL
```

### Request Flow

1. A user authenticates using JWT.
2. The client sends an authenticated API request.
3. FastAPI validates the request and permissions.
4. SQLAlchemy performs the required database operations.
5. For ticket creation, a FastAPI Background Task asynchronously invokes the AI service.
6. Groq Llama 3.1 analyzes the ticket and returns a structured JSON response.
7. The background worker updates the ticket category and priority.
8. The API responds without waiting for the AI, ensuring low response latency.

---

# 📁 Project Structure

```text
saas-ticketing-api/
│
├── app/
│   ├── api/
│   │   ├── auth.py
│   │   ├── tickets.py
│   │   └── users.py
│   │
│   ├── core/
│   │   └── security.py
│   │
│   ├── db/
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── ticket.py
│   │   └── user.py
│   │
│   ├── schemas/
│   │   ├── ticket.py
│   │   └── user.py
│   │
│   ├── services/
│   │   └── ai_service.py
│   │
│   └── main.py
│
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

### Directory Overview

| Directory | Purpose |
|------------|---------|
| `api/` | FastAPI route definitions and HTTP endpoints |
| `core/` | Authentication, security, and reusable core utilities |
| `db/` | Database configuration and SQLAlchemy session management |
| `models/` | SQLAlchemy ORM models representing database tables |
| `schemas/` | Pydantic models for request and response validation |
| `services/` | Business services including AI ticket analysis |
| `main.py` | FastAPI application entry point |

---

# 🛠️ Technology Stack

| Category              | Technologies             |
| --------------------- | ------------------------ |
| Language              | Python 3.14              |
| Backend Framework     | FastAPI                  |
| Database              | PostgreSQL               |
| ORM                   | SQLAlchemy               |
| Data Validation       | Pydantic                 |
| Authentication        | JWT (JSON Web Tokens)    |
| Password Security     | bcrypt + Passlib         |
| AI Integration        | Groq API (Llama 3.1)     |
| Async HTTP Client     | httpx                    |
| Background Processing | FastAPI Background Tasks |
| Containerization      | Docker & Docker Compose  |
| Deployment            | Render                   |

---

# ⚙️ Getting Started

## Prerequisites

* Python 3.12 or later
* Docker Desktop
* PostgreSQL (via Docker)
* Groq API Key

## Clone the Repository

```bash
git clone https://github.com/sanjaykumarmugada18/saas-ticketing-api.git

cd saas-ticketing-api
```

## Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start PostgreSQL

```bash
docker compose up -d
```

## Run the API

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

to access the interactive Swagger UI.

---

# 🔐 Environment Variables

Create a .env file using the following template:

```env
DATABASE_URL=postgresql://username:password@localhost/database_name

SECRET_KEY=your_secret_key

GROQ_API_KEY=your_groq_api_key
```

---

# 📡 API Endpoints

| Method | Endpoint               | Description                             |
| ------ | ---------------------- | --------------------------------------- |
| POST   | `/users/register`      | Register a new user                     |
| POST   | `/auth/login`          | Authenticate user and generate JWT      |
| POST   | `/tickets`             | Create a support ticket                 |
| GET    | `/tickets`             | Retrieve tickets                        |
| PATCH  | `/tickets/{ticket_id}` | Update ticket status (Agent/Admin only) |

---

# 🧪 AI Processing Workflow

```
User submits a support ticket
            │
            ▼
Ticket stored in PostgreSQL
            │
            ▼
201 Created returned immediately
            │
            ▼
FastAPI Background Task starts
            │
            ▼
Groq Llama 3.1 analyzes the ticket
            │
            ▼
Returns structured JSON
            │
            ▼
Database updated with

• Category
• Priority
```

---

## 🚀 Deployment

The application is deployed on **Render** using:

- Render Web Service
- Managed PostgreSQL Database
- Environment Variables
- Automatic GitHub Deployments
- Health Check Endpoint
- CORS Middleware

### Live API

https://saas-ticketing-api.onrender.com

### Swagger UI

https://saas-ticketing-api.onrender.com/docs

---

# 🔮 Future Improvements

Planned enhancements include:

* Email notifications
* File attachment support
* Admin dashboard
* Ticket search and filtering
* Redis + Celery task queue
* WebSocket-based live ticket updates
* Comprehensive automated testing
* CI/CD with GitHub Actions
* Monitoring and logging
* Rate limiting

---

# 👨‍💻 Author

**Sanjay**

Computer Science Engineering Student

GitHub

https://github.com/sanjaykumarmugada18

---

# ⭐ Acknowledgements

This project was built to explore modern backend engineering practices including secure authentication, asynchronous programming, AI integration, cloud deployment, and scalable API design using FastAPI.
