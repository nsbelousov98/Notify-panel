from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import telegram
import os

load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

bot = telegram.Bot(token=bot_token)

# Хранилище заявок
requests_data = []

@app.route("/")
def index():
    return render_template("index.html", requests=requests_data)

@app.route("/api/data")
def api_data():
    return jsonify({"requests": requests_data})

@app.route("/send", methods=["POST"])
def send():
    username = request.form.get("username")
    message = request.form.get("message")
    if username and message:
        bot.send_message(chat_id=chat_id, text=f"📩 Отправлено @{username}: {message}")
    return "OK"

@app.route("/add_request", methods=["POST"])
def add_request():
    data = request.json
    requests_data.append(data)
    return jsonify({"status": "added"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
