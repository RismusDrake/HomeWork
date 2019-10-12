'''Первое задание. Вернуть первое слово из строки.'''



import re

result = re.search(r'^\w+','3 1 123')
print(result)
