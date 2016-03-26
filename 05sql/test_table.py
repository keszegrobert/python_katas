from unittest import TestCase
from database import DBTable
from database import DBError

class TestTable(TestCase):
	def setUp(self):
		self.table = DBTable()

	def test_alter_table(self):
		self.table.alter({'name':'name','type':'varchar','size':100})
		
	def test_insert_empty_row(self):
		self.table.insert({})
		self.assertEqual(self.table.count_rows(),1)

	def test_select(self):
		self.table.select('')

	def test_insert_invalid_data(self):
		self.assertEqual(self.table.count_rows(),0)
		self.table.alter({'name':'name','type':'varchar','size':100})
		bDone = True
		try:
			self.table.insert({'name':'Adam','age':28})
		except DBError:
			bDone = False
		self.assertFalse(bDone)
		self.assertEqual(self.table.count_rows(),0)

	def test_insert_valid_data(self):
		self.assertEqual(self.table.count_rows(),0)
		self.table.alter({'name':'name','type':'varchar','size':100})
		self.table.alter({'name':'age','type':'int','size':4})
		self.table.insert({'name':'Adam','age':28})
		self.assertEqual(self.table.count_rows(),1)

if __name__ == '__main__':
	unittest.main()
