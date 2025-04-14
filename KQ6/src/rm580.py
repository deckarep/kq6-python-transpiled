#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 580
import sci_sh
import kernel
import Main
import KQ6Room
import n913
import Inset
import Conversation
import Scaler
import Osc
import RandCycle
import PolyPath
import Polygon
import Feature
import Sound
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm580 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.instance
class rm580Messager(Kq6Messager):
	#property vars (may be empty)
	@classmethod
	def findTalker(param1 = None, *rest):
		if 
			(= temp0
				match param1
					case 59: global89#end:case
					case 60: global89#end:case
				#end:match
			)
			return
		else:
			super._send('findTalker:', param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class fireSound(Sound):
	#property vars (may be empty)
	number = 560
	loop = -1
	
#end:class or instance

@SCI.instance
class rainSound(Sound):
	#property vars (may be empty)
	number = 567
	loop = -1
	
#end:class or instance

@SCI.instance
class fx0(Sound):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class fx1(Sound):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class fx2(Sound):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class rm580(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 580
	south = 550
	west = 560
	autoLoad = 0
	
	@classmethod
	def init():
		super._send('init:', &rest)
		local1 = global91
		global91 = rm580Messager
		global2._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 89, 165, 42, 185, 0, 185, 0, 0, 319, 0, 319, 189, 249, 189, 208, 167, 261, 154, 255, 120, 213, 119, 166, 119, 126, 122, 56, 138, 49, 153,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 214, 129, 206, 147, 137, 147, 123, 129, 151, 130, 174, 121, 185, 130,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 153, 158, 127, 171, 82, 156, 106, 147, 144, 149,
					'yourself:'
				)
		)
		if ((not proc913_0(25)) and (not proc913_0(74))):
			local0 = 1
		#endif
		if (proc913_0(25) and (not proc913_0(14)) and (not proc913_0(74))):
			proc913_1(14)
			local0 = 2
		#endif
		if local0:
			global69._send(
				'enable:',
				'disable:', 0, 1, 2, 3, 4, 5, 6,
				'height:', -100,
				'activateHeight:', -100
			)
			Cursor._send('showCursor:', 0)
			global102._send('number:', 569, 'loop:', -1, 'flags:', 1, 'play:', 'hold:', 10)
			global103._send('stop:')
			if (local0 == 1):
				druid._send('init:', 'setScale:', Scaler, 100, 70, 190, 112, 'setPri:', 14)
				druid2._send('setScale:', Scaler, 100, 70, 190, 112, 'init:')
			#endif
			druid3._send('init:', 'setScale:', Scaler, 100, 70, 190, 112)
			druid4._send(
				'init:',
				'setScale:', Scaler, 100, 70, 190, 112,
				'ignoreActors:', 1,
				'stopUpd:'
			)
			headDruid._send('init:', 'setScale:', Scaler, 100, 70, 190, 112)
			fire._send('init:', 'setCycle:', RandCycle)
			smoke._send('init:')
			fireSound._send('play:')
			rope._send('init:', 'stopUpd:')
			cage._send('init:', 'setPri:', 14, 'ignoreActors:', 1, 'stopUpd:')
			cageRope._send('init:', 'setPri:', 14, 'ignoreActors:', 1, 'stopUpd:')
		else:
			global102._send('number:', 570, 'loop:', -1, 'flags:', 1, 'play:', 'hold:', 10)
			fire._send('init:', 'setLoop:', 2, 'posn:', 167, 137, 'setCycle:', RandCycle)
			cage._send('init:', 'setPri:', 12, 'ignoreActors:', 1, 'addToPic:')
			cageRope._send('init:', 'setPri:', 12, 'ignoreActors:', 1, 'addToPic:')
		#endif
		bonfire._send('init:')
		circleOfStones._send('init:')
		trees._send('init:')
		global0._send('init:', 'setScale:', Scaler, 100, 70, 190, 112)
		if (global12 == 560):
			global0._send('posn:', 9, 187)
		else:
			global0._send('posn:', 164, 212)
		#endif
		global1._send('handsOff:')
		self._send('setScript:', egoEnters)
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		global102._send('fade:')
		global91 = local1
		super._send('newRoom:', param1)
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(939)
		kernel.Palette(4, 0, 255, 100)
	#end:method

#end:class or instance

@SCI.instance
class egoEnters(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				(cond
					case (local0 == 2):
						global0._send(
							'view:', 5806,
							'posn:', 148, 235,
							'setLoop:', 0,
							'setMotion:', MoveTo, 162, 160, self,
							'setPri:', 14,
							'setSpeed:', 3,
							'setCycle:', Walk
						)
					#end:case
					case (global12 == 560):
						global0._send('setMotion:', MoveTo, 162, global0._send('y:'), self)
					#end:case
					else:
						global0._send('setMotion:', MoveTo, 162, 170, self)
					#end:else
				)
			#end:case
			case 1:
				match local0
					case 0:
						global1._send('handsOn:')
						self._send('dispose:')
					#end:case
					case 1:
						if (global12 == 560):
							global0._send('setMotion:', MoveTo, 162, 170, self)
						else:
							ticks = 1
						#endif
					#end:case
					case 2:
						global2._send('setScript:', meetDruidsTwo)
					#end:case
				#end:match
			#end:case
			case 2:
				global2._send('setScript:', meetDruidsOne)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getEmbers(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('setMotion:', PolyPath, 208, 130, self)
			#end:case
			case 1:
				global0._send('setHeading:', 225, self)
			#end:case
			case 2:
				global0._send(
					'normal:', 0,
					'view:', 5803,
					'setLoop:', 0,
					'cel:', 0,
					'cycleSpeed:', 10,
					'posn:', 206, 131,
					'setCycle:', End, self
				)
			#end:case
			case 3:
				global0._send('reset:', 5, 'posn:', 211, 129)
				cycles = 2
			#end:case
			case 4:
				if (not proc913_1(140)):
					global1._send('givePoints:', 1)
				#endif
				(cond
					case 
						(and
							(temp1 = global9._send('at:', 11)._send('state:') & 0x0004)
							(not (temp1 & 0x0001))
							(not (temp1 & 0x0002))
						):
						global91._send('say:', 4, 51, 13, 1, self)
					#end:case
					case 
						(and
							(temp1 & 0x0004)
							((temp1 & 0x0001) or (temp1 & 0x0002))
						):
						global91._send('say:', 4, 51, 14, 1, self)
					#end:case
					else:
						global91._send('say:', 4, 51, 11, 1, self)
					#end:else
				)
			#end:case
			case 5:
				global0._send('reset:', 2)
				temp0 = global9._send('at:', 11)
				kernel.ScriptID(0, 4)._send('setReal:', temp0, 0, 5, 0)
				temp0._send(
					'setCursor:', 990, 0, 9,
					'loop:', 0,
					'cel:', 10,
					'state:', (| temp0._send('state:') 0x000c)
				)
				temp0._send('cursor:')._send('loop:', 0, 'cel:', 9)
				global1._send('setCursor:', temp0._send('cursor:'), 'handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class meetDruidsOne(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				proc913_1(14)
				global91._send('say:', 1, 0, 1, 1, self)
			#end:case
			case 1:
				global91._send('say:', 1, 0, 1, 2, self)
			#end:case
			case 2:
				global91._send('say:', 1, 0, 1, 3, self)
			#end:case
			case 3:
				druid._send(
					'setPri:', 14,
					'setCycle:', Walk,
					'setSpeed:', 0,
					'xStep:', 6,
					'setMotion:', MoveTo, (global0._send('x:') - 25), (+
							global0._send('y:')
							3
						), self,
					'ignoreActors:', 1,
					'illegalBits:', 0
				)
				druid2._send(
					'setCycle:', Walk,
					'setSpeed:', 0,
					'xStep:', 6,
					'setMotion:', MoveTo, (global0._send('x:') + 24), (+
							global0._send('y:')
							4
						), self,
					'ignoreActors:', 1,
					'illegalBits:', 0
				)
			#end:case
			case 4: 0#end:case
			case 5:
				druid._send('hide:')
				druid2._send('hide:')
				global0._send(
					'view:', 554,
					'normal:', 0,
					'setPri:', 14,
					'setLoop:', 0,
					'setCel:', 0,
					'posn:', (global0._send('x:') - 2), global0._send('y:'),
					'setCycle:', End, self
				)
			#end:case
			case 6:
				global0._send('view:', 5806, 'setLoop:', 0, 'setCycle:', Walk)
				global2._send('setScript:', continueDruids)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class meetDruidsTwo(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				druid._send(
					'view:', 553,
					'posn:', 0, 0,
					'init:',
					'setPri:', 14,
					'ignoreActors:', 1,
					'illegalBits:', 0,
					'hide:'
				)
				druid2._send(
					'view:', 553,
					'posn:', 0, 0,
					'init:',
					'ignoreActors:', 1,
					'illegalBits:', 0,
					'hide:'
				)
				proc913_1(14)
				cycles = 2
			#end:case
			case 1:
				global91._send('say:', 1, 0, 1, 1, self)
			#end:case
			case 2:
				global91._send('say:', 1, 0, 8, 1, self)
			#end:case
			case 3:
				global91._send('say:', 1, 0, 8, 2, self)
			#end:case
			case 4:
				global2._send('setScript:', continueDruids)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class continueDruids(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global91._send('say:', 1, 0, 1, 4, self)
			#end:case
			case 1:
				global91._send('say:', 1, 0, 1, 5, self)
			#end:case
			case 2:
				global91._send('say:', 1, 0, 1, 6, self)
			#end:case
			case 3:
				global102._send('hold:', 20)
				cage._send('signal:', (| cage._send('signal:') 0x6000))
				cycles = 2
			#end:case
			case 4:
				global0._send('setMotion:', MoveTo, 177, 158, self)
			#end:case
			case 5:
				kernel.UnLoad(128, 554)
				global0._send(
					'view:', 588,
					'setLoop:', 0,
					'cel:', 0,
					'setSpeed:', 3,
					'setPri:', (cage._send('priority:') - 1),
					'posn:', (global0._send('x:') - 18), (global0._send('y:') + 2),
					'setCycle:', End, self
				)
			#end:case
			case 6:
				global0._send('view:', 581, 'setLoop:', 1, 'setPri:', -1, 'setCycle:', End, self)
			#end:case
			case 7:
				cage._send('view:', 5807, 'setLoop:', 0, 'cel:', 0, 'posn:', 146, 124, 'setPri:', 14)
				cageRope._send('view:', 5807, 'setLoop:', 1, 'cel:', 0, 'setPri:', 14)
				global0._send('view:', 553, 'hide:')
				kernel.UnLoad(128, 580)
				kernel.UnLoad(128, 581)
				druid._send(
					'show:',
					'posn:', (global0._send('x:') - 12), (global0._send('y:') - 4),
					'setLoop:', -1,
					'setCycle:', Walk
				)
				druid2._send(
					'show:',
					'posn:', (global0._send('x:') - 37), (global0._send('y:') - 10),
					'setLoop:', -1,
					'setCycle:', Walk
				)
				cycles = 2
			#end:case
			case 8:
				global91._send('say:', 1, 0, 1, 7, self)
			#end:case
			case 9:
				druid._send('setMotion:', MoveTo, druid._send('x:'), (druid._send('y:') + 10), self)
				druid2._send('setMotion:', MoveTo, 222, 180, self)
			#end:case
			case 10:
				druid._send('setMotion:', MoveTo, 85, 178, self)
			#end:case
			case 11: 0#end:case
			case 12:
				headDruid._send('view:', 587, 'setLoop:', 0, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 13:
				headDruid._send('view:', 5808)
				druid._send(
					'setLoop:', 4,
					'cel:', 3,
					'setLoop:', -1,
					'setPri:', (cage._send('priority:') + 1)
				)
				druid2._send('setLoop:', 4, 'cel:', 3, 'setLoop:', -1)
				druid3._send(
					'setPri:', (rope._send('priority:') - 1),
					'setLoop:', -1,
					'setCycle:', Walk,
					'setMotion:', PolyPath, 194, 131, self,
					'ignoreActors:', 1
				)
			#end:case
			case 14:
				druid5._send(
					'init:',
					'setLoop:', -1,
					'setScale:', Scaler, 100, 70, 190, 112,
					'setCycle:', Walk,
					'setMotion:', MoveTo, 224, 130, self
				)
			#end:case
			case 15:
				fx0._send('number:', 563, 'loop:', -1, 'play:')
				druid3._send(
					'view:', 5804,
					'setLoop:', 0,
					'posn:', 208, 133,
					'setCycle:', Fwd,
					'setPri:', -1
				)
				rope._send('dispose:')
				druid5._send('dispose:')
				cageRope._send('setCel:', 1)
				cage._send('posn:', 147, 124)
				cycles = 5
			#end:case
			case 16:
				cageRope._send('setCel:', 2)
				cage._send('posn:', 152, 117)
				cycles = 5
			#end:case
			case 17:
				cageRope._send('setCel:', 3)
				cage._send('posn:', 166, 107)
				cycles = 5
			#end:case
			case 18:
				cageRope._send('dispose:')
				cage._send(
					'view:', 5801,
					'setPri:', 14,
					'setCel:', 0,
					'setLoop:', 0,
					'cycleSpeed:', 5,
					'posn:', 170, 54,
					'setCycle:', End, self
				)
			#end:case
			case 19:
				fx0._send('stop:')
				kernel.UnLoad(128, 5807)
				cage._send('cel:', 0, 'setCycle:', End, self)
			#end:case
			case 20:
				druid3._send('setCycle:', 0, 'setPri:', 12, 'stopUpd:')
				cage._send('setLoop:', 1, 'cel:', 6, 'setCycle:', End, self)
			#end:case
			case 21:
				cage._send('cel:', 0, 'setCycle:', End, self)
			#end:case
			case 22:
				cage._send('view:', 5802, 'setLoop:', 0, 'setCel:', 0)
				kernel.UnLoad(128, 5801)
				cycles = 2
			#end:case
			case 23:
				global91._send('say:', 1, 0, 1, 8, self)
			#end:case
			case 24:
				cage._send('setPri:', 12, 'stopUpd:')
				smoke._send('dispose:')
				global2._send('setInset:', cageInset)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class inTheCage(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				seconds = 5
			#end:case
			case 1:
				global102._send('hold:', 30)
				inEgo._send('view:', 583, 'setLoop:', 0, 'cel:', 1)
				ticks = 12
			#end:case
			case 2:
				inEgo._send('stopUpd:')
				global91._send('say:', 1, 0, 2, 0, self)
			#end:case
			case 3:
				seconds = 5
			#end:case
			case 4:
				global102._send('hold:', 0)
				inEgo._send('cel:', 2)
				ticks = 12
			#end:case
			case 5:
				inEgo._send('stopUpd:')
				global91._send('say:', 1, 0, 3, 0, self)
			#end:case
			case 6:
				seconds = 3
			#end:case
			case 7:
				inEgo._send('cel:', 3)
				seconds = 2
			#end:case
			case 8:
				if (not global161):
					global91._send('say:', 1, 0, 4, 0, self)
				else:
					state.post('++')
					global91._send('say:', 1, 0, 7, 0, self)
				#endif
			#end:case
			case 9:
				global91._send('say:', 1, 0, 7, 0, self)
			#end:case
			case 10:
				global102._send('number:', 561, 'loop:', 1, 'play:', self)
				inEgo._send('setLoop:', 1, 'cel:', 0, 'setCycle:', End)
			#end:case
			case 11:
				temp0 = 100
				while (temp0 >= 0): # inline for
					kernel.Palette(4, 0, 255, temp0)
					# for:reinit
					(temp0 -= 10)
				#end:loop
				cycles = 1
			#end:case
			case 12:
				cageInset._send('dispose:', 0)
				cycles = 2
			#end:case
			case 13:
				global2._send('drawPic:', 98)
				global5._send('eachElementDo:', #dispose)
				cycles = 2
			#end:case
			case 14:
				kernel.Palette(4, 0, 255, 100)
				global69._send('height:', 0, 'activateHeight:', 0, 'enable:', 6)
				Cursor._send('showCursor:', 1)
				if (global153 == 5):
					proc0_1(11)
				else:
					proc0_1(10)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class makeRain(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				seconds = 5
			#end:case
			case 1:
				global102._send('hold:', 30)
				inEgo._send('cel:', 1)
				ticks = 12
			#end:case
			case 2:
				inEgo._send('stopUpd:')
				global91._send('say:', 1, 0, 2, 0, self)
			#end:case
			case 3:
				seconds = 5
			#end:case
			case 4:
				global102._send('hold:', 0)
				inEgo._send('cel:', 2)
				ticks = 12
			#end:case
			case 5:
				inEgo._send('stopUpd:')
				global91._send('say:', 1, 0, 3, 0, self)
				seconds = 5
			#end:case
			case 6:
				global91._send('say:', 1, 0, 6, 0, self)
			#end:case
			case 7:
				global91._send('say:', 1, 0, 9, 1)
				fx0._send('number:', 562, 'loop:', -1, 'play:')
				inFlame._send('show:', 'setCycle:', RandCycle)
				seconds = 2
			#end:case
			case 8:
				fx1._send('number:', 568, 'loop:', 1, 'play:')
				inEgo._send(
					'view:', 585,
					'setLoop:', 1,
					'cel:', 0,
					'cycleSpeed:', 15,
					'setCycle:', End, self
				)
			#end:case
			case 9:
				inEgo._send('setCycle:', End, self)
			#end:case
			case 10:
				inFlame._send('dispose:')
				fx0._send('stop:')
				inEgo._send('setCycle:', End, self)
			#end:case
			case 11:
				global0._send('put:', 5, 580)
				if (proc913_0(112) and (not global0._send('has:', 4))):
					global91._send('say:', 1, 0, 15, 1, self)
					global1._send('givePoints:', 1)
					global0._send('get:', 4)
				else:
					global91._send('say:', 1, 0, 9, 2, self)
				#endif
			#end:case
			case 12:
				inEgo._send('view:', 583, 'setLoop:', 0, 'cel:', 2, 'setCycle:', 0)
				kernel.UnLoad(128, 585)
				cycles = 2
			#end:case
			case 13:
				global91._send('say:', 1, 0, 9, 3, self)
			#end:case
			case 14:
				seconds = 2
			#end:case
			case 15:
				fx0._send('number:', 520, 'loop:', -1, 'play:')
				inEgo._send(
					'view:', 582,
					'setLoop:', 7,
					'cel:', 0,
					'cycleSpeed:', 15,
					'setCycle:', Osc, 2, self
				)
			#end:case
			case 16:
				inEgo._send('setCycle:', 0, 'stopUpd:')
				global91._send('say:', 1, 0, 9, 4, self)
			#end:case
			case 17:
				seconds = 2
			#end:case
			case 18:
				inEgo._send('setCycle:', Osc, 2, self)
			#end:case
			case 19:
				inEgo._send('setCycle:', 0, 'stopUpd:')
				global91._send('say:', 1, 0, 9, 5, self)
			#end:case
			case 20:
				seconds = 2
			#end:case
			case 21:
				inEgo._send('setCycle:', Osc, 2, self)
			#end:case
			case 22:
				inEgo._send('setCycle:', 0, 'stopUpd:')
				global91._send('say:', 1, 0, 9, 6, self)
			#end:case
			case 23:
				global1._send('givePoints:', 2)
				inEgo._send('view:', 5821, 'setLoop:', 0, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 24:
				inEgo._send('view:', 582, 'setLoop:', 5, 'cycleSpeed:', 2, 'setCycle:', End, self)
			#end:case
			case 25:
				inEgo._send('setCycle:', End, self)
			#end:case
			case 26:
				inEgo._send('setCycle:', End, self)
			#end:case
			case 27:
				inEgo._send('setCycle:', End, self)
			#end:case
			case 28:
				inEgo._send('cel:', 0, 'setCycle:', End, self)
			#end:case
			case 29:
				inEgo._send('setLoop:', 6, 'setCycle:', End, self)
			#end:case
			case 30:
				inEgo._send('setCycle:', 0, 'stopUpd:')
				global91._send('say:', 1, 0, 9, 7, self)
			#end:case
			case 31:
				global91._send('say:', 1, 0, 9, 8, self)
			#end:case
			case 32:
				fx1._send('number:', 565, 'loop:', -1, 'play:')
				inBillow._send('show:', 'setCycle:', End, self)
			#end:case
			case 33:
				inBillow._send('setLoop:', 1, 'cel:', 0, 'setCycle:', Fwd)
				seconds = 3
			#end:case
			case 34:
				kernel.Palette(1, 580)
				cycles = 3
			#end:case
			case 35:
				fx0._send('stop:')
				fx1._send('stop:')
				global102._send('fade:')
				fx2._send('number:', 566, 'loop:', 1, 'play:')
				kernel.Palette(1, 5801)
				seconds = 2
			#end:case
			case 36:
				fx2._send('play:')
				kernel.Palette(1, 580)
				cycles = 3
			#end:case
			case 37:
				kernel.Palette(1, 5801)
				cycles = 10
			#end:case
			case 38:
				fx2._send('play:')
				kernel.Palette(1, 580)
				cycles = 3
			#end:case
			case 39:
				kernel.Palette(1, 5801)
				cycles = 30
			#end:case
			case 40:
				global91._send('say:', 1, 0, 9, 9, self)
			#end:case
			case 41:
				rainSound._send('play:')
				fireSound._send('stop:')
				cycles = 2
			#end:case
			case 42:
				temp0 = 100
				while (temp0 >= 0): # inline for
					kernel.Palette(4, 0, 255, temp0)
					# for:reinit
					temp0.post('--')
				#end:loop
				cycles = 1
			#end:case
			case 43:
				cageInset._send('dispose:')
				druid3._send('dispose:')
				druid4._send('dispose:')
				smoke._send('dispose:')
				headDruid._send('posn:', headDruid._send('x:'), headDruid._send('y:'), 1000)
				druid._send('posn:', druid._send('x:'), druid._send('y:'), 1000)
				druid2._send('posn:', druid2._send('x:'), druid2._send('y:'), 1000)
				fire._send('posn:', fire._send('x:'), fire._send('y:'), 1000)
				global0._send('posn:', global0._send('x:'), global0._send('y:'), 1000)
				cage._send('posn:', cage._send('x:'), cage._send('y:'), 1000)
				global2._send('drawPic:', 98)
				cycles = 2
			#end:case
			case 44:
				kernel.Palette(4, 0, 255, 100)
				seconds = 3
			#end:case
			case 45:
				fx2._send('play:')
				seconds = 2
			#end:case
			case 46:
				rainSound._send('play:')
				global91._send('say:', 1, 0, 9, 10, self)
				proc913_1(74)
			#end:case
			case 47:
				seconds = 3
			#end:case
			case 48:
				global2._send('drawPic:', 98, 12)
				kernel.Message(0, 580, 1, 0, 9, 11, @temp1)
				kernel.Display(@temp1, 100, 82, 85, 102, 14, 105, 0)
				cycles = 1
			#end:case
			case 49:
				rainSound._send('stop:')
				cycles = 1
			#end:case
			case 50:
				global102._send('number:', 570, 'loop:', -1, 'play:')
				seconds = 5
			#end:case
			case 51:
				global2._send('drawPic:', 580, 11)
				cage._send(
					'view:', 580,
					'loop:', 0,
					'cel:', 0,
					'ignoreActors:', 1,
					'ignoreHorizon:', 1,
					'posn:', 147, 124, 0,
					'setPri:', 12,
					'addToPic:'
				)
				cageRope._send(
					'view:', 580,
					'init:',
					'loop:', 1,
					'cel:', 0,
					'ignoreHorizon:', 1,
					'ignoreActors:', 1,
					'posn:', 170, 54,
					'setPri:', 12,
					'addToPic:'
				)
				fire._send('posn:', 167, 137, 0, 'setLoop:', 2)
				global0._send(
					'reset:', 1,
					'setScale:', Scaler, 100, 70, 190, 112,
					'posn:', 131, 135, 0
				)
				headDruid._send('posn:', headDruid._send('x:'), headDruid._send('y:'), 0)
				druid._send('posn:', druid._send('x:'), druid._send('y:'), 0)
				druid2._send('posn:', druid2._send('x:'), druid2._send('y:'), 0)
				cycles = 2
			#end:case
			case 52:
				druidConv._send(
					'add:', -1, 1, 0, 10, 1,
					'add:', -1, 1, 0, 10, 2,
					'add:', -1, 1, 0, 10, 3,
					'add:', -1, 1, 0, 10, 4,
					'add:', -1, 1, 0, 10, 5,
					'add:', -1, 1, 0, 10, 6,
					'add:', -1, 1, 0, 10, 7,
					'add:', -1, 1, 0, 10, 8,
					'add:', -1, 1, 0, 10, 9,
					'add:', -1, 1, 0, 10, 10,
					'add:', -1, 1, 0, 10, 11,
					'add:', -1, 1, 0, 10, 12,
					'add:', -1, 1, 0, 10, 13,
					'init:', self
				)
			#end:case
			case 53:
				global91._send('say:', 1, 0, 10, 14, self)
			#end:case
			case 54:
				global91._send('say:', 1, 0, 10, 15, self)
			#end:case
			case 55:
				global91._send('say:', 1, 0, 10, 16, self)
			#end:case
			case 56:
				global91._send('say:', 1, 0, 10, 17, self)
			#end:case
			case 57:
				global91._send('say:', 1, 0, 10, 18, self)
			#end:case
			case 58:
				global91._send('say:', 1, 0, 10, 19, self)
			#end:case
			case 59:
				headDruid._send(
					'view:', 584,
					'setLoop:', 0,
					'setCycle:', Walk,
					'setMotion:', MoveTo, 50, headDruid._send('y:'), self
				)
				druid._send('setMotion:', PolyPath, -20, 189, self)
				druid2._send('setMotion:', PolyPath, -20, 189, self)
			#end:case
			case 60: 0#end:case
			case 61: 0#end:case
			case 62:
				headDruid._send('dispose:')
				druid._send('dispose:')
				druid2._send('dispose:')
				global69._send('height:', 0, 'activateHeight:', 0, 'enable:', 6)
				Cursor._send('showCursor:', 1)
				global161 = 0
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class fire(Actor):
	#property vars (may be empty)
	x = 170
	y = 144
	view = 589
	signal = 16384
	cycleSpeed = 17
	detailLevel = 3
	
	@classmethod
	def doVerb(param1 = None, *rest):
		bonfire._send('doVerb:', param1, &rest)
	#end:method

#end:class or instance

@SCI.instance
class smoke(Prop):
	#property vars (may be empty)
	x = 169
	y = 103
	view = 589
	loop = 1
	cel = 4
	detailLevel = 3
	
	@classmethod
	def doit():
		super._send('doit:', &rest)
		cel = fire._send('cel:')
	#end:method

#end:class or instance

@SCI.instance
class cage(Actor):
	#property vars (may be empty)
	x = 147
	y = 124
	noun = 9
	onMeCheck = 2048
	view = 580
	
#end:class or instance

@SCI.instance
class cageRope(Actor):
	#property vars (may be empty)
	x = 170
	y = 54
	view = 580
	loop = 1
	
#end:class or instance

@SCI.instance
class druid(Actor):
	#property vars (may be empty)
	x = 82
	y = 163
	view = 553
	
#end:class or instance

@SCI.instance
class druid2(Actor):
	#property vars (may be empty)
	x = 236
	y = 163
	view = 553
	
#end:class or instance

@SCI.instance
class headDruid(Actor):
	#property vars (may be empty)
	x = 90
	y = 139
	view = 5808
	
#end:class or instance

@SCI.instance
class druid3(Actor):
	#property vars (may be empty)
	x = 227
	y = 129
	view = 553
	loop = 1
	
#end:class or instance

@SCI.instance
class druid4(Prop):
	#property vars (may be empty)
	x = 67
	y = 146
	view = 553
	
#end:class or instance

@SCI.instance
class druid5(Actor):
	#property vars (may be empty)
	x = 240
	y = 130
	view = 553
	
#end:class or instance

@SCI.instance
class rope(View):
	#property vars (may be empty)
	x = 196
	y = 135
	view = 580
	cel = 1
	priority = 9
	signal = 16400
	
#end:class or instance

@SCI.instance
class bonfire(Feature):
	#property vars (may be empty)
	noun = 4
	onMeCheck = 8
	
	@classmethod
	def doVerb(param1 = None, *rest):
		if proc999_5(param1, 57, 58, 59, 60, 96):
			global91._send('say:', noun, 56, 0)
		else:
			match param1
				case 51:
					if (global9._send('at:', 11)._send('state:') & 0x0008):
						global91._send('say:', noun, 51, 16, 1)
					else:
						global1._send('handsOff:')
						global2._send('setScript:', getEmbers)
					#endif
				#end:case
				else:
					super._send('doVerb:', param1, &rest)
				#end:else
			#end:match
		#endif
	#end:method

#end:class or instance

@SCI.instance
class circleOfStones(Feature):
	#property vars (may be empty)
	noun = 7
	onMeCheck = 2
	
#end:class or instance

@SCI.instance
class trees(Feature):
	#property vars (may be empty)
	noun = 6
	onMeCheck = 4
	
#end:class or instance

@SCI.instance
class cageInset(Inset):
	#property vars (may be empty)
	view = 582
	x = 85
	y = 32
	priority = 13
	noun = 8
	
	@classmethod
	def init():
		super._send('init:', &rest)
		inEgo._send('init:', 'setPri:', 14)
		inFire._send('init:', 'setCycle:', Fwd, 'cycleSpeed:', 10, 'setPri:', 14)
		inFlame._send('init:', 'setPri:', 13, 'hide:')
		inBillow._send('init:', 'setPri:', 14, 'hide:')
		if (global0._send('has:', 19) and (global161 == 15)):
			global2._send('setScript:', makeRain)
		else:
			global2._send('setScript:', inTheCage)
		#endif
	#end:method

	@classmethod
	def drawInset():
		if (picture > 0):
			if global169:
				kernel.DrawPic(picture, 15, (0 if anOverlay else 1))
			else:
				kernel.DrawPic(picture, (100 if anOverlay else style), if 
					anOverlay
					0
				else:
					1
				#endif)
			#endif
		#endif
		if view:
			(= insetView
				inView._send('new:')._send(
					'view:', view,
					'loop:', loop,
					'cel:', cel,
					'x:', x,
					'y:', y,
					'setPri:', priority,
					'ignoreActors:', 1,
					'init:',
					'addToPic:',
					'yourself:'
				)
			)
		#endif
	#end:method

	@classmethod
	def dispose():
		inEgo._send('dispose:')
		inFire._send('dispose:')
		inBillow._send('dispose:')
		global10._send('eachElementDo:', #dispose, 'eachElementDo:', #delete)
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class inView(View):
	#property vars (may be empty)
	@classmethod
	def handleEvent():
		return 0
	#end:method

#end:class or instance

@SCI.instance
class inEgo(Prop):
	#property vars (may be empty)
	x = 162
	y = 49
	noun = 8
	view = 583
	
#end:class or instance

@SCI.instance
class inFire(Prop):
	#property vars (may be empty)
	x = 149
	y = 111
	noun = 8
	view = 582
	loop = 8
	detailLevel = 3
	
#end:class or instance

@SCI.instance
class inFlame(Prop):
	#property vars (may be empty)
	x = 179
	y = 88
	noun = 8
	view = 585
	
#end:class or instance

@SCI.instance
class inBillow(Prop):
	#property vars (may be empty)
	x = 162
	y = 49
	noun = 8
	view = 5821
	loop = 2
	cycleSpeed = 15
	
#end:class or instance

@SCI.instance
class druidConv(Conversation):
	#property vars (may be empty)
#end:class or instance

