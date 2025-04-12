#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 960
import sci_sh
import kernel
import System

class TimedCue(Script):
	#property vars (may be empty)
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: param1 param1)
		if (argc >= 2):
			seconds = param2
			if (argc >= 3):
				cycles = param3
			#endif
		#endif
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if state.post('++'):
			(self dispose:)
		#endif
	#end:method

#end:class or instance

