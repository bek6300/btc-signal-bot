# ==== 1. FULL bot code ====
# This is a Flask app that receives signals from TradingView via webhook
# and sends them to Telegram. No database, just real-time.

from flask import Flask, request
import requests

# Telegram credentials (use your own values)
TELEGRAM_TOKEN = "7632904089:AAEwvo1TV08iJntpWn_WK4qRh_6Aq9EruBI"
CHAT_ID = "888976753"

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    # Parsing data
    signal = data.get("signal", "UNKNOWN")
    ticker = data.get("ticker", "BTCUSDT")
    price = data.get("price", "N/A")

    # Format message
    text = f"""
✅ Signal: {signal}
⃣ Pair: {ticker}
💰 Price: {price}
⚖️ Setup: EMA20/50, RSI, Supertrend
"""

    # Send to Telegram
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, json=payload)
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

