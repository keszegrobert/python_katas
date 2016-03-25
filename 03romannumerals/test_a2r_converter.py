from a2r_converter import ArabicToRomanConverter
from unittest import TestCase

class TestArabicToRomanConverter(TestCase):
	def setUp(self):
		self.converter = ArabicToRomanConverter()

	def test_0(self):
		self.check_equals_roman(0,'')

	def test_1(self):
		self.check_equals_roman(1,'I')

	def test_2(self):
		self.check_equals_roman(2,'II')

	def test_3(self):
		self.check_equals_roman(3,'III')

	def test_4(self):
		self.check_equals_roman(4,'IV')

	def test_5(self):
		self.check_equals_roman(5,'V')
	
	def test_6(self):
		self.check_equals_roman(6,'VI')

	def test_7(self):
		self.check_equals_roman(7,'VII')

	def test_8(self):
		self.check_equals_roman(8,'VIII')
	
	def check_equals_roman(self,arabic,roman):
		result = self.converter.convert(arabic)
		self.assertEqual(result,roman)

if __name__ == '__main__':
	unittest.main()
