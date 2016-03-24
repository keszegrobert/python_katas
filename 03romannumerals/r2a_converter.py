SERR = -1
S0 = 0
SI = 1
SII = 2
SIII = 3
SIV = 4
SV = 5
SVI = 6
SVII = 7
SVIII = 8
SIX = 9
SX = 10
SXI = 11
SXX = 20
SXXX = 30
SXL = 40

class RomanToArabicConverter:
	state_machine = {
		S0:   {'I':(SI,1),   'V':(SV,5), 'X':(SX,10) },
		SI:   {'I':(SII,1),  'V':(SIV,3),'X':(SIX,8) },
		SII:  {'I':(SIII,1) 			 },
		SIII: {'I':(SIV,1)               },
		SIV:  {                          },
		SV:   {'I':(SVI,1)               },
		SVI:  {'I':(SVII,1)              },
		SVII: {'I':(SVIII,1)             },
		SVIII:{},
		SIX:  {},
		SX:   {'I':(SI,1),   'V':(SV,5), 'X':(SXX,10) },
		SXX:  {'I':(SI,1),   'V':(SV,5), 'X':(SXXX,10) },
		SXXX: {'I':(SI,1),   'V':(SV,5), 'X':(SXL,10) },
		SXL:  {'I':(SI,1),   'V':(SV,5) }
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
