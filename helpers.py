from urllib.parse import quote
from telebot import types


def send_keyboard(bot, message, text, options):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1)
    markup.add(*options)
    msg = bot.reply_to(message, text, reply_markup=markup)

    return msg


def print_link(bot, chat_id, link, course):
    url = link['url']
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(
        "לדיווח על הלינק",
        url=f"https://docs.google.com/forms/d/e/1FAIpQLSeCUwFK-6XcPS3VpSLlu5_thrg5PQXMx_j2dKGuMbKQRtaIYQ/viewform?usp=pp_url\
            &entry.2005620554={course.courseId}\
            &entry.1045781291={course.year}\
            &entry.1065046570={quote(course.semester)}\
            &entry.1166974658={url}")
    )
    # fix passing semester query fix
    bot.send_message(chat_id, url, reply_markup=markup)
