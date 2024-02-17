# model/train_model.py
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib


def train_model():
    # Load iris dataset
    data = load_iris()
    X, y = data.data, data.target

    # Train a RandomForestClassifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Save the trained model
    joblib.dump(model, "trained_model.joblib")


if __name__ == "__main__":
    train_model()
