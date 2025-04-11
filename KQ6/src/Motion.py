#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 992
import sci_sh
import kernel
import Main
import System

class Cycle(Obj):
	#property vars (may be empty)
	client = 0
	caller = 0
	cycleDir = 1
	cycleCnt = 0
	completed = 0
	
	@classmethod
	def init(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if argc:
			client = param1
		#endif
		cycleCnt = global88
		completed = 0
	#end:method

	@classmethod
	def nextCel():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			if (kernel.Abs((global88 - cycleCnt)) < (client cycleSpeed:)):
				(client cel:)
			else:
				cycleCnt = global88
				((client cel:) + cycleDir)
			#endif
		)
	#end:method

	@classmethod
	def cycleDone():#end:method

	@classmethod
	def motionCue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(client cycler: 0)
		if (completed and kernel.IsObject(caller)):
			(caller cue:)
		#endif
		(self dispose:)
	#end:method

#end:class or instance

class Fwd(Cycle):
	#property vars (may be empty)
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (temp0 = (self nextCel:) > (client lastCel:)):
			(self cycleDone:)
		else:
			(client cel: temp0)
		#endif
	#end:method

	@classmethod
	def cycleDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(client cel: 0)
	#end:method

#end:class or instance

class Walk(Fwd):
	#property vars (may be empty)
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not (client isStopped:)):
			(super doit:)
		#endif
	#end:method

#end:class or instance

class CT(Cycle):
	#property vars (may be empty)
	endCel = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: param1)
		cycleDir = param3
		if (argc == 4):
			caller = param4
		#endif
		temp0 = (client lastCel:)
		endCel = (temp0 if (param2 > temp0) else param2)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp1 = (client lastCel:)
		if (endCel > temp1):
			endCel = temp1
		#endif
		temp0 = (self nextCel:)
		(client
			cel:
				(cond
					case (temp0 > temp1): 0#end:case
					case (temp0 < 0): temp1#end:case
					else: temp0#end:else
				)
		)
		if ((global88 == cycleCnt) and (endCel == (client cel:))):
			(self cycleDone:)
		#endif
	#end:method

	@classmethod
	def cycleDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		completed = 1
		if caller:
			global37 = 1
		else:
			(self motionCue:)
		#endif
	#end:method

#end:class or instance

class End(CT):
	#property vars (may be empty)
	@classmethod
	def init(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: param1 (param1 lastCel:) 1 (param2 if (argc == 2) else 0))
	#end:method

#end:class or instance

class Beg(CT):
	#property vars (may be empty)
	@classmethod
	def init(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: param1 0 -1 (param2 if (argc == 2) else 0))
	#end:method

#end:class or instance

class SyncWalk(Fwd):
	#property vars (may be empty)
	xLast = 0
	yLast = 0
	
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if 
			(and
				kernel.IsObject(temp0 = (client mover:))
				(((client x:) != xLast) or ((client y:) != yLast))
			)
			xLast = (client x:)
			yLast = (client y:)
			(super doit:)
		#endif
	#end:method

	@classmethod
	def nextCel():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		cycleCnt = (global88 + (client cycleSpeed:))
		(super nextCel:)
	#end:method

#end:class or instance

class Motion(Obj):
	#property vars (may be empty)
	client = 0
	caller = 0
	x = 0
	y = 0
	dx = 0
	dy = 0
	b-moveCnt = 0
	b-i1 = 0
	b-i2 = 0
	b-di = 0
	b-xAxis = 0
	b-incr = 0
	completed = 0
	xLast = 0
	yLast = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (argc >= 1):
			client = param1
			if (argc >= 2):
				x = param2
				if (argc >= 3):
					y = param3
					if (argc >= 4):
						caller = param4
					#endif
				#endif
			#endif
		#endif
		yLast = xLast = completed = 0
		b-moveCnt = (+ 1 (client moveSpeed:) global88)
		if temp3 = (client cycler:):
			(temp3 cycleCnt: b-moveCnt)
		#endif
		if kernel.GetDistance(temp2 = (client x:), temp3 = (client y:), x, y):
			(client setHeading: kernel.GetAngle(temp2, temp3, x, y))
		#endif
		kernel.InitBresen(self)
	#end:method

	@classmethod
	def onTarget():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		return (((client x:) == x) and ((client y:) == y))
	#end:method

	@classmethod
	def setTarget(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if argc:
			x = param1
			y = param2
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (kernel.Abs((global88 - b-moveCnt)) >= (client moveSpeed:)):
			b-moveCnt = global88
			kernel.DoBresen(self)
		#endif
	#end:method

	@classmethod
	def moveDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		completed = 1
		if caller:
			global37 = 1
		else:
			(self motionCue:)
		#endif
	#end:method

	@classmethod
	def motionCue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(client mover: 0)
		if (completed and kernel.IsObject(caller)):
			(caller cue:)
		#endif
		(self dispose:)
	#end:method

#end:class or instance

class MoveTo(Motion):
	#property vars (may be empty)
	@classmethod
	def onTarget():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(and
				(kernel.Abs(((client x:) - x)) <= (client xStep:))
				(kernel.Abs(((client y:) - y)) <= (client yStep:))
			)
		)
	#end:method

#end:class or instance

