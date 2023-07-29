from realt import ParsRealt

from constants import bot


@bot.message_handler(commands=["start"])
def start(message):
    mess = f'Привет, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def apartment(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Приступим к выбору квартиры')
    elif message.text == '/help':
        bot.send_message(message.chat.id, 'Начни с приветствия)')
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю, напиши /help.')


bot.polling(none_stop=True, interval=0)
