from telebot import types, TeleBot
import random
API_TOKEN = '7532380964:AAE3ILzlrEVnDoyPguC-rAjg-8lvPUgNM4c'

bot = TeleBot(API_TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "<b>это бот камень ножницы бумага </b>")

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sciccors = types.KeyboardButton('✌️')
    paper = types.KeyboardButton('✋')
    roke = types.KeyboardButton('✊')

    keyboard.add(sciccors, paper, roke )
   
    bot.send_message(message.chat.id, "<b>Привет это игра камень ножницы бумага</b>", reply_markup=keyboard)

@bot.message_handler()
def any_message(message):
    rpc = random.choice(['✊', '✋', '✌️'])
    bot.send_message(message.chat.id, f"{rpc}")
    if message.text == "✋":
        if rpc == '✌️':
            bot.send_message(message.chat.id, f'ты проиграл')
        elif rpc == '✊':
            bot.send_message(message.chat.id, f"ты выиграл")
        else:
            bot.send_message(message.chat.id, f"ничья")
    elif message.text == "✌️":
        if rpc == '✋':
            bot.send_message(message.chat.id, f'ты выйграл')
        elif rpc == '✊':
            bot.send_message(message.chat.id, f"я выиграл")
        else:
            bot.send_message(message.chat.id, f"ничья")
    elif message.text == "✊":
        if rpc == '✋':
            bot.send_message(message.chat.id, f'я выйграл')
        elif rpc == '✌️':
            bot.send_message(message.chat.id, f'ты выйграл')
        else:
            bot.send_message(message.chat.id, f"ничья")

bot.polling()
