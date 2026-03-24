# app/schemas/nlp_schema.py

from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str