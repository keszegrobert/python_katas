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

	def check_0_to_99(self,add,prefix):
		self.check_0_to_9(add+0,prefix+'')
		self.check_0_to_9(add+10,prefix+'X')
		self.check_0_to_9(add+20,prefix+'XX')
		self.check_0_to_9(add+30,prefix+'XXX')
		self.check_0_to_9(add+40,prefix+'XL')
		self.check_0_to_9(add+50,prefix+'L')
		self.check_0_to_9(add+60,prefix+'LX')
		self.check_0_to_9(add+70,prefix+'LXX')
		self.check_0_to_9(add+80,prefix+'LXXX')
		self.check_0_to_9(add+90,prefix+'XC')

	def	check_0_to_999(self,add,prefix):
		self.check_0_to_99(add+0,prefix+'')
		self.check_0_to_99(add+100,prefix+'C')
		self.check_0_to_99(add+200,prefix+'CC')
		self.check_0_to_99(add+300,prefix+'CCC')
		self.check_0_to_99(add+400,prefix+'CD')
		self.check_0_to_99(add+500,prefix+'D')
		self.check_0_to_99(add+600,prefix+'DC')
		self.check_0_to_99(add+700,prefix+'DCC')
		self.check_0_to_99(add+800,prefix+'DCCC')
		self.check_0_to_99(add+900,prefix+'CM')

	def test_every_arabic_convertable_to_roman(self):
		self.check_0_to_999(0,'')
		self.check_0_to_999(1000,'M')
		self.check_0_to_999(2000,'MM')
		self.check_0_to_999(3000,'MMM')
		self.check_0_to_999(4000,'MMMM')

	def check_equals_roman(self,arabic,roman):
		result = self.converter.convert(arabic)
		self.assertEqual(result,roman)

if __name__ == '__main__':
	unittest.main()
