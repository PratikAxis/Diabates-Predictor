import matplotlib.pyplot as plt
import seaborn as sns
from preprocessing import df, X, y

def visualization():

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

if __name__ == "__main__":
    visualization()



