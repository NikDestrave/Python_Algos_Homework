"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

from random import randint
from timeit import timeit


def bubble_sort(array):
    array_len = len(array)
    count = 0
    while count < array_len:
        for i in range(array_len - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        count += 1
    return array


def bubble_sort_mod(array):
    array_len = len(array)
    count = 0
    while count < array_len:
        is_sorted = True
        for i in range(array_len - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
        if is_sorted:
            break
        count += 1
    return array


numbers = [randint(-100, 100) for _ in range(40)]
print(numbers)
print(bubble_sort(numbers))

time = timeit(f'bubble_sort({numbers})', setup='from __main__ import bubble_sort', number=10000)

numbers = [randint(-100, 100) for _ in range(40)]
print(f'\n{numbers}')
print(bubble_sort_mod(numbers))

time2 = timeit(f'bubble_sort_mod({numbers})', setup='from __main__ import bubble_sort_mod', number=10000)

print(f'\nПузырьковая сортировка: {round(time, 3)} сек')
print(f'Улучшенный вариант сортировки: {round(time2, 3)} сек')

'''
Результаты:
[-10, -53, -50, -54, -72, 47, 49, 28, 5, -26, 9, 68, 9, 61, -32, -16, -84, -18, -11, -70, -25, 17, 72, 76, 80, 76, -92, -18, 17, 24, 8, 55, 62, -23, -57, 22, 84, -5, -99, -47]
[84, 80, 76, 76, 72, 68, 62, 61, 55, 49, 47, 28, 24, 22, 17, 17, 9, 9, 8, 5, -5, -10, -11, -16, -18, -18, -23, -25, -26, -32, -47, -50, -53, -54, -57, -70, -72, -84, -92, -99]

[38, 56, 39, -38, 32, -90, -51, -72, -11, -63, -7, -92, 7, 12, -90, 56, -3, -71, 72, -81, 79, 22, -88, 29, -40, 34, -28, 44, -17, 51, 72, 26, 60, 72, -81, 41, -69, -98, -66, 18]
[79, 72, 72, 72, 60, 56, 56, 51, 44, 41, 39, 38, 34, 32, 29, 26, 22, 18, 12, 7, -3, -7, -11, -17, -28, -38, -40, -51, -63, -66, -69, -71, -72, -81, -81, -88, -90, -90, -92, -98]

Пузырьковая сортировка: 2.011 сек
Улучшенный вариант сортировки: 0.052 сек
'''