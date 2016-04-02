from unittest import TestCase
from poker import PokerHand

SAMPLES = {
	'HIGH': 	[('C','2'),('D','4'),('S','3'),('S','Q'),('C','9')],
	'PAIR':		[('C','2'),('D','2'),('S','3'),('S','Q'),('C','9')],
	'TWOPAIRS':	[('C','2'),('D','2'),('S','3'),('C','3'),('C','9')],
	'DRILL':	[('C','2'),('D','2'),('S','2'),('S','Q'),('C','9')],
	'STRAIGHT':	[('C','7'),('D','8'),('S','9'),('H','10'),('C','J')],
	'FLUSH':	[('C','3'),('C','8'),('C','10'),('C','4'),('C','Q')],
	'FULL':		[('C','6'),('D','6'),('S','6'),('H','J'),('C','J')],
	'POKER':	[('C','Q'),('D','Q'),('S','Q'),('H','Q'),('C','9')],
	'SFLUSH':	[('C','7'),('C','8'),('C','9'),('C','10'),('C','J')],
	'ASFLUSH':	[('C','A'),('C','2'),('C','3'),('C','4'),('C','5')],
	'RFLUSH':	[('C','10'),('C','J'),('C','Q'),('C','K'),('C','A')]
}

class TestPokerHand(TestCase):
	def setUp(self):
		pass

	def test_hand_has_pair(self):
		exp_true = ['PAIR','TWOPAIRS','FULL']
		expected = {(key,key in exp_true)for key,sample in SAMPLES.items()}
		actual = {(key,PokerHand(sample).has_pair()) for key,sample in SAMPLES.items()}
		self.assertEqual(expected,actual)

	def test_hand_has_two_pairs(self):
		exp_true = ['TWOPAIRS']
		expected = [(key in exp_true )for key,sample in SAMPLES.items()]
		actual = [PokerHand(sample).has_two_pairs() for key,sample in SAMPLES.items()]
		self.assertEqual(expected,actual)

	def test_hand_has_set(self):
		exp_true = ['DRILL','FULL']
		expected = [(key in exp_true )for key,sample in SAMPLES.items()]
		actual = [PokerHand(sample).has_set() for key,sample in SAMPLES.items()]
		self.assertEqual(expected,actual)

	def test_hand_has_straight(self):
		exp_true = ['STRAIGHT','SFLUSH','ASFLUSH','RFLUSH']
		expected = [(key in exp_true )for key,sample in SAMPLES.items()]
		actual = [PokerHand(sample).has_straight() for key,sample in SAMPLES.items()]
		self.assertEqual(expected,actual)

	def test_hand_has_flush(self):
		exp_true = ['FLUSH','SFLUSH','ASFLUSH','RFLUSH']
		expected = [(key in exp_true )for key,sample in SAMPLES.items()]
		actual = [PokerHand(sample).has_flush() for key,sample in SAMPLES.items()]
		self.assertEqual(expected,actual)

	def test_hand_has_full(self):
		exp_true = ['FULL']
		expected = [(key in exp_true )for key,sample in SAMPLES.items()]
		actual = [PokerHand(sample).has_full() for key,sample in SAMPLES.items()]
		self.assertEqual(expected,actual)

	def test_hand_has_poker(self):
		exp_true = ['POKER']
		expected = [(key in exp_true )for key,sample in SAMPLES.items()]
		actual = [PokerHand(sample).has_poker() for key,sample in SAMPLES.items()]
		self.assertEqual(expected,actual)

	def test_hand_has_straight_flush(self):
		exp_true = ['SFLUSH','ASFLUSH','RFLUSH']
		expected = [(key in exp_true )for key,sample in SAMPLES.items()]
		actual = [PokerHand(sample).has_straight_flush() for key,sample in SAMPLES.items()]
		self.assertEqual(expected,actual)

	def test_hand_has_royal_flush(self):
		exp_true = ['RFLUSH']
		expected = [(key in exp_true )for key,sample in SAMPLES.items()]
		actual = [PokerHand(sample).has_royal_flush() for key,sample in SAMPLES.items()]
		self.assertEqual(expected,actual)

	def test_which_hand_is_stronger(self):
		order = ['HIGH','PAIR','TWOPAIRS','DRILL','STRAIGHT','FLUSH','FULL','POKER','SFLUSH','RFLUSH']
		actual = []
		for i in range(0,len(order)):
			left_hand = PokerHand(SAMPLES[order[i]])
			for j in range(i+1,len(SAMPLES)):
				if j >= len(order):
					break
				right_hand = PokerHand(SAMPLES[order[j]])
				actual.append(right_hand.is_stronger_than(left_hand))
		expected = [True for i in range(0,len(actual))]
		self.assertEqual(expected,actual)


