#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 440
import sci_sh
import kernel
import Main
import minoTrigger
import KQ6Room
import n913
import Conversation
import RandCycle
import PolyPath
import Polygon
import Feature
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm440 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None


@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class rm440(KQ6Room):
	#property vars (may be empty)
	picture = 440
	style = 10
	walkOffEdge = 1
	autoLoad = 0
	
	@classmethod
	def cue():
		if ((not proc913_0(1)) and (not kernel.ScriptID(30, 0)._send('seenByMino:'))):
			proc441_0()
		#endif
	#end:method

	@classmethod
	def init():
		if proc913_0(1):
			global2._send(
				'addObstacle:', Polygon._send('new:')._send(
						'type:', 2,
						'init:', 178, 157, 208, 157, 241, 151, 239, 157, 319, 157, 319, 0, 0, 0, 0, 181, 43, 181, 86, 151, 75, 151, 83, 148, 125, 145, 128, 151, 168, 147,
						'yourself:'
					), Polygon._send('new:')._send(
						'type:', 2,
						'init:', 0, 185, 296, 185, 265, 173, 248, 163, 319, 163, 319, 186, 0, 189,
						'yourself:'
					)
			)
		else:
			kernel.Load(130, 441)
			global2._send(
				'addObstacle:', Polygon._send('new:')._send(
						'type:', 2,
						'init:', 295, 0, 40, 179, 0, 179, 0, 0,
						'yourself:'
					), Polygon._send('new:')._send(
						'type:', 2,
						'init:', 0, 185, 152, 185, 151, 189, 0, 189,
						'yourself:'
					)
			)
		#endif
		super._send('init:', &rest)
		kernel.ScriptID(30, 0)._send('cue:')
		flames._send('setCycle:', RandCycle, 'init:')
		global32._send(
			'add:', alter, toLabExit, exitSkull, alterSkulls, toCliffsExit,
			'eachElementDo:', #init
		)
		if proc913_0(1):
			local0 = 7
		else:
			proc441_1()
			local2 = 8
			local0 = 6
		#endif
		global0._send('init:', 'reset:', 'actions:', egoDoMinotaurCode)
		self._send('setScript:', walkIn)
	#end:method

	@classmethod
	def dispose():
		actTimer._send('dispose:')
		kernel.DisposeScript(441)
		super._send('dispose:')
	#end:method

	@classmethod
	def doit():
		(cond
			case self._send('script:'):#end:case
			case 
				(and
					(not kernel.ScriptID(30, 0)._send('seenByMino:'))
					(not proc913_0(1))
					(global0._send('onControl:', 1) == 4)
				):
				proc441_2()
			#end:case
			case (global0._send('onControl:', 1) == 256):
				self._send('setScript:', fallInPit)
			#end:case
			case (global0._send('onControl:', 1) == 16384):
				global2._send('setScript:', walkOut, 0, 0)
			#end:case
			case (global0._send('onControl:', 1) == 8192):
				if proc913_0(1):
					global2._send('setScript:', walkOut, 0, 1)
				else:
					global0._send('setMotion:', 0, 'posn:', (global0._send('x:') + 2), global0._send('y:'))
					global91._send('say:', 11, 3, 8, 1)
				#endif
			#end:case
		)
		super._send('doit:', &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		(return
			match param1
				case 1:
					global91._send('say:', 2, 1, local0, 1)
					1
				#end:case
				case 5:
					global91._send('say:', 2, 5, local0, 1)
					1
				#end:case
				case 2:
					(cond
						case proc913_0(1):
							global91._send('say:', 2, 2, 7, 1)
						#end:case
						case kernel.ScriptID(30, 0)._send('seenByMino:'):
							global91._send('say:', 2, 2, 9, 1)
						#end:case
						else:
							global91._send('say:', 2, 2, 8, 0, self)
						#end:else
					)
					1
				#end:case
				else:
					global91._send('say:', 2, 0, local0, 1, self)
					1
				#end:else
			#end:match
		)
	#end:method

#end:class or instance

@SCI.instance
class alter(Feature):
	#property vars (may be empty)
	x = 60
	y = 110
	noun = 12
	onMeCheck = 4096
	
#end:class or instance

@SCI.instance
class toLabExit(Feature):
	#property vars (may be empty)
	x = 10
	y = 170
	noun = 11
	onMeCheck = 1024
	
#end:class or instance

@SCI.instance
class toCliffsExit(Feature):
	#property vars (may be empty)
	x = 330
	y = 140
	noun = 9
	onMeCheck = 8192
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				global91._send('say:', 9, 1, local0, 1, 0, 440)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class alterSkulls(Feature):
	#property vars (may be empty)
	x = 60
	y = 110
	noun = 13
	onMeCheck = 2048
	
#end:class or instance

@SCI.instance
class exitSkull(Feature):
	#property vars (may be empty)
	x = 330
	y = 140
	noun = 10
	onMeCheck = 512
	
#end:class or instance

@SCI.instance
class flames(Prop):
	#property vars (may be empty)
	x = 203
	y = 147
	noun = 6
	view = 445
	priority = 1
	signal = 16400
	cycleSpeed = 8
	detailLevel = 3
	
#end:class or instance

@SCI.instance
class walkIn(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				if (global12 == 340):
					global0._send('posn:', 310, 160, 'setMotion:', PolyPath, 230, 160, self)
				else:
					global0._send('posn:', -5, 187, 'setMotion:', MoveTo, 38, 184, self)
				#endif
			#end:case
			case 1:
				if proc913_0(1):
					self._send('cue:')
				else:
					global102._send('number:', 440, 'setLoop:', -1, 'play:')
					global0._send('setHeading:', 0)
					proc913_1(161)
					global105._send('number:', 433, 'setLoop:', 1, 'play:')
					cycles = 10
				#endif
			#end:case
			case 2:
				if (not proc913_0(1)):
					if proc913_0(142):
						global91._send('say:', 1, 0, 19, 0, self, 440)
					else:
						global91._send('say:', 1, 0, 1, 0, self, 440)
					#endif
				else:
					self._send('cue:')
				#endif
			#end:case
			case 3:
				global1._send('handsOn:')
				if (not proc913_0(1)):
					kernel.ScriptID(30, 0)._send('setScript:', actTimer)
				#endif
				self._send('dispose:')
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
				if register:
					global0._send('setMotion:', PolyPath, 315, global0._send('y:'), self)
				else:
					global0._send('setMotion:', MoveTo, -15, global0._send('y:'), self)
				#endif
			#end:case
			case 1:
				global1._send('handsOn:')
				if register:
					global2._send('newRoom:', 340)
				else:
					kernel.ScriptID(30, 0)._send('prevEdgeHit:', 4)
					global2._send('newRoom:', 409)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class fallInPit(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send(
					'view:', 441,
					'normal:', 0,
					'setLoop:', (5 if (global0._send('x:') < 185) else 4),
					'cel:', 0,
					'setMotion:', 0,
					'cycleSpeed:', 2
				)
				cycles = 6
			#end:case
			case 1:
				global91._send('say:', 6, 3, 0, 1, self)
			#end:case
			case 2:
				global91._send('say:', 6, 3, 0, 2, self)
			#end:case
			case 3:
				global0._send(
					'setPri:', (2 if (global0._send('x:') < 185) else -1),
					'setCycle:', End
				)
				global102._send('stop:')
				global105._send('number:', 442, 'setLoop:', 1, 'play:', self)
			#end:case
			case 4:
				ticks = 4
			#end:case
			case 5:
				seconds = 2
			#end:case
			case 6:
				proc0_1(15)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class actTimer(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				seconds = 20
			#end:case
			case 1:
				global91._send('say:', 1, 0, 18, 1, self)
			#end:case
			case 2:
				proc441_0()
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoDoMinotaurCode(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				return 0
			#end:case
			case 1:
				return 0
			#end:case
			case 2:
				return 0
			#end:case
			case 17:
				if proc913_0(1):
					global91._send('say:', 3, 17, 7, 1)
				else:
					global91._send('say:', 3, 17, 6, 1)
				#endif
				return 1
			#end:case
			case 72:
				if (global2._send('script:') == kernel.ScriptID(441, 3)):
					kernel.ScriptID(30, 0)._send('scarfOnMino:', 1)
					global0._send('view:', 441, 'normal:', 0, 'setLoop:', 0, 'cel:', 0)
					kernel.UnLoad(128, 900)
					kernel.ScriptID(441, 4)._send('cycleSpeed:', 6, 'setCycle:', Fwd)
					kernel.ScriptID(441, 3)._send('state:', 19, 'register:', 72, 'cue:')
					global1._send('handsOff:')
					global1._send('givePoints:', 3)
				#endif
			#end:case
			else:
				if (not proc913_0(1)):
					global91._send('say:', 3, 0, 6, 1)
					return 1
				else:
					global91._send('say:', 0, 0, 184, 1, 0, 899)
					return 1
				#endif
			#end:else
		#end:match
	#end:method

#end:class or instance

