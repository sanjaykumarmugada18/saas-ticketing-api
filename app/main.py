from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db.database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app=FastAPI(title="Saas Support API")

@app.get("/health")
async def health_check():
    return {"status":"ok","message":"System operational"}

@app.get("/db-test")
async def teat_db(db: Session = Depends(get_db)):
    return {"status": "ok","message": "Database connected!"}