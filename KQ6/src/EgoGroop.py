#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 103
import sci_sh
import kernel
import Main
import Grooper

# Public Export Declarations
SCI.public_exports(
	EgoGroop = 0,
)

class EgoGroop(Grooper):
	#property vars (may be empty)
	dontHead = 0
	speedState = 0
	
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if 
			(and
				((global0 loop:) == (kernel.NumLoops(global0) - 1))
				(not ((global0 signal:) & 0x0800))
			)
			(global0 loop: (global0 cel:))
		#endif
		(super doit: &rest)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super cue:)
		dontHead = 1
		if (((global0 view:) == 900) and (global1 isHandsOn:)):
			if (< 3 (global0 loop:) 8):
				(global0 setStep: 3 2)
				if speedState:
					(global0 currentSpeed: ((global0 currentSpeed:) - 2))
					(global0 setSpeed: (global0 currentSpeed:))
					speedState = 0
				#endif
			else:
				(global0 setStep: 6 2)
				if (not speedState):
					(global0 currentSpeed: ((global0 currentSpeed:) + 2))
					(global0 setSpeed: (global0 currentSpeed:))
					speedState = 2
				#endif
			#endif
		#endif
		dontHead = 0
	#end:method

#end:class or instance

