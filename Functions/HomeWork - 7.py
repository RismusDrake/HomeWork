'''Седьмое задание. Использовать функцию map и filter'''



n = [10,20,30,40,50]							#Создание переменной
def ten(x):										#Создание функции
	return x//10								#Возвращение функции
n = list(map(ten,n))							#Использование функции map
print(n)										#Вывод результата



n = [10,20,30,40,50,60,70,80,90,100]			#Создание переменной
def check(x):									#Создание функции
	return x > 10								#Возвращение функции
n = list(filter(check,n))						#Использование функции filter
print(n)										#Вывод результата