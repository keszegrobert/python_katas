from a2r_converter import ArabicToRomanConverter
from unittest import TestCase

class TestArabicToRomanConverter(TestCase):
	def setUp(self):
		self.converter = ArabicToRomanConverter()

	def test_0(self):
		roman = self.converter.convert(0)
		self.assertEqual(roman,'')

if __name__ == '__main__':
	unittest.main()
