class ArabicToRomanConverter:

	def convert(self,arabic):
		roman = ''
		while arabic > 0:
			if arabic > 4:
				roman += 'V'
				arabic -= 5
			elif arabic == 4:
				roman += 'IV'
				arabic -= 4
			elif arabic > 0:
				roman += 'I'
				arabic -= 1
		return roman