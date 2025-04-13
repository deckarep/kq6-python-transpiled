#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 222
import sci_sh
import kernel
import Main
import n913
import Scaler
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	giveRingScr = 0,
)

@SCI.instance
class giveRingScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global1._send('givePoints:', 3)
				cycles = 1
			#end:case
			case 1:
				global91._send('say:', 5, 70, register, 1, self)
			#end:case
			case 2:
				global0._send(
					'setSpeed:', 6,
					'normal:', 0,
					'view:', 221,
					'loop:', 0,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				global91._send('say:', 5, 70, register, 2, self)
			#end:case
			case 5:
				kernel.ScriptID(220, 3)._send('setCycle:', Beg, self)
			#end:case
			case 6:
				kernel.ScriptID(220, 3)._send(
					'view:', 725,
					'setCycle:', Walk,
					'setMotion:', MoveTo, 99, 119, self
				)
			#end:case
			case 7:
				kernel.ScriptID(220, 3)._send('setHeading:', 90, self)
			#end:case
			case 8:
				cycles = 2
			#end:case
			case 9:
				global91._send('say:', 5, 70, register, 3, self)
			#end:case
			case 10:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 11:
				global91._send('say:', 5, 70, register, 4, self)
			#end:case
			case 12:
				if (register == 14):
					global91._send('say:', 5, 70, register, 5, self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 13:
				global0._send('reset:', 7)
				kernel.ScriptID(220, 4)._send('setCycle:', Beg)
				kernel.ScriptID(220, 3)._send('setHeading:', 0, self)
			#end:case
			case 14:
				global0._send('loop:', 3)
				self._send('setScript:', kernel.ScriptID(220, 1), self, 0)
			#end:case
			case 15:
				seconds = 4
			#end:case
			case 16:
				script._send('cue:')
			#end:case
			case 17:
				kernel.ScriptID(220, 6)._send('init:', 'setMotion:', MoveTo, 105, 94, self)
			#end:case
			case 18:
				kernel.ScriptID(220, 6)._send(
					'setPri:', -1,
					'setScale:', Scaler, 100, 94, 189, 95,
					'setMotion:', MoveTo, 117, 111, self
				)
			#end:case
			case 19:
				if (not (kernel.ScriptID(220, 6)._send('loop:') == 2)):
					kernel.ScriptID(220, 6)._send('setHeading:', 0, self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 20:
				cycles = 2
			#end:case
			case 21:
				global91._send('say:', 5, 70, 14, 6, self)
			#end:case
			case 22:
				global91._send('say:', 5, 70, 14, 7, self)
			#end:case
			case 23:
				global91._send('say:', 5, 70, 14, 8, self)
			#end:case
			case 24:
				kernel.ScriptID(220, 6)._send('setMotion:', MoveTo, 109, 93, self)
			#end:case
			case 25:
				kernel.ScriptID(220, 6)._send('cue:')
				global0._send(
					'setSpeed:', 10,
					'ignoreActors:',
					'setMotion:', MoveTo, 107, 93, self
				)
			#end:case
			case 26:
				global0._send(
					'setPri:', 2,
					'setScale:', Scaler, 64, 94, 103, 95,
					'moveSpeed:', 8,
					'setMotion:', MoveTo, 75, 100, self
				)
			#end:case
			case 27:
				self._send('setScript:', kernel.ScriptID(220, 2), self)
			#end:case
			case 28:
				global1._send('handsOn:')
				proc913_1(72)
				global2._send('newRoom:', 150)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('dispose:')
		kernel.DisposeScript(222)
	#end:method

#end:class or instance

