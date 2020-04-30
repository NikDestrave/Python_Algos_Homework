"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.
Пример:
Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""

from random import random

height = 4
width = 3
arr = []
for i in range(width):
    arr_2 = []
    for j in range(height):
        num = int(random() * 40)
        arr_2.append(num)
        print('%4d' % num, end='')
    arr.append(arr_2)
    print()

max = -1
for j in range(height):
    min = 40
    for i in range(width):
        if arr[i][j] < min:
            min = arr[i][j]
    if min > max:
        max = min
print(f'Максимальное среди них = {max}')