from unittest import TestCase
from database import DBTable
from database import DBError
import copy

class TestTableUpdate(TestCase):
	def setUp(self):
		self.table = DBTable()
		self.table.alter({'name':'name','type':'varchar','size':100})
		self.table.alter({'name':'age','type':'int','size':4})
		self.table.insert({'name':'Adam','age':28})
		self.table.insert({'name':'Eve','age':25})
		self.before = copy.deepcopy(self.table.filter(True))

	def check_diff(self,expected):
		self.after = self.table.filter(True)
		diff = self.get_diff(self.before,self.after)
		self.assertEqual(expected,diff)

	def test_update_Eve(self):
		self.table.update(('EQ','name','Eve'),[('age',26)])
		self.check_diff([{}, {'age': (25, 26)}])

	def test_update_Eve_and_25_should_update_1_row(self):
		self.table.update(('AND',('EQ','name','Eve'),('EQ','age',25)),[('age',26)])
		self.check_diff([{}, {'age': (25, 26)}])

	def test_update_Eve_and_28_should_update_no_row(self):
		self.table.update(('AND',('EQ','name','Eve'),('EQ','age',28)),[('age',26)])
		self.check_diff([{},{}])

	def test_update_Eve_or_28_should_update_all_rows(self):
		self.table.update(('OR',('EQ','name','Eve'),('EQ','age',28)),[('age',26)])
		self.check_diff([{'age': (28, 26)}, {'age': (25, 26)}])

	def get_diff(self,before,after):
		diff = []
		for i in range(0,len(before)):
			row_before = before[i]
			row_after = after[i]
			row_diff = {}
			for key in row_before:
				if row_after[key] != row_before[key]:
					row_diff[key] = (row_before[key],row_after[key])
			diff.append(row_diff)
		return diff
