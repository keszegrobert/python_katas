from unittest import TestCase 
from r2a_converter import RomanToArabicConverter

class TestRomanToArabicConverter(TestCase):
	def setUp(self):
		self.converter = RomanToArabicConverter()

	def test_i_is_one(self):
		self.check_equality('I',1)

	def test_ii_is_two(self):
		self.check_equality('II',2)

	def test_iii_is_three(self):
		self.check_equality('III',3)

	def test_iiii_is_four(self):
		self.check_equality('IIII',4)

	def test_iv_is_four(self):
		self.check_equality('IV',4)

	def test_iiv_is_invalid(self):
		self.check_invalidity('IIV')

	def test_v_is_five(self):
		self.check_equality('V',5)

	def test_vi_is_six(self):
		self.check_equality('VI',6)

	def check_equality(self,roman,arabic):
		converted = self.converter.convert(roman)
		self.assertTrue(self.converter.is_valid())
		self.assertEquals(converted,arabic)

	def check_invalidity(self,roman):
		self.converter.convert(roman)
		self.assertFalse(self.converter.is_valid())

if __name__ == '__main__':
	unittest.main()
