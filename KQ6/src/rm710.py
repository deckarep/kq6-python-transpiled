#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 710
import sci_sh
import kernel
import Main
import rgCastle
import n913
import PanelInset
import Scaler
import PolyPath
import Polygon
import Feature
import StopWalk
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm710 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = [1, 12, 9, 28, 5, 2, 21]
local7 = None
local8 = None
local9 = None
local10 = None
local11 = None
local12 = None


@SCI.procedure
def localproc_0(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	local8 = (global0 y:)
	if (argc >= 1):
		local7 = param1[0]
		if (argc >= 2):
			local8 = param1[1]
		#endif
	#endif
#end:procedure

class DungeonDoor(Prop):
	#property vars (may be empty)
	noun = 4
	sightAngle = 45
	view = 710
	cycleSpeed = 8
	dungeon# = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 5 35 2)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(cond
					case 
						(or
							(kernel.ScriptID(80, 0) tstFlag: 709 2)
							(kernel.ScriptID(81, 0) tstFlag: 709 4)
						):
						(global91 say: noun param1 8 1)
					#end:case
					case (not (kernel.ScriptID(80, 0) tstFlag: 709 2)):
						(kernel.ScriptID(80, 0) dungeonEntered: dungeon#)
						(global2 setScript: enterDungeon 0 self)
					#end:case
				)
			#end:case
			else:
				(super doVerb: param1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class rm710(CastleRoom):
	#property vars (may be empty)
	noun = 8
	picture = 710
	style = 10
	north = 720
	east = 840
	minScaleSize = 37
	minScaleY = 112
	maxScaleY = 173
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self
			addObstacle:
				((Polygon new:)
					type: 2
					init:
						0
						0
						319
						0
						319
						176
						243
						176
						192
						141
						198
						141
						177
						128
						171
						128
						152
						115
						177
						115
						177
						111
						102
						111
						75
						129
						70
						129
						48
						143
						54
						143
						0
						179
					yourself:
				)
		)
		(global32 add: armour roomStuff eachElementDo: #init)
		(kernel.ScriptID(80, 6) noun: 13 actions: guardDoVerb)
		(kernel.ScriptID(81, 0) guard2Code: path2Code setupGuards:)
		spotEgoScr = captureEgo
		(super init: &rest)
		(dungeonDoor1 init: stopUpd:)
		(dungeonDoor2 init: stopUpd:)
		(dungeonDoor3 init: stopUpd:)
		(treasureDoor init: stopUpd:)
		temp1 = 0
		(global0
			init:
			reset:
			setScale: Scaler maxScaleSize minScaleSize maxScaleY minScaleY
		)
		match global12
			case 770:
				(global0 posn: 65 134)
				if (kernel.ScriptID(81, 0) tstFlag: 709 4):
					(kernel.ScriptID(81, 0) setFlag: 709 2)
					(kernel.ScriptID(81, 0) startGuard:)
				#endif
			#end:case
			case 720:
				if (not (kernel.ScriptID(80, 0) tstFlag: 711 512)):
					temp1 = 1
				#endif
				(global0 posn: 148 114)
			#end:case
			case 820:
				(kernel.ScriptID(80, 0) clrFlag: 709 8192)
				match (kernel.ScriptID(80, 0) dungeonEntered:)
					case 1:
						(global0
							posn:
								(dungeonDoor1 approachX:)
								(dungeonDoor1 approachY:)
						)
					#end:case
					case 2:
						(global0
							posn:
								(dungeonDoor2 approachX:)
								(dungeonDoor2 approachY:)
						)
					#end:case
					case 3:
						(global0
							posn:
								(dungeonDoor3 approachX:)
								(dungeonDoor3 approachY:)
						)
						(cond
							case (kernel.ScriptID(80, 0) tstFlag: 709 1):
								(kernel.ScriptID(80, 0) clrFlag: 709 1)
								(jollo
									view: 717
									loop: 4
									cel: 2
									posn: 170 154
									setScale:
										Scaler
										(global2 maxScaleSize:)
										(global2 minScaleSize:)
										(global2 maxScaleY:)
										(global2 minScaleY:)
									init:
									ignoreActors: 1
									setCycle: StopWalk -1
								)
								(self setScript: jolloHelpedEgo)
							#end:case
							case (kernel.ScriptID(80, 0) tstFlag: 709 2):
								(global102 fadeTo: 701 -1)
								(kernel.ScriptID(81, 0) setFlag: 709 2)
								(self setScript: tempScript)
							#end:case
						)
					#end:case
				#end:match
			#end:case
			case 840:
				temp1 = 1
				(global0 posn: 305 184)
			#end:case
			else:
				(global0 posn: 88 132)
				proc913_1(15)
				(self setScript: kernel.ScriptID(711, 0))
			#end:else
		#end:match
		if 
			(and
				temp1
				(not (kernel.ScriptID(81, 0) tstFlag: 709 1))
				(not (kernel.ScriptID(81, 0) tstFlag: 709 2))
				(not kernel.Random(0, 5))
			)
			(kernel.ScriptID(81, 0) setFlag: 709 2 loiterTimer: 1)
		#endif
		((global0 scaler:) doit:)
		if (not script):
			(global1 handsOn:)
		#endif
	#end:method

	@classmethod
	def notify(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(kernel.ScriptID(80, 0) stopTimers: 0)
		if param1:
			((global2 script:) changeState: 2)
		else:
			((global2 script:) changeState: 7)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		local9 = (global0 onControl: 1)
		(cond
			case script: 0#end:case
			case (local9 & 0x4000):
				(global2 newRoom: 720)
			#end:case
			case (local9 & 0x2000):
				(global2 newRoom: 820)
			#end:case
			case (local9 & 0x0400):
				(global2 newRoom: 770)
			#end:case
		)
		(super doit: &rest)
	#end:method

	@classmethod
	def newRoom(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global0 setMotion: 0)
		(kernel.ScriptID(80, 6) actions: 0)
		(super newRoom: param1 &rest)
	#end:method

	@classmethod
	def warnUser(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				if temp0 = (self roomToEdge: param2):
					match temp0
						case 1:
							(global91 say: 9 0 19)
						#end:case
						case 2:
							(global91 say: 9 0 18)
						#end:case
					#end:match
				#endif
			#end:case
			case 6:
				if (param2 == 8):
					(global91 say: 9 0 35)
				else:
					(global91 say: 9 0 34)
				#endif
			#end:case
			case 4:
				if (kernel.ScriptID(81, 0) tstFlag: 709 1):
					(kernel.ScriptID(81, 0) clrFlag: 709 1)
					(kernel.ScriptID(80, 5) dispose:)
					(global91 say: 9 0 37)
				else:
					(kernel.ScriptID(81, 0) clrFlag: 709 2)
					(kernel.ScriptID(80, 6) dispose:)
					(global91 say: 9 0 36)
				#endif
			#end:case
			case 1:
				temp1 = 0
				(cond
					case ((kernel.ScriptID(80, 0) weddingMusicCount:) >= 3):
						if (not (global5 contains: alphaInset)):
							(kernel.ScriptID(81, 0) setFlag: 709 2)
						else:
							(kernel.ScriptID(81, 0) setFlag: 709 16)
						#endif
					#end:case
					case (not (kernel.ScriptID(80, 0) weddingMusicCount:)):
						if (global12 == 770):
							(kernel.ScriptID(80, 0)
								weddingMusicCount: 2
								weddingRemind: 2
							)
						#endif
						temp1 = 24
					#end:case
					else:
						temp1 = 25
					#end:else
				)
				(kernel.ScriptID(81, 0) warnUser: param1 9 0 temp1)
			#end:case
			else:
				(super warnUser: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(kernel.ScriptID(81, 0) clrFlag: 709 16)
		(super dispose:)
		kernel.DisposeScript(964)
	#end:method

	@classmethod
	def scriptCheck(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case proc999_5(param1, 87, 908):
				if 
					(or
						(kernel.ScriptID(81, 0) tstFlag: 709 1)
						(kernel.ScriptID(81, 0) tstFlag: 709 2)
						(kernel.ScriptID(81, 0) tstFlag: 709 4)
					)
					(global91 say: 1 14 1 0 0 899)
					return 0
				else:
					return (super scriptCheck: param1 &rest)
				#endif
			#end:case
			case 
				(or
					(kernel.ScriptID(81, 0) tstFlag: 709 1)
					(kernel.ScriptID(81, 0) tstFlag: 709 2)
				):
				(global91 say: 0 0 6 0 0 899)
				return 0
			#end:case
			else:
				return (super scriptCheck: param1 &rest)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class tempScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				cycles = 2
			#end:case
			case 1:
				(kernel.ScriptID(81, 0) startGuard:)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class enterDungeon(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91 say: 4 5 7 0 self)
			#end:case
			case 1:
				(global105 number: 821 loop: 1 play:)
				(global0 setPri: (global0 priority:))
				(register setCycle: End)
				(global0
					view: 711
					normal: 0
					loop: 1
					cel: 0
					cycleSpeed: 8
					posn: ((global0 x:) + 2) ((global0 y:) + 7)
					setCycle: End self
				)
			#end:case
			case 2:
				(global0 dispose:)
				cycles = 4
			#end:case
			case 3:
				(global2 newRoom: 820)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class doTreasureDoor(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global91 say: 11 2 31 0 self)
			#end:case
			case 1:
				local10 = (kernel.ScriptID(81, 0) loiterTimer:)
				(kernel.ScriptID(81, 0) loiterTimer: 0)
				(kernel.ScriptID(80, 0) stopTimers: 1)
				(global1 handsOn:)
				(global69 disable: 0 2 3 4 5)
				(alphaInset
					view: 713
					offsetX: 30
					offsetY: 20
					maxCol: 5
					maxRow: 5
					numButtons: 30
					posn: 87 39
					init: @local0 7
				)
			#end:case
			case 2:
				(global1 handsOff:)
				cycles = 2
			#end:case
			case 3:
				(global91 say: 2 5 4 1 self)
			#end:case
			case 4:
				(global105 number: 901 loop: 1 play:)
				(treasureDoor cycleSpeed: 10 setCycle: End self)
			#end:case
			case 5:
				(global105 stop:)
				(global91 say: 2 5 4 2 self)
			#end:case
			case 6:
				proc80_2(4)
				(self dispose:)
			#end:case
			case 7:
				(global1 handsOff:)
				cycles = 2
			#end:case
			case 8:
				(global91 say: 2 5 6 0 self)
			#end:case
			case 9:
				(global1 handsOn:)
				if (kernel.ScriptID(81, 0) tstFlag: 709 16):
					(kernel.ScriptID(81, 0) setFlag: 709 2 clrFlag: 709 16)
					(kernel.ScriptID(81, 0) startGuard:)
				#endif
				(kernel.ScriptID(81, 0) loiterTimer: local10)
				local10 = 0
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class jolloHelpedEgo(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				cycles = 3
			#end:case
			case 1:
				(global91 say: 9 0 9 0 self)
			#end:case
			case 2:
				(jollo setSpeed: 6 setMotion: MoveTo 184 180 self)
			#end:case
			case 3:
				(jollo setMotion: MoveTo 343 180 self)
			#end:case
			case 4:
				if (kernel.ScriptID(81, 0) tstFlag: 709 4):
					(kernel.ScriptID(81, 0) setFlag: 709 2)
					(kernel.ScriptID(81, 0) startGuard:)
				#endif
				if (kernel.ScriptID(80, 0) tstFlag: 709 2):
					(global102 fadeTo: 701 -1)
					(kernel.ScriptID(81, 0) setFlag: 709 2)
					(kernel.ScriptID(81, 0) startGuard:)
					(jollo dispose:)
				else:
					(global102 fadeTo: 704 -1)
					(jollo hide: setScript: followTimer)
				#endif
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class followTimer(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(kernel.ScriptID(80, 0) setFlag: 711 -32768)
				seconds = 6
			#end:case
			case 1:
				(kernel.ScriptID(80, 0) clrFlag: 711 -32768)
				(jollo dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class talkToGuards(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		register = 0
		(super dispose: &rest)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super doit:)
		if ((state == 1) and (register perform: path2Code)):
			(global0 setMotion: 0)
			(self cue:)
		#endif
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(kernel.ScriptID(80, 5) okToCheck: 0)
				(kernel.ScriptID(80, 6) okToCheck: 0 checkCode: 0)
				register = (CueObj client:)
				(global91 say: 13 2 0 1 self)
			#end:case
			case 1:
				(global0 setMotion: PolyPath (register x:) (register y:))
			#end:case
			case 2:
				if (not (global0 facingMe: register)):
					proc913_4(global0, register, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 3:
				cycles = 1
			#end:case
			case 4:
				(global91 say: 13 2 0 2 self oneOnly: 0)
			#end:case
			case 5:
				(client setScript: captureEgo 0 register)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class captureEgo(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				if (not register):
					(global91 say: 9 0 17 1 self)
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				proc913_4(kernel.ScriptID(80, 6), global0, self)
			#end:case
			case 2:
				(global91 say: 9 0 17 2 self)
			#end:case
			case 3:
				(kernel.ScriptID(80, 6) setScript: kernel.ScriptID(80, 4) self 1)
			#end:case
			case 4:
				(global91 say: 9 0 17 3 self)
			#end:case
			case 5:
				(global91 say: 9 0 17 4 self)
			#end:case
			case 6:
				(global5 eachElementDo: #hide)
				(global2 drawPic: 98)
				cycles = 4
			#end:case
			case 7:
				(global91 say: 9 0 17 5 self)
			#end:case
			case 8:
				(global2 newRoom: 820)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class dungeonDoor1(DungeonDoor):
	#property vars (may be empty)
	x = 165
	y = 110
	approachX = 150
	approachY = 121
	loop = 3
	priority = 8
	signal = 20496
	dungeon# = 1
	
#end:class or instance

@SCI.instance
class dungeonDoor2(DungeonDoor):
	#property vars (may be empty)
	x = 193
	y = 117
	approachX = 175
	approachY = 133
	loop = 2
	signal = 20480
	dungeon# = 2
	
#end:class or instance

@SCI.instance
class dungeonDoor3(DungeonDoor):
	#property vars (may be empty)
	x = 227
	y = 134
	approachX = 199
	approachY = 160
	signal = 20480
	dungeon# = 3
	
#end:class or instance

@SCI.instance
class treasureDoor(Prop):
	#property vars (may be empty)
	x = 52
	y = 109
	noun = 11
	sightAngle = 45
	approachX = 66
	approachY = 134
	view = 710
	loop = 1
	signal = 20480
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 5 2)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 2:
				if 
					(or
						(kernel.ScriptID(81, 0) tstFlag: 709 2)
						(kernel.ScriptID(81, 0) tstFlag: 709 4)
					)
					(global91 say: noun 2 30 1)
				else:
					(global2 setScript: doTreasureDoor)
				#endif
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class alphaInset(PanelInset):
	#property vars (may be empty)
	noun = 2
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global69 disable: 6)
		(super init: &rest)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global69 enable: 6)
		if (charCount < strLen):
			(global2 setScript: clearedInset 0 charCount)
		#endif
		(super dispose:)
		local11 = local12 = 0
	#end:method

	@classmethod
	def drawButton():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 0
		if (not proc999_5(value, 26, 27, 29, 30)):
			if (not (local11[(value / 16)] & (0x8000 >> (mod value 16)))):
				(local11[(value / 16)] |= (0x8000 >> (mod value 16)))
				temp0 = (super drawButton: &rest)
				(global104 number: 910 setLoop: 1 play:)
			else:
				temp0 = 0
			#endif
		#endif
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class clearedInset(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				cycles = 2
			#end:case
			case 1:
				if register:
					(global91 say: 2 5 6 0 self)
				else:
					(global91 say: 2 5 5 0 self)
				#endif
			#end:case
			case 2:
				(global1 handsOn:)
				(kernel.ScriptID(80, 0) stopTimers: 0)
				(kernel.ScriptID(81, 0) loiterTimer: local10)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class armour(Feature):
	#property vars (may be empty)
	x = 151
	y = 111
	z = 10
	noun = 10
	nsTop = 91
	nsLeft = 148
	nsBottom = 111
	nsRight = 155
	sightAngle = 45
	approachX = 149
	approachY = 112
	
#end:class or instance

@SCI.instance
class roomStuff(Feature):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		sightAngle = 26505
	#end:method

	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = kernel.OnControl(4, (param1 x:), (param1 y:))
		(return
			(or
				((0x1000 & temp0) and noun = 14)
				((0x0002 & temp0) and noun = 3)
				((0x6404 & temp0) and noun = 12)
				((0x0188 & temp0) and noun = 5)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class jollo(Actor):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class path2Code(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 0
		if 
			(and
				(((param1 regPathID:) currentRoom:) == global11)
				(not (param1 inRect: 140 0 320 116))
				(>= 320 (param1 x:) 0)
			)
			temp1 = (param1 onControl: 1)
			temp0 = ((local9 == temp1) or ((| local9 temp1) & 0x0100))
		#endif
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class guardDoVerb(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 1
		if (param1 == 2):
			(global2 setScript: talkToGuards)
		else:
			temp0 = 0
		#endif
		return temp0
	#end:method

#end:class or instance

