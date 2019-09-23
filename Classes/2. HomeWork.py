'''Второе задание. Создайте класс Circle с методом area, подсчитывающим и возвращающим площадь круга.
Затем создайте объект Circle, вызовите в нем метод area и выведите результат.
Воспользуйтесь функцией pi из встроенного в Python модуля math.'''



import math
class Circle:
	def __init__(self, r):
		self.radius = r
	def area(self):
		return self.radius * self.radius * math.pi
	print('Создано')
c = Circle(5)
print(c)
print(c.radius)
s = c.radius * c.radius * math.pi
print(s)