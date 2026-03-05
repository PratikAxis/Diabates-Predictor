# src/model_evaluation.py
from model_training import lr_model, scaler, X_test, y_test
from sklearn.metrics import classification_report, accuracy_score

def evaluation():
    X_test_scaled = scaler.transform(X_test)
    
    y_pred = lr_model.predict(X_test_scaled)

    print("Obtained Accuracy:", accuracy_score(y_test, y_pred))
    print("\nOverall Model Report:\n", classification_report(y_test, y_pred))

if __name__ == "__main__":
    evaluation()

