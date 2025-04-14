#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 350
import sci_sh
import kernel
import Main
import KQ6Room
import n913
import Conversation
import Scaler
import PolyPath
import Polygon
import Feature
import LoadMany
import StopWalk
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm350 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class rm350(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 350
	
	@classmethod
	def init():
		super._send('init:', &rest)
		global102._send('number:', 350, 'setLoop:', -1, 'play:')
		global2._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 304, 189, 268, 167, 233, 162, 169, 162, 169, 150, 148, 150, 148, 162, 79, 162, 47, 169, 14, 189, 0, 189, 0, 0, 319, 0, 319, 189,
					'yourself:'
				)
		)
		if (not proc913_0(2)):
			proc958_0(128, 343, 344, 348, 3481, 349, 3491)
		#endif
		global32._send('add:', nests, palace, oracleMtn, gate, 'eachElementDo:', #init)
		leftGuard._send('init:')
		riteGuard._send('init:')
		global0._send('reset:', 3, 'posn:', 160, 188, 'init:')
		if (not proc913_0(2)):
			global69._send(
				'enable:',
				'disable:', 0, 1, 2, 3, 4, 5, 6,
				'height:', -100,
				'activateHeight:', -100
			)
			Cursor._send('showCursor:', 0)
			global2._send('setScript:', egoEnters)
		else:
			global1._send('handsOn:')
		#endif
	#end:method

	@classmethod
	def doit():
		(cond
			case global2._send('script:'):#end:case
			case (global0._send('onControl:', 1) == 64):
				global2._send('setScript:', stayOut)
			#end:case
			case (global0._send('edgeHit:') == 3):
				global2._send('setScript:', walkOut)
			#end:case
		)
		super._send('doit:')
	#end:method

	@classmethod
	def dispose():
		global0._send('setScale:', 0)
		super._send('dispose:')
	#end:method

	@classmethod
	def scriptCheck(param1 = None, *rest):
		temp0 = 1
		if (param1 == 87):
			global91._send('say:', 0, 0, 94, 1, 0, 899)
			temp0 = 0
		#endif
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class gate(Feature):
	#property vars (may be empty)
	noun = 5
	onMeCheck = 2
	
#end:class or instance

@SCI.instance
class nests(Feature):
	#property vars (may be empty)
	noun = 6
	onMeCheck = 4
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				global91._send('say:', 6, 1, 0, 1)
			#end:case
			case 2:
				global91._send('say:', 6, 2, 0, 1)
			#end:case
			else:
				global91._send('say:', 6, 5, 0, 1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class palace(Feature):
	#property vars (may be empty)
	noun = 8
	onMeCheck = 16
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				global91._send('say:', 8, 1, 0, 1)
			#end:case
			case 2:
				global91._send('say:', 6, 2, 0, 1)
			#end:case
			else:
				global91._send('say:', 6, 5, 0, 1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class oracleMtn(Feature):
	#property vars (may be empty)
	noun = 7
	onMeCheck = 32
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				global91._send('say:', 7, 1, 0, 1)
			#end:case
			case 2:
				global91._send('say:', 7, 2, 0, 1)
			#end:case
			else:
				global91._send('say:', 7, 5, 0, 1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class stayOut(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', 0)
				leftGuard._send(
					'view:', 345,
					'setLoop:', 1,
					'cel:', 0,
					'cycleSpeed:', 8,
					'setCycle:', End
				)
				riteGuard._send(
					'view:', 345,
					'setLoop:', 0,
					'cel:', 0,
					'cycleSpeed:', 8,
					'setCycle:', End, self
				)
			#end:case
			case 1:
				global91._send('say:', 4, 2, 8, 2, self)
			#end:case
			case 2:
				global0._send(
					'setLoop:', global0._send('cel:'),
					'setMotion:', MoveTo, global0._send('x:'), (global0._send('y:') + 5), self
				)
			#end:case
			case 3:
				global0._send('setLoop:', -1)
				leftGuard._send('setCycle:', Beg)
				riteGuard._send('setCycle:', Beg, self)
			#end:case
			case 4:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class dummyEgo(Actor):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class egoEnters(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', MoveTo, 160, 160, self)
			#end:case
			case 1:
				cycles = 6
			#end:case
			case 2:
				global91._send('say:', 1, 0, 1, 1, self)
			#end:case
			case 3:
				leftGuard._send('setCycle:', StopWalk, -1, 'setMotion:', MoveTo, 134, 158)
				riteGuard._send('setCycle:', StopWalk, -1, 'setMotion:', MoveTo, 189, 158, self)
			#end:case
			case 4:
				leftGuard._send('setHeading:', 90, self)
				riteGuard._send('setHeading:', 270, self)
			#end:case
			case 5: 0#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				myConv._send(
					'add:', -1, 1, 0, 1, 2,
					'add:', -1, 1, 0, 1, 3,
					'add:', -1, 1, 0, 1, 4,
					'add:', -1, 1, 0, 1, 5,
					'add:', -1, 1, 0, 1, 6,
					'add:', -1, 1, 0, 1, 7,
					'init:', self
				)
			#end:case
			case 8:
				leftGuard._send('dispose:')
				riteGuard._send('dispose:')
				global0._send('hide:')
				dummyEgo._send('view:', 351, 'posn:', 160, 164, 'init:', 'setCycle:', End, self)
				kernel.UnLoad(128, 900)
			#end:case
			case 9:
				dummyEgo._send(
					'view:', 352,
					'ignoreHorizon:',
					'cycleSpeed:', 6,
					'moveSpeed:', 6,
					'posn:', 160, 164,
					'setCycle:', End, self
				)
				kernel.UnLoad(128, 351)
			#end:case
			case 10:
				dummyEgo._send(
					'view:', 353,
					'posn:', 162, 103,
					'setCycle:', Fwd,
					'cycleSpeed:', 3,
					'setStep:', 15, 12,
					'setMotion:', MoveTo, global0._send('x:'), -50, self
				)
				kernel.UnLoad(128, 352)
			#end:case
			case 11:
				dummyEgo._send(
					'view:', 353,
					'setScale:', Scaler, 50, 49, 190, 0,
					'setLoop:', 1,
					'setStep:', 3, 2,
					'posn:', 230, -20,
					'setCycle:', Fwd,
					'setMotion:', MoveTo, 139, 7, self
				)
			#end:case
			case 12:
				global102._send('fade:', 0, 20, 15)
				global2._send('newRoom:', 370)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walkOut(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send(
					'setMotion:', MoveTo, global0._send('x:'), (global0._send('y:') + 50), self
				)
			#end:case
			case 1:
				global102._send('fade:', 0, 15, 15)
				global2._send('newRoom:', 340)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class leftGuard(Actor):
	#property vars (may be empty)
	x = 120
	y = 150
	noun = 4
	approachX = 120
	approachY = 160
	yStep = 3
	view = 344
	loop = 2
	signal = 24576
	xStep = 5
	
	@classmethod
	def init():
		self._send('approachVerbs:', 0)
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 2:
				if proc913_0(101):
					global2._send('setScript:', talkToGuards)
				else:
					proc913_1(101)
					super._send('doVerb:', param1, &rest)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class riteGuard(Actor):
	#property vars (may be empty)
	x = 200
	y = 150
	noun = 4
	approachX = 200
	approachY = 160
	yStep = 3
	view = 343
	loop = 2
	signal = 24576
	xStep = 5
	
	@classmethod
	def init():
		self._send('approachVerbs:', 0)
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 2:
				if proc913_0(101):
					global2._send('setScript:', talkToGuards)
				else:
					proc913_1(101)
					super._send('doVerb:', param1, &rest)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class talkToGuards(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 160, 160, self)
			#end:case
			case 1:
				cycles = 4
			#end:case
			case 2:
				global91._send('say:', 4, 2, 8, 0, self)
			#end:case
			case 3:
				global0._send('setLoop:', 3, 'setMotion:', MoveTo, 160, 175, self)
			#end:case
			case 4:
				global0._send('reset:', 3)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

