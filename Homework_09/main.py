from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler, ConversationHandler
from random import randint
import logging
import sqlite3
import brains


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)



TOKEN = ''
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Привет! имеются следующие команды:\n"
                                      "/add - добавить пользователя\n"
                                      "/find - найти пользователя\n"
                                      "/delete_v - удалить строку (номер через пробел) например /delete_v 1\n"
                                      "/show - вывести результат\n"
                                      "/update - обновить строку (номер через строку)")


def add(update, context):
    update.message.reply_text(
        "Для добавлении записи необходимо ответить на вопросы\n"
        "для пропуска поля введите -\n"
        "для выхода введите команду /stop.\n"
        "Введите фамилию:?")
    return 1

def find(update, context):
    update.message.reply_text(
        "Для поиска записи необходимо ответить на вопросы\n"
        "для пропуска поля введите -\n"
        "для выхода введите команду /stop.\n"
        "Введите фамилию:?")
    return 1

def delete_v(update, context):
    msg = update.message.text

    try:
        msg = msg.split(" ")[1]
        brains.delete_val_b(msg)
        update.message.reply_text(
            "Удалено " + msg)
    except:
        update.message.reply_text(
            "Что то пошло не так")
    return 1

def update_us(update, context):
    msg = update.message.text
    print(msg)
    try:
        global id_person
        id_person = msg.split(" ")[1]
        update.message.reply_text(
            f"Вводим только значения для столбов которые хотим менять,"
            f" что не меняем вводим прочерк\n"
            f"Введите Фамилию ")

    except:
        update.message.reply_text(
            "Что то пошло не так")
    return 1

def first_response(update, context):
    global request
    request = {}
    msg = update.message.text
    if msg != "-":
        request["Фамилия"] = msg
    update.message.reply_text(
        f"Введите имя:")
    return 2

def second_response(update, context):
    global request
    name = update.message.text
    if name != "-":
        request["Имя"] = name
    logger.info(name)
    update.message.reply_text(f"Введите отчество")
    return 3

def third_response(update, context):
    global request
    patronymic = update.message.text
    if patronymic != "-":
        request["Отчество"] = patronymic
    logger.info(patronymic)
    update.message.reply_text(f"Введите телефон")
    return 4

def fourth_response(update, context):
    global request
    telephon = update.message.text
    if telephon != "-":
        request["Телефон"] = telephon
    logger.info(telephon)
    update.message.reply_text(f"Введите комментарий")
    return 5

def fifth_response_add(update, context):
    global request
    fifth  = update.message.text
    if fifth != "-":
        request["Комментарий"] = fifth
    logger.info(fifth)
    brains.add_values(request)
    update.message.reply_text(f"Данные добавлены {request}")
    return ConversationHandler.END  # Константа, означающая конец диалога.
    # Все обработчики из states и fallbacks становятся неактивными.

def fifth_response_find(update, context):
    global request
    fifth  = update.message.text
    if fifth != "-":
        request["Комментарий"] = fifth
    logger.info(fifth)
    print(request)
    answer = brains.find_b(request)
    with open("test.txt", "w") as f:
        f.writelines(answer)
    context.bot.send_document(chat_id= update.message.chat.id, document=open("test.txt", 'rb'))
    update.message.reply_text(answer)
    return ConversationHandler.END



def update_last(update, context):
    global request
    global id_person
    fifth  = update.message.text
    if fifth != "-":
        request["Комментарий"] = fifth
    logger.info(fifth)
    brains.update_info(id_person, request)
    return ConversationHandler.END

def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END

def show(update, context):
    answer = brains.show_b()
    with open("test.txt", "w") as f:
        f.writelines(answer)
    context.bot.send_document(chat_id= update.message.chat.id, document=open("test.txt", 'rb'))
    update.message.reply_text(answer)


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('add', add)],
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            1: [MessageHandler(Filters.text & ~Filters.command, first_response)],
            # Функция читает ответ на второй вопрос и завершает диалог.
            2: [MessageHandler(Filters.text & ~Filters.command, second_response)],
            3: [MessageHandler(Filters.text & ~Filters.command, third_response)],
            4: [MessageHandler(Filters.text & ~Filters.command, fourth_response)],
            5: [MessageHandler(Filters.text & ~Filters.command, fifth_response_add)]
        },
        fallbacks=[CommandHandler('stop', stop)])

    find_handler = ConversationHandler(
        entry_points=[CommandHandler('find', find)],
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            1: [MessageHandler(Filters.text & ~Filters.command, first_response)],
            # Функция читает ответ на второй вопрос и завершает диалог.
            2: [MessageHandler(Filters.text & ~Filters.command, second_response)],
            3: [MessageHandler(Filters.text & ~Filters.command, third_response)],
            4: [MessageHandler(Filters.text & ~Filters.command, fourth_response)],
            5: [MessageHandler(Filters.text & ~Filters.command, fifth_response_find)]
        },
        fallbacks=[CommandHandler('stop', stop)])

    update_handler = ConversationHandler(
        entry_points=[CommandHandler('update', update_us)],
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            1: [MessageHandler(Filters.text & ~Filters.command, first_response)],
            # Функция читает ответ на второй вопрос и завершает диалог.
            2: [MessageHandler(Filters.text & ~Filters.command, second_response)],
            3: [MessageHandler(Filters.text & ~Filters.command, third_response)],
            4: [MessageHandler(Filters.text & ~Filters.command, fourth_response)],
            5: [MessageHandler(Filters.text & ~Filters.command, update_last)]
        },
        fallbacks=[CommandHandler('stop', stop)])



    start_handler = CommandHandler('start', start)


    dp.add_handler(CommandHandler('show', show))
    dp.add_handler(CommandHandler('delete_v', delete_v))
    dp.add_handler(start_handler)
    dp.add_handler(conv_handler)
    dp.add_handler(find_handler)
    dp.add_handler(update_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
()