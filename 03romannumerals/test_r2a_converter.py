from unittest import TestCase 
from r2a_converter import RomanToArabicConverter

class TestRomanToArabicConverter(TestCase):
	def setUp(self):
		self.converter = RomanToArabicConverter()

	def test_i_and_v(self):
		self.check_equality('',0)
		self.check_equality('I',1)
		self.check_equality('II',2)
		self.check_equality('IV',4)
		self.check_equality('III',3)
		self.check_invalidity('IIV')
		self.check_invalidity('IVI')
		self.check_invalidity('IVV')
		self.check_equality('IIII',4)
		self.check_invalidity('IIIV')
		self.check_invalidity('IIIIV')
		self.check_equality('V',5)
		self.check_equality('VI',6)
		self.check_invalidity('VV')
		self.check_equality('VII',7)
		self.check_invalidity('VIV')
		self.check_equality('VIII',8)
		self.check_invalidity('VIIV')
		self.check_invalidity('VIIIV')
		self.check_invalidity('VIIII')

	def test_i_and_x(self):
		self.check_equality('IX',9)
		self.check_invalidity('IIX')
		self.check_invalidity('IIIX')
		self.check_invalidity('IIIIX')
		self.check_equality('X',10)
		self.check_equality('XI',11)
		self.check_equality('XX',20)
		self.check_equality('XII',12)
		self.check_equality('XIX',19)
		self.check_equality('XIII',13)
		self.check_invalidity('XIIX')
		self.check_equality('XIIII',14)
		self.check_invalidity('XIIIX')
		self.check_invalidity('XIIIII')

	def check_equality(self,roman,arabic):
		converted = self.converter.convert(roman)
		self.assertTrue(self.converter.is_valid())
		self.assertEquals(converted,arabic)

	def check_invalidity(self,roman):
		self.converter.convert(roman)
		self.assertFalse(self.converter.is_valid())

if __name__ == '__main__':
	unittest.main()
