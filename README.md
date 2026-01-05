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

