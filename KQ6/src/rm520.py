#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 520
import sci_sh
import kernel
import Main
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
	rm520 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = 1
local1 = None
local2 = None


@SCI.instance
class rm520(KQ6Room):
	#property vars (may be empty)
	noun = 5
	picture = 520
	horizon = 70
	north = 510
	south = 500
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.Load(128, 308)
		global2._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 223, 166, 217, 175, 139, 173, 103, 169, 109, 163, 164, 153, 166, 134, 166, 103, 155, 94, 130, 66, 129, 65, 319, 13, 319, 189, 285, 189, 269, 165,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 0, 189, 0, 8, 122, 65, 98, 80, 129, 90, 114, 102, 122, 112, 97, 141, 79, 160, 47, 165, 31, 173, 45, 183, 71, 189,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 199, 189, 168, 189, 176, 185, 194, 186,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 158, 186, 144, 186, 141, 183, 145, 180, 157, 180, 164, 183,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 120, 181, 104, 181, 99, 176, 108, 174, 119, 174, 127, 177,
					'yourself:'
				)
		)
		super._send('init:', &rest)
		if (global12 == north):
			global0._send('init:', 'reset:', 2, 'posn:', 130, 90)
		else:
			global0._send('init:', 'reset:', 3, 'posn:', 105, 187)
		#endif
		if (not proc913_0(13)):
			boilingPond._send(
				'init:',
				'signal:', (| boilingPond._send('signal:') 0x1000),
				'setCycle:', Fwd,
				'setPri:', 9,
				'ignoreActors:', 1,
				'cycleSpeed:', 12
			)
			boilFx._send('play:')
		else:
			boilingPond._send(
				'init:',
				'view:', 525,
				'setLoop:', 0,
				'setPri:', 9,
				'posn:', 141, 125,
				'cycleSpeed:', 12,
				'ignoreActors:', 1,
				'setCycle:', Fwd
			)
		#endif
		finishedPond._send('init:')
		mushrooms._send('init:')
		frontPath._send('init:')
		backPath._send('init:')
		banks._send('init:')
		rocks._send('init:')
		trees._send('init:')
		if (<= temp0 kernel.Random(1, 100) 500):
			bunny._send('init:', 'setScript:', bunnyScript)
		else:
			squirrel._send('init:')
		#endif
		if (global9._send('at:', 19)._send('owner:') == global11):
			theHuntersLamp._send('init:')
		#endif
		global0._send('setScale:', Scaler, 100, 50, 184, 72)
		global0._send('scaler:')._send('doit:')
		global1._send('handsOn:')
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (kernel.GameIsRestarting() and (not proc913_0(13))):
			boilFx._send('play:')
		#endif
		super._send('doit:', &rest)
		temp0 = global0._send('onControl:', 1)
		(cond
			case script: 0#end:case
			case (temp0 & 0x4000):
				global2._send('newRoom:', north)
			#end:case
			case ((temp0 & 0x0002) and local0):
				global1._send('handsOff:')
				self._send('setScript:', bravePond)
			#end:case
		)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			match param1
				case 1:
					if proc913_0(13):
						global91._send('say:', noun, param1, 4)
						1
					else:
						global91._send('say:', noun, param1, 3)
						1
					#endif
				#end:case
				else:
					super._send('doVerb:', param1, &rest)
				#end:else
			#end:match
		)
	#end:method

#end:class or instance

@SCI.instance
class boilFx(Sound):
	#property vars (may be empty)
	flags = 1
	number = 520
	loop = -1
	
#end:class or instance

@SCI.instance
class boilDeath(Sound):
	#property vars (may be empty)
	flags = 1
	number = 521
	
#end:class or instance

@SCI.instance
class theHuntersLamp(Prop):
	#property vars (may be empty)
	x = 111
	y = 65
	noun = 4
	view = 520
	loop = 3
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				global91._send('say:', noun, param1)
			#end:case
			case 5:
				if proc913_0(13):
					global1._send('handsOff:')
					local1 = 1
					global0._send('setScript:', getLamp)
				else:
					global91._send('say:', noun, param1, 3)
				#endif
			#end:case
			case 2:
				super._send('doVerb:', param1, &rest)
			#end:case
			else:
				if proc913_0(13):
					global91._send('say:', noun, 0, 4)
				else:
					global91._send('say:', noun, 0, 3)
				#endif
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class splash(Prop):
	#property vars (may be empty)
	view = 520
	loop = 4
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('x:', (global0._send('x:') + 16), 'y:', (global0._send('y:') - 32))
		super._send('init:')
	#end:method

#end:class or instance

@SCI.instance
class finishedPond(Feature):
	#property vars (may be empty)
	noun = 3
	onMeCheck = 2
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (param1 == 5):
				global1._send('handsOff:')
				local2 = 1
				global0._send('setScript:', feelPond)
			#end:case
			case proc999_5(param1, 1, 2):
				if proc913_0(13):
					global91._send('say:', noun, param1, 4)
				else:
					global91._send('say:', noun, param1, 3)
				#endif
			#end:case
			case proc999_5(param1, 28, 25, 43, 94, 44, 34):
				global91._send('say:', noun, param1, 0)
			#end:case
			case (param1 == 54):
				if proc913_0(13):
					global91._send('say:', noun, param1, 4)
				else:
					global91._send('say:', noun, param1, 3)
				#endif
			#end:case
			case proc999_5(param1, 52, 53):
				global0._send('setScript:', throwLettuceInPond, 0, param1)
			#end:case
			case proc913_0(13):
				global91._send('say:', noun, 0, 4)
			#end:case
			else:
				global91._send('say:', noun, 0, 3)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class boilingPond(Prop):
	#property vars (may be empty)
	x = 85
	y = 150
	noun = 3
	view = 524
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		finishedPond._send('doVerb:', param1, &rest)
	#end:method

#end:class or instance

@SCI.instance
class bunny(Actor):
	#property vars (may be empty)
	x = 143
	y = 176
	noun = 13
	view = 503
	loop = 2
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('ignoreActors:', 1, 'setLoop:', self._send('loop:'))
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class feelPond(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global0._send('setMotion:', MoveTo, 99, 148, self)
			#end:case
			case 1:
				global0._send(
					'view:', 521,
					'normal:', 0,
					'cycleSpeed:', 10,
					'setLoop:', 3,
					'posn:', 110, 154,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				global0._send('reset:', 'posn:', 99, 148)
				cycles = 2
			#end:case
			case 3:
				if proc913_0(13):
					global91._send('say:', 3, 5, 4, 0, self)
				else:
					global91._send('say:', 3, 5, 3, 0, self)
				#endif
			#end:case
			case 4:
				local2 = 0
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getLamp(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global0._send('setMotion:', PolyPath, 119, 99, self)
			#end:case
			case 1:
				global0._send('setHeading:', 315)
				theHuntersLamp._send('dispose:')
				global0._send(
					'normal:', 0,
					'view:', 523,
					'setLoop:', 0,
					'cel:', 0,
					'cycleSpeed:', 10,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				global91._send('say:', 4, 5, 4, 1, self)
			#end:case
			case 3:
				global1._send('handsOn:')
				global0._send('reset:', 1)
				global0._send('get:', 19)
				global1._send('givePoints:', 1)
				local1 = 0
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class throwLettuceInPond(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 113, 159, self)
			#end:case
			case 1:
				global0._send('setHeading:', 0)
				ticks = 6
			#end:case
			case 2:
				if proc913_0(13):
					global91._send('say:', 3, 52, 4, 1, self)
				else:
					global91._send('say:', 3, 52, 3, 1, self)
				#endif
			#end:case
			case 3:
				global0._send(
					'view:', 521,
					'normal:', 0,
					'setLoop:', 1,
					'cel:', 0,
					'cycleSpeed:', 8,
					'setCycle:', End, self
				)
			#end:case
			case 4:
				splash._send('init:', 'setPri:', 10, 'setCycle:', CT, 3, 1, self)
			#end:case
			case 5:
				pondWalk._send('number:', 923, 'loop:', 1, 'play:')
				splash._send('setCycle:', End, self)
			#end:case
			case 6:
				splash._send('dispose:')
				global0._send('put:', 21, global11, 'reset:', 3)
				kernel.ScriptID(0, 7)._send('dispose:')
				ticks = 12
			#end:case
			case 7:
				global1._send('handsOn:')
				if proc913_0(13):
					global91._send('say:', 3, 52, 4, 2, self)
					self._send('dispose:')
				else:
					proc913_1(13)
					global1._send('givePoints:', 4)
					boilingPond._send(
						'setLoop:', 1,
						'cel:', 0,
						'posn:', 92, 150,
						'cycleSpeed:', 24,
						'setCycle:', End, self
					)
					boilFx._send('stop:')
				#endif
			#end:case
			case 8:
				global91._send('say:', 3, 52, 3, 2, self)
			#end:case
			case 9:
				boilingPond._send('view:', 525, 'setLoop:', 0, 'posn:', 141, 125, 'setCycle:', Fwd)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class pondWalk(Sound):
	#property vars (may be empty)
	number = 920
	loop = -1
	
#end:class or instance

@SCI.instance
class bravePond(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(cond
					case (not proc913_0(13)):
						cycles = 1
					#end:case
					case (not proc913_0(83)):
						global91._send('say:', 3, 3, 5, 1, self)
					#end:case
					else:
						cycles = 1
					#end:else
				)
			#end:case
			case 1:
				if proc913_0(13):
					global0._send(
						'illegalBits:', 0,
						'view:', 521,
						'setPri:', 14,
						'setSpeed:', 6,
						'ignoreActors:', 1
					)
					if (global0._send('y:') < 110):
						global0._send('setLoop:', 5, 'setMotion:', PolyPath, 110, 143, self)
					else:
						global0._send('setLoop:', 4, 'setMotion:', PolyPath, 137, 107, self)
					#endif
					pondWalk._send('number:', 920, 'loop:', -1, 'play:')
				else:
					self._send('setScript:', egoBoilsScript)
				#endif
			#end:case
			case 2:
				pondWalk._send('stop:')
				if (global0._send('loop:') == 5):
					global0._send('reset:', 'setMotion:', PolyPath, 94, 154, self)
				else:
					global0._send('reset:', 'setMotion:', PolyPath, 139, 102, self)
				#endif
			#end:case
			case 3:
				if proc913_0(83):
					cycles = 1
				else:
					global91._send('say:', 3, 3, 5, 2, self)
				#endif
			#end:case
			case 4:
				global0._send('reset:')
				if (not proc913_0(83)):
					proc913_1(83)
					global91._send('say:', 3, 3, 5, 3, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 5:
				(cond
					case local1:
						global1._send('handsOff:')
						global0._send('setScript:', getLamp)
					#end:case
					case local2:
						global1._send('handsOff:')
						global0._send('setScript:', feelPond)
					#end:case
					else:
						global1._send('handsOn:')
					#end:else
				)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoBoilsScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global91._send('say:', 3, 3, 3, 1, self)
			#end:case
			case 1:
				global0._send(
					'view:', 521,
					'normal:', 0,
					'setLoop:', 4,
					'cycleSpeed:', 12,
					'setMotion:', PolyPath, (global0._send('x:') + 2), (-
							global0._send('y:')
							3
						), self
				)
			#end:case
			case 2:
				boilDeath._send('play:')
				global0._send('setLoop:', 0, 'cel:', 0, 'cycleSpeed:', 24, 'setCycle:', End, self)
			#end:case
			case 3:
				global0._send('hide:')
				global91._send('say:', 3, 3, 3, 2, self)
			#end:case
			case 4:
				local0 = 0
				proc0_1(5)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class mushrooms(Feature):
	#property vars (may be empty)
	noun = 8
	onMeCheck = 4
	
#end:class or instance

@SCI.instance
class frontPath(Feature):
	#property vars (may be empty)
	noun = 6
	onMeCheck = 16
	
#end:class or instance

@SCI.instance
class backPath(Feature):
	#property vars (may be empty)
	noun = 7
	onMeCheck = 8
	
#end:class or instance

@SCI.instance
class banks(Feature):
	#property vars (may be empty)
	noun = 10
	onMeCheck = 32
	
#end:class or instance

@SCI.instance
class rocks(Feature):
	#property vars (may be empty)
	noun = 2
	onMeCheck = 64
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (param1 == 1):
				global91._send('say:', noun, param1, 2, 0, 0, 0)
			#end:case
			case proc999_5(param1, 1, 2, 5):
				global91._send('say:', noun, param1, 0, 0, 0, 0)
			#end:case
			else:
				global91._send('say:', noun, 0, 0, 0, 0, 0)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class trees(Feature):
	#property vars (may be empty)
	noun = 9
	onMeCheck = 128
	
#end:class or instance

@SCI.instance
class squirrel(Prop):
	#property vars (may be empty)
	x = 204
	y = 179
	view = 520
	loop = 5
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		if proc913_0(13):
			self._send('setScript:', squirrelScript)
		else:
			self._send('stopUpd:')
		#endif
	#end:method

#end:class or instance

@SCI.instance
class squirrelScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				seconds = 10
			#end:case
			case 1:
				client._send('setCycle:', End, self)
			#end:case
			case 2:
				client._send('dispose:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class bunnyScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				bunny._send('setCycle:', Fwd, 'setMotion:', MoveTo, 206, 179, self)
			#end:case
			case 1:
				bunny._send('setLoop:', 3, 'setCycle:', End, self)
			#end:case
			case 2:
				bunny._send('setCycle:', End, self)
			#end:case
			case 3:
				bunny._send('setLoop:', 2, 'setCycle:', Fwd, 'setMotion:', MoveTo, 244, 207, self)
			#end:case
			case 4:
				client._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

