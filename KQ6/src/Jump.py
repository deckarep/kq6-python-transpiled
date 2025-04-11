#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 991
import sci_sh
import Main
import Motion

class Jump(Motion):
	#property vars (may be empty)
	x = 20000
	y = 20000
	gx = 0
	gy = 3
	xStep = 20000
	yStep = 0
	signal = 0
	illegalBits = 0
	waitApogeeX = 1
	waitApogeeY = 1
	
	@classmethod
	def init(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		client = param1
		if (argc == 2):
			caller = param2
		#endif
		illegalBits = (client illegalBits:)
		signal = (client signal:)
		(client illegalBits: 0 setPri:)
		if (xStep == 20000):
			(= xStep
				(cond
					case 
						(or
							(temp0 = (client heading:) > 330)
							(temp0 < 30)
							(< 150 temp0 210)
						):
						0
					#end:case
					case (temp0 < 180):
						(client xStep:)
					#end:case
					else:
						(- (client xStep:))
					#end:else
				)
			)
		#endif
		if (not (waitApogeeX and ((xStep * gx) < 0))):
			waitApogeeX = 0
		#endif
		if (not (waitApogeeY and ((yStep * gy) < 0))):
			waitApogeeY = 0
		#endif
		b-moveCnt = global88
		(self setTest:)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((Abs (global88 - b-moveCnt)) >= (client moveSpeed:)):
			b-moveCnt = global88
			xLast = (client x:)
			yLast = (client y:)
			(client x: (xLast + xStep) y: (yLast + yStep))
			temp0 = xStep
			temp1 = yStep
			(xStep += gx)
			(yStep += gy)
			if 
				(and
					(not waitApogeeX)
					(x != 20000)
					(0 <= (dx * ((client x:) - x)))
				)
				(client x: x)
				(self moveDone:)
				return
			#endif
			if 
				(and
					(not waitApogeeY)
					(y != 20000)
					(0 <= (dy * ((client y:) - y)))
				)
				(client y: y)
				(self moveDone:)
				return
			#endif
			if ((temp0 * xStep) <= 0):
				waitApogeeX = 0
				(self setTest:)
			#endif
			if ((temp1 * yStep) <= 0):
				waitApogeeY = 0
				(self setTest:)
			#endif
		#endif
	#end:method

	@classmethod
	def moveDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(client illegalBits: illegalBits signal: signal)
		if caller:
			global37 = 1
			completed = 1
		#endif
	#end:method

	@classmethod
	def setTest():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(= dx
			if (((client x:) > x) or (((client x:) == x) and (xStep > 0))):
				-1
			else:
				1
			#endif
		)
		(= dy
			if (((client y:) > y) or (((client y:) == y) and (yStep > 0))):
				-1
			else:
				1
			#endif
		)
	#end:method

	@classmethod
	def motionCue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(client mover: 0)
		if (completed and (IsObject caller)):
			(caller cue:)
		#endif
		(self dispose:)
	#end:method

#end:class or instance

class JumpTo(Jump):
	#property vars (may be empty)
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		client = param1
		x = param2
		y = param3
		if ((x == (param1 x:)) and (y == (param1 y:))):
			illegalBits = (client illegalBits:)
			signal = (client signal:)
			(self moveDone:)
			return
		#endif
		temp0 = (x - (param1 x:))
		temp1 = (y - (param1 y:))
		(SetJump self temp0 temp1 gy)
		if (not temp0):
			x = 20000
		#endif
		if (not temp1):
			y = 20000
		#endif
		match argc
			case 3:
				(super init: param1)
			#end:case
			case 4:
				(super init: param1 param4)
			#end:case
		#end:match
	#end:method

	@classmethod
	def moveDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (x != 20000):
			(client x: x)
		#endif
		if (y != 20000):
			(client y: y)
		#endif
		(super moveDone:)
	#end:method

#end:class or instance

