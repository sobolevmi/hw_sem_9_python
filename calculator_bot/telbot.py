import telebot
import logger

TOKEN = "5720439269:AAHv3EhRFlu-rrg2zDDyHX17PW09iM6M4O4"

bot = telebot.TeleBot(TOKEN)

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(   telebot.types.InlineKeyboardButton(" ", callback_data="no"),
                telebot.types.InlineKeyboardButton("C", callback_data="C"),
                telebot.types.InlineKeyboardButton("<=", callback_data="<="),
                telebot.types.InlineKeyboardButton("/", callback_data="/"))

keyboard.row(   telebot.types.InlineKeyboardButton("7", callback_data="7"),
                telebot.types.InlineKeyboardButton("8", callback_data="8"),
                telebot.types.InlineKeyboardButton("9", callback_data="9"),
                telebot.types.InlineKeyboardButton("*", callback_data="*"))

keyboard.row(   telebot.types.InlineKeyboardButton("4", callback_data="4"),
                telebot.types.InlineKeyboardButton("5", callback_data="5"),
                telebot.types.InlineKeyboardButton("6", callback_data="6"),
                telebot.types.InlineKeyboardButton("-", callback_data="-"))

keyboard.row(   telebot.types.InlineKeyboardButton("1", callback_data="1"),
                telebot.types.InlineKeyboardButton("2", callback_data="2"),
                telebot.types.InlineKeyboardButton("3", callback_data="3"),
                telebot.types.InlineKeyboardButton("+", callback_data="+"))

keyboard.row(   telebot.types.InlineKeyboardButton(" ", callback_data="no"),
                telebot.types.InlineKeyboardButton("0", callback_data="0"),
                telebot.types.InlineKeyboardButton(",", callback_data="."),
                telebot.types.InlineKeyboardButton("=", callback_data="="))

value = " "
old_value = " "


@bot.message_handler(commands=["start"])
def start_message(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text="Добро пожаловать в бот-калькулятор!", reply_markup=keyboard)
    logger.log_message("start")


@bot.message_handler()
def calc_operations(message: telebot.types.Message):
    global value
    if value != old_value:
        if value == " ":
            bot.send_message(chat_id=message.from_user.id, text="0", reply_markup=keyboard)
        else:
            bot.send_message(chat_id=message.from_user.id, text=value, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda c: True)
def func_callback_data(query):
    global value, old_value
    data = query.data

    if data == "no":
        pass
    elif data == "C":
        value = " "
    elif data == "=":
        try:
            value = str(eval(value))
            logger.log_time()
        except:
            value = "Ошибка!"
            logger.log_message("critical")
    else:
        value += data

    if value != old_value:
        if value == " ":
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text="0", reply_markup=keyboard)
            logger.log_time()
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=keyboard)

    old_value = value

bot.polling()