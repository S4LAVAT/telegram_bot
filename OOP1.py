class Rectangel:
	def _init_(self, width, height):
		self.width = width
		self.height = height

	def area(self):
		print(self.width, self.height)



r1 = Rectangel(10, 20)
r2 = Rectangel(10, 200)
r1.area()
r2.area()
print(f"{r1.width}, {r2.height}")		