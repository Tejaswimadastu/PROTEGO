# 🛡️ PROTEGO

### AI-Powered Safety Monitoring, Risk Assessment & Crisis Support System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/FastAPI-Backend-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Machine-Learning-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/NLP-Natural%20Language%20Processing-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Supabase-Database-green?style=for-the-badge">
</p>

---

## 🌍 Project Vision

Millions of people experience emotional distress, fear, harassment, abuse, loneliness, and crisis situations every day. Many hesitate to seek help due to fear, stigma, lack of awareness, or limited access to support systems.

**PROTEGO** was developed to bridge this gap through Artificial Intelligence.

The system acts as an intelligent safety companion capable of understanding emotional signals from natural language, detecting potential risk situations, classifying severity levels, and providing immediate guidance and emergency resources when necessary.

Unlike traditional chatbots, PROTEGO combines:

* Machine Learning
* Natural Language Processing
* Safety Rule Engines
* Crisis Detection Logic
* Location Awareness
* Real-Time Risk Monitoring

to create a comprehensive AI-powered safety ecosystem.

---

# 🎯 Problem Statement

Many existing support platforms:

❌ Do not understand emotional context

❌ Cannot identify crisis situations

❌ Provide generic responses

❌ Lack emergency escalation mechanisms

❌ Do not support proactive safety monitoring

PROTEGO addresses these limitations by integrating intelligent risk assessment and contextual response generation.

---

# 🚀 Key Objectives

### 🧠 Emotion Understanding

Identify emotional states from user messages.

### 📊 Risk Classification

Determine severity level of user situations.

### 🚨 Crisis Detection

Recognize emergency and high-risk scenarios.

### 📞 Emergency Assistance

Provide country-specific emergency resources.

### 📍 Location Awareness

Track user locations (with permission) for monitoring and response support.

### 👨‍💼 Administrative Monitoring

Enable administrators to monitor trends, risks, and emergency cases.

### 💬 Human-Centered Conversations

Generate empathetic and supportive responses.

---

# 🏗️ System Overview

PROTEGO operates through multiple intelligent layers:

User Input
↓
NLP Preprocessing
↓
Feature Extraction
↓
Emotion Detection Model
↓
Sentiment Analysis Model
↓
Risk Classification Model
↓
Safety Rule Engine
↓
Response Generation Engine
↓
Emergency Assistance Layer
↓
User Interface

This layered architecture ensures both accuracy and safety.

---

# 🧠 Artificial Intelligence Components

## 1. Emotion Detection Engine

Classifies emotions such as:

* Fear
* Sadness
* Anger
* Neutral
* Distress

Purpose:

Understanding emotional state helps the system personalize support and determine appropriate response strategies.

---

## 2. Sentiment Analysis Engine

Classifies user sentiment into:

* Positive
* Neutral
* Negative

Purpose:

Provides additional emotional context for risk evaluation.

---

## 3. Risk Assessment Engine

Classifies situations into:

🟢 Low Risk

🟡 Medium Risk

🟠 High Risk

🔴 Emergency

Purpose:

Ensures appropriate intervention recommendations.

---

## 4. Safety Rule Engine

Machine Learning predictions are enhanced using deterministic safety rules.

Examples:

* Abuse indicators
* Violence-related keywords
* Threat detection
* Immediate danger situations
* Crisis escalation patterns

This prevents dangerous situations from being underestimated.

---

# 📊 Admin Intelligence Dashboard

The administrator dashboard provides:

### User Analytics

* Registered users
* Active users
* Risk distribution

### Crisis Monitoring

* High-risk users
* Emergency cases
* Escalation tracking

### Geolocation Monitoring

* User locations
* Risk hotspots
* Incident concentration zones

### Chat Analytics

* Conversation statistics
* Sentiment distribution
* Emotional trends

---

# 💡 Advanced Features

✅ Machine Learning Powered

✅ NLP-Based Understanding

✅ Real-Time Chatbot

✅ Emotion Detection

✅ Sentiment Analysis

✅ Risk Classification

✅ Emergency Escalation

✅ Emergency Contact Assistance

✅ Location Tracking

✅ Admin Dashboard

✅ User Authentication

✅ Chat History Storage

✅ Supabase Integration

✅ FastAPI Backend

✅ Responsive Frontend

---

# 🛠️ Technology Stack

## Backend

* Python
* FastAPI
* Uvicorn

## Machine Learning

* Scikit-Learn
* TF-IDF Vectorization
* LinearSVC
* Logistic Regression

## Natural Language Processing

* NLTK
* Lemmatization
* Stopword Removal
* Text Normalization

## Database

* Supabase PostgreSQL

## Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap

## Data Storage

* JSON Knowledge Base
* Trained ML Models (.pkl)

---

# 📂 Core Modules

### API Layer

Handles communication between frontend and ML services.

### NLP Layer

Responsible for preprocessing and feature engineering.

### Machine Learning Layer

Performs emotion, sentiment, and risk prediction.

### Safety Intelligence Layer

Applies rule-based safety validation.

### Response Engine

Generates empathetic and contextual responses.

### Emergency Support Layer

Provides emergency resources and crisis guidance.

### Monitoring Layer

Tracks users, locations, and system activity.

---

# 🔬 Innovation Highlights

PROTEGO is not simply a chatbot.

It represents a hybrid AI safety platform that combines:

* Predictive Intelligence
* Human-Centered Design
* Crisis Prevention
* Emergency Awareness
* Administrative Monitoring

into a unified system.

The project demonstrates how Machine Learning and NLP can be applied to create socially impactful technology capable of assisting individuals during emotionally vulnerable situations.

---

# 🎓 Academic Relevance

This project integrates concepts from:

* Machine Learning
* Natural Language Processing
* Artificial Intelligence
* Data Science
* Software Engineering
* Web Development
* Database Systems
* Human-Computer Interaction

making it suitable as a major academic project, research prototype, or portfolio project.

---

Add this section to your README after the **Installation** section.

---

# ▶️ Execution Guide

## 📋 Prerequisites

Before running PROTEGO, ensure the following software is installed:

### Required Software

* Python 3.11+ (Recommended: Python 3.13)
* Git
* Supabase Account
* Modern Web Browser (Chrome, Edge, Firefox)

Verify installation:

```bash
python --version
```

Expected:

```text
Python 3.13.x
```

---

# 📥 Clone Repository

```bash
git clone https://github.com/your-username/protego.git

cd protego
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is unavailable:

```bash
pip install fastapi uvicorn scikit-learn pandas nltk joblib supabase
```

---

# 📚 Download NLP Resources

PROTEGO uses NLTK resources for preprocessing.

Run once:

```bash
python -m nltk.downloader stopwords wordnet
```

---

# 🗄️ Configure Database

Create the following tables in Supabase:

### Users Table

```sql
create table users(
    id uuid primary key default gen_random_uuid(),
    name text,
    email text unique,
    password text,
    role text
);
```

### Chats Table

```sql
create table chats(
    id uuid primary key default gen_random_uuid(),
    user_id uuid references users(id),
    message text,
    response text,
    risk text,
    created_at timestamp default now()
);
```

### Locations Table

```sql
create table locations(
    id uuid primary key default gen_random_uuid(),
    user_id uuid references users(id),
    latitude float,
    longitude float,
    created_at timestamp default now()
);
```

---

# 🧠 Train Machine Learning Models

Generate model files before first execution.

### Train Emotion Model

```bash
python -m protego.train.train_emotion
```

### Train Sentiment Model

```bash
python -m protego.train.train_sentiment
```

### Train Risk Model

```bash
python -m protego.train.train_risk
```

Expected output:

```text
emotion_model.pkl
emotion_vectorizer.pkl

sentiment_model.pkl
sentiment_vectorizer.pkl

risk_model.pkl
risk_vectorizer.pkl
```

Generated inside:

```text
protego/models/
```

---

# 🚀 Run PROTEGO

From project root:

```bash
python -m uvicorn protego.api.main:app --reload
```

Expected:

```text
INFO: Uvicorn running on http://127.0.0.1:8000
✅ PROTEGO API started successfully
```

---

# 🌐 Access Application

### Login Page

```text
http://localhost:8000
```

### Signup Page

```text
http://localhost:8000/signup
```

### User Dashboard

```text
http://localhost:8000/user
```

### Admin Dashboard

```text
http://localhost:8000/admin
```

### API Documentation

```text
http://localhost:8000/docs
```

### ReDoc Documentation

```text
http://localhost:8000/redoc
```

---

# 🧪 Test API

Open:

```text
http://localhost:8000/docs
```

Navigate to:

```text
POST /chat
```

Example request:

```json
{
  "message": "I feel scared to go home tonight",
  "country": "India"
}
```

Example response:

```json
{
  "reply": "I’m concerned about your safety right now.",
  "risk_level": "high",
  "emotion": "fear",
  "sentiment": "negative",
  "show_emergency": true
}
```

---

# 👤 Test User Login

Insert a sample user:

```sql
insert into users(name,email,password,role)
values(
'Demo User',
'demo@gmail.com',
'1234',
'user'
);
```

Login:

```text
Email: demo@gmail.com
Password: 1234
```

---

# 👨‍💼 Test Admin Login

Insert admin:

```sql
insert into users(name,email,password,role)
values(
'Admin',
'admin@gmail.com',
'admin123',
'admin'
);
```

Login:

```text
Email: admin@gmail.com
Password: admin123
```

---

# 🔥 Full Execution Flow

```text
1. Clone Repository
        ↓
2. Install Dependencies
        ↓
3. Download NLTK Resources
        ↓
4. Configure Supabase Database
        ↓
5. Train ML Models
        ↓
6. Run FastAPI Server
        ↓
7. Open Login Page
        ↓
8. Login / Signup
        ↓
9. Chat with PROTEGO
        ↓
10. Monitor Activity via Admin Dashboard
```

---

# ✅ Successful Run Checklist

* [ ] Dependencies Installed
* [ ] NLTK Resources Downloaded
* [ ] Database Connected
* [ ] Models Trained
* [ ] FastAPI Running
* [ ] Login Working
* [ ] Signup Working
* [ ] Chatbot Responding
* [ ] Locations Stored
* [ ] Chats Stored
* [ ] Admin Dashboard Accessible
* [ ] Emergency Contacts Displayed
* [ ] Risk Classification Working

---

# 👨‍💻 Project Contributors

### Bandi Chandra Kanth

Machine Learning, NLP, Backend Development, System Design

### Tejaswi Madastu

Frontend Development, UI/UX Design, Testing & Integration

---

# 🌟 Future Scope

* Deep Learning Models
* Transformer-Based NLP
* Voice-Based Interaction
* Mobile Application
* SMS Emergency Alerts
* Email Notifications
* Real-Time Incident Reporting
* Multi-Language Support
* Predictive Crisis Forecasting
* AI Safety Analytics Platform

---

# 🏆 Conclusion

PROTEGO demonstrates the potential of Artificial Intelligence in building safer digital environments through intelligent emotional understanding, risk assessment, and crisis support.

By combining Machine Learning, NLP, Safety Intelligence, and Real-Time Monitoring, the system aims to provide meaningful assistance when users need support the most.

---

## © 2026 PROTEGO

**Developed by Bandi Chandra Kanth 

Tejaswi Madastu**
