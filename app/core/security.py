import os
from datetime import datetime, timedelta

import jwt
from dotenv import load_dotenv
from passlib.context import CryptContext

# Load Environment variables from the .env file
load_dotenv()

#Password hashing Configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT Configuration
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Verify a plain password against its hashed version
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Generate a hashed password for storing in the database
def get_password_hash(password):
    return pwd_context.hash(password)

# Generate a JWT access token
def create_access_token(data: dict, expires_delta: timedelta |None=None):
    #Create a copy of payload
    to_encode=data.copy()

    # Set token expiration time
    expire = datetime.utcnow()+(
        expires_delta
        if expires_delta
        else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    # Add expiration time to the payload
    to_encode.update({"exp":expire})

    # Create and sign the JWT
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt