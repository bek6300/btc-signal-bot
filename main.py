import os
import requests
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    signal = data.get("signal", "UNKNOWN")
    ticker = data.get("ticker", "BTCUSDT")
    price = data.get("price", "N/A")
    text = (
        f"📈 {signal} Signal\n"
        f"🪙 Pair: {ticker}\n"
        f"🕒 Timeframe: 15m\n"
        f"💰 Price: ${price}\n"
        f"📊 Setup: EMA20/50, RSI, Supertrend"
    )
    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        json={"chat_id": CHAT_ID, "text": text}
    )
    return '', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
