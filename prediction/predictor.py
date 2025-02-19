import numpy as np
from typing import Tuple
import joblib
from sklearn.linear_model import LinearRegression

def inference_bp(user_dbp:list[float], user_sbp:list[float],loaded_dbp_model, loaded_sbp_model) -> Tuple[float, float, str]:
    user_dbp = list(map(float, user_dbp))
    user_sbp = list(map(float, user_sbp))
    processed_last_5_dbp = np.array(user_dbp[-5:]).reshape(1, -1)
    processed_last_5_sbp = np.array(user_sbp[-5:]).reshape(1, -1)
    dbp_model = loaded_dbp_model
    sbp_model = loaded_sbp_model

    if not loaded_dbp_model or not loaded_sbp_model:
        raise ValueError("model not loaded, please valid the model.")
    output_dbp = dbp_model.predict(processed_last_5_dbp)
    output_sbp = sbp_model.predict(processed_last_5_sbp)
    # return f"{output_dbp[0]:.2f}, {output_sbp[0]:.2f}"

    if output_sbp > 140 or output_dbp > 90:
        desc = "Hypertension detected. Remember consult a doctor."
    elif output_sbp < 90 or output_dbp < 50:
        desc = "Hypotension detected. Remember consult a doctor."
    else:
        desc = "Blood pressure is within normal range."

    # print(sbp, dbp, desc)
    return round(output_sbp, 2), round(output_dbp, 2), desc



# inference_dbp(user_dbp_data, user_sbp_data,loaded_dbp_model=dbp_model, loaded_sbp_model=sbp_model)