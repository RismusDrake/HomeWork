'''Четвёртое задание. Создайте класс Triangle с методом area, подсчитывающим и 
возвращающим площадь треугольника. Затем создайте объект Triangle,
вызовите в нем area и выведите результат'''



class Triangle:
	def __init__(self,o,v):
		self.osnovanie = o
		self.visota = v
	def area(self):
		return 1/2 * self.osnovanie * self.visota
	print('Создано')
S = Triangle(10, 25)
print(S)
print(S.osnovanie)
print(S.visota)
area = 1/2 * S.osnovanie * S.visota
print(area)



'''#Другой способ
class Triangle:
	def __init__(self,o,v):
		self.osnovanie = o
		self.visota = v
	def area(Triangle):
		return Triangle == 1/2 * self.osnovanie * self.visota
S = Triangle(input('Основание треугольника: '), input('Высота треугольника: '))
print(S)
print(S.osnovanie)
print(S.visota)
print(Triangle)'''