#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 955
import sci_sh
import kernel
import Motion

class Track(Motion):
	#property vars (may be empty)
	who = 0
	xOffset = 0
	yOffset = 0
	zOffset = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, param6 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		client = param1
		who = param2
		if (argc >= 3):
			xOffset = param3
			if (argc >= 4):
				yOffset = param4
				if (argc >= 5):
					zOffset = param5
					if (argc >= 6):
						caller = param6
					#endif
				#endif
			#endif
		#endif
		(client ignoreActors: illegalBits: 0)
		(self doit:)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (who heading:)
		(client
			heading: temp0
			x: ((who x:) + xOffset)
			y: ((who y:) + yOffset)
			z: ((who z:) + zOffset)
		)
		if (client looper:):
			((client looper:) doit: client temp0)
		else:
			kernel.DirLoop(client, temp0)
		#endif
	#end:method

#end:class or instance

