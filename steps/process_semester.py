import requests

from telebot import types
from helpers import send_keyboard, print_link
from config import semester_list, course_dict, bot, year_list, divider, flag, API_LINK


def process_semester_step(message):
    global flag

    chat_id = message.chat.id
    semester = message.text

    if semester not in semester_list.keys():
        bot.reply_to(message, 'אופסס, סמסטר לא תקין')

        start_process(message)
        return

    course = course_dict[chat_id]
    course.semester = semester_list[semester]

    request_params = {'courseId': course.courseId, 'year': course.year, 'semester': course.semester}

    if flag:
        flag = False
        r = requests.get(url=API_LINK, params=request_params)
        data = r.json()
    else:
        return

    # if no links found
    if not data['success']:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📤 להוספת לינק למערכת", url="https://bit.ly/openu-bot-add-link"))
        markup.add(types.InlineKeyboardButton("🔍 לחיפוש חדש", callback_data="cb_start"))
        bot.send_message(chat_id, "לא קיים לינק לקבוצה", reply_markup=markup)
        return

    for link in data['data']:
        print_link(bot, chat_id, link, course)

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔍 לחיפוש לינק חדש", callback_data="cb_start"))
    markup.add(types.InlineKeyboardButton("🤖 לעמוד הפייסבוק", url="https://bit.ly/openu-bot-facebook"))
    bot.send_message(chat_id, divider, reply_markup=markup)


# end process_course_id_step #