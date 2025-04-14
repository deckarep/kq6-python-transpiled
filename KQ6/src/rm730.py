#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 730
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
import LoadMany
import StopWalk
import Rev
import Motion
import User
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm730 = 0,
	kitchenDoor = 1,
	basementDoor = 2,
	proc730_3 = 3,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None


@SCI.procedure
def proc730_3():
	global2._send(
		'vanishingX:', 160,
		'vanishingY:', -10000,
		'maxScaleSize:', 100,
		'minScaleSize:', 60
	)
	if local0:
		global2._send('maxScaleY:', 127, 'minScaleY:', 68, 'minScaleSize:', 64)
	else:
		global2._send('maxScaleY:', 174, 'minScaleY:', 127)
	#endif
	global0._send(
		'setScale:', Scaler, global2._send('maxScaleSize:'), global2._send(
				'minScaleSize:'
			), global2._send('maxScaleY:'), global2._send('minScaleY:')
	)
#end:procedure

@SCI.procedure
def localproc_0(param1 = None, param2 = None, param3 = None, *rest):
	temp0 = param3
	while (param1 & kernel.OnControl(4, param2, temp0)): # inline for
	#end:loop
	return temp0
#end:procedure

@SCI.instance
class rm730(CastleRoom):
	#property vars (may be empty)
	noun = 3
	picture = 730
	style = 10
	horizon = 0
	
	@classmethod
	def init():
		kernel.Load(128, 730)
		if kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2):
			0
		else:
			proc958_0(128, 794, 736)
		#endif
		self._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 19, 170, 9, 158, 12, 141, 75, 69, 53, 69, 0, 109, -50, 110, -50, -60, 369, -60, 319, 114, 263, 65, 246, 65, 315, 146, 312, 162, 286, 178, 212, 129, 109, 129, 90, 142, 77, 142, 80, 149, 37, 179,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 176, 134, 196, 134, 200, 141, 176, 141,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 126, 134, 145, 134, 145, 141, 122, 141,
					'yourself:'
				)
		)
		global32._send(
			'add:', urns, chandelier, balconyFtr, pillarsFtr, stairs,
			'eachElementDo:', #init
		)
		kernel.ScriptID(80, 5)._send('noun:', 4)
		kernel.ScriptID(80, 6)._send('noun:', 4)
		super._send('init:', &rest)
		global0._send('init:')
		candles._send('setCycle:', Fwd, 'init:')
		match global12
			case 740:
				global0._send('posn:', throneDoor._send('approachX:'), throneDoor._send('approachY:'))
			#end:case
			case 860:
				local0 = 1
				global0._send('posn:', 272, 84)
			#end:case
			case 850:
				local0 = 1
				global0._send('posn:', 52, 84)
				(cond
					case kernel.ScriptID(80, 0)._send('tstFlag:', 711, 16384):
						kernel.ScriptID(80, 0)._send('clrFlag:', 711, 16384)
						kernel.ScriptID(80, 5)._send(
							'init:',
							'loop:', 0,
							'posn:', 107, 68,
							'setPri:', 0,
							'ignoreActors:',
							'setScale:', Scaler, 35, 64, 107, 59, 1
						)
						kernel.ScriptID(80, 6)._send(
							'init:',
							'loop:', 3,
							'posn:', 111, 68,
							'setPri:', 0,
							'ignoreActors:',
							'setScale:', Scaler, 35, 64, 111, 69, 1
						)
						global0._send('posn:', 46, 83)
						global102._send('fade:', 80, 25, 10, 0)
						self._send('setScript:', followEgoIn)
					#end:case
					case local2 = kernel.ScriptID(80, 0)._send('tstFlag:', 709, 512):
						kernel.ScriptID(80, 5)._send('init:', 'loop:', 0, 'posn:', 82, 165)
						kernel.ScriptID(80, 6)._send('init:', 'loop:', 3, 'posn:', 103, 176)
						kernel.ScriptID(80, 6)._send(
							'signal:', (kernel.ScriptID(80, 6)._send('signal:') & 0xefff)
						)
						saladin._send('init:', 'loop:', 4, 'cel:', 1, 'stopUpd:')
						(cond
							case kernel.ScriptID(80, 0)._send('tstFlag:', 710, 1):
								kernel.ScriptID(80, 5)._send('posn:', 9, 113)
								kernel.ScriptID(80, 6)._send('posn:', 18, 128)
								self._send('spotEgo:', kernel.ScriptID(80, 5))
							#end:case
							case (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2048)):
								global0._send('posn:', 51, 83)
								self._send('setScript:', overseeGuards)
							#end:case
							else:
								self._send('setScript:', tooManyTimes)
							#end:else
						)
					#end:case
				)
			#end:case
			case 840:
				global0._send('setSpeed:', 8, 'posn:', 261, 144)
				self._send('setScript:', kernel.ScriptID(732, 0))
			#end:case
			else:
				global102._send('fadeTo:', 700, -1)
				global0._send('reset:', 3, 733, 'posn:', 229, 181)
				kernel.ScriptID(80, 0)._send('setFlag:', 709, 128)
				self._send('setScript:', kernel.ScriptID(731, 0))
			#end:else
		#end:match
		kitchenDoor._send('init:', 'stopUpd:', 'ignoreActors:')
		throneDoor._send(
			'init:',
			'ignoreActors:',
			'setPri:', 1,
			'cel:', kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2),
			'stopUpd:'
		)
		basementDoor._send('init:', 'stopUpd:', 'ignoreActors:')
		if kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2):
			if script:
				script._send('next:', saladinEnters)
			else:
				self._send('setScript:', saladinEnters)
			#endif
		#endif
		proc730_3()
		kernel.ScriptID(80, 0)._send('setupGuards:')
		if global5._send('contains:', saladin):
			saladin._send(
				'setScale:', Scaler, maxScaleSize, minScaleSize, maxScaleY, minScaleY
			)
			saladin._send('scaler:')._send('doit:')
		#endif
		if global0._send('scaler:'):
			global0._send('scaler:')._send('doit:')
		#endif
		if (not script):
			global1._send('handsOn:')
		#endif
	#end:method

	@classmethod
	def doit():
		local1 = global0._send('onControl:', 1)
		(cond
			case script: 0#end:case
			case (User._send('alterEgo:')._send('edgeHit:') == 3):
				global0._send('y:', (global0._send('y:') - 2))
				self._send('setScript:', don_tLeave)
			#end:case
			case (local1 & 0x4000):
				global2._send('newRoom:', 860)
			#end:case
			case (local1 & 0x2000):
				global2._send('newRoom:', 850)
			#end:case
			case (local1 & 0x0800):
				global2._send('newRoom:', 840)
			#end:case
		)
		if (global0._send('view:') != 881):
			if ((local1 & 0x0200) and local0):
				local0 = 0
				proc730_3()
			#endif
			if ((local1 & 0x0400) and (not local0)):
				local0 = 1
				proc730_3()
			#endif
		#endif
		if ((not (local1 & 0x0600)) and (vanishingY == -10000)):
			if local0:
				vanishingY = -7
			else:
				vanishingY = 92
			#endif
		#endif
		super._send('doit:', &rest)
	#end:method

	@classmethod
	def setScript(param1 = None, *rest):
		if ((script == saladinEnters) and (param1 != showLetter)):
			global1._send('handsOff:')
			saladinEnters._send('cue:')
		else:
			super._send('setScript:', param1, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class don_tLeave(Script):
	#property vars (may be empty)
	name = r"""don'tLeave"""
	
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				cycles = 4
			#end:case
			case 1:
				global91._send('say:', 3, 3, 14, 0, self)
			#end:case
			case 2:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class doKitchen(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 711, -32768)):
					kernel.ScriptID(80, 0)._send('setFlag:', 711, -32768)
					global91._send('say:', 8, 5, 0, 1, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				global105._send('number:', 901, 'loop:', 1, 'play:')
				global104._send('number:', 731, 'loop:', -1, 'play:')
				kitchenDoor._send('setCycle:', End, self)
			#end:case
			case 2:
				global105._send('stop:')
				global0._send('setHeading:', 270, 'setMotion:', MoveTo, 57, 143, self)
			#end:case
			case 3:
				global91._send('say:', 8, 5, 0, 2, self)
			#end:case
			case 4:
				global0._send(
					'setMotion:', MoveTo, kitchenDoor._send('approachX:'), kitchenDoor._send(
							'approachY:'
						), self
				)
			#end:case
			case 5:
				global104._send('stop:')
				kitchenDoor._send('setCycle:', Beg, self)
			#end:case
			case 6:
				global91._send('say:', 8, 5, 0, 3, self, 'oneOnly:', 0)
			#end:case
			case 7:
				global105._send('number:', 902, 'loop:', 1, 'play:')
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class overseeGuards(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		kernel.ScriptID(80, 0)._send('setFlag:', 709, 2048)
		super._send('dispose:')
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				kernel.ScriptID(1015, 6)._send('talkWidth:', 150, 'x:', 15, 'y:', 20)
				kernel.ScriptID(1015, 7)._send('talkWidth:', 135, 'x:', 160, 'y:', 20)
				cycles = 10
			#end:case
			case 1:
				global91._send('say:', 1, 0, 3, 0, self)
			#end:case
			case 2:
				seconds = 2
			#end:case
			case 3:
				global102._send('number:', 710, 'loop:', -1, 'play:')
				if proc913_0(72):
					register = 5
				else:
					register = 4
				#endif
				global91._send('say:', 1, 0, register, 1, self)
			#end:case
			case 4:
				kernel.ScriptID(80, 5)._send('setScript:', kernel.ScriptID(80, 4), self, 1)
			#end:case
			case 5:
				global0._send(
					'setSpeed:', 8,
					'ignoreActors:',
					'setMotion:', PolyPath, (saladin._send('x:') - 45), saladin._send('y:'), self
				)
				seconds = 3
			#end:case
			case 6:
				kernel.ScriptID(80, 5)._send(
					'setSpeed:', 8,
					'ignoreActors:',
					'setMotion:', PolyPath, (saladin._send('x:') - 45), kernel.ScriptID(80, 6)._send(
							'y:'
						), self
				)
			#end:case
			case 7:
				global0._send('setHeading:', 90)
			#end:case
			case 8:
				global91._send('say:', 1, 0, register, 2, self, 'oneOnly:', 0)
			#end:case
			case 9:
				global2._send('newRoom:', 820)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class tooManyTimes(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				cycles = 4
			#end:case
			case 1:
				register = (5 if proc913_0(72) else 4)
				global91._send('say:', 1, 0, register, 1, self)
			#end:case
			case 2:
				kernel.ScriptID(80, 5)._send('setScript:', kernel.ScriptID(80, 4), self, 1)
			#end:case
			case 3:
				global91._send('say:', 1, 0, register, 2, self, 'oneOnly:', 0)
			#end:case
			case 4:
				kernel.ScriptID(80, 0)._send('setFlag:', 709, 8192)
				global2._send('newRoom:', 820)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class saladinEnters(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		super._send('init:', &rest)
		global93._send('add:', self)
		global74._send('add:', self)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		if 
			(and
				global80._send('canInput:')
				(or
					(param1._send('type:') & 0x1000)
					((param1._send('type:') & 0x0040) and (param1._send('message:') != 0))
				)
			)
			param1._send('claimed:', 1)
			self._send('cue:')
		#endif
		param1._send('claimed:')
	#end:method

	@classmethod
	def dispose():
		global93._send('delete:', self)
		global74._send('delete:', self)
		super._send('dispose:')
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				kernel.ScriptID(80, 0)._send('weddingRemind:', 0)
				if (global12 == 840):
					self._send('setScript:', exitBaseScr, self)
				else:
					self._send('setScript:', exitUpstairsScr, self)
				#endif
			#end:case
			case 1:
				global0._send('setMotion:', PolyPath, 150, 128, self)
			#end:case
			case 2:
				global0._send('setHeading:', 45, self)
			#end:case
			case 3:
				cycles = 5
			#end:case
			case 4:
				saladin._send(
					'view:', 737,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', 160, 123,
					'setPri:', 0,
					'sightAngle:', 180,
					'init:'
				)
				throneDoor._send('startUpd:', 'cel:', 2, 'stopUpd:')
				global0._send(
					'setCycle:', Rev,
					'setLoop:', -1,
					'setLoop:', 6,
					'setMotion:', MoveTo, 141, 131, self
				)
			#end:case
			case 5:
				global0._send('setCycle:', StopWalk, -1)
				saladin._send('setCycle:', CT, 2, 1, self)
			#end:case
			case 6:
				kernel.DisposeScript(969)
				global105._send('number:', 901, 'loop:', 1, 'play:')
				saladin._send('setCycle:', End, self)
				throneDoor._send('setCycle:', End)
			#end:case
			case 7:
				cycles = 20
			#end:case
			case 8:
				global105._send('stop:')
				saladin._send('setLoop:', 7, 'cel:', 9, 'setPri:', 9, 'setCycle:', Beg, self)
				global105._send('number:', 652, 'setLoop:', 1, 'play:')
				throneDoor._send('setCycle:', Beg, throneDoor)
			#end:case
			case 9:
				register = (11 if proc913_0(72) else 10)
				global91._send('say:', 1, 0, register, 0, self)
			#end:case
			case 10:
				global1._send('handsOn:')
				if kernel.HaveMouse():
					seconds = 11
				else:
					seconds = 21
				#endif
			#end:case
			case 11:
				global1._send('handsOff:')
				register = (13 if proc913_0(72) else 12)
				global91._send('say:', 1, 0, register, 0, self)
			#end:case
			case 12:
				global0._send('hide:')
				saladin._send('setLoop:', 1, 'cel:', 0, 'posn:', 140, 133, 'setCycle:', End, self)
			#end:case
			case 13:
				global0._send(
					'view:', 737,
					'normal:', 0,
					'setLoop:', 2,
					'cel:', 0,
					'x:', 121,
					'y:', 134,
					'setScale:', 0,
					'setCycle:', Walk,
					'setSpeed:', 8,
					'setStep:', 3, 2,
					'show:',
					'setMotion:', MoveTo, 99, 135, self
				)
				saladin._send(
					'setLoop:', 3,
					'cel:', 0,
					'posn:', 149, 134,
					'setSpeed:', 8,
					'setStep:', 3, 2,
					'setCycle:', Walk,
					'setMotion:', MoveTo, 128, 134
				)
			#end:case
			case 14:
				global0._send('setLoop:', 5, 'cel:', 0)
				saladin._send('setMotion:', MoveTo, 128, 134, self)
			#end:case
			case 15:
				global102._send('number:', 705, 'setLoop:', 1, 'play:')
				saladin._send('setLoop:', 4, 'cel:', 0, 'setCycle:', End, self)
				global103._send('number:', 756, 'setLoop:', 1, 'play:')
			#end:case
			case 16:
				saladin._send('cycleSpeed:', 8, 'setCycle:', CT, 2, -1, self)
			#end:case
			case 17:
				global0._send('setLoop:', 8, 'cel:', 0, 'cycleSpeed:', 5, 'setCycle:', CT, 3, 1, self)
			#end:case
			case 18:
				cycles = 10
			#end:case
			case 19:
				global103._send('number:', 971, 'setLoop:', 1, 'play:', self)
				global0._send('cycleSpeed:', 8, 'setCycle:', End, self)
			#end:case
			case 20:
				proc0_1(32)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class exitBaseScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('setMotion:', PolyPath, 173, 127, self)
			#end:case
			case 1:
				global0._send('setHeading:', 225, self)
			#end:case
			case 2:
				global0._send(
					'normal:', 0,
					'view:', 881,
					'loop:', 2,
					'cel:', 0,
					'x:', 158,
					'y:', 132,
					'setScale:',
					'scaleX:', 90,
					'scaleY:', 90,
					'cycleSpeed:', 8,
					'setCycle:', End, self
				)
			#end:case
			case 3:
				seconds = 3
			#end:case
			case 4:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 5:
				global0._send('posn:', 173, 127, 'reset:', 5, 'setSpeed:', 8)
				cycles = 3
			#end:case
			case 6:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class exitUpstairsScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cycles = 2
			#end:case
			case 1:
				global91._send('say:', 1, 0, 8, 1, self)
			#end:case
			case 2:
				global0._send('setSpeed:', 8, 'setMotion:', PolyPath, 19, 166, self)
			#end:case
			case 3:
				global0._send('setHeading:', 135, self)
			#end:case
			case 4:
				cycles = 4
			#end:case
			case 5:
				global1._send('handsOff:')
				global0._send(
					'normal:', 0,
					'setScale:',
					'scaleX:', 144,
					'scaleY:', 144,
					'view:', 881,
					'loop:', 3,
					'cel:', 4,
					'x:', 38,
					'y:', 175,
					'cycleSpeed:', 8,
					'setCycle:', End, self
				)
			#end:case
			case 6:
				global91._send('say:', 1, 0, 8, 2, self)
			#end:case
			case 7:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 8:
				global0._send('reset:', 4, 'posn:', 19, 166, 'setSpeed:', 8)
				cycles = 4
			#end:case
			case 9:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class showLetter(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				kernel.ScriptID(80, 0)._send('setFlag:', 709, 1024)
				global1._send('givePoints:', 3)
				roomConv._send('add:', -1, 6, 61, 21, 1, 'add:', -1, 6, 61, 21, 2, 'init:', self)
			#end:case
			case 1:
				global0._send('hide:')
				saladin._send(
					'setLoop:', 6,
					'cel:', 0,
					'setPri:', 9,
					'posn:', 140, 133,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				roomConv._send('add:', -1, 6, 61, 21, 3, 'init:', self)
			#end:case
			case 3:
				seconds = 3
			#end:case
			case 4:
				roomConv._send('add:', -1, 6, 61, 21, 4, 'init:', self)
			#end:case
			case 5:
				saladin._send('setCycle:', Beg, self)
			#end:case
			case 6:
				roomConv._send(
					'add:', -1, 6, 61, 21, 5,
					'add:', -1, 6, 61, 21, 6,
					'add:', -1, 6, 61, 21, 7,
					'init:', self
				)
			#end:case
			case 7:
				global0._send('show:')
				saladin._send('setLoop:', 7, 'cel:', 0, 'posn:', 160, 123, 'setCycle:', End, self)
				global105._send('number:', 652, 'setLoop:', 1, 'play:')
			#end:case
			case 8:
				roomConv._send('add:', -1, 6, 61, 21, 8, 'add:', -1, 6, 61, 21, 9)
				if proc913_0(72):
					roomConv._send('add:', -1, 6, 61, 20, 1)
				else:
					roomConv._send('add:', -1, 6, 61, 21, 10)
				#endif
				roomConv._send('init:', self)
			#end:case
			case 9:
				global0._send('put:', 20)
				cycles = 1
			#end:case
			case 10:
				saladin._send(
					'view:', 736,
					'loop:', 4,
					'cel:', 2,
					'scaleSignal:', 1,
					'scaleX:', 87,
					'scaleY:', 87,
					'x:', (saladin._send('x:') + 1),
					'y:', (saladin._send('y:') + 3)
				)
				cycles = 8
			#end:case
			case 11:
				saladin._send('cel:', 0)
				cycles = 8
			#end:case
			case 12:
				saladin._send('cel:', 3)
				cycles = 8
			#end:case
			case 13:
				throneDoor._send('setCycle:', End, self)
				global105._send('number:', 901, 'setLoop:', 1, 'play:')
			#end:case
			case 14:
				saladin._send(
					'setLoop:', 3,
					'setCycle:', Walk,
					'setMotion:', MoveTo, 167, 123, self
				)
			#end:case
			case 15:
				saladin._send('loop:', 4, 'cel:', 3, 'stopUpd:')
				global0._send('setMotion:', MoveTo, 152, 128, self)
			#end:case
			case 16:
				global0._send('setMotion:', MoveTo, 152, 122, self)
			#end:case
			case 17:
				cycles = 4
			#end:case
			case 18:
				global2._send('newRoom:', 740)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class enterThroneRoom(Script):
	#property vars (may be empty)
	@classmethod
	def doit():
		if (local1 & 0x1000):
			global2._send('newRoom:', 740)
		#endif
		super._send('doit:')
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global105._send('number:', 901, 'loop:', 1, 'play:')
				throneDoor._send('setCycle:', End, self)
			#end:case
			case 1:
				global105._send('stop:')
				proc80_2(1)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class followEgoIn(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cycles = 2
			#end:case
			case 1:
				global102._send('stop:')
				global102._send('number:', 700, 'loop:', -1, 'play:', 80, 'fade:', 127, 25, 10, 0)
				cycles = 10
			#end:case
			case 2:
				kernel.ScriptID(80, 5)._send('setMotion:', MoveTo, 59, 68, self)
				kernel.ScriptID(80, 6)._send('setMotion:', MoveTo, 69, 68, self)
			#end:case
			case 3: 0#end:case
			case 4:
				global102._send('number:', 710, 'loop:', -1, 'play:')
				global91._send('say:', 1, 0, 2, 1, self)
			#end:case
			case 5:
				global91._send('say:', 1, 0, 2, 2, self)
			#end:case
			case 6:
				global2._send('moveOtherGuard:', 1)
				kernel.ScriptID(80, 5)._send('setScript:', kernel.ScriptID(80, 4), self, 1)
			#end:case
			case 7:
				global91._send('say:', 1, 0, 2, 3, self, 'oneOnly:', 0)
			#end:case
			case 8:
				global102._send('fade:')
				global2._send('newRoom:', 820)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class tryToOpenDoor(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				cycles = 3
			#end:case
			case 1:
				global0._send(
					'view:', 730,
					'loop:', 4,
					'cel:', 0,
					'normal:', 0,
					'setScale:', 0,
					'scaleX:', 128,
					'scaleY:', 128,
					'cycleSpeed:', 8,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 3:
				global91._send('say:', 7, 5, 0, 0, self)
			#end:case
			case 4:
				global0._send('reset:', 0)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class throneDoor(Prop):
	#property vars (may be empty)
	x = 160
	y = 100
	noun = 9
	approachX = 155
	approachY = 129
	view = 730
	
	@classmethod
	def init():
		super._send('init:', &rest)
		if ((not local2) and (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2))):
			self._send('approachVerbs:', 5)
		#endif
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		return (super._send('onMe:', param1) and (param1._send('y:') <= 127))
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				if ((not local3) or local2):
					local3.post('++')
					if 
						(and
							(not local2)
							(not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2))
						)
						(_approachVerbs |= global66._send('doit:', 1))
					#endif
					global91._send('say:', 9, 1, 25)
				else:
					global91._send('say:', noun, param1, 26, 1, kernel.ScriptID(82))
					global2._send(
						'setScript:', kernel.ScriptID(82)._send('start:', -1, 'yourself:'), 0, lookIntoThroneRoom
					)
				#endif
			#end:case
			case 5:
				if local2:
					global91._send('say:', 7, 5, 22)
				else:
					global2._send('setScript:', enterThroneRoom)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1)
			#end:else
		#end:match
	#end:method

	@classmethod
	def cue():
		self._send('stopUpd:')
	#end:method

#end:class or instance

@SCI.instance
class lookIntoThroneRoom(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		tempGuard1._send('dispose:')
		tempGuard2._send('dispose:')
		super._send('dispose:')
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				kernel.ScriptID(82, 1)._send('noun:', 5, 'init:', 794)
				tempGuard1._send('init:', 'stopUpd:')
				tempGuard2._send('view:', kernel.ScriptID(80, 6)._send('view:'), 'init:', 'stopUpd:')
				cycles = 4
			#end:case
			case 1:
				global91._send('say:', 9, 1, 26, 2)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class tempGuard1(View):
	#property vars (may be empty)
	x = 148
	y = 128
	noun = 5
	view = 724
	loop = 4
	priority = 14
	signal = 16400
	scaleSignal = 1
	
#end:class or instance

@SCI.instance
class tempGuard2(View):
	#property vars (may be empty)
	x = 167
	y = 126
	noun = 5
	loop = 4
	cel = 1
	priority = 14
	signal = 16400
	scaleSignal = 1
	
#end:class or instance

@SCI.instance
class kitchenDoor(Prop):
	#property vars (may be empty)
	x = 70
	y = 143
	z = 28
	noun = 8
	approachX = 79
	approachY = 142
	view = 730
	loop = 1
	signal = 16384
	
	@classmethod
	def init():
		super._send('init:', &rest)
		if ((not local2) and (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2))):
			self._send('approachVerbs:', 5)
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				if local2:
					global91._send('say:', 7, 5, 22)
				else:
					global2._send('setScript:', doKitchen)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class basementDoor(Prop):
	#property vars (may be empty)
	x = 250
	y = 119
	noun = 7
	approachX = 228
	approachY = 144
	view = 730
	loop = 2
	
	@classmethod
	def init():
		super._send('init:', &rest)
		if ((not local2) and (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2))):
			self._send('approachVerbs:', 5)
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				if local2:
					global91._send('say:', 7, 5, 22)
				else:
					global2._send('setScript:', tryToOpenDoor)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class candles(Prop):
	#property vars (may be empty)
	x = 161
	y = 39
	onMeCheck = 0
	view = 730
	loop = 3
	priority = 15
	signal = 16400
	
#end:class or instance

@SCI.instance
class saladin(Actor):
	#property vars (may be empty)
	x = 115
	y = 166
	noun = 6
	view = 736
	loop = 1
	signal = 16384
	
	@classmethod
	def doVerb(param1 = None, *rest):
		(cond
			case local2:
				if (param1 == 1):
					if proc913_0(72):
						global91._send('say:', noun, param1, 18)
					else:
						global91._send('say:', noun, param1, 19)
					#endif
				else:
					global91._send('say:', 6, 5, 22)
				#endif
			#end:case
			case (param1 == 61):
				global2._send('setScript:', showLetter)
			#end:case
			case proc999_5(param1, 1, 2):
				if proc913_0(72):
					global91._send('say:', noun, param1, 20)
				else:
					global91._send('say:', noun, param1, 21)
				#endif
			#end:case
			case proc999_5(param1, 5, 8, 18, 65, 33, 16):
				global91._send('say:', noun, param1, 23)
			#end:case
			else:
				global91._send('say:', 6, 0, 23)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class urns(Feature):
	#property vars (may be empty)
	y = 163
	onMeCheck = 2
	
	@classmethod
	def onMe(param1 = None, *rest):
		(return
			(and
				super._send('onMe:', param1)
				x = param1._send('x:')
				(((param1._send('x:') > 160) and noun = 13) or noun = 12)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class chandelier(Feature):
	#property vars (may be empty)
	x = 160
	y = 160
	noun = 14
	onMeCheck = 4
	
#end:class or instance

@SCI.instance
class balconyFtr(Feature):
	#property vars (may be empty)
	noun = 16
	onMeCheck = 128
	
#end:class or instance

@SCI.instance
class pillarsFtr(Feature):
	#property vars (may be empty)
	noun = 15
	onMeCheck = 256
	
	@classmethod
	def onMe(param1 = None, *rest):
		x = param1._send('x:')
		y = 0
		(return
			(and
				(or
					super._send('onMe:', param1)
					proc999_4(50, 59, 66, 70, param1)
					proc999_4(254, 62, 271, 70, param1)
				)
				y = localproc_0(256, x, 116)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class stairs(Feature):
	#property vars (may be empty)
	noun = 11
	onMeCheck = 1040
	
	@classmethod
	def onMe(param1 = None, *rest):
		x = y = 0
		return (super._send('onMe:', param1) and x = param1._send('x:') and y = param1._send('y:'))
	#end:method

#end:class or instance

@SCI.instance
class roomConv(Conversation):
	#property vars (may be empty)
#end:class or instance

