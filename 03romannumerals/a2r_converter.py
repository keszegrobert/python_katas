class ArabicToRomanConverter:

	def convert(self,arabic):
		roman = ''
		for i in range(0,arabic):
			roman += 'I'
		return roman