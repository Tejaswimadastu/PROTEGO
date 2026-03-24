# app/services/auth_service.py

from app.db.supabase_client import supabase
from app.core.security import hash_password, verify_password

# CREATE USER (with hashing)
def create_user(email: str, password: str):
    hashed_password = hash_password(password)

    response = supabase.table("users").insert({
        "email": email,
        "password": hashed_password
    }).execute()

    return response.data


# GET USER BY EMAIL
def get_user_by_email(email: str):
    response = supabase.table("users").select("*").eq("email", email).execute()

    return response.data


# VERIFY LOGIN
def authenticate_user(email: str, password: str):
    users = get_user_by_email(email)

    if not users:
        return None

    user = users[0]

    if not verify_password(password, user["password"]):
        return None

    return user