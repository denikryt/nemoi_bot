from __future__ import annotations

import yaml
from telebot import TeleBot, types


CONFIGFILE = 'config.yaml'

with open(CONFIGFILE, 'r') as f:
    token = yaml.load(f, Loader=yaml.FullLoader)['config']['token']

bot = TeleBot(token)


@bot.message_handler(commands=['start'])
def welcome(message):
    context.to_default()
    bot.send_message(message.chat.id, 'ну шо?')


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        context.instructions(message)


if __name__ == "__main__":
    """Client code"""
    context = Context(Default())
    bot.polling(none_stop=True)
