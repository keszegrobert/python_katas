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

	def test_delete_Eve(self):
		self.table.delete(('EQ','name','Eve'))
		self.assertEqual(self.table.count_rows(),1)

	def test_delete_Eve_and_25_should_delete_1_row(self):
		self.table.delete(('AND',('EQ','name','Eve'),('EQ','age',25)))
		self.assertEqual(self.table.count_rows(),1)

	def test_delete_Eve_and_28_should_delete_no_row(self):
		self.table.delete(('AND',('EQ','name','Eve'),('EQ','age',28)))
		self.assertEqual(self.table.count_rows(),2)

	def test_delete_Eve_or_28_should_delete_all_rows(self):
		self.table.delete(('OR',('EQ','name','Eve'),('EQ','age',28)))
		self.assertEqual(self.table.count_rows(),0)