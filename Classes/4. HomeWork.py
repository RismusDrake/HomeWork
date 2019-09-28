'''Четвёртое задание. Создайте класс Triangle с методом area, подсчитывающим и 
возвращающим площадь треугольника. Затем создайте объект Triangle,
вызовите в нем area и выведите результат'''



class Triangle:													#Создание класса Triangle

	def __init__(self, o, v):									#Создание 2-е стороны фигур
		self.osnovanie = o
		self.visota = v

	def area(self):												#Создание функции area
		return 1/2 * self.osnovanie * self.visota
	print('Создано')

S = Triangle(int(input('Основание треугольника = ')),
	(int(input('Высота треугольника = '))))						#Вывод результата
#print(S)
print('Площадь треугольника = ', S.area())