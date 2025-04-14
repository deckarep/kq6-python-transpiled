#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 600
import sci_sh
import kernel
import Main
import KQ6Room
import n913
import Conversation
import Scaler
import MCyc
import PolyPath
import Polygon
import Feature
import LoadMany
import DPath
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm600 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = [2, 0, 175, 140, 2, 1, 175, 140, 2, 2, 175, 140, 2, 3, 175, 140, 2, 4, 175, 140, 2, 5, 175, 140, 2, 6, 175, 140, 2, 7, 175, 140, 2, 8, 175, 140, 0, 0, 175, 140, 0, 1, 175, 140, 0, 2, 175, 140, 0, 3, 175, 140, 0, 4, 175, 140, -32768, 600]
local58 = None
local59 = None
local60 = None
local61 = None


@SCI.instance
class rm600(KQ6Room):
	#property vars (may be empty)
	noun = 4
	picture = 605
	horizon = 88
	east = 630
	
	@classmethod
	def init():
		self._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 0, 189, 0, 0, 319, 0, 319, 138, 268, 137, 232, 102, 144, 102, 102, 128, 15, 141,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 319, 163, 319, 189, 224, 189,
					'yourself:'
				)
		)
		super._send('init:', &rest)
		proc913_1(91)
		global1._send('handsOff:')
		proc913_1(15)
		match global12
			case 630:
				global1._send('handsOn:')
				global0._send('init:', 'setScale:', Scaler, 100, 67, 189, 84, 'posn:', 303, 160)
			#end:case
			else:
				if (global103._send('number:') != 155):
					global103._send('number:', 155, 'play:')
				#endif
				self._send('setScript:', horseToon)
			#end:else
		#end:match
		deadGuy._send('init:', 'setScript:', deadOneScript)
		deadGuy2._send('init:', 'setScript:', deadTwoScript)
		queen._send('init:', 'ignoreActors:', 1, 'setScript:', queenScript)
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		deadGuy._send('setMotion:', 0, 'setCycle:', 0)
		deadGuy2._send('setMotion:', 0, 'setCycle:', 0)
		super._send('newRoom:', param1)
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		proc958_0(0, 964, 942)
	#end:method

#end:class or instance

@SCI.instance
class theSky(Feature):
	#property vars (may be empty)
	noun = 7
	onMeCheck = 16384
	
#end:class or instance

@SCI.instance
class horse(Actor):
	#property vars (may be empty)
	x = 196
	y = 160
	view = 606
	loop = 1
	
#end:class or instance

@SCI.instance
class queen(Actor):
	#property vars (may be empty)
	x = 175
	y = 140
	noun = 3
	view = 626
	loop = 4
	cycleSpeed = 30
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				if global0._send('has:', 28):
					global91._send('say:', noun, param1, 1)
				else:
					global91._send('say:', noun, param1, 2)
				#endif
			#end:case
			case 2:
				if global0._send('has:', 28):
					global91._send('say:', noun, param1, 1)
				else:
					global1._send('handsOff:')
					script._send('register:', 1)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class deadGuy(Actor):
	#property vars (may be empty)
	x = -20
	y = 116
	noun = 6
	view = 600
	
	@classmethod
	def doVerb(param1 = None, *rest):
		if (param1 == 5):
			global1._send('handsOff:')
			global2._send('setScript:', egoIsDead, 0, self)
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

	@classmethod
	def doit():
		if 
			(and
				(not local61)
				mover
				(not global2._send('script:'))
				(global0._send('distanceTo:', self) <= 10)
			)
			global1._send('handsOff:')
			local58 = 1
			global2._send('setScript:', egoIsDead, 0, self)
		#endif
		super._send('doit:')
	#end:method

#end:class or instance

@SCI.instance
class deadGuy2(Actor):
	#property vars (may be empty)
	x = 341
	y = 159
	noun = 6
	view = 602
	
	@classmethod
	def doVerb(param1 = None, *rest):
		if (param1 == 5):
			global1._send('handsOff:')
			global2._send('setScript:', egoIsDead, 0, self)
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

	@classmethod
	def doit():
		if 
			(and
				(not local61)
				mover
				(not global2._send('script:'))
				(global0._send('distanceTo:', self) <= 10)
			)
			global1._send('handsOff:')
			local58 = 1
			global2._send('setScript:', egoIsDead, 0, self)
		#endif
		super._send('doit:')
	#end:method

#end:class or instance

@SCI.instance
class deadOneScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				seconds = 8
			#end:case
			case 1:
				if global2._send('script:'):
					self._send('init:')
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				while (register = (kernel.Random(0, 4) + 600) == deadGuy2._send('view:')):

					0
				#end:loop
				client._send(
					'view:', register,
					'posn:', 38, 116,
					'ignoreActors:', 1,
					'init:',
					'setScale:', Scaler, 100, 67, 189, 84,
					'setCycle:', Walk,
					'setMotion:', DPath, -20, 116, 38, 116, 148, 122, 112, 158, -15, 152, self
				)
			#end:case
			case 3:
				self._send('init:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class deadTwoScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				seconds = 8
			#end:case
			case 1:
				if global2._send('script:'):
					self._send('init:')
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				while (register = (kernel.Random(0, 4) + 600) == deadGuy._send('view:')):

					0
				#end:loop
				client._send(
					'view:', register,
					'posn:', 341, 167,
					'ignoreActors:', 1,
					'init:',
					'setScale:', Scaler, 100, 67, 189, 84,
					'setCycle:', Walk,
					'setMotion:', DPath, 331, 167, 149, 151, 108, 107, -21, 100, self
				)
			#end:case
			case 3:
				self._send('init:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class queenScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cycles = 1
			#end:case
			case 1:
				queen._send('setCycle:', End, self)
			#end:case
			case 2:
				queen._send('setCycle:', MCyc, @local0, self)
			#end:case
			case 3:
				cycles = (queen._send('cycleSpeed:') / 2)
			#end:case
			case 4:
				(cond
					case global2._send('script:'):
						self._send('start:', 2, 'init:')
					#end:case
					case register:
						queen._send('setLoop:', 4, 'cel:', 0)
						global2._send('setScript:', egoGetTicket)
					#end:case
					else:
						self._send('start:', 2, 'init:')
					#end:else
				)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoGetTicket(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				local59 = deadGuy._send('mover:')
				deadGuy._send('mover:', 0)
				local60 = deadGuy2._send('mover:')
				deadGuy2._send('mover:', 0)
				global0._send('setMotion:', PolyPath, 149, 157, self)
			#end:case
			case 1:
				global0._send('setHeading:', 315, self)
			#end:case
			case 2:
				theConv._send(
					'add:', -1, 3, 2, 2, 1,
					'add:', -1, 3, 2, 2, 2,
					'add:', -1, 3, 2, 2, 3,
					'add:', -1, 3, 2, 2, 4,
					'add:', -1, 3, 2, 2, 5,
					'add:', -1, 3, 2, 2, 6,
					'add:', -1, 3, 2, 2, 7,
					'add:', -1, 3, 2, 2, 8,
					'add:', -1, 3, 2, 2, 9,
					'add:', -1, 3, 2, 2, 10,
					'add:', -1, 3, 2, 2, 11,
					'init:', self
				)
			#end:case
			case 3:
				theConv._send(
					'add:', -1, 3, 2, 2, 12,
					'add:', -1, 3, 2, 2, 13,
					'add:', -1, 3, 2, 2, 14,
					'add:', -1, 3, 2, 2, 15,
					'add:', -1, 3, 2, 2, 16,
					'add:', -1, 3, 2, 2, 17,
					'init:', self
				)
			#end:case
			case 4:
				queen._send('setLoop:', 4, 'cel:', 0, 'setCycle:', End, self)
				global0._send('normal:', 0, 'view:', 626, 'setLoop:', 5, 'cel:', 0)
			#end:case
			case 5:
				global0._send('get:', 28)
				global1._send('givePoints:', 1)
				queen._send('setCycle:', Beg, self)
			#end:case
			case 6:
				global0._send('reset:', 7)
				cycles = 1
			#end:case
			case 7:
				global91._send('say:', 3, 2, 2, 18, self)
			#end:case
			case 8:
				global91._send('say:', 3, 2, 2, 19, self)
			#end:case
			case 9:
				if local59:
					deadGuy._send('mover:', local59)
				#endif
				if local60:
					deadGuy2._send('mover:', local60)
				#endif
				local59 = local60 = 0
				local61 = 0
				queen._send('setScript:', queenScript, 0, 0)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class theConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class egoIsDead(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				deadGuy._send('setMotion:', 0)
				deadGuy2._send('setMotion:', 0)
				if local58:
					global91._send('say:', 5, 0, 3, 1, self)
				else:
					global91._send('say:', 6, 5, 0, 1, self)
				#endif
			#end:case
			case 1:
				(cond
					case local58:
						cycles = 1
					#end:case
					case (global0._send('x:') > register._send('x:')):
						global0._send(
							'setMotion:', PolyPath, (register._send('x:') + 20), register._send(
									'y:'
								), self
						)
					#end:case
					else:
						global0._send(
							'setMotion:', PolyPath, (register._send('x:') - 20), register._send(
									'y:'
								), self
						)
					#end:else
				)
				global102._send('stop:')
				global103._send('number:', 601, 'play:')
			#end:case
			case 2:
				if local58:
					global91._send('say:', 5, 0, 3, 2, self)
				else:
					global91._send('say:', 6, 5, 0, 2, self)
				#endif
			#end:case
			case 3:
				global0._send(
					'view:', 606,
					'normal:', 0,
					'setLoop:', 0,
					'cel:', 0,
					'cycleSpeed:', 15,
					'setCycle:', End, self
				)
			#end:case
			case 4:
				proc0_1(38)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class horseToon(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				horse._send(
					'init:',
					'setScale:', Scaler, 100, 67, 189, 84,
					'cel:', 0,
					'setCycle:', End, self
				)
				if (global12 == 155):
					kernel.SetCursor(1)
				else:
					global1._send('setCursor:', global19)
				#endif
			#end:case
			case 1:
				global0._send(
					'init:',
					'normal:', 0,
					'setScale:', Scaler, 100, 67, 189, 84,
					'view:', 606,
					'setLoop:', 2,
					'cel:', 0,
					'setPri:', (horse._send('priority:') + 1),
					'posn:', (horse._send('x:') + 38), (horse._send('y:') - 39),
					'setCycle:', End, self
				)
				horse._send(
					'view:', 607,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', (horse._send('x:') + 40), (horse._send('y:') + 5)
				)
			#end:case
			case 2:
				global0._send('reset:', 7, 'posn:', (global0._send('x:') + 17), (global0._send('y:') + 47))
				cycles = 2
			#end:case
			case 3:
				global91._send('say:', 5, 0, 4, 1, self)
			#end:case
			case 4:
				horse._send('setCycle:', End)
				global103._send('fade:', 0, 10, 20, 1, self)
			#end:case
			case 5:
				global102._send('number:', 600, 'flags:', 1, 'play:')
				cycles = 1
			#end:case
			case 6:
				global91._send('say:', 5, 0, 4, 2, self)
			#end:case
			case 7:
				horse._send('dispose:')
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

