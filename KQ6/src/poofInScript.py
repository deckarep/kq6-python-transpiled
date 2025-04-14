#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 89
import sci_sh
import kernel
import Main
import Scaler
import Sound
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	poofInScript = 0,
)

@SCI.instance
class poofInScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				cycles = 15
			#end:case
			case 1:
				global1._send('handsOff:')
				if (not global0._send('x:')):
					global0._send('posn:', 200, 127)
				#endif
				localMusic2._send('loop:', 1, 'number:', 947, 'play:')
				global0._send(
					'view:', 207,
					'init:',
					'cycleSpeed:', 10,
					'normal:', 0,
					'setLoop:', 1,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				global0._send(
					'normal:', 0,
					'cycleSpeed:', 10,
					'view:', 207,
					'setLoop:', 2,
					'cel:', 0,
					'lastCel:',
					'setCycle:', Beg, self
				)
			#end:case
			case 3:
				global1._send('handsOn:')
				global0._send('reset:')
				localMusic2._send('stop:', 'dispose:')
				self._send('dispose:')
				if (global11 == 450):
					global0._send('setScale:', Scaler, 100, 30, 126, 70)
				#endif
				kernel.DisposeScript(89)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class localMusic2(Sound):
	#property vars (may be empty)
#end:class or instance

