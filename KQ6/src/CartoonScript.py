#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 910
import sci_sh
import kernel
import Main
import System

class CartoonScript(Script):
	#property vars (may be empty)
	countDown = 0
	time = 10
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		countDown = time
		(super init: &rest)
		(global72 addToFront: self)
		(global73 addToFront: self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global72 delete: self)
		(global73 delete: self)
		(super dispose:)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if global25:
			(global80 canInput: 1)
			if (countDown > 0):
				countDown.post('--')
			#endif
		#endif
		(super doit:)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				global25
				(or
					(((param1 type:) == 4) and ((param1 message:) == 13))
					((param1 type:) == 1)
				)
			)
			(param1 claimed: 1)
			if (not countDown):
				(global80 canInput: 0)
				(global25 seconds: 0 dispose:)
				countDown = time
			#endif
		#endif
		return 1
	#end:method

#end:class or instance

