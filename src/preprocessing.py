import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# ----- Preprocessing -----
df = pd.read_csv("dataset/framingham.csv")
print(df.columns)
print(df.shape)

df = df.drop(['education'], axis=1)
print(df.isnull().sum())

# Fill missing values with column means
df['cigsPerDay'] = df['cigsPerDay'].fillna(np.mean(df['cigsPerDay']))
df['BPMeds'] = df['BPMeds'].fillna(np.mean(df['BPMeds']))
df['totChol'] = df['totChol'].fillna(np.mean(df['totChol']))
df['BMI'] = df['BMI'].fillna(np.mean(df['BMI']))
df['glucose'] = df['glucose'].fillna(np.mean(df['glucose']))
df['heartRate'] = df['heartRate'].fillna(np.mean(df['heartRate']))

print(df.isnull().sum())

# Remove extreme cholesterol values
df = df[df['totChol'] < 450]

X = df.drop(['diabetes'], axis=1)
y = df['diabetes']

# ----- Visualization -----

plt.xlabel('Independent variable')
plt.ylabel('Dependent variable')
for col in X.columns:
    plt.scatter(df[col], y, label=col)
plt.legend()
plt.show()

plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation between Medical Factors")
plt.show()

plt.boxplot(df)
plt.show()

