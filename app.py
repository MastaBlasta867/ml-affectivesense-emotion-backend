from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import base64
from io import BytesIO
from PIL import Image
import numpy as np
import cv2
from emotion_detection import predict_emotion

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ImagePayload(BaseModel):
    image: str

@app.post("/predict")
async def predict(payload: ImagePayload):
    image_data = payload.image.split(",")[1]
    decoded = base64.b64decode(image_data)
    img = Image.open(BytesIO(decoded)).convert("RGB")
    img = np.array(img)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    emotion, confidence = predict_emotion(gray)

    return {
        "emotion": emotion,
        "confidence": confidence
    }
