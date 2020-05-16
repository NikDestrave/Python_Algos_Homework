"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import random
import timeit
num = int(input('Введите число элементов: '))
arr = [random.uniform(0, 50) for _ in range(num)]

def merge_sort(numbers):
    if len(numbers) > 1:
        center = len(numbers) // 2
        left = numbers[:center]
        right = numbers[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1
        return numbers

print(f'Исходный - {arr}')
print(f'Отсортированный - {merge_sort(arr[:])}')

'''
Результаты:
Введите число элементов: 6
Исходный - [35.44475566882875, 40.69918323126722, 25.273015318214348, 45.95347935762806, 21.163442748307926, 43.98730926610661]
Отсортированный - [21.163442748307926, 25.273015318214348, 35.44475566882875, 40.69918323126722, 43.98730926610661, 45.95347935762806]
'''