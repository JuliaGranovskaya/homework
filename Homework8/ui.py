import controller


def menu():
    while True:
        print('Меню:\n'
            '1 - Добавить\n'
            '2 - Удалить\n'
            '3 - Просмотреть\n'
            '4 - Редактировать\n'
            '5 - Отчет о статусе сотрудников\n'
            '6 - Отчет о зарплате по статусам\n'
            '7 - Выход\n')
        do = int(input('Выберите действие с данными: '))
        if do == 1:
            controller.add_data()
        elif do == 2:
            controller.remove_data()
        elif do == 3:
            controller.view_data()
        elif do == 4:
            controller.edit_data()
        elif do == 5:
            controller.report_status()
        elif do == 6:
            controller.report_salary()        
        elif do == 7:
            break
        else:
            print('Введена некорректная команда')    