'''Второе задание. Вернуть два символа каждого слова.'''



import re

result = re.findall(r'\b\w\w','345 123 189')
print(result)
