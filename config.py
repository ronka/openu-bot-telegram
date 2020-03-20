import telebot
import os

from dotenv import load_dotenv
from flask import request, render_template, Flask

load_dotenv()

API_LINK = os.getenv('API_LINK')
API_COURSE = os.getenv('API_COURSE')
API_TOKEN = os.getenv('TOKEN_API')
ENV = os.getenv('ENV')

isLocal = ENV == 'local'

year_list = ['2020', '2019']
semester_list = {
    'ג': 'c',
    'ב': 'b',
    'א': 'a',
}
course_dict = {}
server = None
divider = "###############"

bot = telebot.TeleBot(API_TOKEN, threaded=False)

server = Flask(__name__, static_folder="build/static", template_folder="build")

if not isLocal:
    @server.route('/' + API_TOKEN, methods=['POST'])
    def get_message():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200


@server.route("/")
def home():
    return render_template("index.html")
