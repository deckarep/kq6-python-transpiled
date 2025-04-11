#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 970
import sci_sh
import kernel
import Motion

class Wander(Motion):
	#property vars (may be empty)
	distance = 30
	
	@classmethod
	def init(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (argc >= 1):
			client = param1
			if (argc >= 2):
				distance = param2
			#endif
		#endif
		(self setTarget:)
		(super init: client)
	#end:method

	@classmethod
	def setTarget():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		x = ((client x:) + (distance - kernel.Random(0, temp0 = (distance * 2))))
		y = ((client y:) + (distance - kernel.Random(0, temp0)))
	#end:method

	@classmethod
	def onTarget():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		return 0
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super doit:)
		if (client isStopped:):
			(self moveDone:)
		#endif
	#end:method

	@classmethod
	def moveDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self init:)
	#end:method

#end:class or instance

