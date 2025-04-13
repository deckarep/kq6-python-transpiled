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
		super._send('init:', &rest)
		global72._send('addToFront:', self)
		global73._send('addToFront:', self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global72._send('delete:', self)
		global73._send('delete:', self)
		super._send('dispose:')
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if global25:
			global80._send('canInput:', 1)
			if (countDown > 0):
				countDown.post('--')
			#endif
		#endif
		super._send('doit:')
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				global25
				(or
					((param1._send('type:') == 4) and (param1._send('message:') == 13))
					(param1._send('type:') == 1)
				)
			)
			param1._send('claimed:', 1)
			if (not countDown):
				global80._send('canInput:', 0)
				global25._send('seconds:', 0, 'dispose:')
				countDown = time
			#endif
		#endif
		return 1
	#end:method

#end:class or instance

