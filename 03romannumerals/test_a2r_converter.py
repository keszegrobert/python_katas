from a2r_converter import ArabicToRomanConverter
from unittest import TestCase

class TestArabicToRomanConverter(TestCase):
	def setUp(self):
		self.converter = ArabicToRomanConverter()

	def test_0(self):
		self.check_equals_roman(0,'')
		self.check_equals_roman(1,'I')
		self.check_equals_roman(2,'II')
		self.check_equals_roman(3,'III')
		self.check_equals_roman(4,'IV')
		self.check_equals_roman(5,'V')
		self.check_equals_roman(6,'VI')
		self.check_equals_roman(7,'VII')
		self.check_equals_roman(8,'VIII')
		self.check_equals_roman(9,'IX')
		self.check_equals_roman(10,'X')
		self.check_equals_roman(11,'XI')
		self.check_equals_roman(12,'XII')
		self.check_equals_roman(13,'XIII')

	def check_equals_roman(self,arabic,roman):
		result = self.converter.convert(arabic)
		self.assertEqual(result,roman)

if __name__ == '__main__':
	unittest.main()
