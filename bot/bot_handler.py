# - *- coding: utf- 8 - *-
from importlib import reload
import sys
from bot.helpers import *
from bot.instances import add_buttons


@bot.message_handler(commands=['start'])
def welcome(message):
    # chat_id = message.chat.id
    # text = message.text
    # message_id = message.message_id
    # from_user_id = message.from_user.id

    add_buttons(message)



@bot.message_handler(content_types=["text"])
def logic_handler(message):
    if message.chat