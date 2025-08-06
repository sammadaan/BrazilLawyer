from pydantic import BaseModel
from typing import List

class TextRequest(BaseModel):
    text: str

class TextResponse(BaseModel):
    text: str

class NLPResponse(BaseModel):
    entities: List[str]
    lemmas: List[str]