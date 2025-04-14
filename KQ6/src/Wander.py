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
	def init(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (argc >= 1):
			client = param1
			if (argc >= 2):
				distance = param2
			#endif
		#endif
		self._send('setTarget:')
		super._send('init:', client)
	#end:method

	@classmethod
	def setTarget():
		x = (client._send('x:') + (distance - kernel.Random(0, temp0 = (distance * 2))))
		y = (client._send('y:') + (distance - kernel.Random(0, temp0)))
	#end:method

	@classmethod
	def onTarget():
		return 0
	#end:method

	@classmethod
	def doit():
		super._send('doit:')
		if client._send('isStopped:'):
			self._send('moveDone:')
		#endif
	#end:method

	@classmethod
	def moveDone():
		self._send('init:')
	#end:method

#end:class or instance

