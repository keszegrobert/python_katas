SERR = -1
S0 = 0
SI = 1
SII = 2
SIII = 3
SIV = 4
SV = 5
SVI = 6


class RomanToArabicConverter:
	state_machine = {
		S0:   {'I':(SI,1),   'V':(SV,5)  },
		SI:   {'I':(SII,1),  'V':(SIV,3) },
		SII:  {'I':(SIII,1) 			 },
		SIII: {'I':(SIV,1)               },
		SIV:  {},
		SV:	  {'I':(SVI,1)}
	}


	def convert(self,roman):
		self.state = S0
		result = 0
		for i in range(0,len(roman)):
			possibilities = self.state_machine[self.state]
			try:
				next_state,add = possibilities[roman[i]]
				self.state = next_state
				result += add
			except KeyError:
				self.state = SERR

		return result

	def is_valid(self):
		return self.state != SERR
