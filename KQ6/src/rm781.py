#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 781
import sci_sh
import kernel
import Main
import rgCastle
import KQ6Print
import n913
import Inset
import Conversation
import Scaler
import Polygon
import Feature
import LoadMany
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm781 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.instance
class rm781(CastleRoom):
	#property vars (may be empty)
	noun = 3
	picture = 780
	style = 10
	vanishingX = 183
	vanishingY = 98
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		proc958_0(128, 787, 785, 786, 724, 726)
		global0._send('init:', 'setPri:', 13, 'setScale:', Scaler, 118, 70, 190, 140)
		self._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', -10, -10, 329, -10, 329, 179, 319, 179, 271, 154, 250, 154, 233, 143, 207, 143, 201, 147, 176, 147, 173, 142, 167, 142, 162, 147, 76, 147, 48, 162, 33, 162, 0, 177, -10, 177,
					'yourself:'
				)
		)
		global32._send('add:', trunk, box, rug, chandelier, 'eachElementDo:', #init)
		door._send('cel:', ((global12 == 850) * 4), 'init:', 'stopUpd:', 'approachVerbs:', 5)
		super._send('init:', &rest)
		trunkLid._send('init:')
		boxLid._send('init:')
		candles._send('init:')
		doorFrame1ATP._send('addToPic:')
		doorFrame2ATP._send('addToPic:')
		fireplaceATP._send('addToPic:')
		fireplace._send('setCycle:', Fwd, 'init:')
		wardrobeDoor._send('init:')
		bedATP._send('addToPic:')
		match global12
			case 810:
				wardrobeDoor._send('hide:')
				self._send('setScript:', wardrobeEntrance)
			#end:case
			else:
				self._send('setScript:', hallDoorEntrance)
			#end:else
		#end:match
		if global0._send('scaler:'):
			global0._send('scaler:')._send('doit:')
		#endif
		if (not script):
			global1._send('handsOn:')
		#endif
		global102._send('fadeTo:', 150, -1)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = global0._send('onControl:', 1)
		(cond
			case script: 0#end:case
			case (temp0 & 0x4000):
				global2._send('newRoom:', 850)
			#end:case
		)
		super._send('doit:', &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			match param1
				case 1:
					if global0._send('has:', 20):
						global91._send('say:', noun, param1, 5)
						1
					else:
						global91._send('say:', noun, param1, 4)
						1
					#endif
				#end:case
				else:
					super._send('doVerb:', param1, &rest)
				#end:else
			#end:match
		)
	#end:method

	@classmethod
	def warnUser(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 2:
				if inset:
					script._send('next:', they_reBack)
					inset._send('dispose:')
				else:
					self._send('setScript:', they_reBack)
				#endif
			#end:case
			else:
				super._send('warnUser:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global0._send('setPri:', -1)
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class hallDoorEntrance(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				door._send('cel:', 4, 'forceUpd:')
				global0._send(
					'setPri:', -1,
					'posn:', 306, 157,
					'setMotion:', MoveTo, door._send('approachX:'), door._send('approachY:'), self
				)
			#end:case
			case 1:
				global0._send('setPri:', 13)
				door._send('setCycle:', Beg, self)
			#end:case
			case 2:
				global105._send('number:', 902, 'loop:', 1, 'play:')
				door._send('stopUpd:')
				if kernel.ScriptID(80, 0)._send('tstFlag:', 709, 1):
					kernel.ScriptID(80, 0)._send('clrFlag:', 709, 1)
					cycles = 10
				else:
					global1._send('handsOn:')
					self._send('dispose:')
				#endif
			#end:case
			case 3:
				global2._send('warnUser:', 2)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class openTrunk(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				if 
					(and
						(not kernel.ScriptID(80, 0)._send('tstFlag:', 711, 4096))
						proc999_5(register, 64, 35)
					)
					global1._send('givePoints:', 1)
				#endif
				global0._send(
					'normal:', 0,
					'view:', 787,
					'loop:', 0,
					'cel:', 0,
					'cycleSpeed:', 8,
					'setScale:', 0,
					'scaleX:', 128,
					'scaleY:', 128,
					'posn:', 151, 154,
					'setCycle:', CT, 3, 1, self
				)
			#end:case
			case 1:
				if kernel.ScriptID(80, 0)._send('tstFlag:', 711, 4096):
					if proc999_5(register, 64, 35):
						state = 4
						global91._send('say:', 4, 35, 14, 0, self)
					else:
						global91._send('say:', 4, 5, 14, 0, self)
					#endif
				else:
					if (not proc999_5(register, 64, 35)):
						state = 4
					else:
						global105._send('number:', 781, 'loop:', 1, 'play:')
					#endif
					global91._send('say:', 4, register, 13, 0, self)
				#endif
			#end:case
			case 2:
				kernel.ScriptID(80, 0)._send('setFlag:', 711, 4096)
				trunkLid._send('hide:')
				global105._send('number:', 904, 'loop:', 1, 'play:')
				global0._send('cel:', 4, 'setCycle:', End, self)
			#end:case
			case 3:
				global105._send('stop:')
				global1._send('handsOn:')
				global69._send('disable:', 0, 3, 4, 5)
				global69._send('disable:', 0)
				chestInset._send('init:', self, global2)
			#end:case
			case 4:
				global105._send('number:', 905, 'loop:', 1, 'play:')
				global0._send('setCycle:', CT, 3, -1, self)
			#end:case
			case 5:
				trunkLid._send('show:')
				global105._send('stop:')
				global0._send('setCycle:', Beg, self)
			#end:case
			case 6:
				global1._send('handsOn:')
				global0._send('reset:', 1, 'setPri:', 13, 'posn:', 171, 148)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class openEbonyBox(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global91._send('say:', 14, 5, 0, 0, self)
			#end:case
			case 1:
				global0._send(
					'normal:', 0,
					'view:', 787,
					'loop:', 2,
					'cel:', 0,
					'setScale:', 0,
					'scaleX:', 128,
					'scaleY:', 128,
					'cycleSpeed:', 8,
					'setCycle:', CT, 4, 1, self
				)
			#end:case
			case 2:
				global69._send('disable:', 0)
				ebonyBoxInset._send('init:', self, global2)
				global1._send('handsOn:')
				global69._send('disable:', 0, 3, 4, 5)
			#end:case
			case 3:
				global1._send('handsOff:')
				global0._send('setCycle:', End, self)
			#end:case
			case 4:
				global0._send(
					'reset:', 6,
					'setPri:', 13,
					'posn:', box._send('approachX:'), box._send('approachY:')
				)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class wardrobeEntrance(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global103._send('number:', 783, 'loop:', 1, 'play:')
				global0._send(
					'normal:', 0,
					'view:', 785,
					'loop:', 2,
					'cel:', 9,
					'posn:', 58, 162,
					'cycleSpeed:', 8,
					'setScale:', 0,
					'scaleX:', 128,
					'scaleY:', 128,
					'setCycle:', Beg, self
				)
				global105._send('number:', 901, 'loop:', 1, 'play:')
			#end:case
			case 1:
				global0._send('loop:', 1, 'cel:', 5, 'setCycle:', CT, 2, -1, self)
			#end:case
			case 2:
				global0._send('setCycle:', Beg)
				global105._send('number:', 902, 'loop:', 1, 'play:')
				ticks = 60
			#end:case
			case 3:
				global0._send(
					'posn:', wardrobeDoor._send('approachX:'), wardrobeDoor._send('approachY:'),
					'reset:', 0,
					'setPri:', 13
				)
				wardrobeDoor._send('show:', 'stopUpd:')
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class they_reBack(Script):
	#property vars (may be empty)
	name = r"""they'reBack"""
	
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global91._send('say:', 1, 0, 3, 1, self)
			#end:case
			case 1:
				proc913_4(global0, door, self)
			#end:case
			case 2:
				global105._send('number:', 901, 'loop:', 1, 'play:')
				door._send('setCycle:', CT, 2, 1, self)
			#end:case
			case 3:
				global105._send('stop:')
				global91._send('say:', 1, 0, 3, 2, self)
			#end:case
			case 4:
				global105._send('number:', 901, 'loop:', 1, 'play:')
				door._send('setCycle:', End, self)
			#end:case
			case 5:
				global105._send('stop:')
				kernel.ScriptID(80, 5)._send('init:', 'posn:', 307, 158, 'loop:', 1)
				kernel.ScriptID(80, 0)._send('setupGuards:')
				kernel.ScriptID(80, 5)._send('setMotion:', MoveTo, 283, 158, self)
			#end:case
			case 6:
				global102._send('number:', 710, 'loop:', -1, 'play:')
				global91._send('say:', 1, 0, 3, 3, self, 'oneOnly:', 0)
			#end:case
			case 7:
				global102._send('fade:')
				kernel.ScriptID(80, 0)._send('setFlag:', 709, 8192)
				global2._send('newRoom:', 820)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class openWardrobe(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not local1):
			match state = param1
				case 0:
					global1._send('handsOff:')
					wardrobeDoor._send('hide:')
					global0._send(
						'normal:', 0,
						'view:', 785,
						'setScale:', 0,
						'scaleX:', 128,
						'scaleY:', 128,
						'loop:', 1,
						'cel:', 0,
						'posn:', 58, 162,
						'cycleSpeed:', 8,
						'setCycle:', CT, 2, 1, self
					)
				#end:case
				case 1:
					global103._send('number:', 901, 'loop:', 1, 'play:')
					global0._send('setCycle:', End, self)
				#end:case
				case 2:
					if (global12 != 810):
						global91._send('say:', 12, 5, 8, 0, self)
					else:
						(state += 2)
						cycles = 1
					#endif
				#end:case
				case 3:
					global0._send('setCycle:', CT, 1, -1, self)
				#end:case
				case 4:
					local1 = 1
					global0._send('cel:', 0)
					global105._send('number:', 902, 'loop:', 1, 'play:', self)
				#end:case
				case 5:
					global103._send('number:', 783, 'loop:', 1, 'play:')
					global0._send('loop:', 2, 'cel:', 0, 'setCycle:', CT, 8, 1, self)
				#end:case
				case 6:
					global0._send('cel:', 9)
					global105._send('number:', 902, 'loop:', 1, 'play:')
					cycles = 2
				#end:case
				case 7:
					global91._send('say:', 12, 5, 9, 0, self)
				#end:case
				case 8:
					global2._send('newRoom:', 810)
				#end:case
			#end:match
		else:
			local1 = 0
			global1._send('handsOn:')
			wardrobeDoor._send('show:', 'stopUpd:')
			global0._send(
				'posn:', wardrobeDoor._send('approachX:'), wardrobeDoor._send('approachY:'),
				'reset:', 1,
				'setPri:', 13
			)
			self._send('dispose:')
		#endif
	#end:method

#end:class or instance

@SCI.instance
class door(Prop):
	#property vars (may be empty)
	x = 298
	y = 161
	noun = 10
	sightAngle = 40
	approachX = 265
	approachY = 157
	view = 786
	loop = 1
	priority = 1
	signal = 16400
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global1._send('handsOff:')
				global0._send('setPri:', -1)
				global105._send('number:', 901, 'loop:', 1, 'play:')
				self._send('setCycle:', End, self)
			#end:case
			case 1:
				if local0:
					global91._send('say:', noun, param1, 12)
					global2._send('setScript:', kernel.ScriptID(82), 0, hallScr)
				else:
					local0.post('++')
					(_approachVerbs |= global66._send('doit:', 1))
					global91._send('say:', noun, param1, 11)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global105._send('stop:')
		proc80_2(2)
	#end:method

#end:class or instance

@SCI.instance
class hallScr(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if register = (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 128)):
			tempGuard1._send(
				'view:', kernel.ScriptID(80, 6)._send('view:'),
				'posn:', 192, 126,
				'setSpeed:', (3 if (global87 < 2) else 5),
				'init:'
			)
			tempGuard2._send(
				'posn:', 200, 128,
				'setSpeed:', (3 if (global87 < 2) else 5),
				'init:'
			)
		#endif
		super._send('init:', &rest)
		client._send('caller:', self)
		kernel.ScriptID(82, 1)._send('noun:', 26, 'actions:', keyHoleDoVerb, 'init:', 786, 0, 0, 91, 59)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if register:
			tempGuard1._send('dispose:')
			tempGuard2._send('dispose:')
		#endif
		super._send('dispose:')
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if client:
			super._send('cue:', &rest)
		else:
			global0._send('setPri:', 13)
		#endif
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if register:
					if (tempGuard1._send('x:') < 160):
						tempGuard1._send('setMotion:', MoveTo, 192, 126, self)
						tempGuard2._send('setMotion:', MoveTo, 200, 128)
					else:
						kernel.ScriptID(80, 0)._send('setFlag:', 711, 128)
						tempGuard1._send('setMotion:', MoveTo, 128, 126, self)
						tempGuard2._send('setMotion:', MoveTo, 120, 128)
					#endif
				else:
					cycles = 4
				#endif
			#end:case
			case 1:
				if register:
					if (tempGuard1._send('x:') < 160):
						seconds = 4
					else:
						seconds = 10
					#endif
				#endif
			#end:case
			case 2:
				kernel.ScriptID(80, 0)._send('clrFlag:', 711, 128)
				self._send('changeState:', 0)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class keyHoleDoVerb(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 1
		match param1
			case 1:
				if kernel.ScriptID(80, 0)._send('tstFlag:', 709, 128):
					global91._send('say:', 26, 1, 8)
				else:
					global91._send('say:', 26, 1, 9)
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
class tempGuard1(Actor):
	#property vars (may be empty)
	noun = 26
	sightAngle = 180
	loop = 4
	priority = 14
	signal = 16400
	scaleSignal = 1
	scaleX = 121
	scaleY = 121
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('setCycle:', Walk, 'setStep:', 4, 2, 'actions:', keyHoleDoVerb)
	#end:method

#end:class or instance

@SCI.instance
class tempGuard2(Actor):
	#property vars (may be empty)
	noun = 26
	sightAngle = 180
	view = 724
	loop = 4
	cel = 1
	priority = 14
	signal = 16400
	scaleSignal = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('setCycle:', Walk, 'setStep:', 4, 2, 'actions:', keyHoleDoVerb)
	#end:method

#end:class or instance

@SCI.instance
class doorJam(View):
	#property vars (may be empty)
	x = 298
	y = 161
	onMeCheck = 0
	view = 786
	loop = 8
	cel = 3
	
#end:class or instance

@SCI.instance
class wardrobeDoor(Prop):
	#property vars (may be empty)
	x = 40
	y = 116
	noun = 12
	approachX = 55
	approachY = 161
	view = 785
	loop = 3
	priority = 12
	signal = 16401
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('approachVerbs:', 5)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 5):
			global2._send('setScript:', openWardrobe)
		else:
			super._send('doVerb:', param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class trunkLid(Prop):
	#property vars (may be empty)
	x = 137
	y = 134
	noun = 4
	sightAngle = 40
	approachX = 166
	approachY = 149
	view = 787
	loop = 3
	priority = 12
	signal = 20496
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('approachVerbs:', 5, 35, 64)
	#end:method

	@classmethod
	def doVerb():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		trunk._send('doVerb:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class boxLid(Prop):
	#property vars (may be empty)
	x = 189
	y = 127
	sightAngle = 40
	onMeCheck = 0
	view = 787
	loop = 4
	signal = 20480
	
#end:class or instance

@SCI.instance
class candles(Prop):
	#property vars (may be empty)
	x = 165
	y = 84
	noun = 25
	view = 785
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('setCycle:', Fwd)
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class doorFrame1ATP(View):
	#property vars (may be empty)
	x = 298
	y = 160
	onMeCheck = 0
	view = 786
	loop = 8
	cel = 2
	signal = 20496
	
#end:class or instance

@SCI.instance
class doorFrame2ATP(View):
	#property vars (may be empty)
	x = 298
	y = 160
	onMeCheck = 0
	view = 786
	loop = 8
	cel = 3
	signal = 16384
	
#end:class or instance

@SCI.instance
class bedATP(View):
	#property vars (may be empty)
	x = 21
	y = 100
	sightAngle = 180
	view = 786
	loop = 8
	priority = 12
	signal = 20496
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = param1._send('x:')
		temp1 = param1._send('y:')
		approachY = approachX = _approachVerbs = 0
		(return
			(and
				super._send('onMe:', temp0, temp1)
				(temp0 -= nsLeft)
				(temp1 -= nsTop)
				(or
					(and
						(temp0 > 41)
						(or
							(and
								(global69._send('curIcon:') == global69._send('at:', 1))
								(_approachVerbs |= global66._send('doit:', 5))
								approachX = 105
								approachY = 150
							)
							1
						)
						noun = 21
					)
					self._send('approachX:', 55, 'approachY:', 161, 'approachVerbs:', 5)
					noun = 12
				)
			)
		)
	#end:method

	@classmethod
	def doVerb():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (noun == 12):
			wardrobeDoor._send('doVerb:', &rest)
		else:
			super._send('doVerb:', &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class fireplaceATP(View):
	#property vars (may be empty)
	x = 224
	y = 126
	view = 786
	loop = 8
	cel = 1
	signal = 20496
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = param1._send('x:')
		temp1 = param1._send('y:')
		(return
			(and
				super._send('onMe:', temp0, temp1)
				(temp0 -= nsLeft)
				(temp1 -= nsTop)
				(or
					((<= 0 temp0 26) and (<= 30 temp1 51) and noun = 20)
					((<= 63 temp0 98) and (<= 44 temp1 60) and noun = 24)
					noun = 23
				)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class fireplace(Prop):
	#property vars (may be empty)
	x = 225
	y = 117
	heading = 180
	noun = 23
	sightAngle = 40
	view = 786
	loop = 9
	priority = 1
	signal = 16400
	cycleSpeed = 8
	detailLevel = 2
	
#end:class or instance

@SCI.instance
class trunk(Feature):
	#property vars (may be empty)
	x = 153
	y = 145
	z = 8
	noun = 4
	nsTop = 132
	nsLeft = 138
	nsBottom = 146
	nsRight = 156
	sightAngle = 40
	approachX = 166
	approachY = 149
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('approachVerbs:', 5, 35, 64)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case proc999_5(param1, 5, 35, 64):
				global2._send('setScript:', openTrunk, 0, param1)
			#end:case
			case (global66._send('doit:', param1) == -32768):
				match param1
					case 61:
						super._send('doVerb:', param1)
					#end:case
					else:
						if kernel.ScriptID(80, 0)._send('tstFlag:', 711, 4096):
							global91._send('say:', noun, 0, 14)
						else:
							global91._send('say:', noun, 0, 13)
						#endif
					#end:else
				#end:match
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class box(Feature):
	#property vars (may be empty)
	x = 191
	y = 144
	z = 19
	heading = 180
	noun = 14
	nsTop = 122
	nsLeft = 183
	nsBottom = 128
	nsRight = 199
	sightAngle = 40
	approachX = 179
	approachY = 150
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('approachVerbs:', 5)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global2._send('setScript:', openEbonyBox)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class rug(Feature):
	#property vars (may be empty)
	noun = 22
	onMeCheck = 2
	
#end:class or instance

@SCI.instance
class chandelier(Feature):
	#property vars (may be empty)
	noun = 25
	onMeCheck = 4
	
#end:class or instance

@SCI.instance
class chestInset(Inset):
	#property vars (may be empty)
	view = 7861
	priority = 13
	disposeNotOnMe = 1
	noun = 8
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global69._send('disable:', 6)
		global0._send('setPri:', 0, 'stopUpd:')
		x = (160 - (kernel.CelWide(view, loop, cel) / 2))
		y = (90 - (kernel.CelHigh(view, loop, cel) / 2))
		super._send('init:', &rest)
		papers_ChestInset._send('init:', self)
		books_ChestInset._send('init:', self)
		vase_ChestInset._send('init:', self)
		lid_ChestInset._send('init:', self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global69._send('enable:', 6)
		if (caller == openTrunk):
			global1._send('handsOff:')
		#endif
		super._send('dispose:')
		global0._send('setPri:', 13, 'startUpd:')
	#end:method

#end:class or instance

@SCI.instance
class ebonyBoxInset(Inset):
	#property vars (may be empty)
	view = 7862
	disposeNotOnMe = 1
	noun = 15
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global69._send('disable:', 6)
		global0._send('stopUpd:')
		x = (160 - (kernel.CelWide(view, loop, cel) / 2))
		y = (90 - (kernel.CelHigh(view, loop, cel) / 2))
		super._send('init:', &rest)
		global105._send('number:', 904, 'play:')
		paper_BoxInset._send('init:', self)
		pens_BoxInset._send('init:', self)
		dice_BoxInset._send('init:', self)
		lid_BoxInset._send('cel:', 1, 'init:', self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global69._send('enable:', 6)
		super._send('dispose:', &rest)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (inset and inset._send('handleEvent:', param1)): 0#end:case
			case (param1._send('type:') & 0x4000):
				(cond
					case self._send('onMe:', param1):
						param1._send('claimed:', 1)
						self._send('doVerb:', param1._send('message:'))
					#end:case
					case disposeNotOnMe:
						param1._send('claimed:', 1)
						lid_BoxInset._send('doVerb:', 5)
					#end:case
					else:
						return 0
					#end:else
				)
			#end:case
		)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 2:
				global91._send('say:', 14, param1)
			#end:case
			else:
				if (global66._send('doit:', param1) == -32768):
					global91._send('say:', 14)
				else:
					super._send('doVerb:', param1)
				#endif
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class letterInset(Inset):
	#property vars (may be empty)
	view = 7863
	priority = 15
	disposeNotOnMe = 1
	noun = 15
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global69._send('disable:', 6)
		x = (160 - (kernel.CelWide(view, loop, cel) / 2))
		y = (100 - (kernel.CelHigh(view, loop, cel) / 2))
		super._send('init:', &rest)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global69._send('enable:', 6)
		super._send('dispose:')
	#end:method

#end:class or instance

class InsetView(View):
	#property vars (may be empty)
	sightAngle = 180
	priority = 15
	signal = 20497
	offsetX = 0
	offsetY = 0
	
	@classmethod
	def init(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		x = (param1._send('x:') + offsetX)
		y = (param1._send('y:') + offsetY)
		super._send('init:', &rest)
		self._send('stopUpd:')
	#end:method

#end:class or instance

@SCI.instance
class papers_ChestInset(InsetView):
	#property vars (may be empty)
	noun = 5
	view = 7861
	cel = 1
	offsetX = 64
	offsetY = 50
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				if global0._send('has:', 20):
					temp0 = 7
				else:
					temp0 = 6
				#endif
				global91._send('say:', noun, param1, temp0)
			#end:case
			case 5:
				if (not global0._send('has:', 20)):
					global0._send('get:', 20)
					global1._send('givePoints:', 1)
					openTrunk._send('next:', viewLetter)
					chestInset._send('dispose:')
				else:
					global91._send('say:', noun, param1, 7)
				#endif
			#end:case
			case 61:
				global91._send('say:', 4, 61)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class viewLetter(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global91._send('say:', 5, 5, 6, 1, self)
			#end:case
			case 1:
				letterInset._send('init:', 0, global2)
				cycles = 2
			#end:case
			case 2:
				roomConv._send(
					'add:', -1, 5, 5, 6, 2,
					'add:', -1, 5, 5, 6, 3,
					'add:', -1, 5, 5, 6, 4,
					'add:', -1, 5, 5, 6, 5,
					'init:', self
				)
			#end:case
			case 3:
				letterInset._send('caller:', self, 'dispose:')
			#end:case
			case 4:
				cycles = 2
			#end:case
			case 5:
				global91._send('say:', 5, 5, 6, 6, self, 'oneOnly:', 0)
			#end:case
			case 6:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class books_ChestInset(InsetView):
	#property vars (may be empty)
	noun = 6
	view = 7861
	cel = 2
	offsetX = 81
	offsetY = 42
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 2:
				papers_ChestInset._send('doVerb:', param1)
			#end:case
			case 61:
				global91._send('say:', 4, 61)
			#end:case
			else:
				if (global66._send('doit:', param1) == -32768):
					global91._send('say:', 5)
				else:
					super._send('doVerb:', param1, &rest)
				#endif
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class vase_ChestInset(InsetView):
	#property vars (may be empty)
	noun = 7
	view = 7861
	cel = 3
	offsetX = 95
	offsetY = 39
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 2:
				papers_ChestInset._send('doVerb:', param1)
			#end:case
			case 61:
				global91._send('say:', 4, 61)
			#end:case
			else:
				if (global66._send('doit:', param1) == -32768):
					global91._send('say:', 5)
				else:
					super._send('doVerb:', param1, &rest)
				#endif
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lid_ChestInset(InsetView):
	#property vars (may be empty)
	view = 7861
	cel = 4
	offsetX = 75
	offsetY = 6
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 5):
			chestInset._send('dispose:')
		else:
			chestInset._send('doVerb:', param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class paper_BoxInset(InsetView):
	#property vars (may be empty)
	noun = 19
	view = 7862
	cel = 1
	offsetX = 68
	offsetY = 39
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 1):
			if (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 64)):
				global1._send('givePoints:', 1)
			#endif
			kernel.ScriptID(80, 0)._send('setFlag:', 709, 64)
			KQ6Print._send('posn:', -1, 10, 'say:', 1, noun, param1, 0, 1, 'init:')
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class pens_BoxInset(InsetView):
	#property vars (may be empty)
	noun = 16
	view = 7862
	cel = 2
	offsetX = 69
	offsetY = 32
	
#end:class or instance

@SCI.instance
class dice_BoxInset(InsetView):
	#property vars (may be empty)
	noun = 17
	view = 7862
	cel = 3
	offsetX = 98
	offsetY = 35
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = param1._send('x:')
		temp1 = param1._send('y:')
		(return
			(and
				super._send('onMe:', temp0, temp1)
				(temp0 -= nsLeft)
				(temp1 -= nsTop)
				(((temp0 > 17) and noun = 18) or noun = 17)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class lid_BoxInset(InsetView):
	#property vars (may be empty)
	view = 7862
	loop = 1
	cel = 1
	offsetX = 91
	offsetY = 24
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				self._send('startUpd:')
				cel = 0
				global105._send('number:', 905, 'play:')
				kernel.Animate(global5._send('elements:'), 0)
				kernel.Animate(global5._send('elements:'), 0)
				ebonyBoxInset._send('dispose:')
			#end:case
			else:
				ebonyBoxInset._send('doVerb:', param1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class roomConv(Conversation):
	#property vars (may be empty)
#end:class or instance

