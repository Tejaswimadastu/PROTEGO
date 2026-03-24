# app/schemas/user_schema.py

from pydantic import BaseModel, EmailStr

# Signup
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Response
class UserResponse(BaseModel):
    id: str
    email: EmailStr