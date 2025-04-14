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
		if ((global12 == 99) and kernel.FileIO(10, r"""g""")):
			proc913_1(77)
			global0._send('get:', 14)
			global0._send('get:', 22)
			global9._send('at:', 33)._send('owner:', global11)
			global153 = 4
		#endif
		global1._send('handsOn:')
		global2._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 0, 189, 0, 0, 319, 0, 319, 189, 148, 189, 216, 158, 228, 144, 291, 141, 297, 133, 232, 136, 216, 126, 214, 116, 313, 86, 302, 82, 178, 101, 116, 101, 74, 102, 63, 95, 3, 91, 3, 101, 38, 101, 38, 109, 25, 116, 2, 116, 2, 135, 34, 135, 34, 145, 26, 158, 1, 158, 1, 188, 59, 189,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 68, 109, 40, 109, 40, 101, 66, 101, 72, 106,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 186, 125, 171, 138, 153, 141, 110, 141, 97, 136, 101, 127, 64, 127, 64, 116, 104, 116, 106, 110, 160, 110, 186, 120,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 147, 160, 84, 160, 84, 144, 158, 144, 163, 155,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 16, 123, 36, 112, 54, 112, 62, 120, 62, 130, 20, 130,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 27, 161, 37, 145, 82, 145, 82, 161,
					'yourself:'
				)
		)
		super._send('init:', &rest)
		global102._send('number:', 480, 'setLoop:', -1, 'play:')
		kernel.ScriptID(40, 0)._send('lampMsg:', 15)
		global32._send(
			'add:', sourGrapes, chokers, greenMaters, pathway, table, lettuce, chair, pillars, wall,
			'eachElementDo:', #init
		)
		if (global12 == 490):
			gates._send('cel:', 4, 'signal:', 26624, 'init:')
		else:
			gates._send('cel:', 0, 'signal:', 16384, 'addToPic:')
		#endif
		snap._send('init:')
		flower1._send('init:')
		flower2._send('init:')
		flower3._send('init:')
		flower4._send('init:')
		if (global9._send('at:', 49)._send('owner:') == global11):
			rotTomato._send('init:')
		#endif
		if ((global9._send('at:', 33)._send('owner:') == global11) and (global153 > 3)):
			drinkBottle._send('init:')
		#endif
		brat1._send('init:')
		brat2._send('init:')
		brat3._send('init:')
		brat4._send('init:')
		if (proc913_0(77) and (global9._send('at:', 46)._send('owner:') == global11)):
			myTeaCup._send('init:', 'stopUpd:')
			glint._send('init:', 'hide:')
			glintTimer._send('setReal:', glint, kernel.Random(3, 6))
		#endif
		global0._send('actions:', fluteVerb, 'init:')
		global2._send('setScript:', egoEnters)
		if (global9._send('at:', 18)._send('owner:') == global11):
			hiw._send('init:')
		#endif
		kernel.Load(143, 480)
	#end:method

	@classmethod
	def doit():
		(cond
			case global0._send('script:'):#end:case
			case global2._send('script:'):#end:case
			case (global0._send('edgeHit:') == 3):
				global2._send('setScript:', egoExits)
			#end:case
			case global0._send('inRect:', 207, 120, 312, 152):
				global0._send('setMotion:', 0)
				if (global0._send('loop:') == 3):
					kernel.ScriptID(480, 5)._send('register:', 1)
					global0._send('setScript:', coverThatButtScr)
				else:
					kernel.ScriptID(480, 5)._send('register:', 1)
					global2._send('setScript:', stepOnSnaps)
				#endif
			#end:case
			case 
				(or
					(global0._send('onControl:', 1) == 4096)
					(global0._send('onControl:', 1) == 8192)
				):
				kernel.ScriptID(480, 5)._send('register:', 1)
				global0._send('setScript:', hanging, 0, 3)
			#end:case
			case 
				(and
					global0._send('inRect:', 194, 80, 300, 100)
					(not kernel.ScriptID(40, 0)._send('flowerDance:'))
				):
				kernel.ScriptID(480, 5)._send('register:', 1)
				global0._send('setScript:', shyFlowers)
			#end:case
		)
		super._send('doit:')
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		glintTimer._send('dispose:', 'delete:')
		roomTimer._send('dispose:', 'delete:')
		super._send('newRoom:', param1)
	#end:method

	@classmethod
	def dispose():
		proc958_0(0, 481, 482, 483, 939, 969)
		kernel.ScriptID(40, 0)._send('bottleSucker:', 0)
		super._send('dispose:')
	#end:method

	@classmethod
	def cue(param1 = None, *rest):
		match param1
			case 3:
				wallFlowerDance._send('cue:')
			#end:case
			case 0:
				kernel.ScriptID(40, 0)._send('flowerDance:', 0)
				flower1._send('setLoop:', 0, 'setCycle:', Beg)
				flower2._send('setLoop:', 1, 'setCycle:', Beg)
				flower3._send('setLoop:', 2, 'setCycle:', Beg)
				flower4._send('setLoop:', 3, 'setCycle:', Beg)
				snap._send('setCycle:', Beg)
			#end:case
			else:
				flower1._send('setCycle:', Beg)
				flower2._send('setCycle:', Beg)
				flower3._send('setCycle:', Beg)
				flower4._send('setCycle:', Beg, flower1)
				snap._send('setCycle:', Beg)
			#end:else
		#end:match
	#end:method

	@classmethod
	def notify():
		flower1._send('view:', 4851, 'stopUpd:')
		flower2._send('view:', 4851, 'stopUpd:')
		flower3._send('view:', 4851, 'stopUpd:')
		flower4._send('view:', 4851, 'stopUpd:')
		kernel.UnLoad(128, 4852)
		snap._send('setCycle:', 0, 'stopUpd:')
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
		self._send('setLoop:', 1, 'cycleSpeed:', 12, 'posn:', 238, 70, 'stopUpd:')
	#end:method

	@classmethod
	def init():
		if proc913_0(159):
			self._send(
				'setLoop:', 4,
				'cel:', 5,
				'posn:', 274, 57,
				'cycleSpeed:', 6,
				'setCycle:', Beg, self
			)
			global105._send('number:', 483, 'setLoop:', 1, 'play:')
		else:
			self._send('setLoop:', 1, 'posn:', 283, 46, 'stopUpd:')
		#endif
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				if proc913_0(159):
					global91._send('say:', 21, 1, 7, 1)
				else:
					wallFlowerDance._send('register:', 1)
					local4 = 1
					proc482_2()
				#endif
			#end:case
			case 5:
				(cond
					case (global2._send('script:') == wallFlowerDance):
						proc482_1()
					#end:case
					case proc913_0(159):
						kernel.ScriptID(40, 0)._send('grabAtHidingHole:', 1)
						global0._send('setScript:', walkToHoleScr)
					#end:case
					else:
						proc913_1(159)
						if global8._send('contains:', danceMusic):
							danceMusic._send('fade:', 10, 10, 0, 1)
						#endif
						proc482_0()
					#end:else
				)
			#end:case
			case 2:
				if proc913_0(159):
					global91._send('say:', 21, 2, 7, 0)
				else:
					global91._send('say:', 21, 2, 8, 0)
				#endif
			#end:case
			else:
				global91._send('say:', 21, 0, 0, 1)
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
		self._send('approachVerbs:', 2, 0)
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				global2._send('setScript:', thruGate)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
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
		self._send('stopUpd:')
		super._send('init:')
	#end:method

	@classmethod
	def cue():
		self._send('setCycle:', 0, 'cel:', 0)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				super._send('doVerb:', param1, &rest)
			#end:case
			case 5:
				kernel.ScriptID(480, 5)._send('register:', 1)
				global0._send('setScript:', snappy, 0, 5)
			#end:case
			case 2:
				kernel.ScriptID(480, 5)._send('register:', 1)
				global0._send('setScript:', talkToSnaps)
			#end:case
			else:
				kernel.ScriptID(480, 5)._send('register:', 1)
				global0._send('setScript:', snappy, 0, 0)
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
		match param1
			case 5:
				proc481_0()
			#end:case
			case 43:
				global91._send('say:', 9, 43, 17, 1)
			#end:case
			else:
				brat1._send('doVerb:', param1)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		self._send('setCycle:', RandCycle)
		kernel.ScriptID(40, 0)._send('babyFed:', 1)
		super._send('init:')
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
		self._send('stopUpd:', 'approachVerbs:', 0, 2, 1)
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				global1._send('givePoints:', 1)
				proc483_0(0)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
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
		match param1
			case 5:
				global1._send('givePoints:', 1)
				proc483_0(1)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
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
		self._send('approachVerbs:', 2, 1, 0, 'stopUpd:')
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				if kernel.ScriptID(40, 0)._send('tomoTalk:'):
					global91._send('say:', 6, 1, 12, 1)
				else:
					myConv._send(
						'add:', -1, 6, 1, 11, 1,
						'add:', -1, 6, 1, 11, 2,
						'add:', -1, 6, 1, 11, 3,
						'init:'
					)
				#endif
			#end:case
			case 2:
				if kernel.ScriptID(40, 0)._send('tomoTalk:'):
					global91._send('say:', 6, 2, 28, 1)
				else:
					kernel.ScriptID(40, 0)._send('tomoTalk:', 1)
					myConv._send(
						'add:', -1, 6, 2, 27, 1,
						'add:', -1, 6, 2, 27, 2,
						'add:', -1, 6, 2, 27, 3,
						'add:', -1, 6, 2, 27, 4,
						'add:', -1, 6, 2, 27, 5,
						'add:', -1, 6, 2, 27, 6,
						'init:'
					)
				#endif
			#end:case
			case 5:
				global0._send('get:', 49)
				proc483_2(self)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
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
		match param1
			case 1:
				if proc913_0(84):
					global91._send('say:', 10, 1, 29, 0)
				else:
					proc913_1(84)
					global91._send('say:', 10, 1, 30, 0)
				#endif
			#end:case
			case 5:
				(cond
					case (not global0._send('has:', 21)):
						proc483_3(self)
					#end:case
					case ((kernel.GetTime(1) - global157) < 150):
						global91._send('say:', 10, 5, 32, 1)
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
				super._send('doVerb:', param1, &rest)
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
		snap._send('setCycle:', 0, 'stopUpd:')
		flower1._send('view:', 4852)
		flower2._send('view:', 4852)
		flower3._send('view:', 4852)
		flower4._send('view:', 4852)
	#end:method

	@classmethod
	def init():
		self._send('approachVerbs:', 5)
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 31:
				if kernel.ScriptID(40, 0)._send('flowerDance:'):
					global91._send('say:', 5, 5, 10, 1)
				else:
					global2._send('setScript:', wallFlowerDance)
				#endif
			#end:case
			case 1:
				super._send('doVerb:', param1, &rest)
			#end:case
			case 2:
				super._send('doVerb:', param1, &rest)
			#end:case
			case 5:
				if kernel.ScriptID(40, 0)._send('flowerDance:'):
					global91._send('say:', 5, 5, 10, 1)
				else:
					super._send('doVerb:', param1, &rest)
				#endif
			#end:case
			else:
				self._send('setScript:', doFlowerInv)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class doFlowerInv(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 180, 106, self)
			#end:case
			case 1:
				global0._send('setHeading:', 90)
				cycles = 8
			#end:case
			case 2:
				global91._send('say:', 5, 0, 0, 0, self)
			#end:case
			case 3:
				global1._send('handsOn:')
				self._send('dispose:')
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
		self._send('approachVerbs:', 5)
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		flower1._send('doVerb:', param1, &rest)
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
		self._send('approachVerbs:', 5)
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		flower1._send('doVerb:', param1, &rest)
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
		self._send('approachVerbs:', 5)
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		flower1._send('doVerb:', param1, &rest)
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
		self._send('approachVerbs:', 0)
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				proc483_4(5)
			#end:case
			case 2:
				kernel.ScriptID(480, 5)._send('register:', 1)
				global0._send('setScript:', talkToVines, 0, self)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
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
		self._send('approachVerbs:', 0)
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 2:
				kernel.ScriptID(480, 5)._send('register:', 1)
				global0._send('setScript:', talkToVines, 0, self)
			#end:case
			case 5:
				proc483_1(self)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
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
		self._send('approachVerbs:', 2)
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 2:
				myConv._send('add:', -1, 7, 2, 0, 1, 'add:', -1, 7, 2, 0, 2, 'init:')
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
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
		self._send('approachVerbs:', 2)
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 14:
				global91._send('say:', 9, 14, 0, 1, 0, 480)
			#end:case
			case 5:
				(cond
					case (kernel.ScriptID(40, 0)._send('bottleSucker:') == self._send('bottleNum:')):
						kernel.ScriptID(480, 5)._send('register:', 1)
						global0._send('setScript:', kernel.ScriptID(481, 2), 0, myBottle)
					#end:case
					case (kernel.ScriptID(40, 0)._send('lampMsg:') == 15):
						global91._send('say:', 9, 5, 15, 1, 0, 480)
					#end:case
					else:
						global91._send('say:', 9, 5, 18, 1, 0, 480)
					#end:else
				)
			#end:case
			case 43:
				(cond
					case (kernel.ScriptID(40, 0)._send('bottleSucker:') == self._send('bottleNum:')):
						global91._send('say:', 9, 43, 17, 1, 0, 480)
					#end:case
					case (not proc913_0(77)):
						global91._send('say:', 9, 43, 21, 1, 0, 480)
					#end:case
					case ((global161 & 0x0004) or proc913_0(144)):
						global91._send('say:', 9, 43, 20, 1, 0, 480)
					#end:case
					case (global161 & 0x0001):
						global91._send('say:', 9, 43, 13, 1, 0, 480)
					#end:case
					case (global161 & 0x0002):
						proc481_3(self._send('bottleNum:'))
					#end:case
					case (kernel.ScriptID(40, 0)._send('lampMsg:') == 15):
						global91._send('say:', 9, 43, 15, 1, 0, 480)
					#end:case
					else:
						proc481_3(self._send('bottleNum:'))
					#end:else
				)
			#end:case
			case 1:
				if (kernel.ScriptID(40, 0)._send('lampMsg:') == 15):
					global91._send('say:', 9, 1, kernel.ScriptID(40, 0)._send('lampMsg:'), 1, 0, 480)
				else:
					global91._send('say:', 9, 1, 16, 1, 0, 480)
				#endif
			#end:case
			case 2:
				if (kernel.ScriptID(40, 0)._send('lampMsg:') == 15):
					global91._send('say:', 9, 2, kernel.ScriptID(40, 0)._send('lampMsg:'), 0, 0, 480)
				else:
					global91._send('say:', 9, 2, 16, 0, 0, 480)
				#endif
			#end:case
			case 62:
				global0._send('put:', 22, 480)
				proc481_1(self._send('bottleNum:'))
			#end:case
			case 44:
				(cond
					case (kernel.ScriptID(40, 0)._send('bottleSucker:') == self._send('bottleNum:')):
						global91._send('say:', 9, 44, 17, 1, 0, 480)
					#end:case
					case (not proc913_0(77)):
						global91._send('say:', 9, 44, 21, 1, 0, 480)
					#end:case
					else:
						global91._send('say:', 9, 44, 22, 1, 0, 480)
					#end:else
				)
			#end:case
			case 24:
				if (kernel.ScriptID(40, 0)._send('lampMsg:') == 15):
					global91._send('say:', 9, 24, 15, 1, 0, 480)
				else:
					global91._send('say:', 9, 24, 16, 1, 0, 480)
				#endif
			#end:case
			else:
				if proc999_5(param1, 57, 58, 59, 60, 96):
					if (kernel.ScriptID(40, 0)._send('bottleSucker:') == self._send('bottleNum:')):
						global91._send('say:', 9, 56, 17, 0, 0, 480)
					else:
						global91._send('say:', 9, 56, kernel.ScriptID(40, 0)._send('lampMsg:'), 0, 0, 480)
					#endif
				else:
					kernel.ScriptID(480, 5)._send('register:', 1)
					global0._send('setScript:', inventOnBaby, 0, self)
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
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send(
					'setMotion:', PolyPath, register._send('walkToX:'), register._send(
							'walkToY:'
						), self
				)
			#end:case
			case 1:
				(= temp0
					kernel.GetAngle(global0._send('x:'), global0._send('y:'), register._send(
						'x:'
					), register._send('y:'))
				)
				global0._send('setHeading:', temp0, self)
			#end:case
			case 2:
				cycles = 6
			#end:case
			case 3:
				if (kernel.ScriptID(40, 0)._send('lampMsg:') == 15):
					global91._send('say:', 9, 0, kernel.ScriptID(40, 0)._send('lampMsg:'), 0, self, 480)
				else:
					global91._send('say:', 9, 0, 16, 0, self, 480)
				#endif
			#end:case
			case 4:
				global1._send('handsOn:')
				self._send('dispose:')
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
		match state = param1
			case 0:
				global1._send('handsOff:')
				if (global12 == 490):
					global0._send(
						'loop:', 2,
						'posn:', 139, 100,
						'setMotion:', MoveTo, 139, 107, self
					)
				else:
					global0._send(
						'setLoop:', 6,
						'posn:', 51, 245,
						'setMotion:', PolyPath, 108, 185, self
					)
				#endif
			#end:case
			case 1:
				if (global12 == 490):
					gates._send('cycleSpeed:', 4, 'setCycle:', Beg, self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 2:
				if (global12 == 490):
					global105._send('number:', 907, 'setLoop:', 1, 'play:')
					gates._send('addToPic:')
				#endif
				global1._send('handsOn:')
				global0._send('reset:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoExits(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', MoveTo, (global0._send('x:') - 55), 240, self)
			#end:case
			case 1:
				global1._send('handsOn:')
				global2._send('newRoom:', 470)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class thruGate(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 160, 106, self)
			#end:case
			case 1:
				global0._send('setHeading:', 335)
				ticks = 8
			#end:case
			case 2:
				global0._send(
					'normal:', 0,
					'view:', 481,
					'cel:', 0,
					'setLoop:', 1,
					'posn:', 142, 107,
					'cycleSpeed:', 8,
					'setCycle:', CT, 1, 1, self
				)
				kernel.UnLoad(128, 900)
			#end:case
			case 3:
				gates._send('dispose:')
				global2._send('drawPic:', 480, (15 if global169 else 100))
				if (global9._send('at:', 49)._send('owner:') == global11):
					rotTomato._send('addToPic:')
				#endif
				global105._send('number:', 906, 'setLoop:', 1, 'play:')
				global0._send('setCycle:', End, self)
				gates._send('signal:', 26624, 'cycleSpeed:', 3, 'init:', 'setCycle:', End)
			#end:case
			case 4:
				global2._send('newRoom:', 490)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class shyFlowers(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', 0)
				cycles = 10
			#end:case
			case 1:
				global104._send('number:', 484, 'setLoop:', 1, 'play:', self)
				flower1._send('view:', 4852, 'cel:', 2, 'setCycle:', CT, 6, 1)
				flower2._send('view:', 4852, 'cel:', 2, 'setCycle:', CT, 6, 1)
				flower3._send('view:', 4852, 'cel:', 2, 'setCycle:', CT, 6, 1)
				flower4._send('view:', 4852, 'cel:', 2, 'setCycle:', CT, 6, 1)
			#end:case
			case 2:
				proc913_4(global0, snap)
				snap._send('setCycle:', Fwd)
				global105._send('number:', 482, 'setLoop:', 2, 'play:', self)
			#end:case
			case 3:
				snap._send('setCycle:', 0, 'cel:', 0, 'stopUpd:')
				cycles = 4
			#end:case
			case 4:
				if (kernel.ScriptID(40, 0)._send('grabAtHidingHole:') == 1):
					kernel.ScriptID(40, 0)._send('grabAtHidingHole:', 0)
					global91._send('say:', 21, 5, 9, 1, self)
				else:
					global91._send('say:', 5, 3, 0, 1, self)
				#endif
			#end:case
			case 5:
				global0._send('setMotion:', PolyPath, 197, 116, self)
				flower1._send('view:', 4851, 'stopUpd:')
				flower2._send('view:', 4851, 'stopUpd:')
				flower3._send('view:', 4851, 'stopUpd:')
				flower4._send('view:', 4851, 'stopUpd:')
				kernel.UnLoad(128, 4852)
				snap._send('setCycle:', Beg)
			#end:case
			case 6:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class hanging(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', 0)
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
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', 0)
				proc913_4(global0, snap)
				cycles = 10
			#end:case
			case 1:
				global105._send('number:', 482, 'setLoop:', 1, 'play:', self)
				snap._send('setCycle:', Fwd)
			#end:case
			case 2:
				snap._send('setCycle:', 0, 'cel:', 0, 'stopUpd:')
				cycles = 4
			#end:case
			case 3:
				global91._send('say:', 11, 3, 0, 1, self)
			#end:case
			case 4:
				global0._send(
					'setLoop:', global0._send('cel:'),
					'setCycle:', Rev,
					'setMotion:', PolyPath, (global0._send('x:') - 5), global0._send('y:'), self
				)
			#end:case
			case 5:
				global0._send('setCycle:', Walk, 'setLoop:', -1)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class coverThatButtScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', 0)
				global105._send('number:', 482, 'setLoop:', 1, 'play:', self)
				snap._send('setCycle:', Fwd)
				ticks = 12
			#end:case
			case 1:
				global0._send(
					'normal:', 0,
					'setSpeed:', 6,
					'view:', 483,
					'loop:', 0,
					'cel:', 0,
					'posn:', (global0._send('x:') - 13), (global0._send('y:') + 2),
					'setCycle:', End, self
				)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				global0._send('reset:', 0, 'posn:', (global0._send('x:') - 13), (global0._send('y:') - 6))
				cycles = 2
			#end:case
			case 4:
				snap._send('setCycle:', 0, 'cel:', 0, 'stopUpd:')
				cycles = 4
			#end:case
			case 5:
				global91._send('say:', 11, 3, 0, 1, self)
			#end:case
			case 6:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class talkToVines(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				if 
					(or
						(global0._send('distanceTo:', register) > 130)
						(global0._send('y:') > 115)
					)
					global0._send('setMotion:', PolyPath, 173, 109, self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 1:
				proc913_4(global0, register)
				cycles = 8
			#end:case
			case 2:
				match register
					case chokers:
						if kernel.ScriptID(40, 0)._send('vineTalk:'):
							global91._send('say:', 13, 2, 26, 1, self)
						else:
							kernel.ScriptID(40, 0)._send('vineTalk:', 1)
							myConv._send(
								'add:', -1, 13, 2, 25, 1,
								'add:', -1, 13, 2, 25, 2,
								'add:', -1, 13, 2, 25, 3,
								'add:', -1, 13, 2, 25, 4,
								'add:', -1, 13, 2, 25, 5,
								'add:', -1, 13, 2, 25, 6,
								'add:', -1, 13, 2, 25, 7,
								'add:', -1, 13, 2, 25, 8,
								'init:', self
							)
						#endif
					#end:case
					else:
						if kernel.ScriptID(40, 0)._send('grapeTalk:'):
							global91._send('say:', 12, 2, 24, 1, self)
						else:
							myConv._send(
								'add:', -1, 12, 2, 23, 1,
								'add:', -1, 12, 2, 23, 2,
								'add:', -1, 12, 2, 23, 3,
								'add:', -1, 12, 2, 23, 4,
								'add:', -1, 12, 2, 23, 5,
								'add:', -1, 12, 2, 23, 6,
								'add:', -1, 12, 2, 23, 7,
								'add:', -1, 12, 2, 23, 8,
								'init:', self
							)
						#endif
					#end:else
				#end:match
			#end:case
			case 3:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class snappy(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				if (register == 5):
					global91._send('say:', 11, 5, 0, 1, self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 1:
				global0._send('setMotion:', PolyPath, 220, 130, self)
			#end:case
			case 2:
				global0._send('setHeading:', 90)
				cycles = 6
			#end:case
			case 3:
				if (register == 5):
					self._send('cue:')
				else:
					global91._send('say:', 11, 0, 0, 1, self)
				#endif
			#end:case
			case 4:
				global105._send('number:', 482, 'setLoop:', 1, 'play:', self)
				snap._send('setCycle:', Fwd)
			#end:case
			case 5:
				snap._send('setCycle:', 0, 'cel:', 0, 'stopUpd:')
				cycles = 4
			#end:case
			case 6:
				if (register == 5):
					global91._send('say:', 11, 5, 0, 2, self)
				else:
					global91._send('say:', 11, 0, 0, 2, self)
				#endif
			#end:case
			case 7:
				global0._send(
					'setLoop:', global0._send('cel:'),
					'setCycle:', Rev,
					'setMotion:', PolyPath, (global0._send('x:') - 15), global0._send('y:'), self
				)
			#end:case
			case 8:
				global0._send('setCycle:', Walk, 'setLoop:', -1)
				global1._send('handsOn:')
				self._send('dispose:')
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
		match state = param1
			case 0:
				seconds = 5
			#end:case
			case 1:
				global102._send('number:', 480, 'setLoop:', -1, 'play:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class fluteVerb(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 31:
				global2._send('setScript:', wallFlowerDance)
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
		super._send('cue:')
		match local2.post('++')
			case 1:
				if (not global5._send('contains:', myTeaCup)):
					self._send('dispose:')
				else:
					self._send('show:', 'cel:', 0, 'setLoop:', kernel.Random(0, 1), 'setCycle:', End, self)
				#endif
			#end:case
			case 2:
				self._send('hide:')
				local2 = 0
				glintTimer._send('setReal:', self, kernel.Random(3, 6))
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
		super._send('init:', &rest)
		local4 = 0
		if (not proc913_0(117)):
			proc913_1(117)
			global1._send('givePoints:', 2)
		#endif
		global93._send('addToFront:', self)
		global73._send('addToFront:', self)
		global72._send('addToFront:', self)
	#end:method

	@classmethod
	def dispose():
		global93._send('delete:', self)
		global73._send('delete:', self)
		global72._send('delete:', self)
		if local3:
			proc481_7()
			myBottle._send('setCycle:', RandCycle)
		#endif
		global102._send('number:', 480, 'setLoop:', -1, 'play:')
		danceMusic._send('prevSignal:', 0)
		global2._send('cue:', 0)
		super._send('dispose:')
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		if proc999_5(param1._send('type:'), 1, 2, 4, 256):
			(cond
				case (state == 9):
					if global25:
						global25._send('dispose:')
					#endif
					self._send('cue:')
					param1._send('localize:')
					param1._send('claimed:', 1)
				#end:case
				case 
					(and
						(state == 10)
						User._send('controls:')
						(param1._send('type:') & 0x1000)
					):
					param1._send('claimed:', 1)
					self._send('cue:')
				#end:case
				else:
					param1._send('claimed:', 0)
				#end:else
			)
		#endif
		param1._send('claimed:')
	#end:method

	@classmethod
	def doit():
		(cond
			case (global0._send('edgeHit:') == 3):
				global2._send('setScript:', egoExits)
			#end:case
			case (register and (state == 10)):
				self._send('cue:')
			#end:case
			case ((state > 6) and (state < 11) and (danceMusic._send('prevSignal:') == -1)):
				danceMusic._send('prevSignal:', 0)
				state = 10
				global1._send('handsOn:')
				self._send('cue:')
			#end:case
			case (danceMusic._send('prevSignal:') == 20):
				self._send('cue:')
				danceMusic._send('prevSignal:', 0)
				local1 = 7
				flower1._send('cycleSpeed:', (flower1._send('cycleSpeed:') - 1))
				flower2._send('cycleSpeed:', (flower2._send('cycleSpeed:') - 1))
				flower3._send('cycleSpeed:', (flower3._send('cycleSpeed:') - 1))
				flower4._send('cycleSpeed:', (flower4._send('cycleSpeed:') - 1))
				snap._send('cycleSpeed:', (snap._send('cycleSpeed:') - 1))
			#end:case
			case 
				(and
					(danceMusic._send('prevSignal:') == 10)
					(state <= 11)
					(state >= 6)
				):
				danceMusic._send('prevSignal:', 0)
				snap._send('setCycle:', Osc, local1, snap)
			#end:case
		)
		super._send('doit:')
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				local1 = 9
				global0._send(
					'ignoreActors:', 1,
					'illegalBits:', 0,
					'setMotion:', PolyPath, 190, 110, self
				)
			#end:case
			case 1:
				if kernel.ScriptID(40, 0)._send('bottleSucker:'):
					proc481_6()
					myBottle._send('setCycle:', 0)
					local3 = 1
				#endif
				global0._send('setHeading:', 45)
				cycles = 4
			#end:case
			case 2:
				global91._send('say:', 5, 31, 0, 1, self)
			#end:case
			case 3:
				global91._send('say:', 5, 31, 0, 2, self)
			#end:case
			case 4:
				register = 0
				if 
					(and
						global5._send('contains:', hiw)
						proc913_0(159)
						(hiw._send('x:') != 283)
						(hiw._send('y:') != 46)
					)
					hiw._send('setLoop:', 1, 'setCycle:', Walk, 'setMotion:', MoveTo, 238, 70)
				#endif
				kernel.ScriptID(40, 0)._send('flowerDance:', 1)
				flower1._send('view:', 4852, 'cel:', 2, 'setCycle:', Fwd)
				flower2._send('view:', 4852, 'cel:', 2, 'setCycle:', Fwd)
				flower3._send('view:', 4852, 'cel:', 6, 'setCycle:', Fwd)
				flower4._send('view:', 4852, 'cel:', 6, 'setCycle:', Fwd)
				if 
					(and
						(global9._send('at:', 18)._send('owner:') == global11)
						proc913_0(159)
					)
					global105._send('number:', 483, 'setLoop:', 1, 'play:')
					hiw._send('setLoop:', 5, 'setCycle:', Walk, 'setMotion:', MoveTo, 259, 49)
				#endif
				ticks = 6
			#end:case
			case 5:
				if (hiw._send('loop:') == 5):
					global105._send('stop:')
					hiw._send('setLoop:', 1)
				#endif
				global0._send(
					'view:', 920,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', global0._send('x:'), (global0._send('y:') + 2),
					'normal:', 0,
					'cycleSpeed:', 6
				)
				ticks = 6
			#end:case
			case 6:
				global102._send('stop:')
				danceMusic._send('number:', 486, 'setLoop:', 1, 'flags:', 0, 'play:')
				global0._send('setCycle:', Fwd)
			#end:case
			case 7:
				global0._send('setCycle:', End, self)
			#end:case
			case 8:
				global0._send('reset:', 0, 'posn:', global0._send('x:'), (global0._send('y:') - 2))
				cycles = 6
			#end:case
			case 9:
				danceMusic._send('flags:', 1)
				if (global90 & 0x0002):
					global91._send('say:', 5, 31, 0, 3, self)
				else:
					Print._send(
						'font:', 4,
						'addText:', 5, 31, 0, 3,
						'posn:', 10, 6,
						'width:', 289,
						'init:'
					)
					ticks = 12
				#endif
			#end:case
			case 10:
				global1._send('handsOn:')
			#end:case
			case 11:
				if global25:
					global25._send('dispose:')
				#endif
				danceMusic._send('fade:')
				seconds = 3
			#end:case
			case 12:
				kernel.ScriptID(40, 0)._send('flowerDance:', 0)
				if (global5._send('contains:', hiw) and proc913_0(159) and (not local4)):
					hiw._send('setLoop:', 1, 'setCycle:', Walk, 'setMotion:', MoveTo, 238, 70)
				#endif
				self._send('dispose:')
				flower1._send('view:', 4851, 'stopUpd:')
				flower2._send('view:', 4851, 'stopUpd:')
				flower3._send('view:', 4851, 'stopUpd:')
				flower4._send('view:', 4851, 'stopUpd:')
				snap._send('cel:', 0, 'stopUpd:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walkToHoleScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				if ((hiw._send('x:') != 238) and (hiw._send('y:') != 70)):
					hiw._send('setLoop:', 5, 'setCycle:', Walk, 'setMotion:', MoveTo, 238, 70, hiw)
				#endif
				global0._send('setMotion:', PolyPath, 242, 93, self)
			#end:case
			case 1:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class talkToSnaps(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 198, 130, self)
			#end:case
			case 1:
				global0._send('setHeading:', 90)
				cycles = 8
			#end:case
			case 2:
				global91._send('say:', 11, 2, 0, 1, self)
			#end:case
			case 3:
				global105._send('number:', 482, 'setLoop:', 1, 'play:', self)
				snap._send('setCycle:', Fwd)
			#end:case
			case 4:
				snap._send('setCycle:', 0, 'cel:', 0, 'stopUpd:')
				cycles = 3
			#end:case
			case 5:
				global91._send('say:', 11, 2, 0, 2, self)
			#end:case
			case 6:
				global1._send('handsOn:')
				snap._send('setCycle:', 0, 'cel:', 0, 'stopUpd:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

