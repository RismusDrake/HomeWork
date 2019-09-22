#Второе задание
'''Даны три числа. Вывести на экран “yes”, 
если можно взять какие-то два из них и в сумме получить третье'''



'''#Создание трёх переменных
number1 = 8
number2 = 8
number3 = 16
#Создание цикла, при котором будет выводиться на экран 'yes' или 'no'
if number1 + number2 == number3:
	print('yes')
elif number2 + number3 == number1:
	print('yes')
elif number1 + number3 == number2:
	print('yes')
else:
	print('no')'''



'''#Почему-то не хочет работать (всегда пишет ответ 'no')
#Создание трёх переменных
number1 = int
print('number1')
number1 = input()
number2 = int
print('number2')
number2 = input()
number3 = int
print('number3')
number3 = input()
#Создание цикла, при котором будет выводиться на экран 'yes' или 'no'
if number1 + number2 == number3:
	print('yes')
elif number2 + number3 == number1:
	print('yes')
elif number1 + number3 == number2:
	print('yes')
else:
	print('no')'''



'''#Другой способ
#Создание трёх переменных
import random
number1 = random.randint(1,5)
number2 = random.randint(1,5)
number3 = random.randint(1,5)
#Создание цикла, при котором будет выводиться на экран 'yes' или 'no'
if number1 + number2 == number3:
	print('yes')
elif number2 + number3 == number1:
	print('yes')
elif number1 + number3 == number2:
	print('yes')
else:
	print('no')'''



#Третий способ
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
#Создание цикла, при котором будет выводиться на экран 'yes' или 'no'
if n['n1'] + n['n2'] == n['n3'] or n['n1'] + n['n3'] == n['n2'] or n['n2'] + n['n3'] == n['n1']:
	print('yes')
else:
	print('no')



'''#Четвертый способ
#Создание переменной
n = []
import random
n = random.randint(1,5)
for a in range(3):
	print(n)
#Создание цикла, при котором будет выводиться на экран 'yes' или 'no' (не хочет работать)
if n[0] + n[1] == n[2] or n[0] + n[2] == n[1] or n[2] + n[1] == n[0]:
	print('yes')
else:
	print('no')'''