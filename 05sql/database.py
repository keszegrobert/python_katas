class DBError(Exception):
	pass

class DBTable:
	def __init__(self):
		self.columns = []
		self.rows = []

	def count_rows(self):
		return len(self.rows)

	def count_columns(self):
		return len(self.columns)

	def alter(self,column):
		self.columns.append(column)

	def insert(self,row):
		if len(row)>len(self.columns):
			raise DBError('too many columns in the inserted row')
		self.rows.append(row)

	def update(self,condition,update):
		updated_rows = []
		for row in self.rows:
			if self.__fits(row,condition):
				updated_row = self.__update_row(row,update)
				updated_rows.append(updated_row)
		return updated_rows

	def __update_row(self,row,update):
		updated_row = row
		for key,value in update:
			updated_row[key] = value
		return updated_row

	def delete(self,condition):
		remaining_rows = []
		for row in self.rows:
			if not self.__fits(row,condition):
				remaining_rows.append(row)
		self.rows = remaining_rows

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
			elif operation == 'OR':
				return self.__fits(row,left) or self.__fits(row,right) 
			elif operation == 'IN':
				return any(row[left] == s for s in right)
			return False

	def __apply_function(self,function,rows):
		if function == 'COUNT':
			return len(rows)
		elif function == 'MIN':
			minval = None
			for row in rows:
				for key,value in row.items():
					if minval == None:
						minval = value
					else:
						minval = value if value < minval else minval
			return minval
		elif function == 'MAX':
			maxval = None
			for row in rows:
				for key,value in row.items():
					if maxval == None:
						maxval = value
					else:
						maxval = value if value > maxval else maxval
			return maxval
		else:
			return rows

	def select(self,projection,condition):
		if type(projection) == tuple:
			function,fields = projection
			filtered_rows = []
			for row in self.rows:
				if self.__fits(row,condition):
					if fields == '*':
						filtered_rows.append(row)
					elif type(fields) == list:
						filtered_row = {}
						for element in fields:
							filtered_row[element] = row[element]
						filtered_rows.append(filtered_row)
					elif type(fields) == str:
						filtered_rows.append({fields:row[fields]})
					else:
						raise DBError('fields not defined properly')

			return self.__apply_function(function,filtered_rows)
		else:
			return []

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

