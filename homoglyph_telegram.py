from tokenize import Token
import telebot
from homoglyph_generator import homograph
import os

Token = os.getenv('TOKEN')
print(Token)

bot = telebot.TeleBot(Token)

@bot.message_handler()
def msg_reply(m):
    print()
    homograph_text = homograph(m.text)

    bot.reply_to(m, homograph_text)
bot.polling()

