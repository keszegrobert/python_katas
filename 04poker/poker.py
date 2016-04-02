
NUMBERS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K','A']
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
		sum = 0
		last = 0
		for number in NUMBERS:
			last = self.cards.count((color,number))
			sum += last
		sum -= last #handling 'A'
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

	def has_royal_flush(self):
		return (
			self.has_straight_flush() 
			and self.__count_cards_of_number('A') == 1
			and self.__count_cards_of_number('K') == 1
		)

	def evaluate_hand(self):
		if self.has_royal_flush():
			return 100
		elif self.has_straight_flush():
			return 90
		elif self.has_poker():
			return 80
		elif self.has_full():
			return 70
		elif self.has_flush():
			return 60
		elif self.has_straight():
			return 50
		elif self.has_set():
			return 40
		elif self.has_two_pairs():
			return 30
		elif self.has_pair():
			return 20
		else:
			return 10

	def is_stronger_than(self,other):
		left_hand_value = self.evaluate_hand()
		right_hand_value = other.evaluate_hand()
		return left_hand_value > right_hand_value

