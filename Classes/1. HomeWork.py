'''Пеовле задание. Определите класс Apple с четырьмя переменными экземпляра,
представляющими четыре свойства яблока'''



class Apple:
	def __init__(self,w,c,t,d):
		self.weight = w
		self.color = c
		self.temp = t
		self.day = d
	print('Создано')
ap = Apple(int(input('Вес яблока: ')), int(input('Цвет яблока: ')), 
int(input('Температура яблока: ')), int(input('Сколько дней яблоку: ')))
print(ap)
print(ap.weight)
print(ap.color)
print(ap.temp)
print(ap.day)