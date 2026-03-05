import pandas as pd

def preprocessing():
    csv_path = '/home/pratik/ML and DL projects/Diabetes predictor/Data/raw.csv'
    
    df = pd.read_csv(csv_path)
    df = df.drop(['education'], axis=1)

    for col in ['cigsPerDay', 'BPMeds', 'totChol', 'BMI', 'glucose', 'heartRate']:
        df[col] = df[col].fillna(df[col].mean())

    df = df[df['totChol'] < 450]

    X = df.drop(['diabetes'], axis=1)
    y = df['diabetes']
    return df, X, y