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

## ICICI Bank — ML Backtesting Result

This section presents the backtesting outcome of a machine learning–driven trading strategy applied to **ICICI Bank (NSE)**.

### Setup
- Model: Random Forest (probability-based directional signals)
- Validation: Time-series split (no random shuffling)
- Strategy:
  - Threshold-based trade entry
  - Multi-day holding period
  - Transaction costs included
- Benchmark: Buy & Hold

### Result (Equity Curve)
<img width="1001" height="470" alt="image" src="https://github.com/user-attachments/assets/2847e1bf-5d76-4403-b7f2-e3e124831ae9" />


### Interpretation
- The ML strategy underperformed Buy & Hold in this period, primarily due to a **strong upward trend** where a conservative, risk-filtering model stayed out of the market.
- The strategy exhibited **lower volatility and controlled drawdowns**, indicating cautious signal generation rather than overfitting.
- This highlights a key trade-off in financial ML: **risk reduction vs. return capture**.

### Key Takeaway
The result demonstrates that ML models must be evaluated not only on returns but on **behavior across market regimes**. In trending markets, simple Buy & Hold can outperform conservative ML strategies, while ML-based risk filters may add value during volatile or drawdown-heavy periods.

> This project emphasizes realistic evaluation and honest reporting over exaggerated profitability claims.

## Disclaimer

This project is for **educational purposes only** and does not constitute financial advice.
