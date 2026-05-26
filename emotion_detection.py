import numpy as np
import cv2
from tensorflow.keras.models import load_model

# Load the model WITHOUT compiling (fixes old Keras optimizer issues)
model = load_model("emotion_model.h5", compile=False)

EMOTIONS = ["angry", "disgust", "fear", "happy", "sad", "surprise", "neutral"]

def predict_emotion(gray_face):
    face = cv2.resize(gray_face, (64, 64))
    face = face.astype("float32") / 255.0
    face = np.expand_dims(face, axis=-1)
    face = np.expand_dims(face, axis=0)

    preds = model.predict(face)[0]
    emotion = EMOTIONS[np.argmax(preds)]
    confidence = float(np.max(preds))
    return emotion, confidence
