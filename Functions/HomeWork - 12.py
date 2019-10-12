'''Двенадцатое задание. Написать функцию date, принимающую 3 аргумента — 
день, месяц и год. Вернуть True, если такая дата есть в нашем календаре, 
и False иначе.'''


def date(year,month,day):											#Создание функции
	if year < 0:													#Создание условия
		return False
	elif year % 4 == 0:												#Создание проверки на високосный год
		if 1<=month<=12:
			if month == 2:
				if 1<=day<=29:
					return True
				else:
					return False
			elif month==4 or month==6 or month==9 or month==11:		#Месяца с 30-ю днями
				if 1<=day<=30:
					return True
				else:
					return False
			else:
				if 1<=day<=31:
					return True
				else:
					return False
		else:
			return False
	else:															#В случае, если год не високосный
		if 1<=month<=12:
			if month==2:
				if 1<=day<=28:
					return True
				else:
					return False
			elif month==4 or month==6 or month==9 or month==11:		#Месяца с 30-ю днями
				if 1<=day<=30:
					return True
				else:
					return False
			else:
				if 1<=day<=31:
					return True
				else:
					return False
		else:
			return False
year = int(input('Введите год = '))									#Вывод текста для года
month = int(input('Введите номер месяца = '))						#Вывод текста для месяца
day = int(input('Введите номер дня = '))							#Вывод текста для дня
print(date(year,month,day))											#Вывод результата