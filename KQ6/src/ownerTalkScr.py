#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 284
import sci_sh
import kernel
import Main
import rm280
import n913
import Rev
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	ownerTalkScr = 0,
	ringMapNotOutScr = 1,
	ringForMapActIScr = 2,
	ringForPearlScr = 3,
	ringForMapNotActIScr = 4,
	talkAfterActI = 5,
)

@SCI.instance
class ownerTalkScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				proc280_10(self)
				global0._send('normal:', 0, 'view:', 280, 'loop:', 7, 'cel:', 0)
				cycles = 2
			#end:case
			case 1:
				kernel.UnLoad(128, 900)
			#end:case
			case 2:
				global91._send('say:', 4, 2, 13, 1, self)
			#end:case
			case 3:
				global91._send('say:', 4, 2, 13, 2, self)
			#end:case
			case 4:
				kernel.ScriptID(280, 2)._send(
					'view:', 286,
					'posn:', 236, 127,
					'loop:', 1,
					'cel:', 0,
					'setPri:', 11,
					'setCycle:', End, self
				)
				global9._send('at:', 0)._send('owner:', -1)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				global91._send('say:', 4, 2, 13, 3, self)
			#end:case
			case 7:
				global91._send('say:', 4, 2, 13, 4, self)
			#end:case
			case 8:
				global91._send('say:', 4, 2, 13, 5, self)
			#end:case
			case 9:
				global91._send('say:', 4, 2, 13, 6, self)
			#end:case
			case 10:
				kernel.ScriptID(280, 2)._send('loop:', 2, 'cel:', 0, 'setCycle:', CT, 4, 1, self)
			#end:case
			case 11:
				kernel.ScriptID(280, 1)._send('init:')
				kernel.ScriptID(280, 2)._send('setCycle:', End, self)
			#end:case
			case 12:
				kernel.ScriptID(280, 2)._send('setPri:', -1, 'view:', 280, 'loop:', 8, 'cel:', 0)
				cycles = 2
			#end:case
			case 13:
				kernel.UnLoad(128, 286)
				global91._send('say:', 4, 2, 13, 7, self, 'oneOnly:', 0)
			#end:case
			case 14:
				kernel.ScriptID(280, 2)._send('setScript:', kernel.ScriptID(280, 9))
				global0._send('reset:', 0)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:', &rest)
		kernel.DisposeScript(284)
	#end:method

#end:class or instance

@SCI.instance
class ringMapNotOutScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				proc280_10(self)
				global0._send('normal:', 0, 'view:', 280, 'loop:', 7, 'cel:', 0)
				cycles = 2
			#end:case
			case 1:
				kernel.UnLoad(128, 900)
			#end:case
			case 2:
				(= register
					if kernel.ScriptID(10, 0)._send('isSet:', 1):
						self._send('setScript:', kernel.ScriptID(286, 2), self)
						36
					else:
						kernel.ScriptID(10, 0)._send('setIt:', 1)
						self._send('setScript:', kernel.ScriptID(286, 1), self, 16384)
						18
					#endif
				)
			#end:case
			case 3:
				global91._send(
					'say:', 4, 70, register, 1, (self if (register == 36) else script)
				)
			#end:case
			case 4:
				global91._send('say:', 4, 70, register, 2, script)
			#end:case
			case 5:
				if (register == 36):
					(state += 2)
					cycles = 2
				else:
					global91._send('say:', 4, 70, register, 3, self)
				#endif
			#end:case
			case 6:
				self._send('setScript:', kernel.ScriptID(286, 0), self)
			#end:case
			case 7:
				global91._send('say:', 4, 70, register, 4, self)
			#end:case
			case 8:
				kernel.ScriptID(280, 2)._send('setScript:', kernel.ScriptID(280, 9))
				global0._send('reset:', 0)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:', &rest)
		kernel.DisposeScript(284)
	#end:method

#end:class or instance

@SCI.instance
class ringForMapActIScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('put:', 39, global11)
				global1._send('handsOff:')
				proc280_10(self)
				global0._send('normal:', 0, 'view:', 280, 'loop:', 7, 'cel:', 0)
				cycles = 2
			#end:case
			case 1:
				kernel.UnLoad(128, 900)
			#end:case
			case 2:
				global1._send('givePoints:', 5)
				self._send('setScript:', kernel.ScriptID(286, 1), self, 16384)
			#end:case
			case 3:
				kernel.UnLoad(128, 2811)
				kernel.UnLoad(128, 284)
				global91._send('say:', 4, 70, 19, 1, kernel.ScriptID(286, 1))
			#end:case
			case 4:
				global91._send('say:', 4, 70, 19, 2, kernel.ScriptID(286, 1))
			#end:case
			case 5:
				global91._send('say:', 4, 70, 19, 3, self)
			#end:case
			case 6:
				global91._send('say:', 4, 70, 19, 4, self)
			#end:case
			case 7:
				global91._send('say:', 4, 70, 19, 5, self)
			#end:case
			case 8:
				global91._send('say:', 4, 70, 19, 6, self)
			#end:case
			case 9:
				global91._send('say:', 4, 70, 19, 7, self)
			#end:case
			case 10:
				global91._send('say:', 4, 70, 19, 8, self)
			#end:case
			case 11:
				global91._send('say:', 4, 70, 19, 9, self)
			#end:case
			case 12:
				proc913_3()
				self._send('setScript:', kernel.ScriptID(286, 3), self)
			#end:case
			case 13:
				kernel.UnLoad(128, 286)
				self._send('setScript:', kernel.ScriptID(282, 2), self)
				cycles = 1
			#end:case
			case 14:
				global0._send(
					'reset:',
					'setSpeed:', 6,
					'setLoop:', 0,
					'setCycle:', Rev,
					'setMotion:', MoveTo, (global0._send('x:') - 10), global0._send('y:'), self
				)
			#end:case
			case 15:
				global0._send('setCycle:', Walk)
			#end:case
			case 16:
				global2._send('newRoom:', 145)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:', &rest)
		kernel.DisposeScript(284)
	#end:method

#end:class or instance

@SCI.instance
class ringForMapNotActIScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('get:', 0, 'put:', 39, global11)
				global1._send('handsOff:')
				proc280_10(self)
				global0._send('normal:', 0, 'view:', 280, 'loop:', 7, 'cel:', 0)
				cycles = 2
			#end:case
			case 1:
				kernel.UnLoad(128, 900)
			#end:case
			case 2:
				global91._send('say:', 4, 70, 21, 1, self)
			#end:case
			case 3:
				global91._send('say:', 4, 70, 21, 2, self)
			#end:case
			case 4:
				self._send('setScript:', kernel.ScriptID(286, 1), self, -32768)
			#end:case
			case 5:
				script._send('cue:')
			#end:case
			case 6:
				ticks = 15
			#end:case
			case 7:
				self._send('setScript:', kernel.ScriptID(286, 3), self)
			#end:case
			case 8:
				kernel.ScriptID(280, 2)._send('setScript:', kernel.ScriptID(280, 9))
				global0._send('reset:', 0)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:', &rest)
		kernel.DisposeScript(284)
	#end:method

#end:class or instance

@SCI.instance
class ringForPearlScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('put:', 39, 'get:', 30)
				global1._send('handsOff:')
				proc280_10(self)
				global0._send('normal:', 0, 'view:', 280, 'loop:', 7, 'cel:', 0)
				cycles = 2
			#end:case
			case 1:
				kernel.UnLoad(128, 900)
			#end:case
			case 2:
				global91._send('say:', 4, 70, 20, 1, self)
			#end:case
			case 3:
				global91._send('say:', 4, 70, 20, 2, self)
			#end:case
			case 4:
				self._send('setScript:', kernel.ScriptID(286, 1), self)
			#end:case
			case 5:
				script._send('cue:')
			#end:case
			case 6:
				ticks = 120
			#end:case
			case 7:
				self._send('setScript:', kernel.ScriptID(286, 0), self)
			#end:case
			case 8:
				global91._send('say:', 4, 70, 20, 3, self)
			#end:case
			case 9:
				global0._send('reset:', 0)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:', &rest)
		kernel.DisposeScript(284)
	#end:method

#end:class or instance

@SCI.instance
class talkAfterActI(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				proc280_10(self)
				global0._send('normal:', 0, 'view:', 280, 'loop:', 7, 'cel:', 0)
				cycles = 2
			#end:case
			case 1:
				kernel.UnLoad(128, 900)
			#end:case
			case 2:
				global91._send('say:', 4, 2, 47, 1, self)
			#end:case
			case 3:
				global91._send(
					'say:', 4, 2, match kernel.Random(0, 4)
							case 0: 15#end:case
							case 1: 37#end:case
							case 2: 44#end:case
							case 3: 45#end:case
							case 4: 46#end:case
						#end:match, 1, self
				)
			#end:case
			case 4:
				global0._send('reset:', 0)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:', &rest)
		kernel.DisposeScript(284)
	#end:method

#end:class or instance

