# app/services/response_service.py

def generate_response(risk_level: str):
    """
    Generate response based on risk level
    """

    if risk_level == "LOW":
        return {
            "message": "Everything seems okay 😊",
            "action": "No action needed"
        }

    elif risk_level == "MEDIUM":
        return {
            "message": "I’m here for you. You’re not alone 💙",
            "action": "Consider talking to someone you trust"
        }

    elif risk_level == "HIGH":
        return {
            "message": "This seems serious. Please seek help immediately ⚠️",
            "action": "Contact a trusted person or helpline"
        }

    elif risk_level == "EMERGENCY":
        return {
            "message": "🚨 URGENT: You are not safe. Get immediate help!",
            "action": "Call emergency services or helpline NOW"
        }

    return {
        "message": "Unable to determine response",
        "action": "Try again"
    }