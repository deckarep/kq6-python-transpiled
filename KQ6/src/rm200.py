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
	if proc913_0(11):
		proc913_2(11)
	else:
		proc913_1(11)
	#endif
	global2._send('obstacles:')._send('delete:', plankPoly)
	global2._send(
		'addObstacle:', if proc913_0(11):
				chest._send('setPri:', -1)
				plankPoly._send('type:', 2, 'points:', @local13, 'size:', 8, 'yourself:')
			else:
				chest._send('setPri:', 1)
				plankPoly._send('type:', 2, 'points:', @local3, 'size:', 5, 'yourself:')
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
		global2._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 150, 108, 114, 115, 102, 134, 62, 152, -50, 189, -50, -200, 319, -200, 319, 189, 215, 189, 263, 143, 271, 117, 222, 107, 210, 99, 205, 87, 211, 70, 235, 60, 267, 54, 250, 51, 192, 67, 187, 80, 191, 102,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 214, 117, 232, 117, 243, 120, 243, 125, 193, 125, 193, 123,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 144, 183, 144, 179, 181, 169, 179, 183,
					'yourself:'
				)
		)
		global69._send('enable:')
		if (global12 == 155):
			style = 6
		#endif
		super._send('init:', &rest)
		global0._send('ignoreActors:', 'actions:', egoDoVerb)
		genericFeatures._send('init:')
		kernel.ScriptID(10, 4)._send('onMeCheck:', 32, 'init:')
		if global2._send('script:'):
			global2._send('script:')._send('caller:', self)
		#endif
		if proc999_5(global12, 105, 106, 108, 99):
			global0._send('init:')
			kernel.Palette(4, 0, 256, 100)
			self._send('setScript:', kernel.ScriptID(201))
			global153 = 1
		else:
			match global12
				case 210:
					global0._send('init:')
					global2._send('setScript:', enterRoomScr)
				#end:case
				case 155:
					global0._send('init:', 'view:', 203)
					global69._send('disable:', 6)
					global1._send('setCursor:', global19)
					self._send('setScript:', kernel.ScriptID(202))
				#end:case
				case 100:
					global0._send(
						'init:',
						'posn:', 175, 130,
						'loop:', 2,
						'setScale:', Scaler, 100, 50, 112, 57
					)
					global1._send('handsOn:')
					global69._send('curIcon:', global69._send('at:', 0))
					global1._send('setCursor:', global69._send('curIcon:')._send('cursor:'))
				#end:case
			#end:match
		#endif
		bush1._send('init:')
		bush2._send('init:')
		bush3._send('init:')
		shipsails._send('init:')
		wave._send('init:')
		if (global1._send('_detailLevel:') > 1):
			wave._send('setScript:', waveScr)
			if (global1._send('_detailLevel:') > 2):
				bush1._send('setScript:', kernel.Clone(kernel.ScriptID(13, 0)))
				bush2._send('setScript:', kernel.Clone(kernel.ScriptID(13, 0)))
				shipsails._send('setScript:', kernel.Clone(kernel.ScriptID(13, 0)))
				bush3._send('setScript:', kernel.ScriptID(13, 0))
			#endif
		#endif
		if (global153 == 0):
			global153 = 1
		#endif
		if (global9._send('at:', 39)._send('owner:') == 200):
			royalRing._send('init:')
		#endif
		plank._send('init:')
		shipWheel._send('init:')
		local0 = 0
		if (global12 == 155):
			global102._send('fade:')
		else:
			global102._send('number:', 915, 'loop:', -1, 'play:')
		#endif
		global103._send('number:', 916, 'loop:', -1, 'play:')
		global93._send('addToFront:', self)
		global74._send('addToFront:', self)
	#end:method

	@classmethod
	def cue():
		global0._send('setScale:', Scaler, 100, 50, 112, 57)
	#end:method

	@classmethod
	def doit():
		super._send('doit:')
		(cond
			case ((temp0 = global0._send('onControl:', 1) & 0x0100) and (not local29)):
				local29 = 1
				plank._send('setPri:', 15)
			#end:case
			case ((not (temp0 & 0x0100)) and local29):
				local29 = 0
				plank._send('setPri:', 3)
			#end:case
		)
		(cond
			case script: 0#end:case
			case (temp0 & 0x4000):
				global2._send('setScript:', exitRoomScr)
			#end:case
			case (temp0 & 0x0004):
				(cond
					case (local0 != 1):
						global104._send('number:', 922, 'loop:', -1, 'play:')
						global0._send('view:', 308)
						if (not global0._send('cycler:')._send('isKindOf:', StopWalk)):
							global0._send('setCycle:', StopWalk, -1)
						#endif
						if (local0 == 0):
							(cond
								case (global0._send('heading:') < 135):
									global0._send('loop:', 0)
								#end:case
								case (global0._send('heading:') > 225):
									global0._send('loop:', 1)
								#end:case
								else:
									global0._send('loop:', 2)
								#end:else
							)
						#endif
						local0 = 1
					#end:case
					case (global0._send('isStopped:') and (not local2) and local1):
						global91._send('say:', 10, 3, 12, 1)
						local2 = 1
					#end:case
				)
			#end:case
			case (temp0 & 0x0200):
				(cond
					case (local0 != 2):
						if (local0 == 0):
							global104._send('number:', 922, 'loop:', -1, 'play:')
						#endif
						global0._send('view:', 3081)
						if 
							(and
								(not global0._send('cycler:')._send('isKindOf:', StopWalk))
								(not global0._send('cycler:')._send('isKindOf:', Rev))
							)
							global0._send('setCycle:', StopWalk, -1)
						#endif
						local0 = 2
					#end:case
					case (global0._send('isStopped:') and (not local2) and local1):
						if local30:
							self._send('setScript:', egoStruggleScr)
							local2 = 1
							local30 = 0
						else:
							global91._send('say:', 10, 3, 12, 1)
							local2 = 1
						#endif
					#end:case
				)
			#end:case
			case (temp0 & 0x0008):
				if (local0 != 3):
					if local1:
						global1._send('handsOff:')
						global0._send(
							'setLoop:', global0._send('loop:'),
							'setMotion:', 0,
							'normal:', 0,
							'setSpeed:', 8,
							'setCycle:', Rev
						)
						while True: #repeat
							global0._send('y:', (global0._send('y:') - 1))
							(breakif (not (global0._send('onControl:', 1) & 0x0008)))
						#end:loop
						local30 = 1
					else:
						self._send('setScript:', deathByWaterScr)
					#endif
					local0 = 3
				#endif
			#end:case
			case (local0 != 0):
				global104._send('fade:', 0, 10, 15, 1)
				global0._send('view:', 900, 'setCycle:', Walk)
				local0 = 0
			#end:case
		)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		if (param1._send('type:') & 0x1040):
			if ((global69._send('at:', 0) == global69._send('curIcon:')) and (local0 == 0)):
				local1 = 1
				local2 = 0
			else:
				local1 = 0
			#endif
		else:
			super._send('handleEvent:', param1)
		#endif
		param1._send('claimed:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		(return
			match param1
				case 2:
					global91._send('say:', noun, param1, 5)
					1
				#end:case
				else:
					super._send('doVerb:', param1)
				#end:else
			#end:match
		)
	#end:method

	@classmethod
	def dispose():
		global102._send('fade:')
		global103._send('fade:')
		global93._send('delete:', self)
		global74._send('delete:', self)
		super._send('dispose:')
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
		super._send(
			'init:', 92, 58, 151, 58, 157, 65, 95, 93, 100, 115, 139, 132, 170, 132, 196, 143, 93, 143
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
		super._send('init:', &rest)
		onMeCheck = sandPoly._send('init:', 'yourself:')
		self._send('setOnMeCheck:', 2, onMeCheck)
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
		super._send('init:', &rest)
		if (global9._send('at:', 9)._send('owner:') == global11):
			coin._send('init:')
		#endif
		sand._send('init:')
		global1._send('handsOn:')
		global69._send('disable:', 0, 3, 4, 5, 6)
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		if 
			proc999_4((insetView._send('nsLeft:') + 5), (insetView._send('nsTop:') + 5), (-
				insetView._send('nsRight:')
				5
			), (insetView._send('nsBottom:') - 5), param1)
			return 1
		else:
			return 0
		#endif
	#end:method

	@classmethod
	def dispose():
		if global5._send('contains:', 9):
			coin._send('dispose:')
		#endif
		sand._send('dispose:')
		super._send('dispose:')
		global69._send('enable:', 0, 3, 6)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				if (global9._send('at:', 9)._send('owner:') == 200):
					global91._send('say:', noun, param1, 10)
				else:
					global91._send('say:', noun, param1, 11)
				#endif
			#end:case
			case 5:
				if (global9._send('at:', 9)._send('owner:') == 200):
					global91._send('say:', noun, param1, 10)
				else:
					global91._send('say:', noun, param1, 11)
				#endif
			#end:case
			case 40:
				global91._send('say:', 5, param1)
			#end:case
			else:
				if (param1 != 2):
					param1 = 0
				#endif
				super._send('doVerb:', param1, &rest)
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
	def doVerb(param1 = None, *rest):
		match param1
			case 12:
				global2._send('setScript:', 130)
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
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 252, 58, self)
			#end:case
			case 1:
				global0._send(
					'ignoreActors:',
					'setPri:', 1,
					'setLoop:', 3,
					'setScale:',
					'illegalBits:', 0,
					'setMotion:', MoveTo, 261, 86, self
				)
			#end:case
			case 2:
				global2._send('newRoom:', 210)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class enterRoomScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send(
					'setPri:', 1,
					'setLoop:', 2,
					'posn:', 261, 86,
					'scaleX:', 64,
					'scaleY:', 64,
					'scaleSignal:', 1,
					'show:',
					'setMotion:', MoveTo, 252, 58, self
				)
			#end:case
			case 1:
				global0._send(
					'setPri:', -1,
					'setLoop:', -1,
					'setScale:', Scaler, 100, 50, 112, 57,
					'setMotion:', PolyPath, 204, 103, self
				)
			#end:case
			case 2:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getCoinScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global69._send('enable:', 6)
				global1._send('handsOff:')
				global0._send('get:', 9)
				global1._send('givePoints:', 1)
				coin._send('dispose:')
				cycles = 2
			#end:case
			case 1:
				global91._send('say:', 7, 5)
				cycles = 2
			#end:case
			case 2:
				chestInset._send('dispose:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoStruggleScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				register = kernel.Random(2, 4)
				ticks = 30
			#end:case
			case 1:
				if (global0._send('loop:') == 2):
					global0._send('setLoop:', 1)
				else:
					global0._send('setLoop:', 2)
				#endif
				if (not register.post('--')):
					state.post('--')
				#endif
				ticks = 30
			#end:case
			case 2:
				global0._send('normal:', 1, 'setCycle:', StopWalk, -1, 'setLoop:', -1)
				cycles = 2
			#end:case
			case 3:
				global91._send('say:', 10, 3, 12, 1, self)
			#end:case
			case 4:
				global0._send('setSpeed:', global0._send('currentSpeed:'))
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoIntoSafeWater(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('setMotion:', 0, 'view:', 308)
				global91._send('say:', 10, 3, 12, 1, self)
			#end:case
			case 1:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class deathByWaterScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global91._send('say:', 10, 3, 15, 0, self)
			#end:case
			case 1:
				global104._send('stop:', 'number:', 921, 'loop:', 1, 'play:')
				global0._send(
					'view:', 269,
					'setLoop:', 0,
					'cel:', 0,
					'normal:', 0,
					'cycleSpeed:', 6,
					'setCycle:', End, self,
					'heading:', 200,
					'setMotion:', MoveFwd, 200
				)
			#end:case
			case 2:
				global2._send('newRoom:', 135)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class replacePlankScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				localproc_0()
				global0._send(
					'normal:', 0,
					'posn:', 242, 139,
					'setSpeed:', 6,
					'view:', 201,
					'loop:', 1,
					'cel:', 8,
					'setScale:', 0,
					'setCycle:', CT, 5, -1, self
				)
			#end:case
			case 1:
				plank._send('cel:', 0, 'hide:')
				global0._send('loop:', 2, 'cel:', 5, 'setCycle:', CT, 3, -1, self)
				global105._send('number:', 200, 'loop:', 1, 'play:')
			#end:case
			case 2:
				plank._send('show:', 'stopUpd:')
				cycles = 1
			#end:case
			case 3:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 4:
				chest._send('dispose:')
				global0._send(
					'posn:', plank._send('approachX:'), plank._send('approachY:'),
					'reset:', 2,
					'setScale:', Scaler, 100, 50, 112, 57
				)
				cycles = 2
			#end:case
			case 5:
				global91._send('say:', 4, 5, 7, 0, self)
			#end:case
			case 6:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class displacePlankScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send(
					'setSpeed:', 6,
					'posn:', 242, 139,
					'view:', 201,
					'normal:', 0,
					'loop:', 2,
					'cel:', 0,
					'setScale:', 0,
					'setCycle:', CT, 3, 1, self
				)
			#end:case
			case 1:
				chest._send('init:')
				global105._send('number:', 200, 'loop:', 1, 'play:')
				cycles = 2
			#end:case
			case 2:
				plank._send('cel:', 1, 'hide:')
				cycles = 1
			#end:case
			case 3:
				global0._send('setCycle:', CT, 4, 1, self)
			#end:case
			case 4:
				plank._send('show:', 'stopUpd:')
				global0._send('setCycle:', End, self)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				global0._send('loop:', 1, 'cel:', 5, 'setCycle:', End, self)
			#end:case
			case 7:
				global0._send(
					'reset:', 5,
					'posn:', plank._send('approachX:'), plank._send('approachY:'),
					'setScale:', Scaler, 100, 50, 112, 57
				)
				localproc_0()
				cycles = 2
			#end:case
			case 8:
				global91._send('say:', 4, 5, 6, 0, self)
			#end:case
			case 9:
				if (not proc913_1(92)):
					global1._send('givePoints:', 1)
				#endif
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class objectGlitter(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				seconds = kernel.Random(2, 7)
			#end:case
			case 1:
				state = -1
				client._send('cel:', 0, 'setCycle:', End, self)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class openChestScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				cycles = 1
			#end:case
			case 1:
				global0._send(
					'setSpeed:', 6,
					'normal:', 0,
					'posn:', chest._send('x:'), chest._send('y:'),
					'view:', 201,
					'loop:', 3,
					'cel:', 0,
					'setScale:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				ticks = 12
			#end:case
			case 3:
				global105._send('number:', 904, 'loop:', 1, 'play:', self)
			#end:case
			case 4:
				ticks = 12
			#end:case
			case 5:
				chestInset._send('init:', self, global2)
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				global1._send('handsOff:')
				ticks = 1
			#end:case
			case 8:
				global105._send('number:', 905, 'loop:', 1, 'play:', self)
			#end:case
			case 9:
				ticks = 12
			#end:case
			case 10:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 11:
				global0._send('posn:', 240, 132, 'reset:', 2, 'setScale:', Scaler, 100, 50, 112, 57)
				cycles = 2
			#end:case
			case 12:
				global1._send('handsOn:')
				self._send('dispose:')
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
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				self._send('setScript:', openChestScr)
			#end:case
			case 1:
				global91._send('say:', noun, param1, 9)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('approachVerbs:', 5)
	#end:method

#end:class or instance

@SCI.instance
class takeRingScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				if (global0._send('loop:') != 1):
					global0._send('setHeading:', 315, self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				global0._send(
					'normal:', 0,
					'setSpeed:', 8,
					'view:', 201,
					'loop:', 4,
					'cel:', 0,
					'setCycle:', End, self
				)
				royalRing._send('dispose:')
			#end:case
			case 3:
				global1._send('givePoints:', 1)
				global0._send('reset:', 7, 'get:', 39)
				cycles = 2
			#end:case
			case 4:
				global91._send('say:', 9, 5, 0, 0, self)
			#end:case
			case 5:
				global1._send('handsOn:')
				self._send('dispose:')
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
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				global2._send('setScript:', takeRingScr)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		self._send(
			'cel:', 0,
			'setCycle:', End,
			'setScript:', kernel.Clone(objectGlitter),
			'approachVerbs:', 5
		)
		if (not proc913_0(48)):
			loop = 3
		#endif
		super._send('init:', &rest)
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
		self._send(
			'cel:', 0,
			'setCycle:', End,
			'setScript:', kernel.Clone(objectGlitter),
			'sightAngle:', 360,
			'setPri:', 15
		)
		super._send('init:', &rest)
		sightAngle = 26505
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				global2._send('setScript:', getCoinScr)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
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
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				if proc913_0(11):
					global2._send('setScript:', replacePlankScr)
				else:
					global2._send('setScript:', displacePlankScr)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		super._send('init:', &rest)
		self._send(
			'approachVerbs:', 5,
			'cel:', if proc913_0(11):
					chest._send('init:')
					1
				else:
					0
				#endif
		)
		global2._send(
			'addObstacle:', if proc913_0(11):
					chest._send('setPri:', -1)
					plankPoly._send('type:', 2, 'points:', @local13, 'size:', 8, 'yourself:')
				else:
					chest._send('setPri:', 1)
					plankPoly._send('type:', 2, 'points:', @local3, 'size:', 5, 'yourself:')
				#endif
		)
	#end:method

#end:class or instance

@SCI.instance
class genericFeatures(Feature):
	#property vars (may be empty)
	@classmethod
	def onMe(param1 = None, *rest):
		temp0 = kernel.OnControl(4, param1._send('x:'), param1._send('y:'))
		genericFeatures._send('x:', param1._send('x:'), 'y:', param1._send('y:'))
		(return
			(= noun
				(cond
					case (temp0 == 128): 15#end:case
					case 
						(or
							(temp0 == 256)
							((temp0 == 2048) and (param1._send('y:') > 91))
						):
						14
					#end:case
					case (temp0 == 64): 12#end:case
					case (temp0 == 16): 11#end:case
					case ((temp0 == 512) and (param1._send('y:') < 130)): 16#end:case
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
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				wave._send('cel:', 0, 'setCycle:', End, self)
			#end:case
			case 1:
				wave._send('setCycle:', Beg, self)
			#end:case
			case 2:
				wave._send('hide:')
				seconds = kernel.Random(3, 8)
			#end:case
			case 3:
				wave._send('show:')
				state = -1
				self._send('cue:')
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
	def onMe(param1 = None, *rest):
		(return
			(or
				proc999_4(145, 175, 160, 181, param1._send('x:'), param1._send('y:'))
				proc999_4(162, 169, 175, 177, param1._send('x:'), param1._send('y:'))
				proc999_4(171, 164, 177, 169, param1._send('x:'), param1._send('y:'))
				proc999_4(156, 170, 162, 175, param1._send('x:'), param1._send('y:'))
			)
		)
	#end:method

#end:class or instance

