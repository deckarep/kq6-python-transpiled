#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 968
import sci_sh
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	SmoothLooper = 0,
)

class SmoothLooper(Code):
	#property vars (may be empty)
	nextLoop = 0
	client = 0
	oldCycler = 0
	oldMover = 0
	newMover = 0
	oldCycleSpeed = 0
	cycleSpeed = 0
	inProgress = 0
	vNormal = 0
	vChangeDir = 0
	
	@classmethod
	def doit(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((param1 signal:) & 0x0800):
			return
		#endif
		temp1 = 0
		if inProgress:
			if newMover:
				(newMover dispose:)
			#endif
			newMover = (param1 mover:)
			(param1 mover: 0)
			return
		else:
			if (not vNormal):
				vNormal = (param1 view:)
			#endif
			client = param1
			inProgress = 1
		#endif
		if (((client loop:) > 3) and ((client view:) == vNormal)):
			if inProgress:
				if (IsObject oldMover):
					(oldMover dispose:)
				#endif
			else:
				(client view: vNormal)
				(DirLoop client param2)
			#endif
		#endif
		match temp0 = (client loop:)
			case 3:
				(cond
					case ((param2 <= 45) or (param2 > 315)):#end:case
					case (param2 <= 135):
						temp0 = 4
						nextLoop = 0
						temp1 = 1
					#end:case
					case (param2 <= 225):
						temp0 = 4
						nextLoop = 16
						temp1 = 1
					#end:case
					case (param2 <= 315):
						temp0 = 5
						temp1 = nextLoop = 1
					#end:case
				)
			#end:case
			case 0:
				(cond
					case ((param2 <= 45) or (param2 > 315)):
						temp0 = 6
						nextLoop = 3
						temp1 = 1
					#end:case
					case (param2 <= 135):#end:case
					case (param2 <= 225):
						temp0 = 0
						nextLoop = 2
						temp1 = 1
					#end:case
					case (param2 <= 315):
						temp0 = 6
						nextLoop = 21
						temp1 = 1
					#end:case
				)
			#end:case
			case 1:
				(cond
					case ((param2 <= 45) or (param2 > 315)):
						temp0 = 7
						nextLoop = 3
						temp1 = 1
					#end:case
					case (param2 <= 135):
						temp0 = 1
						nextLoop = 18
						temp1 = 1
					#end:case
					case (param2 <= 225):
						temp0 = 1
						nextLoop = 2
						temp1 = 1
					#end:case
					else:
						(param2 <= 315)
					#end:else
				)
			#end:case
			case 2:
				(cond
					case ((param2 <= 45) or (param2 > 315)):
						temp0 = 3
						nextLoop = 23
						temp1 = 1
					#end:case
					case (param2 <= 135):
						temp0 = 2
						nextLoop = 0
						temp1 = 1
					#end:case
					case (param2 <= 225):#end:case
					case (param2 <= 315):
						temp0 = 3
						temp1 = nextLoop = 1
					#end:case
				)
			#end:case
		#end:match
		if temp1:
			oldCycler = (client cycler:)
			oldMover = (client mover:)
			oldCycleSpeed = (client cycleSpeed:)
			(client
				view: vChangeDir
				cycleSpeed: cycleSpeed
				mover: 0
				cycler: 0
				loop: temp0
				cel: 0
				setCycle: End self
			)
		else:
			inProgress = 0
		#endif
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (nextLoop < 15):
			(client
				view: vNormal
				loop: nextLoop
				mover: oldMover
				cycler: oldCycler
				cycleSpeed: oldCycleSpeed
			)
			inProgress = oldCycler = oldMover = 0
			if newMover:
				(client setMotion: newMover)
				newMover = 0
			#endif
		else:
			(nextLoop -= 16)
			(client loop: nextLoop cel: 0 setCycle: End self)
			(= nextLoop
				match nextLoop
					case 0: 2#end:case
					case 5: 1#end:case
					case 2: 0#end:case
					case 7: 3#end:case
				#end:match
			)
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if oldMover:
			(oldMover dispose:)
		#endif
		if newMover:
			(newMover dispose:)
		#endif
		if oldCycler:
			(oldCycler dispose:)
		#endif
		inProgress = oldMover = newMover = oldCycler = 0
		(client view: vNormal looper: 0)
		(DirLoop client (client heading:))
		(super dispose:)
	#end:method

#end:class or instance

