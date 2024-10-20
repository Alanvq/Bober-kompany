from telebot import types, TeleBot
import random
API_TOKEN = '7532380964:AAE3ILzlrEVnDoyPguC-rAjg-8lvPUgNM4c'

bot = TeleBot(API_TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "<b>Добро пожаловать!</b>)")
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    name = message.text
    bot.send_message(message.chat.id, f"Приятно познакомиться, {name}! Сколько тебе лет?")
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    try: 
        age = int(message.text)
        bot.send_message(message.chat.id, f"отлично! тебе {age} лет?")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введи число!")
        bot.register_next_step_handler(message, get_age)

bot.polling()
