#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 946
import sci_sh
import kernel
import System

class Polygon(Obj):
	#property vars (may be empty)
	size = 0
	points = 0
	type = 1
	dynamic = 0
	
	@classmethod
	def init(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		size = (argc / 2)
		points = kernel.Memory(1, (2 * argc))
		kernel.StrCpy(points, @param1, -(argc * 2))
		dynamic = 1
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (dynamic and points):
			kernel.Memory(3, points)
		#endif
		(super dispose:)
	#end:method

#end:class or instance

