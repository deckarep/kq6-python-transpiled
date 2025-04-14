#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 406
import sci_sh
import kernel
import Main
import rLab
import n402
import n913
import RandCycle
import PolyPath
import Polygon
import Feature
import LoadMany
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm406 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = 10


@SCI.instance
class rm406(LabRoom):
	#property vars (may be empty)
	south = 400
	west = 400
	
	@classmethod
	def init():
		kernel.ScriptID(30, 0)._send('labCoords:', 152)
		if ((global12 == 435) and (not proc913_0(1))):
			proc958_0(128, 391, 392, 393, 432)
			kernel.Load(139, 400)
			global2._send('picture:', 98)
			global102._send('stop:')
			super._send('init:')
			kernel.ScriptID(30, 0)._send('cue:')
			global0._send(
				'normal:', 0,
				'view:', 433,
				'x:', 165,
				'y:', 95,
				'ignoreHorizon:',
				'actions:', egoDoTinderBoxCode,
				'init:'
			)
			kernel.UnLoad(128, 900)
			global2._send('setScript:', timerMinotaurKillEgo)
		else:
			global2._send('picture:', 400)
			proc402_4()
			super._send('init:')
			kernel.ScriptID(30, 3)._send('init:')
			kernel.ScriptID(30, 5)._send('addToPic:')
			kernel.ScriptID(30, 9)._send('addToPic:')
			kernel.ScriptID(30, 0)._send('initCrypt:', 1)
			if (global12 == 435):
				global2._send('setScript:', fallDownInLight)
			else:
				global2._send('setScript:', kernel.ScriptID(30, 1))
			#endif
		#endif
	#end:method

	@classmethod
	def notify():
		kernel.ScriptID(30, 5)._send('addToPic:')
		kernel.ScriptID(30, 9)._send('addToPic:')
		kernel.ScriptID(30, 3)._send('init:', 'show:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		(return
			match param1
				case 20:
					if kernel.ScriptID(30, 0)._send('darkRoomLit:'):
						global91._send('say:', 3, 20, 37, 1, 0, 400)
						1
					else:
						global2._send('setScript:', lightItUp)
						1
					#endif
				#end:case
				case 1:
					if kernel.ScriptID(30, 0)._send('darkRoomLit:'):
						super._send('doVerb:', param1, &rest)
						1
					else:
						global91._send('say:', 2, 1, 36, 1, 0, 400)
						1
					#endif
				#end:case
				case 2:
					if kernel.ScriptID(30, 0)._send('darkRoomLit:'):
						super._send('doVerb:', param1, &rest)
						1
					else:
						global91._send('say:', 2, 2, 36, 0, 0, 400)
						1
					#endif
				#end:case
				case 5:
					if kernel.ScriptID(30, 0)._send('darkRoomLit:'):
						super._send('doVerb:', param1, &rest)
						1
					else:
						global91._send('say:', 2, 5, 36, 1, 0, 400)
						1
					#endif
				#end:case
				else:
					global91._send('say:', 3, 0, 36, 1, 0, 400)
					1
				#end:else
			#end:match
		)
	#end:method

	@classmethod
	def scriptCheck():
		temp0 = 0
		if (local1 < 100):
			global91._send('say:', 3, 0, 36, 1, 0, 400)
		else:
			temp0 = 1
		#endif
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class bigEyes(View):
	#property vars (may be empty)
	view = 433
	loop = 6
	priority = 15
	signal = 16400
	
#end:class or instance

@SCI.instance
class fallDownInLight(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global105._send('number:', 960, 'setLoop:', 1, 'play:')
				global0._send(
					'setSpeed:', 6,
					'posn:', 151, 153,
					'view:', 307,
					'loop:', 4,
					'cel:', 0,
					'normal:', 0,
					'init:'
				)
				cycles = 8
			#end:case
			case 1:
				global0._send('setCycle:', End, self)
			#end:case
			case 2:
				global0._send('posn:', 181, 157, 'reset:', 5)
				kernel.UnLoad(128, 307)
				cycles = 6
			#end:case
			case 3:
				global91._send('say:', 1, 0, 34, 0, self, 400)
			#end:case
			case 4:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lightItUp(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global2._send('obstacles:')._send('dispose:')
				global105._send('number:', 932, 'setLoop:', 1, 'play:')
				global0._send(
					'view:', 391,
					'x:', (global0._send('x:') + 7),
					'normal:', 0,
					'setLoop:', 2,
					'cel:', 0,
					'cycleSpeed:', 12,
					'setCycle:', End, self
				)
			#end:case
			case 1:
				global91._send('say:', 3, 20, 36, 1, self, 400)
			#end:case
			case 2:
				global1._send('givePoints:', 2)
				proc402_4()
				global0._send(
					'view:', 3931,
					'setLoop:', 6,
					'cel:', 0,
					'cycleSpeed:', 4,
					'setCycle:', End, self
				)
				kernel.UnLoad(128, 391)
			#end:case
			case 3:
				global0._send(
					'view:', 3931,
					'setLoop:', 5,
					'cel:', 0,
					'cycleSpeed:', 4,
					'setCycle:', End, self
				)
			#end:case
			case 4:
				global0._send(
					'view:', 392,
					'setLoop:', 1,
					'cycleSpeed:', 1,
					'setCycle:', Walk,
					'setMotion:', PolyPath, 125, 142, self
				)
				0
				kernel.UnLoad(128, 3931)
			#end:case
			case 5:
				global91._send('say:', 3, 20, 36, 2, self, 400)
			#end:case
			case 6:
				global103._send('fade:', 0, 10, 10)
				global102._send(
					'number:', 400,
					'setLoop:', -1,
					'setVol:', 0,
					'play:',
					'fade:', 127, 10, 10
				)
				global0._send(
					'view:', 432,
					'setLoop:', 0,
					'cel:', 0,
					'cycleSpeed:', 6,
					'setCycle:', End
				)
				kernel.UnLoad(128, 392)
				self._send('setScript:', shiftThePalette, self)
			#end:case
			case 7:
				global91._send('say:', 3, 20, 36, 3, self, 400)
			#end:case
			case 8:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class shiftThePalette(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				kernel.Palette(1, 400)
				global2._send('picture:', 400)
				global2._send('drawPic:', 400, (15 if global169 else 100))
				kernel.Palette(4, 77, 255, local1)
				ticks = 4
			#end:case
			case 1:
				kernel.ScriptID(30, 5)._send('addToPic:')
				kernel.ScriptID(30, 9)._send('addToPic:')
				kernel.ScriptID(30, 3)._send('init:')
				kernel.ScriptID(30, 0)._send('darkRoomLit:', 1, 'notify:')
				ticks = 2
			#end:case
			case 2:
				if (local1 == 100):
					(state += 2)
					self._send('cue:')
				else:
					ticks = 2
				#endif
			#end:case
			case 3:
				if (local1 == 30):
					global0._send(
						'posn:', (global0._send('x:') + 4), (global0._send('y:') - 2),
						'reset:', 1
					)
					kernel.UnLoad(128, 432)
				#endif
				kernel.Palette(4, 77, 255, local1)
				ticks = 2
			#end:case
			case 4:
				if (local1 < 100):
					(local1 += 5)
					(state -= 2)
				#endif
				self._send('cue:')
			#end:case
			case 5:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class timerMinotaurKillEgo(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('setStep:', 3, 15, 'setMotion:', MoveTo, 165, 160, self)
			#end:case
			case 1:
				global102._send('stop:')
				global103._send('number:', 405, 'setLoop:', -1, 'play:')
				global0._send('hide:')
				kernel.ShakeScreen(4, kernel.Random(0, 2))
				seconds = 1
			#end:case
			case 2:
				global2._send(
					'addObstacle:', Polygon._send('new:')._send(
							'type:', 3,
							'init:', 231, 145, 82, 145, 28, 183, 285, 183,
							'yourself:'
						)
				)
				global0._send('show:', 'cycleSpeed:', 46, 'setCycle:', RandCycle)
				seconds = 4
			#end:case
			case 3:
				global0._send(
					'setLoop:', 1,
					'setStep:', 6, 10,
					'cel:', 0,
					'cycleSpeed:', 6,
					'setCycle:', End, self
				)
			#end:case
			case 4:
				(cond
					case proc913_0(1):
						global91._send('say:', 1, 0, 34, 1, self, 400)
					#end:case
					case (global12 == 400):
						self._send('cue:')
					#end:case
					else:
						global91._send('say:', 1, 0, 31, 0, self, 400)
					#end:else
				)
			#end:case
			case 5:
				if ((global12 == 400) and (not proc913_0(1))):
					global91._send('say:', 1, 0, 33, 1, self, 400)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 6:
				global0._send('setLoop:', 2, 'cycleSpeed:', 24, 'setCycle:', RandCycle)
				seconds = 4
			#end:case
			case 7:
				global1._send('handsOn:')
				if proc913_0(1):
					self._send('dispose:')
				else:
					self._send('setScript:', lookAround, self)
				#endif
			#end:case
			case 8:
				cycles = 4
			#end:case
			case 9:
				global1._send('handsOff:')
				global104._send('number:', 401, 'setLoop:', 1, 'play:', self)
			#end:case
			case 10:
				global105._send('number:', 433, 'setLoop:', 1, 'play:')
				cycles = 10
			#end:case
			case 11:
				global91._send('say:', 1, 0, 32, 1, self, 400)
			#end:case
			case 12:
				bigEyes._send('posn:', global0._send('x:'), (global0._send('y:') - 48), 'init:')
				global0._send('hide:')
				seconds = 2
			#end:case
			case 13:
				global91._send('say:', 1, 0, 32, 2, self, 400)
			#end:case
			case 14:
				bigEyes._send('dispose:')
				kernel.UnLoad(128, 433)
				global91._send('say:', 1, 0, 32, 3, self, 400)
			#end:case
			case 15:
				global103._send('stop:')
				global102._send('number:', 406, 'setLoop:', -1, 'play:')
				global0._send('setLoop:', 4, 'cycleSpeed:', 0, 'cel:', 0, 'show:', 'setCycle:', Fwd)
				seconds = 1
			#end:case
			case 16:
				global0._send('posn:', (global0._send('x:') + 30), global0._send('y:'))
				seconds = 1
			#end:case
			case 17:
				global0._send('posn:', (global0._send('x:') - 30), global0._send('y:'))
				seconds = 1
			#end:case
			case 18:
				global0._send('posn:', (global0._send('x:') + 30), global0._send('y:'))
				seconds = 1
			#end:case
			case 19:
				global0._send('setLoop:', 4, 'setCycle:', End, self)
			#end:case
			case 20:
				global102._send('number:', 430, 'setLoop:', 1, 'play:')
				global0._send('setLoop:', 5, 'cel:', 0, 'cycleSpeed:', 8, 'setCycle:', CT, 5, 1, self)
			#end:case
			case 21:
				global102._send('number:', 431, 'setLoop:', 1, 'play:', self)
				global0._send('setCycle:', End, self)
			#end:case
			case 22:#end:case
			case 23:
				global102._send('number:', 431, 'setLoop:', 1, 'play:')
				global0._send('setLoop:', 7, 'cel:', 0, 'cycleSpeed:', 30, 'setCycle:', End, self)
			#end:case
			case 24:
				proc0_1(26)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lookAround(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if (global87 == 0):
					seconds = 8
				else:
					seconds = kernel.Random(2, 4)
				#endif
			#end:case
			case 1:
				global0._send('setLoop:', 3, 'cel:', 0, 'cycleSpeed:', 6, 'setCycle:', End, self)
			#end:case
			case 2:
				global0._send('setLoop:', 2, 'cel:', 0, 'cycleSpeed:', 48, 'setCycle:', Fwd)
				if (local0 < 4):
					local0.post('++')
					(state -= 3)
				#endif
				self._send('cue:')
			#end:case
			case 3:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoDoTinderBoxCode(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		temp0 = 1
		match param1
			case 20:
				if kernel.ScriptID(30, 0)._send('darkRoomLit:'):
					global91._send('say:', 3, 20, 37, 1, 0, 400)
				else:
					global2._send('setScript:', lightItUp)
				#endif
			#end:case
			else:
				if (global66._send('doit:', param1) == -32768):
					global91._send('say:', 3, 0, 36, 1, 0, 400)
				else:
					temp0 = 0
				#endif
			#end:else
		#end:match
		return temp0
	#end:method

#end:class or instance

