import telebot
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
filmbot = TeleBot("Your_Bot_Token")


def help_markup():
    help_m = InlineKeyboardMarkup()
    help_m.add(InlineKeyboardButton(
       text="How can I download the movie?",
       callback_data="question1"
    ))

@filmbot.messsge_handler(commands=["start"])
def start_bot_msg(message):
    filmbot.send_message(message.chat.id, f"""<b>Hi Dear <a href"tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>!
        <i>🍿 Kino Vaqti | Badiiy filmlar va oʻzbek kinolar...</i> You welcome to https://t.me/bf_wa_kanodol channel!
        🎬 Subscribe to our channel and start loading movies!</b>""", parse_mode="html", reply_markup=help_markup())

@filmbot.messsge_handler(cotent_types=["text"])
def download_movies(message):
    try:
        filmbot.send_video(message.chat.id, message.text)
    except:
        filmbot.send_message(message.chat.id, """<b>This link is invalid! ️\nPlease refer to the sample ✅</b>\n\n<i>Sample: https://t.me/bf_va_kinos/96</i>""", parse_mode="html")

@hilmbot.callback_query_handler()
def call(call):
    filmbot.edit_message_text(text="Go to our channel and send me a media link to me ✅", chat_id=call.message.chat.id, message_id=call.message.message_id)

filmbot.infinity_polling()
