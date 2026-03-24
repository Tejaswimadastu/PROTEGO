# app/routes/auth.py

from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserCreate, UserLogin
from app.services.auth_service import create_user, authenticate_user
from app.core.security import create_access_token

router = APIRouter()

# SIGNUP
@router.post("/signup")
def signup(user: UserCreate):
    try:
        result = create_user(user.email, user.password)

        return {
            "message": "User created successfully",
            "user": result
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# LOGIN
@router.post("/login")
def login(user: UserLogin):
    db_user = authenticate_user(user.email, user.password)

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Create token
    token = create_access_token({
        "sub": db_user["email"]
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }