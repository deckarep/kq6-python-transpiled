#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 276
import sci_sh
import kernel
import Main
import rm270
import n913
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	giveRareBookScr = 1,
	talkOwnerScr = 2,
	talkAfterLLoc = 3,
)

@SCI.instance
class giveRareBookScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				proc913_1(77)
				proc270_7(self)
			#end:case
			case 1:
				global91._send('say:', 18, 27, 0, 1, self)
			#end:case
			case 2:
				global0._send(
					'setSpeed:', 6,
					'normal:', 0,
					'put:', 36,
					'get:', 45,
					'view:', 2771,
					'loop:', 4,
					'cel:', 0,
					'cycleSpeed:', 5,
					'posn:', 264, 151,
					'setCycle:', End
				)
				kernel.ScriptID(270, 2)._send(
					'view:', 2771,
					'loop:', 5,
					'cel:', 0,
					'posn:', 307, 152,
					'setCycle:', End, self
				)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				global91._send('say:', 18, 27, 0, 2, self)
			#end:case
			case 5:
				kernel.ScriptID(270, 2)._send(
					'loop:', 0,
					'cel:', 0,
					'posn:', 300, 161,
					'setCycle:', CT, 3, 1, self
				)
			#end:case
			case 6:
				kernel.ScriptID(270, 6)._send('dispose:')
				cycles = 2
			#end:case
			case 7:
				kernel.ScriptID(270, 2)._send('setCycle:', CT, 7, 1, self)
			#end:case
			case 8:
				global0._send('loop:', 3, 'cel:', 0, 'setCycle:', CT, 2, 1, self)
			#end:case
			case 9:
				kernel.ScriptID(270, 2)._send('setCycle:', End, self)
				global0._send('setCycle:', End, self)
			#end:case
			case 10: 0#end:case
			case 11:
				cycles = 2
			#end:case
			case 12:
				global0._send(
					'reset:', 0,
					'posn:', kernel.ScriptID(270, 2)._send('approachX:'), kernel.ScriptID(270, 2)._send(
							'approachY:'
						)
				)
				kernel.ScriptID(270, 2)._send(
					'view:', 277,
					'loop:', 2,
					'cel:', 0,
					'posn:', 303, 151,
					'stopUpd:'
				)
				cycles = 2
			#end:case
			case 13:
				global91._send('say:', 18, 27, 0, 3, self)
			#end:case
			case 14:
				global91._send('say:', 18, 27, 0, 4, self)
			#end:case
			case 15:
				global1._send('givePoints:', 1)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(276)
	#end:method

#end:class or instance

@SCI.instance
class talkOwnerScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				proc270_7(self)
			#end:case
			case 1:
				if 
					(and
						global5._send('contains:', kernel.ScriptID(271, 0))
						kernel.ScriptID(10, 0)._send('isSet:', -32768)
					)
					self._send('setScript:', kernel.ScriptID(278, 1), self)
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				if (not proc913_0(16)):
					proc913_1(16)
					global1._send('givePoints:', 1)
					global91._send('say:', 18, 2, 22, 0, self)
				else:
					global91._send('say:', 18, 2, 23, 1, self)
				#endif
			#end:case
			case 3:
				if 
					(and
						global5._send('contains:', kernel.ScriptID(271, 0))
						kernel.ScriptID(10, 0)._send('isSet:', -32768)
					)
					kernel.ScriptID(10, 0)._send('setIt:', -32768)
					self._send('setScript:', kernel.ScriptID(278, 1), self)
				else:
					cycles = 1
				#endif
			#end:case
			case 4:
				self._send('dispose:')
				global1._send('handsOn:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(276)
	#end:method

#end:class or instance

@SCI.instance
class talkAfterLLoc(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				proc270_7(self)
			#end:case
			case 1:
				if 
					(and
						global5._send('contains:', kernel.ScriptID(271, 0))
						kernel.ScriptID(10, 0)._send('isSet:', -32768)
					)
					self._send('setScript:', kernel.ScriptID(278, 1), self)
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				global91._send('say:', 18, 2, 21, 0, self)
			#end:case
			case 3:
				global91._send('say:', 18, 2, 22, 5, self, 'oneOnly:', 0)
			#end:case
			case 4:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(276)
	#end:method

#end:class or instance

