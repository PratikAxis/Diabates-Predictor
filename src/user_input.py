def get_user_data():
    keys = [
        'gender',          
        'age', 
        'currentSmoker',   
        'cigsPerDay', 
        'BPMeds',          
        'prevalentStroke', 
        'prevalentHyp', 
        'totChol', 
        'sysBP', 
        'diaBP', 
        'BMI', 
        'heartRate', 
        'glucose', 
        'TenYearCHD'       
    ]
    
    user_values = []
    print("\n--- Please enter the following health details ---")
    for k in keys:
        val = input(f"{k}: ")
        user_values.append(float(val))
    
    return user_values

