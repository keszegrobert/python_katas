from unittest import TestCase 
from r2a_converter import RomanToArabicConverter

class TestRomanToArabicConverter(TestCase):
	def setUp(self):
		self.converter = RomanToArabicConverter()

	def test_i_is_one(self):
		arabic = self.converter.convert('I')
		self.assertTrue(arabic == 1)
		
if __name__ == '__main__':
	unittest.main()