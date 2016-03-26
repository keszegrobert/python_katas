from unittest import TestCase
from database import DataBase
from database import DataBaseError

class TestDataBase(TestCase):
	def setUp(self):
		self.db = DataBase()

	def test_create_non_existing_table(self):
		self.assertFalse(self.db.table_exists('persons'))
		self.db.create_table('persons')
		self.assertTrue(self.db.table_exists('persons'))

	def test_create_existing_table(self):
		self.assertFalse(self.db.table_exists('persons'))
		self.db.create_table('persons')
		bTableExists = False

		try:
			self.db.create_table('persons')
		except DataBaseError, e:
			bTableExists = True

		self.assertTrue(bTableExists)

	def test_drop_existing_table(self):
		self.assertFalse(self.db.table_exists('persons'))
		self.db.create_table('persons')
		self.assertTrue(self.db.table_exists('persons'))
		self.db.drop_table('persons')
		self.assertFalse(self.db.table_exists('persons'))

	def test_drop_non_existing_table(self):
		bTableExists = False
		try:
			self.db.drop_table('persons')
		except DataBaseError, e:
			bTableExists = True
		self.assertTrue(bTableExists)

if __name__ == '__main__':
	unittest.main()
