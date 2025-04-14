#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 96
import sci_sh
import kernel
import Main
import System

# Public Export Declarations
SCI.public_exports(
	readNote = 0,
)

@SCI.instance
class readNote(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(96)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global91._send('say:', 36, 5, 0, 0, self, 907)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

