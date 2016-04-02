from unittest import TestCase
from r2a_converter import RomanToArabicConverter
from a2r_converter import ArabicToRomanConverter


class TestConvert(TestCase):
	def setUp(self):
		self.r2a = RomanToArabicConverter()
		self.a2r = ArabicToRomanConverter()

	def test_0_to_10(self):
		for number in range(0,5000):
			roman = self.a2r.convert(number)
			arabic = self.r2a.convert(roman)
			self.assertEqual(arabic,number)
			roman2 = self.a2r.convert(arabic)
			self.assertEqual(roman,roman2)

if __name__ == '__main__':
	unittest.main()