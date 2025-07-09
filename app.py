from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import json
import os

app = Flask(__name__)
CORS(app)

TELEGRAM_BOT_TOKEN = "7682430753:AAH5SReY8fNL6kwI9Zcm6EQeLlSd0-nkNQM"
TELEGRAM_CHAT_ID = "7757453206"

DATA_FILE = 'data.json'

@app.route('/')
def index():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return render_template('index.html', data=data)

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    name = data.get('name', 'Без имени')
    username = data.get('username', '')
    city = data.get('city', '')
    action = data.get('action', 'Запрос')
    play = data.get('play', '')
    time = data.get('time', '')
    meet_time = data.get('meet_time', '')

    message = f"📬 Новый запрос от бота:\n\n"
    message += f"👤 {name} ({username})\n"
    message += f"🏙️ Город: {city}\n"
    message += f"🎭 Спектакль: {play}\n"
    message += f"🕒 Встреча: {meet_time}, спектакль: {time}\n\n"
    message += f"📌 Действие: {action}"

    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
        json={"chat_id": TELEGRAM_CHAT_ID, "text": message}
    )

    return jsonify({"status": "ok"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
