import sys

import telebot
import logging

import config

telebot.logger.setLevel(logging.INFO)


log = telebot.logger


# logger = logging.getLogger('TeleBot')
# formatter = logging.Formatter(
#     '%(asctime)s (%(filename)s:%(lineno)d %(threadName)s) %(levelname)s - %(name)s: "%(message)s"'
# )
# console_output_handler = logging.StreamHandler(sys.stderr)
# console_output_handler.setFormatter(formatter)
# logger.addHandler(console_output_handler)
#
# logger.setLevel(logging.INFO)

# TOKEN = '963004625:AAHgQxjlFFiOVSx7tmeyORmWx28vy2maK8E'  # полученный у @BotFather

telebot.apihelper.proxy = dict(https=config.PROXY)
# https://t.me/socks?server=116.202.18.252&port=4002&user=user_8abd0cee&pass=c3f33dee779316d24e597d1c8abd0cee
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    log.info('received /start command from {name}'.format(name=message.from_user.username))
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


bot.polling()
