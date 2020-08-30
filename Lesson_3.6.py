"""
Задание_6. В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
Подсказки:
1) берем первый минимальный и максимальный
2) не забудьте, что сначала может быть минимальный, потом максимальный
а может - наоборот. во всех этих случаях нужна корректная работа
Пример:
Введите количество элементов в массиве: 10
Массив: [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]
Сумма элементов между минимальным (6) и максимальным (88) элементами: 234
"""

from random import random

quantity = int(input('Введите количество элементов в массиве: '))
arr = [0] * quantity
for i in range(quantity):
    arr[i] = int(random() * 30)
print(f'Массив: {arr}')

min = 0
max = 0
for i in range(1, quantity):
    if arr[i] < arr[min]:
        min = i
    elif arr[i] > arr[max]:
        max = i

sum = 0
for i in range(min + 1, max):
    sum += arr[i]

print(f'Сумма элементов между минимальным ({arr[min]}) и максимальным ({arr[max]}) элементами: {sum}')