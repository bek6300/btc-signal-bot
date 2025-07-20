from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "7632904089:AAEwvo1TV08iJntpWn_WK4qRh_6Aq9EruBI"
CHAT_ID = "888976753"

@app.route("/", methods=["POST"])
def send_signal():
    data = request.get_json()
    message = data.get("message", "⚠️ No message received.")
    
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    
    response = requests.post(telegram_url, json=payload)
    return ("✅ Sent", 200) if response.ok else (f"❌ Error: {response.text}", 400)
