import os
import config

from telebot import types
from config import *

from steps.process_course_id import *
from steps.process_year import *
from steps.process_semester import *
from steps.process_name import *


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔍 לחיפוש לינק", callback_data="cb_start"))
    markup.add(types.InlineKeyboardButton("📤 להוספת לינק חדש", url="https://bit.ly/openu-bot-add-link"))
    markup.add(types.InlineKeyboardButton("🤖 לעמוד הפייסבוק", url="https://bit.ly/openu-bot-facebook"))
    bot.send_message(chat_id, "שלום וברוכים הבאים!\nיש לי מטרה פשוטה והיא לספק לך לינקים לקבוצות לימוד",
                     reply_markup=markup)


def start_process(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, divider)

    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(types.InlineKeyboardButton("🔢 מספר קורס", callback_data="cb_number"),
               types.InlineKeyboardButton("🖊️ שם קורס", callback_data="cb_name"))

    bot.send_message(chat_id, "לפי מה תרצה לחפש?",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "cb_start")
def callback_query(call):
    start_process(call.message)


@bot.callback_query_handler(func=lambda call: call.data == "cb_number")
def callback_by_number(call):
    config.flag = True  # ajax flag

    chat_id = call.message.chat.id
    msg = bot.send_message(chat_id, 'מספר קורס:')
    bot.register_next_step_handler(msg, process_course_id_step)


@bot.callback_query_handler(func=lambda call: call.data == "cb_name")
def callback_by_name(call):
    config.flag = True  # ajax flag

    chat_id = call.message.chat.id
    msg = bot.send_message(chat_id, 'שם הקורס:')
    bot.register_next_step_handler(msg, process_name_step)


if __name__ != "__main__":
    exit(0)

if isLocal:
    bot.polling()
    server.run()
else:
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
