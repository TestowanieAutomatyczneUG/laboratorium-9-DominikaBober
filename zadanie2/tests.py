from modules.car import Car
from modules.carimp import CarImpl
from mock import Mock, patch
import unittest


class Test_Car(unittest.TestCase):
	# def __init__(self):

	# def setUp(self):
	# 	print(CarImpl.needsFuel)
	# 	self.carImpl = CarImpl()
	@patch("modules.Car.getEngineTemperature")
	@patch("modules.Car.needsFuel")
	def test_needs_fuel(self, needsFuel, getEngineTemperature):
		needsFuel.return_value = True
		getEngineTemperature.return_value = 500
		carImpl = CarImpl((0,0))
		self.assertTrue(carImpl.warnings["fuel"])
	@patch("modules.Car.getEngineTemperature")
	@patch("modules.Car.needsFuel")
	def test_doesnt_needs_fuel(self, needsFuel, getEngineTemperature):
		needsFuel.return_value = False
		getEngineTemperature.return_value = 500
		carImpl = CarImpl((0,0))
		self.assertFalse(carImpl.warnings["fuel"])
	@patch("modules.Car.getEngineTemperature")
	@patch("modules.Car.needsFuel")
	def test_high_temperature(self, needsFuel, getEngineTemperature):
		needsFuel.return_value = False
		getEngineTemperature.return_value = 600
		carImpl = CarImpl((0,0))
		self.assertTrue(carImpl.warnings["temperature"])
	@patch("modules.Car.getEngineTemperature")	
	@patch("modules.Car.needsFuel")
	def test_low_temperature(self, needsFuel, getEngineTemperature):
		needsFuel.return_value = False
		getEngineTemperature.return_value = 20
		carImpl = CarImpl((0,0))
		self.assertFalse(carImpl.warnings["temperature"])
	@patch("modules.Car.getEngineTemperature")
	@patch("modules.Car.needsFuel")
	def test_drive(self, needsFuel, getEngineTemperature):
		needsFuel.return_value = False
		getEngineTemperature.return_value = 100
		carImpl = CarImpl((0,0))
		carImpl.driveTo((3,4))
		self.assertFalse(carImpl.current_place==(0,0))
	@patch("modules.Car.getEngineTemperature")
	@patch("modules.Car.needsFuel")
	def test_distance(self, needsFuel, getEngineTemperature):
		needsFuel.return_value = False
		getEngineTemperature.return_value = 100
		carImpl = CarImpl((0,0))
		distance = carImpl.driveTo((3,4))
		self.assertEqual(distance, 5)

unittest.main()