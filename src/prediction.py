import numpy as np
from src.model_training import lr_model
from src.user_input import get_user_data


def prediction(data_list):
    try:
        inputs = np.array(data_list).reshape(1, -1)
        prob = lr_model.predict_proba(inputs)[0][1]
        return prob
    except Exception as e:
        return f"error: {e}"


raw_data = get_user_data()
final_risk = prediction(raw_data)


    