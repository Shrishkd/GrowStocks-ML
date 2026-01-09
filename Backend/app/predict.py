import pandas as pd
import joblib
from pathlib import Path

# Base directory: backend/
BASE_DIR = Path(__file__).resolve().parent.parent

# Decision threshold
BUY_THRESHOLD = 0.6

# Supported stocks mapping
SUPPORTED_STOCKS = {
    "RELIANCE": "reliance",
    "TCS": "tcs",
    "ICICIBANK": "icicibank",
    "INFY": "infy",
    "HDFCBANK": "hdfcbank"
}

# Feature list (must match training exactly)
FEATURES = [
    "return",
    "sma_20",
    "sma_50",
    "rsi",
    "volatility",
    "nifty_return",
    "nifty_volatility",
    "banknifty_return"
]


def _get_paths(stock: str):
    """
    Resolve model and dataset paths for a given stock.
    """
    stock = stock.upper()

    if stock not in SUPPORTED_STOCKS:
        raise ValueError(
            f"Unsupported stock '{stock}'. "
            f"Supported stocks: {list(SUPPORTED_STOCKS.keys())}"
        )

    name = SUPPORTED_STOCKS[stock]

    model_path = BASE_DIR / "models" / f"rf_{name}.pkl"
    data_path = BASE_DIR / "data" / f"{name}_ml_dataset.csv"

    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found: {model_path}")

    if not data_path.exists():
        raise FileNotFoundError(f"Dataset file not found: {data_path}")

    return model_path, data_path


def predict_buy_signal(stock: str):
    """
    Predict BUY / DO NOT BUY decision for a given stock.
    """

    # Resolve paths
    model_path, data_path = _get_paths(stock)

    # Load ML dataset
    df = pd.read_csv(
        data_path,
        index_col=0,
        parse_dates=True
    )

    # Safety check
    missing_features = [f for f in FEATURES if f not in df.columns]
    if missing_features:
        raise ValueError(f"Missing features in dataset: {missing_features}")

    # Use latest available row
    latest = df.iloc[-1]

    X_latest = latest[FEATURES].values.reshape(1, -1)

    # Load trained model
    model = joblib.load(model_path)

    # Predict probability
    prob_buy = float(model.predict_proba(X_latest)[0][1])

    # Decision logic
    decision = "BUY" if prob_buy >= BUY_THRESHOLD else "DO NOT BUY"

    # Confidence label
    if prob_buy >= 0.7:
        confidence = "High"
    elif prob_buy >= BUY_THRESHOLD:
        confidence = "Medium"
    else:
        confidence = "Low"

    return {
        "stock": stock.upper(),
        "decision": decision,
        "probability": round(prob_buy, 3),
        "threshold": BUY_THRESHOLD,
        "confidence": confidence
    }
