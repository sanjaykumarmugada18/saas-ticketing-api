from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db.database import engine, Base, get_db
from app.api import users
from app.api import auth
from app.models import ticket

Base.metadata.create_all(bind=engine)

app=FastAPI(title="Saas Support API")

app.include_router(users.router)
app.include_router(auth.router)

@app.get("/health")
async def health_check():
    return {"status":"ok","message":"System operational"}

@app.get("/db-test")
async def teat_db(db: Session = Depends(get_db)):
    return {"status": "ok","message": "Database connected!"}