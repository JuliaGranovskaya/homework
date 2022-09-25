#1. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# 
# def difference(a = []):
#     i = 0
#     s = []
#     while i < len(a):
#         b = int(a[i])
#         s.append(round(a[i] - b,2))
#         i += 1
#     print(s)
#     max = s[0]
#     e = 1
#     while e < len(s):
#         if s[e] > max:
#             max = s[e]
#         e += 1
#     min = s[0]
#     n = 1
#     while n < len(s):
#         if s[n] < min:
#             min = s[n]
#         n += 1
#     result = max - min
#     return result
# print(difference([1.1, 1.2, 3.1, 5.4, 10.01]))


# a = [1.1, 1.2, 3.1, 5.4, 10.01]
# s = [round(a[i] - int(a[i]),2) for i in range(len(a))]
# print(s)
# print(max(s) - min(s))


# 2. Для натурального n создать список, состоящий из элементов последовательности 3n + 1.
# 1, 4, 7, 10

# N = int(input('Введите количество значений: '))
# a = [1]
# for i in range(1, N):
#     a.append(3*i + 1)
# print(a)


# N = int(input('Введите количество значений: '))
# print([3 * i + 1 for i in range(0, N)])


#3. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# def couples(a = []):
#     i = 0
#     e = 1
#     s = []
#     while i < len(a)/2:
#         s.append(a[i]*a[len(a)-e])
#         i += 1
#         e += 1
#     return s
# print(couples([2, 3, 4, 5, 6]))


# a = [2, 3, 4, 5, 6]
# s = [a[i] * a[len(a) - i - 1] for i in range(0, int(len(a)/2 + 1))]
# print(s)


#4. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# num = float(input('Введите число: '))
# N = str(num)
# i = 0
# sum = 0
# while i < len(N):
#     if N[i].isdigit():
#         a = int(N[i])
#         sum = sum + a
#     i += 1
# print(sum)


# num = float(input('Введите число: '))
# print(sum(map(int, list(str(num).replace('.','')))))


