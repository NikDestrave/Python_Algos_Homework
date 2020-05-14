"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

import random
import statistics

num = int(input('Введите число: '))
numbers = [random.randint(-100, 100) for _ in range(2 * num + 1)]


def median(nums):
    half = len(nums) // 2
    nums.sort()
    print(f'Отсортированный список: {numbers}')
    if not len(nums) % 2:
        return (nums[half - 1] + nums[half]) / 2
    return nums[half]


print(f'Исходный массив: {numbers}')
print(f'Медиана: {median(numbers)}')
print(f'Медиана через модуль Statistics: {statistics.median(numbers)}')

'''
Результаты:
Введите число: 5
Исходный массив: [59, 57, 6, 86, 45, -51, 40, -54, -30, 83, 88]
Отсортированный список: [-54, -51, -30, 6, 40, 45, 57, 59, 83, 86, 88]
Медиана: 45
Медиана через модуль Statistics: 45
'''