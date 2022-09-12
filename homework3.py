#1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# def sum(a = []):
#     sum = 0
#     i = 1
#     while i < len(a):
#         sum = sum + a[i]
#         i += 2
#     return sum
# print(sum([2, 3, 5, 9, 3]))

#2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# def couples(a = []):
#     i = 0
#     e = 1
#     s = []
#     while i < len(a)/2:
#         s.append(a[i]*a[len(a)-e])
#         i += 1
#         e += 1
#     return s
# print(couples([2, 3, 5, 6]))

#3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# def difference(a = []):
#     i = 0
#     s = []
#     while i < len(a):
#         b = int(a[i])
#         s.append(round(a[i] - b,2))
#         i += 1
#     print(s)
#     k = 0
#     while k < len(s):
#         if s[k] == 0:
#             del s[k]
#         k += 1
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
# print(difference([1.1, 1.2, 3.1, 5, 10.01]))

# #4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# def binary(num):
#     result = str()
#     while num > 0:
#         a = num % 2
#         num = num // 2
#         b = str(a)
#         result = b + result
#     return result
# print(binary(2))

#5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# def fibonacci(k):
#     a = [1, 0, 1]
#     e = -4
#     while e >= -k-2:
#         a.insert(0,a[e+2] - a[e+1])
#         e -= 1
#     i = k+2
#     while i <= k*2:
#         a.append(a[i-2] + a[i-1])
#         i += 1
#     return a
# print(fibonacci(8))