from unittest import TestCase 
from r2a_converter import RomanToArabicConverter

class TestRomanToArabicConverter(TestCase):
	def setUp(self):
		self.converter = RomanToArabicConverter()

	def check_0_to_9(self,prefix,add):
		self.check_equality(prefix+'',add+0)

		self.check_equality(prefix+'I',add+1)
		self.check_invalidity(prefix+'IL')
		self.check_invalidity(prefix+'IC')
		self.check_invalidity(prefix+'ID')
		self.check_invalidity(prefix+'IM')

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
		self.check_invalidity(prefix+'XD')
		self.check_invalidity(prefix+'XM')

		self.check_0_to_9(prefix+'XX',add+20)
		self.check_invalidity(prefix+'XXL')
		self.check_invalidity(prefix+'XXC')
		self.check_invalidity(prefix+'XXD')
		self.check_invalidity(prefix+'XXM')

		self.check_0_to_9(prefix+'XXX',add+30)
		self.check_invalidity(prefix+'XXXL')
		self.check_invalidity(prefix+'XXXC')
		self.check_invalidity(prefix+'XXXD')
		self.check_invalidity(prefix+'XXXM')

		self.check_0_to_9(prefix+'XXXX',add+40)
		self.check_invalidity(prefix+'XXXXX')
		self.check_invalidity(prefix+'XXXXL')
		self.check_invalidity(prefix+'XXXXC')
		self.check_invalidity(prefix+'XXXXD')
		self.check_invalidity(prefix+'XXXXM')

		self.check_0_to_9(prefix+'XL',add+40)
		self.check_invalidity(prefix+'XLX')
		self.check_invalidity(prefix+'XLL')
		self.check_invalidity(prefix+'XLC')
		self.check_invalidity(prefix+'XLD')
		self.check_invalidity(prefix+'XLM')

		self.check_0_to_9(prefix+'L',add+50)
		self.check_invalidity(prefix+'LL')
		self.check_invalidity(prefix+'LC')
		self.check_invalidity(prefix+'LD')
		self.check_invalidity(prefix+'LM')

		self.check_0_to_9(prefix+'LX',add+60)
		self.check_invalidity(prefix+'LXL')
		self.check_invalidity(prefix+'LXC')
		self.check_invalidity(prefix+'LXD')
		self.check_invalidity(prefix+'LXM')

		self.check_0_to_9(prefix+'LXX',add+70)
		self.check_invalidity(prefix+'LXXL')
		self.check_invalidity(prefix+'LXXC')
		self.check_invalidity(prefix+'LXXD')
		self.check_invalidity(prefix+'LXXM')

		self.check_0_to_9(prefix+'LXXX',add+80)
		self.check_invalidity(prefix+'LXXXL')
		self.check_invalidity(prefix+'LXXXC')
		self.check_invalidity(prefix+'LXXXD')
		self.check_invalidity(prefix+'LXXXM')

		self.check_0_to_9(prefix+'XC',add+90)
		self.check_invalidity(prefix+'XCX')
		self.check_invalidity(prefix+'XCL')
		self.check_invalidity(prefix+'XCC')
		self.check_invalidity(prefix+'XCD')
		self.check_invalidity(prefix+'XCM')

	def check_0_to_999(self,prefix,add):
		self.check_0_to_99(prefix+'',add+0)
		self.check_0_to_99(prefix+'C',add+100)
		self.check_0_to_99(prefix+'CC',add+200)
		self.check_invalidity(prefix+'CCD')
		self.check_invalidity(prefix+'CCM')

		self.check_0_to_99(prefix+'CCC',add+300)
		self.check_invalidity(prefix+'CCCD')
		self.check_invalidity(prefix+'CCCM')

		self.check_0_to_99(prefix+'CCCC',add+400)
		self.check_invalidity(prefix+'CCCCC')
		self.check_invalidity(prefix+'CCCCD')
		self.check_invalidity(prefix+'CCCCM')

		self.check_0_to_99(prefix+'CD',add+400)
		self.check_invalidity(prefix+'CDC')
		self.check_invalidity(prefix+'CDD')
		self.check_invalidity(prefix+'CDM')

		self.check_0_to_99(prefix+'D',add+500)
		self.check_invalidity(prefix+'DD')
		self.check_invalidity(prefix+'DM')

		self.check_0_to_99(prefix+'DC',add+600)
		self.check_invalidity(prefix+'DCD')
		self.check_invalidity(prefix+'DCM')

		self.check_0_to_99(prefix+'DCC',add+700)
		self.check_invalidity(prefix+'DCCD')
		self.check_invalidity(prefix+'DCCM')

		self.check_0_to_99(prefix+'DCCC',add+800)
		self.check_invalidity(prefix+'DCCCD')
		self.check_invalidity(prefix+'DCCCM')

		self.check_0_to_99(prefix+'CM',add+900)
		self.check_invalidity(prefix+'CMC')
		self.check_invalidity(prefix+'CMD')
		self.check_invalidity(prefix+'CMM')

	def test_0_to_999(self):
		self.check_0_to_999('',0)
		self.check_0_to_999('M',1000)
		self.check_0_to_999('MM',2000)
		self.check_0_to_999('MMM',3000)
		self.check_0_to_999('MMMM',4000)
		self.check_invalidity('MMMMM')

	def check_equality(self,roman,arabic):
		converted = self.converter.convert(roman)
		self.assertTrue(self.converter.is_valid())
		self.assertEquals(converted,arabic)

	def check_invalidity(self,roman):
		self.converter.convert(roman)
		self.assertFalse(self.converter.is_valid())

if __name__ == '__main__':
	unittest.main()
