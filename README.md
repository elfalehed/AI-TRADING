# AI-Powered Trading Bot
Answering a TikTok question I got from a follower follow me on <a href="https://tiktok.com/@elfalehed">TikTok</a>

## Overview
This is a **real-time AI-powered trading bot** that fetches market data, analyzes technical indicators, and executes trades automatically using the **Alpaca API** for stocks. The bot applies **Simple Moving Averages (SMA)** and **Relative Strength Index (RSI)** to generate buy and sell signals.

## Features
✅ **Real-time market data** fetching from Alpaca API  
✅ **Technical analysis indicators** (SMA-50, SMA-200, RSI)  
✅ **Automated buy/sell execution** based on strategy  
✅ **Live trading with risk management**  
✅ **Continuous monitoring** with minute-by-minute updates  

## Installation

### 1️⃣ Install Dependencies
```bash
pip install alpaca-trade-api pandas numpy matplotlib
```

### 2️⃣ Set Up Alpaca API Keys
Sign up at [Alpaca](https://alpaca.markets/) and get your API keys.

Replace `API_KEY` and `SECRET_KEY` in the script:
```python
API_KEY = "your_alpaca_api_key"
SECRET_KEY = "your_alpaca_secret_key"
BASE_URL = "https://paper-api.alpaca.markets"  # Use for paper trading
```

### 3️⃣ Run the Trading Bot
```bash
python trading_bot.py
```

## Trading Strategy
1️⃣ **Buy Signal** 📈  
- 50-day SMA **crosses above** 200-day SMA (bullish trend)  
- RSI is **below 30** (oversold)  

2️⃣ **Sell Signal** 📉  
- 50-day SMA **crosses below** 200-day SMA (bearish trend)  
- RSI is **above 70** (overbought)  

## Code Breakdown
- `get_data(symbol)`: Fetches real-time price data.
- `compute_rsi(data)`: Calculates the **RSI indicator**.
- `generate_signals(data)`: Generates buy/sell trading signals.
- `place_order(symbol, qty, side)`: Places market orders via Alpaca.
- `while True`: **Runs continuously**, executing trades every minute.

## Roadmap
🚀 **Backtest with historical data**  
🚀 **Integrate Machine Learning (Reinforcement Learning, LSTM)**  
🚀 **Support for Crypto (Binance API)**  
🚀 **Multi-asset trading (Forex, Stocks, Crypto)**  

## Disclaimer
**This bot is for educational purposes only.** Use a **paper trading** account before deploying real funds. Invest responsibly!

---
### 📩 Need Help?
Feel free to open an issue or reach out! Happy trading! 🚀

