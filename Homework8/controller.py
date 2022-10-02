import os


def get_surname():
    while True:
        surname = input('Введите фамилию: ')
        if surname.isalpha():
            return surname
        else:
            print('Введено некорректное значение')
            continue


def get_name():
    while True:
        name = input('Введите имя: ')
        if name.isalpha():
            return name
        else:
            print('Введено некорректное значение')
            continue


def get_telephone():
    while True:
        telephone = input('Введите номер телефона: ')
        if telephone.isnumeric():
            return telephone
        else:
            print('Введено некорректное значение')
            continue


def get_position():
    while True:
        position = input('Введите должность: ')
        if position.isalpha():
            return position
        else:
            print('Введено некорректное значение')
            continue


def get_salary():
    while True:
        salary = input('Введите зарплату: ')
        if salary.isnumeric():
            return salary
        else:
            print('Введено некорректное значение')
            continue


def get_status():
    while True:
        status = input('Введите статус (office or vacation): ')
        if status.isalpha():
            return status
        else:
            print('Введено некорректное значение')
            continue


def add_data():
    surname = get_surname()
    name = get_name()
    telephone = get_telephone()
    position = get_position()
    salary = get_salary()
    status = get_status()
    num = []
    with open('Homework8/employees.txt', 'r') as file:
        for line in file:
            data = line.split(', ')
            if data[0].isnumeric():
                num.append(data[0])
    id_ = int(num[- 1]) + 1
    with open('Homework8/employees.txt', 'a') as file:
        file.write('{}, {}, {}, {}, {}, {}, {}\n'.format(id_, surname, name, telephone, position, salary, status))


def view_data():
    with open('Homework8/employees.txt', 'r') as file:
        for line in file:
            print(line)


def edit_data():
    id_ = input('Введите id для редактирования данных: ')
    current = int(input('Что меняем (1 - Фамилия, 2 - Имя, 3 - Телефон, 4 - Должность, 5 - Зарплата, 6 - Статус): '))
    new = input('Введите новую запись: ')
    base = []
    with open('Homework8/employees.txt', 'r') as file:
        for line in file:
            base.append(line.split(', '))
    while id_ in base:
        with open('Homework8/employees.txt', 'r') as f1, open('Homework8/employees1.txt', 'w') as f2:
            for line in f1:
                if line.startswith(id_):
                    data = line.split(', ')
                    data[current] = new
                    new_line = ', '.join(data)
                    f2.write(new_line)
                else:
                    f2.write(line)
        os.remove('Homework8/employees.txt')
        os.rename('Homework8/employees1.txt', 'Homework8/employees.txt')
    else:
        print('Такого сотрудника нет')


def remove_data():
    id_ = input('Введите id сотрудника, которого хотите удалить: ')
    base = []
    with open('Homework8/employees.txt', 'r') as file:
        for line in file:
            base.append(line.split(', '))
    while id_ in base:
        with open('Homework8/employees.txt', 'r') as f1, open('Homework8/employees1.txt', 'w') as f2:
            for line in f1:
                if line.startswith(id_):
                    pass
                else:
                    f2.write(line)
        os.remove('Homework8/employees.txt')
        os.rename('Homework8/employees1.txt', 'Homework8/employees.txt')
    else:
        print('Такого сотрудника нет')


def report_status():
    status1 = 'office\n'
    status2 = 'vacation\n'
    count1 = 0
    count2 = 0
    with open('Homework8/employees.txt', 'r') as f1:
        for line in f1:
            data = line.split(', ')
            if data[6] == status1:
                count1 += 1
            elif data[6] == status2:
                count2 += 1
    print(f'{status1}: {count1}')
    print(f'{status2}: {count2}')


def report_salary():
    status1 = 'office\n'
    status2 = 'vacation\n'
    salary1 = 0
    salary2 = 0
    with open('Homework8/employees.txt', 'r') as f1:
        for line in f1:
            data = line.split(', ')
            if data[6] == status1:
                salary1 = salary1 + int(data[5])
            elif data[6] == status2:
                salary2 = salary2 + int(data[5])
    salary = salary1 + salary2
    print(f'{status1}: {salary1}')
    print(f'{status2}: {salary2}')
    print(f'Итого: {salary}')
