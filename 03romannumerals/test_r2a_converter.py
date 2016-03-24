from unittest import TestCase 
from r2a_converter import RomanToArabicConverter

class TestRomanToArabicConverter(TestCase):
	def setUp(self):
		self.converter = RomanToArabicConverter()

	def test_i_is_one(self):
		arabic = self.convert('I')
		self.assertTrue(arabic == 1)

	def test_ii_is_two(self):
		arabic = self.convert('II')
		self.assertTrue(arabic == 2)

	def test_iii_is_three(self):
		arabic = self.convert('III')
		self.assertTrue(arabic == 3)

	def test_iiii_is_four(self):
		arabic = self.convert('IIII')
		self.assertTrue(arabic == 4)

	def convert(self,roman):
		return self.converter.convert(roman)

if __name__ == '__main__':
	unittest.main()