import pandas as pd
import numpy as np
import joblib

def run_backtest():
    # Load ML dataset
    ml_data = pd.read_csv(
        "data/reliance_ml_dataset.csv",
        index_col=0,
        parse_dates=True
    )

    # Load price data
    price_data = pd.read_csv("data/reliance.csv")

    # normalize column names
    price_data.columns = price_data.columns.str.lower().str.strip()

    # parse date
    price_data["date"] = pd.to_datetime(price_data["date"], errors="coerce")
    price_data.set_index("date", inplace=True)

    # FORCE numeric close price
    price_data["close"] = (
        price_data["close"]
        .astype(str)
        .str.replace(",", "", regex=False)
    )

    price_data["close"] = pd.to_numeric(
        price_data["close"],
        errors="coerce"
    )

    # drop bad rows
    price_data = price_data.dropna(subset=["close"])

    price_data = price_data.sort_index()


    # Align
    common_idx = ml_data.index.intersection(price_data.index)
    ml_data = ml_data.loc[common_idx]
    price_data = price_data.loc[common_idx]

    # Features
    features = [
        "return", "sma_20", "sma_50", "rsi", "volatility",
        "nifty_return", "nifty_volatility", "banknifty_return"
    ]

    X = ml_data[features]
    prices = price_data["close"]

    # Split
    split = int(len(X) * 0.8)
    X_test = X.iloc[split:]
    prices_test = prices.iloc[split:]

    # Load model
    model = joblib.load("models/rf_reliance.pkl")
    probs = model.predict_proba(X_test)[:, 1]

    # Strategy
    threshold = 0.5
    signals = (probs > threshold).astype(int)

    returns = prices_test.pct_change().fillna(0)
    strategy_returns = returns * signals

    ml_equity = (1 + strategy_returns).cumprod()
    bh_equity = (1 + returns).cumprod()

    return {
        "dates": ml_equity.index.astype(str).tolist(),
        "ml_equity": ml_equity.round(4).tolist(),
        "buy_hold": bh_equity.round(4).tolist()
    }
