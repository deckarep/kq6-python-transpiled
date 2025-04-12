#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 914
import sci_sh
import kernel
import Main
import EgoGroop
import Scaler
import Grooper
import Ego
import Motion

# Public Export Declarations
SCI.public_exports(
	Body = 0,
)

class Body(Ego):
	#property vars (may be empty)
	normal = 1
	currentSpeed = 0
	setHeadingCode = 0
	oldScaleSignal = 0
	oldMaxScale = 0
	oldBackSize = 0
	oldFrontY = 0
	oldBackY = 0
	oldXStep = 6
	oldYStep = 2
	
	@classmethod
	def setScale(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			(super setScale: param1 &rest)
		else:
			(super setScale:)
		#endif
		(scaleSignal |= 0x0004)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super doit:)
		(cond
			case (self isStopped:):
				if 
					(and
						(temp0 = loop != temp1 = (kernel.NumLoops(self) - 1))
						(global5 contains: self)
						(((global0 view:) == 900) or ((global0 view:) == 308))
						kernel.IsObject(cycler)
						(not (cycler isKindOf: Grycler))
						normal
					)
					(self loop: temp1 cel: temp0)
				#endif
			#end:case
			case 
				(and
					normal
					(loop == (kernel.NumLoops(self) - 1))
					(not (signal & 0x0800))
				):
				(self loop: cel)
			#end:case
		)
	#end:method

	@classmethod
	def findStep():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = (temp2 if temp2 = (scaleX / 15) else 1)
		temp1 = (temp2 if temp2 = (scaleY / 63) else 1)
		if ((temp0 != xStep) or (temp1 != yStep)):
			(self setStep: temp0 temp1 1)
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(= oldScaleSignal
			oldMaxScale = oldBackSize = oldFrontY = oldBackY = 0
		)
		(self setScale: 0)
		(super dispose:)
	#end:method

	@classmethod
	def setLoop(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(= temp0
				(cond
					case (argc == 0):
						(super setLoop:)
						0
					#end:case
					case (not kernel.IsObject(param1)):
						(super setLoop: param1 &rest)
						0
					#end:case
					else: param1#end:else
				)
			)
			if looper:
				(looper dispose:)
			#endif
			(looper = temp0 init: self &rest)
		#endif
	#end:method

	@classmethod
	def reset(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (argc > 0):
			(global0 loop: param1)
		#endif
		(global0
			view: (param2 if (argc > 1) else 900)
			signal: 4096
			z: 0
			setLoop: -1
			setLoop: global151
			setPri: -1
			setMotion: 0
			illegalBits: 0
			ignoreActors: 0
			ignoreHorizon: 1
			setStep: oldXStep oldYStep
			setCycle: Walk
			normal: 1
			setSpeed: currentSpeed
		)
		if (oldScaleSignal and (view == 900)):
			(cond
				case (oldScaleSignal & 0x0002):
					scaleSignal = oldScaleSignal
					maxScale = oldMaxScale
				#end:case
				case (oldMaxScale or oldBackSize or oldFrontY or oldBackY):
					(global0
						setScale:
							Scaler
							oldMaxScale
							oldBackSize
							oldFrontY
							oldBackY
					)
				#end:case
				else:
					(global0 setScale:)
				#end:else
			)
			(= oldScaleSignal
				oldMaxScale = oldBackSize = oldFrontY = oldBackY = 0
			)
		#endif
	#end:method

	@classmethod
	def put():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super put: &rest)
		(global69 curIcon: (global69 walkIconItem:))
	#end:method

	@classmethod
	def setHeading(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			heading = param1
		#endif
		(cond
			case setHeadingCode:
				(setHeadingCode doit: heading &rest)
			#end:case
			case 
				(and
					kernel.IsObject((global0 looper:))
					((global0 looper:) isKindOf: EgoGroop)
					(not (looper dontHead:))
				):
				(looper doit: self heading ((argc >= 2) and param1[1]))
			#end:case
			else:
				if kernel.IsObject((global0 looper:)):
					if (not ((global0 looper:) isKindOf: EgoGroop)):
						temp0 = 1
					else:
						temp0 = 0
					#endif
				else:
					temp0 = 1
				#endif
				if temp0:
					kernel.DirLoop(self, heading)
				#endif
				if ((argc >= 2) and kernel.IsObject(param1[1])):
					(param1[1] cue: &rest)
				#endif
			#end:else
		)
	#end:method

#end:class or instance

