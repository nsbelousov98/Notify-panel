from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

TELEGRAM_BOT_TOKEN = "тут_вставь_токен"
TELEGRAM_CHAT_ID = "тут_вставь_чат_id"

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
    app.run(debug=True)
