from unittest import TestCase
from database import DBTable
from database import DBError

class TestTable(TestCase):
	def setUp(self):
		self.table = DBTable()
		self.table.alter({'name':'name','type':'varchar','size':100})
		self.table.alter({'name':'age','type':'int','size':4})
		self.table.insert({'name':'Adam','age':28})
		self.table.insert({'name':'Eve','age':25})

	def test_filter_true(self):
		res = self.table.filter(True)
		self.assertEqual(len(res),2)

	def test_filter_false(self):
		res = self.table.filter(False)
		self.assertEqual(len(res),0)

	def test_filter_name_is_Adam(self):
		res = self.table.filter(('EQ','name','Adam'))
		self.assertEqual(len(res),1)

	def test_filter_name_is_not_Adam(self):
		res = self.table.filter(('NE','name','Adam'))
		self.assertEqual(len(res),1)

	def test_filter_age_is_less_than_28(self):
		res = self.table.filter(('LT','age',28))
		self.assertEqual(len(res),1)

	def test_filter_age_is_greater_than_25(self):
		res = self.table.filter(('GT','age',25))
		self.assertEqual(len(res),1)

	def test_filter_age_is_greater_or_equal_than_25(self):
		res = self.table.filter(('GE','age',25))
		self.assertEqual(len(res),2)

	def test_filter_age_is_less_or_equal_than_28(self):
		res = self.table.filter(('LE','age',28))
		self.assertEqual(len(res),2)

	def test_filter_age_is_25_and_name_is_Eve(self):
		res = self.table.filter(('AND',('EQ','age',25),('EQ','name','Eve')))
		self.assertEqual(len(res),1)

