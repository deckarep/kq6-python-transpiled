#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 870
import sci_sh
import kernel
import Main
import rgCastle
import n913
import Conversation
import Scaler
import PolyPath
import Polygon
import Feature
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	rm870 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.instance
class rm870(CastleRoom):
	#property vars (may be empty)
	noun = 3
	picture = 870
	style = 10
	east = 860
	west = 850
	vanishingY = -400
	minScaleSize = 70
	minScaleY = 138
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.Load(128, 723)
		(self
			addObstacle:
				((Polygon new:)
					type: 2
					init:
						0
						-10
						319
						-10
						319
						140
						298
						140
						288
						143
						219
						143
						202
						140
						90
						140
						80
						144
						0
						144
					yourself:
				)
		)
		(global32 add: roomStuff cassima_door horse bench eachElementDo: #init)
		spotEgoScr = walkGuardOn
		(super init: &rest)
		(global0
			init:
			setScale: Scaler maxScaleSize minScaleSize maxScaleY minScaleY
		)
		match global12
			case 860:
				(global0 posn: 305 168)
			#end:case
			else:
				(global0 posn: 13 167)
				(cond
					case (not (kernel.ScriptID(80, 0) tstFlag: 710 64)):
						(self setScript: firstTime)
					#end:case
					case (not (kernel.ScriptID(80, 0) tstFlag: 710 32)):
						(self setScript: stillCrying)
					#end:case
					case 
						(and
							(not (kernel.ScriptID(80, 0) tstFlag: 711 256))
							kernel.Random(0, 1)
						):
						(global2 spotEgo: kernel.ScriptID(80, 5))
					#end:case
					else:
						(kernel.ScriptID(80, 0) guard2Timer: 15)
					#end:else
				)
			#end:else
		#end:match
		((global0 scaler:) doit:)
		if (not script):
			(global1 handsOn:)
		#endif
		if 
			(and
				((global103 number:) != 710)
				(kernel.ScriptID(80, 0) tstFlag: 710 4)
				(not (kernel.ScriptID(80, 0) tstFlag: 710 8))
			)
			(global102 fadeTo: 703 -1)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (temp0 = (global0 onControl: 1) & 0x6000):
			(global2 newRoom: east)
		#endif
		(super doit: &rest)
	#end:method

	@classmethod
	def warnUser(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 3:
				if ((argc > 1) and param2):
					(global2 spotEgo: kernel.ScriptID(80, 5))
				else:
					(self setScript: warnAboutGuard)
				#endif
			#end:case
			else:
				(super warnUser: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class firstTime(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(kernel.ScriptID(80, 0) setFlag: 710 64)
				cycles = 2
			#end:case
			case 1:
				(global91 say: 1 0 1 0 self)
			#end:case
			case 2:
				(kernel.ScriptID(80, 0) guard2Timer: 31)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class stillCrying(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				register = (kernel.ScriptID(80, 0) guard2Timer:)
				(kernel.ScriptID(80, 0) guard2Timer: 0)
				cycles = 2
			#end:case
			case 1:
				(global91 say: 1 0 6 0 self)
			#end:case
			case 2:
				(global1 handsOn:)
				(kernel.ScriptID(80, 0) guard2Timer: (register + 1))
				register = 0
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class bendOverToDoor(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((client == global2) and (not next)):
			(kernel.ScriptID(80, 0) guardTimer: local0 guard2Timer: local1)
			local0 = local1 = 0
			(global1 handsOn:)
		#endif
		(super dispose: &rest)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				if (not local1):
					local0 = (kernel.ScriptID(80, 0) guardTimer:)
					local1 = (kernel.ScriptID(80, 0) guard2Timer:)
				#endif
				(kernel.ScriptID(80, 0) guardTimer: 0 guard2Timer: 0)
				(global0
					view: 723
					normal: 0
					loop: 0
					cel: 0
					posn: 32 154
					setScale: 0
					scaler: 0
					cycleSpeed: 9
					setCycle: End self
				)
			#end:case
			case 1:
				(global0
					reset: 3
					posn: (cassima_door approachX:) (cassima_door approachY:)
					setScale:
						Scaler
						(global2 maxScaleSize:)
						(global2 minScaleSize:)
						(global2 maxScaleY:)
						(global2 minScaleY:)
				)
				((global0 scaler:) doit:)
				cycles = 2
			#end:case
			case 2:
				if next:
					(next next: self)
				#endif
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class giveDagger(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global91 say: 6 8 11 0 self)
				(global1 givePoints: 3)
				(global0 put: 8 870)
				next = 0
			#end:case
			case 1:
				(global1 handsOn:)
				(kernel.ScriptID(80, 0) guardTimer: local0 guard2Timer: local1)
				local0 = local1 = 0
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class showLetter(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global91 say: 6 61 12 1 self)
			#end:case
			case 1:
				(global91 say: 6 61 12 2 self)
			#end:case
			case 2:
				seconds = 6
			#end:case
			case 3:
				(global91 say: 6 61 12 3 self oneOnly: 0)
			#end:case
			case 4:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walkGuardOn(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global105 number: 702 loop: 1 play:)
				(kernel.ScriptID(80, 5)
					init:
					loop: 3
					setScale:
						Scaler
						(global2 maxScaleSize:)
						(global2 minScaleSize:)
						(global2 maxScaleY:)
						(global2 minScaleY:)
					posn: 336 172
					setMotion: MoveTo 314 150 self
				)
			#end:case
			case 1:
				proc913_4(register, global0, self)
			#end:case
			case 2:
				(global91 say: 1 0 3 1 self)
			#end:case
			case 3:
				(global91 say: 1 0 3 2 self)
			#end:case
			case 4:
				(kernel.ScriptID(80, 5) setScript: kernel.ScriptID(80, 4) self 1)
			#end:case
			case 5:
				(global91 say: 1 0 3 3 self)
			#end:case
			case 6:
				temp0 = proc999_3(160, proc999_2(185, (kernel.ScriptID(80, 5) y:)))
				(kernel.ScriptID(80, 6)
					init:
					setScale:
						Scaler
						(global2 maxScaleSize:)
						(global2 minScaleSize:)
						(global2 maxScaleY:)
						(global2 minScaleY:)
					posn: 336 172
					setSpeed: (kernel.ScriptID(80, 5) cycleSpeed:)
					setMotion: MoveTo 300 temp0 self
				)
			#end:case
			case 7:
				(kernel.ScriptID(80, 6)
					setMotion:
						PolyPath
						((kernel.ScriptID(80, 5) x:) + 10)
						(global0 y:)
						self
				)
			#end:case
			case 8:
				(global91 say: 1 0 3 4 self oneOnly: 0)
			#end:case
			case 9:
				cycles = 2
			#end:case
			case 10:
				(global2 newRoom: 820)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class warnAboutGuard(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global91 say: 1 0 2 0 self)
			#end:case
			case 1:
				(kernel.ScriptID(80, 0) guard2Timer: 6)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class cassima_door(Feature):
	#property vars (may be empty)
	x = 44
	y = 141
	z = 21
	noun = 6
	nsTop = 100
	nsLeft = 32
	nsBottom = 141
	nsRight = 57
	sightAngle = 40
	approachX = 35
	approachY = 144
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 8 2)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if proc999_5(param1, 5, 1):
			(super doVerb: param1 &rest)
		else:
			match param1
				case 2:
					if (kernel.ScriptID(80, 0) tstFlag: 710 4):
						if (((global9 at: 8) owner:) == 870):
							(global91 say: noun param1 15)
						else:
							(global91 say: noun param1 9)
						#endif
					else:
						(global1 givePoints: 1)
						(global102 fadeTo: 703 -1)
						(roomConv
							add: -1 noun param1 7 1
							add: -1 noun param1 7 2
							add: -1 noun param1 7 3
						)
						if (not proc999_5(((global9 at: 39) owner:), 140, 210)):
							(roomConv
								add: -1 noun param1 7 4
								add: -1 noun param1 7 5
								add: -1 noun param1 7 6
							)
						else:
							(roomConv
								add: -1 noun param1 8 1
								add: -1 noun param1 8 2
								add: -1 noun param1 8 3
							)
						#endif
						(roomConv
							add: -1 noun param1 7 7
							add: -1 noun param1 7 8
							add: -1 noun param1 7 9
							add: -1 noun param1 7 10
							add: -1 noun param1 7 11
							add: -1 noun param1 7 12
							add: -1 noun param1 7 13
							add: -1 noun param1 7 14
							init:
						)
					#endif
					(kernel.ScriptID(80, 0) setFlag: 710 4)
				#end:case
				case 8:
					if (kernel.ScriptID(80, 0) tstFlag: 710 4):
						(bendOverToDoor next: giveDagger)
						(global2 setScript: bendOverToDoor)
					else:
						(global91 say: noun 0 10 0)
					#endif
				#end:case
				case 64:
					(global91 say: noun param1)
				#end:case
				case 16:
					(global91 say: noun param1)
				#end:case
				case 61:
					(cond
						case (kernel.ScriptID(80, 0) tstFlag: 710 8):
							(global91 say: noun param1 14)
						#end:case
						case (kernel.ScriptID(80, 0) tstFlag: 710 4):
							(kernel.ScriptID(80, 0) setFlag: 710 8)
							(bendOverToDoor next: showLetter)
							(global2 setScript: bendOverToDoor)
						#end:case
						else:
							(global91 say: noun 0 10 0)
						#end:else
					)
				#end:case
				else:
					if (kernel.ScriptID(80, 0) tstFlag: 710 4):
						(global91 say: noun 0 11 0)
					else:
						(global91 say: noun 0 10 0)
					#endif
				#end:else
			#end:match
		#endif
	#end:method

#end:class or instance

@SCI.instance
class bench(Feature):
	#property vars (may be empty)
	y = 1
	noun = 11
	onMeCheck = 128
	
#end:class or instance

@SCI.instance
class horse(Feature):
	#property vars (may be empty)
	y = 1
	noun = 12
	onMeCheck = 256
	
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
				((0x2002 & temp0) and noun = 9)
				((<= 0 (param1 y:) 137) and noun = 10)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class roomConv(Conversation):
	#property vars (may be empty)
#end:class or instance

