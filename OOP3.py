

class Animal:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def make_sound(self):
		print('привет')
		# raise NotImplementedError


class Cat(Animal):
	def __init__(self, name, age):
		self.name = name
		self.age = age

class Dog(Animal):
	def make_sound(self):
		print('rrr')


class Parrot(Animal):
	pass
			

animal1 = Animal('муму', 5)
animal1.make_sound()

dog1 = Dog('муму', 5)
dog1.make_sound()

parrot1 = Parrot('муму', 5)
parrot1.make_sound()