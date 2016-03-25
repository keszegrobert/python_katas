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
SL = 50
SLX = 60
SLXX = 70
SLXXX = 80
SXC = 90
SC = 100
SCC = 200
SCCC = 300
SCD = 400
SD = 500
SDC = 600
SDCC = 700
SDCCC = 800
SCM = 900
SM = 1000

class RomanToArabicConverter:
	state_machine = {
		S0:   {'I':(SI,1), 'V':(SV,5), 'X':(SX,10), 'L':(SL,50), 'C':(SC,100),'D':(SD,500) },
		SI:   {'I':(SII,1),'V':(SIV,3),'X':(SIX,8), },
		SII:  {'I':(SIII,1)},
		SIII: {'I':(SIV,1)},
		SIV:  {},
		SV:   {'I':(SVI,1)},
		SVI:  {'I':(SVII,1)},
		SVII: {'I':(SVIII,1)},
		SVIII:{},
		SIX:  {},
		SX:   {'I':(SI,1),'V':(SV,5),'X':(SXX,10), 'L':(SXL,30), 'C':(SXC,80) },
		SXX:  {'I':(SI,1),'V':(SV,5),'X':(SXXX,10) },
		SXXX: {'I':(SI,1),'V':(SV,5),'X':(SXL,10) },
		SXL:  {'I':(SI,1),'V':(SV,5)},
		SL:	  {'I':(SI,1),'V':(SV,5),'X':(SLX,10)},
		SLX:  {'I':(SI,1),'V':(SV,5),'X':(SLXX,10)},
		SLXX: {'I':(SI,1),'V':(SV,5),'X':(SLXXX,10)},
		SLXXX:{'I':(SI,1),'V':(SV,5),'X':(SXC,10)},
		SXC:  {'I':(SI,1),'V':(SV,5)},
		SC:   {'I':(SI,1),'V':(SV,5),'X':(SX,10),'L':(SL,50),'C':(SCC,100),'D':(SCD,300),'M':(SCM,800)},
		SCC:  {'I':(SI,1),'V':(SV,5),'X':(SX,10),'L':(SL,50),'C':(SCCC,100)},
		SCCC: {'I':(SI,1),'V':(SV,5),'X':(SX,10),'L':(SL,50),'C':(SCD,100)},
		SCD:  {'I':(SI,1),'V':(SV,5),'X':(SX,10),'L':(SL,50)},
		SD:   {'I':(SI,1),'V':(SV,5),'X':(SX,10),'L':(SL,50),'C':(SDC,100)},
		SDC:  {'I':(SI,1),'V':(SV,5),'X':(SX,10),'L':(SL,50),'C':(SDCC,100)},
		SDCC: {'I':(SI,1),'V':(SV,5),'X':(SX,10),'L':(SL,50),'C':(SDCCC,100)},
		SDCCC:{'I':(SI,1),'V':(SV,5),'X':(SX,10),'L':(SL,50),'C':(SCM,100)},
		SCM:  {'I':(SI,1),'V':(SV,5),'X':(SX,10),'L':(SL,50)},
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
