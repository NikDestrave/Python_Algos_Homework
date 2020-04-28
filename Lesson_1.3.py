"""
Задание 3. По введенным пользователем координатам двух
точек вывести уравнение прямой, проходящей через эти точки.

Подсказка:
Запросите у пользователя значения координат X и Y для первой и второй точки
Найдите в учебнике по высшей математике формулы расчета:
k – угловой коэффициент (действительное число), b – свободный член (действительное число)
Сформируйте уравнение прямой по формуле: y = kx + b – функция общего вида

Пример:
X1_VAL = 2, Y1_VAL = 3, X2_VAL = 4, Y2_VAL = 5
Уравнение прямой, проходящей через эти точки: y = 1.0x + 1.0
"""
COOR_X1 = int(input('Введите значение координаты X1: '))
COOR_Y1 = int(input('Введите значение координаты Y1: '))
COOR_X2 = int(input('Введите значение координаты X2: '))
COOR_Y2 = int(input('Введите значение координаты Y2: '))

K = (COOR_Y1 - COOR_Y2) / (COOR_X1 - COOR_X2)
B = COOR_Y2 - K*COOR_X2

print(f'Уравнение прямой, проходящей через эти точки: y = {K}x + {B}')