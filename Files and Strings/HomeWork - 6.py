'''Шестое задание. Проверить телефонный номер (номер должен быть 
длиной 10 знаков и начинаться с 8 или 9)'''



import re

nomer = ['67947658725', '8957413585', '928-712-855']

for result in nomer:
	if re.match(r'[8-9]{1}[0-9]{9}', result) and len(result) == 10:
		print('yes')
	else:
		print('no')