from prediction import prediction
from user_input import get_user_data

def get_result():
    raw_data = get_user_data() 
    
    proba = prediction(raw_data) 

    print(f"Based on your input the chances of having diabetes is {proba}%.")
    print("If you have doubts then please confirm from your doctor.")

if __name__ == "__main__":
    get_result()