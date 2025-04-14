#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 640
import sci_sh
import kernel
import Main
import KQ6Print
import KQ6Room
import n913
import Scaler
import MCyc
import PolyPath
import Polygon
import Feature
import LoadMany
import Rev
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm640 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = [0, -3, 12, 11]
local4 = [0, 8, 9, 9]
local8 = [2, 0, 124, 93, 2, 1, 128, 74, 2, 2, 143, 61, 2, 3, 152, 60, 2, 4, 153, 75, 2, 5, 154, 94, 2, 6, 159, 121, 2, 7, 161, 149, 2, 8, 159, 167, -32768]
local45 = [2, 9, 166, 154, 2, 10, 178, 153, 2, 11, 182, 156, 2, 12, 185, 167, -32768]
local62 = [0, 0, 194, 135, 0, 1, 197, 135, 0, 2, 214, 120, 0, 3, 226, 116, 0, 4, 226, 110, 0, 5, 238, 95, 0, 6, 252, 87, 0, 7, 239, 108, 0, 8, 205, 130, 0, 9, 205, 130, -32768]


@SCI.instance
class rm640(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 640
	horizon = 0
	north = 650
	south = 630
	
	@classmethod
	def init():
		global2._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 0, 189, 0, -10, 319, -10, 319, 189, 227, 189, 191, 160, 181, 142, 149, 120, 156, 108, 140, 98, 148, 91, 142, 86, 142, 42, 135, 42, 135, 87, 119, 95, 119, 99, 135, 107, 121, 117, 122, 126, 132, 139, 142, 150, 142, 175, 27, 175, 49, 189,
					'yourself:'
				)
		)
		super._send('init:', &rest)
		kernel.Lock(143, modNum, 0)
		global69._send('enable:')
		global1._send('handsOff:')
		global0._send('init:', 'reset:', 3, 'setScale:', Scaler, 100, 70, 200, 70)
		doorMaster._send(
			'init:',
			'signal:', (| doorMaster._send('signal:') 0x1000),
			'approachVerbs:', 2, 0
		)
		keyMaster._send('init:', 'signal:', (| keyMaster._send('signal:') 0x1000), 'approachVerbs:', 2)
		(cond
			case global0._send('has:', 44): 0#end:case
			case proc913_0(115):
				boneKey._send(
					'init:',
					'view:', 647,
					'setLoop:', 0,
					'cel:', 1,
					'posn:', (keyMaster._send('x:') + 78), (keyMaster._send('y:') + 1),
					'noun:', 7,
					'ignoreActors:', 1
				)
			#end:case
			else:
				boneKey._send(
					'init:',
					'posn:', (keyMaster._send('x:') + 16), (keyMaster._send('y:') - 14),
					'ignoreActors:', 1
				)
			#end:else
		)
		skelLeft._send('init:')
		skelRight._send('init:')
		boneMallet._send('init:')
		ghost._send('init:', 'setScript:', ghostScr)
		door._send('init:')
		theSkull._send('init:')
		xylophone._send('init:')
		if proc913_0(44):
			global102._send('stop:')
			global103._send('stop:')
			global104._send('stop:')
			global105._send('stop:')
			self._send('setScript:', deathCartoonScr)
		else:
			global0._send('setScript:', musicStuffScript)
			lineGhost._send('init:', 'setScript:', ghostLineScr)
			match global12
				case 650:
					global0._send('posn:', 133, 97)
				#end:case
				else:
					global0._send('posn:', 109, 187)
				#end:else
			#end:match
		#endif
	#end:method

	@classmethod
	def doit():
		super._send('doit:', &rest)
		temp0 = global0._send('onControl:', 1)
		(cond
			case script: 0#end:case
			case (temp0 == 16384):
				global1._send('handsOff:')
				self._send('setScript:', goNoFarther)
			#end:case
		)
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:', &rest)
		proc958_0(0, 969, 942)
	#end:method

#end:class or instance

@SCI.instance
class musicStuffScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global102._send('number:', 640, 'loop:', 1, 'play:', self)
			#end:case
			case 1:
				global102._send('stop:')
				global102._send('number:', 600, 'loop:', -1, 'play:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class goNoFarther(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				doorMaster._send(
					'view:', 6407,
					'loop:', 0,
					'cel:', 0,
					'posn:', (doorMaster._send('x:') + 6), (doorMaster._send('y:') + 19),
					'setCycle:', End, self
				)
			#end:case
			case 1:
				ticks = 30
			#end:case
			case 2:
				global0._send('setHeading:', 45, self)
			#end:case
			case 3:
				ticks = 15
			#end:case
			case 4:
				global91._send('say:', 8, 3, 0, 2, self)
			#end:case
			case 5:
				if (global0._send('x:') > 129):
					global0._send(
						'setLoop:', 6,
						'setCycle:', Rev,
						'setMotion:', MoveTo, (global0._send('x:') - 4), (+
								global0._send('y:')
								7
							), self
					)
				else:
					global0._send(
						'setLoop:', 3,
						'setCycle:', Rev,
						'setMotion:', MoveTo, global0._send('x:'), (global0._send('y:') + 7), self
					)
				#endif
			#end:case
			case 6:
				global0._send('setCycle:', 0, 'setLoop:', -1)
				doorMaster._send('cel:', 5, 'setCycle:', Beg, self)
			#end:case
			case 7:
				doorMaster._send(
					'view:', 642,
					'loop:', 0,
					'cel:', 0,
					'posn:', (doorMaster._send('x:') - 6), (doorMaster._send('y:') - 19)
				)
				cycles = 1
			#end:case
			case 8:
				global0._send('reset:', 6)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class deathCartoonScr(Script):
	#property vars (may be empty)
	@classmethod
	def doit():
		super._send('doit:')
		(cond
			case (global0._send('has:', 44) or proc913_0(115)): 0#end:case
			case (keyMaster._send('view:') == 6404):
				boneKey._send('posn:', (keyMaster._send('x:') + 14), (keyMaster._send('y:') - 14))
			#end:case
			case (keyMaster._send('loop:') == 1):
				match keyMaster._send('cel:')
					case 7:
						boneKey._send(
							'posn:', (keyMaster._send('x:') + 9), (keyMaster._send('y:') - 16)
						)
					#end:case
					case 9:
						boneKey._send(
							'posn:', (keyMaster._send('x:') + 9), (keyMaster._send('y:') - 18)
						)
					#end:case
					case 10:
						boneKey._send(
							'posn:', (keyMaster._send('x:') + 16), (keyMaster._send('y:') - 14)
						)
					#end:case
				#end:match
			#end:case
			case (keyMaster._send('loop:') == 2):
				boneKey._send('posn:', (keyMaster._send('x:') + 13), (keyMaster._send('y:') - 16))
			#end:case
		)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cycles = 2
				global0._send('hide:')
			#end:case
			case 1:
				global102._send('loop:', 1, 'number:', 975, 'flags:', 1, 'play:')
				keyMaster._send('view:', 643, 'loop:', 1, 'cel:', 0, 'setCycle:', End, self)
				global0._send(
					'posn:', 146, 174,
					'show:',
					'view:', 6402,
					'loop:', 0,
					'cel:', 0,
					'normal:', 0,
					'cycleSpeed:', 15,
					'setCycle:', CT, 4, 1, self
				)
			#end:case
			case 2: 0#end:case
			case 3:
				keyMaster._send('loop:', 1, 'cel:', 0)
				global0._send('setCycle:', End, self)
			#end:case
			case 4:
				keyMaster._send(
					'view:', 6404,
					'loop:', 0,
					'cel:', 0,
					'posn:', keyMaster._send('x:'), (keyMaster._send('y:') - 3)
				)
				global0._send('posn:', 142, 133, 'loop:', 1, 'cel:', 0, 'setCycle:', CT, 1, 1, self)
			#end:case
			case 5:
				self._send('setScript:', modeLessScript)
				doorMaster._send('view:', 6406, 'loop:', 0, 'cel:', 0, 'setCycle:', CT, 2, 1, self)
			#end:case
			case 6:
				doorMaster._send('setCycle:', End)
				global0._send('setCycle:', End, self)
			#end:case
			case 7:
				doorMaster._send('loop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 8:
				modeLessScript._send('cue:')
				doorMaster._send('view:', 6406, 'loop:', 0, 'cel:', 0)
				global0._send('loop:', 2, 'cel:', 0, 'cycleSpeed:', 10, 'setCycle:', End, self)
			#end:case
			case 9:
				door._send('setCycle:', End, self)
			#end:case
			case 10:
				global0._send('dispose:')
				door._send('setCycle:', Beg, self)
			#end:case
			case 11:
				global5._send('eachElementDo:', #addToPic)
				seconds = 3
			#end:case
			case 12:
				if global25:
					global25._send('dispose:')
				#endif
				global1._send('setCursor:', global20)
				while True: #repeat
					match
						KQ6Print._send(
							'posn:', -1, 10,
							'addIcon:', 649, 0, 0, 67, 1,
							'say:', 1, 0, 0, global160, 1, 0, 40, 916,
							'addButton:', 1, r"""Restore""", 0, 78,
							'addButton:', 2, r"""Restart""", 67, 78,
							'addButton:', 3, r"""Quit""", 134, 78,
							'init:'
						)
						case 1:
							global1._send('restore:')
						#end:case
						case 2:
							global1._send('restart:', 1)
						#end:case
						case 3:
							global4 = 1
							(break)
						#end:case
					#end:match
				#end:loop
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class modeLessScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				KQ6Print._send(
					'font:', global22,
					'posn:', 200, 100,
					'say:', 0, 1, 0, 1, 1,
					'modeless:', 1,
					'init:'
				)
				seconds = 4
			#end:case
			case 1:
				if global25:
					global25._send('dispose:')
				#endif
			#end:case
			case 2:
				KQ6Print._send(
					'font:', global22,
					'posn:', 200, 100,
					'say:', 0, 1, 0, 1, 2,
					'modeless:', 1,
					'init:'
				)
				seconds = 3
			#end:case
			case 3:
				if global25:
					global25._send('dispose:')
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoGiveTicketScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('givePoints:', 3)
				global0._send('put:', 28, 640)
				global0._send('setMotion:', PolyPath, 145, 133, self)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				global91._send('say:', 5, 49, 0, 1, self)
			#end:case
			case 3:
				global0._send('setHeading:', 0, self)
			#end:case
			case 4:
				self._send('setScript:', takeTicketScr, self)
			#end:case
			case 5:
				takeTicketScr._send('cue:')
			#end:case
			case 6:
				global91._send('say:', 5, 49, 0, 2, self)
			#end:case
			case 7:
				global0._send('reset:', 0)
				cycles = 1
			#end:case
			case 8:
				global0._send('setMotion:', PolyPath, 139, 90, self)
			#end:case
			case 9:
				door._send('setCycle:', End, self)
			#end:case
			case 10:
				global0._send('dispose:')
				door._send('setCycle:', Beg, self)
			#end:case
			case 11:
				global2._send('newRoom:', global2._send('north:'))
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class takeTicketScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if (client != egoGiveTicketScr):
					global91._send('say:', 1, 0, 2, 2, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				doorMaster._send('view:', 6406, 'loop:', 0, 'cel:', 0, 'setCycle:', CT, 2, 1, self)
			#end:case
			case 2:
				client._send('cue:')
			#end:case
			case 3:
				doorMaster._send('setCycle:', End, self)
			#end:case
			case 4:
				doorMaster._send('loop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 5:
				doorMaster._send('view:', 642, 'loop:', 0, 'cel:', 0)
				cycles = 2
			#end:case
			case 6:
				if (client != egoGiveTicketScr):
					global91._send('say:', 1, 0, 2, 3, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 7:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class ghostLineScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				client._send('setCycle:', End, self)
			#end:case
			case 1:
				client._send('cel:', 0, 'loop:', 0, 'posn:', 141, 167, 'setCycle:', End, self)
			#end:case
			case 2:
				client._send('cel:', 0, 'loop:', 1, 'setCycle:', Fwd)
				keyMaster._send('view:', 643, 'loop:', 1, 'cel:', 0, 'setCycle:', CT, 9, 1, self)
			#end:case
			case 3:
				client._send('cel:', 0, 'loop:', 2, 'setCycle:', End, self)
				keyMaster._send('setCycle:', End, self)
			#end:case
			case 4: 0#end:case
			case 5:
				keyMaster._send('loop:', 1, 'cel:', 0)
				cycles = 2
			#end:case
			case 6:
				global91._send('say:', 1, 0, 2, 1, self)
			#end:case
			case 7:
				client._send('cel:', 0, 'loop:', 3, 'y:', 136, 'setCycle:', Fwd)
				ticks = 30
			#end:case
			case 8:
				self._send('setScript:', takeTicketScr, self)
			#end:case
			case 9:
				script._send('cue:')
			#end:case
			case 10:
				client._send('cel:', 0, 'loop:', 4, 'setCycle:', End, self)
			#end:case
			case 11:
				door._send('setCycle:', End, self)
			#end:case
			case 12:
				client._send('hide:')
				door._send('setCycle:', Beg, self)
			#end:case
			case 13:
				keyMaster._send('view:', 6404, 'loop:', 0, 'cel:', 0)
				client._send('dispose:')
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class playXylophone(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('setMotion:', PolyPath, 200, 185, self)
			#end:case
			case 1:
				global0._send(
					'normal:', 0,
					'view:', 641,
					'posn:', (boneMallet._send('x:') - 3), (boneMallet._send('y:') + 9),
					'setLoop:', 0,
					'cycleSpeed:', 10,
					'cel:', 0,
					'setCycle:', End, self
				)
				boneMallet._send('hide:')
			#end:case
			case 2:
				kernel.UnLoad(128, 900)
				if proc913_0(100):
					global91._send('say:', 6, 5, 4, 1, self)
				else:
					global91._send('say:', 6, 5, 3, 1, self)
				#endif
			#end:case
			case 3:
				if proc913_0(100):
					cycles = 1
				else:
					global1._send('givePoints:', 2)
					global91._send('say:', 6, 5, 3, 2, self)
					proc913_1(100)
				#endif
				if global0._send('script:'):
					global0._send('setScript:', 0)
				#endif
				global102._send('stop:')
			#end:case
			case 4:
				global0._send(
					'posn:', (boneMallet._send('x:') + local0[1]), (+
							boneMallet._send('y:')
							local4[1]
						),
					'setLoop:', 1,
					'setCycle:', End, self
				)
			#end:case
			case 5:
				global102._send('number:', 641, 'loop:', 1, 'play:')
				global102._send('prevSignal:', 0)
				keyMaster._send('setScript:', keyDanceScript)
				register = 2
				cycles = 1
			#end:case
			case 6:
				global0._send(
					'posn:', (boneMallet._send('x:') + local0[register]), (+
							boneMallet._send('y:')
							local4[register]
						),
					'setLoop:', register,
					'setCycle:', End, self
				)
			#end:case
			case 7:
				if (global102._send('prevSignal:') == -1):
					keyDanceScript._send('cue:')
					global102._send('number:', 600, 'loop:', -1, 'play:')
					cycles = 1
				else:
					register = kernel.Random(2, 3)
					self._send('start:', 6, 'init:')
				#endif
			#end:case
			case 8:
				global0._send(
					'posn:', (boneMallet._send('x:') + local0[1]), (+
							boneMallet._send('y:')
							local4[1]
						),
					'setLoop:', 1
				)
				global0._send('cel:', global0._send('lastCel:'), 'setCycle:', Beg, self)
			#end:case
			case 9:
				global0._send('setLoop:', 0, 'cel:', 5, 'setCycle:', Beg, self)
			#end:case
			case 10:
				boneMallet._send('show:')
				global0._send('reset:', 0, 'posn:', 198, 181)
				cycles = 1
			#end:case
			case 11:
				global91._send('say:', 6, 5, 3, 4, self)
			#end:case
			case 12: 0#end:case
			case 13:
				doorMaster._send('view:', 642, 'setLoop:', 0, 'cel:', 0, 'setCycle:', 0)
				global1._send('handsOn:')
				self._send('start:', 0, 'dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def doit():
		super._send('doit:')
		if ((state == 6) and (global102._send('prevSignal:') == -1)):
			global0._send('setCycle:', 0)
			self._send('cue:')
		#endif
		if ((state == 12) and (not chorusRight._send('script:'))):
			self._send('cue:')
		#endif
	#end:method

#end:class or instance

@SCI.instance
class keyDanceScript(Script):
	#property vars (may be empty)
	@classmethod
	def doit():
		super._send('doit:')
		if 
			(and
				global5._send('contains:', chorusRight)
				(not chorusRight._send('script:'))
				(global102._send('prevSignal:') == 10)
			)
			global102._send('prevSignal:', 1)
			chorusRight._send('setScript:', chorusScript, 0, 0)
			skelLeft._send('script:')._send('cue:')
			skelRight._send('script:')._send('cue:')
		#endif
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				register = 0
				seconds = 3
			#end:case
			case 1:
				global102._send('pause:')
				KQ6Print._send('font:', global22, 'posn:', -1, 10, 'say:', 0, 6, 5, 3, 3, 'init:', self)
			#end:case
			case 2:
				global102._send('pause:', 0)
				skelLeft._send('setScript:', skelLeftScript)
				skelRight._send('setScript:', skelRightScript)
				doorMaster._send('view:', 646, 'setLoop:', 0, 'cel:', 0)
				chorusRight._send('init:')
				seconds = 10
			#end:case
			case 3:
				doorMaster._send('setScript:', doorScript)
				seconds = 10
			#end:case
			case 4:
				keyMaster._send('view:', 645, 'setLoop:', 0, 'cel:', 0, 'setCycle:', Fwd)
				if ((not global0._send('has:', 44)) and (not proc913_0(115))):
					boneKey._send('view:', 645, 'setLoop:', 1, 'cel:', 1)
					register = 1
				#endif
				seconds = 20
			#end:case
			case 5:
				register = 0
				if ((not global0._send('has:', 44)) and (not proc913_0(115))):
					boneKey._send(
						'setLoop:', 2,
						'cel:', 0,
						'posn:', keyMaster._send('x:'), keyMaster._send('y:'),
						'cycleSpeed:', 0,
						'setCycle:', MCyc, @local8, self
					)
					global103._send('number:', 825, 'loop:', 1)
				else:
					cycles = 1
				#endif
			#end:case
			case 6:
				if ((not global0._send('has:', 44)) and (not proc913_0(115))):
					global103._send('play:')
					boneKey._send('setCycle:', MCyc, @local45, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 7:
				if ((not global0._send('has:', 44)) and (not proc913_0(115))):
					global103._send('play:')
					proc913_1(115)
					boneKey._send('view:', 647, 'loop:', 0, 'cel:', 1, 'noun:', 7)
				#endif
				doorMaster._send('script:')._send('cue:')
			#end:case
			case 8:
				keyMaster._send('view:', 6404, 'setLoop:', 0, 'cel:', 0, 'setCycle:', 0)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class skelLeftScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				skelLeft._send('view:', 6403, 'setLoop:', 1, 'cel:', 0, 'setCycle:', Fwd)
			#end:case
			case 1:
				skelLeft._send('view:', 644, 'setLoop:', 0, 'cel:', 0, 'setCycle:', 0)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class skelRightScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				skelRight._send('view:', 6403, 'setLoop:', 0, 'cel:', 0, 'setCycle:', Fwd)
			#end:case
			case 1:
				skelRight._send('view:', 644, 'setLoop:', 0, 'cel:', 0, 'setCycle:', 0)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class doorScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				doorMaster._send('setCycle:', Fwd)
			#end:case
			case 1:
				doorMaster._send('setLoop:', 0, 'cel:', 0, 'setCycle:', 0)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class chorusScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				chorusRight._send('setCycle:', Fwd, 'setMotion:', MoveTo, 160, 184, self)
				chorusMid._send('init:')
				chorusLeft._send('init:')
			#end:case
			case 1:
				chorusRight._send('setCycle:', Fwd, 'setMotion:', MoveTo, -18, 184, self)
			#end:case
			case 2:
				if (not register):
					chorusMid._send('dispose:')
					chorusLeft._send('dispose:')
					chorusRight._send('dispose:')
					self._send('dispose:')
				else:
					register.post('--')
					self._send('init:')
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getKeyScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send(
					'setMotion:', PolyPath, (boneKey._send('x:') - 41), boneKey._send('y:'), self
				)
			#end:case
			case 1:
				global0._send(
					'normal:', 0,
					'view:', 6405,
					'setLoop:', 3,
					'cel:', 0,
					'posn:', (boneKey._send('x:') - 20), (boneKey._send('y:') + 5),
					'setCycle:', CT, 3, 1, self
				)
			#end:case
			case 2:
				boneKey._send('dispose:')
				global0._send('setCycle:', End, self)
			#end:case
			case 3:
				global0._send(
					'reset:', 0,
					'posn:', (global0._send('x:') - 21), (global0._send('y:') - 5),
					'get:', 44
				)
				global1._send('givePoints:', 1)
				proc913_2(115)
				cycles = 1
			#end:case
			case 4:
				global91._send('say:', 7, 5, 0, 1, self)
			#end:case
			case 5:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class ghostScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				client._send('setCycle:', MCyc, @local62, self)
			#end:case
			case 1:
				if (global2._send('script:') == playXylophone):
					client._send('dispose:')
					self._send('dispose:')
				else:
					seconds = kernel.Random(5, 10)
				#endif
			#end:case
			case 2:
				self._send('init:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class chorusRight(Actor):
	#property vars (may be empty)
	x = -18
	y = 184
	view = 648
	loop = 2
	signal = 18432
	
#end:class or instance

@SCI.instance
class chorusMid(Actor):
	#property vars (may be empty)
	x = -18
	y = 184
	view = 648
	signal = 18432
	
	@classmethod
	def doit():
		self._send(
			'cel:', chorusRight._send('cel:'),
			'x:', (chorusRight._send('x:') - 25),
			'y:', chorusRight._send('y:')
		)
		super._send('doit:')
	#end:method

#end:class or instance

@SCI.instance
class chorusLeft(Actor):
	#property vars (may be empty)
	x = -18
	y = 184
	view = 648
	loop = 1
	signal = 18432
	
	@classmethod
	def doit():
		self._send(
			'cel:', chorusRight._send('cel:'),
			'x:', (chorusRight._send('x:') - 50),
			'y:', chorusRight._send('y:')
		)
		super._send('doit:')
	#end:method

#end:class or instance

@SCI.instance
class boneMallet(View):
	#property vars (may be empty)
	x = 221
	y = 177
	noun = 6
	view = 647
	signal = 16384
	
	@classmethod
	def doVerb(param1 = None, *rest):
		if (param1 == 5):
			global1._send('handsOff:')
			global2._send('setScript:', playXylophone)
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class skelLeft(Prop):
	#property vars (may be empty)
	x = 85
	y = 144
	noun = 9
	view = 644
	loop = 1
	
#end:class or instance

@SCI.instance
class skelRight(Prop):
	#property vars (may be empty)
	x = 192
	y = 132
	noun = 9
	view = 644
	
#end:class or instance

@SCI.instance
class doorMaster(Prop):
	#property vars (may be empty)
	x = 170
	y = 118
	noun = 5
	approachX = 141
	approachY = 134
	view = 642
	signal = 16384
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				global91._send('say:', noun, param1, 0, 0)
			#end:case
			case 1:
				global91._send('say:', noun, param1, 0, 0)
			#end:case
			case 2:
				global91._send('say:', noun, param1, 0, 0)
			#end:case
			case 50:
				global91._send('say:', noun, param1, 0, 1)
			#end:case
			case 49:
				global1._send('handsOff:')
				global2._send('setScript:', egoGiveTicketScr)
			#end:case
			case 35:
				global91._send('say:', 5, 35, 0, 0)
			#end:case
			else:
				global91._send('say:', 5, 0, 0, 0)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class boneKey(Prop):
	#property vars (may be empty)
	noun = 11
	view = 647
	cel = 1
	
	@classmethod
	def doit():
		if keyDanceScript._send('register:'):
			self._send(
				'cel:', keyMaster._send('cel:'),
				'x:', (keyMaster._send('x:') + 4),
				'y:', (keyMaster._send('y:') - 53)
			)
		#endif
		super._send('doit:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				if proc913_0(115):
					global1._send('handsOff:')
					global2._send('setScript:', getKeyScript)
				else:
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
class keyMaster(Prop):
	#property vars (may be empty)
	x = 101
	y = 164
	noun = 4
	approachX = 109
	approachY = 176
	view = 6404
	
#end:class or instance

@SCI.instance
class ghost(Actor):
	#property vars (may be empty)
	x = 226
	y = 96
	view = 640
	priority = 13
	signal = 16
	
#end:class or instance

@SCI.instance
class lineGhost(Prop):
	#property vars (may be empty)
	x = 133
	y = 183
	view = 6401
	loop = 5
	
#end:class or instance

@SCI.instance
class door(Prop):
	#property vars (may be empty)
	x = 141
	y = 32
	approachX = 140
	approachY = 90
	view = 647
	loop = 1
	signal = 16384
	
	@classmethod
	def init():
		super._send('init:', &rest)
		global93._send('addToFront:', self)
	#end:method

	@classmethod
	def dispose():
		global93._send('delete:', self)
		super._send('dispose:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		if proc999_5(param1, 5, 3):
			global91._send('say:', 8, 3, 0, 1)
			global0._send('setMotion:', PolyPath, approachX, approachY)
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class theSkull(Feature):
	#property vars (may be empty)
	noun = 10
	onMeCheck = 8
	
#end:class or instance

@SCI.instance
class xylophone(Feature):
	#property vars (may be empty)
	noun = 6
	onMeCheck = 16
	
	@classmethod
	def doVerb(param1 = None, *rest):
		if (param1 == 5):
			global1._send('handsOff:')
			global2._send('setScript:', playXylophone)
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

#end:class or instance

