from fastapi import FastAPI, HTTPException, status
from models.model import BPOutput, SignalInput
from prediction.predictor import predict_bp
import json

app = FastAPI(title="Predicting your blood pressure")

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/predict", response_model=BPOutput)
async def predict_bp_endpoint(signals:SignalInput):
    try:
        ecg_list = signals.ecg
        ppg_list = signals.ppg

        sbp, dbp, description = predict_bp(ecg_list, ppg_list)
        return BPOutput(sbp=sbp, dbp=dbp, description=description)

    except Exception as e:  # Catch any exception
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Prediction error: {str(e)}")

@app.get("/")
def root():
    return {"message": "Blood Pressure Prediction API is running"}