class ArabicToRomanConverter:
	romans = [
		('M',1000),
		('CM',900),
		('D',500),
		('CD',400),
		('C',100),
		('XC',90),
		('L',50),
		('XL',40),
		('X',10),
		('IX',9),
		('V',5),
		('IV',4),
		('I',1),
	]
	def convert(self,arabic):
		roman = ''
		while arabic > 0:
			for key,val in self.romans:
				if arabic >= val:
					arabic -= val
					roman += key
					break
		return roman