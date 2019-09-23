'''Щестое задание. В классе Square определите метод change_size,
позволяющий передавать ему число, которое увеличивает или уменьшает
(если оно отрицательное) каждую сторону объекта Square на
соответствующее значение'''



class Square:
	def __init__(self, o, s):
		self.object = o
		self.storona = s
	def change_size(self):
		if o<0:
			return o == o - b * 2
		else:
			return o == o + b * 2
	print(change_size)
stor = Square(15, 10)
print(stor)
print(stor.object)
print(stor.storona)