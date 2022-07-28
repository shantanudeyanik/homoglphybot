import telebot
from homoglyph_generator import homograph
import os
from dotenv import load_dotenv


if __name__ == "__main__":

    load_dotenv()

    token = os.getenv('TOKEN_KEY')
    
    bot = telebot.TeleBot(token)

    @bot.message_handler()
    def msg_reply(m):
        print(m)
        homograph_text = homograph(m.text)
        bot.reply_to(m, homograph_text)


    bot.polling()

