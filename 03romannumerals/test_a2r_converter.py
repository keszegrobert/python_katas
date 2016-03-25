from a2r_converter import ArabicToRomanConverter
from unittest import TestCase

class TestArabicToRomanConverter(TestCase):
	def setUp(self):
		self.converter = ArabicToRomanConverter()

	def check_0_to_9(self,add,prefix):
		self.check_equals_roman(add+0,prefix+'')
		self.check_equals_roman(add+1,prefix+'I')
		self.check_equals_roman(add+2,prefix+'II')
		self.check_equals_roman(add+3,prefix+'III')
		self.check_equals_roman(add+4,prefix+'IV')
		self.check_equals_roman(add+5,prefix+'V')
		self.check_equals_roman(add+6,prefix+'VI')
		self.check_equals_roman(add+7,prefix+'VII')
		self.check_equals_roman(add+8,prefix+'VIII')
		self.check_equals_roman(add+9,prefix+'IX')

	def test_0(self):
		self.check_0_to_9(0,'')
		self.check_0_to_9(10,'X')
		self.check_0_to_9(20,'XX')
		self.check_0_to_9(30,'XXX')
		self.check_0_to_9(40,'XL')
		self.check_0_to_9(50,'L')
		self.check_0_to_9(60,'LX')
		self.check_0_to_9(70,'LXX')
		self.check_0_to_9(80,'LXXX')
		self.check_0_to_9(90,'XC')

	def check_equals_roman(self,arabic,roman):
		result = self.converter.convert(arabic)
		self.assertEqual(result,roman)

if __name__ == '__main__':
	unittest.main()
