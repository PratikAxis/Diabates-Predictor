def get_user_data():
    keys = ['age', 'currentSmoker', 'cigsPerDay', 'BPMeds', 'prevalentStroke', 
            'prevalentHyp', 'diabetes', 'totChol', 'sysBP', 'diaBP', 
            'BMI', 'heartRate', 'glucose']
    
    return [float(input(f"{k}: ")) for k in keys]