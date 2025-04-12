#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 480
import sci_sh
import kernel
import Main
import CryBaby
import n482
import n483
import KQ6Room
import n913
import Print
import Conversation
import Osc
import RandCycle
import PolyPath
import Polygon
import Feature
import LoadMany
import Rev
import Timer
import Sound
import Motion
import User
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm480 = 0,
	hiw = 1,
	brat1 = 2,
	drinkBottle = 3,
	myTeaCup = 4,
	wallFlowerDance = 5,
	myBottle = 6,
	gates = 7,
	rotTomato = 8,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None
local4 = None


@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class rm480(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 480
	walkOffEdge = 1
	autoLoad = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((global12 == 99) and kernel.FileIO(10, r"""g""")):
			proc913_1(77)
			(global0 get: 14)
			(global0 get: 22)
			((global9 at: 33) owner: global11)
			global153 = 4
		#endif
		(global1 handsOn:)
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
						148
						189
						216
						158
						228
						144
						291
						141
						297
						133
						232
						136
						216
						126
						214
						116
						313
						86
						302
						82
						178
						101
						116
						101
						74
						102
						63
						95
						3
						91
						3
						101
						38
						101
						38
						109
						25
						116
						2
						116
						2
						135
						34
						135
						34
						145
						26
						158
						1
						158
						1
						188
						59
						189
					yourself:
				)
				((Polygon new:)
					type: 2
					init: 68 109 40 109 40 101 66 101 72 106
					yourself:
				)
				((Polygon new:)
					type: 2
					init:
						186
						125
						171
						138
						153
						141
						110
						141
						97
						136
						101
						127
						64
						127
						64
						116
						104
						116
						106
						110
						160
						110
						186
						120
					yourself:
				)
				((Polygon new:)
					type: 2
					init: 147 160 84 160 84 144 158 144 163 155
					yourself:
				)
				((Polygon new:)
					type: 2
					init: 16 123 36 112 54 112 62 120 62 130 20 130
					yourself:
				)
				((Polygon new:)
					type: 2
					init: 27 161 37 145 82 145 82 161
					yourself:
				)
		)
		(super init: &rest)
		(global102 number: 480 setLoop: -1 play:)
		(kernel.ScriptID(40, 0) lampMsg: 15)
		(global32
			add:
				sourGrapes
				chokers
				greenMaters
				pathway
				table
				lettuce
				chair
				pillars
				wall
			eachElementDo: #init
		)
		if (global12 == 490):
			(gates cel: 4 signal: 26624 init:)
		else:
			(gates cel: 0 signal: 16384 addToPic:)
		#endif
		(snap init:)
		(flower1 init:)
		(flower2 init:)
		(flower3 init:)
		(flower4 init:)
		if (((global9 at: 49) owner:) == global11):
			(rotTomato init:)
		#endif
		if ((((global9 at: 33) owner:) == global11) and (global153 > 3)):
			(drinkBottle init:)
		#endif
		(brat1 init:)
		(brat2 init:)
		(brat3 init:)
		(brat4 init:)
		if (proc913_0(77) and (((global9 at: 46) owner:) == global11)):
			(myTeaCup init: stopUpd:)
			(glint init: hide:)
			(glintTimer setReal: glint kernel.Random(3, 6))
		#endif
		(global0 actions: fluteVerb init:)
		(global2 setScript: egoEnters)
		if (((global9 at: 18) owner:) == global11):
			(hiw init:)
		#endif
		kernel.Load(143, 480)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (global0 script:):#end:case
			case (global2 script:):#end:case
			case ((global0 edgeHit:) == 3):
				(global2 setScript: egoExits)
			#end:case
			case (global0 inRect: 207 120 312 152):
				(global0 setMotion: 0)
				if ((global0 loop:) == 3):
					(kernel.ScriptID(480, 5) register: 1)
					(global0 setScript: coverThatButtScr)
				else:
					(kernel.ScriptID(480, 5) register: 1)
					(global2 setScript: stepOnSnaps)
				#endif
			#end:case
			case 
				(or
					((global0 onControl: 1) == 4096)
					((global0 onControl: 1) == 8192)
				):
				(kernel.ScriptID(480, 5) register: 1)
				(global0 setScript: hanging 0 3)
			#end:case
			case 
				(and
					(global0 inRect: 194 80 300 100)
					(not (kernel.ScriptID(40, 0) flowerDance:))
				):
				(kernel.ScriptID(480, 5) register: 1)
				(global0 setScript: shyFlowers)
			#end:case
		)
		(super doit:)
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(glintTimer dispose: delete:)
		(roomTimer dispose: delete:)
		(super newRoom: param1)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		proc958_0(0, 481, 482, 483, 939, 969)
		(kernel.ScriptID(40, 0) bottleSucker: 0)
		(super dispose:)
	#end:method

	@classmethod
	def cue(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 3:
				(wallFlowerDance cue:)
			#end:case
			case 0:
				(kernel.ScriptID(40, 0) flowerDance: 0)
				(flower1 setLoop: 0 setCycle: Beg)
				(flower2 setLoop: 1 setCycle: Beg)
				(flower3 setLoop: 2 setCycle: Beg)
				(flower4 setLoop: 3 setCycle: Beg)
				(snap setCycle: Beg)
			#end:case
			else:
				(flower1 setCycle: Beg)
				(flower2 setCycle: Beg)
				(flower3 setCycle: Beg)
				(flower4 setCycle: Beg flower1)
				(snap setCycle: Beg)
			#end:else
		#end:match
	#end:method

	@classmethod
	def notify():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(flower1 view: 4851 stopUpd:)
		(flower2 view: 4851 stopUpd:)
		(flower3 view: 4851 stopUpd:)
		(flower4 view: 4851 stopUpd:)
		kernel.UnLoad(128, 4852)
		(snap setCycle: 0 stopUpd:)
	#end:method

#end:class or instance

@SCI.instance
class hiw(Actor):
	#property vars (may be empty)
	view = 482
	signal = 26624
	cycleSpeed = 12
	illegalBits = 0
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self setLoop: 1 cycleSpeed: 12 posn: 238 70 stopUpd:)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc913_0(159):
			(self
				setLoop: 4
				cel: 5
				posn: 274 57
				cycleSpeed: 6
				setCycle: Beg self
			)
			(global105 number: 483 setLoop: 1 play:)
		else:
			(self setLoop: 1 posn: 283 46 stopUpd:)
		#endif
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				if proc913_0(159):
					(global91 say: 21 1 7 1)
				else:
					(wallFlowerDance register: 1)
					local4 = 1
					proc482_2()
				#endif
			#end:case
			case 5:
				(cond
					case ((global2 script:) == wallFlowerDance):
						proc482_1()
					#end:case
					case proc913_0(159):
						(kernel.ScriptID(40, 0) grabAtHidingHole: 1)
						(global0 setScript: walkToHoleScr)
					#end:case
					else:
						proc913_1(159)
						if (global8 contains: danceMusic):
							(danceMusic fade: 10 10 0 1)
						#endif
						proc482_0()
					#end:else
				)
			#end:case
			case 2:
				if proc913_0(159):
					(global91 say: 21 2 7 0)
				else:
					(global91 say: 21 2 8 0)
				#endif
			#end:case
			else:
				(global91 say: 21 0 0 1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class gates(Prop):
	#property vars (may be empty)
	x = 142
	y = 76
	noun = 15
	approachX = 148
	approachY = 106
	view = 4801
	cycleSpeed = 12
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self approachVerbs: 2 0)
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				(global2 setScript: thruGate)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class snap(Prop):
	#property vars (may be empty)
	x = 277
	y = 129
	noun = 11
	view = 4801
	loop = 1
	priority = 8
	signal = 26640
	cycleSpeed = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self stopUpd:)
		(super init:)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self setCycle: 0 cel: 0)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				(super doVerb: param1 &rest)
			#end:case
			case 5:
				(kernel.ScriptID(480, 5) register: 1)
				(global0 setScript: snappy 0 5)
			#end:case
			case 2:
				(kernel.ScriptID(480, 5) register: 1)
				(global0 setScript: talkToSnaps)
			#end:case
			else:
				(kernel.ScriptID(480, 5) register: 1)
				(global0 setScript: snappy 0 0)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class myBottle(Prop):
	#property vars (may be empty)
	view = 4861
	signal = 16400
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				proc481_0()
			#end:case
			case 43:
				(global91 say: 9 43 17 1)
			#end:case
			else:
				(brat1 doVerb: param1)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self setCycle: RandCycle)
		(kernel.ScriptID(40, 0) babyFed: 1)
		(super init:)
	#end:method

#end:class or instance

@SCI.instance
class drinkBottle(View):
	#property vars (may be empty)
	x = 240
	y = 156
	z = 20
	noun = 8
	approachX = 215
	approachY = 155
	view = 4811
	loop = 4
	priority = 12
	signal = 26640
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self stopUpd: approachVerbs: 0 2 1)
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				(global1 givePoints: 1)
				proc483_0(0)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class myTeaCup(View):
	#property vars (may be empty)
	x = 305
	y = 86
	z = 22
	noun = 22
	view = 4801
	loop = 2
	priority = 2
	signal = 26640
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				(global1 givePoints: 1)
				proc483_0(1)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class rotTomato(View):
	#property vars (may be empty)
	x = 132
	y = 152
	noun = 6
	approachX = 180
	approachY = 160
	view = 4801
	loop = 3
	priority = 12
	signal = 26640
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self approachVerbs: 2 1 0 stopUpd:)
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				if (kernel.ScriptID(40, 0) tomoTalk:):
					(global91 say: 6 1 12 1)
				else:
					(myConv
						add: -1 6 1 11 1
						add: -1 6 1 11 2
						add: -1 6 1 11 3
						init:
					)
				#endif
			#end:case
			case 2:
				if (kernel.ScriptID(40, 0) tomoTalk:):
					(global91 say: 6 2 28 1)
				else:
					(kernel.ScriptID(40, 0) tomoTalk: 1)
					(myConv
						add: -1 6 2 27 1
						add: -1 6 2 27 2
						add: -1 6 2 27 3
						add: -1 6 2 27 4
						add: -1 6 2 27 5
						add: -1 6 2 27 6
						init:
					)
				#endif
			#end:case
			case 5:
				(global0 get: 49)
				proc483_2(self)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lettuce(Feature):
	#property vars (may be empty)
	noun = 10
	onMeCheck = 256
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				if proc913_0(84):
					(global91 say: 10 1 29 0)
				else:
					proc913_1(84)
					(global91 say: 10 1 30 0)
				#endif
			#end:case
			case 5:
				(cond
					case (not (global0 has: 21)):
						proc483_3(self)
					#end:case
					case ((kernel.GetTime(1) - global157) < 150):
						(global91 say: 10 5 32 1)
					#end:case
					case ((kernel.GetTime(1) - global157) < 300):
						proc483_3(self)
					#end:case
					else:
						proc483_3(self)
					#end:else
				)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class chair(Feature):
	#property vars (may be empty)
	noun = 17
	onMeCheck = 16384
	
#end:class or instance

@SCI.instance
class flower1(Prop):
	#property vars (may be empty)
	x = 215
	y = 91
	noun = 5
	approachX = 225
	approachY = 95
	view = 4851
	signal = 30720
	cycleSpeed = 7
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(snap setCycle: 0 stopUpd:)
		(flower1 view: 4852)
		(flower2 view: 4852)
		(flower3 view: 4852)
		(flower4 view: 4852)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self approachVerbs: 5)
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 31:
				if (kernel.ScriptID(40, 0) flowerDance:):
					(global91 say: 5 5 10 1)
				else:
					(global2 setScript: wallFlowerDance)
				#endif
			#end:case
			case 1:
				(super doVerb: param1 &rest)
			#end:case
			case 2:
				(super doVerb: param1 &rest)
			#end:case
			case 5:
				if (kernel.ScriptID(40, 0) flowerDance:):
					(global91 say: 5 5 10 1)
				else:
					(super doVerb: param1 &rest)
				#endif
			#end:case
			else:
				(self setScript: doFlowerInv)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class doFlowerInv(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: PolyPath 180 106 self)
			#end:case
			case 1:
				(global0 setHeading: 90)
				cycles = 8
			#end:case
			case 2:
				(global91 say: 5 0 0 0 self)
			#end:case
			case 3:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class flower2(Prop):
	#property vars (may be empty)
	x = 229
	y = 93
	noun = 5
	approachX = 225
	approachY = 95
	view = 4851
	loop = 1
	signal = 30720
	cycleSpeed = 7
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self approachVerbs: 5)
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(flower1 doVerb: param1 &rest)
	#end:method

#end:class or instance

@SCI.instance
class flower3(Prop):
	#property vars (may be empty)
	x = 252
	y = 84
	noun = 5
	approachX = 225
	approachY = 95
	view = 4851
	loop = 2
	signal = 30720
	cycleSpeed = 7
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self approachVerbs: 5)
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(flower1 doVerb: param1 &rest)
	#end:method

#end:class or instance

@SCI.instance
class flower4(Prop):
	#property vars (may be empty)
	x = 253
	y = 85
	noun = 5
	approachX = 225
	approachY = 95
	view = 4851
	loop = 3
	signal = 30720
	cycleSpeed = 7
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self approachVerbs: 5)
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(flower1 doVerb: param1 &rest)
	#end:method

#end:class or instance

@SCI.instance
class table(Feature):
	#property vars (may be empty)
	x = 250
	y = 150
	noun = 14
	nsTop = 133
	nsLeft = 231
	nsBottom = 147
	nsRight = 274
	
#end:class or instance

@SCI.instance
class chokers(Feature):
	#property vars (may be empty)
	x = 60
	y = 90
	noun = 13
	onMeCheck = 64
	approachX = 173
	approachY = 109
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self approachVerbs: 0)
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				proc483_4(5)
			#end:case
			case 2:
				(kernel.ScriptID(480, 5) register: 1)
				(global0 setScript: talkToVines 0 self)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class sourGrapes(Feature):
	#property vars (may be empty)
	x = 16
	y = 85
	noun = 12
	onMeCheck = 32
	approachX = 16
	approachY = 95
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self approachVerbs: 0)
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 2:
				(kernel.ScriptID(480, 5) register: 1)
				(global0 setScript: talkToVines 0 self)
			#end:case
			case 5:
				proc483_1(self)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class greenMaters(Feature):
	#property vars (may be empty)
	x = 120
	y = 150
	noun = 7
	onMeCheck = 4224
	approachX = 180
	approachY = 160
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self approachVerbs: 2)
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 2:
				(myConv add: -1 7 2 0 1 add: -1 7 2 0 2 init:)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class pathway(Feature):
	#property vars (may be empty)
	noun = 18
	onMeCheck = 2
	
#end:class or instance

@SCI.instance
class pillars(Feature):
	#property vars (may be empty)
	noun = 19
	onMeCheck = 8
	
#end:class or instance

@SCI.instance
class wall(Feature):
	#property vars (may be empty)
	noun = 16
	onMeCheck = 4
	
#end:class or instance

class Brat(Feature):
	#property vars (may be empty)
	bottleNum = 0
	walkToX = 0
	walkToY = 0
	stoopX = 0
	stoopY = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self approachVerbs: 2)
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 14:
				(global91 say: 9 14 0 1 0 480)
			#end:case
			case 5:
				(cond
					case ((kernel.ScriptID(40, 0) bottleSucker:) == (self bottleNum:)):
						(kernel.ScriptID(480, 5) register: 1)
						(global0 setScript: kernel.ScriptID(481, 2) 0 myBottle)
					#end:case
					case ((kernel.ScriptID(40, 0) lampMsg:) == 15):
						(global91 say: 9 5 15 1 0 480)
					#end:case
					else:
						(global91 say: 9 5 18 1 0 480)
					#end:else
				)
			#end:case
			case 43:
				(cond
					case ((kernel.ScriptID(40, 0) bottleSucker:) == (self bottleNum:)):
						(global91 say: 9 43 17 1 0 480)
					#end:case
					case (not proc913_0(77)):
						(global91 say: 9 43 21 1 0 480)
					#end:case
					case ((global161 & 0x0004) or proc913_0(144)):
						(global91 say: 9 43 20 1 0 480)
					#end:case
					case (global161 & 0x0001):
						(global91 say: 9 43 13 1 0 480)
					#end:case
					case (global161 & 0x0002):
						proc481_3((self bottleNum:))
					#end:case
					case ((kernel.ScriptID(40, 0) lampMsg:) == 15):
						(global91 say: 9 43 15 1 0 480)
					#end:case
					else:
						proc481_3((self bottleNum:))
					#end:else
				)
			#end:case
			case 1:
				if ((kernel.ScriptID(40, 0) lampMsg:) == 15):
					(global91 say: 9 1 (kernel.ScriptID(40, 0) lampMsg:) 1 0 480)
				else:
					(global91 say: 9 1 16 1 0 480)
				#endif
			#end:case
			case 2:
				if ((kernel.ScriptID(40, 0) lampMsg:) == 15):
					(global91 say: 9 2 (kernel.ScriptID(40, 0) lampMsg:) 0 0 480)
				else:
					(global91 say: 9 2 16 0 0 480)
				#endif
			#end:case
			case 62:
				(global0 put: 22 480)
				proc481_1((self bottleNum:))
			#end:case
			case 44:
				(cond
					case ((kernel.ScriptID(40, 0) bottleSucker:) == (self bottleNum:)):
						(global91 say: 9 44 17 1 0 480)
					#end:case
					case (not proc913_0(77)):
						(global91 say: 9 44 21 1 0 480)
					#end:case
					else:
						(global91 say: 9 44 22 1 0 480)
					#end:else
				)
			#end:case
			case 24:
				if ((kernel.ScriptID(40, 0) lampMsg:) == 15):
					(global91 say: 9 24 15 1 0 480)
				else:
					(global91 say: 9 24 16 1 0 480)
				#endif
			#end:case
			else:
				if proc999_5(param1, 57, 58, 59, 60, 96):
					if ((kernel.ScriptID(40, 0) bottleSucker:) == (self bottleNum:)):
						(global91 say: 9 56 17 0 0 480)
					else:
						(global91 say: 9 56 (kernel.ScriptID(40, 0) lampMsg:) 0 0 480)
					#endif
				else:
					(kernel.ScriptID(480, 5) register: 1)
					(global0 setScript: inventOnBaby 0 self)
				#endif
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class inventOnBaby(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					setMotion:
						PolyPath
						(register walkToX:)
						(register walkToY:)
						self
				)
			#end:case
			case 1:
				(= temp0
					kernel.GetAngle((global0 x:), (global0 y:), (register x:), (register
						y:
					))
				)
				(global0 setHeading: temp0 self)
			#end:case
			case 2:
				cycles = 6
			#end:case
			case 3:
				if ((kernel.ScriptID(40, 0) lampMsg:) == 15):
					(global91 say: 9 0 (kernel.ScriptID(40, 0) lampMsg:) 0 self 480)
				else:
					(global91 say: 9 0 16 0 self 480)
				#endif
			#end:case
			case 4:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class brat1(Brat):
	#property vars (may be empty)
	x = 58
	y = 152
	noun = 9
	onMeCheck = 512
	approachX = 95
	approachY = 159
	bottleNum = 1
	walkToX = 95
	walkToY = 159
	stoopX = 83
	stoopY = 162
	
#end:class or instance

@SCI.instance
class brat2(Brat):
	#property vars (may be empty)
	x = 10
	y = 147
	noun = 9
	onMeCheck = 16
	approachX = 55
	approachY = 153
	bottleNum = 2
	walkToX = 55
	walkToY = 153
	stoopX = 36
	stoopY = 157
	
#end:class or instance

@SCI.instance
class brat3(Brat):
	#property vars (may be empty)
	x = 39
	y = 122
	noun = 9
	onMeCheck = 1024
	approachX = 81
	approachY = 131
	bottleNum = 3
	walkToX = 81
	walkToY = 131
	stoopX = 63
	stoopY = 135
	
#end:class or instance

@SCI.instance
class brat4(Brat):
	#property vars (may be empty)
	x = 19
	y = 107
	noun = 9
	onMeCheck = 2048
	approachX = 62
	approachY = 116
	bottleNum = 4
	walkToX = 62
	walkToY = 116
	stoopX = 43
	stoopY = 119
	
#end:class or instance

@SCI.instance
class egoEnters(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				if (global12 == 490):
					(global0
						loop: 2
						posn: 139 100
						setMotion: MoveTo 139 107 self
					)
				else:
					(global0
						setLoop: 6
						posn: 51 245
						setMotion: PolyPath 108 185 self
					)
				#endif
			#end:case
			case 1:
				if (global12 == 490):
					(gates cycleSpeed: 4 setCycle: Beg self)
				else:
					(self cue:)
				#endif
			#end:case
			case 2:
				if (global12 == 490):
					(global105 number: 907 setLoop: 1 play:)
					(gates addToPic:)
				#endif
				(global1 handsOn:)
				(global0 reset:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoExits(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: MoveTo ((global0 x:) - 55) 240 self)
			#end:case
			case 1:
				(global1 handsOn:)
				(global2 newRoom: 470)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class thruGate(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: PolyPath 160 106 self)
			#end:case
			case 1:
				(global0 setHeading: 335)
				ticks = 8
			#end:case
			case 2:
				(global0
					normal: 0
					view: 481
					cel: 0
					setLoop: 1
					posn: 142 107
					cycleSpeed: 8
					setCycle: CT 1 1 self
				)
				kernel.UnLoad(128, 900)
			#end:case
			case 3:
				(gates dispose:)
				(global2 drawPic: 480 (15 if global169 else 100))
				if (((global9 at: 49) owner:) == global11):
					(rotTomato addToPic:)
				#endif
				(global105 number: 906 setLoop: 1 play:)
				(global0 setCycle: End self)
				(gates signal: 26624 cycleSpeed: 3 init: setCycle: End)
			#end:case
			case 4:
				(global2 newRoom: 490)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class shyFlowers(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: 0)
				cycles = 10
			#end:case
			case 1:
				(global104 number: 484 setLoop: 1 play: self)
				(flower1 view: 4852 cel: 2 setCycle: CT 6 1)
				(flower2 view: 4852 cel: 2 setCycle: CT 6 1)
				(flower3 view: 4852 cel: 2 setCycle: CT 6 1)
				(flower4 view: 4852 cel: 2 setCycle: CT 6 1)
			#end:case
			case 2:
				proc913_4(global0, snap)
				(snap setCycle: Fwd)
				(global105 number: 482 setLoop: 2 play: self)
			#end:case
			case 3:
				(snap setCycle: 0 cel: 0 stopUpd:)
				cycles = 4
			#end:case
			case 4:
				if ((kernel.ScriptID(40, 0) grabAtHidingHole:) == 1):
					(kernel.ScriptID(40, 0) grabAtHidingHole: 0)
					(global91 say: 21 5 9 1 self)
				else:
					(global91 say: 5 3 0 1 self)
				#endif
			#end:case
			case 5:
				(global0 setMotion: PolyPath 197 116 self)
				(flower1 view: 4851 stopUpd:)
				(flower2 view: 4851 stopUpd:)
				(flower3 view: 4851 stopUpd:)
				(flower4 view: 4851 stopUpd:)
				kernel.UnLoad(128, 4852)
				(snap setCycle: Beg)
			#end:case
			case 6:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class hanging(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: 0)
				cycles = 2
			#end:case
			case 1:
				proc483_4(3)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class stepOnSnaps(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: 0)
				proc913_4(global0, snap)
				cycles = 10
			#end:case
			case 1:
				(global105 number: 482 setLoop: 1 play: self)
				(snap setCycle: Fwd)
			#end:case
			case 2:
				(snap setCycle: 0 cel: 0 stopUpd:)
				cycles = 4
			#end:case
			case 3:
				(global91 say: 11 3 0 1 self)
			#end:case
			case 4:
				(global0
					setLoop: (global0 cel:)
					setCycle: Rev
					setMotion: PolyPath ((global0 x:) - 5) (global0 y:) self
				)
			#end:case
			case 5:
				(global0 setCycle: Walk setLoop: -1)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class coverThatButtScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: 0)
				(global105 number: 482 setLoop: 1 play: self)
				(snap setCycle: Fwd)
				ticks = 12
			#end:case
			case 1:
				(global0
					normal: 0
					setSpeed: 6
					view: 483
					loop: 0
					cel: 0
					posn: ((global0 x:) - 13) ((global0 y:) + 2)
					setCycle: End self
				)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				(global0 reset: 0 posn: ((global0 x:) - 13) ((global0 y:) - 6))
				cycles = 2
			#end:case
			case 4:
				(snap setCycle: 0 cel: 0 stopUpd:)
				cycles = 4
			#end:case
			case 5:
				(global91 say: 11 3 0 1 self)
			#end:case
			case 6:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class talkToVines(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				if 
					(or
						((global0 distanceTo: register) > 130)
						((global0 y:) > 115)
					)
					(global0 setMotion: PolyPath 173 109 self)
				else:
					(self cue:)
				#endif
			#end:case
			case 1:
				proc913_4(global0, register)
				cycles = 8
			#end:case
			case 2:
				match register
					case chokers:
						if (kernel.ScriptID(40, 0) vineTalk:):
							(global91 say: 13 2 26 1 self)
						else:
							(kernel.ScriptID(40, 0) vineTalk: 1)
							(myConv
								add: -1 13 2 25 1
								add: -1 13 2 25 2
								add: -1 13 2 25 3
								add: -1 13 2 25 4
								add: -1 13 2 25 5
								add: -1 13 2 25 6
								add: -1 13 2 25 7
								add: -1 13 2 25 8
								init: self
							)
						#endif
					#end:case
					else:
						if (kernel.ScriptID(40, 0) grapeTalk:):
							(global91 say: 12 2 24 1 self)
						else:
							(myConv
								add: -1 12 2 23 1
								add: -1 12 2 23 2
								add: -1 12 2 23 3
								add: -1 12 2 23 4
								add: -1 12 2 23 5
								add: -1 12 2 23 6
								add: -1 12 2 23 7
								add: -1 12 2 23 8
								init: self
							)
						#endif
					#end:else
				#end:match
			#end:case
			case 3:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class snappy(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				if (register == 5):
					(global91 say: 11 5 0 1 self)
				else:
					(self cue:)
				#endif
			#end:case
			case 1:
				(global0 setMotion: PolyPath 220 130 self)
			#end:case
			case 2:
				(global0 setHeading: 90)
				cycles = 6
			#end:case
			case 3:
				if (register == 5):
					(self cue:)
				else:
					(global91 say: 11 0 0 1 self)
				#endif
			#end:case
			case 4:
				(global105 number: 482 setLoop: 1 play: self)
				(snap setCycle: Fwd)
			#end:case
			case 5:
				(snap setCycle: 0 cel: 0 stopUpd:)
				cycles = 4
			#end:case
			case 6:
				if (register == 5):
					(global91 say: 11 5 0 2 self)
				else:
					(global91 say: 11 0 0 2 self)
				#endif
			#end:case
			case 7:
				(global0
					setLoop: (global0 cel:)
					setCycle: Rev
					setMotion: PolyPath ((global0 x:) - 15) (global0 y:) self
				)
			#end:case
			case 8:
				(global0 setCycle: Walk setLoop: -1)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class danceMusic(Sound):
	#property vars (may be empty)
	number = 486
	
#end:class or instance

@SCI.instance
class pauseForMusic(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				seconds = 5
			#end:case
			case 1:
				(global102 number: 480 setLoop: -1 play:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class fluteVerb(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 31:
				(global2 setScript: wallFlowerDance)
				return 1
			#end:case
			else:
				return 0
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class glint(Prop):
	#property vars (may be empty)
	x = 303
	y = 63
	view = 902
	signal = 26624
	cycleSpeed = 1
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super cue:)
		match local2.post('++')
			case 1:
				if (not (global5 contains: myTeaCup)):
					(self dispose:)
				else:
					(self show: cel: 0 setLoop: kernel.Random(0, 1) setCycle: End self)
				#endif
			#end:case
			case 2:
				(self hide:)
				local2 = 0
				(glintTimer setReal: self kernel.Random(3, 6))
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class glintTimer(Timer):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class roomTimer(Timer):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class wallFlowerDance(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		local4 = 0
		if (not proc913_0(117)):
			proc913_1(117)
			(global1 givePoints: 2)
		#endif
		(global93 addToFront: self)
		(global73 addToFront: self)
		(global72 addToFront: self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global93 delete: self)
		(global73 delete: self)
		(global72 delete: self)
		if local3:
			proc481_7()
			(myBottle setCycle: RandCycle)
		#endif
		(global102 number: 480 setLoop: -1 play:)
		(danceMusic prevSignal: 0)
		(global2 cue: 0)
		(super dispose:)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc999_5((param1 type:), 1, 2, 4, 256):
			(cond
				case (state == 9):
					if global25:
						(global25 dispose:)
					#endif
					(self cue:)
					(param1 localize:)
					(param1 claimed: 1)
				#end:case
				case 
					(and
						(state == 10)
						(User controls:)
						((param1 type:) & 0x1000)
					):
					(param1 claimed: 1)
					(self cue:)
				#end:case
				else:
					(param1 claimed: 0)
				#end:else
			)
		#endif
		(param1 claimed:)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case ((global0 edgeHit:) == 3):
				(global2 setScript: egoExits)
			#end:case
			case (register and (state == 10)):
				(self cue:)
			#end:case
			case ((state > 6) and (state < 11) and ((danceMusic prevSignal:) == -1)):
				(danceMusic prevSignal: 0)
				state = 10
				(global1 handsOn:)
				(self cue:)
			#end:case
			case ((danceMusic prevSignal:) == 20):
				(self cue:)
				(danceMusic prevSignal: 0)
				local1 = 7
				(flower1 cycleSpeed: ((flower1 cycleSpeed:) - 1))
				(flower2 cycleSpeed: ((flower2 cycleSpeed:) - 1))
				(flower3 cycleSpeed: ((flower3 cycleSpeed:) - 1))
				(flower4 cycleSpeed: ((flower4 cycleSpeed:) - 1))
				(snap cycleSpeed: ((snap cycleSpeed:) - 1))
			#end:case
			case 
				(and
					((danceMusic prevSignal:) == 10)
					(state <= 11)
					(state >= 6)
				):
				(danceMusic prevSignal: 0)
				(snap setCycle: Osc local1 snap)
			#end:case
		)
		(super doit:)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				local1 = 9
				(global0
					ignoreActors: 1
					illegalBits: 0
					setMotion: PolyPath 190 110 self
				)
			#end:case
			case 1:
				if (kernel.ScriptID(40, 0) bottleSucker:):
					proc481_6()
					(myBottle setCycle: 0)
					local3 = 1
				#endif
				(global0 setHeading: 45)
				cycles = 4
			#end:case
			case 2:
				(global91 say: 5 31 0 1 self)
			#end:case
			case 3:
				(global91 say: 5 31 0 2 self)
			#end:case
			case 4:
				register = 0
				if 
					(and
						(global5 contains: hiw)
						proc913_0(159)
						((hiw x:) != 283)
						((hiw y:) != 46)
					)
					(hiw setLoop: 1 setCycle: Walk setMotion: MoveTo 238 70)
				#endif
				(kernel.ScriptID(40, 0) flowerDance: 1)
				(flower1 view: 4852 cel: 2 setCycle: Fwd)
				(flower2 view: 4852 cel: 2 setCycle: Fwd)
				(flower3 view: 4852 cel: 6 setCycle: Fwd)
				(flower4 view: 4852 cel: 6 setCycle: Fwd)
				if 
					(and
						(((global9 at: 18) owner:) == global11)
						proc913_0(159)
					)
					(global105 number: 483 setLoop: 1 play:)
					(hiw setLoop: 5 setCycle: Walk setMotion: MoveTo 259 49)
				#endif
				ticks = 6
			#end:case
			case 5:
				if ((hiw loop:) == 5):
					(global105 stop:)
					(hiw setLoop: 1)
				#endif
				(global0
					view: 920
					setLoop: 0
					cel: 0
					posn: (global0 x:) ((global0 y:) + 2)
					normal: 0
					cycleSpeed: 6
				)
				ticks = 6
			#end:case
			case 6:
				(global102 stop:)
				(danceMusic number: 486 setLoop: 1 flags: 0 play:)
				(global0 setCycle: Fwd)
			#end:case
			case 7:
				(global0 setCycle: End self)
			#end:case
			case 8:
				(global0 reset: 0 posn: (global0 x:) ((global0 y:) - 2))
				cycles = 6
			#end:case
			case 9:
				(danceMusic flags: 1)
				if (global90 & 0x0002):
					(global91 say: 5 31 0 3 self)
				else:
					(Print
						font: 4
						addText: 5 31 0 3
						posn: 10 6
						width: 289
						init:
					)
					ticks = 12
				#endif
			#end:case
			case 10:
				(global1 handsOn:)
			#end:case
			case 11:
				if global25:
					(global25 dispose:)
				#endif
				(danceMusic fade:)
				seconds = 3
			#end:case
			case 12:
				(kernel.ScriptID(40, 0) flowerDance: 0)
				if ((global5 contains: hiw) and proc913_0(159) and (not local4)):
					(hiw setLoop: 1 setCycle: Walk setMotion: MoveTo 238 70)
				#endif
				(self dispose:)
				(flower1 view: 4851 stopUpd:)
				(flower2 view: 4851 stopUpd:)
				(flower3 view: 4851 stopUpd:)
				(flower4 view: 4851 stopUpd:)
				(snap cel: 0 stopUpd:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walkToHoleScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				if (((hiw x:) != 238) and ((hiw y:) != 70)):
					(hiw setLoop: 5 setCycle: Walk setMotion: MoveTo 238 70 hiw)
				#endif
				(global0 setMotion: PolyPath 242 93 self)
			#end:case
			case 1:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class talkToSnaps(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: PolyPath 198 130 self)
			#end:case
			case 1:
				(global0 setHeading: 90)
				cycles = 8
			#end:case
			case 2:
				(global91 say: 11 2 0 1 self)
			#end:case
			case 3:
				(global105 number: 482 setLoop: 1 play: self)
				(snap setCycle: Fwd)
			#end:case
			case 4:
				(snap setCycle: 0 cel: 0 stopUpd:)
				cycles = 3
			#end:case
			case 5:
				(global91 say: 11 2 0 2 self)
			#end:case
			case 6:
				(global1 handsOn:)
				(snap setCycle: 0 cel: 0 stopUpd:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

