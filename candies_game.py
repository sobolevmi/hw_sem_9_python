import telebot
from random import randint

TOKEN = "5773156050:AAEg5pGPYisCRjxIxUaT53c3n3A21Xbukgk"

bot = telebot.TeleBot(TOKEN)

left = 100


@bot.message_handler()
def answer(message: telebot.types.Message):
    global left
    count_2 = player_move(left, message.text)
    # if not count_2:
    #     bot.send_message(chat_id=message.from_user.id, text="Некорректный ввод. Попробуйте снова")
    #     return
    left -= count_2
    bot.send_message(chat_id=message.from_user.id, text=f"Взято конфет: {count_2}")
    bot.send_message(chat_id=message.from_user.id, text=f"На столе осталось {left} конфет(ы)")
    count_1 = bot_move(left)
    # if not count_1:
    #     bot.send_message(chat_id=message.from_user.id, text="Некорректный ввод. Попробуйте снова")
    #     return
    left -= count_1
    bot.send_message(chat_id=message.from_user.id, text=f"Взято конфет: {count_1}")
    bot.send_message(chat_id=message.from_user.id, text=f"На столе осталось {left} конфет(ы)")
    if left == 0:
        bot.send_message(chat_id=message.from_user.id, text="Игра окончена")
        left = 100


def player_move(left, count):
    """Функция хода игрока. Аргументы: left - общее количество конфет; count - количество взятых
    пользователем конфет"""
    if not count.isnumeric():
        return 0
    count = int(count)
    if count <= 1 or count >= 29:
        return 0
    if count > left:
        return 0
    return count


def bot_move(left):
    """Функция хода бота. Аргумент left - общее количество конфет"""
    if left <= 57 and left > 29:
        count = left - 29
        return count
    elif left < 29:
        count = left
        return count
    else:
        count = randint(1, 28)
        return count


bot.polling()