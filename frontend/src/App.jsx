import { useState } from "react";
import axios from "axios";
import "./App.css";
import iconImage from "./assets/icon-2.png";

const STOCKS = ["RELIANCE", "TCS", "ICICIBANK", "INFY", "HDFCBANK"];

function App() {
  const [stock, setStock] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeStock = async () => {
    if (!stock) return;

    setLoading(true);
    setResult(null);

    try {
      const res = await axios.get(
        `http://127.0.0.1:8000/predict?stock=${stock}`
      );
      setResult(res.data);
    } catch (err) {
      alert("API Error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="container">
        <div className="icon">
          <img src={iconImage} alt="GrowStocks Icon" />
        </div>

        <h1>
          Grow<span>stocks</span>
        </h1>
        <p className="subtitle">
          ML-based probability-driven stock analysis
        </p>

        <label>Select Stock</label>
        <select value={stock} onChange={(e) => setStock(e.target.value)}>
          <option value="">Choose a stock</option>
          {STOCKS.map((s) => (
            <option key={s} value={s}>
              {s}
            </option>
          ))}
        </select>

        <button onClick={analyzeStock} disabled={!stock || loading}>
          {loading ? "Analyzing..." : "⚡ Analyze Stock ↗"}
        </button>

        {result && (
          <div
            className={`result-card ${
              result.decision === "BUY" ? "buy" : "no-buy"
            }`}
          >
            <span className="tag">ANALYSIS COMPLETE</span>

            <h2 className="result-stock-name">{result.stock}</h2>

            <div className={`decision ${result.decision === "BUY" ? "buy-decision" : "no-buy-decision"}`}>
              {result.decision === "BUY" ? "↗ BUY" : "↘ DO NOT BUY"}
            </div>

            <div className="stats">
              <div className={`stat-box confidence-box ${result.decision === "BUY" ? "buy-stat" : "no-buy-stat"}`}>
                <p>Confidence Score</p>
                <h3>{Math.round(result.probability * 100)}%</h3>
              </div>

              <div className="stat-box signal-box">
                <p>Signal Strength</p>
                <h3>{result.confidence}</h3>
              </div>
            </div>

            <div className="note">
              <span className="note-icon">ℹ️</span>
              Moderate signal with mixed market conditions
            </div>
          </div>
        )}
      </div>
      <footer className="app-footer">
        For educational and research purposes only. Not financial advice.
      </footer>
    </div>
  );
}

export default App;
