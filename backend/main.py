from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def read_root():
    return {"message": "Investment Strategy Simulator API is running"}

@app.get("/stock/{ticker}")
def get_stock_data(ticker: str, period: str = "1mo", interval: str = "1d"):
    stock = yf.Ticker(ticker)
    history = stock.history(period=period, interval=interval)
    return history.reset_index().to_dict(orient="records")

# @app.get("/stock/{symbol}")
# async def get_stock(symbol: str):
#     return {"symbol": symbol, "price": 150.00}