#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 88
import sci_sh
import kernel
import Main
import LoadMany
import Sound
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	boringBookScript = 0,
)

@SCI.instance
class boringBookScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				seconds = 2
			#end:case
			case 1:
				global0._send(
					'normal:', 0,
					'view:', 903,
					'cel:', 0,
					'setLoop:', 2,
					'cycleSpeed:', 5,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				global0._send('cel:', 0, 'setLoop:', 0, 'setCycle:', End, self)
			#end:case
			case 3:
				global0._send('setLoop:', 1, 'setCycle:', Fwd)
				seconds = 4
			#end:case
			case 4:
				global91._send('say:', 1, 42, 0, 1, self, 0)
			#end:case
			case 5:
				global91._send('say:', 1, 42, 0, 2, self, 0)
			#end:case
			case 6:
				global0._send('setLoop:', 2, 'lastCel:', 'setCycle:', Beg, self)
			#end:case
			case 7:
				seconds = 1
			#end:case
			case 8:
				localMusic._send('loop:', 1, 'number:', 961, 'play:')
				global0._send('setLoop:', 3, 'cycleSpeed:', 10, 'setCycle:', End, self)
			#end:case
			case 9:
				global0._send('setCel:', 0, 'setCycle:', CT, 5, 1, self)
			#end:case
			case 10:
				cycles = 15
			#end:case
			case 11:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 12:
				cycles = 15
			#end:case
			case 13:
				global0._send('reset:', 2)
				cycles = 10
			#end:case
			case 14:
				global91._send('say:', 1, 42, 0, 3, self, 0)
			#end:case
			case 15:
				global91._send('say:', 1, 42, 0, 4, self, 0)
			#end:case
			case 16:
				global1._send('handsOn:')
				localMusic._send('stop:', 'dispose:')
				self._send('dispose:')
				proc958_0(0, 88)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class localMusic(Sound):
	#property vars (may be empty)
#end:class or instance

