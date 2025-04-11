#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 939
import sci_sh
import kernel
import Motion

class Osc(Cycle):
	#property vars (may be empty)
	howManyCycles = -1
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (argc >= 2):
			howManyCycles = param2
			if (argc >= 3):
				caller = param3
			#endif
		#endif
		(super init: param1)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((temp0 = (self nextCel:) > (client lastCel:)) or (temp0 < 0)):
			cycleDir = -cycleDir
			(self cycleDone:)
		else:
			(client cel: temp0)
		#endif
	#end:method

	@classmethod
	def cycleDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if howManyCycles:
			(client cel: (self nextCel:))
			if (howManyCycles > 0):
				howManyCycles.post('--')
			#endif
		else:
			completed = 1
			(self motionCue:)
		#endif
	#end:method

#end:class or instance

