from telegram import Update, Bot, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler, ConversationHandler
import logging
import brains
import random


TOKEN = ''


reply_keyboard = [['/play', '/rules'],
                  ['/stop']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
cont = ReplyKeyboardMarkup([['Продолжить']], one_time_keyboard=False)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


global player

global n
global m
n_init = 80 #2021
m_init = 28
n = n_init
m = m_init


def start(update, context):
    global n
    global m
    n = n_init
    m = m_init
    update.message.reply_text("Привет давай поиграем в игру", reply_markup=markup)
        #chat_id=update.effective_chat.id,
        #                         text="Привет! Давай поиграем в игру")

def rules(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга."
                                  " Первый ход определяется жеребьёвкой. За один ход можно забрать не более "
                                  "чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. ")


def move_draw(update, context):
    global player
    player = brains.move_draw_b()
    val = ['Игрока', 'бота'][player]
    if player == 1:
        update.message.reply_text(f"Ход {val} нажми продолжить", reply_markup=cont)
    else:
        update.message.reply_text(f"Ход {val}! Введите количество конфет", reply_markup=ReplyKeyboardRemove())

    return player


def player_turn(update, context):
    global n
    global m
    #update.message.reply_text(f"Ход игрока")
    try:
        msg = int(update.message.text)
        if msg <= m:
            n = n - msg
            if n == 0:
                update.message.reply_text(f"Вы взяли {msg} конфет, остаток {n} конфет.")
                update.message.reply_text("Поздравляю Вы победили!", reply_markup=ReplyKeyboardRemove())
                return ConversationHandler.END
            update.message.reply_text(f"Вы взяли {msg} конфет, остаток {n} конфет, ход бота. Нажмите продолжить ", reply_markup=cont)
            return 1
        else:
            update.message.reply_text(f"Необходимо ввести число конфет до {m}")
            return 0
    except:
        update.message.reply_text("Необходимо ввести число конфет")
        return 0



def bot_turn(update, context):
    global n
    global m
    bot_input = brains.bot_brain(n, m)
    n = n - bot_input
    if n == 0:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"Бот взял {bot_input}, остаток {n} конфет. Нажмите продолжить", reply_markup=cont)
        update.message.reply_text("Выйграл бот!", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"Бот взял {bot_input}, остаток {n} конфет."
                              f"\nВаш ход: ", reply_markup=ReplyKeyboardRemove())
    return 0


def stop(update, context):

    update.message.reply_text("Игра отключена!")
    return ConversationHandler.END

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    game_handler = ConversationHandler(
        entry_points=[CommandHandler('play', move_draw)],
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            0: [MessageHandler(Filters.text & ~Filters.command, player_turn)],
            # Функция читает ответ на второй вопрос и завершает диалог.
            1: [MessageHandler(Filters.text & ~Filters.command, bot_turn)]
        },
        fallbacks=[CommandHandler('stop', stop)])


    dp.add_handler(CommandHandler('start', start))
    #dp.add_handler(CommandHandler('stop', stop))
    dp.add_handler(CommandHandler('rules', rules))

    dp.add_handler(game_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
()