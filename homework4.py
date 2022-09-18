# 1 Вычислить число π c заданной точностью d
# n = 100
# my_pi = 0.0
# for i in range(n):
#     my_pi = my_pi + (1/16**i * (4/(8 * i + 1) - 2/(8 * i + 4) - 1/(8 * i + 5) - 1/(8 * i + 6)))
# print(my_pi)

# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# def factor(N):
#     a = []
#     k = 2
#     while N > 1:
#         if N % k == 0:
#             a.append(k)
#             N = N / k
#         else:
#             k += 1
#     return a
# print(factor(36))

# print(factor(20))

# 3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# def repeat(a):
#     i = 0
#     k = 1
#     s = []
#     while i < len(a):
#         while k < len(a):
#             if a[i] == a[k]:
#                 s.append(a[i])
#             k += 1
#         i += 1
#         k = i + 1
#     return s
# print(repeat([1, 2, 2, 3, 4, 4, 6]))

# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# from random import randrange
# k = 2
# a = randrange(0, 101)
# b = randrange(0, 101)
# c = randrange(0, 101)
# res = f'{a} * x**{k} + {b} * x + {c} = 0'
# print(res)
# data = open('file1.txt', 'w')
# data.writelines(res)
# data.close()

# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# f1 = open('file.txt', 'r')
# file1 = f1.readline()
# f2 = open('file1.txt', 'r')
# file2 = f2.readline()

# def get_ones(line):
#     tmp = []
#     last = 0
#     positive = True
#     for i, item in enumerate(line):
#         if item in {'+', '-'}:
#             if positive:
#                 tmp.append(line[last:i])
#             else:
#                 tmp.append('-' + line[last:i])
#             last = i + 1
#             positive = item == '+'
#     if positive:
#         tmp.append(line[last:])
#     else:
#         tmp.append('-' + line[last:])
#     return tmp

# def get_coef(one):
#     for i, item in enumerate(one):
#         if item == 'x':
#             return int(one[:i]), one[i:]
#     return int(one), None

# def sum(d1,d2):
#     f = open('file3.txt', 'w')
#     lst = ''
#     keys1 = []
#     keys2 = []
#     for index in d1.keys():
#         keys1.append(index)
#     for ind in d2.keys():
#         keys2.append(ind)
#     for i in keys1:
#         for k in keys2:
#             if i == k:
#                 lst = lst[:len(lst)] + ' + ' + str(d1[i] + d2[k]) + ' * ' + str(i)
#             # else:
#             #     lst = lst[:len(lst)] + ' + ' + str(d1[i]) + ' * ' + str(i)+ ' + ' + str(d1[i]) + ' * ' + str(i)
#     f.write(lst)
#     f.close()
#     return f

# lst1 = get_ones(file1.replace(' ', '').replace('*', ''))
# lst2 = get_ones(file2.replace(' ', '').replace('*', ''))

# dct1 = {item[1]: item[0] for item in map(get_coef, lst1)}
# dct2 = {item[1]: item[0] for item in map(get_coef, lst2)}

# print(dct1)
# print(dct2)

# sum(dct1, dct2)

# f1.close()
# f2.close()