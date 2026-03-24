# app/routes/health.py

from fastapi import APIRouter

# Create router object
router = APIRouter()

@router.get("/health")
def health_check():
    """
    Health check endpoint
    Used to verify API is working
    """
    return {"status": "OK", "message": "Protego API is healthy"}