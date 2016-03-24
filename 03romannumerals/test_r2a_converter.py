from unittest import TestCase 
from r2a_converter import RomanToArabicConverter

class TestRomanToArabicConverter(TestCase):
	def setUp(self):
		self.converter = RomanToArabicConverter()

	def test_i_is_one(self):
		self.check_equality('I',1)

	def test_ii_is_two(self):
		self.check_equality('II',2)

	def test_iv_is_four(self):
		self.check_equality('IV',4)

	def test_iii_is_three(self):
		self.check_equality('III',3)

	def test_iiv_is_invalid(self):
		self.check_invalidity('IIV')

	def test_ivi_is_invalid(self):
		self.check_invalidity('IVI')

	def test_ivi_is_invalid(self):
		self.check_invalidity('IVV')

	def test_iiii_is_four(self):
		self.check_equality('IIII',4)

	def test_iiiv_is_invalid(self):
		self.check_invalidity('IIIV')

	def test_iiiiv_is_invalid(self):
		self.check_invalidity('IIIIV')

	def test_v_is_five(self):
		self.check_equality('V',5)

	def test_vi_is_six(self):
		self.check_equality('VI',6)

	def test_vv_is_invalid(self):
		self.check_invalidity('VV')

	def test_vii_is_seven(self):
		self.check_equality('VII',7)

	def test_viv_is_invalid(self):
		self.check_invalidity('VIV')

	def test_viii_is_eight(self):
		self.check_equality('VIII',8)

	def test_viiv_is_invalid(self):
		self.check_invalidity('VIIV')

	def test_viiiv_is_invalid(self):
		self.check_invalidity('VIIIV')

	def test_viiii_is_invalid(self):
		self.check_invalidity('VIIII')

	def check_equality(self,roman,arabic):
		converted = self.converter.convert(roman)
		self.assertTrue(self.converter.is_valid())
		self.assertEquals(converted,arabic)

	def check_invalidity(self,roman):
		self.converter.convert(roman)
		self.assertFalse(self.converter.is_valid())

if __name__ == '__main__':
	unittest.main()
