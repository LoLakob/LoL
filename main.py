import telebot

TOKEN = "5792055854:AAHEB73x-3jnkEjfYh6EuYT1XDPqVhy52Gg"

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def greetings(message):
    reply = "Hi! I'm a simple data collection bot"
    bot.reply_to(message, reply)


is_taking_name = False

@bot.message_handler(content_types=['text'])
def message_handler(message):
    chat_id = message.chat.id
    global is_taking_name

    if is_taking_name:
            user_name = message.text
            print(user_name)
            is_talking_data = False

    if message.text == 'Save user':
        is_taking_data = True
        bot.send_message(chat_id, "Input ur name:")


bot.infinity_polling()