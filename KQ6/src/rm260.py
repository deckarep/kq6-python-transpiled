#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 260
import sci_sh
import kernel
import Main
import KQ6Room
import n913
import Scaler
import MCyc
import PolyPath
import Polygon
import Feature
import MoveFwd
import LoadMany
import TimedCue
import Motion
import Game
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm260 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = 1
local1 = None
local2 = None
local3 = [0, 0, 0, 30, 0, 1, 4, 34, 0, 2, 8, 38, 0, 3, 13, 41, 0, 4, 18, 44, 0, 5, 24, 47, 0, 6, 30, 50, 0, 0, 37, 52, 0, 1, 44, 53, 0, 2, 52, 53, 0, 3, 60, 53, 0, 4, 68, 52, 0, 5, 75, 51, 0, 6, 82, 50, 0, 0, 89, 49, 0, 1, 97, 47, 0, 2, 104, 45, 2, 0, 108, 42, 2, 0, 114, 40, 2, 0, 119, 38, 2, 0, 124, 35, 2, 0, 129, 32, 2, 0, 134, 29, 2, 0, 139, 26, 2, 0, 145, 22, 2, 0, 151, 18, 2, 0, 157, 14, 2, 0, 163, 10, 2, 0, 169, 6, 2, 0, 176, 2, -32768, -32768]
local125 = [6, 0, 130, 1, 6, 1, 131, 3, 6, 2, 133, 6, 6, 3, 136, 9, 6, 4, 139, 13, 6, 5, 142, 17, 6, 6, 146, 21, 6, 0, 150, 24, 6, 1, 154, 27, 6, 2, 158, 30, 6, 3, 163, 33, 6, 4, 169, 35, 6, 5, 175, 36, 6, 6, 181, 35, 6, 0, 186, 33, 6, 1, 190, 30, 6, 2, 194, 27, 6, 3, 197, 23, 6, 4, 200, 19, 6, 5, 203, 15, 6, 6, 206, 11, 6, 0, 208, 6, 6, 1, 210, 2, -32768, -32768]
local219 = [6, 0, 177, 2, 6, 1, 176, 5, 6, 2, 174, 9, 6, 3, 172, 13, 6, 4, 169, 17, 6, 5, 166, 21, 6, 6, 163, 25, 6, 0, 159, 29, 6, 0, 155, 33, 6, 0, 151, 37, 6, 0, 146, 41, 6, 0, 141, 44, 7, 0, 136, 46, 7, 0, 132, 45, 7, 0, 128, 43, 7, 0, 124, 41, 7, 0, 120, 38, 7, 0, 116, 35, 7, 0, 112, 32, 7, 0, 109, 29, 7, 0, 105, 26, 7, 0, 101, 23, 7, 0, 97, 20, 7, 0, 92, 17, 7, 0, 86, 14, 7, 0, 80, 11, -32768, -32768]
local325 = [0, 0, 27, 3, 0, 1, 30, 7, 0, 2, 33, 12, 0, 3, 37, 16, 0, 4, 41, 20, 0, 5, 46, 24, 0, 6, 52, 28, 0, 0, 57, 32, 0, 1, 62, 35, 0, 2, 68, 37, 0, 3, 73, 38, 0, 4, 77, 38, 0, 5, 77, 38, 0, 6, 77, 38, 0, 0, 77, 38, 0, 1, 77, 38, 0, 2, 77, 38, 0, 3, 77, 38, 0, 4, 77, 38, 1, 0, 80, 37, 1, 0, 75, 36, 1, 0, 70, 35, 1, 0, 65, 34, 1, 0, 60, 32, 1, 0, 56, 30, 1, 0, 51, 28, 1, 0, 46, 26, 1, 0, 41, 24, 1, 0, 35, 22, 1, 0, 30, 20, 1, 0, 25, 19, 1, 0, 20, 18, 1, 0, 14, 17, 1, 0, 9, 16, 1, 0, 4, 15, -32768, -32768]
local467 = [0, 0, 264, 1, 0, 1, 260, 3, 0, 2, 255, 5, 0, 3, 249, 8, 0, 4, 243, 11, 0, 5, 237, 14, 0, 6, 231, 17, 0, 0, 226, 20, 0, 1, 221, 23, 0, 2, 216, 26, 0, 3, 209, 29, 0, 4, 202, 31, 0, 5, 195, 33, 0, 6, 187, 34, 0, 0, 180, 34, 0, 1, 174, 32, 0, 2, 169, 28, 0, 3, 165, 24, 0, 4, 162, 20, 0, 5, 158, 15, 0, 6, 155, 10, 0, 0, 153, 5, 0, 1, 152, 1, -32768, -32768]
local561 = None


@SCI.procedure
def localproc_0():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	local1 = 1
	(global0 observeControl: -32768 setMotion: MoveTo global70 (global71 - 11))
#end:procedure

class GenieCycler(Fwd):
	#property vars (may be empty)
	waitCounter = 3
	
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (temp0 = (self nextCel:) > (client lastCel:)):
				(self cycleDone:)
			#end:case
			case proc999_5((client loop:), 1, 5):
				if 
					(and
						(temp0 == 4)
						waitCounter.post('--')
						waitCounter = 3
						kernel.Random(0, 1)
					)
					(self cycleDone:)
				else:
					(client cel: temp0)
				#endif
			#end:case
			else:
				(client cel: temp0)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class rm260(KQ6Room):
	#property vars (may be empty)
	noun = 4
	picture = 260
	horizon = 0
	walkOffEdge = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global2
			addObstacle:
				((Polygon new:)
					type: 2
					init:
						186
						76
						199
						89
						199
						95
						190
						95
						188
						102
						179
						108
						84
						87
						50
						97
						3
						88
						3
						103
						36
						110
						90
						93
						171
						111
						158
						115
						157
						123
						139
						123
						133
						126
						134
						189
						0
						189
						0
						-10
						274
						-10
						274
						36
						259
						53
						226
						60
						197
						71
					yourself:
				)
				((Polygon new:)
					type: 2
					init:
						232
						93
						199
						74
						210
						69
						227
						63
						267
						55
						290
						38
						290
						-10
						319
						-10
						319
						105
						260
						105
					yourself:
				)
				((Polygon new:)
					type: 0
					init:
						260
						107
						318
						107
						317
						189
						137
						189
						136
						127
						218
						127
						218
						120
						232
						120
						232
						109
						220
						109
						220
						102
						231
						102
						230
						94
					yourself:
				)
				((Polygon new:)
					type: 2
					init: 220 125 220 122 239 122 239 125
					yourself:
				)
				((Polygon new:)
					type: 2
					init: 222 104 236 104 236 107 222 107
					yourself:
				)
		)
		(super init: &rest)
		(genericFeatures init:)
		(global0
			setScale: Scaler 97 20 150 30
			init:
			reset: 2
			actions: egoDoVerb
		)
		(kernel.ScriptID(10, 4) onMeCheck: 128 setOnMeCheck: 1 128 init:)
		(hatch init:)
		(sail1 init:)
		(sail2 init:)
		(sail3 init:)
		(sail4 init:)
		if ((global1 _detailLevel:) > 0):
			(BeachBird init:)
			if ((global1 _detailLevel:) >= 2):
				(sail1 setScript: kernel.Clone(sailScr))
				(sail2 setScript: kernel.Clone(sailScr))
				(sail3 setScript: sailScr)
			#endif
		#endif
		match global12
			case 290:
				(global1 handsOn:)
				(global0 posn: 18 105)
			#end:case
			else:
				(global2 setScript: enterVillage2Scr)
			#end:else
		#end:match
		if 
			(and
				proc913_0(16)
				(not (kernel.ScriptID(10, 0) isSet: 32))
				(global153 == 1)
			)
			(kernel.ScriptID(10, 0) setIt: 32)
			(genieBoy init: setScript: genieScr)
			(global102 number: 260 loop: -1 play:)
		else:
			(global102 number: 915 loop: -1 play:)
			(global103 number: 916 loop: -1 play:)
		#endif
		(ocean init:)
		(boatDoor init:)
		(holeInBoat init:)
		(reflect1 init: setCycle: Fwd)
		(reflect2 init: setCycle: Fwd)
		(reflect3 init: setCycle: Fwd)
		(reflect4 init: setCycle: Fwd)
		(reflect5 init: setCycle: Fwd)
		if 
			(and
				(not kernel.Random(0, 2))
				(global12 == 250)
				(not (global5 contains: genieBoy))
			)
			(smFerryman init: setScript: ferrymanScr)
		#endif
		(global73 addToFront: self)
		(global72 addToFront: self)
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 claimed:):
			return 1
		#endif
		if 
			(and
				(not (global2 script:))
				((param1 type:) != 16384)
				((param1 type:) & 0x0005)
				(not (param1 modifiers:))
				((param1 y:) > 56)
				(or
					(and
						((global69 curIcon:) == (global69 at: 0))
						proc999_5(kernel.OnControl(4, (param1 x:), (param1 y:)), 4, 32, 512)
						(global5 contains: genieBoy)
					)
					(and
						(kernel.OnControl(4, (param1 x:), (param1 y:)) == 4)
						((global69 curIcon:) == (global69 at: 1))
					)
				)
			)
			(self setScript: diveIntoWaterScr)
			(param1 claimed: 1)
			return
		else:
			(super handleEvent: param1 &rest)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case ((temp0 = (global0 onControl: 1) & 0x2000) and (not local561)):
				(global0 setPri: 5)
				local561 = 1
			#end:case
			case (local561 and (not (temp0 & 0x2000))):
				(global0 setPri: -1)
				local561 = 0
			#end:case
			case script: 0#end:case
			case (global0 inRect: 242 46 288 55):
				(global2 setScript: bailScr)
			#end:case
			case (temp0 & 0x0224):
				(global0 setMotion: 0)
				local1 = 0
				if ((global0 y:) > 124):
					(self setScript: egoFallForwardScr)
				else:
					(self setScript: egoFallRightScr)
				#endif
			#end:case
			case ((temp0 == 8192) and (global5 contains: genieBoy)):
				(global2 setScript: genieBailScr)
			#end:case
		)
		(super doit: &rest)
	#end:method

	@classmethod
	def scriptCheck():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((boatDoor script:) == knockOnDoorScr):
			(global91 say: 7 0 16 0 0 0)
			return 0
		#endif
		return 1
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global102 fade:)
		if (not (global5 contains: genieBoy)):
			(global103 fade:)
		#endif
		(global73 delete: self)
		(global72 delete: self)
		(super dispose:)
		kernel.DisposeScript(964)
		kernel.DisposeScript(231)
		kernel.DisposeScript(960)
		kernel.DisposeScript(942)
		kernel.DisposeScript(951)
	#end:method

#end:class or instance

@SCI.instance
class myMoveCycle(MCyc):
	#property vars (may be empty)
	@classmethod
	def nextCel():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (temp0 = proc999_6(points, value) == -4095):
				(client setPri: proc999_6(points, (value + 1)))
				(value += (cycleDir * 2))
				temp0 = proc999_6(points, value)
			#end:case
			case (temp0 == -4094):
				(client setPri: -1)
				(value += cycleDir)
				temp0 = proc999_6(points, value)
			#end:case
		)
		(client
			loop: proc999_6(points, value)
			cel: proc999_6(points, (value + 1))
			x: proc999_6(points, (value + 2))
			y: proc999_6(points, (value + 3))
		)
		(value += (cycleDir * 4))
		if 
			(or
				((cycleDir == 1) and (value >= size))
				((cycleDir == -1) and (value < 0))
			)
			(self cycleDone:)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class birdTimedCue(TimedCue):
	#property vars (may be empty)
	register = 1
	
#end:class or instance

@SCI.instance
class bailScr(Script):
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
				(global2 newRoom: 250)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class sailScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(client cycleSpeed: kernel.Random(10, 19) setCycle: End self)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				(client cycleSpeed: kernel.Random(10, 19) setCycle: Beg self)
				state = -1
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class ferrymanScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(client loop: 1 cel: 0 posn: 117 77 setCycle: End self)
			#end:case
			case 1:
				ticks = kernel.Random(45, 90)
			#end:case
			case 2:
				(client setCycle: End self)
			#end:case
			case 3:
				ticks = 30
			#end:case
			case 4:
				(client loop: 2 cel: 0 posn: 104 77 setCycle: End self)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				(global1 handsOn:)
				(client dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class snakeScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				seconds = kernel.Random(3, 5)
			#end:case
			case 1:
				(client setCycle: End self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				(client dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class snake(Prop):
	#property vars (may be empty)
	x = 313
	y = 64
	view = 264
	loop = 2
	scaleSignal = 1
	scaleX = 64
	scaleY = 64
	
#end:class or instance

@SCI.instance
class smFerryman(Actor):
	#property vars (may be empty)
	x = 117
	y = 77
	view = 263
	loop = 1
	signal = 16384
	
#end:class or instance

class BeachBird(Prop):
	#property vars (may be empty)
	view = 267
	signal = 16384
	previous = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self fly:)
	#end:method

	@classmethod
	def fly():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		while (previous == temp0 = kernel.Random(0, 3)):

		#end:loop
		match previous = temp0
			case 0:
				(self setPri: 2 cycleSpeed: 5 setCycle: MCyc @local3 self)
			#end:case
			case 1:
				(self setPri: 1 cycleSpeed: 10 setCycle: MCyc @local125 self)
			#end:case
			case 2:
				(self setPri: 1 cycleSpeed: 9 setCycle: MCyc @local219 self)
			#end:case
			case 3:
				(self setPri: 1 cycleSpeed: 7 setCycle: MCyc @local325 self)
			#end:case
			case 4:
				(self setPri: 2 cycleSpeed: 6 setCycle: MCyc @local467 self)
			#end:case
		#end:match
	#end:method

	@classmethod
	def cue(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (param1 == 1):
				(BeachBird show:)
				(self fly:)
			#end:case
			case (param1 == 4660):
				(self setScript: birdTimedCue kernel.Random(4, 12))
			#end:case
			else:
				(BeachBird hide:)
				if (not global18):
					global18 = (Set new:)
				#endif
				(global18
					add:
						((Cue new:)
							cuee: self
							cuer: self
							register: 4660
							yourself:
						)
				)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class toWaterNotFromPierScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				if ((global0 onControl: 1) & 0x2000):
					(global0 setMotion: PolyPath 196 73 self)
				else:
					(global0 setMotion: PolyPath 181 109 self)
				#endif
			#end:case
			case 1:
				(global1 handsOn:)
				(localproc_0)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoFallRightScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				proc958_0(128, 296, 269)
				(global0
					normal: 0
					setSpeed: 6
					view: 296
					loop: 2
					cel: 0
					setScale:
				)
				cycles = 2
			#end:case
			case 1:
				(global0 setCycle: End self)
			#end:case
			case 2:
				ticks = 45
			#end:case
			case 3:
				(global0 loop: 3 cel: 0)
				ticks = 15
			#end:case
			case 4:
				(global105 number: 923 loop: 1 play:)
				(global0 setPri: 1 setCycle: End self)
			#end:case
			case 5:
				(global102 stop:)
				(global104 number: 921 loop: 1 play:)
				(global0
					view: 269
					posn: ((global0 x:) + 21) ((global0 y:) + 48)
					setLoop: 0
					setSpeed: 5
					setStep: 5 5
					cel: 0
					setScale:
						Scaler
						100
						(((global0 scaleX:) * 100) / 128)
						190
						(global0 y:)
					setMotion: MoveTo 320 210 self
				)
				(self setScript: egoDrowningScr)
			#end:case
			case 6:
				(global2 newRoom: 135)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoFallForwardScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				proc958_0(128, 296, 269)
				(global0
					setSpeed: 6
					normal: 0
					view: 296
					setPri: 15
					posn: ((global0 x:) - 5) ((global0 y:) + 4)
					loop: 0
					cel: 0
					scaleX: 109
					scaleY: 109
					setScale:
				)
				cycles = 2
			#end:case
			case 1:
				(global0 setCycle: End self)
			#end:case
			case 2:
				ticks = 10
			#end:case
			case 3:
				(global0 loop: 1 cel: 0)
				ticks = 30
			#end:case
			case 4:
				(global105 number: 923 loop: 1 play:)
				(global0
					cel: 1
					posn: ((global0 x:) + 3) ((global0 y:) + 4)
					setCycle: End self
				)
			#end:case
			case 5:
				(global102 stop:)
				(global104 number: 921 loop: 1 play:)
				(global0
					view: 269
					setLoop: 0
					cel: 3
					posn: (global0 x:) 186
					setScale:
						Scaler
						100
						(((global0 scaleX:) * 100) / 128)
						190
						(global0 y:)
					setMotion: MoveTo (global0 x:) 210 self
				)
				(self setScript: egoDrowningScr)
			#end:case
			case 6:
				(global2 newRoom: 135)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoDrowningScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 setCycle: CT 7 1 self)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				(global0 setCycle: CT 3 -1 self)
			#end:case
			case 3:
				state = -1
				cycles = 2
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class enterVillage2Scr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 posn: 266 53 setMotion: MoveTo 226 61 self)
			#end:case
			case 1:
				(global0 setMotion: MoveTo 197 74 self)
			#end:case
			case 2:
				(global0 loop: 2)
				if 
					(and
						(not (global5 contains: genieBoy))
						(not (global5 contains: smFerryman))
					)
					(global1 handsOn:)
				#endif
				cycles = 1
			#end:case
			case 3:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genieBailScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: 0)
				cycles = 2
			#end:case
			case 1:
				(global0 setHeading: 180 self)
			#end:case
			case 2:
				if ((genieScr state:) < 25):
					(genieScr state: 26 seconds: 0 ticks: 0)
					if (not (genieScr cycles:)):
						(genieScr cycles: 1)
					#endif
				#endif
				((genieBoy script:) caller: self)
			#end:case
			case 3:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class changeMusicScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global102 number: 915 loop: -1 play: 0 fade: 127 10 25 0)
				(global103 number: 916 loop: -1 play:)
				state = -1
				client = 0
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class eye(Prop):
	#property vars (may be empty)
	x = 234
	y = 90
	view = 902
	priority = 15
	signal = 16
	
#end:class or instance

@SCI.instance
class genieScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				ticks = 12
			#end:case
			case 1:
				(eye init: setCycle: End self)
			#end:case
			case 2:
				ticks = 30
			#end:case
			case 3:
				(eye setCycle: Beg self)
			#end:case
			case 4:
				(eye dispose:)
				(genieBoy setCycle: CT 7 1 self)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				(global105 number: 923 loop: 1 play:)
				(genieBoy cel: 8 posn: 233 118)
				cycles = 2
			#end:case
			case 7:
				(genieBoy setCycle: End self)
			#end:case
			case 8:
				ticks = 48
			#end:case
			case 9:
				(genieBoy
					view: 262
					loop: 7
					cel: 0
					posn: 267 145
					setCycle: GenieCycler
				)
				ticks = 12
			#end:case
			case 10:
				(genieBoy setMotion: MoveTo 267 131 self)
			#end:case
			case 11:
				(genieBoy cycleSpeed: 9 loop: 9 cel: 0 setCycle: End self)
			#end:case
			case 12:
				(genieBoy cel: 0 setCycle: End self)
			#end:case
			case 13:
				(genieBoy cycleSpeed: 6 setCycle: GenieCycler loop: 7)
				cycles = 2
			#end:case
			case 14:
				(global91 say: 1 0 2 0 self)
			#end:case
			case 15:
				local2 = 1
				if (global2 script:):
					((global2 script:) caller: self)
				else:
					cycles = 2
				#endif
			#end:case
			case 16:
				(global0 setMotion: MoveTo 221 97 self)
			#end:case
			case 17:
				(global0 setHeading: 90 self)
			#end:case
			case 18:
				(global1 handsOn:)
				seconds = 6
			#end:case
			case 19:
				local2 = 0
				(genieBoy
					setLoop: (10 if ((genieBoy loop:) == 1) else 9)
					cel: 0
				)
				ticks = 72
			#end:case
			case 20:
				local2 = 1
				ticks = 12
			#end:case
			case 21:
				(global91 say: 1 0 3 0 self)
			#end:case
			case 22:
				seconds = 6
			#end:case
			case 23:
				local2 = 0
				(genieBoy
					setLoop: (10 if ((genieBoy loop:) == 1) else 9)
					cel: 0
				)
				ticks = 72
			#end:case
			case 24:
				local2 = 1
				cycles = 2
			#end:case
			case 25:
				(global91 say: 1 0 4 0 self)
			#end:case
			case 26:
				seconds = 7
			#end:case
			case 27:
				(global91 say: 1 0 5 1 self)
			#end:case
			case 28:
				local2 = 0
				(genieBoy view: 262 loop: 11 cel: 0 noun: 7 setCycle: End self)
				(global105 number: 943 loop: 1 play:)
			#end:case
			case 29:
				cycles = 2
			#end:case
			case 30:
				(changeMusicScr client: self)
				(global102 client: changeMusicScr fade:)
				(global91 say: 1 0 5 2 self)
			#end:case
			case 31:
				local2 = 0
				(client dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super doit: &rest)
		(cond
			case (not local2): 0#end:case
			case (((global0 y:) < 87) and ((genieBoy loop:) != 7)):
				(genieBoy loop: 7)
			#end:case
			case 
				(and
					((global0 y:) >= 87)
					((global0 y:) <= 111)
					((genieBoy loop:) != 1)
				):
				(genieBoy loop: 1)
			#end:case
			case (((global0 y:) >= 111) and ((genieBoy loop:) != 5)):
				(genieBoy loop: 5)
			#end:case
		)
	#end:method

#end:class or instance

@SCI.instance
class genieBoy(Actor):
	#property vars (may be empty)
	x = 229
	y = 110
	noun = 6
	approachX = 221
	approachY = 97
	view = 266
	loop = 1
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (noun == 7):
			(super doVerb: param1 &rest)
		else:
			match param1
				case 2:
					if (not (global5 contains: self)):
						return
					#endif
					if local0:
						local0 = 0
						(global91 say: noun param1 11)
					else:
						(global91 say: noun param1 12)
					#endif
				#end:case
				else:
					(super doVerb: param1 &rest)
				#end:else
			#end:match
		#endif
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 2)
	#end:method

#end:class or instance

@SCI.instance
class eyeGlint1(Prop):
	#property vars (may be empty)
	x = 275
	y = 142
	view = 262
	loop = 3
	priority = 15
	signal = 16
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self setCycle: End genieScr)
	#end:method

#end:class or instance

@SCI.instance
class diveIntoWaterScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				register = (global5 contains: genieBoy)
				if register:
					proc913_1(79)
					(genieBoy setScript: 0)
				#endif
				cycles = 1
			#end:case
			case 1:
				(global91 say: 7 3 13 1 self)
			#end:case
			case 2:
				(global0 setMotion: PolyPath 232 114 self)
			#end:case
			case 3:
				(global0
					normal: 0
					setPri: 8
					setSpeed: 6
					view: 265
					loop: 0
					cel: 0
					posn: 227 115
					setScale: 0
					scaleX: 98
					scaleY: 98
					scaleSignal: 1
					setCycle: CT 7 1 self
				)
				if register:
					(genieBoy loop: 5)
				#endif
			#end:case
			case 4:
				(global105 number: 923 loop: 1 play:)
				(global0 posn: 229 124 setCycle: End self)
				if register:
					(genieBoy loop: 2)
				#endif
			#end:case
			case 5:
				if register:
					(global91 say: 7 3 13 2 self)
				else:
					(self cue:)
				#endif
			#end:case
			case 6:
				(global91 say: 7 3 13 3 self)
			#end:case
			case 7:
				(global102 stop:)
				(global104 number: 921 loop: 1 play:)
				if register:
					(genieBoy setHeading: 180 setMotion: MoveFwd 100)
				#endif
				(global0
					view: 269
					moveSpeed: 3
					setLoop: 0
					cel: 3
					posn: 282 168
					setScale:
						Scaler
						100
						(((global0 scaleX:) * 100) / 128)
						190
						(global0 y:)
					setMotion: MoveTo 305 210 self
				)
				(self setScript: egoDrowningScr)
			#end:case
			case 8:
				(global2 newRoom: 135)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class ocean(Feature):
	#property vars (may be empty)
	noun = 7
	sightAngle = 40
	onMeCheck = 4
	approachX = 228
	approachY = 110
	
	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(ocean x: (param1 x:) y: (param1 y:))
		if temp0 = (super onMe: param1 &rest):
			if ((param1 y:) > 56):
				x = 320
				y = 91
				noun = 7
			else:
				x = 61
				y = 54
				noun = 29
			#endif
		#endif
		return temp0
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if proc999_5(param1, 5, 1):
			(super doVerb: param1 &rest)
		else:
			noun = 7
			(super doVerb: param1 &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class knockOnDoorScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				kernel.Load(132, 908)
				kernel.Load(128, 261)
				(global0 setHeading: 45 self)
			#end:case
			case 1:
				if (global5 contains: genieBoy):
					if ((genieScr state:) < 25):
						(genieScr state: 26 seconds: 0 ticks: 0 cycles: 0)
						if (not (genieScr cycles:)):
							(genieScr cycles: 1)
						#endif
					#endif
					((genieBoy script:) caller: self)
				else:
					ticks = 20
				#endif
			#end:case
			case 2:
				(global0
					normal: 0
					view: 261
					posn: 20 108
					loop: 2
					cel: 0
					scaleX: 128
					scaleY: 128
					setScale:
					setMotion: 0
					setSpeed: 6
				)
				cycles = 2
			#end:case
			case 3:
				(global0 setCycle: End self)
				register = 5
			#end:case
			case 4:
				register.post('--')
				(global0 cel: 0 loop: 3 setCycle: End self)
			#end:case
			case 5:
				(global105 number: 908 loop: 1 play:)
				if register:
					(state -= 2)
					ticks = 25
				else:
					(self cue:)
				#endif
			#end:case
			case 6:
				(global0 setCycle: Beg self)
			#end:case
			case 7:
				cycles = 2
			#end:case
			case 8:
				(global0
					posn: (boatDoor approachX:) (boatDoor approachY:)
					reset: 6
					setScale: Scaler 97 20 150 30
				)
				cycles = 2
			#end:case
			case 9:
				kernel.UnLoad(128, 261)
				ticks = 60
			#end:case
			case 10:
				(ferryMan view: 263 loop: 2 cel: 8 posn: 23 96 init:)
				(global105 number: 901 loop: 1 play:)
				(boatDoor setCycle: End self)
			#end:case
			case 11:
				ticks = 60
			#end:case
			case 12:
				if proc913_0(17):
					(state += 4)
					(global91 say: 2 5 8 0 self)
				else:
					(global91 say: 2 5 (18 if proc913_1(106) else 7) 0 self)
				#endif
			#end:case
			case 13:
				(global1 handsOn:)
				seconds = 10
			#end:case
			case 14:
				(global1 handsOff:)
				(global91 say: 1 0 6 1 self)
			#end:case
			case 15:
				(boatDoor setCycle: Beg self)
			#end:case
			case 16:
				(ferryMan dispose:)
				(global105 number: 902 loop: 1 play:)
				(boatDoor stopUpd:)
				(global1 handsOn:)
				(self dispose:)
			#end:case
			case 17:
				(global2 newRoom: 290)
			#end:case
		#end:match
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super doit: &rest)
		if (seconds and (not (global0 inRect: 5 94 33 109))):
			seconds = 0
			(self cue:)
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		seconds = 0
		if 
			(and
				temp0 = (global2 script:)
				(not proc999_5(temp0, talkReferenceScr, talkOrItemScr))
			)
			(temp0 dispose:)
		#endif
		(super dispose:)
	#end:method

#end:class or instance

@SCI.instance
class boatDoor(Prop):
	#property vars (may be empty)
	x = 22
	y = 80
	noun = 2
	approachX = 12
	approachY = 107
	view = 260
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(self setScript: knockOnDoorScr)
			#end:case
			else:
				(super doVerb: param1)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self sightAngle: 26505 approachVerbs: 5 stopUpd:)
	#end:method

#end:class or instance

@SCI.instance
class talkReferenceScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(boatDoor setScript: 0)
				(global91 say: 5 2 10 0 self)
			#end:case
			case 1:
				(global2 newRoom: 290)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class talkOrItemScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(boatDoor setScript: 0)
				if (register == 2):
					if proc913_1(105):
						temp0 = 17
					else:
						temp0 = 9
					#endif
				else:
					temp0 = 0
				#endif
				(global91 say: 5 register temp0 0 self)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				(boatDoor setCycle: Beg self)
			#end:case
			case 3:
				(ferryMan dispose:)
				(global105 number: 902 loop: 1 play:)
				(boatDoor stopUpd:)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		register = 0
		(super dispose:)
	#end:method

#end:class or instance

@SCI.instance
class ferryMan(View):
	#property vars (may be empty)
	x = 23
	y = 96
	noun = 5
	view = 263
	loop = 2
	cel = 8
	priority = 3
	signal = 16
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 2:
				if proc913_0(16):
					(global2 setScript: talkReferenceScr)
				else:
					(global2 setScript: talkOrItemScr 0 param1)
				#endif
			#end:case
			case 70:
				if proc913_1(104):
					(global91 say: noun param1 16)
				else:
					(global91 say: noun param1 15)
				#endif
			#end:case
			case 40:
				(global2 setScript: talkOrItemScr 0 param1)
			#end:case
			else:
				if ((global66 doit: param1) == -32768):
					(global2 setScript: talkOrItemScr 0 0)
				else:
					(super doVerb: param1 &rest)
				#endif
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self stopUpd:)
	#end:method

#end:class or instance

@SCI.instance
class hatch(Feature):
	#property vars (may be empty)
	x = 100
	y = 78
	noun = 24
	nsTop = 74
	nsLeft = 91
	nsBottom = 81
	nsRight = 109
	sightAngle = 45
	
#end:class or instance

@SCI.instance
class genericFeatures(Feature):
	#property vars (may be empty)
	sightAngle = 45
	
	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = kernel.OnControl(4, (param1 x:), (param1 y:))
		(genericFeatures x: (param1 x:) y: (param1 y:))
		(return
			(= noun
				match temp0
					case 1024: 10#end:case
					case 2048: 15#end:case
					case 8: 14#end:case
					case 16:
						(17 if ((param1 x:) < 170) else 0)
					#end:case
					case 512: 23#end:case
					case 256: 19#end:case
					case 2: 8#end:case
					case 4096: 13#end:case
					case 64:
						(16 if ((param1 y:) > 74) else 22)
					#end:case
					else:
						(18 if proc999_5(temp0, 16384, 8192) else 0)
					#end:else
				#end:match
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class sail1(Prop):
	#property vars (may be empty)
	x = 80
	y = 83
	z = 83
	noun = 14
	view = 260
	loop = 2
	priority = 15
	signal = 20496
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self
			cycleSpeed: ((sailScr register:) - 1)
			setCycle: kernel.ScriptID(231) ((self lastCel:) - 1)
		)
	#end:method

#end:class or instance

@SCI.instance
class sail2(Prop):
	#property vars (may be empty)
	x = 54
	y = 83
	z = 75
	noun = 14
	view = 260
	loop = 3
	priority = 15
	signal = 20496
	
#end:class or instance

@SCI.instance
class sail3(Prop):
	#property vars (may be empty)
	x = 21
	y = 83
	z = 57
	noun = 14
	view = 260
	loop = 4
	cel = 3
	priority = 15
	signal = 4112
	
#end:class or instance

@SCI.instance
class sail4(View):
	#property vars (may be empty)
	x = 9
	y = 83
	z = 52
	noun = 14
	view = 260
	loop = 5
	priority = 15
	signal = 4112
	
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
class reflect1(Prop):
	#property vars (may be empty)
	x = 65
	y = 176
	noun = 7
	view = 268
	cel = 2
	signal = 16384
	cycleSpeed = 10
	detailLevel = 3
	
#end:class or instance

@SCI.instance
class reflect2(Prop):
	#property vars (may be empty)
	x = 146
	y = 178
	noun = 7
	view = 268
	loop = 1
	cel = 1
	priority = 15
	signal = 16400
	cycleSpeed = 10
	detailLevel = 3
	
#end:class or instance

@SCI.instance
class reflect3(Prop):
	#property vars (may be empty)
	x = 210
	y = 186
	noun = 7
	view = 268
	loop = 2
	cel = 2
	priority = 15
	signal = 16400
	cycleSpeed = 10
	detailLevel = 3
	
#end:class or instance

@SCI.instance
class reflect4(Prop):
	#property vars (may be empty)
	x = 178
	y = 136
	noun = 7
	view = 268
	loop = 3
	signal = 16384
	cycleSpeed = 10
	detailLevel = 3
	
#end:class or instance

@SCI.instance
class reflect5(Prop):
	#property vars (may be empty)
	x = 277
	y = 113
	noun = 7
	view = 268
	loop = 4
	cel = 1
	priority = 1
	signal = 16400
	cycleSpeed = 20
	detailLevel = 3
	
#end:class or instance

@SCI.instance
class holeInBoat(Feature):
	#property vars (may be empty)
	x = 91
	y = 100
	noun = 11
	nsTop = 112
	nsLeft = 83
	nsBottom = 123
	nsRight = 100
	sightAngle = 45
	
#end:class or instance

