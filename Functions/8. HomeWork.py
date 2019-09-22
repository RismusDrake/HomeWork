'''Создать чистую и нечистую функцию'''


#Создание чистой функции
def pure_function(a,b):						#Создание функции
	temp = a + 2*b							
	return temp / (2*a + b)					#Возвращение функции
print(pure_function)						#Вывод результата



#Создание нечистой функции
some_list = [1,2,3]							#Создание переменной
def impure(arg):							#Создание функции
	some_list.append(arg)					
print(some_list)							#Вывод результата