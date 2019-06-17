from abc import ABC, abstractmethod

class Shape(ABC):
	def __init__(self):
		print("\tA shape is the outline of an area or figure\n")
	def draw(self):
		print("\tNo sub-class is selected!!")

class Square(Shape):
	def __init__(self):
		pass
	def draw(self):
		print("This is a square!!")

class Ellispe(Shape):
	def __init__(self):
		pass
	def draw(self):
		print("This is and ellispe!!")

class rectangle(Shape):
	def __init__(self):
		pass
	def draw(self):
		super().draw()
		print("This a rectangle!!")
