# 🚀 AI-Powered SaaS Support API

![Python](https://img.shields.io/badge/Python-3.14-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![JWT](https://img.shields.io/badge/JWT-Authentication-orange)
![Groq AI](https://img.shields.io/badge/Groq-LLM-purple)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED)
![Render](https://img.shields.io/badge/Render-Deployed-success)

## 📖 Overview

AI-Powered SaaS Support API is a production-ready backend application built with **FastAPI** that enables secure user authentication, role-based ticket management, and intelligent AI-assisted ticket triaging.

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
