#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 660
import sci_sh
import kernel
import Main
import rgDead
import KQ6Room
import n913
import Scaler
import PolyPath
import Polygon
import Feature
import Sound
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm660 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = [18, 73, 2, 69, 50, 0, 135, 46, 1, 223, 48, 1, 291, 48, 1, 277, 83, 3, 0]
local20 = [26, 159, 5, 69, 82, 6, 136, 63, 7, 224, 67, 7, 291, 64, 8, 0]
local36 = [69, 46, 0, 135, 43, 1, 222, 45, 2, 291, 46, 3, 0]


@SCI.instance
class rm660(KQ6Room):
	#property vars (may be empty)
	noun = 4
	picture = 660
	south = 650
	
	@classmethod
	def init():
		self._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 0, 189, 0, -10, 319, -10, 319, 174, 241, 159, 236, 146, 187, 147, 107, 151, 81, 159, 102, 167, 116, 173, 108, 179, 75, 189,
					'yourself:'
				)
		)
		super._send('init:', &rest)
		global0._send(
			'posn:', 160, 180,
			'setPri:', 12,
			'setScale:', Scaler, 100, 64, 189, 74,
			'actions:', egoActions,
			'init:'
		)
		riverStyx._send('init:')
		boat._send('addToPic:')
		charon._send(
			'posn:', (boat._send('x:') - 79), (boat._send('y:') + 36),
			'ignoreActors:', 1,
			'init:',
			'stopUpd:'
		)
		spiritFeat._send('init:')
		proc70_1(torch, @local1)
		proc70_1(shimmer, @local20)
		proc70_1(glow, @local36)
		global5._send('eachElementDo:', #checkDetail)
		global1._send('handsOn:')
	#end:method

#end:class or instance

@SCI.instance
class fx(Sound):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class splashSound(Sound):
	#property vars (may be empty)
	number = 923
	
#end:class or instance

@SCI.instance
class swimScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('setMotion:', PolyPath, 99, 182, self)
			#end:case
			case 1:
				global102._send('number:', 653, 'loop:', 1, 'play:')
				global0._send(
					'normal:', 0,
					'view:', 665,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', 89, 187,
					'setCycle:', CT, 6, 1, self
				)
			#end:case
			case 2:
				splashSound._send('play:')
				global0._send('setCycle:', End, self)
			#end:case
			case 3:
				global0._send('dispose:')
				cycles = 2
			#end:case
			case 4:
				global91._send('say:', 3, 3, 0, 1, self)
			#end:case
			case 5:
				global91._send('say:', 3, 3, 0, 2, self)
			#end:case
			case 6:
				proc0_1(31)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class missedCharonScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cycles = 2
			#end:case
			case 1:
				global91._send('say:', 6, 0, 9, 1, self)
			#end:case
			case 2:
				global102._send('number:', 601, 'loop:', 1, 'play:')
				if 
					(>
						kernel.GetDistance(global0._send('x:'), global0._send('y:'), charon._send(
							'x:'
						), charon._send('y:'))
						40
					)
					global0._send('setMotion:', PolyPath, 114, 160, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 3:
				global91._send('say:', 6, 0, 9, 2, self)
			#end:case
			case 4:
				charon._send('view:', 667, 'setLoop:', 0, 'setCycle:', End, self)
				global103._send('number:', 662, 'loop:', 1, 'play:')
			#end:case
			case 5:
				charon._send('setLoop:', 1, 'setCycle:', Fwd)
				global0._send(
					'normal:', 0,
					'view:', 749,
					'setLoop:', 3,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 6:
				global0._send('setLoop:', 5, 'cel:', 0, 'setCycle:', End)
				charon._send('setLoop:', 0)
				charon._send('cel:', charon._send('lastCel:'), 'setCycle:', Beg, self)
			#end:case
			case 7:
				global91._send('say:', 6, 0, 9, 3, self)
			#end:case
			case 8:
				proc0_1(39)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class buyTransportScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send(
					'illegalBits:', 0,
					'ignoreActors:', 1,
					'setMotion:', MoveTo, 106, 147, self
				)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				global91._send('say:', 2, 7, 0, 1, self)
			#end:case
			case 3:
				global1._send('givePoints:', 3)
				global0._send(
					'normal:', 0,
					'put:', 7, -1,
					'view:', 661,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', 110, 150,
					'setCycle:', End, self
				)
				charon._send('setCycle:', End)
			#end:case
			case 4:
				fx._send('number:', 661, 'loop:', 1, 'play:')
				global0._send(
					'reset:', 7,
					'setPri:', 12,
					'posn:', (global0._send('x:') - 2), (global0._send('y:') - 1)
				)
				charon._send('setCycle:', Beg, self)
			#end:case
			case 5:
				seconds = 1
			#end:case
			case 6:
				global91._send('say:', 2, 7, 0, 2, self)
			#end:case
			case 7:
				seconds = 1
			#end:case
			case 8:
				global0._send('setMotion:', MoveTo, 124, 144, self)
			#end:case
			case 9:
				global0._send(
					'normal:', 0,
					'view:', 661,
					'setLoop:', 1,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 10:
				ticks = 15
			#end:case
			case 11:
				boat._send('dispose:')
				charon._send('view:', 668, 'setLoop:', 0, 'cel:', 0, 'setCycle:', End, self)
				kernel.UnLoad(128, 663)
			#end:case
			case 12:
				global0._send('setPri:', -1, 'dispose:')
				charon._send('dispose:')
				if global169:
					kernel.DrawPic(660, 15)
				else:
					global2._send('drawPic:', 660)
				#endif
				boat._send(
					'signal:', 16384,
					'ignoreActors:', 1,
					'view:', 662,
					'setLoop:', 0,
					'cel:', 0,
					'setScale:', Scaler, 100, 50, 137, 59,
					'init:'
				)
				kernel.UnLoad(128, 668)
				kernel.UnLoad(128, 661)
				ticks = 10
			#end:case
			case 13:
				boat._send('cel:', 1)
				ticks = 10
			#end:case
			case 14:
				boat._send('setLoop:', 1, 'cel:', 0)
				ticks = 10
			#end:case
			case 15:
				boat._send('cel:', 1)
				ticks = 10
			#end:case
			case 16:
				boat._send('view:', 6621, 'setLoop:', 0, 'cel:', 0)
				ticks = 10
			#end:case
			case 17:
				boat._send(
					'ignoreActors:', 1,
					'ignoreHorizon:', 1,
					'setPri:', 3,
					'setMotion:', MoveTo, 345, 63, self
				)
			#end:case
			case 18:
				global2._send('newRoom:', 670)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getWaterScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('setMotion:', MoveTo, 119, 184, self)
			#end:case
			case 1:
				global0._send(
					'normal:', 0,
					'view:', 666,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', 110, 189,
					'setCycle:', CT, 3, 1, self
				)
			#end:case
			case 2:
				fx._send('number:', 924, 'loop:', 1, 'play:')
				global0._send('setCycle:', End, self)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				global91._send('say:', 3, 44, (4 if proc913_0(68) else 3), 0, self)
			#end:case
			case 5:
				global0._send('reset:', 1, 'setPri:', 12, 'posn:', 119, 184)
				cycles = 1
			#end:case
			case 6:
				kernel.UnLoad(128, 666)
				proc913_1(58)
				global1._send('givePoints:', 1)
				self._send('dispose:')
				global1._send('handsOn:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class playFlute(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				self._send('setScript:', kernel.ScriptID(85, 0), self)
			#end:case
			case 1:
				global91._send('say:', 8, 31, 0, 0, self)
			#end:case
			case 2:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class playNightingale(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				self._send('setScript:', kernel.ScriptID(93, 0), self)
			#end:case
			case 1:
				global91._send('say:', 8, 37, 0, 0, self)
			#end:case
			case 2:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class tryToBoardScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if 
					(>
						kernel.GetDistance(global0._send('x:'), global0._send('y:'), charon._send(
							'x:'
						), charon._send('y:'))
						20
					)
					global0._send('setMotion:', MoveTo, 112, 149, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				proc913_4(global0, charon, self)
			#end:case
			case 2:
				charonHead._send(
					'posn:', (charon._send('x:') - 5), (charon._send('y:') - 43),
					'init:',
					'setCycle:', Fwd
				)
				cycles = 15
			#end:case
			case 3:
				charonHead._send('dispose:')
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class talkCharonScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if 
					(>
						kernel.GetDistance(global0._send('x:'), global0._send('y:'), charon._send(
							'x:'
						), charon._send('y:'))
						20
					)
					global0._send('setMotion:', MoveTo, 112, 149, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				proc913_4(global0, charon, self)
			#end:case
			case 2:
				global91._send('say:', 2, register, 0, 1, self)
			#end:case
			case 3:
				if (charon._send('cel:') != 3):
					charon._send('setCycle:', End, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 4:
				charonHead._send(
					'posn:', (charon._send('x:') - 5), (charon._send('y:') - 43),
					'init:',
					'setCycle:', Fwd
				)
				cycles = 15
			#end:case
			case 5:
				if proc999_5(register, 48, 2, 37):
					global91._send('say:', 2, register, 0, 2, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 6:
				charonHead._send('dispose:')
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class charonHead(Prop):
	#property vars (may be empty)
	view = 663
	loop = 2
	priority = 12
	signal = 16400
	
#end:class or instance

@SCI.instance
class torch(Prop):
	#property vars (may be empty)
	noun = 7
	view = 660
	loop = 8
	priority = 5
	signal = 16400
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class shimmer(Prop):
	#property vars (may be empty)
	noun = 3
	view = 660
	loop = 5
	priority = 1
	signal = 16400
	detailLevel = 1
	
	@classmethod
	def doVerb(param1 = None, *rest):
		riverStyx._send('doVerb:', param1, &rest)
	#end:method

#end:class or instance

@SCI.instance
class glow(Prop):
	#property vars (may be empty)
	noun = 4
	view = 664
	signal = 16400
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class spiritFeat(Feature):
	#property vars (may be empty)
	noun = 5
	
	@classmethod
	def init():
		(= onMeCheck
			(= local0
				Polygon._send('new:')._send(
					'type:', 0,
					'init:', 132, 117, 138, 121, 151, 124, 169, 115, 186, 122, 193, 130, 185, 139, 177, 141, 119, 142, 119, 131, 127, 119,
					'yourself:'
				)
			)
		)
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class boat(Actor):
	#property vars (may be empty)
	x = 156
	y = 108
	noun = 1
	view = 663
	illegalBits = 0
	
	@classmethod
	def init():
		super._send('init:', &rest)
		global93._send('addToFront:', self)
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		global93._send('delete:', self)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		(cond
			case (param1._send('type:') & 0x1000):
				super._send('handleEvent:', param1)
			#end:case
			case spiritFeat._send('onMe:', param1):
				spiritFeat._send('handleEvent:', param1)
			#end:case
			else:
				super._send('handleEvent:', param1)
			#end:else
		)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 3:
				global1._send('handsOff:')
				global2._send('setScript:', tryToBoardScript)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class charon(Actor):
	#property vars (may be empty)
	noun = 2
	view = 663
	loop = 1
	
	@classmethod
	def init():
		super._send('init:', &rest)
		(cond
			case (kernel.ScriptID(0, 6)._send('client:') == kernel.ScriptID(70, 0)): 0#end:case
			case proc913_0(121):
				global1._send('handsOff:')
				global2._send('setScript:', missedCharonScript)
			#end:case
			else:
				kernel.ScriptID(0, 6)._send('setReal:', kernel.ScriptID(70, 0), 0, 2, 0)
			#end:else
		)
		global93._send('addToFront:', self)
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		global93._send('delete:', self)
	#end:method

	@classmethod
	def doit():
		super._send('doit:')
		(cond
			case global2._send('script:'): 0#end:case
			case proc913_0(121):
				global1._send('handsOff:')
				global2._send('setScript:', missedCharonScript)
			#end:case
			case ((self._send('distanceTo:', global0) < 40) and (cel != 3) and (not cycler)):
				self._send('setCycle:', End)
			#end:case
			case ((self._send('distanceTo:', global0) > 40) and cel and (not cycler)):
				self._send('setCycle:', Beg)
			#end:case
		)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 7:
				global1._send('handsOff:')
				kernel.ScriptID(0, 6)._send('dispose:')
				global2._send('setScript:', buyTransportScr)
			#end:case
			case 3:
				global1._send('handsOff:')
				global2._send('setScript:', tryToBoardScript)
			#end:case
			case 31:
				global1._send('handsOff:')
				global2._send('setScript:', playFlute)
			#end:case
			case 37:
				global1._send('handsOff:')
				global2._send('setScript:', playNightingale)
			#end:case
			else:
				if proc999_5(param1, 2, 5, 1, 13, 28, 8, 30, 48, 50, 16, 35):
					global1._send('handsOff:')
					global2._send('setScript:', talkCharonScript, 0, param1)
				else:
					global1._send('handsOff:')
					global2._send('setScript:', talkCharonScript, 0, 0)
				#endif
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class riverStyx(Feature):
	#property vars (may be empty)
	noun = 3
	onMeCheck = 2
	
	@classmethod
	def init():
		super._send('init:', &rest)
		global93._send('addToFront:', self)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 44:
				if (not proc913_0(58)):
					global1._send('handsOff:')
					global2._send('setScript:', getWaterScr)
				else:
					global91._send('say:', noun, param1, 5)
				#endif
			#end:case
			case 3:
				global1._send('handsOff:')
				global2._send('setScript:', swimScr)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		global93._send('delete:', self)
	#end:method

#end:class or instance

@SCI.instance
class egoActions(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 31:
				global1._send('handsOff:')
				global2._send('setScript:', playFlute)
			#end:case
			case 37:
				global1._send('handsOff:')
				global2._send('setScript:', playNightingale)
			#end:case
			else:
				return 0
			#end:else
		#end:match
	#end:method

#end:class or instance

