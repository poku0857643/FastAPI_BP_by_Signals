from pydantic import BaseModel
from typing import Tuple
from sklearn.linear_model import LinearRegression


class SignalInput(BaseModel):
    ecg: list
    ppg:list

class BPOutput(BaseModel):
    sbp: float
    dbp: float
    description: str

class LinearModel(LinearRegression):

