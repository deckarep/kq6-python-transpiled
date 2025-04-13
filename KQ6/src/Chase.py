#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 972
import sci_sh
import kernel
import Motion

class Chase(Motion):
	#property vars (may be empty)
	who = 0
	distance = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (argc >= 1):
			client = param1
			if (argc >= 2):
				who = param2
				if (argc >= 3):
					distance = param3
					if (argc >= 4):
						caller = param4
					#endif
				#endif
			#endif
		#endif
		super._send('init:', client, who._send('x:'), who._send('y:'), caller)
	#end:method

	@classmethod
	def onTarget():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return (client._send('distanceTo:', who) <= distance)
	#end:method

	@classmethod
	def setTarget():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case argc:
				super._send('setTarget:', &rest)
			#end:case
			case (not self._send('onTarget:')):
				super._send('setTarget:', who._send('x:'), who._send('y:'))
			#end:case
		)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if self._send('onTarget:'):
			self._send('moveDone:')
		else:
			super._send('doit:')
			if (b-moveCnt == 0):
				super._send('init:', client, who._send('x:'), who._send('y:'), caller)
			#endif
		#endif
	#end:method

#end:class or instance

