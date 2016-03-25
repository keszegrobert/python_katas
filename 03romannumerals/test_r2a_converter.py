from unittest import TestCase 
from r2a_converter import RomanToArabicConverter

class TestRomanToArabicConverter(TestCase):
	def setUp(self):
		self.converter = RomanToArabicConverter()

	def check_0_to_9(self,prefix,add):
		self.check_equality(prefix+'',add+0)

		self.check_equality(prefix+'I',add+1)

		self.check_equality(prefix+'II',add+2)
		self.check_invalidity(prefix+'IIV')
		self.check_invalidity(prefix+'IIX')
		self.check_invalidity(prefix+'IIL')
		self.check_invalidity(prefix+'IIC')
		self.check_invalidity(prefix+'IID')
		self.check_invalidity(prefix+'IIM')

		self.check_equality(prefix+'III',add+3)
		self.check_invalidity(prefix+'IIIV')
		self.check_invalidity(prefix+'IIIX')
		self.check_invalidity(prefix+'IIIL')
		self.check_invalidity(prefix+'IIIC')
		self.check_invalidity(prefix+'IIID')
		self.check_invalidity(prefix+'IIIM')

		self.check_equality(prefix+'IIII',add+4)
		self.check_invalidity(prefix+'IIIII')
		self.check_invalidity(prefix+'IIIIV')
		self.check_invalidity(prefix+'IIIIX')
		self.check_invalidity(prefix+'IIIIL')
		self.check_invalidity(prefix+'IIIIC')
		self.check_invalidity(prefix+'IIIID')
		self.check_invalidity(prefix+'IIIIM')

		self.check_equality(prefix+'IV',add+4)
		self.check_invalidity(prefix+'IVI')
		self.check_invalidity(prefix+'IVV')
		self.check_invalidity(prefix+'IVX')
		self.check_invalidity(prefix+'IVL')
		self.check_invalidity(prefix+'IVC')
		self.check_invalidity(prefix+'IVD')
		self.check_invalidity(prefix+'IVM')

		self.check_equality(prefix+'V',add+5)
		self.check_invalidity(prefix+'VV')
		self.check_invalidity(prefix+'VX')
		self.check_invalidity(prefix+'VL')
		self.check_invalidity(prefix+'VC')
		self.check_invalidity(prefix+'VD')
		self.check_invalidity(prefix+'VM')

		self.check_equality(prefix+'VI',add+6)
		self.check_invalidity(prefix+'VIV')
		self.check_invalidity(prefix+'VIX')
		self.check_invalidity(prefix+'VIL')
		self.check_invalidity(prefix+'VIC')
		self.check_invalidity(prefix+'VID')
		self.check_invalidity(prefix+'VIM')

		self.check_equality(prefix+'VII',add+7)
		self.check_invalidity(prefix+'VIIV')
		self.check_invalidity(prefix+'VIIX')
		self.check_invalidity(prefix+'VIIL')
		self.check_invalidity(prefix+'VIIC')
		self.check_invalidity(prefix+'VIID')
		self.check_invalidity(prefix+'VIIM')

		self.check_equality(prefix+'VIII',add+8)
		self.check_invalidity(prefix+'VIIII')
		self.check_invalidity(prefix+'VIIIV')
		self.check_invalidity(prefix+'VIIIX')
		self.check_invalidity(prefix+'VIIIL')
		self.check_invalidity(prefix+'VIIIC')
		self.check_invalidity(prefix+'VIIID')
		self.check_invalidity(prefix+'VIIIM')

		self.check_equality(prefix+'IX',add+9)
		self.check_invalidity(prefix+'IXI')
		self.check_invalidity(prefix+'IXV')
		self.check_invalidity(prefix+'IXX')
		self.check_invalidity(prefix+'IXL')
		self.check_invalidity(prefix+'IXC')
		self.check_invalidity(prefix+'IXD')
		self.check_invalidity(prefix+'IXM')

	def check_0_to_99(self,prefix,add):
		self.check_0_to_9(prefix+'',add+0)
		self.check_0_to_9(prefix+'X',add+10)
		self.check_0_to_9(prefix+'XX',add+20)
		self.check_0_to_9(prefix+'XXX',add+30)
		self.check_0_to_9(prefix+'XXXX',add+40)
		self.check_0_to_9(prefix+'XL',add+40)
		self.check_0_to_9(prefix+'L',add+50)
		self.check_0_to_9(prefix+'LX',add+60)
		self.check_0_to_9(prefix+'LXX',add+70)
		self.check_0_to_9(prefix+'LXXX',add+80)
		self.check_0_to_9(prefix+'XC',add+90)

	def check_0_to_999(self,prefix,add):
		self.check_0_to_99(prefix+'',add+0)
		self.check_0_to_99(prefix+'C',add+100)
		self.check_0_to_99(prefix+'CC',add+200)
		self.check_0_to_99(prefix+'CCC',add+300)
		self.check_0_to_99(prefix+'CCCC',add+400)
		self.check_0_to_99(prefix+'CD',add+400)
		self.check_0_to_99(prefix+'D',add+500)
		self.check_0_to_99(prefix+'DC',add+600)
		self.check_0_to_99(prefix+'DCC',add+700)
		self.check_0_to_99(prefix+'DCCC',add+800)
		self.check_0_to_99(prefix+'CM',add+900)

	def test_0_to_999(self):
		self.check_0_to_999('',0)

	def check_equality(self,roman,arabic):
		converted = self.converter.convert(roman)
		self.assertTrue(self.converter.is_valid())
		self.assertEquals(converted,arabic)

	def check_invalidity(self,roman):
		self.converter.convert(roman)
		self.assertFalse(self.converter.is_valid())

if __name__ == '__main__':
	unittest.main()
