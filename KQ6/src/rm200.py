#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 200
import sci_sh
import kernel
import Main
import KQ6Room
import n913
import Inset
import Scaler
import PolyPath
import Polygon
import Feature
import MoveFwd
import StopWalk
import Rev
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm200 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = [176, 147, 238, 130, 250, 130, 250, 135, 189, 151]
local13 = [235, 133, 243, 133, 243, 139, 227, 139, 189, 151, 177, 146, 222, 129, 235, 129]
local29 = None
local30 = None


@SCI.procedure
def localproc_0():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	if proc913_0(11):
		proc913_2(11)
	else:
		proc913_1(11)
	#endif
	((global2 obstacles:) delete: plankPoly)
	(global2
		addObstacle:
			if proc913_0(11):
				(chest setPri: -1)
				(plankPoly type: 2 points: @local13 size: 8 yourself:)
			else:
				(chest setPri: 1)
				(plankPoly type: 2 points: @local3 size: 5 yourself:)
			#endif
	)
#end:procedure

@SCI.instance
class rm200(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 200
	horizon = 10
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global2
			addObstacle:
				((Polygon new:)
					type: 2
					init:
						150
						108
						114
						115
						102
						134
						62
						152
						-50
						189
						-50
						-200
						319
						-200
						319
						189
						215
						189
						263
						143
						271
						117
						222
						107
						210
						99
						205
						87
						211
						70
						235
						60
						267
						54
						250
						51
						192
						67
						187
						80
						191
						102
					yourself:
				)
				((Polygon new:)
					type: 2
					init: 214 117 232 117 243 120 243 125 193 125 193 123
					yourself:
				)
				((Polygon new:)
					type: 2
					init: 144 183 144 179 181 169 179 183
					yourself:
				)
		)
		(global69 enable:)
		if (global12 == 155):
			style = 6
		#endif
		(super init: &rest)
		(global0 ignoreActors: actions: egoDoVerb)
		(genericFeatures init:)
		(kernel.ScriptID(10, 4) onMeCheck: 32 init:)
		if (global2 script:):
			((global2 script:) caller: self)
		#endif
		if proc999_5(global12, 105, 106, 108, 99):
			(global0 init:)
			kernel.Palette(4, 0, 256, 100)
			(self setScript: kernel.ScriptID(201))
			global153 = 1
		else:
			match global12
				case 210:
					(global0 init:)
					(global2 setScript: enterRoomScr)
				#end:case
				case 155:
					(global0 init: view: 203)
					(global69 disable: 6)
					(global1 setCursor: global19)
					(self setScript: kernel.ScriptID(202))
				#end:case
				case 100:
					(global0
						init:
						posn: 175 130
						loop: 2
						setScale: Scaler 100 50 112 57
					)
					(global1 handsOn:)
					(global69 curIcon: (global69 at: 0))
					(global1 setCursor: ((global69 curIcon:) cursor:))
				#end:case
			#end:match
		#endif
		(bush1 init:)
		(bush2 init:)
		(bush3 init:)
		(shipsails init:)
		(wave init:)
		if ((global1 _detailLevel:) > 1):
			(wave setScript: waveScr)
			if ((global1 _detailLevel:) > 2):
				(bush1 setScript: kernel.Clone(kernel.ScriptID(13, 0)))
				(bush2 setScript: kernel.Clone(kernel.ScriptID(13, 0)))
				(shipsails setScript: kernel.Clone(kernel.ScriptID(13, 0)))
				(bush3 setScript: kernel.ScriptID(13, 0))
			#endif
		#endif
		if (global153 == 0):
			global153 = 1
		#endif
		if (((global9 at: 39) owner:) == 200):
			(royalRing init:)
		#endif
		(plank init:)
		(shipWheel init:)
		local0 = 0
		if (global12 == 155):
			(global102 fade:)
		else:
			(global102 number: 915 loop: -1 play:)
		#endif
		(global103 number: 916 loop: -1 play:)
		(global93 addToFront: self)
		(global74 addToFront: self)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global0 setScale: Scaler 100 50 112 57)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super doit:)
		(cond
			case ((temp0 = (global0 onControl: 1) & 0x0100) and (not local29)):
				local29 = 1
				(plank setPri: 15)
			#end:case
			case ((not (temp0 & 0x0100)) and local29):
				local29 = 0
				(plank setPri: 3)
			#end:case
		)
		(cond
			case script: 0#end:case
			case (temp0 & 0x4000):
				(global2 setScript: exitRoomScr)
			#end:case
			case (temp0 & 0x0004):
				(cond
					case (local0 != 1):
						(global104 number: 922 loop: -1 play:)
						(global0 view: 308)
						if (not ((global0 cycler:) isKindOf: StopWalk)):
							(global0 setCycle: StopWalk -1)
						#endif
						if (local0 == 0):
							(cond
								case ((global0 heading:) < 135):
									(global0 loop: 0)
								#end:case
								case ((global0 heading:) > 225):
									(global0 loop: 1)
								#end:case
								else:
									(global0 loop: 2)
								#end:else
							)
						#endif
						local0 = 1
					#end:case
					case (and (global0 isStopped:) (not local2) local1):
						(global91 say: 10 3 12 1)
						local2 = 1
					#end:case
				)
			#end:case
			case (temp0 & 0x0200):
				(cond
					case (local0 != 2):
						if (local0 == 0):
							(global104 number: 922 loop: -1 play:)
						#endif
						(global0 view: 3081)
						if 
							(and
								(not ((global0 cycler:) isKindOf: StopWalk))
								(not ((global0 cycler:) isKindOf: Rev))
							)
							(global0 setCycle: StopWalk -1)
						#endif
						local0 = 2
					#end:case
					case (and (global0 isStopped:) (not local2) local1):
						if local30:
							(self setScript: egoStruggleScr)
							local2 = 1
							local30 = 0
						else:
							(global91 say: 10 3 12 1)
							local2 = 1
						#endif
					#end:case
				)
			#end:case
			case (temp0 & 0x0008):
				if (local0 != 3):
					if local1:
						(global1 handsOff:)
						(global0
							setLoop: (global0 loop:)
							setMotion: 0
							normal: 0
							setSpeed: 8
							setCycle: Rev
						)
						while True: #repeat
							(global0 y: ((global0 y:) - 1))
							(breakif (not ((global0 onControl: 1) & 0x0008)))
						#end:loop
						local30 = 1
					else:
						(self setScript: deathByWaterScr)
					#endif
					local0 = 3
				#endif
			#end:case
			case (local0 != 0):
				(global104 fade: 0 10 15 1)
				(global0 view: 900 setCycle: Walk)
				local0 = 0
			#end:case
		)
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((param1 type:) & 0x1040):
			if (((global69 at: 0) == (global69 curIcon:)) and (local0 == 0)):
				local1 = 1
				local2 = 0
			else:
				local1 = 0
			#endif
		else:
			(super handleEvent: param1)
		#endif
		(param1 claimed:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			match param1
				case 2:
					(global91 say: noun param1 5)
					1
				#end:case
				else:
					(super doVerb: param1)
				#end:else
			#end:match
		)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global102 fade:)
		(global103 fade:)
		(global93 delete: self)
		(global74 delete: self)
		(super dispose:)
		kernel.DisposeScript(951)
		kernel.DisposeScript(969)
		kernel.DisposeScript(923)
		kernel.DisposeScript(13)
	#end:method

#end:class or instance

@SCI.instance
class sandPoly(Polygon):
	#property vars (may be empty)
	type = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super
			init:
				92
				58
				151
				58
				157
				65
				95
				93
				100
				115
				139
				132
				170
				132
				196
				143
				93
				143
		)
	#end:method

#end:class or instance

@SCI.instance
class sand(Feature):
	#property vars (may be empty)
	y = 190
	noun = 14
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		onMeCheck = (sandPoly init: yourself:)
		(self setOnMeCheck: 2 onMeCheck)
		sightAngle = 26505
	#end:method

#end:class or instance

@SCI.instance
class chestInset(Inset):
	#property vars (may be empty)
	view = 202
	x = 170
	y = 98
	priority = 15
	disposeNotOnMe = 1
	noun = 8
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		if (((global9 at: 9) owner:) == global11):
			(coin init:)
		#endif
		(sand init:)
		(global1 handsOn:)
		(global69 disable: 0 3 4 5 6)
	#end:method

	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if 
			proc999_4(((insetView nsLeft:) + 5), ((insetView nsTop:) + 5), (-
				(insetView nsRight:)
				5
			), ((insetView nsBottom:) - 5), param1)
			return 1
		else:
			return 0
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (global5 contains: 9):
			(coin dispose:)
		#endif
		(sand dispose:)
		(super dispose:)
		(global69 enable: 0 3 6)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				if (((global9 at: 9) owner:) == 200):
					(global91 say: noun param1 10)
				else:
					(global91 say: noun param1 11)
				#endif
			#end:case
			case 5:
				if (((global9 at: 9) owner:) == 200):
					(global91 say: noun param1 10)
				else:
					(global91 say: noun param1 11)
				#endif
			#end:case
			case 40:
				(global91 say: 5 param1)
			#end:case
			else:
				if (param1 != 2):
					param1 = 0
				#endif
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class plankPoly(Polygon):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class egoDoVerb(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 12:
				(global2 setScript: 130)
				return 1
			#end:case
			else:
				return 0
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class exitRoomScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: PolyPath 252 58 self)
			#end:case
			case 1:
				(global0
					ignoreActors:
					setPri: 1
					setLoop: 3
					setScale:
					illegalBits: 0
					setMotion: MoveTo 261 86 self
				)
			#end:case
			case 2:
				(global2 newRoom: 210)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class enterRoomScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0
					setPri: 1
					setLoop: 2
					posn: 261 86
					scaleX: 64
					scaleY: 64
					scaleSignal: 1
					show:
					setMotion: MoveTo 252 58 self
				)
			#end:case
			case 1:
				(global0
					setPri: -1
					setLoop: -1
					setScale: Scaler 100 50 112 57
					setMotion: PolyPath 204 103 self
				)
			#end:case
			case 2:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getCoinScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global69 enable: 6)
				(global1 handsOff:)
				(global0 get: 9)
				(global1 givePoints: 1)
				(coin dispose:)
				cycles = 2
			#end:case
			case 1:
				(global91 say: 7 5)
				cycles = 2
			#end:case
			case 2:
				(chestInset dispose:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoStruggleScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				register = kernel.Random(2, 4)
				ticks = 30
			#end:case
			case 1:
				if ((global0 loop:) == 2):
					(global0 setLoop: 1)
				else:
					(global0 setLoop: 2)
				#endif
				if (not register.post('--')):
					state.post('--')
				#endif
				ticks = 30
			#end:case
			case 2:
				(global0 normal: 1 setCycle: StopWalk -1 setLoop: -1)
				cycles = 2
			#end:case
			case 3:
				(global91 say: 10 3 12 1 self)
			#end:case
			case 4:
				(global0 setSpeed: (global0 currentSpeed:))
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoIntoSafeWater(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 setMotion: 0 view: 308)
				(global91 say: 10 3 12 1 self)
			#end:case
			case 1:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class deathByWaterScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91 say: 10 3 15 0 self)
			#end:case
			case 1:
				(global104 stop: number: 921 loop: 1 play:)
				(global0
					view: 269
					setLoop: 0
					cel: 0
					normal: 0
					cycleSpeed: 6
					setCycle: End self
					heading: 200
					setMotion: MoveFwd 200
				)
			#end:case
			case 2:
				(global2 newRoom: 135)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class replacePlankScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(localproc_0)
				(global0
					normal: 0
					posn: 242 139
					setSpeed: 6
					view: 201
					loop: 1
					cel: 8
					setScale: 0
					setCycle: CT 5 -1 self
				)
			#end:case
			case 1:
				(plank cel: 0 hide:)
				(global0 loop: 2 cel: 5 setCycle: CT 3 -1 self)
				(global105 number: 200 loop: 1 play:)
			#end:case
			case 2:
				(plank show: stopUpd:)
				cycles = 1
			#end:case
			case 3:
				(global0 setCycle: Beg self)
			#end:case
			case 4:
				(chest dispose:)
				(global0
					posn: (plank approachX:) (plank approachY:)
					reset: 2
					setScale: Scaler 100 50 112 57
				)
				cycles = 2
			#end:case
			case 5:
				(global91 say: 4 5 7 0 self)
			#end:case
			case 6:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class displacePlankScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					setSpeed: 6
					posn: 242 139
					view: 201
					normal: 0
					loop: 2
					cel: 0
					setScale: 0
					setCycle: CT 3 1 self
				)
			#end:case
			case 1:
				(chest init:)
				(global105 number: 200 loop: 1 play:)
				cycles = 2
			#end:case
			case 2:
				(plank cel: 1 hide:)
				cycles = 1
			#end:case
			case 3:
				(global0 setCycle: CT 4 1 self)
			#end:case
			case 4:
				(plank show: stopUpd:)
				(global0 setCycle: End self)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				(global0 loop: 1 cel: 5 setCycle: End self)
			#end:case
			case 7:
				(global0
					reset: 5
					posn: (plank approachX:) (plank approachY:)
					setScale: Scaler 100 50 112 57
				)
				(localproc_0)
				cycles = 2
			#end:case
			case 8:
				(global91 say: 4 5 6 0 self)
			#end:case
			case 9:
				if (not proc913_1(92)):
					(global1 givePoints: 1)
				#endif
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class objectGlitter(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				seconds = kernel.Random(2, 7)
			#end:case
			case 1:
				state = -1
				(client cel: 0 setCycle: End self)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class openChestScr(Script):
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
					setSpeed: 6
					normal: 0
					posn: (chest x:) (chest y:)
					view: 201
					loop: 3
					cel: 0
					setScale: 0
					setCycle: End self
				)
			#end:case
			case 2:
				ticks = 12
			#end:case
			case 3:
				(global105 number: 904 loop: 1 play: self)
			#end:case
			case 4:
				ticks = 12
			#end:case
			case 5:
				(chestInset init: self global2)
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				(global1 handsOff:)
				ticks = 1
			#end:case
			case 8:
				(global105 number: 905 loop: 1 play: self)
			#end:case
			case 9:
				ticks = 12
			#end:case
			case 10:
				(global0 setCycle: Beg self)
			#end:case
			case 11:
				(global0 posn: 240 132 reset: 2 setScale: Scaler 100 50 112 57)
				cycles = 2
			#end:case
			case 12:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class chest(Prop):
	#property vars (may be empty)
	x = 237
	y = 137
	noun = 5
	sightAngle = 45
	approachX = 235
	approachY = 132
	view = 200
	loop = 4
	cel = 2
	signal = 16385
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(self setScript: openChestScr)
			#end:case
			case 1:
				(global91 say: noun param1 9)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 5)
	#end:method

#end:class or instance

@SCI.instance
class takeRingScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				if ((global0 loop:) != 1):
					(global0 setHeading: 315 self)
				else:
					(self cue:)
				#endif
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				(global0
					normal: 0
					setSpeed: 8
					view: 201
					loop: 4
					cel: 0
					setCycle: End self
				)
				(royalRing dispose:)
			#end:case
			case 3:
				(global1 givePoints: 1)
				(global0 reset: 7 get: 39)
				cycles = 2
			#end:case
			case 4:
				(global91 say: 9 5 0 0 self)
			#end:case
			case 5:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class royalRing(Prop):
	#property vars (may be empty)
	x = 104
	y = 134
	noun = 9
	sightAngle = 45
	approachX = 134
	approachY = 136
	view = 202
	loop = 2
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global2 setScript: takeRingScr)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self
			cel: 0
			setCycle: End
			setScript: kernel.Clone(objectGlitter)
			approachVerbs: 5
		)
		if (not proc913_0(48)):
			loop = 3
		#endif
		(super init: &rest)
	#end:method

#end:class or instance

@SCI.instance
class coin(Prop):
	#property vars (may be empty)
	x = 188
	y = 191
	z = 70
	noun = 7
	sightAngle = 360
	view = 202
	loop = 1
	cel = 8
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self
			cel: 0
			setCycle: End
			setScript: kernel.Clone(objectGlitter)
			sightAngle: 360
			setPri: 15
		)
		(super init: &rest)
		sightAngle = 26505
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global2 setScript: getCoinScr)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class shipsails(Prop):
	#property vars (may be empty)
	x = 56
	y = 46
	noun = 11
	view = 200
	cel = 2
	signal = 4097
	cycleSpeed = 2
	
#end:class or instance

@SCI.instance
class bush1(Prop):
	#property vars (may be empty)
	x = 98
	y = 99
	noun = 15
	view = 200
	loop = 1
	cel = 4
	signal = 4097
	cycleSpeed = 2
	
#end:class or instance

@SCI.instance
class bush2(Prop):
	#property vars (may be empty)
	x = 291
	y = 85
	noun = 15
	view = 200
	loop = 2
	cel = 2
	signal = 4097
	cycleSpeed = 3
	
#end:class or instance

@SCI.instance
class bush3(Prop):
	#property vars (may be empty)
	x = 162
	y = 20
	noun = 15
	view = 200
	loop = 3
	cel = 2
	signal = 4097
	cycleSpeed = 3
	
#end:class or instance

@SCI.instance
class plank(View):
	#property vars (may be empty)
	x = 242
	y = 139
	noun = 4
	sightAngle = 45
	approachX = 244
	approachY = 132
	view = 200
	loop = 4
	signal = 20481
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				if proc913_0(11):
					(global2 setScript: replacePlankScr)
				else:
					(global2 setScript: displacePlankScr)
				#endif
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self
			approachVerbs: 5
			cel:
				if proc913_0(11):
					(chest init:)
					1
				else:
					0
				#endif
		)
		(global2
			addObstacle:
				if proc913_0(11):
					(chest setPri: -1)
					(plankPoly type: 2 points: @local13 size: 8 yourself:)
				else:
					(chest setPri: 1)
					(plankPoly type: 2 points: @local3 size: 5 yourself:)
				#endif
		)
	#end:method

#end:class or instance

@SCI.instance
class genericFeatures(Feature):
	#property vars (may be empty)
	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = kernel.OnControl(4, (param1 x:), (param1 y:))
		(genericFeatures x: (param1 x:) y: (param1 y:))
		(return
			(= noun
				(cond
					case (temp0 == 128): 15#end:case
					case 
						(or
							(temp0 == 256)
							((temp0 == 2048) and ((param1 y:) > 91))
						):
						14
					#end:case
					case (temp0 == 64): 12#end:case
					case (temp0 == 16): 11#end:case
					case ((temp0 == 512) and ((param1 y:) < 130)): 16#end:case
					case (temp0 == 2048): 17#end:case
					case (temp0 == 16): 11#end:case
					case proc999_5(temp0, 8, 4, 512): 10#end:case
					case proc999_5(temp0, 1024, 16384): 19#end:case
					else: 0#end:else
				)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class waveScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(wave cel: 0 setCycle: End self)
			#end:case
			case 1:
				(wave setCycle: Beg self)
			#end:case
			case 2:
				(wave hide:)
				seconds = kernel.Random(3, 8)
			#end:case
			case 3:
				(wave show:)
				state = -1
				(self cue:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class wave(Prop):
	#property vars (may be empty)
	x = 129
	y = 158
	noun = 10
	view = 204
	priority = 1
	signal = 20496
	
#end:class or instance

@SCI.instance
class shipWheel(Feature):
	#property vars (may be empty)
	x = 160
	y = 176
	noun = 18
	
	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(or
				proc999_4(145, 175, 160, 181, (param1 x:), (param1 y:))
				proc999_4(162, 169, 175, 177, (param1 x:), (param1 y:))
				proc999_4(171, 164, 177, 169, (param1 x:), (param1 y:))
				proc999_4(156, 170, 162, 175, (param1 x:), (param1 y:))
			)
		)
	#end:method

#end:class or instance

