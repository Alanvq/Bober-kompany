
import telebot

API_TOKEN = '7532380964:AAE3ILzlrEVnDoyPguC-rAjg-8lvPUgNM4c'

bot = telebot.TeleBot(API_TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "<b>Добро пожаловать!</b>)")

bot.polling()
