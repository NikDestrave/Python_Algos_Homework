"""
Задание 9. Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).
Подсказка: можно добавить проверку, что введены равные числа
"""

NUMBER_A = int(input('Введите первое число: '))
NUMBER_B = int(input('Введите второе число: '))
NUMBER_C = int(input('Введите третье число: '))

if NUMBER_B < NUMBER_A < NUMBER_C or NUMBER_C < NUMBER_A < NUMBER_B:
    print(f'Среднее значение из трех: {NUMBER_A}')
elif NUMBER_A < NUMBER_B < NUMBER_C or NUMBER_C < NUMBER_B < NUMBER_A:
    print(f'Среднее значение из трех: {NUMBER_B}')
else:
    print(f'Среднее значение из трех: {NUMBER_C}')