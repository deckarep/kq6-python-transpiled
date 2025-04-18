#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 742
import sci_sh
import kernel
import Main
import n913
import Scaler
import Polygon
import LoadMany
import Motion
import User
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	vizierWedding = 0,
	stopWedding = 1,
	giveMint = 2,
	kingQueenEntry = 3,
	genieReappears = 4,
	genieScr = 5,
	glint = 7,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


@SCI.instance
class vizierWedding(Script):
	#property vars (may be empty)
	@classmethod
	def handleEvent(param1 = None, *rest):
		if 
			(and
				(global69._send('at:', 0) == global69._send('curIcon:'))
				(param1._send('type:') & 0x1040)
			)
			if (param1._send('y:') < global0._send('y:')):
				kernel.ScriptID(740, 7)._send('add:', -1, 3, 3, 23, 1)
				client._send('setScript:', stopWedding)
			else:
				client._send('setScript:', triedToEscape)
			#endif
			param1._send('claimed:', 1)
		#endif
		param1._send('claimed:')
	#end:method

	@classmethod
	def dispose():
		global93._send('delete:', self)
		global74._send('delete:', self)
		global73._send('delete:', self)
		global72._send('delete:', self)
		super._send('dispose:')
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				kernel.ScriptID(1005, 28)._send('talkWidth:', 87, 'textX:', 60, 'textY:', 23)
				kernel.ScriptID(740, 2)._send('init:')
				kernel.ScriptID(80, 5)._send(
					'view:', 7425,
					'loop:', 0,
					'cel:', 0,
					'x:', 236,
					'y:', 182,
					'scaleSignal:', 1,
					'scaleX:', 143,
					'scaleY:', 143,
					'init:',
					'setCycle:', 0,
					'setLoop:', -1,
					'loop:', 0,
					'cel:', 0,
					'noun:', 12,
					'stopUpd:'
				)
				kernel.ScriptID(80, 6)._send(
					'view:', 7426,
					'loop:', 0,
					'cel:', 0,
					'x:', 78,
					'y:', 178,
					'scaleSignal:', 1,
					'scaleX:', 138,
					'scaleY:', 138,
					'init:',
					'setCycle:', 0,
					'setLoop:', -1,
					'loop:', 0,
					'cel:', 0,
					'noun:', 12,
					'stopUpd:'
				)
				if (not proc913_0(10)):
					kernel.ScriptID(740, 4)._send(
						'view:', 746,
						'loop:', 0,
						'cel:', 0,
						'x:', 54,
						'y:', 157,
						'stopUpd:'
					)
				#endif
				kernel.ScriptID(740, 1)._send('init:', 'cel:', 4, 'setCycle:', Beg, self)
			#end:case
			case 1:
				global91._send('say:', 1, 0, 3, 1, self)
			#end:case
			case 2:
				kernel.ScriptID(740, 2)._send('setCycle:', End, self)
			#end:case
			case 3:
				proc913_1(59)
				global91._send('say:', 1, 0, 3, 2, self)
			#end:case
			case 4:
				proc913_2(59)
				kernel.ScriptID(740, 2)._send('cel:', 2)
				kernel.ScriptID(740, 1)._send('setScript:', preachPriest)
				cycles = 10
			#end:case
			case 5:
				kernel.ScriptID(740, 2)._send('stopUpd:')
				global91._send('say:', 1, 0, 3, 3, self, 'oneOnly:', 0)
			#end:case
			case 6:
				global1._send('handsOn:')
				global93._send('addToFront:', self)
				global74._send('addToFront:', self)
				global73._send('addToFront:', self)
				global72._send('addToFront:', self)
				seconds = 13
			#end:case
			case 7:
				global1._send('handsOff:')
				client._send('setScript:', kernel.ScriptID(744, 1))
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class stopWedding(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(964)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				kernel.ScriptID(740, 7)._send('init:', self)
			#end:case
			case 1:
				kernel.ScriptID(740, 1)._send('setScript:', 0, 'setCycle:', Beg)
				kernel.ScriptID(740, 2)._send('setCycle:', End, self)
			#end:case
			case 2:
				cycles = 10
			#end:case
			case 3:
				kernel.ScriptID(740, 2)._send('setCycle:', Beg)
				global0._send('setSpeed:', 8, 'setStep:', 5, 3, 'setMotion:', MoveTo, 158, 146)
				kernel.ScriptID(740, 5)._send(
					'view:', 7361,
					'setSpeed:', 8,
					'setStep:', 5, 3,
					'setMotion:', MoveTo, 192, 148, self
				)
			#end:case
			case 4:
				kernel.ScriptID(740, 5)._send('setHeading:', 0)
				cycles = 10
			#end:case
			case 5:
				global0._send('reset:', 6)
				client._send('setScript:', kernel.ScriptID(745, 0))
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genieScr(Script):
	#property vars (may be empty)
	@classmethod
	def doit():
		super._send('doit:')
		if ((not local0) and User._send('alterEgo:')._send('edgeHit:')):
			local0 = 1
			global91._send('say:', 3, 3, 25, 1)
		#endif
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				self._send('setScript:', kernel.ScriptID(752, 2), self, kernel.ScriptID(740, 3))
			#end:case
			case 1:
				kernel.ScriptID(740, 3)._send(
					'loop:', 8,
					'cel:', 4,
					'x:', 109,
					'y:', 145,
					'scaleSignal:', 1,
					'scaleX:', 112,
					'scaleY:', 112
				)
				seconds = 3
			#end:case
			case 2:
				self._send('setScript:', kernel.ScriptID(752, 1), self, kernel.ScriptID(740, 3))
			#end:case
			case 3:
				kernel.UnLoad(128, 7501)
				if (not local0):
					global91._send('say:', 1, 0, 6, 8, self)
				else:
					ticks = 1
				#endif
			#end:case
			case 4:
				if (not local0):
					(= global106
						match global106
							case kernel.ScriptID(740, 5):
								kernel.ScriptID(80, 5)._send('view:', 7421, 'yourself:')
							#end:case
							case kernel.ScriptID(80, 5):
								kernel.ScriptID(80, 6)._send('view:', 7422, 'yourself:')
							#end:case
							else:
								kernel.ScriptID(740, 5)
							#end:else
						#end:match
					)
					global156 = killDog._send('register:', global106)
				else:
					global91._send('say:', 3, 3, 25, 2)
					register = 1
					local0 = 0
					global106 = global0
					global156 = 0
				#endif
				global106._send('setCycle:', End, self)
			#end:case
			case 5:
				if (global106 != kernel.ScriptID(740, 5)):
					global106._send(
						'setLoop:', 1,
						'cel:', 0,
						'setCycle:', Walk,
						'setMotion:', MoveTo, kernel.ScriptID(740, 3)._send('x:'), kernel.ScriptID(740, 3)._send(
								'y:'
							)
					)
				#endif
				cycles = 1
			#end:case
			case 6:
				self._send('setScript:', kernel.ScriptID(752, 0), self, kernel.ScriptID(740, 3))
			#end:case
			case 7:
				if (not local0):
					if (not proc999_5(global106, kernel.ScriptID(80, 6), global0)):
						(state -= 4)
					#endif
					if (not kernel.HaveMouse()):
						seconds = 4
					else:
						seconds = 2
					#endif
				else:
					if (global106 == global0):
						state.post('++')
					#endif
					ticks = 5
				#endif
			#end:case
			case 8:
				if register:
					proc0_1(18)
				else:
					global1._send('handsOff:')
					global91._send('say:', 1, 0, 8, 0, self)
				#endif
			#end:case
			case 9:
				global106 = global0
				global156 = 0
				self._send('setScript:', kernel.ScriptID(752, 0), 0, kernel.ScriptID(740, 3))
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class killDog(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global106._send('setLoop:', 2, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 1:
				global106._send('setPri:', (global106._send('priority:') + 1), 'addToPic:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genieReappears(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				kernel.UnLoad(128, 748)
				global105._send('number:', 943, 'loop:', 1, 'play:')
				kernel.ScriptID(740, 2)._send(
					'view:', 7414,
					'setLoop:', 0,
					'cel:', 0,
					'setPri:', (kernel.ScriptID(740, 8)._send('priority:') + 1),
					'setCycle:', End, self
				)
			#end:case
			case 1:
				kernel.ScriptID(740, 2)._send(
					'view:', 7413,
					'loop:', 0,
					'cel:', 0,
					'setScale:', 0,
					'x:', 207,
					'y:', 131,
					'cycleSpeed:', (4 if (not global87) else 8),
					'stopUpd:'
				)
				kernel.ScriptID(740, 3)._send(
					'view:', 7021,
					'loop:', 8,
					'cel:', 4,
					'x:', 169,
					'y:', 141,
					'scaleSignal:', 1,
					'scaleX:', 112,
					'scaleY:', 112,
					'ignoreActors:', 1,
					'setPri:', 10,
					'init:',
					'noun:', 5,
					'stopUpd:'
				)
				if (client == kingQueenEntry):
					king._send('loop:', 3, 'cel:', 0, 'setCycle:', End, king)
				#endif
				kernel.ScriptID(740, 1)._send(
					'view:', 7412,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', 152, 134,
					'setPri:', 0,
					'setCycle:', End, self
				)
				if (not proc913_0(10)):
					kernel.ScriptID(740, 4)._send(
						'startUpd:',
						'view:', 7465,
						'setLoop:', 0,
						'cel:', 0,
						'cycleSpeed:', 6,
						'setPri:', 13,
						'setCycle:', End, kernel.ScriptID(740, 4)
					)
				#endif
				kernel.UnLoad(128, 741)
				kernel.UnLoad(128, 746)
				kernel.UnLoad(128, 7414)
			#end:case
			case 2:
				cycles = 10
			#end:case
			case 3:
				kernel.ScriptID(740, 1)._send('addToPic:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class giveMint(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				cycles = 4
			#end:case
			case 1:
				kernel.ScriptID(740, 2)._send(
					'view:', 7415,
					'setLoop:', 0,
					'cel:', 0,
					'setPri:', 9,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				global91._send('say:', 4, 67, 0, 0, self, 160)
			#end:case
			case 3:
				client._send('setScript:', kernel.ScriptID(744, 1))
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class triedToEscape(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global91._send('say:', 3, 3, 24, 0, self)
			#end:case
			case 1:
				client._send('setScript:', kernel.ScriptID(744, 1), 0, 1)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class preachPriest(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if (not kernel.ScriptID(740, 1)._send('cel:')):
					kernel.ScriptID(740, 1)._send('setLoop:', kernel.Random(0, 1), 'setCycle:', End, self)
				else:
					kernel.ScriptID(740, 1)._send('setCycle:', Beg, self)
				#endif
			#end:case
			case 1:
				state = -1
				cycles = kernel.Random(10, 40)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class king(Actor):
	#property vars (may be empty)
	x = 120
	y = 182
	noun = 16
	view = 7441
	loop = 3
	
	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('setCycle:', Walk, 'setScale:', Scaler, 100, 75, 189, 134)
	#end:method

	@classmethod
	def cue():
		self._send('view:', 7464, 'loop:', 0, 'cel:', 2, 'addToPic:')
	#end:method

#end:class or instance

@SCI.instance
class glint(Prop):
	#property vars (may be empty)
	view = 902
	priority = 15
	signal = 18448
	
#end:class or instance

@SCI.instance
class kingQueenEntry(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				king._send(
					'init:',
					'setSpeed:', 5,
					'yStep:', (4 if (not global87) else 2),
					'setCycle:', Walk,
					'ignoreActors:',
					'setScale:', Scaler, 101, 90, 189, 141
				)
				kernel.ScriptID(740, 2)._send('view:', 7414, 'setLoop:', 0, 'cel:', 0)
				cycles = 2
			#end:case
			case 1:
				global69._send('enable:')
				proc913_4(global0, king, self)
			#end:case
			case 2:
				seconds = 3
			#end:case
			case 3:
				global91._send('say:', 1, 0, 7, 1, self)
			#end:case
			case 4:
				king._send('setMotion:', MoveTo, 122, 142, self)
			#end:case
			case 5:
				global0._send('setHeading:', 315)
				king._send(
					'view:', 744,
					'loop:', 2,
					'cel:', 0,
					'x:', 133,
					'y:', 143,
					'setScale:', 0,
					'setCycle:', End, self
				)
				kernel.UnLoad(128, 7441)
			#end:case
			case 6:
				king._send('stopUpd:')
				global91._send('say:', 1, 0, 7, 2, self)
			#end:case
			case 7:
				global91._send('say:', 1, 0, 7, 3, self)
			#end:case
			case 8:
				kernel.ScriptID(740, 2)._send(
					'view:', 7415,
					'setLoop:', 0,
					'cel:', 0,
					'setPri:', 9,
					'setCycle:', CT, 3, 1, self
				)
			#end:case
			case 9:
				kernel.ScriptID(742, 7)._send('init:', 'posn:', 164, 107, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 10:
				kernel.ScriptID(742, 7)._send('dispose:')
				cycles = 2
			#end:case
			case 11:
				proc913_1(59)
				global91._send('say:', 1, 0, 7, 4, self)
			#end:case
			case 12:
				proc913_2(59)
				global91._send('say:', 1, 0, 7, 5, self)
			#end:case
			case 13:
				global91._send('say:', 1, 0, 7, 6, self)
			#end:case
			case 14:
				global1._send('givePoints:', 5)
				kernel.ScriptID(740, 2)._send('view:', 7414, 'cel:', 0)
				global91._send('say:', 1, 0, 7, 7, self)
			#end:case
			case 15:
				self._send('setScript:', kernel.ScriptID(742, 4), self)
			#end:case
			case 16:
				global91._send('say:', 1, 0, 7, 8, self)
			#end:case
			case 17:
				global91._send('say:', 1, 0, 7, 9, self)
			#end:case
			case 18:
				global91._send('say:', 1, 0, 7, 10, self)
			#end:case
			case 19:
				proc958_0(0, 1063, 1029, 1001)
				kernel.UnLoad(128, 899)
				kernel.UnLoad(128, 8992)
				kernel.UnLoad(128, 891)
				kernel.UnLoad(128, 890)
				self._send('setScript:', kernel.ScriptID(740, 23), self)
			#end:case
			case 20:
				global91._send('say:', 1, 0, 7, 11, self)
			#end:case
			case 21:
				global91._send('say:', 1, 0, 7, 12, self)
			#end:case
			case 22:
				global2._send(
					'addObstacle:', Polygon._send('new:')._send(
							'type:', 2,
							'init:', 150, 139, 208, 139, 208, 153, 180, 153, 150, 146,
							'yourself:'
						)
				)
				proc958_0(0, 1004, 1026)
				kernel.UnLoad(128, 892)
				kernel.UnLoad(128, 899)
				kernel.UnLoad(128, 8921)
				kernel.UnLoad(128, 8992)
				kernel.UnLoad(128, 891)
				kernel.UnLoad(128, 890)
				kernel.ScriptID(740, 3)._send('setScript:', kernel.ScriptID(742, 5))
				global1._send('handsOn:')
				self._send('dispose:')
				kernel.DisposeScript(744)
			#end:case
		#end:match
	#end:method

#end:class or instance

