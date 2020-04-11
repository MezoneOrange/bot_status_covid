import COVID19Py
import telebot
from telebot import apihelper



covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1273093716:AAERkwdQPWftZ-hUdedT6dccUDGuR0m8Ra0')
countries = {
    'вьетнам': 'VN',
    'ватикан': 'VA',
    'узбекистан': 'UZ',
    'сша': 'US',
    'великобритания': 'GB',
    'англия': 'GB',
    'украина': 'UA',
    'турция': 'TR',
    'тайланд': 'TH',
    'швейцария': 'CH',
    'шведция': 'SE',
    'испания': 'ES',
    'южная корея': 'KR',
    'словения': 'SI',
    'словакия': 'SK',
    'россия': 'RU',
    'румыния': 'RO',
    'португалия': 'PT',
    'польша': 'PL',
    'норвегия': 'NO',
    'новая зеландия': 'NZ',
    'нидерланды': 'NL',
    'мексика': 'MX',
    'люксеибург': 'LU',
    'лихтенштейн': 'LI',
    'латвия': 'LV',
    'япония': 'JP',
    'италия': 'IT',
    'индия': 'IN',
    'венгрия': 'HU',
    'германия': 'DE',
    'грузия': 'GE',
    'франция': 'FR',
    'финляндия': 'FI',
    'чехия': 'CZ',
    'китай': 'CN',
    'канада': 'CA',
    'бразилия': 'BR',
    'аргентина': 'AR',

}


@bot.message_handler(commands=['start'])
def start_message(message):
    send_mess = f"<b>Привет {message.from_user.first_name}!</b>\nВведите название страны на русском."
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()
    if get_message_bot in countries:
        location = covid19.getLocationByCountryCode(countries[get_message_bot])
        mess = f"""В {location[0]['country']} зараженно - {location[0]['latest']['confirmed']}
умерло - {location[0]['latest']['deaths']}"""
        bot.send_message(message.chat.id, mess, parse_mode='html')
    else:
        location = covid19.getLatest()
        mess = f"""<em>Локация не найдена в базе</em>\nВсего заболевших в мире - {location['confirmed']},
Всего умерло в мире - {location['deaths']}"""
        bot.send_message(message.chat.id, mess, parse_mode='html')

bot.polling(none_stop=True)

# latest = covid19.getLatest()
# location = covid19.getLocationByCountryCode('US')

#
# print(location)


