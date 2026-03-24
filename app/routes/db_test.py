# app/routes/db_test.py

from fastapi import APIRouter
from app.db.supabase_client import supabase

# Create router
router = APIRouter()

@router.get("/db-test")
def test_db():
    """
    Test Supabase connection
    """
    try:
        # Simple query (even if table doesn't exist, connection works)
        response = supabase.table("test").select("*").limit(1).execute()
        return {
            "status": "Connected to Supabase",
            "data": response.data
        }
    except Exception as e:
        return {
            "status": "Connected but no table",
            "error": str(e)
        }