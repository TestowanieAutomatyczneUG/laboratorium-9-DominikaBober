from modules.checker import Checker
from unittest.mock import Mock
import unittest
from pandas import to_datetime

class Test_Checker(unittest.TestCase):
	def setUp(self):
		self.checker = Checker()

	def test_remainder_after_17(self):
		self.checker.clock.getTime = Mock(name = "getTime")
		self.checker.clock.getTime.return_value = to_datetime("2021-10-01 18:00:00")
		self.assertTrue(self.checker.remainder())
		
	def test_remainder_before_17(self):
		self.checker.clock.getTime = Mock(name = "getTime")
		self.checker.clock.getTime.return_value = to_datetime("2021-10-01 08:00:00")
		self.assertFalse(self.checker.remainder())

unittest.main()