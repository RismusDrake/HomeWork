'''Щестое задание. В классе Square определите метод change_size,
позволяющий передавать ему число, которое увеличивает или уменьшает
(если оно отрицательное) каждую сторону объекта Square на
соответствующее значение'''



class Square:																				#Создание класса Square

	def __init__(self, o, n):																#Создание функции с 2-мя переменными
		self.object = o
		self.number = n

	def change_size(self):																	#Создание функции change_size
		if self.number < 0:
			return self.number
		else:
			return self.number
	print('Создано')																		#Проверка

stor = Square(int(input('Чему равны стороны объекта Square (см)? ')),
	(int(input('Введите число: '))))														#Задание параметров

#print(stor)																				#Вывод результата
print('Каждая сторона объекта Square была изменена на:', stor.change_size(), 'см')



'''Если интересно сколько сторон объекта Square
class Square:

	def __init__(self, o, n, s):
		self.object = o
		self.number = n
		self.storona = s

	def change_size(self):
		if self.number < 0:
			return self.object + self.storona * self.number
		else:
			return self.object + self.storona * self.number
	print('Создано')

stor = Square(int(input('Чему равны стороны объекта Square (см)? ')), 
	(int(input('Введите число: '))), 
	(int(input('Количество сторон объекта: '))))

#print(stor)
print(int(input('Каждая сторона объекта Square была изменена на:', stor.change_size(), 'см')))'''