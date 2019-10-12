'''Пятое задание. Извлечь все слова, начинающиеся на гласную'''


import re

result = re.findall(r'\b[aeiouAEIOU]\w+', 'lorem ipsum dolor sit ametist')
print(result)
