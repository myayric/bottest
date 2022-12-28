import telebot

bot = telebot.TeleBot('5621475158:AAE_SdKFxDsqKcSOkajnEHMdG14aOEJxyuA')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'It works!')


bot.polling()
