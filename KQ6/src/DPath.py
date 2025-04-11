#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 964
import sci_sh
import kernel
import Motion
import System

class DPath(Motion):
	#property vars (may be empty)
	points = 0
	value = 0
	
	@classmethod
	def init(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		points = (points or (List new:))
		if argc:
			client = param1
			temp0 = 0
			while (temp0 <= (argc - 3)): # inline for
				(points add: param2[temp0] param2[temp0.post('++')])
				# for:reinit
				temp0.post('++')
			#end:loop
			if (temp0 <= (argc - 2)):
				caller = param2[temp0]
			#endif
		#endif
		((points contains: -32768) or (points add: -32768))
		(self setTarget:)
		(super init:)
		if (not argc):
			(self doit:)
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if kernel.IsObject(points):
			(points dispose:)
		#endif
		(super dispose:)
	#end:method

	@classmethod
	def setTarget():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((points at: value) != -32768):
			x = (points at: value)
			y = (points at: value.post('++'))
			value.post('++')
		#endif
	#end:method

	@classmethod
	def moveDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((points at: value) == -32768):
			(super moveDone:)
		else:
			(self init:)
		#endif
	#end:method

#end:class or instance

