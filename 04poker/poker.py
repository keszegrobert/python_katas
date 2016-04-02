
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

	def __count_numbers(self):
		return [self.__count_colors(number) for number in NUMBERS]

	def has_pair(self):
		return 2 in self.__count_numbers()

	def has_set(self):
		return 3 in self.__count_numbers()

	def has_poker(self):
		return 4 in self.__count_numbers()

	def has_two_pairs(self):
		return self.__count_numbers().count(2) == 2
