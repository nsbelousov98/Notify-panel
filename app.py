from flask import Flask, render_template, request, jsonify
from telethon import TelegramClient
from dotenv import load_dotenv
import telegram
import os
import json

# Загружаем настройки из .env
load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = os.getenv("SESSION")
bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

client = TelegramClient(session_name, api_id, api_hash)
client.start()
bot = telegram.Bot(token=bot_token)

DATA_FILE = "logic/current_data.json"
if not os.path.exists("logic"):
    os.makedirs("logic")
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({"requests": []}, f, ensure_ascii=False)

def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

@app.route("/")
def index():
    data = load_data()
    return render_template("index.html", data=data)

@app.route("/api/data")
def api_data():
    return jsonify(load_data())

@app.route("/send", methods=["POST"])
def send_message():
    username = request.form.get("username")
    message = request.form.get("message")
    if username and message:
        client.loop.run_until_complete(client.send_message(username, message))
        bot.send_message(chat_id=chat_id, text=f"📩 Отправлено @{username}: {message}")
    return ("", 204)

@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return ("", 400)
    file = request.files['file']
    if file.filename != '':
        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)
        bot.send_message(chat_id=chat_id, text=f"📎 Прикреплён билет: {file.filename}")
    return ("", 204)

@app.route("/action", methods=["POST"])
def action():
    action_type = request.form.get("action_type")
    profile_id = request.form.get("profile_id")
    bot.send_message(chat_id=chat_id, text=f"✅ Действие: {action_type} для {profile_id}")
    return ("", 204)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
