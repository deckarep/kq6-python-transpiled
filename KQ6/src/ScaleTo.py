#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 975
import sci_sh
import kernel
import Main
import Scaler

class ScaleTo(Scaler):
	#property vars (may be empty)
	caller = 0
	endScale = 0
	step = 6
	waitCount = 1
	scaleDir = 0
	saveWaitCount = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			client = param1
			if (argc >= 2):
				endScale = param2
				if (argc >= 3):
					if kernel.IsObject(param3):
						caller = param3
					else:
						step = param3
						if (argc >= 4):
							if kernel.IsObject(param4):
								caller = param4
							else:
								waitCount = param4
								if (argc >= 5):
									caller = param5
								#endif
							#endif
						#endif
					#endif
				#endif
			#endif
		#endif
		saveWaitCount = waitCount
		scaleDir = (1 if ((client maxScale:) <= endScale) else <<NO ELSE CLAUSE>>)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((global88 - waitCount) > 0):
			(= temp0
				if scaleDir:
					((client maxScale:) + step)
				else:
					((client maxScale:) - step)
				#endif
			)
			(client maxScale: temp0 scaleX: temp0 scaleY: temp0)
			(cond
				case scaleDir:
					if ((client maxScale:) >= endScale):
						(self dispose:)
					#endif
				#end:case
				case ((client maxScale:) <= endScale):
					(self dispose:)
				#end:case
			)
			waitCount = (saveWaitCount + global88)
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		endScale = 0
		step = 6
		waitCount = 1
		(client scaler: 0)
		if caller:
			temp0 = caller
			caller = 0
			(temp0 cue:)
		#endif
		(super dispose:)
	#end:method

#end:class or instance

