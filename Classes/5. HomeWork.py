'''Пятое задание. Создайте классы Rectangle и Square с методом calculate_perimeter,
вычисляющим периметр фигур, которые эти классы представляют.
Создайте объекты Rectangle и Square вызовите в них этот метод.'''



class Rectangle():
	def __init__(self,a,b,c):
		self.stora = a
		self.storb = b
		self.storc = c	
	def calculate_perimeter(self):
		return self.stora + self.storb + self.storc
	print('Создано')
class Square(Rectangle):
	def calculate_perimeter2(self):
		return self.stora + 2 * self.storb
	print('Создано')
p1 = Rectangle('Сторона a: 15', 'Сторона b: 10', 'Сторона c: 20')
print(p1)
print(p1.stora)
print(p1.storb)
print(p1.storc)
p2 = 15 + 10 + 20
print('Периметр треугольника = ', p2)
p3 = 15 + 10 * 2
print('Периметр равностороннего треугольника = ', p3)