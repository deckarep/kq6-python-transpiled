#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 840
import sci_sh
import Main
import rgCastle
import n913
import Scaler
import PolyPath
import Polygon
import Feature
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm840 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None
local4 = None
local5 = None
local6 = None
local7 = None
local8 = None
local9 = None


@SCI.instance
class rm840(CastleRoom):
	#property vars (may be empty)
	noun = 9
	picture = 840
	style = 10
	horizon = 10
	north = 720
	west = 710
	vanishingX = 202
	vanishingY = 95
	minScaleSize = 35
	minScaleY = 111
	maxScaleY = 173
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		scalerCode = guardScalerCode
		(self
			addObstacle:
				((Polygon new:)
					type: 2
					init:
						-260
						-10
						319
						-10
						319
						179
						266
						142
						272
						142
						252
						129
						246
						129
						220
						111
						147
						111
						147
						115
						171
						115
						137
						135
						85
						103
						65
						55
						31
						55
						31
						58
						58
						58
						80
						105
						134
						139
						77
						178
						-260
						178
					yourself:
				)
		)
		(global32 add: stairCase roomFeatures floors eachElementDo: #init)
		(super init: &rest)
		spotEgoScr = captureEgo
		((ScriptID 80 5) noun: 1 okToCheck: CheckCode actions: guardDoVerb)
		((ScriptID 80 6) noun: 1 okToCheck: CheckCode actions: guardDoVerb)
		((ScriptID 81 0)
			guard1Code: path1Code
			guard2Code: path1Code
			setupGuards:
		)
		(clownDoor init: stopUpd:)
		(grandHallDoor init: stopUpd:)
		(global0
			init:
			actions: egoDoVerb
			setScale: Scaler maxScaleSize minScaleSize maxScaleY minScaleY
		)
		match global12
			case 720:
				(global0 posn: 175 116)
			#end:case
			case 710:
				(global0 posn: 16 184)
			#end:case
			case 780:
				(global0 posn: 232 122)
			#end:case
			else:
				local1 = local2 = 1
				(global0 posn: 48 58 setScale: scaleX: 107 scaleY: 107)
			#end:else
		#end:match
		if (IsObject (global0 scaler:)):
			((global0 scaler:) doit:)
		#endif
		if 
			(and
				((ScriptID 81 0) tstFlag: 709 4)
				(not ((ScriptID 81 0) tstFlag: 709 8))
			)
			(self setScript: weddingCorralCrunch)
		#endif
		if ((ScriptID 80 0) tstFlag: 711 -32768):
			if script:
				(followedClown next: script)
			#endif
			(self setScript: followedClown)
		#endif
		if (not script):
			(global1 handsOn:)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		local0 = (global0 onControl: 1)
		(cond
			case script: 0#end:case
			case (local0 & 0x4000):
				(global2 newRoom: 720)
			#end:case
			case ((not local7) and (local0 & 0x3000)):
				(self setScript: climbStairs)
			#end:case
			case (local0 & 0x0800):
				(global2 newRoom: 780)
			#end:case
			case ((proc999_4 61 45 137 130 global0) and (global0 isStopped:)):
				(self setScript: climbStairs 0 1)
			#end:case
		)
		if 
			(and
				(proc999_4 61 45 136 137 global0)
				(global0 isBlocked:)
				(script != captureEgo)
			)
			if temp0 = (global5 firstTrue: #perform RoomCheck):
				(self spotEgo: temp0)
			else:
				(global0 ignoreActors: 1)
			#endif
		#endif
		if local1:
			if (global0 inRect: 0 0 85 78):
				local3 = 0
				if (not local2):
					local2 = 1
					(global0
						oldScaleSignal: 0
						setScale:
						scaleX: 107
						scaleY: 107
					)
				#endif
			else:
				local2 = 0
				if (not local3):
					local3 = 1
					(global0
						oldScaleSignal: 0
						setScale:
							Scaler
							maxScaleSize
							minScaleSize
							maxScaleY
							minScaleY
					)
				#endif
			#endif
		#endif
		(cond
			case (local1 and (local0 & 0x0008)):
				local1 = 0
			#end:case
			case ((not local1) and (local0 & 0x1000)):
				local1 = 1
			#end:case
		)
		(super doit: &rest)
	#end:method

	@classmethod
	def doLoiter():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not argc):
			(global91 say: 10 0 26)
			((ScriptID 81 0) loiterTimer: 15)
		#endif
	#end:method

	@classmethod
	def warnUser(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				local9 = 0
				(cond
					case (((ScriptID 80 0) weddingMusicCount:) >= 3):
						local9 = 30
						((ScriptID 81 0) setFlag: 709 1 2)
					#end:case
					case (not ((ScriptID 80 0) weddingMusicCount:)):
						(clownDoor _approachVerbs: 0)
						local9 = 28
					#end:case
					else:
						local9 = 29
					#end:else
				)
				((ScriptID 81 0) warnUser: param1 10 0 local9)
			#end:case
			case 6:
				(global91 say: 10 0 22)
			#end:case
			case 5:
				if 
					(and
						(not ((global2 script:) == weddingCorralCrunch))
						temp0 = (self roomToEdge: param2)
					)
					match temp0
						case 4:
							(global91 say: 10 0 19)
						#end:case
						case 1:
							(global91 say: 10 0 18)
						#end:case
					#end:match
				#endif
			#end:case
			case 4:
				if (not ((ScriptID 81 0) tstFlag: 709 4)):
					if ((ScriptID 81 0) tstFlag: 709 2):
						(global91 say: 10 0 23)
					else:
						(global91 say: 10 0 21)
					#endif
				#endif
			#end:case
			else:
				(super warnUser: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def newRoom(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		((ScriptID 80 5) actions: 0)
		((ScriptID 80 6) actions: 0)
		((ScriptID 80 0) clrFlag: 711 -32768)
		(super newRoom: param1 &rest)
	#end:method

	@classmethod
	def scriptCheck(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (proc999_5 param1 87 908):
				if 
					(or
						((ScriptID 81 0) tstFlag: 709 1)
						((ScriptID 81 0) tstFlag: 709 2)
						((ScriptID 81 0) tstFlag: 709 4)
					)
					(global91 say: 3 14 1 0 0 899)
					return 0
				else:
					return (super scriptCheck: param1 &rest)
				#endif
			#end:case
			case 
				(or
					((ScriptID 81 0) tstFlag: 709 1)
					((ScriptID 81 0) tstFlag: 709 2)
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
class RoomCheck(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(and
				(param1 isKindOf: GuardDog)
				(((param1 regPathID:) currentRoom:) == global11)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class talkToGuards(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose: &rest)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super doit:)
		if ((state == 1) and (register perform: (register checkCode:))):
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
				((ScriptID 80 5) okToCheck: 0)
				((ScriptID 80 6) okToCheck: 0)
				register = (CueObj client:)
				(global91 say: 1 2 0 1 self)
			#end:case
			case 1:
				local6 = 1
				local7 = 1
				(global0 setMotion: PolyPath (register x:) (register y:))
			#end:case
			case 2:
				if (not (global0 facingMe: register)):
					(proc913_4 global0 register self)
				else:
					cycles = 1
				#endif
			#end:case
			case 3:
				cycles = 1
			#end:case
			case 4:
				(global91 say: 1 2 0 2 self oneOnly: 0)
			#end:case
			case 5:
				(global2 spotEgo: register)
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
				if 
					(and
						(global5 contains: (ScriptID 80 5))
						(global5 contains: (ScriptID 80 6))
						(==
							(((ScriptID 80 5) regPathID:) currentRoom:)
							global11
						)
						(==
							(((ScriptID 80 6) regPathID:) currentRoom:)
							global11
						)
					)
					(global2 moveOtherGuard: 1)
				#endif
				ticks = 2
			#end:case
			case 1:
				if (not local6):
					(global91 say: 10 0 16 1 self)
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				(proc913_4 register global0 self)
			#end:case
			case 3:
				cycles = 14
			#end:case
			case 4:
				(global0 stopUpd:)
				(grandHallDoor setCycle: 0 stopUpd:)
				cycles = 4
			#end:case
			case 5:
				(global91 say: 10 0 16 2 self)
			#end:case
			case 6:
				(register setScript: (ScriptID 80 4) self 1)
			#end:case
			case 7:
				(register stopUpd:)
				cycles = 4
			#end:case
			case 8:
				(global91 say: 10 0 16 3 self)
			#end:case
			case 9:
				(global91 say: 10 0 16 4 self)
			#end:case
			case 10:
				(global5 eachElementDo: #hide)
				(global2 drawPic: 98)
				cycles = 4
			#end:case
			case 11:
				(global91 say: 10 0 16 5 self)
			#end:case
			case 12:
				(global2 newRoom: 820)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class weddingCorralCrunch(Script):
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
				if ((((ScriptID 80 6) regPathID:) value:) < 8):
					(((ScriptID 80 6) regPathID:) value: 8 moveDone:)
				#endif
				((ScriptID 81 0) setFlag: 709 1 8)
				(global91 say: 10 0 15 0 self)
			#end:case
			case 2:
				((ScriptID 81 0) startGuard:)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class climbStairs(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				if register:
					(= register
						(grandHallDoor if ((global0 x:) <= 88) else stairCase)
					)
				else:
					(= register
						(grandHallDoor if (local0 & 0x2000) else stairCase)
					)
				#endif
				(global0
					setMotion:
						PolyPath
						(register approachX:)
						(register approachY:)
						self
				)
			#end:case
			case 1:
				(global1 handsOn:)
				register = 0
				(global0 oldScaleSignal: 0 reset:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class followedClown(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				((ScriptID 80 0) clrFlag: 711 -32768)
				(jollo view: 717 loop: 8)
				if (global12 == 710):
					(jollo posn: 142 150 loop: 3)
				else:
					(jollo posn: 177 130 loop: 1)
				#endif
				(jollo
					ignoreActors: 1
					setCycle: Walk
					setScale:
						Scaler
						(global2 maxScaleSize:)
						(global2 minScaleSize:)
						(global2 maxScaleY:)
						(global2 minScaleY:)
					init:
				)
				cycles = 2
			#end:case
			case 1:
				if (((global9 at: 25) owner:) == 750):
					(self setScript: jolloClimbStairs self)
				else:
					(self setScript: jolloGotoBed self)
				#endif
			#end:case
			case 2:
				if (not next):
					(global1 handsOn:)
				#endif
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class jolloClimbStairs(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(jollo setMotion: MoveTo 132 134 self)
			#end:case
			case 1:
				(jollo setMotion: PolyPath 90 134 self)
			#end:case
			case 2:
				(jollo
					setScale:
					scaleX: 107
					scaleY: 107
					setMotion: PolyPath 48 55 self
				)
			#end:case
			case 3:
				(global105 number: 901 loop: 1 play:)
				(grandHallDoor priority: 10 setCycle: End self)
			#end:case
			case 4:
				(global105 stop:)
				(jollo setMotion: MoveTo ((jollo x:) - 15) (jollo y:) self)
			#end:case
			case 5:
				(jollo hide:)
				(grandHallDoor priority: 0 setCycle: Beg self)
			#end:case
			case 6:
				(global105 number: 902 loop: 1 play:)
				(grandHallDoor stopUpd:)
				if (((global9 at: 25) owner:) == 750):
					(jollo setScript: followTimer)
				else:
					(jollo dispose:)
				#endif
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
				((ScriptID 80 0) setFlag: 711 -32768)
				seconds = 10
			#end:case
			case 1:
				((ScriptID 80 0) clrFlag: 711 -32768)
				(jollo dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class jolloGotoBed(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(jollo setMotion: MoveTo 236 124 self)
			#end:case
			case 1:
				(global105 number: 901 loop: 1 play:)
				(clownDoor setCycle: End self)
			#end:case
			case 2:
				(global105 stop:)
				(jollo setMotion: MoveTo 238 121 self)
			#end:case
			case 3:
				(jollo setMotion: MoveTo ((jollo x:) + 10) (jollo y:) self)
			#end:case
			case 4:
				(jollo dispose:)
				(clownDoor setCycle: Beg self)
			#end:case
			case 5:
				(global105 number: 902 loop: 1 play:)
				(clownDoor stopUpd:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class clownDoor(Prop):
	#property vars (may be empty)
	x = 237
	y = 104
	noun = 5
	sightAngle = 45
	approachX = 234
	approachY = 122
	view = 840
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self ignoreActors: 1 yStep: -1)
		if (not ((ScriptID 80 0) tstFlag: 709 2)):
			(self approachVerbs: 5)
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				if ((ScriptID 80 0) tstFlag: 709 4):
					(global91 say: noun param1 9 0)
				else:
					(global91 say: noun param1 8 0)
				#endif
			#end:case
			case 5:
				(cond
					case 
						(or
							((ScriptID 80 0) tstFlag: 709 2)
							((ScriptID 81 0) tstFlag: 709 4)
						):
						(global91 say: noun param1 7 0)
					#end:case
					case 
						(or
							((ScriptID 81 0) tstFlag: 709 1)
							((ScriptID 81 0) tstFlag: 709 2)
						):
						if ((ScriptID 80 0) tstFlag: 709 4):
							(global91 say: noun param1 6 0 self)
						else:
							(global91 say: noun param1 5 0 self)
						#endif
					#end:case
					case (not ((ScriptID 80 0) tstFlag: 709 4)):
						(global91 say: noun param1 3 0 self)
					#end:case
					else:
						(self cue: 0)
					#end:else
				)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def cue(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1 = yStep++
			case 0:
				(global1 handsOff:)
				(self ignoreActors: setCycle: End self)
				(global104 number: 901 setLoop: 1 play:)
			#end:case
			case 1:
				((ScriptID 80 0) setFlag: 709 4)
				(proc80_2 2)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class grandHallDoor(Prop):
	#property vars (may be empty)
	x = 26
	y = 55
	z = 36
	noun = 7
	sightAngle = 45
	approachX = 48
	approachY = 55
	view = 840
	loop = 1
	cycleSpeed = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(signal |= 0x0010)
		(self approachVerbs: 5)
	#end:method

	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		local7 = 0
		if 
			(and
				temp0 = (super onMe: param1)
				(&
					_approachVerbs
					(global66 doit: ((global69 curIcon:) message:))
				)
			)
			local7 = 1
		#endif
		return temp0
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = ((ScriptID 80 5) onControl: 1)
		temp1 = ((ScriptID 80 6) onControl: 1)
		(super doit:)
		if (not cycler):
			(cond
				case 
					(and
						cel
						(or
							(and
								((ScriptID 81 0) tstFlag: 709 1)
								(not (temp0 & 0x0400))
							)
							(and
								((ScriptID 81 0) tstFlag: 709 2)
								(IsObject ((ScriptID 80 6) regPathID:))
								(==
									(((ScriptID 80 6) regPathID:) currentRoom:)
									global11
								)
								(not (temp1 & 0x0400))
							)
						)
					):
					(self setCycle: Beg self)
				#end:case
				case 
					(and
						(not cel)
						(or
							(and
								((ScriptID 81 0) tstFlag: 709 1)
								((ScriptID 80 5) mover:)
								(temp0 & 0x0400)
							)
							(and
								((ScriptID 81 0) tstFlag: 709 2)
								(IsObject ((ScriptID 80 6) regPathID:))
								(==
									(((ScriptID 80 6) regPathID:) currentRoom:)
									global11
								)
								(temp1 & 0x0400)
							)
						)
					):
					(self cue: 1 setCycle: End)
				#end:case
				else: 0#end:else
			)
		#endif
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self ignoreActors: (not (signal & 0x4000)))
		if (not local5):
			if argc:
				priority = 10
				(global105 number: 901 loop: 1 play:)
			else:
				priority = 0
				(self stopUpd:)
				(global105 number: 902 loop: 1 play:)
			#endif
		else:
			(global2 newRoom: 730)
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		local7 = 0
		match param1
			case 5:
				(global1 handsOff:)
				(global2 newRoom: 730)
			#end:case
			case 1:
				if (not local4):
					local4++
					(_approachVerbs |= (global66 doit: 1))
					(global91 say: noun param1 11)
				else:
					(global0
						oldScaleSignal: 0
						oldMaxScale: 0
						oldBackSize: 0
						oldFrontY: 0
						oldBackY: 0
					)
					(global1 handsOff:)
					(global91 say: noun param1 10 1)
					(global2 setScript: (ScriptID 82) 0 lookIntoGrandHall)
				#endif
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class keyHoleActions(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 1
		match param1
			case 1:
				if ((ScriptID 80 0) tstFlag: 709 2):
					(global91 say: 8 param1 32)
				else:
					temp0 = 0
				#endif
			#end:case
			else:
				temp0 = 0
			#end:else
		#end:match
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class lookIntoGrandHall(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if register:
			register = 0
			(tempGuard1 dispose:)
			(tempGuard2 dispose:)
		#endif
		(accessaryView dispose:)
		if ((ScriptID 80 0) tstFlag: 711 -32768):
			(jollo dispose:)
		#endif
		((ScriptID 80 0) clrFlag: 711 -32768)
		(super dispose:)
		((ScriptID 80 0) stopTimers: 0)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				((ScriptID 80 0) stopTimers: 1)
				((ScriptID 82 1)
					noun: 8
					actions: keyHoleActions
					init: 793 0 0 74 46
				)
				(jollo setScript: 0)
				(accessaryView init:)
				if (not register = ((ScriptID 80 0) tstFlag: 709 2)):
					(tempGuard1 init: stopUpd:)
					(tempGuard2 init: stopUpd:)
				#endif
				cycles = 2
			#end:case
			case 1:
				local9 = (32 if register else 10)
				(global91 say: 7 1 local9 2 self)
			#end:case
			case 2:
				if ((ScriptID 80 0) tstFlag: 711 -32768):
					(jollo
						view: 717
						loop: 0
						cel: 5
						x: 143
						y: 96
						setScale:
						scaleX: 49
						scaleY: 49
						priority: 12
						setCycle: Walk
						signal: 16400
						init:
						setMotion: MoveTo 173 79
					)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class accessaryView(View):
	#property vars (may be empty)
	view = 793
	cel = 1
	priority = 11
	signal = 16400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		x = ((ScriptID 82 1) x:)
		y = ((ScriptID 82 1) y:)
		(super init: &rest)
	#end:method

#end:class or instance

@SCI.instance
class tempGuard1(View):
	#property vars (may be empty)
	x = 148
	y = 128
	noun = 8
	sightAngle = 180
	view = 793
	loop = 1
	priority = 14
	signal = 16400
	scaleSignal = 1
	
#end:class or instance

@SCI.instance
class tempGuard2(View):
	#property vars (may be empty)
	x = 167
	y = 126
	noun = 8
	sightAngle = 180
	view = 793
	loop = 1
	cel = 1
	priority = 14
	signal = 16400
	scaleSignal = 1
	
#end:class or instance

@SCI.instance
class stairCase(Feature):
	#property vars (may be empty)
	x = 129
	y = 136
	z = 24
	noun = 11
	nsTop = 90
	nsLeft = 123
	nsBottom = 135
	nsRight = 136
	sightAngle = 45
	approachX = 141
	approachY = 137
	
#end:class or instance

@SCI.instance
class roomFeatures(Feature):
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

		temp0 = (OnControl 4 (param1 x:) (param1 y:))
		(return
			(or
				((0x0010 & temp0) and noun = 13)
				((0x0002 & temp0) and noun = 4)
				((0x7804 & temp0) and noun = 12)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class floors(Feature):
	#property vars (may be empty)
	noun = 6
	onMeCheck = 392
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(global93 add: self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global93 delete: self)
		(super dispose:)
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		local7 = 0
		if 
			(and
				((param1 type:) & 0x1000)
				(not (param1 modifiers:))
				(self onMe: param1)
			)
			local7 = 1
		else:
			(super handleEvent: param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class jollo(Actor):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class guardScalerCode(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (param1 inRect: 0 0 88 86):
				if (param1 scaler:):
					(param1 setScale: scaleX: 107 scaleY: 107)
				#endif
			#end:case
			case (not (param1 scaler:)):
				(param1
					setScale:
						Scaler
						(global2 maxScaleSize:)
						(global2 minScaleSize:)
						(global2 maxScaleY:)
						(global2 minScaleY:)
				)
				((param1 scaler:) doit:)
			#end:case
		)
	#end:method

#end:class or instance

@SCI.instance
class CheckCode(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(and
				(param1 regPathID:)
				(((param1 regPathID:) currentRoom:) == global11)
				(not (param1 inRect: 136 64 174 118))
				(not (param1 inRect: -20 0 35 67))
				((param1 x:) > 0)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class path1Code(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp1 = 0
		temp0 = (param1 onControl: 1)
		if (param1 regPathID:):
			if ((not local1) and ((global2 script:) != climbStairs)):
				(= temp1
					if 
						(and
							(((param1 regPathID:) currentRoom:) == global11)
							(temp0 & 0x0188)
						)
						if ((param1 loop:) == 3):
							((global0 y:) <= (param1 y:))
						else:
							((local0 == temp0) or ((| local0 temp0) & 0x0100))
						#endif
					else:
						0
					#endif
				)
			else:
				(= temp1
					if (((param1 regPathID:) currentRoom:) == global11):
						(param1 inRect: 0 0 119 131)
					#endif
				)
			#endif
		#endif
		return temp1
	#end:method

#end:class or instance

@SCI.instance
class egoDoVerb(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 1
		if (proc999_5 param1 14 19):
			if 
				(or
					((ScriptID 81 0) tstFlag: 709 1)
					((ScriptID 81 0) tstFlag: 709 2)
					((ScriptID 81 0) tstFlag: 709 4)
				)
				(global91 say: 3 14 1)
			else:
				temp0 = 0
			#endif
		else:
			temp0 = 0
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

