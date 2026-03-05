import numpy as np
from model_training import lr_model, scaler

def prediction(data_list):
    try:
        inputs = np.array(data_list).reshape(1, -1)
        inputs_scaled = scaler.transform(inputs)
        prob = lr_model.predict_proba(inputs_scaled)[0][1]
        return round(prob * 100, 2)
    
    except Exception as e:
        return f"error: {e}"


    