#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 371
import sci_sh
import kernel
import Main
import Print

class AnimatePrint(Print):
	#property vars (may be empty)
	myMouth = 0
	myEyes = 0
	theLength = 0
	
	@classmethod
	def init():
		modeless = 1
		ticks = 120
		if myMouth:
			myMouth._send('init:', theLength)
		#endif
		if myEyes:
			myEyes._send('init:')
		#endif
		super._send('init:')
	#end:method

	@classmethod
	def addText(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
		width = 230
		theLength = (kernel.Message(2, global11, param1, param2, param3, param4) / 12)
		super._send('addText:', param1, param2, param3, param4, &rest)
	#end:method

	@classmethod
	def dispose():
		if myMouth:
			myMouth._send('dispose:')
		#endif
		if myEyes:
			myEyes._send('dispose:')
		#endif
		super._send('dispose:')
		global2._send('script:')._send('cue:')
	#end:method

#end:class or instance

