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

# Backtesting

This repository demonstrates a **machine learning–driven backtesting framework** for Indian equities, focusing on **realistic evaluation** rather than raw prediction accuracy.

The goal is to assess how ML signals behave when translated into an actual trading strategy.

---

## Backtesting Setup

- Market: **NSE (India)**
- Asset: **Reliance Industries**
- Model: Random Forest (probability-based signals)
- Validation: Time-series–aware split
- Strategy:
  - Threshold-based entry using predicted probabilities
  - Multi-day holding period
  - Transaction costs included
- Benchmark: Buy & Hold

---

## Visualization Backtesting (Equity curve)

Below is the backtest equity curve comparing the **ML strategy** with a **Buy & Hold** baseline:

<img width="1001" height="470" alt="image" src="https://github.com/user-attachments/assets/bda04100-9cbf-44d6-bf32-b096b24083d6" />

- The ML strategy significantly reduced drawdowns compared to buy-and-hold, demonstrating effective risk control during adverse market regimes. Further optimization focused on improving return capture.
- My ML model behaved as a downside-risk filter, significantly reducing drawdowns relative to buy-and-hold. This validates the robustness of the feature set and execution logic, even before alpha optimization.


---

## Key Observations

- The ML strategy significantly **reduced drawdowns** compared to Buy & Hold
- Capital remained relatively stable during adverse market regimes
- Demonstrates ML behaving as a **risk-aware filter**, not an overfitted return engine

---

## Disclaimer

This project is for **educational purposes only** and does not constitute financial advice.
