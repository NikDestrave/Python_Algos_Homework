
"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

import timeit

user_number = int(input('Введите число для анализа: '))

def cycle(num):
    even = 0
    odd = 0
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    print(f'В числе {user_number} всего {even + odd} цифр(ы), из которых {even} чётных и {odd} нечётных')


def recur(num, even=0, odd=0):
    if num == 0:
        return even, odd
    else:
        n = num % 10
        num = num // 10
        if n % 2 == 0:
            even += 1
            return recur(num, even, odd)
        else:
            odd += 1
            return recur(num, even, odd)


def memorize(func):
    def wrapper(n, memory={}):
        value = memory.get(n)
        if value is None:
            value = func(n)
            memory[n] = value
        return value
    return wrapper


@memorize
def recur_2(num, even=0, odd=0):
    if num == 0:
        return even, odd
    else:
        n = num % 10
        num = num // 10
        if n % 2 == 0:
            even += 1
            return recur(num, even, odd)
        else:
            odd += 1
            return recur(num, even, odd)

cycle(user_number)
print(f'Результат рекурсии {recur(user_number)}')

start_time = timeit.default_timer()

print('\nИтоговые данные:')
result_time_1 = timeit.timeit("cycle", setup="from __main__ import cycle")
print(f'{"Время цикла:":30}{round(result_time_1, 5)} секунд(ы)')
result_time_2 = timeit.timeit("recur(user_number)", setup="from __main__ import recur, user_number")
print(f'{"Время рекурсии:":30}{round(result_time_2, 5)} секунд(ы)')
result_time_3 = timeit.timeit("recur_2(user_number)", setup="from __main__ import recur_2, user_number")
print(f'{"Время рекурсии с декоратором:":30}{round(result_time_3, 5)} секунд(ы)')

print(f'\nИтоговое время проверки: {round(timeit.default_timer() - start_time, 5)} секунд(ы)')

'''

Введите число для анализа: 15789
В числе 15789 всего 5 цифр(ы), из которых 1 чётных и 4 нечётных
Результат рекурсии (1, 4)

Итоговые данные:
Время цикла:                  0.01152 секунд(ы)
Время рекурсии:               1.51937 секунд(ы)
Время рекурсии с декоратором: 0.16735 секунд(ы)

Итоговое время проверки: 1.69988 секунд(ы)

-----------

Введите число для анализа: 15489765
В числе 15489765 всего 8 цифр(ы), из которых 3 чётных и 5 нечётных
Результат рекурсии (3, 5)

Итоговые данные:
Время цикла:                  0.01149 секунд(ы)
Время рекурсии:               2.49029 секунд(ы)
Время рекурсии с декоратором: 0.1646 секунд(ы)

Итоговое время проверки: 2.66809 секунд(ы)
 
--- Декоратор отрабатывает медленней цикла, но в разы быстрее рекурсии.
 
 '''