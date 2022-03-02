

# class Rectangle:
# 	def __init__(self, width, height):
# 		self.width = width
# 		self.height = height

# 	def area(self):
# 		print(self.width + self.height)



# r1 = Rectangle(10, 20)
# r2 = Rectangle(10, 200)
# r1.area()
# r2.area()
# print(f"{r1.width}, {r2.height}")		






# class Rectangel:
# 	def __init__(self, dog):
# 		self.dog = dog


# 	def area(self):
# 		print(self.dog,)



# r1 = Rectangel('SHARIK')
# r1.area()
# print(f"{r1.dog}")		




# class X:
# 	def __init__(self, arg):
# 	    self.arg = arg

# obj1 = X(10)
# print(obj1)  


# obj2 = X(2)	
# print(obj2)




class Car:
	def __init__(self, max_speed, petroleum):
		self.__max_speed = max_speed
		self.__petroleum = petroleum
		self.__current_speed = 0

	def current_speed(self):
		return self.__current_speed

	def decrease_speed(self, val):
		"""уменьшает скорость """
		if self.__current_speed - int(val)<0:
			raise ValueError('скорость не может быть меньше 0')
		elif int(val)<0:
			raise ValueError('значение не должно быть отрицательным')
		else:
			self.__current_speed-=int(val)

		return self.__current_speed



	def increase_speed(self, val):
		"""увеличивает скорость"""
		if self.__current_speed + int(val)>self.__max_speed:
			raise ValueError('привышено макс значение скорости')
		elif int(val)<0:
			raise ValueError('значение не должно быть отрицательным')
		else:
			self.__current_speed+=int(val)

		return self.__current_speed



# car1 = Car(200, 10)
# car1.increase_speed(2)

# print(car1.current_speed())
# car1.decrease_speed(1)
# print(car1.current_speed())





class Car:
	def __init__(self, max_speed, petroleum):
		self.__max_speed = max_speed
		self.__petroleum = petroleum
		self.__current_speed = 0

	def current_speed(self):
		return self.__current_speed


	def change_speed(self, val):
		"""увеличивает скорость"""
		result = self.__current_speed + int(val)
		if result>self.__max_speed or result < 0:
			raise ValueError('результат не может быть больше максимума и меньше нуля ')
		else:
			self.__current_speed+=int(val)

		return self.__current_speed





car1 = Car(200, 10)
car1.change_speed(2)

print(car1.current_speed())
car1.change_speed(-1)
print(car1.current_speed())






