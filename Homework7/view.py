import controller


def menu():
    do = 1
    while True:
        print('Меню:\n'
              '1 - Просмотр справочника\n'
              '2 - Добавление записи\n'
              '3 - Экспорт справочника\n'
              '4 - Импорт справочника\n'
              '5 - Выход\n')
        do = int(input('Введите порядковый номер действия: '))
        if do == 1:
            controller.view_data()
        elif do == 2:
            controller.get_info()
        elif do == 3:
            controller.export_lines()
        elif do == 4:
            controller.import_lines()
        elif do == 5:
            break
        else:
            print('Введено некорректное значение')
