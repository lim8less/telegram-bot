import os
import time
import telebot
from dotenv import load_dotenv
from bot import Bot
load_dotenv()


bot = telebot.TeleBot(os.getenv("TOKEN"))
bot_fn = Bot()


@bot.message_handler(commands=['weather'])
def send_welcome(message):
	bot.reply_to(message, bot_fn.hourly_weather())


@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "For more help and updates join telegram channel given in description.")

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)


while True:
	try:
		bot.polling()
	except:
		time.sleep(5)
