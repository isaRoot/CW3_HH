import sys


# from CW3_HH import bot


def message_forward_income(message):
    # bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))
    print('received forward from {name}'.format(name=message.from_user.username))
    if message.forward_from.id == 265204902:
        forward_from_cw3(message)


def forward_from_cw3(message):
    geroi_substring = 'Битва семи замков через'
    if geroi_substring in message.text:
        geroi_read(message)
    in_text = message.text.splitlines()
    print(in_text[0])
    print('received CW3 forward from {name}'.format(name=message.from_user.username))
    print('received CW3 forward from {name}'.format(name=message.from_user.username))


def geroi_read(message):
    geroi = message.text.splitlines()
    for g in geroi:
        print(g)
        if g.startswith(('🌹', '🐢', '🍁', '🍆', '☘', '🖤', '🦇')):
            print('ff')
    print('читаю данные героя')
# 🌹 🐢 🍁 🍆 ☘️ 🖤 🦇
