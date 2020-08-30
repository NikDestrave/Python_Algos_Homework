"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
Пример:
строка: рара
подстроки:
рар
ра
р
а
ар
ара
Итог: 6 подстрок
"""

import hashlib

user_str = input('Ваша строка: ').lower()
result = set()

for i in range(len(user_str)):
	for j in range(i,len(user_str)):
		result.add(hashlib.sha1(user_str[i:j].encode('utf-8')).hexdigest())

print(f'\n{result}')
print(f'Итог: {len(list(result))} подстрок(и)')

'''
Результат:
Ваша строка: рарара

{'da39a3ee5e6b4b0d3255bfef95601890afd80709', '51b4eac98af84251c4ea43be6cbb444dc0e2c450', '5a3b4bcf554007112bd227924c5d8d99b3bcdab6', 'f80f71869054bd31710c7d42c08bdc98d9315830', '328fe759105a6beaccd1ac29da9744017206f8ca', '33a538c43046679d1ae99e7cd282c12881e1bfd6', 'a0be2f63531a3a1d4577cc1fb2a1303519aee3a1', '114ce3b483544858924d5cff8412fb5bde359d3b', '2fbe2b4b61b24f46c5d8f85d5e032581f88912d7', 'ba063f2cac8074daf50970c43d950d84e4957a0c'}
Итог: 10 подстрок(и)
'''