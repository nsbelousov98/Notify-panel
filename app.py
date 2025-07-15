from flask import Flask, render_template, request, redirect
from telethon import TelegramClient
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

# Flask приложение
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Данные из .env
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = os.getenv("SESSION", "session_name")
chat_id = int(os.getenv("CHAT_ID"))

# Инициализация Telethon клиента
client = TelegramClient(session_name, api_id, api_hash)

# Стартуем Telethon отдельно
loop = asyncio.get_event_loop()
loop.run_until_complete(client.start())

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    username = request.form.get("username")
    message = request.form.get("message")
    if username and message:
        # Отправляем сообщение пользователю
        loop.run_until_complete(client.send_message(username, message))
        # Уведомляем тебя в личку
        loop.run_until_complete(client.send_message(chat_id, f"📩 Отправлено @{username}: {message}"))
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
