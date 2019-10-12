'''Четвертое задание. Извлечь дату из строки.'''



import re

result = re.findall(r'\d{2}-\d{2}-\d{4}', 'Allen 05-10-2015 08-04-1990 31-01-2013')
print(result)
