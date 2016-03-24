class RomanToArabicConverter:
	STATE_ERR = -1
	STATE_0 = 0
	STATE_I = 1
	STATE_II = 2
	STATE_IV = 3
	STATE_V = 4

	def convert(self,roman):
		self.state = self.STATE_0
		result = 0
		for i in range(0,len(roman)):
			if self.state == self.STATE_0:
				if roman[i] == 'I':
					self.state = self.STATE_I
					result = 1
			elif self.state == self.STATE_I:
				if roman[i] == 'I':
					self.state = self.STATE_II
					result = 2
				elif roman[i] == 'V':
					self.state = self.STATE_II
					result = 4
			elif self.state == self.STATE_II:
				if roman[i] == 'I':
					self.state = self.STATE_II
					result += 1
				elif roman[i] == 'V':
					self.state = self.STATE_ERR
		return result

	def is_valid(self):
		self.state != self.STATE_ERR
