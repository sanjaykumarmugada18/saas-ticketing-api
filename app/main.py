from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import engine, Base
from app.api import users, auth, tickets

# Ensure database tables exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SaaS Support API")

# CORS configuration
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://my-saas-frontend.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check route
@app.get("/", tags=["Health Check"])
def health_check():
    return {"status": "ok", "message": "API is running securely in production"}

# Routers
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(tickets.router)