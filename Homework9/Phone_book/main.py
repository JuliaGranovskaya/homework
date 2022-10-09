# bot https://t.me/gb_phone_book_bot

import telebot

TOKEN = 

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands = ['start'])
def answer(msg: telebot.types.Message):
    bot.send_message(chat_id = msg.from_user.id, text = f'Выберите действие:\n'
                                                         '/view - просмотр справочника\n'
                                                         '/add - добавление записи\n'
                                                         '/export - экспорт справочника в файл\n'
                                                         '/import - импорт справочника из файла\n')


@bot.message_handler(commands = ['view'])
def view(msg: telebot.types.Message):
    with open('Homework9/Phone_book/base.csv', 'rb') as file:
        for line in file:
            bot.send_message(chat_id = msg.from_user.id, text = line)


@bot.message_handler(commands = ['add'])
def surname(msg: telebot.types.Message):
    bot.send_message(chat_id = msg.from_user.id, text = 'Введите фамилию')
    bot.register_next_step_handler(msg, name)


def name(msg: telebot.types.Message):
    surname = msg.text
    with open('Homework9/Phone_book/base.csv', 'a') as file:
        file.write('{}, '.format(surname))
    bot.send_message(chat_id = msg.from_user.id, text = 'Введите имя')
    bot.register_next_step_handler(msg, telephone)


def telephone(msg: telebot.types.Message):
    name = msg.text
    with open('Homework9/Phone_book/base.csv', 'a') as file:
        file.write('{}, '.format(name))
    bot.send_message(chat_id = msg.from_user.id, text = 'Введите номер телефона')
    bot.register_next_step_handler(msg, comment)


def comment(msg: telebot.types.Message):
    telephone = msg.text
    with open('Homework9/Phone_book/base.csv', 'a') as file:
        file.write('{}, '.format(telephone))
    bot.send_message(chat_id = msg.from_user.id, text = 'Введите коментарий')
    bot.register_next_step_handler(msg, add)


def add(msg: telebot.types.Message):
    comment = msg.text
    with open('Homework9/Phone_book/base.csv', 'a') as file:
        file.write('{}\n'.format(comment))
    bot.send_message(chat_id = msg.from_user.id, text = 'Данные внесены в справочник')


@bot.message_handler(commands = ['import'])
def request_file(msg: telebot.types.Message):
    bot.send_message(chat_id = msg.from_user.id, text = 'Отправьте файл, из которого вы ходите импортировать данные')


@bot.message_handler(content_types=['document'])
def import_file(msg: telebot.types.Message):
    file = bot.get_file(msg.document.file_id)
    downloaded_file = bot.download_file(file.file_path)
    with open(msg.document.file_name, 'wb') as import_data:
        import_data.write(downloaded_file)
    bot.send_message(chat_id = msg.from_user.id, text = 'Какой формат записи вы использовали?\n'
                                                        '1 - Через запятую\n'
                                                        '2 - Построчно\n')
    bot.register_next_step_handler(msg, save)


def save(msg: telebot.types.Message):
    format = msg.text
    if format == '1':
        lines = ''
        with open('import_data.txt', 'r') as file:
            for line in file:
                lines = lines + line
        with open('Homework9/Phone_book/base.csv', 'a') as base:
            base.write(lines + '\n')
        bot.send_message(chat_id = msg.from_user.id, text = 'Данные внесены в справочник')
    elif format == '2':
        lines = ''
        with open('import_data.txt', 'r') as file:
            for line in file:
                if line == '\n':
                    lines = lines + '\n'
                else:
                    lines = lines + line.replace('\n', ', ')
        with open('Homework9/Phone_book/base.csv', 'a') as base:
            base.write(lines + '\n')
        bot.send_message(chat_id = msg.from_user.id, text = 'Данные внесены в справочник')
    else:
        bot.send_message(chat_id = msg.from_user.id, text = 'Введено некорректное значение')


@bot.message_handler(commands = ['export'])
def type(msg: telebot.types.Message):
    bot.send_message(chat_id = msg.from_user.id, text = 'В каком формате вы хотите получить данные?\n'
                                                        '1- Через запятую\n'
                                                        '2 - Построчно\n')
    bot.register_next_step_handler(msg, export)


def export(msg: telebot.types.Message):
    format = msg.text
    if format == '1':
        lines = ''
        with open('Homework9/Phone_book/base.csv', 'r') as base:
            for line in base:
                lines = lines + line
        with open('export_data.txt', 'w') as file:
            file.write(lines)
        bot.send_document(chat_id=msg.from_user.id, document=open('export_data.txt', 'rb'))
    elif format == '2':
        lines = ''
        with open('Homework9/Phone_book/base.csv', 'r') as base:
            for line in base:
                lines = lines + '\n' + line.replace(', ', '\n')
        with open('export_data.txt', 'w') as file:
            file.write(lines)
        bot.send_document(chat_id=msg.from_user.id, document=open('export_data.txt', 'rb'))
    else:
        bot.send_message(chat_id = msg.from_user.id, text = 'Введено некорректное значение')


bot.polling()
