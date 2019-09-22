#Третье задание
'''Посчитать сумму числового ряда от 0 до 14 включительно. 
Например, 0+1+2+3+…+14'''



'''#Создание переменных
number0 = 0
number1 = 1
number2 = 2
number3 = 3
number4 = 4
number5 = 5
number6 = 6
number7 = 7
number8 = 8
number9 = 9
number10 = 10
number11= 11
number12 = 12
number13 = 13
number14 = 14
number15 = 105
#Создание суммы переменых и выведение результата
if number15 == number1 + number2 + number3 + number4 + number5 + number6 + number7 + number8 + number9 + number10 + number11 + number12 + number13 + number14:
	print('1+2+3+4+5+6+7+8+9+10+11+12+13+14=105. Сумма всех чисел равна 105')
else:
	print('no')'''



#Другой спобой
#Создание цикла от 0 до 14 и выведение результата
for number in range(0, 15):
	print(number)
#При помощи формулы определить сумму всех чисел от 0 до 14 и вывод результата
n=((number*1)/2)*15
print(n)