def get_info():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    telephone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    add_note(surname, name, telephone, comment)


def add_note(surname, name, telephone, comment):
    with open('base.csv', 'a') as file:
        file.write('{}, {}, {}, {}\n'
                    .format(surname, name, telephone, comment))


def view_data():
    with open('base.csv', 'r') as file:
        for line in file:
            print(line)


def import_lines():
    name = input('Введите название файла: ')
    print('1 - Через запятую\n'
          '2 - Построчно\n')
    format = int(input('Какой формат записи вы использовали? '))
    if format == 1:
        lines = ''
        with open(name, 'r') as file:
            for line in file:
                lines = lines + line
        with open('base.csv', 'a') as base:
            base.write(lines + '\n')
    elif format == 2:
        lines = ''
        with open(name, 'r') as file:
            for line in file:
                if line == '\n':
                    lines = lines + '\n'
                else:
                    lines = lines + line.replace('\n', ', ')
        with open('base.csv', 'a') as base:
            base.write(lines + '\n')
    else:
        print('Введено некорректное значение')


def export_lines():
    print('1 - Через запятую\n'
          '2 - Построчно\n')
    format = int(input('В каком формате вы хотите получить данные? '))
    if format == 1:
        lines = ''
        with open('base.csv', 'r') as base:
            for line in base:
                lines = lines + line
        with open('export_lines.txt', 'w') as file:
            file.write(lines)
    elif format == 2:
        lines = ''
        with open('base.csv', 'r') as base:
            for line in base:
                lines = lines + '\n' + line.replace(', ', '\n')
        with open('export_lines.txt', 'w') as file:
            file.write(lines)
    else:
        print('Введено некорректное значение')