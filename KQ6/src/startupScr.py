#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 201
import sci_sh
import kernel
import Main
import Scaler
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	startupScr = 0,
)

@SCI.instance
class startupScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send(
					'setSpeed:', 6,
					'posn:', 173, 133,
					'show:',
					'view:', 201,
					'loop:', 0,
					'cel:', 0,
					'normal:', 0,
					'setScale:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 1:
				global91._send('say:', 1, 0, 1, 1, self)
			#end:case
			case 2:
				global0._send('loop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 3:
				global0._send('posn:', 177, 127, 'reset:', 5, 'setScale:', Scaler, 100, 50, 112, 57)
				ticks = 20
			#end:case
			case 4:
				global0._send('loop:', 2)
				cycles = 2
			#end:case
			case 5:
				global91._send('say:', 1, 0, 1, 2, self)
			#end:case
			case 6:
				global91._send('say:', 1, 0, 1, 3, self, 'oneOnly:', 0)
			#end:case
			case 7:
				global1._send('handsOn:')
				global69._send('curIcon:', global69._send('at:', 0))
				global1._send('setCursor:', global69._send('curIcon:')._send('cursor:'))
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(201)
	#end:method

#end:class or instance

