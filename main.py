from flask import Flask, request
from telegram import Bot
import os

TOKEN = os.getenv("BOT_TOKEN") or "ISI_TOKEN_DISINI"
CHAT_ID = os.getenv("CHAT_ID") or "ISI_CHAT_ID_DISINI"

bot = Bot(token=TOKEN)
app = Flask(__name__)

@app.route('/')
def index():
    return 'Bot is alive!'

@app.route('/alert', methods=['POST'])
def alert():
    data = request.get_json()
    message = data.get('message', 'No message received.')
    bot.send_message(chat_id=CHAT_ID, text=f'📊 Alert:\n{message}')
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)