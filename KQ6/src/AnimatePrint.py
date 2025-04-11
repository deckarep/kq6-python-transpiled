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
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		modeless = 1
		ticks = 120
		if myMouth:
			(myMouth init: theLength)
		#endif
		if myEyes:
			(myEyes init:)
		#endif
		(super init:)
	#end:method

	@classmethod
	def addText(param1 = None, param2 = None, param3 = None, param4 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		width = 230
		theLength = (kernel.Message(2, global11, param1, param2, param3, param4) / 12)
		(super addText: param1 param2 param3 param4 &rest)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if myMouth:
			(myMouth dispose:)
		#endif
		if myEyes:
			(myEyes dispose:)
		#endif
		(super dispose:)
		((global2 script:) cue:)
	#end:method

#end:class or instance

