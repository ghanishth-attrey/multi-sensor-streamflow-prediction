from src.preprocessing import load_datasets, merge_datasets
from src.feature_engineering import engineer_features
from src.models import split_data, train_random_forest
from src.evaluation import evaluate_model
from src.fusion import early_fusion
from src.config import DATA_PATH, FEATURE_COLUMNS, TARGET_COLUMN


def run_pipeline():
    # Load
    sat, ground, flow = load_datasets(DATA_PATH)

    # Merge
    df = merge_datasets(sat, ground, flow)

    # Feature Engineering
    df = engineer_features(df)

    # Early Fusion
    X = early_fusion(df, FEATURE_COLUMNS)
    y = df[TARGET_COLUMN]

    # Split
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Train
    model = train_random_forest(X_train, y_train)

    # Predict
    preds = model.predict(X_test)

    # Evaluate
    metrics = evaluate_model(y_test, preds)

    print("Model Performance:")
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")


if __name__ == "__main__":
    run_pipeline()
