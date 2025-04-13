#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 915
import sci_sh
import kernel
import Main
import n913
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	mixPaintScr = 0,
)

@SCI.instance
class mixPaintScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global9._send('hide:')
				cycles = 2
			#end:case
			case 1:
				global0._send('setHeading:', 180, self)
			#end:case
			case 2:
				global0._send('setSpeed:', 6, 'normal:', 0, 'view:', 915, 'setLoop:', 0)
				seconds = 3
			#end:case
			case 3:
				global91._send('say:', 3, 0, 8, 1, self, 0)
			#end:case
			case 4:
				global0._send('setLoop:', 1, 'setCycle:', Fwd)
				seconds = 2
			#end:case
			case 5:
				global91._send('say:', 3, 0, 8, 2, self, 0)
			#end:case
			case 6:
				global0._send('setLoop:', 2, 'setCycle:', Fwd)
				seconds = 2
			#end:case
			case 7:
				global0._send('setLoop:', 3, 'setCycle:', Fwd)
				seconds = 2
			#end:case
			case 8:
				global0._send('setLoop:', 4, 'setCycle:', Fwd)
				seconds = 2
			#end:case
			case 9:
				global0._send('setLoop:', 5, 'setCycle:', Fwd)
				seconds = 2
			#end:case
			case 10:
				global105._send('loop:', 1, 'number:', 946, 'play:')
				global91._send('say:', 3, 0, 8, 3, self, 0)
			#end:case
			case 11:
				global0._send('reset:', 2)
				cycles = 2
			#end:case
			case 12:
				global0._send('put:', 12)
				global1._send('givePoints:', 1)
				global91._send('say:', 3, 0, 8, 4, self, 0)
			#end:case
			case 13:
				proc913_1(22)
				self._send('dispose:')
				global1._send('handsOn:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('dispose:')
		register = 0
		kernel.DisposeScript(915)
	#end:method

#end:class or instance

