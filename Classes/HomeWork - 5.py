'''Пятое задание. Создайте классы Rectangle и Square с методом calculate_perimeter,
вычисляющим периметр фигур, которые эти классы представляют.
Создайте объекты Rectangle и Square вызовите в них этот метод.'''



class Rectangle():														#Создание отцовского класса Rectangle

	def __init__(self,a,b,c):											#Создание 3-х переменных
		self.stora = a
		self.storb = b
		self.storc = c

	def calculate_perimeter(self):										#Создание функции calculate_perimeter
		return self.stora + self.storb + self.storc
	print('Создано')													#Проверка

class Square(Rectangle):												#Создание дочернего класса Square

	def calculate_perimeter2(self):										#Создание функции calculate_perimeter2
		return self.stora + 2 * self.storb
	print('Создано')													#Проверка
																		#Вывод результата
p1 = Rectangle(int(input('Сторона a фигуры Rectangle = ')), 
	(int(input('Сторона b фигуры Rectangle = '))),
	(int(input('Сторона c фигуры Rectangle =  '))))
#print(p1)
print('Периметр фигуры Rectangle = ', p1.calculate_perimeter())
p2 = Square(int(input('Сторона a фигуры Square = ')), 
	(int(input('Сторона b и c фигуры Square = '))), 0)
print('Периметр фигуры Square = ', p2.calculate_perimeter2())
#print(p2)