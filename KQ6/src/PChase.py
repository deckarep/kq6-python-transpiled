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
					obstacles = (global2 obstacles:)
				#end:case
			)
			if (argc >= 1):
				client = param1
				if (argc >= 2):
					who = param2
					targetX = (who x:)
					targetY = (who y:)
					if (argc >= 3):
						distance = param3
						if (argc >= 4):
							caller = param4
						#endif
					#endif
				#endif
			#endif
			(super init: client targetX targetY caller 1 obstacles)
		else:
			(super init:)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (kernel.GetDistance(targetX, targetY, (who x:), (who y:)) > distance):
				if points:
					kernel.Memory(3, points)
				#endif
				points = 0
				value = 2
				(self init: client who)
			#end:case
			case (temp0 = (client distanceTo: who) <= distance):
				(self moveDone:)
			#end:case
			else:
				(super doit:)
			#end:else
		)
	#end:method

	@classmethod
	def moveDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (temp0 = (client distanceTo: who) <= distance):
				(super moveDone:)
			#end:case
			case (proc999_6(points, value) == 30583):
				if points:
					kernel.Memory(3, points)
				#endif
				points = 0
				value = 2
				(self init: client who)
			#end:case
			else:
				(self setTarget: init:)
			#end:else
		)
	#end:method

#end:class or instance

