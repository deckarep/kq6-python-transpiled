#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 451
import sci_sh
import kernel
import Main
import rm450
import n913
import Conversation
import Scaler
import PolyPath
import LoadMany
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	proc451_0 = 0,
)

@SCI.procedure
def proc451_0(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	global2._send('setScript:', boreTheOyster, 0, param1)
#end:procedure

@SCI.instance
class boreTheOyster(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				if register:
					global91._send('say:', 1, 42, 5, 1, self, 450)
				else:
					global91._send('say:', 1, 42, 1, 1, self, 451)
				#endif
			#end:case
			case 1:
				global91._send('say:', 1, 42, 1, 2, self, 451)
			#end:case
			case 2:
				global0._send('setMotion:', PolyPath, 132, 141, self)
			#end:case
			case 3:
				proc913_1(59)
				global0._send(
					'view:', 451,
					'loop:', 0,
					'cel:', 0,
					'posn:', 115, 143,
					'normal:', 0,
					'cycleSpeed:', 6,
					'setCycle:', End, self
				)
			#end:case
			case 4:
				cycles = 3
			#end:case
			case 5:
				global0._send(
					'loop:', 2,
					'cel:', 0,
					'posn:', 104, 146,
					'cycleSpeed:', 6,
					'setCycle:', End, self
				)
			#end:case
			case 6:
				OI._send('init:')
				kernel.ScriptID(450, 1)._send('hide:', 'view:', 2002)
				global0._send('dispose:')
				seconds = 3
			#end:case
			case 7:
				global1._send('handsOn:')
				global69._send('disable:', 0, 3, 4, 5)
				book._send('setCycle:', End, self)
			#end:case
			case 8:
				book._send('cel:', 0)
				cycles = 3
			#end:case
			case 9:
				global91._send('say:', 1, 42, 1, 4, self, 451)
			#end:case
			case 10:
				book._send('setCycle:', End, self)
			#end:case
			case 11:
				book._send('cel:', 0)
				cycles = 3
			#end:case
			case 12:
				pearl._send('y:', 184, 'z:', 80)
				global104._send('number:', 961, 'setLoop:', 1, 'play:')
				insetOyster._send('view:', 4532, 'setLoop:', 0, 'cycleSpeed:', 1, 'setCycle:', End)
				seconds = 2
			#end:case
			case 13:
				if global25:
					global25._send('dispose:')
				#endif
				insetOyster._send('setCycle:', Beg, self)
			#end:case
			case 14:
				pearl._send('y:', 104, 'z:', 0)
				insetOyster._send('view:', 453, 'setLoop:', 1, 'cel:', 0)
				seconds = 2
			#end:case
			case 15:
				book._send('setCycle:', End, self)
			#end:case
			case 16:
				book._send('cel:', 0)
				cycles = 3
			#end:case
			case 17:
				global91._send('say:', 1, 42, 1, 6, self, 451)
			#end:case
			case 18:
				pearl._send('y:', 184, 'z:', 80)
				global104._send('number:', 961, 'setLoop:', 1, 'play:')
				insetOyster._send('view:', 4532, 'setLoop:', 0, 'setCycle:', End)
				seconds = 3
			#end:case
			case 19:
				if global25:
					global25._send('dispose:')
				#endif
				insetOyster._send('setCycle:', Beg, self)
			#end:case
			case 20:
				pearl._send('y:', 104, 'z:', 0)
				insetOyster._send('view:', 453, 'setLoop:', 1)
				seconds = 2
			#end:case
			case 21:
				book._send('setCycle:', End, self)
			#end:case
			case 22:
				book._send('cel:', 0)
				cycles = 3
			#end:case
			case 23:
				global91._send('say:', 1, 42, 1, 8, self, 451)
			#end:case
			case 24:
				pearl._send('y:', 184, 'z:', 80)
				global104._send('number:', 961, 'setLoop:', 1, 'play:')
				insetOyster._send('view:', 4532, 'setLoop:', 0, 'setCycle:', End)
				seconds = 6
			#end:case
			case 25:
				if global25:
					global25._send('dispose:')
				#endif
				insetOyster._send('setCycle:', Beg, self)
			#end:case
			case 26:
				pearl._send('y:', 104, 'z:', 0)
				insetOyster._send('view:', 453, 'setLoop:', 1)
				seconds = 1
			#end:case
			case 27:
				global1._send('handsOff:')
				book._send('setCycle:', End, self)
			#end:case
			case 28:
				book._send('cel:', 0)
				cycles = 3
			#end:case
			case 29:
				global104._send('setLoop:', 5, 'play:')
				insetOyster._send('view:', 4533, 'cycleSpeed:', 0, 'setLoop:', 5, 'setCycle:', Fwd)
				seconds = 5
			#end:case
			case 30:
				if global25:
					global25._send('dispose:')
				#endif
				global91._send('say:', 1, 42, 1, 11, self, 451)
			#end:case
			case 31:
				OI._send('dispose:')
				kernel.ScriptID(450, 1)._send(
					'view:', 4531,
					'setLoop:', 2,
					'show:',
					'cycleSpeed:', 50,
					'setCycle:', End
				)
				global0._send(
					'view:', 451,
					'loop:', 2,
					'cel:', 2,
					'posn:', 104, 146,
					'cycleSpeed:', 6,
					'normal:', 0,
					'setScale:', Scaler, 100, 30, 126, 70,
					'init:'
				)
				cycles = 4
			#end:case
			case 32:
				global91._send('say:', 1, 42, 1, 12, self, 451)
			#end:case
			case 33:
				global0._send(
					'view:', 451,
					'loop:', 0,
					'cel:', 7,
					'posn:', 115, 143,
					'setCycle:', Beg, self
				)
			#end:case
			case 34:
				global0._send('reset:', 1, 'posn:', 132, 141)
				global2._send('notify:')
				kernel.ScriptID(40, 0)._send('oysterDozing:', 1)
				cycles = 6
			#end:case
			case 35:
				proc913_2(59)
				global1._send('handsOn:')
				kernel.DisposeScript(1038)
				proc450_8(0)
				cycles = 4
			#end:case
			case 36:
				self._send('dispose:')
				kernel.DisposeScript(451)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class grabPearl(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('givePoints:', 1)
				insetOyster._send('setCycle:', 0)
				book._send('dispose:')
				ticks = 4
			#end:case
			case 1:
				global91._send('say:', 4, 5, 0, 1, self, 451)
			#end:case
			case 2:
				arm._send('init:', 'setCycle:', CT, 1, 1, self)
			#end:case
			case 3:
				pearl._send('dispose:')
				arm._send('setCycle:', End, self)
			#end:case
			case 4:
				arm._send('dispose:')
				insetOyster._send('setCycle:', Beg, self)
			#end:case
			case 5:
				insetOyster._send('view:', 4533, 'cycleSpeed:', 3, 'setLoop:', 5, 'setCycle:', Fwd)
				seconds = 3
			#end:case
			case 6:
				OI._send('dispose:')
				proc913_2(59)
				kernel.ScriptID(450, 1)._send(
					'view:', 4531,
					'setLoop:', 2,
					'cel:', 0,
					'show:',
					'cycleSpeed:', 50,
					'setCycle:', End
				)
				global0._send(
					'view:', 451,
					'loop:', 2,
					'cel:', 2,
					'posn:', 104, 146,
					'cycleSpeed:', 6,
					'normal:', 0,
					'cycleSpeed:', 6,
					'get:', 30,
					'init:',
					'setScale:', Scaler, 100, 30, 126, 70,
					'setCycle:', Beg, self
				)
			#end:case
			case 7:
				global91._send('say:', 4, 5, 0, 2, self, 451)
			#end:case
			case 8:
				global104._send('number:', 963, 'setLoop:', 1, 'play:')
				global2._send('notify:')
				kernel.ScriptID(40, 0)._send('oysterDozing:', 1)
				global0._send(
					'view:', 451,
					'loop:', 0,
					'cel:', 7,
					'posn:', 115, 143,
					'cycleSpeed:', 6,
					'setCycle:', Beg, self
				)
			#end:case
			case 9:
				global0._send('reset:', 1, 'posn:', 132, 141)
				cycles = 6
			#end:case
			case 10:
				global91._send('say:', 4, 5, 0, 3, self, 451)
			#end:case
			case 11:
				global1._send('handsOn:')
				global104._send('setLoop:', 5, 'play:')
				proc450_8(0)
				cycles = 4
			#end:case
			case 12:
				self._send('dispose:')
				proc958_0(0, 1038, 451)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class almostGotScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				arm._send('init:', 'setCycle:', CT, 1, 1, self)
			#end:case
			case 1:
				arm._send('setCycle:', Beg, self)
			#end:case
			case 2:
				arm._send('dispose:')
				cycles = 2
			#end:case
			case 3:
				global91._send('say:', 3, 5, 2, 1, self, 451)
			#end:case
			case 4:
				global1._send('handsOn:')
				global69._send('disable:', 0, 3, 4, 5)
				insetOyster._send('view:', 453, 'setLoop:', 1, 'cel:', 0)
				boreTheOyster._send('start:', 20)
				global2._send('setScript:', boreTheOyster)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class OI(View):
	#property vars (may be empty)
	x = 122
	y = 113
	noun = 2
	view = 453
	priority = 11
	signal = 16400
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global91._send('say:', noun, param1, 0, 1, 0, 451)
			#end:case
			case 1:
				global91._send('say:', noun, param1, 0, 1, 0, 451)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global103._send('number:', 450, 'setLoop:', -1, 'play:')
		global73._send('addToFront:', self)
		global72._send('addToFront:', self)
		book._send('init:')
		pearl._send('init:')
		botShell._send('init:')
		insetOyster._send('init:')
		super._send('init:')
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global73._send('delete:', self)
		global72._send('delete:', self)
		global2._send('cue:')
		global103._send('fade:', 0, 10, 10)
		book._send('dispose:')
		insetOyster._send('dispose:')
		botShell._send('dispose:')
		pearl._send('dispose:')
		super._send('dispose:')
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				(not param1._send('modifiers:'))
				(or
					(param1._send('type:') & 0x0001)
					((param1._send('message:') & 0x000d) and (param1._send('type:') & 0x0004))
				)
				(not global92)
				(not global84)
				(param1._send('type:') != 16384)
				(not self._send('onMe:', param1))
			)
			param1._send('claimed:', 1)
			boreTheOyster._send('start:', 31, 'init:')
		else:
			super._send('handleEvent:', param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class book(Prop):
	#property vars (may be empty)
	x = 198
	y = 87
	onMeCheck = 0
	view = 453
	loop = 2
	priority = 13
	signal = 16400
	
#end:class or instance

@SCI.instance
class arm(Prop):
	#property vars (may be empty)
	x = 198
	y = 87
	onMeCheck = 0
	view = 4532
	loop = 1
	priority = 14
	signal = 16400
	
#end:class or instance

@SCI.instance
class insetOyster(Prop):
	#property vars (may be empty)
	x = 63
	y = 171
	z = 70
	noun = 3
	view = 453
	loop = 1
	priority = 14
	signal = 16400
	cycleSpeed = 10
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global91._send('say:', noun, param1, 0, 1, 0, 451)
			#end:case
			case 1:
				global91._send('say:', noun, param1, 0, 1, 0, 451)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class botShell(View):
	#property vars (may be empty)
	x = 87
	y = 180
	z = 90
	noun = 3
	view = 453
	cel = 1
	priority = 12
	signal = 16400
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global91._send('say:', noun, param1, 0, 1, 0, 451)
			#end:case
			case 1:
				global91._send('say:', noun, param1, 0, 1, 0, 451)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class pearl(Prop):
	#property vars (may be empty)
	x = 93
	y = 104
	noun = 4
	view = 453
	loop = 6
	priority = 13
	signal = 16400
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				if (insetOyster._send('cel:') != insetOyster._send('lastCel:')):
					global1._send('handsOff:')
					global2._send('setScript:', almostGotScript)
				else:
					global1._send('handsOff:')
					global2._send('setScript:', grabPearl)
				#endif
			#end:case
			case 1:
				global91._send('say:', noun, param1, 0, 1, 0, 451)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

