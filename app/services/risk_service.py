# app/services/risk_service.py

def calculate_risk(emotion: str, sentiment: str, text: str):
    """
    Convert AI output into risk level
    """

    text_lower = text.lower()

    # 🚨 Emergency keywords
    emergency_keywords = [
        "kill", "suicide", "help me", "danger", "hurt me", "die"
    ]

    # Check emergency
    for word in emergency_keywords:
        if word in text_lower:
            return "EMERGENCY"

    # High risk
    if emotion in ["fear", "anger"] and sentiment == "NEGATIVE":
        return "HIGH"

    # Medium risk
    if emotion in ["sadness"] and sentiment == "NEGATIVE":
        return "MEDIUM"

    # Default
    return "LOW"