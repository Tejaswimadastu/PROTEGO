# 🛡️ PROTEGO - AI-Powered Safety Monitoring & Crisis Support System

## 📌 Overview

PROTEGO is an AI-powered safety monitoring system designed to provide emotional support, risk assessment, and emergency guidance using Machine Learning, Natural Language Processing (NLP), and rule-based safety intelligence.

The system analyzes user messages, identifies emotional states, classifies risk levels, detects potential crisis situations, and provides appropriate guidance along with emergency contacts when required.

---

## 🚀 Key Features

### 🤖 AI Chat Assistant

* Real-time conversational interface
* Human-like empathetic responses
* Emotional support guidance
* Safety-focused interactions

### 🧠 Machine Learning Engine

* Emotion Classification
* Sentiment Analysis
* Risk Classification
* Safety Rule Enforcement

### 🚨 Crisis Detection

* Emergency keyword detection
* Self-harm indicator detection
* Physical abuse detection
* Escalation monitoring

### 📍 Location Tracking

* User location collection (with permission)
* Admin visibility of user locations
* Emergency monitoring support

### 👤 Authentication System

* User Signup
* User Login
* Session Management
* Role-based Access Control

### 📊 Admin Dashboard

* User Monitoring
* Chat Analytics
* Risk Distribution Charts
* Emergency Case Tracking
* Location Visualization

### 📞 Emergency Assistance

* Country-specific emergency contacts
* Women Helpline
* Police Assistance
* Mental Health Support
* Child Protection Services

---

# 🏗️ System Architecture

User
↓
Frontend (HTML + CSS + JavaScript)
↓
FastAPI Backend
↓
ML Models + Safety Rules
↓
Response Engine
↓
Supabase Database
↓
Admin Dashboard

---

# 🧠 Machine Learning Components

## Emotion Classification

Detects:

* Sadness
* Fear
* Anger
* Shame
* Neutral

Model:

* Linear Support Vector Machine (LinearSVC)
* TF-IDF Vectorization

---

## Sentiment Analysis

Detects:

* Positive
* Neutral
* Negative

Model:

* Logistic Regression
* TF-IDF Vectorization

---

## Risk Classification

Detects:

* Low Risk
* Medium Risk
* High Risk
* Emergency Risk

Model:

* LinearSVC
* Safety-Oriented Risk Weights

---

# 🛡️ Safety Rule Engine

Deterministic safety overrides ensure that dangerous situations are never ignored.

Rules include:

* Emergency keyword detection
* Physical abuse detection
* Repeated high-risk escalation
* Emergency persistence tracking
* Risk trend analysis

---

# 📂 Project Structure

PROTEGO/

├── protego/

│ ├── api/

│ │ ├── main.py

│ │ ├── chatbot_service.py

│ │ └── schemas.py

│

│ ├── nlp/

│ │ ├── preprocess.py

│ │ ├── features.py

│ │ └── keywords.py

│

│ ├── logic/

│ │ ├── response_engine.py

│ │ ├── safety_rules.py

│ │ ├── risk_scoring.py

│ │ └── context_memory.py

│

│ ├── frontend/

│ │ ├── index.html

│ │ ├── login.html

│ │ ├── signup.html

│ │ └── admin.html

│

│ ├── train/

│ │ ├── train_emotion.py

│ │ ├── train_sentiment.py

│ │ └── train_risk.py

│

│ ├── models/

│ │ ├── emotion_model.pkl

│ │ ├── sentiment_model.pkl

│ │ └── risk_model.pkl

│

│ └── knowledge/

│ ├── guidance_templates.json

│ ├── emergency_contacts.json

│ └── keyword_responses.json

---

# 💾 Database Design

## Users Table

| Column   | Type |
| -------- | ---- |
| id       | UUID |
| name     | Text |
| email    | Text |
| password | Text |
| role     | Text |

---

## Chats Table

| Column   | Type |
| -------- | ---- |
| id       | UUID |
| user_id  | UUID |
| message  | Text |
| response | Text |
| risk     | Text |

---

## Locations Table

| Column     | Type      |
| ---------- | --------- |
| id         | UUID      |
| user_id    | UUID      |
| latitude   | Float     |
| longitude  | Float     |
| created_at | Timestamp |

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/protego.git
cd protego
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Download NLTK Resources

```bash
python -m nltk.downloader stopwords wordnet
```

---

# 🎯 Train Models

## Emotion Model

```bash
python -m protego.train.train_emotion
```

## Sentiment Model

```bash
python -m protego.train.train_sentiment
```

## Risk Model

```bash
python -m protego.train.train_risk
```

---

# ▶️ Run Application

```bash
python -m uvicorn protego.api.main:app --reload
```

Application:

```text
http://localhost:8000
```

API Docs:

```text
http://localhost:8000/docs
```

---

# 📡 API Endpoints

## Chat

POST

```text
/chat
```

Example:

```json
{
  "message": "I feel scared to go home tonight",
  "country": "India"
}
```

Response:

```json
{
  "reply": "I’m concerned about your safety.",
  "risk_level": "high",
  "emotion": "fear",
  "sentiment": "negative"
}
```

---

# 🔒 Security Features

* Input Validation
* Rule-Based Safety Overrides
* Crisis Detection
* Risk Escalation Monitoring
* Emergency Contact Routing

---

# 🎓 Academic Concepts Used

* Machine Learning
* Natural Language Processing
* Text Classification
* Feature Engineering
* Sentiment Analysis
* Risk Assessment
* FastAPI Development
* Database Management
* Frontend Integration

---

# 🌟 Future Enhancements

* Deep Learning Models
* Transformer-Based NLP
* Real-Time Notifications
* SMS Alerts
* Email Alerts
* Mobile Application
* Multi-Language Support
* Live Emergency Dispatch System

---

# 👨‍💻 Developed By
Madastu Tejaswi(23B81A05EA)


Bandi Chandra Kanth(23B81A05CE)

PROTEGO – AI-Powered Safety Monitoring System

2026
