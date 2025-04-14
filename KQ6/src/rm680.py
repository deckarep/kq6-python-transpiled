#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 680
import sci_sh
import kernel
import Main
import KQ6Room
import n913
import Scaler
import RandCycle
import MCyc
import PolyPath
import Polygon
import Feature
import Sound
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm680 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None
local4 = [3, 0, 147, 10, 3, 1, 147, 5, 3, 2, 146, 14, 3, 3, 147, 25, 3, 4, 147, 35, 3, 5, 147, 45, 3, 6, 147, 53, 3, 7, 147, 60, 3, 8, 147, 65, 3, 9, 147, 68, 3, 10, 147, 71, 3, 11, 147, 73, -32768]


@SCI.instance
class rm680Messager(Kq6Messager):
	#property vars (may be empty)
	@classmethod
	def findTalker(param1 = None, *rest):
		if 
			(= temp0
				match param1
					case 78: global89#end:case
				#end:match
			)
			return
		else:
			super._send('findTalker:', param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class rm680(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 680
	north = 690
	south = 670
	
	@classmethod
	def init():
		global69._send('enable:')
		global1._send('handsOff:')
		self._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 149, 108, 145, 122, 144, 147, 131, 173, 113, 183, 95, 189, 0, 189, 0, -10, 319, -10, 319, 189, 199, 189, 196, 184, 168, 160, 158, 132, 155, 108, 158, 86, 152, 86,
					'yourself:'
				)
		)
		super._send('init:', &rest)
		kernel.UnLoad(128, 670)
		kernel.UnLoad(128, 671)
		kernel.UnLoad(128, 672)
		kernel.UnLoad(128, 690)
		kernel.UnLoad(128, 691)
		kernel.UnLoad(128, 692)
		local0 = global91
		global91 = rm680Messager
		flame1._send('init:', 'setCycle:', RandCycle)
		flame2._send('init:', 'setCycle:', RandCycle)
		flame3._send('init:', 'setCycle:', RandCycle)
		flame4._send('init:', 'setCycle:', RandCycle)
		flame5._send('init:', 'setCycle:', RandCycle)
		flame6._send('init:', 'setCycle:', RandCycle)
		flame7._send('init:', 'setCycle:', RandCycle)
		flame8._send('init:', 'setCycle:', RandCycle)
		flame9._send('init:', 'setCycle:', RandCycle)
		flame10._send('init:', 'setCycle:', RandCycle)
		flame11._send('init:', 'setCycle:', RandCycle)
		flame12._send('init:', 'setCycle:', RandCycle)
		if (global12 == 670):
			global1._send('handsOn:')
			if (global87 > 1):
				lordGhoul._send('init:', 'setScript:', lordGhoulScript)
				poolGhoulRight._send('init:', 'ignoreActors:', 1, 'setScript:', pgrScript)
				poolGhoulLeft._send('init:', 'ignoreActors:', 1, 'setScript:', pglScript)
				rArm._send('init:')
				lArm._send('init:')
			#endif
			rGuard._send('view:', 683, 'init:', 'setScale:', Scaler, 100, 69, 189, 90)
			lGuard._send('view:', 683, 'init:', 'setScale:', Scaler, 100, 69, 189, 90)
			global0._send(
				'init:',
				'reset:', 3,
				'setScale:', Scaler, 100, 69, 189, 90,
				'posn:', 153, 185
			)
			lord._send('init:')
			path._send('init:')
			sea._send('init:')
			global102._send('number:', 680, 'loop:', -1, 'play:')
		else:
			global0._send(
				'init:',
				'posn:', 125, 82,
				'setScale:', Scaler, 100, 54, 189, 92,
				'setPri:', 4,
				'setLoop:', -1,
				'loop:', 4
			)
			rGuard._send(
				'view:', 6804,
				'init:',
				'setPri:', 7,
				'setLoop:', 1,
				'setScale:', Scaler, 100, 69, 189, 90,
				'addToPic:'
			)
			lGuard._send(
				'view:', 6804,
				'init:',
				'setPri:', 7,
				'setLoop:', 0,
				'setScale:', Scaler, 100, 69, 189, 90,
				'addToPic:'
			)
			self._send('setScript:', wonDeadScript)
		#endif
		global5._send('eachElementDo:', #checkDetail)
	#end:method

	@classmethod
	def doit():
		(cond
			case script: 0#end:case
			case (global0._send('y:') <= 168):
				global1._send('handsOff:')
				self._send('setScript:', takeHimAway)
			#end:case
		)
		super._send('doit:', &rest)
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		if (param1 == 670):
			global1._send('handsOff:')
			self._send('setScript:', dontGoAlex)
		else:
			super._send('newRoom:', param1)
		#endif
	#end:method

	@classmethod
	def dispose():
		global91 = local0
		super._send('dispose:', &rest)
		kernel.DisposeScript(942)
	#end:method

#end:class or instance

@SCI.instance
class sfx(Sound):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class lord(Feature):
	#property vars (may be empty)
	noun = 4
	onMeCheck = 2
	
#end:class or instance

@SCI.instance
class path(Feature):
	#property vars (may be empty)
	noun = 7
	onMeCheck = 8
	
#end:class or instance

@SCI.instance
class sea(Feature):
	#property vars (may be empty)
	noun = 5
	onMeCheck = 4
	
#end:class or instance

@SCI.instance
class flame1(Prop):
	#property vars (may be empty)
	x = 68
	y = 70
	noun = 9
	view = 680
	cel = 1
	priority = 7
	signal = 16400
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class flame2(Prop):
	#property vars (may be empty)
	x = 89
	y = 124
	noun = 9
	view = 680
	priority = 7
	signal = 16400
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class flame3(Prop):
	#property vars (may be empty)
	x = 226
	y = 86
	noun = 9
	view = 680
	cel = 2
	priority = 7
	signal = 16400
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class flame4(Prop):
	#property vars (may be empty)
	x = 239
	y = 48
	noun = 9
	view = 680
	cel = 2
	priority = 7
	signal = 16400
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class flame5(Prop):
	#property vars (may be empty)
	x = 132
	y = 94
	noun = 9
	view = 680
	loop = 1
	priority = 7
	signal = 16400
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class flame6(Prop):
	#property vars (may be empty)
	x = 189
	y = 99
	noun = 9
	view = 680
	loop = 1
	cel = 2
	priority = 7
	signal = 16400
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class flame7(Prop):
	#property vars (may be empty)
	x = 212
	y = 89
	noun = 9
	view = 680
	loop = 1
	cel = 2
	priority = 7
	signal = 16400
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class flame8(Prop):
	#property vars (may be empty)
	x = 100
	y = 91
	noun = 9
	view = 680
	loop = 1
	cel = 3
	priority = 7
	signal = 16400
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class flame9(Prop):
	#property vars (may be empty)
	x = 208
	y = 64
	noun = 9
	view = 680
	loop = 2
	cel = 1
	priority = 3
	signal = 16400
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class flame10(Prop):
	#property vars (may be empty)
	x = 106
	y = 70
	noun = 9
	view = 680
	loop = 2
	cel = 3
	priority = 3
	signal = 16400
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class flame11(Prop):
	#property vars (may be empty)
	x = 123
	y = 56
	noun = 9
	view = 680
	loop = 2
	cel = 3
	priority = 3
	signal = 16400
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class flame12(Prop):
	#property vars (may be empty)
	x = 200
	y = 49
	noun = 9
	view = 680
	loop = 2
	priority = 3
	signal = 16400
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class rArm(Prop):
	#property vars (may be empty)
	x = 172
	y = 59
	noun = 4
	view = 682
	priority = 5
	signal = 16400
	cycleSpeed = 20
	
#end:class or instance

@SCI.instance
class lArm(Actor):
	#property vars (may be empty)
	x = 151
	y = 58
	noun = 4
	view = 682
	loop = 1
	priority = 5
	signal = 24592
	cycleSpeed = 20
	
#end:class or instance

@SCI.instance
class lordGhoul(Prop):
	#property vars (may be empty)
	x = 156
	y = 38
	noun = 8
	view = 6802
	priority = 14
	signal = 16400
	cycleSpeed = 10
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class poolGhoulRight(Actor):
	#property vars (may be empty)
	x = 158
	y = 65
	noun = 8
	view = 682
	loop = 4
	priority = 5
	signal = 24592
	cycleSpeed = 10
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class poolGhoulLeft(Prop):
	#property vars (may be empty)
	x = 158
	y = 65
	noun = 8
	view = 682
	loop = 3
	priority = 5
	signal = 24592
	cycleSpeed = 10
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class rGuard(Actor):
	#property vars (may be empty)
	x = 196
	y = 163
	noun = 6
	loop = 2
	signal = 24576
	
	@classmethod
	def doVerb(param1 = None, *rest):
		(cond
			case proc999_5(param1, 5, 1):
				super._send('doVerb:', param1, &rest)
			#end:case
			case (param1 == 2):
				global1._send('handsOff:')
				global2._send('setScript:', talkGuards)
			#end:case
			else:
				global1._send('handsOff:')
				global2._send('setScript:', giveGuards)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class lGuard(Actor):
	#property vars (may be empty)
	x = 114
	y = 163
	noun = 6
	loop = 3
	signal = 24576
	
	@classmethod
	def doVerb(param1 = None, *rest):
		(cond
			case proc999_5(param1, 5, 1):
				super._send('doVerb:', param1, &rest)
			#end:case
			case (param1 == 2):
				global1._send('handsOff:')
				global2._send('setScript:', talkGuards)
			#end:case
			else:
				global1._send('handsOff:')
				global2._send('setScript:', giveGuards)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class pgrScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				seconds = kernel.Random(3, 10)
			#end:case
			case 1:
				client._send('show:', 'setLoop:', 4, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 2:
				cycles = kernel.Random(5, 10)
			#end:case
			case 3:
				rArm._send('setCycle:', End, self)
			#end:case
			case 4:
				rArm._send('cel:', 0)
				client._send('setLoop:', 5, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 5:
				client._send('hide:')
				self._send('init:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class pglScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				seconds = kernel.Random(3, 10)
			#end:case
			case 1:
				client._send('show:', 'setLoop:', 3, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 2:
				cycles = kernel.Random(5, 10)
			#end:case
			case 3:
				lArm._send('setCycle:', End, self)
			#end:case
			case 4:
				lArm._send('cel:', 0)
				client._send('setLoop:', 6, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 5:
				client._send('hide:')
				self._send('init:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lordGhoulScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				seconds = kernel.Random(10, 30)
			#end:case
			case 1:
				client._send('show:', 'setLoop:', 0, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 2:
				client._send('setLoop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 3:
				client._send('hide:')
				self._send('init:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class dontGoAlex(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global91._send('say:', 1, 0, 5, 1, self)
			#end:case
			case 1:
				global0._send(
					'setMotion:', PolyPath, global0._send('x:'), (global0._send('y:') - 10), self
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
class talkGuards(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global91._send('say:', 6, 2, 0, 1, self)
			#end:case
			case 1:
				global91._send('say:', 6, 2, 0, 2, self)
			#end:case
			case 2:
				self._send('setScript:', takeHimAway)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class giveGuards(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global91._send('say:', 6, 0, 0, 1, self)
			#end:case
			case 1:
				global91._send('say:', 6, 0, 0, 2, self)
			#end:case
			case 2:
				self._send('setScript:', takeHimAway)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class takeHimAway(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if (client == global2):
					global91._send('say:', 3, 3, 4, 0, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				global0._send('setMotion:', PolyPath, 155, 153, self)
			#end:case
			case 2:
				rGuard._send('setCycle:', End, self)
				lGuard._send('setCycle:', End, self)
			#end:case
			case 3: 0#end:case
			case 4:
				rGuard._send(
					'setLoop:', 0,
					'setCycle:', Walk,
					'setMotion:', MoveTo, (rGuard._send('x:') - 20), (rGuard._send('y:') - 20)
				)
				lGuard._send(
					'setLoop:', 0,
					'setCycle:', Walk,
					'setMotion:', MoveTo, (lGuard._send('x:') + 20), (lGuard._send('y:') - 20)
				)
				global0._send(
					'setMotion:', PolyPath, global0._send('x:'), (global0._send('y:') - 20), self
				)
			#end:case
			case 5:
				global2._send('newRoom:', 690)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class wonDeadScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cycles = 1
			#end:case
			case 1:
				local1 = global89._send('x:')
				local2 = global89._send('y:')
				local3 = global89._send('talkWidth:')
				global89._send('x:', 10, 'y:', 10, 'talkWidth:', 100)
				lArm._send(
					'init:',
					'view:', 684,
					'loop:', 3,
					'cel:', 0,
					'x:', 147,
					'y:', 10,
					'setPri:', 6,
					'setScale:', 0,
					'cycleSpeed:', 10,
					'ignoreActors:', 1,
					'ignoreHorizon:', 1,
					'setCycle:', MCyc, @local4, self, 1
				)
			#end:case
			case 2:
				cycles = 5
			#end:case
			case 3:
				global91._send('say:', 1, 0, 2, 1, self)
			#end:case
			case 4:
				cycles = 5
			#end:case
			case 5:
				sfx._send('number:', 687, 'loop:', 1, 'play:')
				rArm._send(
					'init:',
					'view:', 684,
					'setLoop:', 5,
					'cel:', 0,
					'posn:', 161, 56,
					'ignoreActors:', 1
				)
				lordGhoul._send(
					'init:',
					'view:', 684,
					'setLoop:', 2,
					'cel:', 0,
					'setPri:', 5,
					'posn:', 147, 80,
					'ignoreActors:', 1,
					'setCycle:', Fwd
				)
				seconds = 1
			#end:case
			case 6:
				lArm._send('setLoop:', 4, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 7:
				proc913_2(91)
				lordGhoul._send('dispose:')
				rArm._send('dispose:')
				cycles = 2
			#end:case
			case 8:
				global91._send('say:', 1, 0, 2, 2, self)
			#end:case
			case 9:
				global91._send('say:', 1, 0, 2, 3, self)
			#end:case
			case 10:
				poolGhoulRight._send(
					'init:',
					'view:', 6801,
					'setLoop:', 0,
					'cel:', 0,
					'setPri:', 8,
					'posn:', -33, 68,
					'cycleSpeed:', 10,
					'moveSpeed:', 10,
					'setStep:', 10, 10,
					'ignoreActors:', 1,
					'setCycle:', Fwd,
					'setMotion:', MoveTo, 73, 129, self
				)
			#end:case
			case 11:
				sfx._send('number:', 346, 'loop:', 1, 'play:')
				poolGhoulRight._send('setMotion:', MoveTo, 124, 166, self)
			#end:case
			case 12:
				poolGhoulRight._send('view:', 685, 'setLoop:', 0, 'setCycle:', End, self)
				kernel.UnLoad(128, 6801)
			#end:case
			case 13:
				poolGhoulRight._send(
					'setLoop:', 4,
					'cel:', 0,
					'posn:', (poolGhoulRight._send('x:') + 34), (poolGhoulRight._send('y:') + 7)
				)
				seconds = 1
			#end:case
			case 14:
				global91._send('say:', 1, 0, 2, 4, self)
			#end:case
			case 15:
				global91._send('say:', 1, 0, 2, 5, self)
			#end:case
			case 16:
				global91._send('say:', 1, 0, 2, 6, self)
			#end:case
			case 17:
				global91._send('say:', 1, 0, 2, 7, self)
			#end:case
			case 18:
				lArm._send(
					'view:', 687,
					'setLoop:', 0,
					'setCycle:', Walk,
					'setScale:', -1, global0,
					'setPri:', (poolGhoulRight._send('priority:') - 1),
					'setSpeed:', global0._send('currentSpeed:'),
					'setStep:', 5, 4,
					'posn:', lArm._send('x:'), (lArm._send('y:') + 20),
					'setMotion:', PolyPath, (poolGhoulRight._send('x:') - 10), (-
							poolGhoulRight._send('y:')
							10
						), self
				)
				global0._send(
					'setPri:', (poolGhoulRight._send('priority:') - 1),
					'setMotion:', PolyPath, (poolGhoulRight._send('x:') - 20), (-
							poolGhoulRight._send('y:')
							20
						)
				)
			#end:case
			case 19:
				poolGhoulRight._send('setLoop:', 2, 'setCycle:', End, self)
			#end:case
			case 20:
				poolGhoulRight._send('setLoop:', 3, 'cel:', 0, 'setCycle:', End, self)
				lArm._send('dispose:')
			#end:case
			case 21:
				poolGhoulRight._send('setLoop:', 5, 'cel:', 0)
				global0._send(
					'setPri:', 7,
					'ignoreActors:', 1,
					'setMotion:', MoveTo, (poolGhoulRight._send('x:') - 11), (-
							poolGhoulRight._send('y:')
							10
						), self
				)
			#end:case
			case 22:
				global0._send(
					'normal:', 0,
					'view:', 685,
					'setLoop:', 1,
					'cel:', 0,
					'setPri:', (poolGhoulRight._send('priority:') + 1),
					'posn:', poolGhoulRight._send('x:'), poolGhoulRight._send('y:'),
					'setScale:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 23:
				poolGhoulRight._send('dispose:')
				global89._send('x:', local1, 'y:', local2, 'talkWidth:', local3)
				global102._send('number:', 155, 'loop:', -1, 'play:')
				seconds = 3
			#end:case
			case 24:
				global2._send('newRoom:', 155)
			#end:case
		#end:match
	#end:method

#end:class or instance

