from unittest import TestCase 
from r2a_converter import RomanToArabicConverter

class TestRomanToArabicConverter(TestCase):
	def setUp(self):
		self.converter = RomanToArabicConverter()

if __name__ == '__main__':
	unittest.main()