#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 231
import sci_sh
import kernel
import Motion

# Public Export Declarations
SCI.public_exports(
	ForwardFrom = 0,
)

class ForwardFrom(Fwd):
	#property vars (may be empty)
	startAt = 0
	cycleCount = -1
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		client = param1
		client._send('cel:', startAt = param2)
		if (argc > 2):
			cycleCount = param3
			if (argc > 3):
				caller = param4
			#endif
		#endif
	#end:method

	@classmethod
	def cycleDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		client._send('cel:', startAt)
		if (not cycleCount.post('--')):
			completed = 1
			self._send('motionCue:')
		#endif
	#end:method

#end:class or instance

