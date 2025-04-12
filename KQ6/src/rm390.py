#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 390
import sci_sh
import kernel
import Main
import KQ6Print
import KQ6Room
import n913
import PolyPath
import Polygon
import Feature
import LoadMany
import StopWalk
import SmoothLooper
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm390 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = [37, 122, 85, 157, 246, 157, 286, 141, 276, 139, 241, 151, 89, 151, 45, 121]
local18 = [33, 137, 75, 159, 207, 149, 255, 122, 233, 122, 203, 141, 84, 152, 48, 134]


@SCI.instance
class rm390(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 390
	horizon = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		local0 = 10
		(global2 addObstacle: (roomPoly points: @local2 yourself:))
		kernel.Palette(4, 64, 223, 60)
		(super init: &rest)
		proc958_0(128, 3931, 390, 3903, 3904, 391, 392, 393)
		(global32
			add: opening floor westEnd eastEnd mintHole
			eachElementDo: #init
		)
		(global103 number: 390 setLoop: -1 play:)
		(global2 setScript: enterScr)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				(global91 say: 3 1 local0 1)
				1
			#end:case
			case 5:
				if (local0 == 10):
					(global91 say: 3 5 local0 1)
					1
				else:
					(super doVerb: param1 &rest)
				#endif
			#end:case
			case 2:
				if (local0 == 10):
					(self setScript: caveTalkScr)
				else:
					(super doVerb: param1 &rest)
				#endif
			#end:case
			case 20:
				if (local0 == 10):
					(global2 setScript: lightItUp)
				else:
					1
					(global91 say: 2 20 local0 1)
				#endif
			#end:case
			else:
				if (local0 == 10):
					(global91 say: 3 0 local0 1)
					1
				else:
					(super doVerb: param1 &rest)
				#endif
			#end:else
		#end:match
		return 1
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.Wait(3)
		(super doit: &rest)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.Palette(4, 64, 223, 100)
		(global103 fade: 0 10 10)
		kernel.DisposeScript(968)
		(super dispose:)
	#end:method

#end:class or instance

@SCI.instance
class roomPoly(Polygon):
	#property vars (may be empty)
	size = 8
	type = 3
	
#end:class or instance

@SCI.instance
class mySmooper(SmoothLooper):
	#property vars (may be empty)
	cycleSpeed = 6
	vChangeDir = 3931
	
#end:class or instance

@SCI.instance
class floor(Feature):
	#property vars (may be empty)
	x = 160
	y = 150
	noun = 13
	onMeCheck = 16
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				if (local0 == 10):
					(global91 say: 12 1 10 1)
				else:
					(global91 say: 13 1 11 1)
				#endif
			#end:case
			case 5:
				if (local0 == 10):
					(global91 say: 12 5 10 1)
				else:
					(global91 say: 13 5 11 1)
				#endif
			#end:case
			else:
				(global2 doVerb: param1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class toCave1(Feature):
	#property vars (may be empty)
	x = 30
	y = 130
	noun = 11
	onMeCheck = 2
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				(global91 say: 11 1 local0 1)
			#end:case
			case 5:
				(global2 setScript: crawl2Cave1)
			#end:case
			case 2:
				(rm390 doVerb: param1 &rest)
			#end:case
			else:
				(super doVerb: param1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class opening(Feature):
	#property vars (may be empty)
	x = 40
	y = 115
	noun = 11
	onMeCheck = 4
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				(global91 say: 11 1 local0 1)
			#end:case
			case 5:
				(global2 setScript: leaveHere)
			#end:case
			case 2:
				(rm390 doVerb: param1 &rest)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class mintHole(Feature):
	#property vars (may be empty)
	x = 290
	y = 130
	noun = 12
	onMeCheck = 2
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				(global91 say: 12 1 local0 1)
			#end:case
			case 2:
				(rm390 doVerb: param1 &rest)
			#end:case
			case 5:
				if (local0 == 11):
					(global2 setScript: crawl2Cave2)
				else:
					(global91 say: 12 5 10 1)
				#endif
			#end:case
			else:
				if (local0 == 11):
					(global91 say: 12 0 11 1)
				else:
					(global91 say: 3 0 10 1)
				#endif
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class westEnd(Feature):
	#property vars (may be empty)
	x = 10
	y = 150
	onMeCheck = 32
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global93 add: self)
		(super init:)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global93 delete: self)
		(super dispose:)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 3):
			(global91 say: 1 0 1 1)
		else:
			(rm390 doVerb: param1 &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class eastEnd(Feature):
	#property vars (may be empty)
	x = 310
	y = 150
	onMeCheck = 64
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global93 add: self)
		(super init:)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global93 delete: self)
		(super dispose:)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 3):
			(global91 say: 1 0 4 1)
		else:
			(rm390 doVerb: param1 &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class pepperBush(View):
	#property vars (may be empty)
	x = 277
	y = 94
	noun = 7
	approachX = 238
	approachY = 127
	view = 390
	loop = 1
	cel = 2
	priority = 2
	signal = 20496
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				if (not (global0 has: 31)):
					(global2 setScript: getLeaf)
				else:
					(global91 say: 7 5 8 1)
				#endif
			#end:case
			case 1:
				(global91 say: 7 1 0 1)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init:)
		(self approachVerbs: 1 5)
	#end:method

#end:class or instance

@SCI.instance
class ledge(View):
	#property vars (may be empty)
	x = 249
	y = 103
	noun = 14
	view = 390
	loop = 1
	priority = 2
	signal = 20496
	
#end:class or instance

@SCI.instance
class rBlock(View):
	#property vars (may be empty)
	x = 265
	y = 103
	noun = 3
	onMeCheck = 0
	view = 390
	priority = 1
	signal = 16400
	
#end:class or instance

@SCI.instance
class myHeadingCode(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			if (param1 > 180):
				param1 = 270
			else:
				param1 = 90
			#endif
		#endif
		if (global0 looper:):
			((global0 looper:) doit: global0 param1 ((argc >= 2) and param2))
		else:
			(global0 heading: param1)
			kernel.DirLoop(global0, param1)
			if ((argc >= 2) and kernel.IsObject(param2)):
				(param2 cue: &rest)
			#endif
		#endif
		return param1
	#end:method

#end:class or instance

@SCI.instance
class caveTalkScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(KQ6Print
					font: global22
					posn: -1 15
					say: 0 3 2 local0 1
					init: self
				)
			#end:case
			case 1:
				(global91 say: 3 2 local0 2 self oneOnly: 0)
			#end:case
			case 2:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class enterScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				cycles = 2
			#end:case
			case 1:
				(global0
					init:
					setStep: 5 2
					view: 390
					show:
					setLoop: -1
					setPri: -1
					setSpeed: 6
					normal: 0
					loop: 5
					cel: 4
					posn: 43 123
					setScale: 0
					actions: egoActions
					ignoreActors: 1
				)
				cycles = 2
			#end:case
			case 2:
				(global0 signal: (| (global0 signal:) 0x1000) setCycle: Beg self)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				(global0
					view: 3902
					posn: 43 123
					setCycle: StopWalk 3903
					setSpeed: (global0 currentSpeed:)
					setHeadingCode: myHeadingCode
				)
				cycles = 2
			#end:case
			case 5:
				(global0 looper: 0)
				if (not proc913_0(96)):
					proc913_1(96)
					(global1 givePoints: 1)
				#endif
				(global91 say: 1 0 9 1 self)
			#end:case
			case 6:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class leaveHere(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: PolyPath 55 130 self)
			#end:case
			case 1:
				(global91 say: 11 5 13 1 self)
			#end:case
			case 2:
				if proc999_5((global0 view:), 392, 393):
					(global0
						view: 391
						loop: 3
						cel: 5
						setSpeed: 6
						setCycle: Beg self
					)
					kernel.Palette(4, 64, 223, 60)
				else:
					(self cue:)
				#endif
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				(global0
					view: 390
					cel: 0
					loop: 6
					normal: 0
					cycleSpeed: 6
					setCycle: End self
				)
			#end:case
			case 5:
				(global0 looper: 0 setHeadingCode: 0 hide:)
				(global2 drawPic: 98 -32758)
				cycles = 6
			#end:case
			case 6:
				(global2 newRoom: 340)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class crawl2Cave2(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: PolyPath 253 151 self)
			#end:case
			case 1:
				(global91 say: 12 5 11 1 self)
			#end:case
			case 2:
				(global0
					normal: 0
					view: 391
					loop: 2
					cel: 5
					setSpeed: 6
					looper: 0
					setCycle: Beg self
				)
				kernel.Palette(4, 64, 223, 60)
			#end:case
			case 3:
				(global0 view: 390 loop: 5 cel: 0 setCycle: End self)
			#end:case
			case 4:
				(global0
					view: 390
					setLoop: 7
					cel: 0
					posn: 247 149
					setCycle: Walk
					setPri: 2
					setMotion: MoveTo 288 135 self
				)
			#end:case
			case 5:
				(global0 setLoop: -1 setPri: -1 hide:)
				((global2 obstacles:) delete: roomPoly)
				(global2 drawPic: 98 10)
				seconds = 2
			#end:case
			case 6:
				local0 = 12
				(global2
					style: 16394
					drawPic: 390 16394
					addObstacle: (roomPoly points: @local18 yourself:)
				)
				(opening dispose:)
				(mintHole dispose:)
				(pepperBush addToPic:)
				(ledge addToPic:)
				(toCave1 init:)
				(rBlock addToPic:)
				cycles = 2
			#end:case
			case 7:
				kernel.Load(143, 390)
				(global0
					show:
					posn: 49 138
					view: 3901
					loop: 7
					cel: 4
					setCycle: Beg self
				)
			#end:case
			case 8:
				(global0
					setSpeed: (global0 currentSpeed:)
					view: 3904
					loop: 0
					posn: 49 138
					setCycle: StopWalk 3905
				)
				cycles = 10
			#end:case
			case 9:
				(global91 say: 1 0 2 1 self)
			#end:case
			case 10:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class crawl2Cave1(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: PolyPath 77 149 self)
			#end:case
			case 1:
				(global91 say: 11 5 12 1 self)
			#end:case
			case 2:
				(global0
					normal: 0
					setSpeed: 6
					view: 3901
					loop: 6
					cel: 0
					posn: 78 147
					setCycle: End self
				)
			#end:case
			case 3:
				(global0
					setLoop: 8
					setCycle: Walk
					setPri: 2
					setMotion: MoveTo 29 133 self
				)
			#end:case
			case 4:
				((global2 obstacles:) delete: roomPoly)
				(global0 setPri: -1 setLoop: -1 hide:)
				(rBlock dispose:)
				(toCave1 dispose:)
				(global2 style: 10 drawPic: 98 -32758)
				seconds = 1
			#end:case
			case 5:
				(global2
					drawPic: 390 100
					addObstacle: (roomPoly points: @local2 yourself:)
				)
				kernel.Palette(4, 64, 223, 60)
				(opening init:)
				(mintHole init:)
				cycles = 2
			#end:case
			case 6:
				(global0 show: view: 390 loop: 6 posn: 270 142 cel: 4)
				ticks = 15
			#end:case
			case 7:
				(global0 setCycle: Beg self)
			#end:case
			case 8:
				cycles = 2
			#end:case
			case 9:
				(global0
					view: 3902
					loop: 1
					setCycle: StopWalk 3903
					setSpeed: (global0 currentSpeed:)
				)
				cycles = 6
			#end:case
			case 10:
				(global91 say: 1 0 3 1 self)
			#end:case
			case 11:
				(global1 handsOn:)
				local0 = 10
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lightItUp(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91 say: 2 20 10 1 self)
			#end:case
			case 1:
				local0 = 11
				(global105 number: 932 setLoop: 1 play:)
				(global0
					view: 391
					loop: ((global0 loop:) + 2)
					cel: 0
					cycleSpeed: 21
					setCycle: End self
				)
				if proc913_0(48):
					(global0 setScript: cyclePalette 0 0)
				#endif
			#end:case
			case 2:
				if (not proc913_0(97)):
					proc913_1(97)
					(global1 givePoints: 2)
				#endif
				(global0
					view: 392
					loop: ((global0 loop:) - 2)
					setSpeed: (global0 currentSpeed:)
					looper: mySmooper
					setCycle: StopWalk 393
				)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getLeaf(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				if (not proc913_1(138)):
					(global1 givePoints: 1)
				#endif
				(global0
					setSpeed: 7
					view: 3901
					loop: 0
					cel: -1
					get: 31
					setCycle: End self
				)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				(global0
					view: 3904
					loop: 0
					setSpeed: (global0 currentSpeed:)
					setCycle: StopWalk 3905
				)
				cycles = 2
			#end:case
			case 3:
				ticks = 20
			#end:case
			case 4:
				(global91 say: 7 5 7 1 self)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoActions(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				return 0
			#end:case
			case 5:
				return 0
			#end:case
			case 2:
				return 0
			#end:case
			case 20:
				if (local0 == 10):
					(global2 setScript: lightItUp)
				else:
					(global91 say: 2 20 local0 1)
				#endif
				return 1
			#end:case
			else:
				(global91 say: 0 0 134 1 0 899)
				return 1
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class cyclePalette(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				kernel.Palette(4, 64, 223, 100)
				ticks = 2
			#end:case
			case 1:
				local1 = 0
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

