from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from src.model_training import lr_model, X_test, y_pred, y_test

def main():

    y_pred = lr_model.predict(X_test)

    print("Obtained Accuracy:", accuracy_score(y_pred, y_test))
    print("\nConfusion Matrix:\n", confusion_matrix(y_pred, y_test))
    print("\nOverall Model Report:\n", classification_report(y_pred, y_test))

if __name__ == "__main__":
    main()

