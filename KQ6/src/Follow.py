#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 971
import sci_sh
import kernel
import Motion

class Follow(Motion):
	#property vars (may be empty)
	who = 0
	distance = 20
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (argc >= 1):
			client = param1
			if (argc >= 2):
				who = param2
				if (argc >= 3):
					distance = param3
				#endif
			#endif
		#endif
		if (client._send('distanceTo:', who) > distance):
			super._send('init:', client, who._send('x:'), who._send('y:'))
		#endif
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

		if (client._send('distanceTo:', who) > distance):
			if (b-moveCnt == 0):
				super._send('init:', client, who._send('x:'), who._send('y:'))
			#endif
			super._send('doit:')
		else:
			xLast = client._send('x:')
			yLast = client._send('y:')
			if 
				(!=
					temp0 = kernel.GetAngle(xLast, yLast, who._send('x:'), who._send('y:'))
					client._send('heading:')
				)
				client._send('heading:', temp0)
				if client._send('looper:'):
					client._send('looper:')._send('doit:', client, temp0)
				else:
					kernel.DirLoop(client, temp0)
				#endif
			#endif
		#endif
	#end:method

	@classmethod
	def moveDone():#end:method

#end:class or instance

