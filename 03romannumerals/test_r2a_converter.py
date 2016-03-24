from unittest import TestCase 
from r2a_converter import RomanToArabicConverter

class TestRomanToArabicConverter(TestCase):
	def setUp(self):
		self.converter = RomanToArabicConverter()

	def test_i_is_one(self):
		arabic = self.convert('I')
		self.assertEquals(arabic,1)
		self.assertTrue(self.converter.is_valid())

	def test_ii_is_two(self):
		arabic = self.convert('II')
		self.assertEquals(arabic,2)
		self.assertTrue(self.converter.is_valid())

	def test_iii_is_three(self):
		arabic = self.convert('III')
		self.assertEquals(arabic,3)
		self.assertTrue(self.converter.is_valid())

	def test_iiii_is_four(self):
		arabic = self.convert('IIII')
		self.assertEquals(arabic,4)
		self.assertTrue(self.converter.is_valid())

	def test_iv_is_four(self):
		arabic = self.convert('IV')
		self.assertEquals(arabic,4)
		self.assertTrue(self.converter.is_valid())

	def test_iiv_is_invalid(self):
		arabic = self.convert('IIV')
		self.assertFalse(self.converter.is_valid())

	def convert(self,roman):
		return self.converter.convert(roman)

if __name__ == '__main__':
	unittest.main()
