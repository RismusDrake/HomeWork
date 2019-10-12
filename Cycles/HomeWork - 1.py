#Первое задание
'''Даны три числа. Вывести на экран “yes”, 
если среди них есть одинаковые, иначе вывести “ERROR”'''



'''#Создание трёх переменных
number1 = ''
print('number1')
number1 = input()
number2 = ''
print('number2')
number2 = input()
number3 = ''
print('number3')
number3 = input()
#Создание цикла, при котором будет выводиться на экран 'yes' или 'ERROR'
if number1 == number2 or number2 == number3 or number1 == number3:
	print('yes')
else:
	print('ERROR')'''



'''#Можно и таким образом
#Создание трёх переменных
number1 = ''
print('number1')
number1 = input()
number2 = ''
print('number2')
number2 = input()
number3 = ''
print('number3')
number3 = input()
#Создание цикла, при котором будет выводиться на экран 'yes' или 'ERROR'
if number1 == number2:
	print('yes')
elif number2 == number3:
	print('yes')
elif number1 == number3:
	print('yes')
else:
	print('ERROR')'''



#Другой способ
#Создание переменной
import random
n = {
	'n1':random.randint(1,5),
	'n2':random.randint(1,5),
	'n3':random.randint(1,5),
}
#Выведение переменной
print(n['n1'])
print(n['n2'])
print(n['n3'])
#Создание цикла, при котором будет выводиться на экран 'yes' или 'ERROR'
if n['n1'] == n['n2'] or n['n1'] == n['n3'] or n['n2'] == n['n3']:
	print('yes')
else:
	print('ERROR')