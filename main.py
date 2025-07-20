from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Muhit o'zgaruvchilar (Renderda sozlanadi)
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    if not data:
        return "No JSON payload", 400

    message = data.get('message', '⚠️ No message received')
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"  # agar kerak bo‘lsa markdown ham bo‘lishi mumkin
    }

    response = requests.post(url, json=payload)
    return {'status': 'ok', 'telegram_response': response.json()}

@app.route('/', methods=['GET'])
def index():
    return "🟢 TradingView → Telegram server is running."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
