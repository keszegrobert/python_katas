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
