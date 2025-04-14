#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 500
import sci_sh
import kernel
import Main
import KQ6Room
import n913
import Conversation
import PolyPath
import Polygon
import Feature
import Sound
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm500 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = 1
local2 = 1
local3 = None
local4 = None


@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class partSong(Sound):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class rm500(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 500
	north = 520
	
	@classmethod
	def init():
		kernel.Load(128, 308)
		global2._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 319, 189, 245, 189, 245, 162, 266, 147, 228, 105, 255, 94, 264, 79, 319, 82,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 0, 189, 0, 0, 259, 78, 251, 90, 225, 102, 210, 96, 149, 118, 156, 145, 93, 177, 37, 189,
					'yourself:'
				)
		)
		water1._send('setCycle:', Fwd, 'init:')
		water2._send('setCycle:', Fwd, 'init:')
		water3._send('setCycle:', Fwd, 'init:')
		water4._send('setCycle:', Fwd, 'init:')
		water5._send('setCycle:', Fwd, 'init:')
		plant._send('setCycle:', Fwd, 'init:')
		global102._send('number:', 915, 'loop:', -1, 'flags:', 1, 'play:')
		global103._send('number:', 917, 'flags:', 1, 'loop:', -1, 'play:')
		super._send('init:', &rest)
		ocean._send('init:')
		trees._send('init:')
		pathway._send('init:')
		stump._send('init:')
		rocks._send('init:')
		branch._send('init:')
		if (proc913_0(61) and (not proc913_0(45))):
			dangle._send('init:', 'setScript:', dangleScript, 'approachVerbs:', 5, 2, 85)
			global105._send('number:', 500, 'flags:', 1, 'loop:', -1, 'play:')
		#endif
		if (global12 == north):
			global0._send('init:', 'reset:', 2, 'posn:', 256, 91)
			global1._send('handsOn:')
		#endif
		global0._send('actions:', egoDoVerb)
		if (<= temp0 kernel.Random(1, 1000) 500):
			deer._send('init:', 'setScript:', deerScript)
		else:
			raccoon._send('init:', 'setLoop:', 14, 'setCycle:', End, raccoon)
		#endif
	#end:method

	@classmethod
	def doit():
		local4 = global0._send('onControl:', 1)
		(cond
			case script: 0#end:case
			case ((local4 & 0x0004) and local1):
				if (global0._send('view:') != 308):
					global104._send('number:', 922, 'loop:', -1, 'flags:', 1, 'play:')
					global0._send(
						'ignoreActors:', 1,
						'illegalBits:', 0,
						'view:', 308,
						'setPri:', 15,
						'setLoop:', 2,
						'setLoop:', -1
					)
				#endif
			#end:case
			case (local4 & 0x0040):
				if local2:
					local1 = 0
					local2 = 0
					global91._send('say:', 4, 3, 4)
					global0._send('setMotion:', 0)
				#endif
			#end:case
			case (local4 & 0x0002):
				if local1:
					global0._send('setMotion:', 0)
					while True: #repeat
						global0._send('posn:', global0._send('x:'), (global0._send('y:') - 1))
						(breakif (global0._send('onControl:', 1) & 0x0004))
					#end:loop
					global91._send('say:', 4, 3, 4)
					local1 = 0
				else:
					global1._send('handsOff:')
					self._send('setScript:', wateryDeathScr)
				#endif
			#end:case
			case ((not (local4 & 0x0004)) and (global0._send('view:') == 308)):
				global104._send('fade:', 0, 10, 15, 1)
				global0._send('reset:', 3)
				local1 = 1
			#end:case
			case (local4 & 0x4000):
				global2._send('newRoom:', north)
				global102._send('fade:')
			#end:case
		)
		super._send('doit:', &rest)
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		global102._send('fade:')
		global105._send('fade:', 0, 50, 50, 1)
		super._send('newRoom:', param1)
	#end:method

#end:class or instance

@SCI.instance
class water1(Actor):
	#property vars (may be empty)
	x = 293
	y = 164
	noun = 4
	view = 500
	signal = 16384
	cycleSpeed = 20
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class water2(Actor):
	#property vars (may be empty)
	x = 262
	y = 166
	noun = 4
	view = 500
	loop = 1
	cel = 2
	signal = 16384
	cycleSpeed = 25
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class water3(Actor):
	#property vars (may be empty)
	x = 116
	y = 152
	noun = 4
	view = 500
	loop = 2
	cel = 2
	signal = 16384
	cycleSpeed = 15
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class water4(Actor):
	#property vars (may be empty)
	x = 57
	y = 164
	noun = 4
	view = 500
	loop = 3
	signal = 16384
	cycleSpeed = 30
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class water5(Actor):
	#property vars (may be empty)
	x = 150
	y = 155
	noun = 4
	view = 500
	loop = 4
	cel = 2
	signal = 16384
	cycleSpeed = 20
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class dangle(Actor):
	#property vars (may be empty)
	x = 182
	y = 22
	noun = 7
	approachX = 189
	approachY = 103
	view = 479
	priority = 6
	signal = 24592
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 85:
				if (not global162):
					global91._send('say:', noun, 0, 10)
				else:
					global1._send('handsOff:')
					self._send('setScript:', getDangPartScript)
				#endif
			#end:case
			case 2:
				global1._send('handsOff:')
				self._send('setScript:', partKludgeScript, 0, 2)
			#end:case
			case 5:
				if (global162 > 0):
					global1._send('handsOff:')
					self._send('setScript:', partKludgeScript, 0, 5)
				else:
					global91._send('say:', 7, 5, 10, 1)
				#endif
			#end:case
			case 1:
				global91._send('say:', 7, 1, 0, 1)
			#end:case
			else:
				if global162:
					global91._send('say:', 7, 0, 11, 0)
				else:
					global91._send('say:', 7, 0, 10, 0)
				#endif
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class plant(Prop):
	#property vars (may be empty)
	x = 142
	y = 82
	view = 500
	loop = 5
	cel = 2
	cycleSpeed = 30
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class deer(Prop):
	#property vars (may be empty)
	x = 20
	y = 116
	noun = 10
	view = 503
	loop = 5
	detailLevel = 2
	
#end:class or instance

@SCI.instance
class raccoon(Actor):
	#property vars (may be empty)
	x = 282
	y = 114
	noun = 11
	view = 503
	loop = 13
	detailLevel = 2
	
	@classmethod
	def cue():
		self._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class ocean(Feature):
	#property vars (may be empty)
	noun = 4
	onMeCheck = 6
	
#end:class or instance

@SCI.instance
class trees(Feature):
	#property vars (may be empty)
	noun = 5
	onMeCheck = 16
	
#end:class or instance

@SCI.instance
class pathway(Feature):
	#property vars (may be empty)
	noun = 8
	onMeCheck = 8
	
#end:class or instance

@SCI.instance
class branch(Feature):
	#property vars (may be empty)
	noun = 5
	onMeCheck = 32
	
	@classmethod
	def doVerb(param1 = None, *rest):
		trees._send('doVerb:', param1)
	#end:method

#end:class or instance

@SCI.instance
class stump(Feature):
	#property vars (may be empty)
	noun = 12
	onMeCheck = 128
	
#end:class or instance

@SCI.instance
class rocks(Feature):
	#property vars (may be empty)
	noun = 2
	onMeCheck = 256
	
	@classmethod
	def doVerb(param1 = None, *rest):
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
class partKludgeScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				client._send('setCycle:', 0, 'setLoop:', 0)
				cycles = 2
			#end:case
			case 1:
				if (register == 2):
					match global162
						case 0:
							myConv._send(
								'add:', -1, 7, 2, 12, 1,
								'add:', -1, 7, 2, 12, 2,
								'add:', -1, 7, 2, 12, 3,
								'add:', -1, 7, 2, 12, 4,
								'init:', self
							)
							global162.post('++')
						#end:case
						case 1:
							myConv._send(
								'add:', -1, 7, 2, 13, 1,
								'add:', -1, 7, 2, 13, 2,
								'add:', -1, 7, 2, 13, 3,
								'add:', -1, 7, 2, 13, 4,
								'add:', -1, 7, 2, 13, 5,
								'init:', self
							)
							global162.post('++')
						#end:case
						case 2:
							myConv._send(
								'add:', -1, 7, 2, 14, 1,
								'add:', -1, 7, 2, 14, 2,
								'init:', self
							)
							global162.post('++')
						#end:case
						else:
							global91._send('say:', 7, 2, 15, 0, self)
						#end:else
					#end:match
				else:
					myConv._send('add:', -1, 7, 5, 11, 1, 'add:', -1, 7, 5, 11, 2, 'init:', self)
				#endif
			#end:case
			case 2:
				client._send('setLoop:', -1, 'setScript:', dangleScript)
				global1._send('handsOn:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getDangPartScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				dangle._send('setLoop:', 0, 'setCycle:', 0)
				cycles = 1
			#end:case
			case 1:
				myConv._send(
					'add:', -1, 7, 85, 0, 1,
					'add:', -1, 7, 85, 0, 2,
					'add:', -1, 7, 85, 0, 3,
					'add:', -1, 7, 85, 0, 4,
					'add:', -1, 7, 85, 0, 5,
					'init:', self
				)
			#end:case
			case 2:
				global0._send('hide:')
				dangle._send(
					'view:', 479,
					'setLoop:', 4,
					'posn:', 189, 102,
					'cel:', 0,
					'cycleSpeed:', 10,
					'setPri:', 14,
					'ignoreHorizon:', 1,
					'setCycle:', End, self
				)
			#end:case
			case 3:
				dangle._send(
					'view:', 478,
					'setLoop:', 1,
					'cel:', 0,
					'posn:', (dangle._send('x:') - 1), dangle._send('y:'),
					'setCycle:', End, self
				)
			#end:case
			case 4:
				dangle._send('setLoop:', 0, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 5:
				dangle._send('setCycle:', End, self)
			#end:case
			case 6:
				dangle._send('hide:')
				global0._send('put:', 50, 500, 'get:', 29, 'reset:', 4, 'show:')
				global105._send('fade:')
				global1._send('givePoints:', 2)
				proc913_1(45)
				cycles = 2
			#end:case
			case 7:
				global91._send('say:', 7, 85, 0, 6, self)
			#end:case
			case 8:
				global1._send('handsOn:')
				client._send('dispose:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class wateryDeathScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global91._send('say:', 4, 3, 7, 0, self)
			#end:case
			case 1:
				global2._send('walkOffEdge:', 1)
				global104._send('stop:', 'number:', 921, 'flags:', 1, 'loop:', 1, 'play:')
				global0._send(
					'view:', 269,
					'setLoop:', 1,
					'cel:', 0,
					'normal:', 0,
					'cycleSpeed:', 6,
					'setCycle:', End, self,
					'setMotion:', PolyPath, global0._send('x:'), 190, self
				)
			#end:case
			case 2: 0#end:case
			case 3:
				global2._send('newRoom:', 135)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class dangleScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				seconds = 2
			#end:case
			case 1:
				dangle._send('setLoop:', kernel.Random(1, 3), 'setCycle:', End, self)
			#end:case
			case 2:
				dangle._send('setCycle:', End, self)
			#end:case
			case 3:
				self._send('init:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class deerScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				seconds = kernel.Random(2, 5)
			#end:case
			case 1:
				deer._send('setCycle:', End, self)
			#end:case
			case 2:
				deer._send('setCel:', 0)
				cycles = 1
			#end:case
			case 3:
				self._send('init:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoDoVerb(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 12:
				global2._send('setScript:', 130)
				return 1
			#end:case
			else:
				return 0
			#end:else
		#end:match
	#end:method

#end:class or instance

