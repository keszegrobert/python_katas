
NUMBERS = ['A','2','3','4','5','6','7','8','9','J','Q','K']
COLORS = [
	'C', # clubs
	'D', # diamonds
	'S', # spades
	'H'  # hearts
]

class PokerHand:
	def __init__(self,cards):
		self.cards = cards

	def __count_colors(self,number):
		sum = 0;
		for color in COLORS:
			sum += self.cards.count((color,number))
		return sum

	def __has_equal_numbers(self,count):
		for number in NUMBERS:
			if (self.__count_colors(number) == count):
				return True
		return False

	def has_pair(self):
		return self.__has_equal_numbers(2)

	def has_drill(self):
		return self.__has_equal_numbers(3)

	def has_poker(self):
		return self.__has_equal_numbers(4)
