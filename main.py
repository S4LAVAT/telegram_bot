# from dotenv import load_dotenv 
# import os 
# import telebot 

# load_dotenv()
# token = os.environ.get('TELEGRAM_TOKEN') 
# bot = telebot.TeleBot(token)


# @bot.message_handler(commands=['start'])
# def start(message):
# 	bot.send_message(message.chat.id, '')

# @bot.message_handler(content_types=['text'])
# def echo(message):
# bot.polling()

from dotenv import load_dotenv
import os
import telebot
from get_weather import get_weather 

load_dotenv()
token = os.environ.get('TELEGRAM_TOKEN')

bot = telebot.TeleBot(token)

# /start
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Hallo i am weather bot, enter yoit city')

@bot.message_handler(content_types=["text"])
def show_weather(message):
	try:
		weather, degrees = get_weather(message.text)
		bot.send_message(message.chat.id,'weather in '+ message.text + ':' + weather + ' degrees ' + str(degrees))
	except TypeError:
		bot.send_message(message.chat.id, ' город введен неправильно попробуй снова')
bot.polling()
 






