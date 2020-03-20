import requests

from config import semester_list, course_dict, bot, year_list, API_COURSE
from telebot import types

from steps.process_year import *

flag = True


def process_name_step(message):
    global flag

    chat_id = message.chat.id
    courseName = message.text

    request_params = {'name': courseName}

    try:
        if flag:
            flag = False
            r = requests.get(url=API_COURSE, params=request_params)
            data = r.json()
        else:
            return

        if (not data['success']) or (len(data['data']) == 0):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("🔍 לחיפוש חדש", callback_data="cb_start"))
            bot.send_message(chat_id, "לא נמצא קורס בשם הזה", reply_markup=markup)
            return

        links = []
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 1

        for link in data['data']:
            links.append(
                types.InlineKeyboardButton("{0} ({1})".format(link['name'], link['id']),
                                           callback_data="cid_{}".format(link['id'])))

        markup.add(*links)

        bot.send_message(chat_id, "בחר קורס:", reply_markup=markup)
        flag = True

    except Exception as e:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔍 לחיפוש חדש", callback_data="cb_start"))
        print(e)
        bot.send_message(chat_id, "אראה שגיאה, אנא נסה שנית", reply_markup=markup)
        return
