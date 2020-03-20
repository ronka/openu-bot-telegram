import re

from telebot import types
from helpers import send_keyboard
from course import Course
from config import semester_list, course_dict, bot, year_list

from steps.process_year import *


def process_course_id_step(message):
    try:
        chat_id = message.chat.id
        course_id = message.text

        if not course_id.isdigit() or not (4 <= len(str(course_id)) <= 5):
            msg = bot.reply_to(message, 'מספר קורס איננו תקין\nאנא נסה שנית 👇')
            bot.register_next_step_handler(msg, process_course_id_step)
            return

        course = Course(course_id)
        course_dict[chat_id] = course

        msg = send_keyboard(bot, message, 'איזה שנה?', year_list)
        bot.register_next_step_handler(msg, process_year_step)
    except Exception as e:
        bot.reply_to(message, 'אופסס קרתה תקלה,\n יש לשלוח /start כדי להתחיל מהתחלה')
    # end exception #


# end process_course_id_step #


@bot.callback_query_handler(func=lambda call: call.data.startswith("cid_"))
def callback_query(call):
    course_id = re.findall('\d+', call.data)

    chat_id = call.message.chat.id

    course = Course(course_id)
    course_dict[chat_id] = course

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(*year_list)
    msg = bot.send_message(chat_id, 'איזה שנה?', reply_markup=markup)
    bot.register_next_step_handler(msg, process_year_step)
