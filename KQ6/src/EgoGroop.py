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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				(global0._send('loop:') == (kernel.NumLoops(global0) - 1))
				(not (global0._send('signal:') & 0x0800))
			)
			global0._send('loop:', global0._send('cel:'))
		#endif
		super._send('doit:', &rest)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('cue:')
		dontHead = 1
		if ((global0._send('view:') == 900) and global1._send('isHandsOn:')):
			if (< 3 global0._send('loop:') 8):
				global0._send('setStep:', 3, 2)
				if speedState:
					global0._send('currentSpeed:', (global0._send('currentSpeed:') - 2))
					global0._send('setSpeed:', global0._send('currentSpeed:'))
					speedState = 0
				#endif
			else:
				global0._send('setStep:', 6, 2)
				if (not speedState):
					global0._send('currentSpeed:', (global0._send('currentSpeed:') + 2))
					global0._send('setSpeed:', global0._send('currentSpeed:'))
					speedState = 2
				#endif
			#endif
		#endif
		dontHead = 0
	#end:method

#end:class or instance

