from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from app.predict import predict_buy_signal

app = FastAPI(
    title="Stock Buy Decision API",
    description="ML-based BUY / DO NOT BUY decision system for Indian stocks",
    version="1.0.0"
)

# Enable CORS (for React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # OK for local dev
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "Stock Buy Decision API is running",
        "usage": "/predict?stock=RELIANCE"
    }

@app.get("/predict")
def predict(
    stock: str = Query(
        ...,
        description="Stock symbol (e.g. RELIANCE, TCS, ICICIBANK, INFY, HDFCBANK)"
    )
):
    """
    Predict BUY / DO NOT BUY decision for a given stock.
    """
    return predict_buy_signal(stock)
