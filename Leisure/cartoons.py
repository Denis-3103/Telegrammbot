import telebot
from conf import *
from random import choice, randint
from telebot import types

bot = telebot.TeleBot(TOKEN)

randlist = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg']
randlist_1 = ['16.jpg', '17.jpg', '18.jpg', '19.jpg', '20.jpg', '21.jpg', '22.jpg', '23.jpg', '24.jpg', '25.jpg', '26.jpg', '27.jpg','28.jpg', '29.jpg', '30.jpg']


@bot.message_handler(commands=['start', 'help'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Анекдоты")
    btn2 = types.KeyboardButton("Карикатуры")
    markup.add(btn1, btn2)
    photo = open('title.jpg', 'rb')
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я подниму тебе настроение. Выбери, что нравится, анекдоты или карикатуры.".format(message.from_user), reply_markup=markup)
    bot.send_photo(message.chat.id, photo)


@bot.message_handler()
def get_text(message):
    if message.text == 'Карикатуры'or message.text == 'карикатуры' or message.text =='Карикатура' or message.text =='карикатура':
        photo = open(choice(randlist), 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Хочешь ещё, тогда нажми на кнопку!')
    elif message.text == 'Анекдоты' or message.text == 'анекдоты' or message.text == 'Анекдот' or message.text == 'анекдот':
        photo = open(choice(randlist_1), 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Хочешь ещё, тогда нажми на кнопку!')
    elif message.text == 'help' or message.text == '/help':
        bot.send_message(message.chat.id, 'Выбери кнопку или напиши, что хочешь, анекдот или карикатуру. Чтобы вызвать кнопки напиши /start')
    elif message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, я БОТ, я знаю анекдоты и показываю картинки, нажми /start")
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю. Напиши /help')

bot.polling(none_stop=True)