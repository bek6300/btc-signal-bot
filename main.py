from flask import Flask, request
import os
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    signal = data.get("signal", "UNKNOWN")
    ticker = data.get("ticker", "BTCUSDT")
    price = data.get("price", "N/A")

    text = f"""
📈 Signal: {signal}
🪙 Pair: {ticker}
💰 Price: ${price}
📊 Setup: EMA20/50, RSI, Supertrend
"""
    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        json={"chat_id": CHAT_ID, "text": text}
    )
    return {"status": "ok"}

if __name__ == "__main__":
