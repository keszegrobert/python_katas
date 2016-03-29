from unittest import TestCase
from database import DBTable
from database import DBError

class TestSelect(TestCase):
	def setUp(self):
		self.table = DBTable()
		self.table.alter({'name':'name','type':'varchar','size':100})
		self.table.alter({'name':'age','type':'int','size':4})
		self.table.insert({'name':'Adam','age':28})
		self.table.insert({'name':'Eve','age':25})

	def test_select_star(self):
		res = self.table.select(('','*'),True)
		self.assertEqual(res,[{'name':'Adam','age':28},{'name':'Eve','age':25}])

	def test_select_only_name(self):
		res = self.table.select(('','name'),True)
		self.assertEqual(res,[{'name':'Adam'},{'name':'Eve'}])

	def test_select_minimum_of_age(self):
		res = self.table.select(('MIN','age'),True)
		self.assertEqual(res,25)

	def test_select_maximum_of_age(self):
		res = self.table.select(('MAX','age'),True)
		self.assertEqual(res,28)

	def test_select_count_of_star(self):
		res = self.table.select(('COUNT','*'),True)
		self.assertEqual(res,2)

	def test_select_count_of_all(self):
		res = self.table.select(('COUNT',['name','age']),True)
		self.assertEqual(res,2)