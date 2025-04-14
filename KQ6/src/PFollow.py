#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 932
import sci_sh
import kernel
import Main
import PolyPath

class PFollow(PolyPath):
	#property vars (may be empty)
	who = 0
	distance = 0
	targetX = 0
	targetY = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			(= temp0
				if (argc >= 4):
					param4
				else:
					global2._send('obstacles:')
				#endif
			)
			if (argc >= 1):
				client = param1
				if (argc >= 2):
					who = param2
					targetX = who._send('x:')
					targetY = who._send('y:')
					if (argc >= 3):
						distance = param3
					#endif
				#endif
			#endif
			super._send('init:', client, targetX, targetY, 0, 1, temp0)
		else:
			super._send('init:')
		#endif
	#end:method

	@classmethod
	def doit():
		(cond
			case (kernel.GetDistance(targetX, targetY, who._send('x:'), who._send('y:')) > distance):
				if points:
					kernel.Memory(3, points)
				#endif
				points = 0
				value = 2
				self._send('init:', client, who)
				0
			#end:case
			case (temp0 = client._send('distanceTo:', who) <= distance):
				temp1 = kernel.GetAngle(client._send('x:'), client._send('y:'), who._send('x:'), who._send('y:'))
				if (client._send('heading:') != temp1):
					client._send('setHeading:', temp1)
				#endif
				xLast = client._send('x:')
				yLast = client._send('y:')
				b-moveCnt = global88
				0
			#end:case
			else:
				super._send('doit:')
			#end:else
		)
	#end:method

	@classmethod
	def moveDone():
		self._send('setTarget:', 'init:')
	#end:method

#end:class or instance

