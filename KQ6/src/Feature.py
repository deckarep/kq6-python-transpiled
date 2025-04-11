#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 950
import sci_sh
import Main
import PolyPath
import System

class CueObj(Script):
	#property vars (may be empty)
	theVerb = 0
	
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 1:
				(global0
					setHeading:
						(GetAngle
							(global0 x:)
							(global0 y:)
							(client x:)
							(client y:)
						)
						self
				)
				(global78 add: self)
			#end:case
			case 2:
				cycles = 3
			#end:case
			case 3:
				(global78 delete: self)
				if 
					(not
						(and
							(IsObject client)
							(IsObject (client actions:))
							((client actions:) doVerb: theVerb)
						)
					)
					(client doVerb: theVerb)
				#endif
				state = 0
			#end:case
		#end:match
	#end:method

#end:class or instance

class Feature(Obj):
	#property vars (may be empty)
	x = 0
	y = 0
	z = 0
	heading = 0
	noun = 0
	modNum = -1
	nsTop = 0
	nsLeft = 0
	nsBottom = 0
	nsRight = 0
	sightAngle = 26505
	actions = 0
	onMeCheck = 26505
	state = 0
	approachX = 0
	approachY = 0
	approachDist = 0
	_approachVerbs = 0
	
	@classmethod
	def init(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self initialize: (param1 if argc else 0))
		if (self respondsTo: #underBits):
			(global5 add: self)
		else:
			(global32 add: self)
		#endif
	#end:method

	@classmethod
	def initialize(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (argc and param1):
				(self perform: param1)
			#end:case
			case global64:
				(self perform: global64)
			#end:case
		)
	#end:method

	@classmethod
	def approachVerbs(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		_approachVerbs = 0
		if (and argc global66 param1[0]):
			temp0 = 0
			while (temp0 < argc): # inline for
				temp1 = (global66 doit: param1[temp0])
				(self _approachVerbs: (| (self _approachVerbs:) temp1))
				# for:reinit
				temp0++
			#end:loop
		#endif
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (param1 claimed:):
				return 1
			#end:case
			case 
				(and
					((param1 type:) & 0x4000)
					(self onMe: param1)
					(self isNotHidden:)
				):
				(CueObj
					state: 0
					cycles: 0
					client: self
					theVerb: (param1 message:)
				)
				(param1 claimed: 1)
				if 
					(and
						(global80 canControl:)
						((global0 state:) & 0x0002)
						(>
							(GetDistance
								(global0 x:)
								(global0 y:)
								approachX
								approachY
							)
							approachDist
						)
						global66
						(_approachVerbs & (global66 doit: (param1 message:)))
					)
					(global0
						setMotion:
							PolyPath
							approachX
							((global0 z:) + approachY)
							CueObj
					)
				else:
					(global0 setMotion: 0)
					if (self facingMe:):
						(CueObj changeState: 3)
					#endif
				#endif
			#end:case
		)
		(param1 claimed:)
	#end:method

	@classmethod
	def notFacing():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global0 setMotion: 0)
		(CueObj client: self state: 0 cycles: 0 cue:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (global65 if global65 else dftDoVerb)
		if (modNum == -1):
			modNum = global11
		#endif
		if (global90 and (Message 0 modNum noun param1 0 1)):
			(global91 say: noun param1 0 0 0 modNum)
		else:
			(temp0 doit: param1 self)
		#endif
	#end:method

	@classmethod
	def facingMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case argc:
				temp0 = param1
			#end:case
			case (global5 contains: global0):
				temp0 = global0
			#end:case
			else:
				return 1
			#end:else
		)
		if 
			(>
				(= temp1
					(Abs
						(-
							(GetAngle (temp0 x:) (temp0 y:) x y)
							(temp0 heading:)
						)
					)
				)
				180
			)
			temp1 = (360 - temp1)
		#endif
		if (temp1 <= sightAngle):
			return 1
		else:
			if (sightAngle != 26505):
				(self notFacing:)
			#endif
			return 0
		#endif
	#end:method

	@classmethod
	def isNotHidden():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		return 1
	#end:method

	@classmethod
	def onMe(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (IsObject param1):
			temp0 = (param1 x:)
			temp1 = (param1 y:)
		else:
			temp0 = param1
			temp1 = param2
		#endif
		(return
			(cond
				case (state & 0x0004):
					if 
						(or
							(not (or nsLeft nsRight nsTop nsBottom))
							(and
								(<= nsLeft temp0 nsRight)
								(<= nsTop temp1 nsBottom)
							)
						)
						(onMeCheck & (OnControl 4 temp0 temp1))
					else:
						0
					#endif
				#end:case
				case (IsObject onMeCheck):
					(AvoidPath temp0 temp1 onMeCheck)
				#end:case
				case 
					(or
						(not (or nsLeft nsRight nsTop nsBottom))
						(and
							(<= nsLeft temp0 nsRight)
							(<= nsTop temp1 nsBottom)
						)
					):
					1
				#end:case
				else: 0#end:else
			)
		)
	#end:method

	@classmethod
	def setName(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(state |= 0x0001)
		name = (Memory 1 ((StrLen param1) + 1))
		(StrCpy name param1)
	#end:method

	@classmethod
	def setOnMeCheck(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 26505:
				onMeCheck = param1
				(state &= 0xfffb)
			#end:case
			case 2:
				onMeCheck = param2[0]
				(state &= 0xfffb)
			#end:case
			case 1:
				temp0 = onMeCheck = 0
				while (temp0 < (argc - 1)): # inline for
					(onMeCheck |= param2[temp0])
					# for:reinit
					temp0++
				#end:loop
				(state |= 0x0004)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if actions:
			(actions dispose:)
			actions = 0
		#endif
		if ((IsObject onMeCheck) and (not (state & 0x0004))):
			(onMeCheck dispose:)
			onMeCheck = 0
		#endif
		(global32 delete: self)
		if (state & 0x0001):
			(Memory 3 name)
			name = 0
		#endif
		(super dispose:)
	#end:method

#end:class or instance

@SCI.instance
class dftDoVerb(Code):
	#property vars (may be empty)
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		return 1
	#end:method

#end:class or instance

class Actions(Code):
	#property vars (may be empty)
	@classmethod
	def doVerb():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		return 0
	#end:method

#end:class or instance

