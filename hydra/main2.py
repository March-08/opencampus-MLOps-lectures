# train.py
import hydra
from omegaconf import DictConfig
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def preprocess_data(X, y, cfg):
    # Perform scaling
    if cfg.preprocessing.scaling:
        scaler = StandardScaler()
        X = scaler.fit_transform(X)

    # Perform feature selection
    if cfg.preprocessing.feature_selection.enabled:
        if cfg.preprocessing.feature_selection.method == "variance_threshold":
            selector = VarianceThreshold(
                threshold=cfg.preprocessing.feature_selection.threshold
            )
            X = selector.fit_transform(X)

    return X, y


def evaluate_model(y_true, y_pred, metrics):
    results = {}
    for metric in metrics:
        if metric == "accuracy":
            results[metric] = accuracy_score(y_true, y_pred)
        elif metric == "precision":
            results[metric] = precision_score(y_true, y_pred, average="macro")
        elif metric == "recall":
            results[metric] = recall_score(y_true, y_pred, average="macro")
        elif metric == "f1":
            results[metric] = f1_score(y_true, y_pred, average="macro")
    return results


@hydra.main(config_path="conf", config_name="conf2.yaml")
def train(cfg: DictConfig) -> None:
    # Load dataset
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=cfg.data.test_size, random_state=42
    )

    # Preprocess data
    X_train, y_train = preprocess_data(X_train, y_train, cfg)
    X_test, y_test = preprocess_data(X_test, y_test, cfg)

    # Initialize model
    model = RandomForestClassifier(**cfg.model.hyperparameters)

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate model
    evaluation_results = evaluate_model(y_test, y_pred, cfg.evaluation.metrics)
    print("Evaluation results:")
    print(evaluation_results)

    # Log metrics using Hydra


if __name__ == "__main__":
    train()
