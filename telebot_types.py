
from telebot import types, TeleBot
API_TOKEN = '7532380964:AAE3ILzlrEVnDoyPguC-rAjg-8lvPUgNM4c'

bot = TeleBot(API_TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "<b>Добро пожаловать!</b>)")

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn_yes = types.KeyboardButton('пополнить баланс')
    btn_no = types.KeyboardButton('купить')

    keyboard.add(btn_yes, btn_no)

    bot.send_message(message.chat.id, "<b>Hello friends</b>", reply_markup=keyboard)

@bot.message_handler()
def any_message(message):
    if message.text == 'good':
        bot.send_message(message.chat.id, "<b>it's good</b>")
    elif message.text == 'bad':
        bot.send_message(message.chat.id, "<b>капец ты неудачник</b>")

bot.polling()


from telebot import types, TeleBot
API_TOKEN = '7532380964:AAE3ILzlrEVnDoyPguC-rAjg-8lvPUgNM4c'

bot = TeleBot(API_TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "<b>Добро пожаловать!</b>)")
    keyboard = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("Callback", callback_data="btn1")
    btn2 = types.InlineKeyboardButton("url", url="https://www.youtube.com/")

    keyboard.row(btn1)
    keyboard.row(btn2)
    bot.send_message(message.chat.id, "<b>Hello friends</b>", reply_markup=keyboard)

@bot.message_handler(content_types=["text"])
def send_photo(message):
    bot.reply_to(message, "да саян такой")

bot.polling()


