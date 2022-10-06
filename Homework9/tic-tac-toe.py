# Крестики-нолики
import emoji


a = dict()
a[1, 1] = ' '
a[1, 2] = ' '
a[1, 3] = ' '
a[2, 1] = ' '
a[2, 2] = ' '
a[2, 3] = ' '
a[3, 1] = ' '
a[3, 2] = ' '
a[3, 3] = ' '
i = 1
while i < 10:
    line = int(input(emoji.emojize(':small_blue_diamond: Введите строку: ')))
    column = int(input(emoji.emojize(':small_orange_diamond: Введите столбец: ')))
    if 0 < line < 4 and 0 < column < 4:
        if a[line, column] != emoji.emojize(':cross_mark:') and a[line, column] != emoji.emojize(':hollow_red_circle:'):
            if i % 2 != 0:
                a[line,column] = emoji.emojize(':cross_mark:')
            else:
                a[line,column] = emoji.emojize(':hollow_red_circle:')
            print(str(a[1, 1]) + "  |  " + str(a[1, 2]) + "  |  " + str(a[1, 3]))
            print('----------')
            print(str(a[2, 1]) + "  |  " + str(a[2, 2]) + "  |  " + str(a[2, 3]))
            print('----------')
            print(str(a[3, 1]) + "  |  " + str(a[3, 2]) + "  |  " + str(a[3, 3]))
        else:
            print(emoji.emojize('Эта клетка уже занята :prohibited:'))
            continue
    else:
        print(emoji.emojize('Введено некорретное значение :prohibited:'))
        continue
    if a[1, 1] == a[1, 2] == a[1, 3] == emoji.emojize(':cross_mark:') or\
       a[2, 1] == a[2, 2] == a[2, 3] == emoji.emojize(':cross_mark:') or\
       a[3, 1] == a[3, 2] == a[3, 3] == emoji.emojize(':cross_mark:') or\
       a[1, 1] == a[2, 1] == a[3, 1] == emoji.emojize(':cross_mark:') or\
       a[1, 2] == a[2, 2] == a[3, 2] == emoji.emojize(':cross_mark:') or\
       a[1, 3] == a[2, 3] == a[3, 3] == emoji.emojize(':cross_mark:') or\
       a[1, 1] == a[2, 2] == a[3, 3] == emoji.emojize(':cross_mark:') or\
       a[1, 3] == a[2, 2] == a[3, 1] == emoji.emojize(':cross_mark:'):
        print(emoji.emojize('Победил первый игрок :bottle_with_popping_cork:'))
        break
    if a[1, 1] == a[1, 2] == a[1, 3] == emoji.emojize(':hollow_red_circle:') or\
       a[2, 1] == a[2, 2] == a[2, 3] == emoji.emojize(':hollow_red_circle:') or\
       a[3, 1] == a[3, 2] == a[3, 3] == emoji.emojize(':hollow_red_circle:') or\
       a[1, 1] == a[2, 1] == a[3, 1] == emoji.emojize(':hollow_red_circle:') or\
       a[1, 2] == a[2, 2] == a[3, 2] == emoji.emojize(':hollow_red_circle:') or\
       a[1, 3] == a[2, 3] == a[3, 3] == emoji.emojize(':hollow_red_circle:') or\
       a[1, 1] == a[2, 2] == a[3, 3] == emoji.emojize(':hollow_red_circle:') or\
       a[1, 3] == a[2, 2] == a[3, 1] == emoji.emojize(':hollow_red_circle:'):
        print(emoji.emojize('Победил второй игрок :bottle_with_popping_cork:'))
        break
    i += 1