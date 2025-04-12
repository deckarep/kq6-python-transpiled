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
					(global2 obstacles:)
				#endif
			)
			if (argc >= 1):
				client = param1
				if (argc >= 2):
					who = param2
					targetX = (who x:)
					targetY = (who y:)
					if (argc >= 3):
						distance = param3
					#endif
				#endif
			#endif
			(super init: client targetX targetY 0 1 temp0)
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
				0
			#end:case
			case (temp0 = (client distanceTo: who) <= distance):
				temp1 = kernel.GetAngle((client x:), (client y:), (who x:), (who y:))
				if ((client heading:) != temp1):
					(client setHeading: temp1)
				#endif
				xLast = (client x:)
				yLast = (client y:)
				b-moveCnt = global88
				0
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

		(self setTarget: init:)
	#end:method

#end:class or instance

