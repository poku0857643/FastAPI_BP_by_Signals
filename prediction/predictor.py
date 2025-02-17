import numpy as np
from typing import Tuple

def predict_bp(ecg:list[float], ppg:list[float]) -> Tuple[float, float, str]:
    sbp = np.mean(ecg) * 120
    dbp = np.mean(ppg) * 80

    if sbp > 140 or dbp > 90:
        desc = "Hypertension detected. Remember consult a doctor."
    elif sbp < 90 or dbp < 50:
        desc = "Hypotension detected. Remember consult a doctor."
    else:
        desc = "Blood pressure is within normal range."

    print(sbp, dbp, desc)
    return round(sbp, 2), round(dbp, 2), desc


