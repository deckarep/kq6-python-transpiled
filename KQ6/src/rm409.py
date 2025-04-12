#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 409
import sci_sh
import kernel
import Main
import rLab
import n404
import KQ6Room
import n913
import RandCycle
import PolyPath
import Polygon
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm409 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.instance
class rm409(KQ6Room):
	#property vars (may be empty)
	modNum = 400
	noun = 2
	picture = 400
	style = 10
	horizon = 135
	south = 400
	walkOffEdge = 1
	autoLoad = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (rLab hiddenDoorOpen:):
			local0 = 54
			(global2
				addObstacle:
					((Polygon new:)
						type: 2
						init:
							232
							144
							83
							144
							26
							185
							130
							185
							130
							189
							0
							189
							0
							0
							319
							4
							319
							171
							238
							171
							242
							154
						yourself:
					)
					((Polygon new:)
						type: 2
						init: 319 189 192 189 192 184 319 184
						yourself:
					)
			)
		else:
			if (rLab seenSecretLatch:):
				local0 = 53
			else:
				local0 = 55
			#endif
			(global2
				addObstacle:
					((Polygon new:)
						type: 2
						init:
							0
							189
							0
							0
							319
							0
							319
							189
							190
							189
							190
							185
							266
							185
							237
							161
							235
							143
							86
							143
							39
							185
							130
							185
							130
							189
						yourself:
					)
			)
		#endif
		(super init: &rest)
		if ((kernel.ScriptID(30, 0) holeCoords:) == global11):
			proc404_1()
		#endif
		(kernel.ScriptID(30, 0) initCrypt: 1)
		(tapestry init:)
		(openDoor init:)
		(door init:)
		(myTorch init:)
		(self setScript: walkIn)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (global2 script:):#end:case
			case (global0 inRect: 287 167 319 189):
				(kernel.ScriptID(30, 0) prevEdgeHit: 2)
				(global2 setScript: walkOut)
			#end:case
			case ((global0 edgeHit:) == 3):
				(kernel.ScriptID(30, 0) prevEdgeHit: 3)
				(global2 setScript: walkOut)
			#end:case
		)
		(super doit: &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			match param1
				case 1:
					if (rLab hiddenDoorOpen:):
						(global91 say: 2 1 54 1 0 400)
						1
					else:
						(global91 say: 2 1 53 1 0 400)
						1
					#endif
				#end:case
				else:
					(super doVerb: param1 &rest)
				#end:else
			#end:match
		)
	#end:method

#end:class or instance

@SCI.instance
class tapestry(Prop):
	#property vars (may be empty)
	x = 246
	y = 189
	z = 100
	noun = 18
	modNum = 400
	view = 400
	loop = 5
	priority = 5
	signal = 26640
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self stopUpd:)
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 0:
				if (rLab seenSecretLatch:):
					0
				else:
					(global91 say: 19 0 55 1 0 400)
				#endif
			#end:case
			case 5:
				if (rLab hiddenDoorOpen:):
					(global2 setScript: lookAtTapestry)
				else:
					(global2 setScript: liftTapestry)
				#endif
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class door(Prop):
	#property vars (may be empty)
	x = 278
	y = 189
	z = 73
	noun = 19
	modNum = 400
	approachX = 260
	approachY = 170
	view = 402
	loop = 3
	priority = 13
	signal = 16400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self approachVerbs: 5)
		if (rLab hiddenDoorOpen:):
			(self cel: 5 stopUpd:)
		else:
			(self cel: 0 stopUpd:)
		#endif
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 25:
				proc404_0(2)
			#end:case
			case 1:
				(global91 say: 19 1 local0 1 0 400)
			#end:case
			case 5:
				(global91 say: 19 5 local0 1 0 400)
			#end:case
			case 2:
				(cond
					case (not (rLab seenSecretLatch:)):
						(global91 say: 19 2 55 1 0 400)
					#end:case
					case 
						(and
							(rLab seenSecretLatch:)
							(not (rLab hiddenDoorOpen:))
						):
						(global91 say: 19 2 53 1 0 400)
					#end:case
					case ((rLab hiddenDoorOpen:) and (not proc913_0(1))):
						(global91 say: 19 2 56 1 0 400)
					#end:case
					case proc913_0(1):
						(global91 say: 19 2 57 1 0 400)
					#end:case
				)
			#end:case
			else:
				(cond
					case (not (rLab seenSecretLatch:)):
						(global91 say: 19 0 55 1 0 400)
					#end:case
					case 
						(and
							(rLab seenSecretLatch:)
							(not (rLab hiddenDoorOpen:))
						):
						(global91 say: 19 0 53 1 0 400)
					#end:case
					else:
						(global91 say: 19 0 54 1 0 400)
					#end:else
				)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class openDoor(View):
	#property vars (may be empty)
	x = 278
	y = 189
	z = 73
	noun = 19
	modNum = 400
	approachX = 260
	approachY = 170
	view = 402
	loop = 2
	priority = 13
	signal = 16400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self approachVerbs: 5)
		(self stopUpd:)
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(door doVerb: param1 &rest)
	#end:method

#end:class or instance

@SCI.instance
class myTorch(View):
	#property vars (may be empty)
	x = 77
	y = 141
	z = 71
	noun = 9
	modNum = 400
	view = 400
	loop = 8
	priority = 14
	signal = 17
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self stopUpd:)
		(super init:)
		(myFlame init:)
		(myFlick init:)
	#end:method

#end:class or instance

@SCI.instance
class myFlame(Prop):
	#property vars (may be empty)
	x = 84
	y = 141
	z = 95
	noun = 9
	modNum = 400
	view = 400
	loop = 2
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self setCycle: Fwd checkDetail:)
		(super init:)
	#end:method

#end:class or instance

@SCI.instance
class myFlick(Prop):
	#property vars (may be empty)
	x = 82
	y = 50
	modNum = 400
	onMeCheck = 0
	view = 400
	loop = 6
	signal = 16401
	cycleSpeed = 9
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self setCycle: RandCycle checkDetail:)
		(super init:)
	#end:method

#end:class or instance

@SCI.instance
class mino(Actor):
	#property vars (may be empty)
	x = 315
	y = 171
	yStep = 3
	view = 443
	signal = 16384
	xStep = 5
	
#end:class or instance

@SCI.instance
class walkIn(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				match (kernel.ScriptID(30, 0) prevEdgeHit:)
					case 4:
						(global0
							posn: 282 164
							init:
							setMotion: PolyPath 247 164 self
						)
					#end:case
					case 1:
						(global0
							posn: 158 225
							init:
							setMotion: PolyPath 158 187 self
						)
					#end:case
					else:
						(global0 posn: 160 160 loop: 2 init:)
						ticks = 6
					#end:else
				#end:match
			#end:case
			case 1:
				cycles = 6
			#end:case
			case 2:
				if ((global12 == 440) and (not proc913_0(1))):
					proc913_1(142)
					(global91 say: 1 0 50 1 self 400)
				else:
					(self cue:)
				#endif
			#end:case
			case 3:
				(global1 handsOn:)
				(global69 enable: 6)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walkOut(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				match (kernel.ScriptID(30, 0) prevEdgeHit:)
					case 3:
						(global0 setMotion: PolyPath (global0 x:) 250 self)
					#end:case
					case 2:
						(global0 setMotion: PolyPath 315 (global0 y:) self)
					#end:case
				#end:match
			#end:case
			case 1:
				match (kernel.ScriptID(30, 0) prevEdgeHit:)
					case 3:
						(global2 newRoom: 400)
					#end:case
					case 2:
						(global2 newRoom: 440)
					#end:case
				#end:match
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lookAtTapestry(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: PolyPath 235 149 self)
			#end:case
			case 1:
				(global0 setHeading: 90)
				cycles = 6
			#end:case
			case 2:
				(global91 say: 18 5 54 1 self 400)
			#end:case
			case 3:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class liftTapestry(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: PolyPath 229 146 self)
			#end:case
			case 1:
				(global0 setHeading: 90)
				cycles = 6
			#end:case
			case 2:
				if (rLab seenSecretLatch:):
					local1 = 1
					local0 = 53
					(global91 say: 18 5 53 1 self 400)
				else:
					(self cue:)
				#endif
			#end:case
			case 3:
				(global0
					view: 401
					setLoop: 3
					cel: 0
					normal: 0
					illegalBits: 0
					ignoreActors: 1
					cycleSpeed: 12
					posn: ((global0 x:) + 6) ((global0 y:) + 3)
					setCycle: CT 3 1 self
				)
			#end:case
			case 4:
				(global0 cel: 4)
				(tapestry startUpd: cel: 1)
				cycles = 2
			#end:case
			case 5:
				(global0 cel: 5)
				(tapestry cel: 2)
				cycles = 2
			#end:case
			case 6:
				if local1:
					(global0
						setLoop: 4
						cel: 0
						posn: ((global0 x:) + 3) (global0 y:)
						setCycle: CT 5 1 self
					)
				else:
					(self cue:)
				#endif
			#end:case
			case 7:
				if local1:
					(global0 cel: 6)
					cycles = 6
				else:
					(self cue:)
				#endif
			#end:case
			case 8:
				if local1:
					(global0 cel: 5)
					cycles = 6
				else:
					(self cue:)
				#endif
			#end:case
			case 9:
				if local1:
					(global0 cel: 4)
					cycles = 6
				else:
					(self cue:)
				#endif
			#end:case
			case 10:
				if local1:
					(global0 cel: 5)
					cycles = 6
				else:
					(self cue:)
				#endif
			#end:case
			case 11:
				if local1:
					(global91 say: 18 5 53 2 self 400)
				else:
					(global91 say: 18 5 55 1 self 400)
				#endif
			#end:case
			case 12:
				if local1:
					(global0 cel: 4)
					cycles = 6
				else:
					(self cue:)
				#endif
			#end:case
			case 13:
				if local1:
					(global0 cel: 5)
					cycles = 6
				else:
					(self cue:)
				#endif
			#end:case
			case 14:
				if local1:
					(global0 cel: 4)
					cycles = 6
				else:
					(self cue:)
				#endif
			#end:case
			case 15:
				if local1:
					(global105 number: 408 setLoop: 1 play:)
					(global0 cel: 5)
					cycles = 6
				else:
					(self cue:)
				#endif
			#end:case
			case 16:
				if local1:
					(global91 say: 18 5 53 3 self 400)
				else:
					(self cue:)
				#endif
			#end:case
			case 17:
				if local1:
					(global0 cel: 6)
					(tapestry setCycle: Beg self)
				else:
					(self cue:)
				#endif
			#end:case
			case 18:
				if local1:
					(global105 number: 909 setLoop: 1 play:)
					(door setCycle: End self)
					(rLab hiddenDoorOpen: 1)
					((global2 obstacles:) dispose:)
					local0 = 54
				else:
					(self cue:)
				#endif
			#end:case
			case 19:
				if local1:
					(door dispose:)
					(global2
						addObstacle:
							((Polygon new:)
								type: 2
								init:
									232
									144
									83
									144
									26
									185
									130
									185
									130
									189
									0
									189
									0
									0
									319
									4
									319
									171
									238
									171
									242
									154
								yourself:
							)
							((Polygon new:)
								type: 2
								init: 319 189 192 189 192 184 319 184
								yourself:
							)
					)
					(global91 say: 18 5 53 4 self 400)
				else:
					(self cue:)
				#endif
			#end:case
			case 20:
				if local1:
					(global1 givePoints: 1)
					(self cue:)
				else:
					(tapestry cel: 1)
					(global0 setLoop: 3 cel: 5)
					cycles = 2
				#endif
			#end:case
			case 21:
				if local1:
					(self cue:)
				else:
					(tapestry cel: 0)
					(global0 cel: 4)
					cycles = 2
				#endif
			#end:case
			case 22:
				if local1:
					(self cue:)
				else:
					(global0 setCycle: Beg self)
				#endif
			#end:case
			case 23:
				(global1 handsOn:)
				(tapestry stopUpd:)
				if local1:
					(global0
						posn: ((global0 x:) - 9) ((global0 y:) - 3)
						reset: 0
					)
				else:
					(global0
						posn: ((global0 x:) - 6) ((global0 y:) - 3)
						reset: 0
					)
				#endif
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

