from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
try:
    model = joblib.load("msa_text_classifier.joblib")
except FileNotFoundError:
    model = None
    print("Model file not found. Please ensure 'msa_text_classifier.joblib' exists.")
except Exception as e:
    model = None
    print(f"Error loading model: {e}")

class TextRequest(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    label: str

@app.post("/predict", response_model=PredictionResponse)
def predict(req: TextRequest):
    if model is None:
        return PredictionResponse(label="Model not available")
    pred = model.predict([req.text])[0]
    return PredictionResponse(label=pred)