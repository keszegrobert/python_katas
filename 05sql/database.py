class DBError(Exception):
	pass

class DBTable:
	def __init__(self):
		self.columns = []
		self.rows = []

	def count_rows(self):
		return len(self.rows)

	def count_clumns(self):
		return len(self.columns)

	def alter(self,column):
		self.columns.append(column)

	def insert(self,row):
		if len(row)>len(self.columns):
			raise DBError('too many columns in the inserted row')
		self.rows.append(row)

	def update(self,which,row):
		#self.rows.(row)
		pass

	def delete(self,which):
		#self.rows.append(row)
		pass

	def filter(self,condition):
		filtered_rows = []
		for row in self.rows:
			if self.__fits(row,condition):
				filtered_rows.append(row)
		return filtered_rows

	def __fits(self,row,condition):
		if condition == False or condition == True:
			return condition
		else:
			operation, left, right = condition
			if operation == 'EQ':
				return row[left] == right
			elif operation == 'NE':
				return row[left] != right
			elif operation == 'GT':
				return row[left] > right
			elif operation == 'LT':
				return row[left] < right
			elif operation == 'LE':
				return row[left] <= right
			elif operation == 'GE':
				return row[left] >= right
			elif operation == 'AND':
				return self.__fits(row,left) and self.__fits(row,right) 
			return False

class DataBase:
	def __init__(self):
		self.tables = {}

	def table_exists(self,tablename):
		try:
			tmp = self.tables[tablename]
			return self.tables[tablename] != None
		except KeyError:
			return False

	def create_table(self,tablename):
		if not self.table_exists(tablename):
			self.tables[tablename] = DBTable()
		else:
			raise DBError('table "'+tablename+'" already exists')

	def drop_table(self,tablename):
		if not self.table_exists(tablename):
			raise DBError('table "'+tablename+' does not exist')
		self.tables[tablename] = None

