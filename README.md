# 📈 Growstocks (ML Based Stock Buy Decision System)

**Author:** Shrish  
**Degree:** B.Tech CSE (AI/ML)

---

## 🚀 Project Overview

This project is an end-to-end **Machine Learning–based decision-support system** that predicts whether a user should **BUY or DO NOT BUY** a selected Indian stock.

> ⚠️ This is **NOT a trading bot** and does **NOT execute trades**.  
> The system is designed purely for **educational, analytical, and decision-support purposes**.

Instead of predicting stock prices or claiming profitability, the project focuses on a more **realistic and interview-safe ML objective**:

> **“Should I consider buying this stock today based on recent market behavior?”**

Live 🔗 : https://growstocks-ml-2.onrender.com

---

## ✨ Key Features

- ✅ BUY / DO NOT BUY recommendation  
- 📊 Probability-based confidence score  
- 🧠 Stock-specific ML models  
- 🔁 Walk-forward validation  
- 🧪 Offline backtesting for evaluation  
- 🌐 FastAPI backend  
- 🎨 Modern React frontend  

---

## 🎯 Problem Formulation

### Input
- Historical stock price data  
- Technical indicators  
- Market index signals (NIFTY, BANKNIFTY)

### Output
- **Decision:** BUY or DO NOT BUY  
- **Probability:** Likelihood of positive future return  
- **Signal Strength:** Low / Medium / High  

---

## 🧠 Machine Learning Approach

### Target Definition (Important)

Instead of predicting **next-day price movement** (which is extremely noisy), the model predicts:

> **Whether the stock price will be higher after N future trading days**


- `target = 1` → BUY candidate  
- `target = 0` → DO NOT BUY  

This formulation aligns much better with **real-world buy decisions**.

---

## 🧩 Feature Engineering

The following features are used consistently across all stocks:

- `return`
- `sma_20`
- `sma_50`
- `rsi`
- `volatility`
- `nifty_return`
- `nifty_volatility`
- `banknifty_return`

All features are computed using **only past data** to avoid data leakage.

---


🧪 Technologies Used
### Machine Learning

Python, Pandas, NumPy, Scikit-learn (RandomForest)

### Backend

FastAPI, Joblib, Pydantic, CORS Middleware

### Frontend

React (Vite), Axios, Custom CSS (Fintech dark theme)

## Model Validation (Walk-Forward Analysis)

To ensure time-series correctness and avoid data leakage, the models were evaluated using **walk-forward validation** instead of random train-test splits.

- Training window: ~2 years
- Testing window: ~3 months
- Sliding window approach across the full dataset
- Evaluation performed across multiple market regimes

The results show consistent performance across time, demonstrating that the model learns stable patterns rather than overfitting a single period.

Results are stored in:
`results/reliance_walk_forward_results.csv`

## Visualization (Walk-Forward Analysis)
<img width="985" height="390" alt="image" src="https://github.com/user-attachments/assets/a7892293-0954-49d1-814c-70c9f0ef0d4b" />

### Walk-Forward Validation (Time-Series Correct)
The model was evaluated using rolling train-test windows across multiple market regimes to ensure temporal generalization. This avoids data leakage and provides a realistic estimate of real-world performance.

## 📊 Backtesting (Offline Evaluation Only)

Backtesting is used **only for evaluation**, not shown to end users.

### Purpose
- Compare ML-based decisions against Buy & Hold  
- Analyze drawdowns and signal quality  
- Validate walk-forward predictions  

### Example: ICICI Bank Backtest

<img width="1001" height="470" alt="image" src="https://github.com/user-attachments/assets/2847e1bf-5d76-4403-b7f2-e3e124831ae9" />

> Blue: ML-based decisions  
> Orange: Buy & Hold  


### Interpretation
- The ML strategy underperformed Buy & Hold in this period, primarily due to a **strong upward trend** where a conservative, risk-filtering model stayed out of the market.
- The strategy exhibited **lower volatility and controlled drawdowns**, indicating cautious signal generation rather than overfitting.
- This highlights a key trade-off in financial ML: **risk reduction vs. return capture**.

⚠️ Backtesting results are **NOT financial advice** and **NOT optimized for profit**.

---

### Key Takeaway
The result demonstrates that ML models must be evaluated not only on returns but on **behavior across market regimes**. In trending markets, simple Buy & Hold can outperform conservative ML strategies, while ML-based risk filters may add value during volatile or drawdown-heavy periods.

> This project emphasizes realistic evaluation and honest reporting over exaggerated profitability claims.

## Disclaimer
This project is for **educational purposes only** and does not constitute financial advice.
