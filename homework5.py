#1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"". 
#(Не поняла как поменять кодировку файла, чтобы на русском данные корректно записывались, поэтому сделала на английском)
# f = open('textfile.txt', 'w')
# f.write("abc kjnlk; absklj; lkjl;lok jkhklabcbbknn")
# f = open('textfile.txt', 'r')
# line = f.readline()
# line = " ".join(filter(lambda x: "abc" not in x, line.split()))
# f = open('textfile.txt', 'w')
# f.write(line)
# f.close()

#2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента? 
# - Первый игрок должен взять 20 конфет, а потом каждый ход соперника добивать до 29 конфет за круг.
# candy = 2021
# count = 0
# while candy > 0:
#     a = input('Введите кол-во конфет, которые хотите забрать:')
#     if a.isdigit():
#         a = int(a)
#         if 0 < a < 29 and a <= candy:
#             candy = candy - a
#             count +=1
#         else:
#             print('Введено некорретное значение')
#             continue
#     else:
#         print('Введено некорретное значение')
#         continue
#     print(count)
# if count % 2 == 0:
#     print('Выиграл второй игрок')
# else:
#     print('Выиграл первый игрок')

# a) Добавьте игру против бота. Достаточно сделать так, чтобы бот не брал конфет больше положенного или больше чем имеется в куче.
# from random import randint
# candy = 2021
# count = 0
# while candy > 0:
#     if count % 2 == 0:
#         a = input('Введите кол-во конфет, которые хотите забрать:')
#         if a.isdigit():
#             a = int(a)
#             if 0 < a < 29 and a <= candy:
#                 candy = candy - a
#             else:
#                 print('Введено некорретное значение')
#                 continue
#         else:
#             print('Введено некорретное значение')
#             continue
#     else:
#         if candy < 28:
#             candy = candy - randint(1, candy)
#         else:
#             candy = candy - randint(1, 28)
#     count +=1
# if count % 2 == 0:
#     print('Выиграл бот')
# else:
#     print('Выиграл игрок')

# b) Подумайте как наделить бота ""интеллектом"". 
# Напоминаю, если перед пользователем будет лежать 29 конфет, то он, однозначно, проиграет. Достаточно довести игру до такой ситуации.
# from random import randint
# candy = 2021
# count = 0
# candy = candy - 20
# count = 1
# while candy > 0:
#     if count % 2 != 0:
#         a = input('Введите кол-во конфет, которые хотите забрать:')
#         if a.isdigit():
#             a = int(a)
#             if 0 < a < 29 and a <= candy:
#                 candy = candy - a
#             else:
#                 print('Введено некорретное значение')
#                 continue
#         else:
#             print('Введено некорретное значение')
#             continue
#     else:
#         candy = candy - (29 - a)
#     count +=1
# if count % 2 == 0:
#     print('Выиграл игрок')
# else:
#     print('Выиграл бот')

#3. Создайте программу для игры в ""Крестики-нолики"".
# a = dict()
# a[1, 1] = ' '
# a[1, 2] = ' '
# a[1, 3] = ' '
# a[2, 1] = ' '
# a[2, 2] = ' '
# a[2, 3] = ' '
# a[3, 1] = ' '
# a[3, 2] = ' '
# a[3, 3] = ' '
# i = 1
# while i < 10:
#     line = int(input('Введите строку: '))
#     column = int(input('Введите столбец: '))
#     if 0 < line < 4 and 0 < column < 4:
#         if a[line, column] != 'x' and a[line, column] != '0':
#             if i % 2 != 0:
#                 a[line,column] = 'x'
#             else:
#                 a[line,column] = '0'
#             print(str(a[1, 1]) + " | " + str(a[1, 2]) + " | " + str(a[1, 3]))
#             print('----------')
#             print(str(a[2, 1]) + " | " + str(a[2, 2]) + " | " + str(a[2, 3]))
#             print('----------')
#             print(str(a[3, 1]) + " | " + str(a[3, 2]) + " | " + str(a[3, 3]))
#         else:
#             print('"Эта клетка уже занята"')
#             continue
#     else:
#         print('Введено некорретное значение')
#         continue
#     if a[1, 1] == a[1, 2] == a[1, 3] == 'x' or\
#        a[2, 1] == a[2, 2] == a[2, 3] == 'x' or\
#        a[3, 1] == a[3, 2] == a[3, 3] == 'x' or\
#        a[1, 1] == a[2, 1] == a[3, 1] == 'x' or\
#        a[1, 2] == a[2, 2] == a[3, 2] == 'x' or\
#        a[1, 3] == a[2, 3] == a[3, 3] == 'x' or\
#        a[1, 1] == a[2, 2] == a[3, 3] == 'x' or\
#        a[1, 3] == a[2, 2] == a[3, 1] == 'x':
#         print('Победил первый игрок')
#         break
#     if a[1, 1] == a[1, 2] == a[1, 3] == '0' or\
#        a[2, 1] == a[2, 2] == a[2, 3] == '0' or\
#        a[3, 1] == a[3, 2] == a[3, 3] == '0' or\
#        a[1, 1] == a[2, 1] == a[3, 1] == '0' or\
#        a[1, 2] == a[2, 2] == a[3, 2] == '0' or\
#        a[1, 3] == a[2, 3] == a[3, 3] == '0' or\
#        a[1, 1] == a[2, 2] == a[3, 3] == '0' or\
#        a[1, 3] == a[2, 2] == a[3, 1] == '0':
#         print('Победил второй игрок')
#         break
#     i += 1

#4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# def compression(line):
#     count = 1
#     line_fin = ''
#     for i in range(len(line)-1):
#         if line[i] == line[i + 1]:
#             count += 1
#         else:
#             line_fin = line_fin + str(count) + str(line[i])
#             count = 1
#     line_fin = line_fin + str(count) + str(line[i])
#     return line_fin
# def recovery(line):
#     count = 1
#     line_fin = ''
#     for e in range(len(line)-1):
#         if line[e].isdigit():
#             count = int(line[e])
#         while count > 0:
#             line_fin = line_fin + line[e + 1]
#             count -= 1
#         e +=2
#     return line_fin
# f = open('rlefile.txt', 'w')
# f.write("aaaaagghhhffffffttt")
# f = open('rlefile.txt', 'r')
# line = f.readline()
# f = open('rlefile.txt', 'w')
# f.write(compression(line))
# f.close()
# f = open('rlefile.txt', 'r')
# line = f.readline()
# f = open('rlefile.txt', 'w')
# f.write(recovery(line))
# f.close()