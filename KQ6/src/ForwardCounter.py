#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 956
import sci_sh
import kernel
import Motion

class ForwardCounter(Fwd):
	#property vars (may be empty)
	count = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: param1)
		if (argc >= 2):
			count = param2
			if (argc >= 3):
				caller = param3
			#endif
		#endif
	#end:method

	@classmethod
	def cycleDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if count.post('--'):
			(super cycleDone:)
		else:
			completed = 1
			(self motionCue:)
		#endif
	#end:method

#end:class or instance

