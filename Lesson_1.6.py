"""
Задание 6. Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.
Пример:
Введите номер буквы: 4
Введёному номеру соответствует буква: d
Подсказка: используйте ф-ции chr() и ord()
"""

NUMBER_SYMBOL = int(input('Введите номер буквы: '))
NUMBER_SYMBOL = ord('a') + NUMBER_SYMBOL - 1
print(f'Введёному номеру соответствует буква: {chr(NUMBER_SYMBOL)}')