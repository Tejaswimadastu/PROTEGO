# app/routes/protected.py

from fastapi import APIRouter, Depends
from app.core.security import get_current_user

router = APIRouter()

@router.get("/protected")
def protected_route(current_user: dict = Depends(get_current_user)):
    """
    Protected route (only logged-in users)
    """
    return {
        "message": "You are authorized",
        "user": current_user
    }