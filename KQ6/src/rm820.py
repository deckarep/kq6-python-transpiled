#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 820
import sci_sh
import kernel
import Main
import rgCastle
import Print
import Conversation
import Scaler
import RandCycle
import PolyPath
import Polygon
import Feature
import LoadMany
import Window
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm820 = 0,
	noWayOut = 1,
	roomConv = 2,
	dungeonDoor = 3,
	flame = 4,
	wallReflection = 5,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.instance
class rm820(CastleRoom):
	#property vars (may be empty)
	noun = 3
	picture = 820
	style = 10
	horizon = 0
	vanishingX = 186
	vanishingY = 92
	minScaleSize = 89
	maxScaleSize = 113
	minScaleY = 130
	maxScaleY = 144
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		proc958_0(128, 825, 822)
		(global2
			addObstacle:
				((Polygon new:)
					type: 3
					init:
						10
						166
						10
						174
						301
						174
						301
						161
						280
						147
						147
						147
						147
						132
						95
						132
					yourself:
				)
		)
		(kernel.ScriptID(1015, 6) x: 19 y: 41)
		(kernel.ScriptID(1015, 7) x: 19 y: 77)
		(global32 add: bed torch gargoyle eachElementDo: #init)
		(super init: &rest)
		(flame setCycle: Fwd init:)
		(wallReflection setCycle: RandCycle init:)
		(dungeonDoor cel: 3 setPri: 10 init: stopUpd:)
		(extraView addToPic:)
		(ant init: setScript: antScript)
		(global0
			init:
			reset: 0
			posn: 43 143
			setPri: 9
			setScale: Scaler maxScaleSize minScaleSize maxScaleY minScaleY
		)
		((global0 scaler:) doit:)
		if (kernel.ScriptID(80, 0) tstFlag: 709 8192):
			if (global5 contains: kernel.ScriptID(80, 5)):
				(kernel.ScriptID(81, 0) resetGuard: kernel.ScriptID(80, 5) 1)
				(kernel.ScriptID(80, 5) dispose:)
			#endif
			if (global5 contains: kernel.ScriptID(80, 6)):
				(kernel.ScriptID(81, 0) resetGuard: kernel.ScriptID(80, 6) 2)
				(kernel.ScriptID(80, 6) dispose:)
			#endif
			(kernel.ScriptID(81, 0) clrFlag: 709 1 2)
			(self setScript: kernel.ScriptID(821, 0))
			(global102 fadeTo: 824 -1)
			local0 = 1
		else:
			(self setScript: enterDungeon)
			if 
				(and
					proc999_5((kernel.ScriptID(80, 0) dungeonEntered:), 1, 2)
					(not (kernel.ScriptID(80, 0) tstFlag: 709 -32768))
				)
				(global102 fadeTo: 820 -1)
				if (not (global0 has: 17)):
					(dungeonDoor approachX: 111)
				#endif
				(enterDungeon next: kernel.ScriptID(822, 0))
			else:
				(global102 fadeTo: 824 -1)
			#endif
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if 
			(and
				(param1 == 2)
				proc999_5((kernel.ScriptID(80, 0) dungeonEntered:), 1, 2)
				(not (kernel.ScriptID(80, 0) tstFlag: 709 -32768))
			)
			(global91 say: 3 2 20 1)
		else:
			(super doVerb: param1 &rest)
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global0 setPri: -1)
		(super dispose: &rest)
		kernel.DisposeScript(991)
		kernel.DisposeScript(964)
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
				cycles = 1
			#end:case
			case 1:
				(global0
					setMotion:
						MoveTo
						(dungeonDoor approachX:)
						(dungeonDoor approachY:)
						self
				)
			#end:case
			case 2:
				(dungeonDoor setCycle: Beg self)
			#end:case
			case 3:
				(global105 number: 822 loop: 1 play:)
				(dungeonDoor setPri: -1 stopUpd:)
				if 
					(or
						(kernel.ScriptID(81, 0) tstFlag: 709 1)
						(kernel.ScriptID(81, 0) tstFlag: 709 2)
					)
					(global91 say: 1 0 7 1 self)
				else:
					cycles = 2
				#endif
				if (global5 contains: kernel.ScriptID(80, 5)):
					(kernel.ScriptID(81, 0) resetGuard: kernel.ScriptID(80, 5) 1)
					(kernel.ScriptID(80, 5) dispose:)
				#endif
				if (global5 contains: kernel.ScriptID(80, 6)):
					(kernel.ScriptID(81, 0) resetGuard: kernel.ScriptID(80, 6) 2)
					(kernel.ScriptID(80, 6) dispose:)
				#endif
				(kernel.ScriptID(81, 0) clrFlag: 709 1 2)
			#end:case
			case 4:
				if (not next):
					(global1 handsOn:)
				else:
					next = 0
					(kernel.ScriptID(822, 1) init:)
				#endif
				(global0 reset: 0)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class exitDungeon(Script):
	#property vars (may be empty)
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (global0 onControl: 1)
		if ((state == 1) and (temp0 & 0x4000)):
			(self cue:)
		#endif
		(super doit: &rest)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(dungeonDoor hide:)
				(global0
					normal: 0
					setScale: 0
					scaleX: 128
					scaleY: 128
					view: 821
					loop: 4
					cel: 0
					posn: 56 109
					setCycle: CT 2 1 self
				)
			#end:case
			case 1:
				(global105 number: 821 loop: 1 play:)
				(dungeonDoor setPri: 10 cel: 3)
				(global0 setCycle: End self)
			#end:case
			case 2:
				(dungeonDoor show: stopUpd:)
				(global105 stop:)
				(global0
					posn: (dungeonDoor approachX:) (dungeonDoor approachY:)
					reset: 1
					setPri: 9
					setMotion: MoveTo 0 143 self
				)
			#end:case
			case 3:
				(global0 hide:)
				(dungeonDoor setCycle: Beg self)
			#end:case
			case 4:
				(global105 number: 822 loop: 1 play: self)
				(global0 setPri: -1)
			#end:case
			case 5:
				(global2 newRoom: 710)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class antScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				register = 0
				(state += (kernel.Random(0, 1) * 3))
				(ant hide: setPri: 15 ignoreActors: setCycle: Walk)
				seconds = kernel.Random(7, 25)
			#end:case
			case 1:
				(ant show:)
				if register = kernel.Random(0, 1):
					(ant
						setLoop: 6
						posn: 220 201 0
						setMotion: MoveTo 172 167 self
					)
				else:
					(ant
						setLoop: 5
						posn: 106 195 0
						setMotion: MoveTo 155 169 self
					)
				#endif
			#end:case
			case 2:
				seconds = kernel.Random(1, 10)
			#end:case
			case 3:
				state = -1
				(ant setPri: 14)
				if register:
					(ant
						setLoop: 8
						posn: 164 195 28
						setMotion: MoveTo 164 213 self
					)
				else:
					(ant
						setLoop: 7
						posn: 162 195 24
						setMotion: MoveTo 162 209 self
					)
				#endif
			#end:case
			case 4:
				(ant
					show:
					setLoop: 5
					posn: 0 189 0
					setMotion: MoveTo 44 172 self
				)
			#end:case
			case 5:
				seconds = kernel.Random(2, 10)
			#end:case
			case 6:
				state = -1
				(ant loop: 7 setMotion: MoveTo 88 197 self)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class noWayOut(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(ant setScript: 0)
				(global1 handsOff:)
				(global102 fadeTo: 823 1)
				cycles = 2
			#end:case
			case 1:
				(global0 setMotion: PolyPath 90 144 self)
			#end:case
			case 2:
				(global0
					view: 821
					normal: 0
					setPri: 12
					setScale: 0
					scaleX: 128
					scaleY: 128
					posn: 93 144
					loop: 5
					cel: 0
					cycleSpeed: 8
					setCycle: End self
				)
			#end:case
			case 3:
				(global105 number: 825 setLoop: -1 play:)
				(global0 loop: 6 cel: 0 setCycle: Fwd)
				seconds = 4
			#end:case
			case 4:
				(global105 stop:)
				(global0 setCycle: 0)
				cycles = 3
			#end:case
			case 5:
				(global91 say: 1 0 2 1 self)
			#end:case
			case 6:
				(global91 say: 1 0 2 2 self)
			#end:case
			case 7:
				(global5 eachElementDo: #hide)
				(global2 drawPic: 98 10)
				kernel.Message(1, @temp1)
				kernel.Display(@temp1, 100, 30, 11, 106, 260, 102, 16, 105, global22, 101, 1)
				kernel.Display(@temp1, 100, 29, 10, 106, 260, 102, 47, 105, global22, 101, 1)
				(global0
					view: 8901
					loop: 0
					cel: 0
					normal: 0
					setScale: 0
					scaleX: 128
					scaleY: 128
					posn: 160 43
					setMotion: 0
					show:
				)
				(global102 number: 970 loop: 1 play:)
				cycles = 2
			#end:case
			case 8:
				(global1 setCursor: global20)
				while True: #repeat
					match
						(= temp0
							(Print
								window: DeathWindow
								addText: r"""Please select:""" 60 0
								posn: 70 130
								addButton: 1 r"""Restore""" 0 15
								addButton: 2 r"""Restart""" 70 15
								addButton: 3 r"""Quit""" 140 15
								init:
							)
						)
						case 1:
							(global1 restore:)
						#end:case
						case 2:
							(global1 restart: 1)
						#end:case
						case 3:
							global4 = 1
							(break)
						#end:case
					#end:match
				#end:loop
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class doorLocked(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: PolyPath 90 144 self)
			#end:case
			case 1:
				(global0
					view: 821
					normal: 0
					setPri: 12
					setScale: 0
					scaleX: 128
					scaleY: 128
					posn: 93 144
					loop: 5
					cel: 0
					cycleSpeed: 8
					setCycle: End self
				)
			#end:case
			case 2:
				(global0 loop: 6 cel: 0 setCycle: Fwd)
				seconds = 4
			#end:case
			case 3:
				(global0 setCycle: 0)
				cycles = 3
			#end:case
			case 4:
				(global91 say: 5 5 15 0 self)
			#end:case
			case 5:
				(global0 loop: 5 cel: 2 cycleSpeed: 8 setCycle: Beg self)
			#end:case
			case 6:
				(global0 reset: 1 posn: 90 144)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class unlockDoor(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(dungeonDoor hide:)
				(global0
					normal: 0
					setScale: 0
					view: 823
					loop: 0
					cel: 0
					cycleSpeed: 8
					posn: 56 109
					setCycle: CT 5 1 self
				)
			#end:case
			case 1:
				cycles = 50
			#end:case
			case 2:
				(global0 cel: 6)
				(global104 number: 781 loop: 1 play: self)
			#end:case
			case 3:
				(global91 say: 5 35 15 0 self)
			#end:case
			case 4:
				(global0 loop: 1 cel: 0 setCycle: End self)
				(global104 number: 821 loop: 1 play:)
			#end:case
			case 5:
				(kernel.ScriptID(80, 0) setFlag: 709 4096)
				(global2 newRoom: 710)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lookOutDoor(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: PolyPath 90 144 self)
			#end:case
			case 1:
				(global0
					view: 821
					normal: 0
					setPri: 12
					setScale: 0
					scaleX: 128
					scaleY: 128
					posn: 93 144
					loop: 5
					cel: 0
					cycleSpeed: 8
					setCycle: End self
				)
			#end:case
			case 2:
				(global91 say: 7 1 0 0 self)
			#end:case
			case 3:
				(global0 setCycle: Beg self)
			#end:case
			case 4:
				(global1 handsOn:)
				(global0 reset: 1 posn: 90 144)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class extraView(View):
	#property vars (may be empty)
	onMeCheck = 0
	view = 821
	loop = 3
	signal = 16400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match (kernel.ScriptID(80, 0) dungeonEntered:)
			case 3:
				(self cel: 1 x: 211 y: 125 noun: 8)
			#end:case
			else:
				(self cel: 0 x: 159 y: 108 noun: 9 onMeCheck: 26505)
			#end:else
		#end:match
		(super init: &rest)
	#end:method

#end:class or instance

@SCI.instance
class flame(Prop):
	#property vars (may be empty)
	x = 116
	y = 76
	noun = 11
	view = 821
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(torch doVerb: param1)
	#end:method

#end:class or instance

@SCI.instance
class wallReflection(Prop):
	#property vars (may be empty)
	x = 115
	y = 72
	onMeCheck = 0
	view = 821
	loop = 1
	signal = 16400
	cycleSpeed = 12
	
#end:class or instance

@SCI.instance
class dungeonDoor(Prop):
	#property vars (may be empty)
	x = 56
	y = 109
	noun = 5
	sightAngle = 45
	approachX = 91
	approachY = 145
	approachDist = 2
	view = 821
	loop = 2
	signal = 16384
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 5 35 2)
	#end:method

	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (param1 x:)
		temp1 = (param1 y:)
		if 
			(and
				((global69 curIcon:) == (global69 at: 4))
				((global69 curInvIcon:) == (global9 at: 44))
			)
			approachX = 82
			approachY = 144
		else:
			approachX = 91
			approachY = 145
		#endif
		(temp0 -= nsLeft)
		(temp1 -= nsTop)
		if ((<= 5 temp0 15) and (<= 11 temp1 24)):
			noun = 7
		else:
			noun = 5
		#endif
		return (super onMe: param1)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (noun == 5):
			match param1
				case 35:
					(cond
						case (not local0):
							(global91 say: noun param1 14)
						#end:case
						case (kernel.ScriptID(80, 0) tstFlag: 709 8192):
							(kernel.ScriptID(80, 0) setFlag: 709 4096)
							local0 = 0
							(global2 setScript: unlockDoor)
						#end:case
					)
				#end:case
				case 5:
					if (not local0):
						(global2 setScript: exitDungeon)
					else:
						(global2 setScript: doorLocked)
					#endif
				#end:case
				case 2:
					(global91
						say:
							noun
							param1
							(14 + (kernel.ScriptID(80, 0) tstFlag: 709 8192))
					)
				#end:case
				else:
					if ((global66 doit: param1) == -32768):
						(global91
							say:
								noun
								0
								(14 + (kernel.ScriptID(80, 0) tstFlag: 709 8192))
						)
					else:
						(super doVerb: param1)
					#endif
				#end:else
			#end:match
		else:
			match param1
				case 2:
					if local0:
						(global91 say: noun param1 15)
					else:
						(global91 say: noun param1 14)
					#endif
				#end:case
				case 1:
					(global2 setScript: lookOutDoor)
				#end:case
				else:
					noun = 5
					(self doVerb: param1)
				#end:else
			#end:match
		#endif
	#end:method

#end:class or instance

@SCI.instance
class ant(Actor):
	#property vars (may be empty)
	x = 149
	y = 185
	noun = 13
	view = 820
	loop = 8
	
#end:class or instance

@SCI.instance
class bed(Feature):
	#property vars (may be empty)
	noun = 8
	onMeCheck = 2
	
#end:class or instance

@SCI.instance
class torch(Feature):
	#property vars (may be empty)
	noun = 11
	onMeCheck = 4
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global91 say: noun param1 (14 + local0))
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class gargoyle(Feature):
	#property vars (may be empty)
	x = 56
	y = 144
	noun = 12
	onMeCheck = 8
	
#end:class or instance

@SCI.instance
class roomConv(Conversation):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose: &rest)
		caller = 0
	#end:method

#end:class or instance

@SCI.instance
class DeathWindow(SysWindow):
	#property vars (may be empty)
	@classmethod
	def open():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		color = 47
		back = 0
		(super open: &rest)
	#end:method

#end:class or instance

