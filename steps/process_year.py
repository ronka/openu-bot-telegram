from helpers import send_keyboard
from config import semester_list, course_dict, bot, year_list, flag

from steps.process_semester import process_semester_step


def process_year_step(message):
    global flag

    flag = True  # reset process name ajax flag

    try:
        chat_id = message.chat.id
        year = message.text

        if year not in year_list:
            raise Exception()

        course = course_dict[chat_id]
        course.year = year

        msg = send_keyboard(bot, message, 'איזה סמסטר?', semester_list.keys())
        bot.register_next_step_handler(msg, process_semester_step)
    except Exception as e:
        bot.reply_to(message, 'אופסס, שנה לא תקינה')

        msg = send_keyboard(bot, message, 'איזה שנה?', year_list)
        bot.register_next_step_handler(msg, process_year_step)
    # end exception #

# end process_year_step #
