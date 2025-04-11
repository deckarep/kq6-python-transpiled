#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 945
import sci_sh
import Main
import Motion
import System

class PolyPath(Motion):
	#property vars (may be empty)
	value = 2
	points = 0
	finalX = 0
	finalY = 0
	obstacles = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, param6 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if argc:
			client = param1
			if (argc > 1):
				(cond
					case (argc >= 6):
						obstacles = param6
					#end:case
					case (not (IsObject obstacles)):
						obstacles = (global2 obstacles:)
					#end:case
				)
				if points:
					(Memory 3 points)
				#endif
				(= points
					(AvoidPath
						(param1 x:)
						(param1 y:)
						finalX = param2
						finalY = param3
						(obstacles and (obstacles elements:))
						(obstacles and (obstacles size:))
						(param5 if (argc >= 5) else 1)
					)
				)
				if (argc > 3):
					caller = param4
				#endif
			#endif
			(self setTarget:)
		#endif
		(super init:)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if points:
			(Memory 3 points)
		#endif
		points = 0
		(super dispose:)
	#end:method

	@classmethod
	def setTarget():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((proc999_6 points value) != 30583):
			x = (proc999_6 points value)
			y = (proc999_6 points value++)
			value++
			if ((IsObject global95) and temp3 = (global95 size:)):
				(= temp0
					(AvoidPath
						(client x:)
						(client y:)
						x
						y
						(global95 elements:)
						temp3
						0
					)
				)
				temp1 = (proc999_6 temp0 2)
				temp2 = (proc999_6 temp0 3)
				if ((x != temp1) or (y != temp2)):
					x = temp1
					y = temp2
					(Memory 6 (+ points value 2) 30583)
				#endif
				(Memory 3 temp0)
			#endif
		#endif
	#end:method

	@classmethod
	def moveDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((proc999_6 points value) == 30583):
			(super moveDone:)
		else:
			(self setTarget: init:)
		#endif
	#end:method

#end:class or instance

