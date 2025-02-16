import alpaca_trade_api as tradeapi
import pandas as pd
import numpy as np
import time

# CONFIGURATION (Use your API Keys)
API_KEY = "your_alpaca_api_key"
SECRET_KEY = "your_alpaca_secret_key"
BASE_URL = "https://paper-api.alpaca.markets"  # Use for paper trading

# Connect to Alpaca API
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

# Trading Parameters
TICKER = "AAPL"
ORDER_SIZE = 1  # Number of shares per trade
RSI_PERIOD = 14
SMA_SHORT = 50
SMA_LONG = 200

# Function to fetch real-time data
def get_data(symbol, limit=500):
    barset = api.get_barset(symbol, 'minute', limit=limit)
    df = pd.DataFrame(barset[symbol]._raw)
    df['time'] = pd.to_datetime(df['t'])
    df.set_index('time', inplace=True)
    return df

# Function to compute RSI
def compute_rsi(data, window=14):
    delta = data["c"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

# Function to generate buy/sell signals
def generate_signals(data):
    data["SMA_50"] = data["c"].rolling(SMA_SHORT).mean()
    data["SMA_200"] = data["c"].rolling(SMA_LONG).mean()
    data["RSI"] = compute_rsi(data, RSI_PERIOD)

    buy_signal = (data["SMA_50"].iloc[-1] > data["SMA_200"].iloc[-1]) and (data["RSI"].iloc[-1] < 30)
    sell_signal = (data["SMA_50"].iloc[-1] < data["SMA_200"].iloc[-1]) and (data["RSI"].iloc[-1] > 70)
    
    return buy_signal, sell_signal

# Function to place an order
def place_order(symbol, qty, side):
    try:
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type='market',
            time_in_force='gtc'
        )
        print(f"✅ Order placed: {side} {qty} shares of {symbol}")
    except Exception as e:
        print(f"⚠️ Order failed: {e}")

# Live trading loop
while True:
    try:
        # Fetch latest data
        data = get_data(TICKER)
        
        # Generate signals
        buy, sell = generate_signals(data)

        # Get current position
        position = api.get_position(TICKER) if TICKER in [p.symbol for p in api.list_positions()] else None

        # Execute trades
        if buy and not position:  # Buy only if we don’t already hold the asset
            place_order(TICKER, ORDER_SIZE, "buy")
        elif sell and position:  # Sell only if we hold the asset
            place_order(TICKER, ORDER_SIZE, "sell")

        # Wait before the next check
        time.sleep(60)  # Check every minute

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(10)  # Retry after a short delay
