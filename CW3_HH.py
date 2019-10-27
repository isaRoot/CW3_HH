import sys

import telebot
import time
import logging

import config
import forward_handler
telebot.logger.setLevel(logging.INFO)


log = telebot.logger

telebot.apihelper.proxy = {'https': config.PROXY}
# https://t.me/socks?server=116.202.18.252&port=4002&user=user_8abd0cee&pass=c3f33dee779316d24e597d1c8abd0cee
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Добро пожаловать, {name}!'.format(name=message.from_user.username))
    log.info('received /start command from {name}'.format(name=message.from_user.username))


@bot.message_handler(func=lambda message: message.forward_from, content_types=["text", "photo", "video"])
def is_forward(message):
    forward_handler.message_forward_income(message)
    sent = bot.send_message(message.chat.id, 'Добро пожаловать, {name}!'.format(name=message.from_user.username))
    log.info('received /start command from {name}'.format(name=message.from_user.username))


@bot.message_handler(regexp='Лот #.*')
def test_lot(message):
    sent = bot.send_message(message.chat.id, 'Посмотри лот, {name}!'.format(name=message.from_user.username))
    log.info('received /start command from {name}'.format(name=message.from_user.username))


@bot.message_handler(commands=['hello'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    log.info('received /hello command from {name}'.format(name=message.from_user.username))
    bot.register_next_step_handler(sent, hello)


def hello(message):
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))


@bot.message_handler(commands=['command1'])
def command1(message):
    bot.send_message(message.chat.id, 'Oops')


@bot.message_handler(regexp='.*(ambush).*')
def def_handler(message):
    bot.reply_to(message, 'isaroot')
    # bot.send_message(message.chat.id, '@isaroot')  #, reply_to_message_id=message.message_id)
    # members = telebot.TeleBot.get_chat_member(telebot, chat_id=message.chat.id)

    print("Test")
    # bot.reply_to(message.chat.id, 'something')


# Polling
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        log.error(e)
        time.sleep(15)
