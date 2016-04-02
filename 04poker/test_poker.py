from unittest import TestCase
from poker import PokerHand

SAMPLE_HIGH =		[('C','2'),('D','4'),('S','3'),('S','Q'),('C','9')]
SAMPLE_PAIR =		[('C','2'),('D','2'),('S','3'),('S','Q'),('C','9')]
SAMPLE_TWOPAIRS =	[('C','2'),('D','2'),('S','3'),('C','3'),('C','9')]
SAMPLE_DRILL =		[('C','2'),('D','2'),('S','2'),('S','Q'),('C','9')]
SAMPLE_STRAIGHT =	[('C','7'),('D','8'),('S','9'),('H','10'),('C','J')]
SAMPLE_POKER =		[('C','Q'),('D','Q'),('S','Q'),('H','Q'),('C','9')]

SAMPLES = [SAMPLE_HIGH,SAMPLE_PAIR,SAMPLE_TWOPAIRS,
	SAMPLE_DRILL,SAMPLE_STRAIGHT,SAMPLE_POKER
]

class TestPokerHand(TestCase):
	def setUp(self):
		pass

	def test_hand_has_pair(self):
		expected = [False,True,True,False,False,False]
		actual = [PokerHand(sample).has_pair() for sample in SAMPLES]
		self.assertEqual(expected,actual)

	def test_hand_has_two_pairs(self):
		expected = [False,False,True,False,False,False]
		actual = [PokerHand(sample).has_two_pairs() for sample in SAMPLES]
		self.assertEqual(expected,actual)

	def test_hand_has_set(self):
		expected = [False,False,False,True,False,False]
		actual = [PokerHand(sample).has_set() for sample in SAMPLES]
		self.assertEqual(expected,actual)

	def test_hand_has_straight(self):
		expected = [False,False,False,False,True,False]
		actual = [PokerHand(sample).has_straight() for sample in SAMPLES]
		self.assertEqual(expected,actual)

	def test_hand_has_poker(self):
		expected = [False,False,False,False,False,True]
		actual = [PokerHand(sample).has_poker() for sample in SAMPLES]
		self.assertEqual(expected,actual)



