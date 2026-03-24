# app/main.py

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from app.routes.health import router as health_router
from app.routes.db_test import router as db_router
from app.routes.auth import router as auth_router
from app.routes.protected import router as protected_router
from app.routes.nlp import router as nlp_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(db_router)
app.include_router(auth_router)
app.include_router(protected_router)
app.include_router(nlp_router)

# ✅ FIXED PATH (IMPORTANT)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@app.get("/", response_class=HTMLResponse)
def home():
    file_path = os.path.join(BASE_DIR, "templates", "index.html")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()