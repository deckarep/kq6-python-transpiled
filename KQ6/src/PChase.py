#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 930
import sci_sh
import kernel
import Main
import PolyPath
import System

class PChase(PolyPath):
	#property vars (may be empty)
	who = 0
	distance = 0
	targetX = 0
	targetY = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			(cond
				case (argc >= 5):
					obstacles = param5
				#end:case
				case (not kernel.IsObject(obstacles)):
					obstacles = global2._send('obstacles:')
				#end:case
			)
			if (argc >= 1):
				client = param1
				if (argc >= 2):
					who = param2
					targetX = who._send('x:')
					targetY = who._send('y:')
					if (argc >= 3):
						distance = param3
						if (argc >= 4):
							caller = param4
						#endif
					#endif
				#endif
			#endif
			super._send('init:', client, targetX, targetY, caller, 1, obstacles)
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
			#end:case
			case (temp0 = client._send('distanceTo:', who) <= distance):
				self._send('moveDone:')
			#end:case
			else:
				super._send('doit:')
			#end:else
		)
	#end:method

	@classmethod
	def moveDone():
		(cond
			case (temp0 = client._send('distanceTo:', who) <= distance):
				super._send('moveDone:')
			#end:case
			case (proc999_6(points, value) == 30583):
				if points:
					kernel.Memory(3, points)
				#endif
				points = 0
				value = 2
				self._send('init:', client, who)
			#end:case
			else:
				self._send('setTarget:', 'init:')
			#end:else
		)
	#end:method

#end:class or instance

