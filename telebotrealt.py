from constants import bot

from realt import ParsRealt

from constants import url


@bot.message_handler(commands=["start"])
def start(message):
    mess = f'Привет, {message.from_user.first_name}, Приступим к выбору квартиры. Напишите количество комнат в квартире.'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def number_of_rooms(message):
    if message.text == "1":
        bot.send_message(message.chat.id,
                         f"{ParsRealt(url=url, values=1).parse(), ParsRealt.number_of_rooms(), ParsRealt.number_of_pages(), ParsRealt.apartment_links()}")
    elif message.text == "2":
        bot.send_message(message.chat.id,
                         f"{ParsRealt(url=url, values=2).parse(), ParsRealt.number_of_rooms(), ParsRealt.number_of_pages(), ParsRealt.apartment_links()}")
    elif message.text == "3":
        bot.send_message(message.chat.id,
                         f"{ParsRealt(url=url, values=3).parse(), ParsRealt.number_of_rooms(), ParsRealt.number_of_pages(), ParsRealt.apartment_links()}")
    elif message.text == "4":
        bot.send_message(message.chat.id,
                         f"{ParsRealt(url=url, values=4).parse(), ParsRealt.number_of_rooms(), ParsRealt.number_of_pages(), ParsRealt.apartment_links()}")


bot.polling(none_stop=True, interval=0)
