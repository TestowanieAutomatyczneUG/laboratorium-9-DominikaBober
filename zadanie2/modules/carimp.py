from .car import Car
import math

class CarImpl:

	def __init__(self, starting_place):
		self.car = Car()
		self.warnings = {
			"fuel": self.car.needsFuel(),
			"temperature": True if self.car.getEngineTemperature() > 140 else False,
		}
		self.current_place = starting_place

	def driveTo(self, destination):
		distance = math.sqrt((self.current_place[0]-destination[0])**2+(self.current_place[1]-destination[1])**2)
		self.car.driveTo(distance)
		self.current_place = destination
		return distance

	# def getWarnings(self):
	# 	return self.warnings 
