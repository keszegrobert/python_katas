
NUMBERS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
COLORS = [
	'C', # clubs
	'D', # diamonds
	'S', # spades
	'H'  # hearts
]

class PokerHand:
	def __init__(self,cards):
		self.cards = cards

	def __count_cards_of_number(self,number):
		sum = 0;
		for color in COLORS:
			sum += self.cards.count((color,number))
		return sum

	def __count_cards_of_color(self,color):
		sum = 0;
		for number in NUMBERS:
			sum += self.cards.count((color,number))
		return sum

	def __count_numbers(self):
		return [self.__count_cards_of_number(number) for number in NUMBERS]

	def __count_colors(self):
		return [self.__count_cards_of_color(color) for color in COLORS]

	def has_pair(self):
		return 2 in self.__count_numbers()

	def has_two_pairs(self):
		return self.__count_numbers().count(2) == 2

	def has_set(self):
		return 3 in self.__count_numbers()

	def has_straight(self):
		numbers = self.__count_numbers()
		groups = ''
		for i in range(0, len(numbers)):
			groups += str(numbers[i])
		return groups.find('11111') > -1

	def has_flush(self):
		return 5 in self.__count_colors()

	def has_full(self):
		return self.has_pair() and self.has_set()

	def has_poker(self):
		return 4 in self.__count_numbers()

	def has_straight_flush(self):
		return self.has_straight() and self.has_flush()
