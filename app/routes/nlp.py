# app/routes/nlp.py

from fastapi import APIRouter, Depends
from app.schemas.nlp_schema import TextRequest
from app.services.nlp_service import analyze_text
from app.services.risk_service import calculate_risk
from app.services.response_service import generate_response
from app.core.security import get_current_user

router = APIRouter()

@router.post("/analyze")
def analyze(request: TextRequest, current_user: dict = Depends(get_current_user)):
    """
    Full pipeline: NLP → Risk → Response
    """

    # Step 1: NLP
    result = analyze_text(request.text)

    # Step 2: Risk
    risk = calculate_risk(
        emotion=result["emotion"],
        sentiment=result["sentiment"],
        text=request.text
    )

    # Step 3: Response
    response = generate_response(risk)

    return {
        "user": current_user,
        "analysis": result,
        "risk_level": risk,
        "response": response
    }