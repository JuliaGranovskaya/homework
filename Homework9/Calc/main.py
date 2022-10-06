# bot https://t.me/gb_calc_bot

import telebot
from datetime import datetime

TOKEN = '5797822942:AAGo1yPVnTYIBOS83ZxpS0PLHtx5-SVNris'

bot = telebot.TeleBot(TOKEN)
 
buttons1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons1.row(telebot.types.KeyboardButton('Комплексные'),
             telebot.types.KeyboardButton('Рациональные'))

 
buttons2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons2.row(telebot.types.KeyboardButton('+'),
             telebot.types.KeyboardButton('-'))
buttons2.row(telebot.types.KeyboardButton('*'),
             telebot.types.KeyboardButton('/'))


@bot.message_handler(commands = ['start'])
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id = msg.from_user.id, 
                     text='Здравствуйте!\nВыберите режим работы калькулятора',
                     reply_markup=buttons1)
    bot.register_next_step_handler(msg, action)
    logger(msg.from_user.id, msg.text, 'Здравствуйте!Выберите режим работы калькулятора')


def action(msg: telebot.types.Message):
    if msg.text == 'Комплексные':
        bot.register_next_step_handler(msg, complex_counter)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Выберите действие',
                         reply_markup=buttons2)
        logger(msg.from_user.id, msg.text, 'Выберите действие')
    elif msg.text == 'Рациональные':
        bot.register_next_step_handler(msg, rational_counter)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Выберите действие',
                         reply_markup=buttons2)
        logger(msg.from_user.id, msg.text, 'Выберите действие')
    else:
        bot.register_next_step_handler(msg, action)
        bot.send_message(chat_id=msg.from_user.id, text='Пожалуйста, используйте кнопки')
        bot.send_message(chat_id=msg.from_user.id, 
                         text='Выберите режим работы калькулятора',
                         reply_markup=buttons1)
        logger(msg.from_user.id, msg.text, 'Пожалуйста, используйте кнопки. Выберите режим работы калькулятора')


def rational_counter(msg: telebot.types.Message):
    if msg.text == '+':
        bot.send_message(chat_id = msg.from_user.id, text = 'Введите значения через пробел')
        bot.register_next_step_handler(msg, sum_rat)
        logger(msg.from_user.id, msg.text, 'Введите значения через пробел')
    elif msg.text == '-':
        bot.send_message(chat_id = msg.from_user.id, text = 'Введите значения через пробел')
        bot.register_next_step_handler(msg, sub_rat)
        logger(msg.from_user.id, msg.text, 'Введите значения через пробел')
    elif msg.text == '*':
        bot.send_message(chat_id = msg.from_user.id, text = 'Введите значения через пробел')
        bot.register_next_step_handler(msg, mult_rat)
        logger(msg.from_user.id, msg.text, 'Введите значения через пробел')
    elif msg.text == '/':
        bot.send_message(chat_id = msg.from_user.id, text = 'Введите значения через пробел')
        bot.register_next_step_handler(msg, div_rat)
        logger(msg.from_user.id, msg.text, 'Введите значения через пробел')
    else:
        bot.register_next_step_handler(msg, rational_counter)
        bot.send_message(chat_id=msg.from_user.id, text='Пожалуйста, используйте кнопки')
        bot.send_message(chat_id=msg.from_user.id, 
                         text='Выберите действие',
                         reply_markup=buttons2)
        logger(msg.from_user.id, msg.text, 'Пожалуйста, используйте кнопки. Выберите действие')


def sum_rat(msg: telebot.types.Message):
    message = msg.text
    items = message.split()
    x = float(items[0])
    y = float(items[1])
    result = x + y
    bot.send_message(chat_id = msg.from_user.id, text = result)
    logger(msg.from_user.id, msg.text, result)


def sub_rat(msg: telebot.types.Message):
    message = msg.text
    items = message.split()
    x = float(items[0])
    y = float(items[1])
    result = x - y
    bot.send_message(chat_id = msg.from_user.id, text = result)
    logger(msg.from_user.id, msg.text, result)


def mult_rat(msg: telebot.types.Message):
    message = msg.text
    items = message.split()
    x = float(items[0])
    y = float(items[1])
    result = x * y
    bot.send_message(chat_id = msg.from_user.id, text = result)
    logger(msg.from_user.id, msg.text, result)


def div_rat(msg: telebot.types.Message):
    message = msg.text
    items = message.split()
    x = float(items[0])
    y = float(items[1])
    result = x / y
    bot.send_message(chat_id = msg.from_user.id, text = result)
    logger(msg.from_user.id, msg.text, result)


def complex_counter(msg: telebot.types.Message):
    if msg.text == '+':
        bot.send_message(chat_id = msg.from_user.id, text = 'Введите значения через пробел')
        bot.register_next_step_handler(msg, sum_com)
        logger(msg.from_user.id, msg.text, 'Введите значения через пробел')
    elif msg.text == '-':
        bot.send_message(chat_id = msg.from_user.id, text = 'Введите значения через пробел')
        bot.register_next_step_handler(msg, sub_com)
        logger(msg.from_user.id, msg.text, 'Введите значения через пробел')
    elif msg.text == '*':
        bot.send_message(chat_id = msg.from_user.id, text = 'Введите значения через пробел')
        bot.register_next_step_handler(msg, mult_com)
        logger(msg.from_user.id, msg.text, 'Введите значения через пробел')
    elif msg.text == '/':
        bot.send_message(chat_id = msg.from_user.id, text = 'Введите значения через пробел')
        bot.register_next_step_handler(msg, div_com)
        logger(msg.from_user.id, msg.text, 'Введите значения через пробел')
    else:
        bot.register_next_step_handler(msg, rational_counter)
        bot.send_message(chat_id=msg.from_user.id, text='Пожалуйста, используйте кнопки')
        bot.send_message(chat_id=msg.from_user.id, 
                         text='Выберите дейтсвие',
                         reply_markup=buttons2)
        logger(msg.from_user.id, msg.text, 'Пожалуйста, используйте кнопки. Выберите действие')


def sum_com(msg: telebot.types.Message):
    message = msg.text
    items = message.split()
    x = complex(items[0])
    y = complex(items[1])
    result = x + y
    bot.send_message(chat_id = msg.from_user.id, text = result)
    logger(msg.from_user.id, msg.text, result)


def sub_com(msg: telebot.types.Message):
    message = msg.text
    items = message.split()
    x = complex(items[0])
    y = complex(items[1])
    result = x - y
    bot.send_message(chat_id = msg.from_user.id, text = result)
    logger(msg.from_user.id, msg.text, result)


def mult_com(msg: telebot.types.Message):
    message = msg.text
    items = message.split()
    x = complex(items[0])
    y = complex(items[1])
    result = x * y
    bot.send_message(chat_id = msg.from_user.id, text = result)
    logger(msg.from_user.id, msg.text, result)


def div_com(msg: telebot.types.Message):
    message = msg.text
    items = message.split()
    x = complex(items[0])
    y = complex(items[1])
    result = x / y
    bot.send_message(chat_id = msg.from_user.id, text = result)
    logger(msg.from_user.id, msg.text, result)


@bot.message_handler(commands=['log'])
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Лог программы\n')
    bot.send_document(chat_id=msg.from_user.id, document=open('Homework9/Calc/CalcBot.log', 'rb'))


def logger(chat_id, msg, text):
    dt_now = datetime.now()
    with open('Homework9/Phone_book/CalcBot.log', 'a') as file:
        file.write('{}, {}, {}, {}\n'
                   .format(dt_now, chat_id, msg, text))


bot.polling()