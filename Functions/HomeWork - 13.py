'''Тринадцатое задание. Список [16, -17, 2, 78.7, False, False, 
{‘True’: True}, 555, 12, 23, 42, ‘DD’] Функция, принимает на вход 
список -выбирает из него все int и float -составить из него новый 
список, отсортированный от наименьшего значения большему'''



spisok = [16, -17, 2, 78.7, False, False, {'True': True}, 555, 12, 23, 42, 'DD']		#Создание переменных
def filt1(int1): 																		#Создание функции
	spisok_new = [ 
	s 
	for s in int1																		#Создание цикла for 
		if type(s) in [int,float]] 
	spisok_new.sort() 
	return spisok_new 
print(filt1(spisok))																	#Вывод результата