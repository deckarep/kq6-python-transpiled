#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 811
import sci_sh
import kernel
import Main
import KQ6Print
import rm810
import CartoonScript
import n913
import Conversation
import Scaler
import Rev
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	studyInset = 0,
)

@SCI.instance
class studyInset(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(811)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 711, 16)):
					global1._send('givePoints:', 1)
				#endif
				self._send('setScript:', convScript, self)
			#end:case
			case 1:
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 711, 16)):
					kernel.ScriptID(80, 0)._send('setFlag:', 711, 16)
					convScript._send('start:', (convScript._send('state:') + 1))
					register = 1
					global102._send('fadeTo:', 150, -1)
					self._send('setScript:', writeLetter, self)
				else:
					register = 0
					roomConv._send('add:', -1, 4, 1, 8, 2, 'init:', self)
				#endif
			#end:case
			case 2:
				global5._send('eachElementDo:', #startUpd)
				cycles = 1
			#end:case
			case 3:
				roomConv._send('caller:', 0)
				candles._send('dispose:')
				feather._send('dispose:')
				desk._send('dispose:')
				door._send('dispose:')
				background._send('dispose:')
				proc810_1()
				cycles = 5
			#end:case
			case 4:
				if register:
					global91._send('say:', 4, 1, 9, 9, self, 'oneOnly:', 0)
					global102._send('fadeTo:', 810, -1)
				#endif
				global0._send('setCycle:', Beg, self)
			#end:case
			case 5:
				global1._send('handsOn:')
				global0._send('reset:', 1, 900)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class writeLetter(CartoonScript):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				proc913_1(59)
				kernel.ScriptID(810, 3)._send('setScript:', 0, 1)
				self._send('setScript:', inkUp, self)
			#end:case
			case 1:
				KQ6Print._send(
					'font:', global22,
					'posn:', -1, 10,
					'say:', 0, 4, 1, 9, 2,
					'modeless:', 1,
					'ticks:', 20,
					'init:', self
				)
			#end:case
			case 2:
				if global25:
					global25._send('dispose:')
				#endif
				KQ6Print._send(
					'font:', global22,
					'posn:', -1, 10,
					'say:', 0, 4, 1, 9, 3,
					'modeless:', 1,
					'init:', self
				)
			#end:case
			case 3:
				self._send('setScript:', inkUp, self)
			#end:case
			case 4:
				if global25:
					global25._send('dispose:')
				#endif
				KQ6Print._send(
					'font:', global22,
					'posn:', -1, 10,
					'say:', 0, 4, 1, 9, 4,
					'modeless:', 1,
					'init:', self
				)
			#end:case
			case 5:
				inkUp._send('start:', 0)
				self._send('setScript:', inkUp, self)
			#end:case
			case 6:
				if global25:
					global25._send('dispose:')
				#endif
				KQ6Print._send(
					'font:', global22,
					'posn:', -1, 10,
					'say:', 0, 4, 1, 9, 5,
					'modeless:', 1,
					'init:', self
				)
			#end:case
			case 7:
				self._send('setScript:', inkUp, self)
			#end:case
			case 8:
				KQ6Print._send(
					'font:', global22,
					'posn:', -1, 10,
					'say:', 0, 4, 1, 9, 6,
					'modeless:', 1,
					'init:', self
				)
			#end:case
			case 9:
				KQ6Print._send(
					'font:', global22,
					'posn:', -1, 10,
					'say:', 0, 4, 1, 9, 7,
					'modeless:', 1,
					'init:', self
				)
			#end:case
			case 10:
				self._send('setScript:', inkUp, self, 1)
			#end:case
			case 11:
				vizier._send('setLoop:', 3, 'cel:', 0, 'posn:', 165, 116, 'priority:', 9)
				cycles = 10
			#end:case
			case 12:
				if kernel.ScriptID(80, 0)._send('tstFlag:', 710, 256):
					KQ6Print._send(
						'font:', global22,
						'posn:', -1, 10,
						'modeless:', 1,
						'say:', 0, 4, 1, 9, 8,
						'init:', self
					)
				else:
					KQ6Print._send(
						'font:', global22,
						'posn:', -1, 10,
						'modeless:', 1,
						'say:', 0, 4, 1, 10, 1,
						'init:', self
					)
				#endif
			#end:case
			case 13:
				if global25:
					global25._send('dispose:')
				#endif
				self._send('setScript:', convScript, self)
			#end:case
			case 14:
				proc913_2(59)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class inkUp(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				vizier._send('setLoop:', 2, 'cel:', 0, 'cycleSpeed:', 8, 'setCycle:', End, self)
			#end:case
			case 1:
				seconds = kernel.Random(3, 5)
			#end:case
			case 2:
				vizier._send('setCycle:', Beg, self)
			#end:case
			case 3:
				start = state
				vizier._send('setLoop:', 7, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 4:
				seconds = 2
			#end:case
			case 5:
				if register:
					vizier._send('setLoop:', 8, 'cel:', 0, 'setCycle:', CT, 1, 1, self)
				else:
					vizier._send('setCycle:', Beg, self)
				#endif
			#end:case
			case 6:
				if register:
					feather._send('init:')
					vizier._send('setCycle:', End, self)
				else:
					vizier._send('setLoop:', 0, 'cycleSpeed:', 20, 'setCycle:', Rev)
					self._send('dispose:')
				#endif
			#end:case
			case 7:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class convScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send(
					'view:', 814,
					'normal:', 0,
					'loop:', 0,
					'cel:', 0,
					'setScale:', 0,
					'scaleX:', 128,
					'scaleY:', 128,
					'x:', 164,
					'y:', 169,
					'setCycle:', End, self
				)
			#end:case
			case 1:
				KQ6Print._send(
					'font:', global22,
					'say:', 0, 4, 1, (8 + (not kernel.ScriptID(80, 0)._send('tstFlag:', 711, 16))), 1,
					'init:', self
				)
				cycles = 10
			#end:case
			case 2:
				global5._send('eachElementDo:', #startUpd)
				ticks = 1
			#end:case
			case 3:
				global5._send('eachElementDo:', #hide)
				global2._send('drawPic:', 802, 10)
				candles._send('setCycle:', Fwd, 'init:')
				door._send('init:')
				desk._send('addToPic:')
				background._send('addToPic:')
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 711, 16)):
					feet._send('init:')
					vizier._send('init:')
					cycles = 1
				else:
					feather._send('init:')
					seconds = 5
				#endif
			#end:case
			case 4:
				self._send('dispose:')
			#end:case
			case 5:
				vizier._send('setCycle:', End, self)
			#end:case
			case 6:
				feet._send('dispose:')
				vizier._send(
					'posn:', 153, 113,
					'setLoop:', 4,
					'cel:', 0,
					'setCycle:', Walk,
					'cycleSpeed:', 6,
					'moveSpeed:', 6,
					'setScale:', Scaler, 100, 73, 113, 103,
					'setMotion:', MoveTo, 92, 106, self
				)
			#end:case
			case 7:
				door._send('hide:')
				global105._send('number:', 901, 'loop:', 1, 'play:')
				vizier._send(
					'setLoop:', 5,
					'cel:', 0,
					'cycleSpeed:', 8,
					'posn:', 82, 72,
					'setScale:', 0,
					'scaleX:', 128,
					'scaleY:', 128,
					'setCycle:', End, self
				)
			#end:case
			case 8:
				global105._send('number:', 902, 'loop:', 1, 'play:')
				door._send('show:')
				vizier._send('dispose:')
				cycles = 2
			#end:case
			case 9:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class roomConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class background(View):
	#property vars (may be empty)
	x = 154
	y = 123
	view = 811
	loop = 1
	signal = 16400
	
#end:class or instance

@SCI.instance
class feet(View):
	#property vars (may be empty)
	x = 165
	y = 115
	view = 812
	loop = 1
	priority = 9
	signal = 16400
	scaleSignal = 1
	
#end:class or instance

@SCI.instance
class vizier(Actor):
	#property vars (may be empty)
	x = 164
	y = 117
	view = 812
	cel = 2
	priority = 13
	signal = 24592
	scaleSignal = 1
	cycleSpeed = 19
	illegalBits = 0
	
#end:class or instance

@SCI.instance
class desk(View):
	#property vars (may be empty)
	x = 137
	y = 89
	view = 811
	loop = 1
	cel = 1
	priority = 14
	signal = 16
	
#end:class or instance

@SCI.instance
class candles(Prop):
	#property vars (may be empty)
	x = 185
	y = 91
	view = 811
	loop = 2
	cel = 1
	priority = 15
	signal = 16
	
#end:class or instance

@SCI.instance
class feather(View):
	#property vars (may be empty)
	x = 170
	y = 95
	view = 811
	loop = 1
	cel = 2
	priority = 15
	signal = 16400
	
#end:class or instance

@SCI.instance
class door(View):
	#property vars (may be empty)
	x = 92
	y = 74
	view = 812
	loop = 6
	priority = 1
	signal = 16400
	
#end:class or instance

