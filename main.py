from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from cred import token
from key_buttons import tele_button , button , nazad
from menu import main_menu_keyboard , course_menu_keyboard

def record(update: Update, context: CallbackContext):
    text = update.message.text
    if text[:6] == 'Запись':
        print(text)
        context.bot.send_message(
            chat_id='-886822325',
            text=text
        )
        
    if text[:6] == 'запись':
        print(text)
        context.bot.send_message(
            chat_id='-886822325',
            text=text
        )    

def on_click(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="""
1. напишате сооющение "Запись: " и ваше ФИО.
2. ваш номер телефона.
3.выберите удобное вам время.
        """
    )

def start(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id = update.effective_chat.id,
        sticker = 'CAACAgIAAxkBAAEGbXdjc3m2rb2qhj0bY_3s1LKmOs_2SwACDwADwDZPEwXo1IXy1A6fKwQ'
    )
    update.message.reply_text(
        f"Добро Пожаловать {update.effective_user.username}" ,
        reply_markup = main_menu_keyboard()
    )

ABOUT = tele_button[0]
COURSE_MENU = tele_button[1]
WE = tele_button[2]
NAZAD = nazad[0]
PYTHON = button[0]
JS = button[1]
UX = button[2]
RECORD = button[3]

def resive_curse_menu (update: Update, context: CallbackContext):
    update.message.reply_text(
        'Выберите курс',
        reply_markup=course_menu_keyboard()
    ) 

def about (update: Update, context: CallbackContext):
    update.message.reply_text(
        'Выберите куasdaaaaaaaadasdasdasdasdasfahthtsthрс',
        reply_markup=main_menu_keyboard()
    )

def naza (update: Update, context: CallbackContext):
    update.message.reply_text(
        'ВЫ сделали ход назад ',
        reply_markup=main_menu_keyboard()
    )

def location(update: Update, context: CallbackContext):
    msg = context.bot.send_message(
        update.effective_chat.id,
        text = 'Location of OGOGO'
    )
    
    update.message.reply_location(
        #42.87374567176816, 74.61999399202698
        longitude=74.61999399202698,
        latitude=42.87374567176816,
        reply_to_message_id=msg.message_id

    )


def python_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
    [
        InlineKeyboardButton('Mentor', callback_data='python_mentor'),
        InlineKeyboardButton('Lesson', callback_data='pytohn_lesson'),
    ],
    [InlineKeyboardButton('Price', callback_data='python_price')]
    ,
    [InlineKeyboardButton('Назад', callback_data='python_back')]
    ]
    reply_murkup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите опцию Python',
        reply_markup=reply_murkup
    )

def button(update: Update, context: CallbackContext):
    keyboard = [
    [
        InlineKeyboardButton('Mentor', callback_data='python_mentor'),
        InlineKeyboardButton('Lesson', callback_data='pytohn_lesson'),
    ],
    [InlineKeyboardButton('Price', callback_data='python_price')]
    ,
    [InlineKeyboardButton('Назад', callback_data='python_back')]
    ]
    reply_murkup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    if query.data == 'python_mentor':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/ili.jpg', 'rb'),
            caption = """
name: Ilias
age: 16
expierence: 6 years
work place: Google, Microsoft, Facebook, Oazis
            """,
        reply_markup=reply_murkup
        )

    if query.data == 'python_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = "Price PY: 16000 som per month",
            reply_markup=reply_murkup
            )
    if query.data == 'pytohn_lesson':
        context.bot.send_message(
            update.effective_chat.id,
            text = "Lessons PY:  5/7 -- 3/24  15:30-18:30",
            reply_markup=reply_murkup
            )
    keyboard = [
    [
        InlineKeyboardButton('Mentor', callback_data='js_mentor'),
        InlineKeyboardButton('Lesson', callback_data='js_lesson'),
    ],
    [InlineKeyboardButton('Price', callback_data='js_price')]    
    ]
    reply_murkup = InlineKeyboardMarkup(keyboard)
    if query.data == 'js_mentor':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/js.jpg', 'rb'),
            caption = """
name: Ilias js
age: 26
expierence: 16 years
work place: Google, Microsoft, Facebook, Oazis
            """,
            reply_markup=reply_murkup
        )

    if query.data == 'js_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = "Price js: 16000 som per month",
            reply_markup=reply_murkup
            )
    if query.data == 'js_lesson':
        context.bot.send_message(
            update.effective_chat.id,
            text = "Lessons js:  5/7 -- 3/24  18:30-21:30",
            reply_markup=reply_murkup
            )

####
    keyboard = [
    [
        InlineKeyboardButton('Mentor', callback_data='ux_mentor'),
        InlineKeyboardButton('Lesson', callback_data='ux_lesson'),
    ],
    [InlineKeyboardButton('Price', callback_data='ux_price')]    
    ]
    reply_murkup = InlineKeyboardMarkup(keyboard)
    if query.data == 'ux_mentor':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/ux.jpg', 'rb'),
            caption = """
name: Koro UX
age: 36
expierence: 23 years
work place: Google, Microsoft, Facebook, Oazis
            """,
            reply_markup=reply_murkup
        )

    if query.data == 'ux_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = "Price ux: 16000 som per month",
            reply_markup=reply_murkup
            )
    if query.data == 'ux_lesson':
        context.bot.send_message(
            update.effective_chat.id,
            text = "Lessons ux:  5/7 -- 3/24  12:30-15:30",
            reply_markup=reply_murkup
            )


def js_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
    [
        InlineKeyboardButton('Mentor', callback_data='js_mentor'),
        InlineKeyboardButton('Lesson', callback_data='js_lesson'),
    ],
    [InlineKeyboardButton('Price', callback_data='js_price')]    
    ]
    reply_murkup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите опцию JS',
        reply_markup=reply_murkup
    )  


def ux_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
    [
        InlineKeyboardButton('Mentor', callback_data='ux_mentor'),
        InlineKeyboardButton('Lesson', callback_data='ux_lesson'),
    ],
    [InlineKeyboardButton('Price', callback_data='ux_price')]    
    ]
    reply_murkup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите опцию UX',
        reply_markup=reply_murkup
    )  


updater = Updater(token , persistence=PicklePersistence (filename='bod_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSE_MENU),
    resive_curse_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ABOUT),
    about
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(NAZAD),
    naza
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PYTHON),
    python_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JS),
    js_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(UX),
    ux_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(WE),
    location
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(RECORD),
    on_click
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.text,
    record
))



updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()
updater.idle() 