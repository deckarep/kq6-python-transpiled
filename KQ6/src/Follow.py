#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 971
import sci_sh
import Motion

class Follow(Motion):
	#property vars (may be empty)
	who = 0
	distance = 20
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (argc >= 1):
			client = param1
			if (argc >= 2):
				who = param2
				if (argc >= 3):
					distance = param3
				#endif
			#endif
		#endif
		if ((client distanceTo: who) > distance):
			(super init: client (who x:) (who y:))
		#endif
	#end:method

	@classmethod
	def onTarget():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		return ((client distanceTo: who) <= distance)
	#end:method

	@classmethod
	def setTarget():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case argc:
				(super setTarget: &rest)
			#end:case
			case (not (self onTarget:)):
				(super setTarget: (who x:) (who y:))
			#end:case
		)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((client distanceTo: who) > distance):
			if (b-moveCnt == 0):
				(super init: client (who x:) (who y:))
			#endif
			(super doit:)
		else:
			xLast = (client x:)
			yLast = (client y:)
			if 
				(!=
					temp0 = (GetAngle xLast yLast (who x:) (who y:))
					(client heading:)
				)
				(client heading: temp0)
				if (client looper:):
					((client looper:) doit: client temp0)
				else:
					(DirLoop client temp0)
				#endif
			#endif
		#endif
	#end:method

	@classmethod
	def moveDone():#end:method

#end:class or instance

