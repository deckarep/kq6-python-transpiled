#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 283
import sci_sh
import kernel
import Main
import rm280
import n913
import Inset
import Conversation
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	counterInset = 0,
	buyItemWithCoinScr = 1,
	genericExchangeScr = 2,
	offerCoinForMapScr = 3,
	lookAtCounterScr = 4,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = [48, 3, 14, 27, -1, 0, 5, 38, 1, 0, 0, -1, -1, 10, 5, 38, 2, 0, 0, -1, 0]
local22 = None
local23 = None


@SCI.instance
class counterInset(Inset):
	#property vars (may be empty)
	view = 287
	x = 84
	y = 48
	priority = 15
	disposeNotOnMe = 1
	noun = 35
	
	@classmethod
	def init():
		super._send('init:', &rest)
		if (global9._send('at:', 48)._send('owner:') == global11):
			tinderBox._send('init:')
		#endif
		if (global9._send('at:', 3)._send('owner:') == global11):
			paintBrush._send('init:')
		#endif
		if (global9._send('at:', 27)._send('owner:') == global11):
			windupBird._send('init:')
		#endif
		if (global9._send('at:', 14)._send('owner:') == global11):
			flute._send('init:')
		#endif
		if ((global2._send('script:') == lookAtCounterScr) and 1):
			global91._send('say:', 9, 1)
		#endif
		if (proc913_0(29) and proc913_0(30) and (not global0._send('has:', 0))):
			counterMap._send('init:')
		#endif
		self._send('setScript:', initDoneScr)
	#end:method

	@classmethod
	def doit():
		if script:
			script._send('doit:')
		#endif
	#end:method

	@classmethod
	def drawInset():
		super._send('drawInset:')
		insetView._send('ignoreActors:', 'addToPic:')
	#end:method

	@classmethod
	def dispose():
		global69._send('enable:', 6)
		global1._send('handsOff:')
		kernel.DisposeClone(insetView)
		if (not local0):
			proc913_2(51)
			proc913_2(50)
		#endif
		super._send('dispose:', &rest)
		global2._send('drawPic:', global11, 100)
	#end:method

#end:class or instance

class counterItemObj(View):
	#property vars (may be empty)
	view = 287
	loop = 1
	priority = 15
	signal = 16401
	baseFlag = 32
	lookFlagNum = 0
	invItemNum = 0
	item = 0
	
	@classmethod
	def init(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		if (argc > 0):
			item = param1
		#endif
		invItemNum = local1[item]
		lookFlagNum = (baseFlag + item)
		sightAngle = 26505
		self._send('addToPic:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				if (not proc913_0(lookFlagNum)):
					proc913_1(lookFlagNum)
					global91._send('say:', noun, 1, 42, 0, 0, 280)
				else:
					global91._send('say:', noun, 1, 43)
				#endif
			#end:case
			case 5:
				local0 = 1
				if global2._send('script:'):
					global2._send('script:')._send(
						'setScript:', itemTradeScr, counterInset._send('caller:'), noun
					)
				else:
					global2._send(
						'setScript:', itemTradeScr, counterInset._send('caller:'), noun
					)
				#endif
				counterInset._send('caller:', 0)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class roomTalk(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class tinderBox(counterItemObj):
	#property vars (may be empty)
	x = 197
	y = 89
	noun = 10
	
#end:class or instance

@SCI.instance
class paintBrush(counterItemObj):
	#property vars (may be empty)
	x = 191
	y = 67
	noun = 13
	cel = 2
	item = 1
	
#end:class or instance

@SCI.instance
class windupBird(counterItemObj):
	#property vars (may be empty)
	x = 92
	y = 76
	noun = 12
	cel = 1
	item = 3
	
#end:class or instance

@SCI.instance
class flute(counterItemObj):
	#property vars (may be empty)
	x = 143
	y = 62
	noun = 11
	cel = 3
	item = 2
	
#end:class or instance

@SCI.instance
class counterMap(View):
	#property vars (may be empty)
	x = 145
	y = 106
	noun = 37
	view = 287
	loop = 1
	cel = 4
	priority = 15
	signal = 20496
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				global91._send(
					'say:', noun, param1, (cond
							case proc913_0(50): 16#end:case
							case proc913_0(51): 39#end:case
							else: 0#end:else
						)
				)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		super._send('init:', &rest)
		sightAngle = 26505
		self._send('addToPic:')
	#end:method

#end:class or instance

@SCI.instance
class itemTradeScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cycles = 2
			#end:case
			case 1:
				counterInset._send('dispose:')
				cycles = 2
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				temp1 = 0
				temp0 = 0
				while (temp0 < 4): # inline for
					if global0._send('has:', local1[temp0]):
						temp1 = 1
						(break)
					#endif
					# for:reinit
					temp0.post('++')
				#end:loop
				(cond
					case temp1:
						state = 5
						global91._send('say:', register, 5, 41, 1, self)
					#end:case
					case (proc913_0(50) or proc913_0(51)):
						state = 3
						local22 = (4 if proc913_0(50) else 6)
						global91._send('say:', register, 5, 16, 1, self)
					#end:case
					else:
						state = 7
						global91._send('say:', register, 5, 38, 1, self)
					#end:else
				)
			#end:case
			case 4:
				state = local22
				self._send(
					'setScript:', kernel.ScriptID(287, 1), self, match register
							case 11: 2#end:case
							case 10: 0#end:case
							case 12: 3#end:case
							case 13: 1#end:case
						#end:match
				)
			#end:case
			case 5:
				state = 8
				global91._send('say:', 10, 5, 16, 2, self, 'oneOnly:', 0)
			#end:case
			case 6:
				state = 8
				global91._send('say:', 10, 5, 41, 2, self, 'oneOnly:', 0)
			#end:case
			case 7:
				state = 8
				global91._send(
					'say:', register, 5, (39 if (global153 == 1) else 40), 0, self
				)
			#end:case
			case 8:
				state = 8
				global91._send('say:', 10, 5, 38, 2, self)
			#end:case
			case 9:
				proc913_2(50)
				proc913_2(51)
				if (client == global2):
					global1._send('handsOn:')
				#endif
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lookAtCounterScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				proc280_10(self)
			#end:case
			case 1:
				global0._send('normal:', 0, 'view:', 280, 'loop:', 7, 'cel:', 0)
				cycles = 2
			#end:case
			case 2:
				kernel.UnLoad(128, 900)
				cycles = 2
			#end:case
			case 3:
				counterInset._send('init:', self, global2)
			#end:case
			case 4:
				global0._send('reset:', 0)
				cycles = 2
			#end:case
			case 5:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(283)
	#end:method

#end:class or instance

@SCI.instance
class buyItemWithCoinScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				proc280_10(self)
			#end:case
			case 1:
				self._send(
					'setScript:', kernel.ScriptID(286, 1), self, if 
							proc913_1(109)
							register = 69
							-32768
						else:
							register = 23
							-16384
						#endif
				)
			#end:case
			case 2:
				global91._send('say:', 4, 40, register, 1, script)
			#end:case
			case 3:
				global91._send(
					'say:', 4, 40, register, 2, if (register != 23):
							state.post('++')
							self
						else:
							script
						#endif
				)
			#end:case
			case 4:
				global91._send('say:', 4, 40, 23, 3, self, 'oneOnly:', 0)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				proc913_1(50)
				counterInset._send('init:', self, global2)
			#end:case
			case 7:
				cycles = 2
			#end:case
			case 8:
				if (not local0):
					global91._send('say:', 1, 5, 63, 0, self)
				else:
					state.post('++')
					global1._send('givePoints:', 2)
					global0._send('put:', 9, global11)
					cycles = 1
				#endif
			#end:case
			case 9:
				self._send('setScript:', kernel.ScriptID(286, 0), self, 1)
			#end:case
			case 10:
				global0._send('reset:', 0)
				cycles = 2
			#end:case
			case 11:
				kernel.ScriptID(280, 2)._send('setScript:', kernel.ScriptID(280, 9))
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(283)
	#end:method

#end:class or instance

@SCI.instance
class genericExchangeScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				proc280_10(self)
			#end:case
			case 1:
				(= register
					match register
						case 20: 0#end:case
						case 37: 3#end:case
						case 29: 1#end:case
						case 31: 2#end:case
					#end:match
				)
				self._send('setScript:', kernel.ScriptID(287, 0), self, register)
			#end:case
			case 2:
				global91._send('say:', 4, 20, 24, 1, script)
			#end:case
			case 3:
				if (global153 == 1):
					global91._send('say:', 4, 20, 24, 2, self)
				else:
					global91._send('say:', 4, 20, 25, 1, self)
				#endif
			#end:case
			case 4:
				global91._send('say:', 4, 20, 24, 3, self)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				proc913_1(51)
				counterInset._send('init:', self, global2)
			#end:case
			case 7:
				cycles = 10
			#end:case
			case 8:
				if (not local0):
					global91._send('say:', 1, 5, 63, 1, self)
				else:
					(state += 2)
					cycles = 1
				#endif
			#end:case
			case 9:
				global91._send('say:', 1, 5, 64, 2, self)
			#end:case
			case 10:
				self._send('setScript:', kernel.ScriptID(287, 1), self, register)
			#end:case
			case 11:
				cycles = 2
			#end:case
			case 12:
				global0._send('reset:', 0)
				cycles = 2
			#end:case
			case 13:
				kernel.ScriptID(280, 2)._send('setScript:', kernel.ScriptID(280, 9))
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(283)
	#end:method

#end:class or instance

@SCI.instance
class offerCoinForMapScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				proc280_10(self)
			#end:case
			case 1:
				self._send(
					'setScript:', kernel.ScriptID(286, 1), self, if 
							proc913_1(109)
							register = 70
							-32768
						else:
							register = 22
							-16384
						#endif
				)
			#end:case
			case 2:
				global91._send('say:', 4, 40, register, 1, script)
			#end:case
			case 3:
				global91._send(
					'say:', 4, 40, register, 2, if (register != 22):
							state.post('++')
							self
						else:
							script
						#endif
				)
			#end:case
			case 4:
				global91._send('say:', 4, 40, 22, 3, self, 'oneOnly:', 0)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				proc913_1(50)
				counterInset._send('init:', self, global2)
			#end:case
			case 7:
				cycles = 2
			#end:case
			case 8:
				if (not local0):
					global91._send('say:', 1, 5, 63, 0, self)
				else:
					state.post('++')
					global1._send('givePoints:', 2)
					global0._send('put:', 9, global11)
					cycles = 1
				#endif
			#end:case
			case 9:
				self._send('setScript:', kernel.ScriptID(286, 0), self)
			#end:case
			case 10:
				global0._send('reset:', 0)
				cycles = 2
			#end:case
			case 11:
				kernel.ScriptID(280, 2)._send('setScript:', kernel.ScriptID(280, 9))
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(283)
	#end:method

#end:class or instance

@SCI.instance
class initDoneScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cycles = 2
			#end:case
			case 1:
				global1._send('handsOn:')
				global69._send('curIcon:', global69._send('at:', 1))
				global1._send('setCursor:', global69._send('curIcon:')._send('cursor:'))
				global69._send('disable:', 0, 3, 4, 5, 6)
				local0 = 0
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

