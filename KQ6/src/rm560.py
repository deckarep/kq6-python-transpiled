#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 560
import sci_sh
import kernel
import Main
import KQ6Room
import n913
import Scaler
import PolyPath
import Polygon
import Feature
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm560 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


@SCI.instance
class rm560(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 560
	horizon = 0
	east = 580
	south = 550
	vanishingY = -200
	
	@classmethod
	def init():
		super._send('init:', &rest)
		global1._send('handsOff:')
		global2._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 164, 152, 137, 160, 119, 162, 83, 158, 75, 151, 74, 148, 68, 139, 78, 134, 94, 128, 138, 128, 158, 147,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 319, 0, 319, 132, 232, 148, 201, 147, 196, 141, 221, 137, 197, 134, 182, 128, 169, 132, 159, 125, 147, 118, 168, 117, 191, 94, 161, 94, 149, 98, 140, 108, 91, 96, 70, 113, 43, 104, 15, 97, 13, 99, 38, 105, 74, 122, 62, 128, 62, 143, 56, 145, 33, 148, 26, 166, 19, 184, 78, 184, 88, 171, 110, 171, 130, 177, 136, 189, 0, 189, 0, 0,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 319, 189, 244, 189, 248, 186, 319, 186,
					'yourself:'
				)
		)
		stairs._send('init:')
		rocks._send('init:')
		bear._send('init:')
		skull._send('init:')
		pit._send('init:')
		doors._send('init:', 'approachVerbs:', 1, 5, 2)
		trees._send('init:', 'approachVerbs:', 2)
		roomPath._send('init:')
		if (global9._send('at:', 42)._send('owner:') == 560):
			scythe._send('init:', 'stopUpd:', 'setPri:', 13)
		#endif
		global2._send('setScript:', egoEnters)
	#end:method

	@classmethod
	def doit():
		super._send('doit:', &rest)
		temp0 = global0._send('onControl:', 1)
		(cond
			case script: 0#end:case
			case (temp0 & 0x0800):
				global1._send('handsOff:')
				self._send('setScript:', backUpScript)
			#end:case
			case ((temp0 & 0x0080) and (not (global0._send('priority:') == 14))):
				global0._send('setPri:', 14)
				local0 = 1
			#end:case
			case ((not (temp0 & 0x0080)) and local0):
				global0._send('setPri:', -1)
				local0 = 0
			#end:case
		)
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		super._send('newRoom:', param1)
	#end:method

#end:class or instance

@SCI.instance
class trees(Feature):
	#property vars (may be empty)
	noun = 9
	onMeCheck = 2
	
	@classmethod
	def onMe(param1 = None, *rest):
		if super._send('onMe:', param1):
			if (global70 <= 180):
				self._send('approachX:', 92, 'approachY:', 107, 'x:', 53, 'y:', 70)
			else:
				self._send('approachX:', 197, 'approachY:', 143, 'x:', 249, 'y:', 105)
			#endif
			return 1
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		(cond
			case (param1 != 2):
				super._send('doVerb:', param1, &rest)
			#end:case
			case proc913_0(25):
				global91._send('say:', noun, param1, 4)
			#end:case
			else:
				global91._send('say:', noun, param1, 3)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class roomPath(Feature):
	#property vars (may be empty)
	noun = 10
	onMeCheck = 256
	
#end:class or instance

@SCI.instance
class rocks(Feature):
	#property vars (may be empty)
	noun = 2
	onMeCheck = 8
	
	@classmethod
	def doVerb(param1 = None, *rest):
		(cond
			case (param1 == 1):
				global91._send('say:', noun, param1, 10, 0, 0, 0)
			#end:case
			case proc999_5(param1, 2, 5):
				global91._send('say:', noun, param1, 0, 0, 0, 0)
			#end:case
			else:
				global91._send('say:', noun, 0, 0, 0, 0, 0)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class bear(Feature):
	#property vars (may be empty)
	noun = 12
	onMeCheck = 16
	
#end:class or instance

@SCI.instance
class stairs(Feature):
	#property vars (may be empty)
	noun = 13
	onMeCheck = 128
	
#end:class or instance

@SCI.instance
class doors(Feature):
	#property vars (may be empty)
	noun = 7
	onMeCheck = 4
	
	@classmethod
	def onMe(param1 = None, *rest):
		if super._send('onMe:', param1):
			if (global70 <= 180):
				self._send('approachX:', 92, 'approachY:', 107, 'x:', 53, 'y:', 70)
			else:
				self._send('approachX:', 197, 'approachY:', 143, 'x:', 249, 'y:', 105)
			#endif
			return 1
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		(cond
			case proc999_5(param1, 8, 16, 35):
				global91._send('say:', noun, param1, 0)
			#end:case
			case proc999_5(param1, 2, 5):
				if proc913_0(25):
					global91._send('say:', noun, param1, 4)
				else:
					global91._send('say:', noun, param1, 3)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class skull(Feature):
	#property vars (may be empty)
	noun = 8
	onMeCheck = 64
	
#end:class or instance

@SCI.instance
class pit(Feature):
	#property vars (may be empty)
	noun = 5
	onMeCheck = 32
	
	@classmethod
	def doVerb(param1 = None, *rest):
		(cond
			case (param1 == 1):
				global2._send('setScript:', lookFireKludgeScript)
			#end:case
			case (param1 != 5):
				super._send('doVerb:', param1, &rest)
			#end:case
			case (global9._send('at:', 6)._send('owner:') != 560):
				global91._send('say:', noun, param1, 6)
			#end:case
			else:
				global2._send('setScript:', getCoal)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class scythe(View):
	#property vars (may be empty)
	x = 15
	y = 45
	noun = 4
	view = 560
	signal = 16384
	
	@classmethod
	def doVerb(param1 = None, *rest):
		if (param1 == 5):
			global1._send('handsOff:')
			global2._send('setScript:', getScythe)
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class lookFireKludgeScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global91._send('say:', 5, 1, 0, 1, self)
			#end:case
			case 1:
				if (not proc913_0(14)):
					global91._send('say:', 5, 1, 8, 1, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class backUpScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global91._send('say:', 1, 0, 7, 0, self)
			#end:case
			case 1:
				global0._send(
					'setMotion:', PolyPath, global0._send('x:'), (global0._send('y:') + 10), self
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
class egoEnters(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global104._send('number:', 580, 'loop:', 1, 'flags:', 1, 'play:')
				if (global12 == 550):
					global0._send(
						'init:',
						'posn:', 150, 188,
						'setScale:', Scaler, 100, 75, 190, 84,
						'setMotion:', MoveTo, 150, 170, self
					)
				else:
					global0._send(
						'init:',
						'posn:', 318, 162,
						'setScale:', Scaler, 100, 75, 190, 84,
						'setMotion:', MoveTo, 250, 162, self
					)
				#endif
			#end:case
			case 1:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getCoal(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 152, 142, self)
			#end:case
			case 1:
				global0._send(
					'view:', 561,
					'setPri:', 14,
					'normal:', 0,
					'setPri:', 12,
					'setLoop:', 1,
					'cel:', 0,
					'cycleSpeed:', 14,
					'setCycle:', CT, 3, 1, self
				)
			#end:case
			case 2:
				global0._send('setCycle:', End, self)
			#end:case
			case 3:
				global1._send('givePoints:', 1)
				global0._send('get:', 6, 'reset:')
				global91._send('say:', 5, 5, 5, 1, self)
			#end:case
			case 4:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getScythe(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send(
					'ignoreActors:', 1,
					'illegalBits:', 0,
					'setMotion:', PolyPath, 34, 103, self
				)
			#end:case
			case 1:
				scythe._send('dispose:')
				global0._send(
					'normal:', 0,
					'view:', 561,
					'cel:', 0,
					'setLoop:', 0,
					'setSpeed:', 8,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				global0._send('get:', 42)
				global1._send('givePoints:', 1)
				global91._send('say:', 4, 5, 0, 1, self)
			#end:case
			case 3:
				global1._send('handsOn:')
				global0._send('reset:')
				global0._send('setPri:', 14)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

