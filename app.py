from fastapi import FastAPI
from pydantic import BaseModel
from emotion_detection import emotion_detector

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/analyze")
def analyze_text(input: TextInput):
    result = emotion_detector(input.text)
    return {"input": input.text, "emotions": result}
