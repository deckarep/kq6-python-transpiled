#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 977
import sci_sh
import kernel
import Main
import StopWalk
import Sight
import Motion
import System

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = [2, 6, 4, 0, 3, 5, 1, 7]
local8 = [3, 6, 0, 4, 2, 5, 1, 7]


class Grooper(Code):
	#property vars (may be empty)
	client = 0
	oldCycler = 0
	oldMover = 0
	caller = 0
	
	@classmethod
	def doit(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not client):
			client = param1
		#endif
		if (argc >= 3):
			caller = param3
		#endif
		if ((client signal:) & 0x0800):
			if caller:
				(caller cue:)
			#endif
			caller = 0
			return
		#endif
		temp1 = (4 if (kernel.NumLoops(client) < 8) else 8)
		if ((not (global5 contains: client)) or ((argc >= 4) and param4)):
			(client
				loop:
					[local8
						(*
							(2 if (temp1 == 4) else 1)
							(/
								proc999_1(((client heading:) + (180 / temp1)), 360)
								(360 / temp1)
							)
						)
					]
			)
			if caller:
				(caller cue:)
			#endif
			caller = 0
			return
		#endif
		(= temp0
			if 
				(and
					((client loop:) == (kernel.NumLoops(client) - 1))
					((client cycler:) isKindOf: StopWalk)
					(((client cycler:) vStopped:) == -1)
				)
				local0[(client cel:)]
			else:
				local0[(client loop:)]
			#endif
		)
		if oldMover:
			(oldMover dispose:)
			oldMover = 0
		#endif
		if 
			(and
				kernel.IsObject(oldCycler)
				(or
					(oldCycler isMemberOf: Grycler)
					(not ((client cycler:) isMemberOf: Grycler))
				)
			)
			(oldCycler dispose:)
			oldCycler = 0
		#endif
		if (not oldCycler):
			oldCycler = (client cycler:)
		#endif
		if ((client cycler:) and ((client cycler:) isMemberOf: Grycler)):
			((client cycler:) dispose:)
		#endif
		oldMover = (client mover:)
		(client cycler: 0 mover: 0 setMotion: 0 setCycle: Grycler self temp0)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not kernel.IsObject((client mover:))):
			(client mover: oldMover)
		#endif
		if kernel.IsObject(oldCycler):
			(client cycler: oldCycler)
		#endif
		temp0 = caller
		caller = oldMover = oldCycler = 0
		if temp0:
			(temp0 cue: &rest)
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if kernel.IsObject(oldCycler):
			(oldCycler dispose:)
			oldCycler = 0
		#endif
		if kernel.IsObject(oldMover):
			(oldMover dispose:)
			oldMover = 0
		#endif
		if client:
			(client looper: 0)
		#endif
		(super dispose:)
	#end:method

#end:class or instance

class Grycler(Cycle):
	#property vars (may be empty)
	loopIndex = 0
	numOfLoops = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: param1)
		caller = param2
		numOfLoops = (4 if (kernel.NumLoops(client) < 8) else 8)
		cycleDir = -proc999_0(proc982_2((param3 * 45), (param1 heading:)))
		loopIndex = param3
		if (self loopIsCorrect:):
			if 
				(and
					(((client looper:) oldCycler:) isKindOf: StopWalk)
					((((client looper:) oldCycler:) vStopped:) == -1)
				)
				(client loop: local8[loopIndex])
			#endif
			(self cycleDone:)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(client loop: (self nextCel:))
		if (self loopIsCorrect:):
			(self cycleDone:)
		#endif
	#end:method

	@classmethod
	def cycleDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global37 = completed = 1
	#end:method

	@classmethod
	def loopIsCorrect():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(<
				kernel.Abs(proc982_2((loopIndex * 45), (client heading:)))
				((180 / numOfLoops) + 1)
			)
		)
	#end:method

	@classmethod
	def nextCel():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			if 
				(or
					(kernel.Abs((global88 - cycleCnt)) < (client cycleSpeed:))
					(self loopIsCorrect:)
				)
				(client loop:)
			else:
				cycleCnt = global88
				(loopIndex += (cycleDir * (8 / numOfLoops)))
				loopIndex = proc999_1(loopIndex, 8)
				local8[loopIndex]
			#endif
		)
	#end:method

#end:class or instance

