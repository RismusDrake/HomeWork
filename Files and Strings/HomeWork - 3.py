'''Третье задание. Вернуть список доменов из списка адресов
электронной почты.'''



import re

result = re.findall(r'@(\w+\S+)','123123@321.ru sauyuawhj@maih.com jhsgjsal@gmail.ri')
print(result)
