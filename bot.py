import telebot
import urllib
import config
import requests

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "howdy, how are you doing?")

#@bot.message_handler(commands=['inf'])
#def inf(message):
   # text = m.text.replace("/inf ","")
#    urllib.urlretrieve("https://api.spotify.com/v1/albums/5OZJflQcQCdZLQjtUudCin")
##
print("bot run successfuly")

bot.polling(none_stop=True, interval=0, timeout=3)