#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 670
import sci_sh
import kernel
import Main
import KQ6Print
import KQ6Room
import n913
import GatePanel
import Conversation
import Scaler
import PolyPath
import Polygon
import Feature
import LoadMany
import Sound
import Motion
import User
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm670 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = [12, 15, 22, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
local27


@SCI.instance
class rm670(KQ6Room):
	#property vars (may be empty)
	noun = 4
	picture = 670
	south = 660
	
	@classmethod
	def init():
		global1._send('handsOff:')
		self._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 224, 76, 319, 76, 319, 189, 95, 189, 44, 165, 27, 143, 64, 118, 105, 113, 162, 91, 168, 86, 184, 86,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 181, 81, 163, 81, 102, 108, 71, 109, 45, 115, 26, 127, 8, 146, 10, 172, 30, 189, 0, 189, 0, 0, 319, 0, 319, 72, 215, 72,
					'yourself:'
				)
		)
		super._send('init:')
		kernel.Lock(143, 670, 0)
		global0._send('init:', 'reset:', 'posn:', 49, 230, 'setScale:', Scaler, 90, 80, 250, 50)
		self._send('setScript:', enterRoomScript)
		torch1._send('setCycle:', Fwd, 'ignoreActors:', 1, 'init:')
		torch2._send('setCycle:', Fwd, 'ignoreActors:', 1, 'init:')
		shimmer1._send('setCycle:', Fwd, 'ignoreActors:', 1, 'init:')
		shimmer2._send('setCycle:', Fwd, 'ignoreActors:', 1, 'init:')
		gate._send('init:', 'ignoreHorizon:', 1, 'ignoreActors:', 1)
		path._send('init:')
		river._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		(return
			if (param1 == 1):
				if local0:
					global91._send('say:', noun, param1, 3)
					1
				else:
					global91._send('say:', noun, param1, 4)
					1
				#endif
			else:
				super._send('doVerb:', param1, &rest)
			#endif
		)
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		if (param1 == 660):
			global1._send('handsOff:')
			self._send('setScript:', dontGoAlex)
		else:
			super._send('newRoom:', param1, &rest)
		#endif
	#end:method

	@classmethod
	def doit():
		temp0 = global0._send('onControl:', 1)
		(cond
			case script: 0#end:case
			case ((temp0 & 0x4000) and (not local0)):
				global1._send('handsOff:')
				self._send('setScript:', convertGate)
			#end:case
		)
		super._send('doit:', &rest)
	#end:method

	@classmethod
	def notify(param1 = None, *rest):
		if global25:
			global25._send('dispose:')
		#endif
		kernel.DrawPic(global2._send('picture:'))
		global0._send('reset:')
		gate._send('view:', 677)
		shimmer1._send('view:', 670, 'loop:', 1)
		shimmer2._send('view:', 670, 'loop:', 1)
		torch1._send('view:', 670)
		torch2._send('view:', 670)
		global5._send('eachElementDo:', #show)
		if param1:
			script._send('cue:')
		else:
			global1._send('handsOff:')
			self._send('setScript:', killAlexScript)
		#endif
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:', &rest)
		proc958_0(0, 916)
	#end:method

#end:class or instance

@SCI.instance
class torch1(Prop):
	#property vars (may be empty)
	x = 170
	y = 57
	noun = 7
	view = 670
	
#end:class or instance

@SCI.instance
class torch2(Prop):
	#property vars (may be empty)
	x = 250
	y = 54
	noun = 7
	view = 670
	cel = 1
	priority = 10
	signal = 16
	
#end:class or instance

@SCI.instance
class shimmer1(Prop):
	#property vars (may be empty)
	x = 172
	y = 176
	view = 670
	loop = 1
	
	@classmethod
	def doVerb(param1 = None, *rest):
		river._send('doVerb:', param1, &rest)
	#end:method

#end:class or instance

@SCI.instance
class shimmer2(Prop):
	#property vars (may be empty)
	x = 252
	y = 179
	view = 670
	loop = 1
	
	@classmethod
	def doVerb(param1 = None, *rest):
		river._send('doVerb:', param1, &rest)
	#end:method

#end:class or instance

@SCI.instance
class path(Feature):
	#property vars (may be empty)
	noun = 8
	onMeCheck = 2
	
#end:class or instance

@SCI.instance
class river(Feature):
	#property vars (may be empty)
	noun = 3
	onMeCheck = 4
	
	@classmethod
	def init():
		global93._send('addToFront:', self)
		super._send('init:', &rest)
	#end:method

	@classmethod
	def dispose():
		global93._send('delete:', self)
		super._send('dispose:', &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 3:
				global1._send('handsOff:')
				global2._send('setScript:', walkInWater)
			#end:case
			case 44:
				if proc913_0(58):
					global91._send('say:', noun, param1, 14)
				else:
					global91._send('say:', noun, param1, 15)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class gate(Actor):
	#property vars (may be empty)
	x = 216
	y = 36
	noun = 2
	approachX = 172
	approachY = 82
	view = 672
	cycleSpeed = 10
	
	@classmethod
	def doit():
		if 
			(and
				local0
				(not global2._send('script:'))
				(global0._send('distanceTo:', self) < 40)
			)
			global1._send('handsOff:')
			global2._send('setScript:', walkCloseToGate)
		#endif
		super._send('doit:', &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		(cond
			case (param1 == 2):
				if local0:
					global1._send('handsOff:')
					gate._send('setScript:', 0)
					global2._send('setScript:', talkGate)
				else:
					global91._send('say:', noun, param1, 4)
				#endif
			#end:case
			case (param1 == 5):
				if local0:
					global1._send('handsOff:')
					global2._send('setScript:', handGateDead)
				else:
					global1._send('handsOff:')
					global2._send('setScript:', handGate)
				#endif
			#end:case
			case (param1 == 1):
				if local0:
					global91._send('say:', noun, param1, 3)
				else:
					global91._send('say:', noun, param1, 4)
				#endif
			#end:case
			case proc999_5(param1, 48, 35, 28, 16, 13):
				if local0:
					global91._send('say:', noun, param1, 3, 0)
				else:
					global91._send('say:', noun, param1, 4, 0)
				#endif
			#end:case
			case local0:
				global91._send('say:', noun, 0, 3)
			#end:case
			else:
				global91._send('say:', noun, 0, 4)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class gateMorph(Sound):
	#property vars (may be empty)
	flags = 1
	
#end:class or instance

@SCI.instance
class enterRoomScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cycles = 2
			#end:case
			case 1:
				global0._send('setMotion:', PolyPath, global0._send('x:'), 186, self)
			#end:case
			case 2:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class convertGate(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global102._send('pause:', 1)
				gateMorph._send('number:', 670, 'loop:', 1, 'play:', self)
				gate._send(
					'view:', 675,
					'ignoreHorizon:', 1,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', 210, 48,
					'setCycle:', End, self
				)
			#end:case
			case 1: 0#end:case
			case 2:
				global102._send('pause:', 0)
				local0 = 1
				gate._send('view:', 677, 'setLoop:', 0, 'cel:', 0, 'setScript:', randomMsg)
				if (client == global2):
					global1._send('handsOn:')
				#endif
				self._send('dispose:')
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
				global91._send('say:', 4, 3, 8, 0, self)
			#end:case
			case 1:
				global0._send(
					'setMotion:', MoveTo, global0._send('x:'), (global0._send('y:') - 10), self
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
class talkGate(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if 
					(>
						kernel.GetDistance(global0._send('x:'), global0._send('y:'), gate._send(
							'x:'
						), gate._send('y:'))
						50
					)
					global0._send(
						'setMotion:', PolyPath, gate._send('approachX:'), gate._send(
								'approachY:'
							), self
					)
				else:
					proc913_4(global0, gate, self)
				#endif
			#end:case
			case 1:
				theConv._send(
					'add:', -1, 2, 2, 3, 1,
					'add:', -1, 2, 2, 3, 2,
					'add:', -1, 2, 2, 3, 3,
					'add:', -1, 2, 2, 3, 4,
					'add:', -1, 2, 2, 3, 5,
					'add:', -1, 2, 2, 3, 6,
					'add:', -1, 2, 2, 3, 7,
					'add:', -1, 2, 2, 3, 8,
					'add:', -1, 2, 2, 3, 9,
					'add:', -1, 2, 2, 3, 10,
					'add:', -1, 2, 2, 3, 11,
					'add:', -1, 2, 2, 3, 12,
					'init:', self
				)
			#end:case
			case 2:
				User._send('canInput:', 1, 'canControl:', 1)
				global5._send('eachElementDo:', #hide)
				proc913_1(49)
				kernel.DrawPic(98)
				cycles = 2
			#end:case
			case 3:
				docoProtect._send('init:', @local1, 4, 26)
			#end:case
			case 4:
				global1._send('givePoints:', 3)
				global1._send('setCursor:', global21)
				cycles = 2
			#end:case
			case 5:
				proc913_2(49)
				global91._send('say:', 1, 5, 1, 0, self)
			#end:case
			case 6:
				global102._send('pause:', 1)
				gateMorph._send('number:', 671, 'loop:', 1, 'play:', self)
				gate._send('view:', 675, 'setLoop:', 0)
				gate._send('cel:', gate._send('lastCel:'), 'setCycle:', Beg, self)
			#end:case
			case 7: 0#end:case
			case 8:
				gate._send('view:', 672, 'setLoop:', 0, 'cel:', 0, 'posn:', 216, 36)
				cycles = 5
			#end:case
			case 9:
				gate._send(
					'view:', 672,
					'setCel:', 0,
					'setLoop:', 1,
					'posn:', 216, 36,
					'ignoreActors:', 1,
					'setPri:', 5,
					'setCycle:', End, self
				)
				gateMorph._send('number:', 342, 'loop:', 1, 'play:', self)
			#end:case
			case 10: 0#end:case
			case 11:
				global102._send('pause:', 0)
				local0 = 0
				global0._send(
					'ignoreHorizon:', 1,
					'setPri:', (gate._send('priority:') + 1),
					'setMotion:', PolyPath, 217, 74, self
				)
			#end:case
			case 12:
				global0._send(
					'setPri:', (gate._send('priority:') - 1),
					'setMotion:', PolyPath, 248, 74, self
				)
			#end:case
			case 13:
				global69._send('enable:')
				global2._send('newRoom:', 680)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class killAlexScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('setCursor:', global21)
				cycles = 2
			#end:case
			case 1:
				gate._send('setScript:', 0)
				global91._send('say:', 1, 5, 2, 1, self)
			#end:case
			case 2:
				global91._send('say:', 1, 5, 2, 2, self)
			#end:case
			case 3:
				global0._send('setMotion:', PolyPath, 182, 81, self)
			#end:case
			case 4:
				global0._send(
					'normal:', 0,
					'view:', 673,
					'setLoop:', 0,
					'cel:', 0,
					'cycleSpeed:', 5,
					'setScale:', 0,
					'posn:', (gate._send('x:') + 3), (gate._send('y:') + 20),
					'setCycle:', CT, 6, 1, self
				)
			#end:case
			case 5:
				global0._send('setCycle:', End, self)
				eatSound._send('play:')
			#end:case
			case 6:
				global0._send('dispose:')
				cycles = 30
			#end:case
			case 7:
				global91._send('say:', 1, 5, 2, 3, self)
			#end:case
			case 8:
				proc0_1(17)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class eatSound(Sound):
	#property vars (may be empty)
	number = 672
	
#end:class or instance

@SCI.instance
class handGateDead(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				gate._send('setScript:', 0)
				global91._send('say:', 2, 5, 3, 1, self)
			#end:case
			case 1:
				global0._send('setMotion:', PolyPath, 182, 81, self)
			#end:case
			case 2:
				global91._send('say:', 2, 5, 3, 2, self)
			#end:case
			case 3:
				global0._send(
					'normal:', 0,
					'view:', 673,
					'setLoop:', 0,
					'cel:', 0,
					'cycleSpeed:', 5,
					'setScale:', 0,
					'posn:', (gate._send('x:') + 3), (gate._send('y:') + 20),
					'setScale:', 0,
					'setCycle:', CT, 6, 1, self
				)
			#end:case
			case 4:
				global0._send('setCycle:', End, self)
				eatSound._send('play:')
			#end:case
			case 5:
				global0._send('dispose:')
				cycles = 30
			#end:case
			case 6:
				global91._send('say:', 2, 5, 3, 3, self)
			#end:case
			case 7:
				cycles = 2
			#end:case
			case 8:
				proc0_1(16)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class handGate(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('setMotion:', PolyPath, 184, 82, self)
			#end:case
			case 1:
				global0._send(
					'normal:', 0,
					'view:', 673,
					'setLoop:', 1,
					'cel:', 0,
					'posn:', 178, 82,
					'setScale:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				global91._send('say:', 2, 5, 4, 1, self)
			#end:case
			case 3:
				global91._send('say:', 2, 5, 4, 2, self)
			#end:case
			case 4:
				global0._send('reset:', 6, 'setScale:', Scaler, 90, 80, 250, 50)
				self._send('setScript:', convertGate, self)
			#end:case
			case 5:
				global91._send('say:', 2, 5, 4, 3, self)
			#end:case
			case 6:
				global91._send('say:', 2, 5, 4, 4, self)
			#end:case
			case 7:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class randomMsg(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				seconds = 30
			#end:case
			case 1:
				match temp0 = kernel.Random(1, 3)
					case 1:
						global91._send('say:', 6, 0, 10, 0, self)
					#end:case
					case 2:
						global91._send('say:', 6, 0, 11, 0, self)
					#end:case
					case 3:
						global91._send('say:', 6, 0, 12, 0, self)
					#end:case
				#end:match
			#end:case
			case 2:
				self._send('init:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walkCloseToGate(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				gate._send('setScript:', 0)
				local0 = 0
				global91._send('say:', 4, 3, 13, 1, self)
			#end:case
			case 1:
				global91._send('say:', 4, 3, 13, 2, self)
			#end:case
			case 2:
				global0._send(
					'normal:', 0,
					'view:', 673,
					'setLoop:', 0,
					'cel:', 0,
					'cycleSpeed:', 5,
					'posn:', (gate._send('x:') + 3), (gate._send('y:') + 20),
					'setCycle:', CT, 6, 1, self
				)
			#end:case
			case 3:
				global0._send('setCycle:', End, self)
				eatSound._send('play:')
			#end:case
			case 4:
				global0._send('dispose:')
				cycles = 30
			#end:case
			case 5:
				global91._send('say:', 4, 3, 13, 3, self)
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				proc0_1(16)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class splashSound(Sound):
	#property vars (may be empty)
	number = 923
	
#end:class or instance

@SCI.instance
class walkInWater(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				gate._send('setScript:', 0)
				global0._send('setMotion:', PolyPath, 138, 103, self)
			#end:case
			case 1:
				kernel.Load(128, 674)
				cycles = 2
			#end:case
			case 2:
				global102._send('number:', 653, 'loop:', 1, 'play:')
				global0._send(
					'normal:', 0,
					'view:', 674,
					'setLoop:', 0,
					'cel:', 0,
					'cycleSpeed:', 3,
					'setCycle:', CT, 8, 1, self
				)
			#end:case
			case 3:
				splashSound._send('play:')
				global0._send('setCycle:', End, self)
			#end:case
			case 4:
				global0._send('dispose:')
				cycles = 2
			#end:case
			case 5:
				if local0:
					global91._send('say:', 3, 3, 3, 1, self)
				else:
					global91._send('say:', 3, 3, 4, 1, self)
				#endif
			#end:case
			case 6:
				if local0:
					global91._send('say:', 3, 3, 3, 2, self)
				else:
					global91._send('say:', 3, 3, 4, 2, self)
					cycles = 1
				#endif
			#end:case
			case 7:
				if local0:
					global91._send('say:', 3, 3, 3, 3, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 8:
				proc0_1(31)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class docoProtect(GatePanel):
	#property vars (may be empty)
	x = 84
	y = 17
	noun = 1
	view = 678
	offsetX = 30
	offsetY = 20
	maxCol = 5
	maxRow = 5
	numButtons = 30
	
	@classmethod
	def init():
		gate._send('setScript:', 0)
		global0._send('view:', 2002)
		gate._send('view:', 2002)
		torch1._send('view:', 2002)
		torch2._send('view:', 2002)
		shimmer1._send('view:', 2002)
		shimmer2._send('view:', 2002)
		KQ6Print._send(
			'modeless:', 1,
			'width:', 290,
			'posn:', 10, 146,
			'say:', 1, 0, 0, 0, 1, 0, 0, 671,
			'init:'
		)
		super._send('init:', &rest)
	#end:method

	@classmethod
	def drawButton():
		temp0 = 0
		if (not proc999_5(value, 26, 27, 29, 30)):
			if (not (local27[(value / 16)] & (0x8000 >> (mod value 16)))):
				(local27[(value / 16)] |= (0x8000 >> (mod value 16)))
				temp0 = super._send('drawButton:', &rest)
				global104._send('number:', 910, 'setLoop:', 1, 'play:')
			else:
				temp0 = 0
			#endif
		#endif
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class theConv(Conversation):
	#property vars (may be empty)
#end:class or instance

