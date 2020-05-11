"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

import sys
import random
from memory_profiler import profile

@profile
def find_idx():
    numbers = [random.randint(0, 200) for i in range(60000)]
    multiples_idx = [idx for idx, num in enumerate(numbers) if num % 2 == 0]

    print(numbers)
    print(f'Индексы четных элементов {multiples_idx}')
    print(sys.getrefcount(multiples_idx))

find_idx()

@profile
def replace_digits():
    numbers = [random.randint(0, 200) for i in range(60000)]

    num_min = min(numbers)
    num_max = max(numbers)

    idx_min = numbers.index(num_min)
    idx_max = numbers.index(num_max)

    replace_numbers = numbers[:]
    replace_numbers[idx_min], replace_numbers[idx_max] = replace_numbers[idx_max], replace_numbers[idx_min]
    print(numbers)
    print(replace_numbers)
    print(sys.getrefcount(replace_numbers))

replace_digits()

'''
Line #    Mem usage    Increment   Line Contents
================================================
    18     13.4 MiB     13.4 MiB   @profile
    19                             def find_idx():
    20     14.0 MiB      0.2 MiB       numbers = [random.randint(0, 200) for i in range(60000)]
    21     14.4 MiB      0.1 MiB       multiples_idx = [idx for idx, num in enumerate(numbers) if num % 2 == 0]
    22                             
    23     14.3 MiB      0.0 MiB       print(numbers)
    24     14.3 MiB      0.0 MiB       print('Индексы четных элементов,', multiples_idx)
    25     14.3 MiB      0.0 MiB       print(sys.getrefcount(multiples_idx))
    
Line #    Mem usage    Increment   Line Contents
================================================
    31     13.9 MiB     13.9 MiB   @profile
    32                             def replace_digits():
    33     14.2 MiB      0.0 MiB       numbers = [random.randint(0, 200) for i in range(60000)]
    34                             
    35     14.2 MiB      0.0 MiB       num_min = min(numbers)
    36     14.2 MiB      0.0 MiB       num_max = max(numbers)
    37                             
    38     14.2 MiB      0.0 MiB       idx_min = numbers.index(num_min)
    39     14.2 MiB      0.0 MiB       idx_max = numbers.index(num_max)
    40                             
    41     14.4 MiB      0.2 MiB       replace_numbers = numbers[:]
    42     14.4 MiB      0.0 MiB       replace_numbers[idx_min], replace_numbers[idx_max] = replace_numbers[idx_max], replace_numbers[idx_min]
    43     14.4 MiB      0.0 MiB       print(numbers)
    44     14.4 MiB      0.0 MiB       print(replace_numbers)
    45     14.4 MiB      0.0 MiB       print(sys.getrefcount(replace_numbers))
    
Обе программы не потребляют память, не увеличивают её.
Python 3.8
Windows 10 x64
'''