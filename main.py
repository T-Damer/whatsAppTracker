import telepot

import time
from dotenv import load_dotenv
import os

from macheronte.whatsapp.enums.browsers import Browsers
from macheronte.whatsapp.client import WhatsappClient
from macheronte.tracker.user import User

load_dotenv()

telegramUsers = ['395659658']
user = None


def on_chat_message(msg):
    global user

    content_type, chat_type, chat_id = telepot.glance(msg)

    if (str(chat_id) in telegramUsers):
        if content_type == 'text' and (user is None or msg['text'] != user.user_name):
            user = User(msg['text'], client)
            bot.sendMessage(chat_id, "Trying to track " + user.user_name)


bot = telepot.Bot(os.environ.get('tgToken'))
bot.message_loop(on_chat_message)

client = WhatsappClient(Browsers.CHROME)
client.connect()

while True:
    try:
        if user is not None and client.is_logged():
            bot.sendMessage(telegramUsers[0], 'User is not valid')
            user = None
        else:
            user.sample()

            if user.is_new() and user.header != None:
                bot.sendPhoto(telegramUsers[0], photo=user.header)

            if user.has_new_status():
                bot.sendMessage(telegramUsers[0], str(user.user_name + ": " + user.status.value))

    except Exception as e:
        print(e)

    time.sleep(2)