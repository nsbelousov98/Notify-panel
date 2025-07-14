from flask import Flask, render_template, request, redirect
from telethon import TelegramClient
from dotenv import load_dotenv
import telegram
import os

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

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    username = request.form.get("username")
    message = request.form.get("message")
    if username and message:
        client.loop.run_until_complete(client.send_message(username, message))
        bot.send_message(chat_id=chat_id, text=f"📩 Отправлено @{username}: {message}")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
