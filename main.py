from fastapi import FastAPI, HTTPException, status
from models.model import BPOutput, SignalInput
from prediction.predictor import inference_bp
import json
import joblib
from utils.utils import read_config_file

app = FastAPI(title="Predicting your blood pressure")

config_path = "./config/configs.yaml"
config = read_config_file(config_path)

if config:
    print("Configuration loaded successfully.")

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/predict", response_model=BPOutput)
async def predict_bp_endpoint(signals:SignalInput):
    try:
        sbp_list = signals.sbp
        dbp_list = signals.dbp

        if not sbp_list or not dbp_list:
            raise ValueError("data not loaded, please valid the data.")

        sbp_predict_model = config["model"]["sbp_model_path"]
        dbp_predict_model = config["model"]["dbp_model_path"]
        loaded_sbp_model = joblib.load(sbp_predict_model)
        loaded_dbp_model = joblib.load(dbp_predict_model)

        if not sbp_predict_model or not dbp_predict_model:
            raise ValueError("model not loaded, please valid the model.")

        sbp, dbp, description = inference_bp(sbp_list, dbp_list, loaded_sbp_model, loaded_dbp_model)
        return BPOutput(sbp=sbp, dbp=dbp, description=description)

    except Exception as e:  # Catch any exception
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Prediction error: {str(e)}")

@app.get("/")
def root():
    return {"message": "Blood Pressure Prediction API is running"}