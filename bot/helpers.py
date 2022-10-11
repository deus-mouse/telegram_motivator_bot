import re
from bot.instances import *
from telebot import types



def add_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButtonPollType("⬆️ to increase")
    item2 = types.KeyboardButtonPollType("⬇️ to spend")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Hi', reply_markup=markup)
