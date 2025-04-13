#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 540
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
import Rev
import Sound
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm540 = 0,
)

@SCI.instance
class rm540(KQ6Room):
	#property vars (may be empty)
	noun = 2
	picture = 540
	south = 510
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global2._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 268, 189, 314, 118, 307, 100, 253, 92, 190, 93, 156, 96, 87, 97, 89, 103, 62, 105, 43, 112, 29, 125, 41, 149, 102, 157, 58, 187, 0, 182, 0, 0, 319, 0, 319, 189,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 281, 115, 250, 120, 211, 122, 146, 120, 114, 117, 110, 104, 131, 101, 206, 100, 273, 107,
					'yourself:'
				)
		)
		super._send('init:', &rest)
		global102._send('number:', 540, 'flags:', 1, 'loop:', -1, 'play:')
		global1._send('handsOff:')
		castle._send('init:')
		hedge._send('init:')
		beastPath._send('init:')
		fountain._send('init:')
		gateFeat._send('init:')
		spout._send('init:', 'setCycle:', Fwd)
		spray._send('init:', 'setCycle:', Fwd)
		gate._send('init:')
		global0._send('init:', 'reset:', 3, 'posn:', 125, 187, 'setScale:', Scaler, 100, 68, 190, 80)
		if global0._send('scaler:'):
			global0._send('scaler:')._send('doit:')
		#endif
		(cond
			case (global12 == 250):
				beauty._send(
					'init:',
					'setScale:', Scaler, 100, 68, 190, 100,
					'setStep:', 4, 3,
					'setCycle:', Walk
				)
				beast._send('init:')
				kernel.ScriptID(0, 5)._send('dispose:')
				weasel._send('init:', 'setCycle:', Walk)
				glint._send('init:', 'hide:')
				self._send('setScript:', beautyScript)
			#end:case
			case (not proc913_0(46)):
				beast._send('init:')
				self._send('setScript:', beastScript)
				global0._send('setMotion:', MoveTo, 116, 131)
			#end:case
			else:
				global1._send('handsOn:')
				global0._send('setMotion:', MoveTo, 116, 131)
			#end:else
		)
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global102._send('fade:')
		super._send('newRoom:', param1, &rest)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('dispose:')
		kernel.DisposeScript(969)
	#end:method

#end:class or instance

@SCI.instance
class gateFx(Sound):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class beast(Actor):
	#property vars (may be empty)
	x = 72
	y = 62
	view = 533
	loop = 2
	signal = 24576
	illegalBits = 0
	
#end:class or instance

@SCI.instance
class beauty(Actor):
	#property vars (may be empty)
	x = 158
	y = 189
	view = 252
	loop = 3
	signal = 24576
	
#end:class or instance

@SCI.instance
class weasel(Actor):
	#property vars (may be empty)
	x = 301
	y = 163
	view = 545
	loop = 1
	
#end:class or instance

@SCI.instance
class glint(Prop):
	#property vars (may be empty)
	view = 902
	signal = 16384
	
#end:class or instance

@SCI.instance
class spout(Prop):
	#property vars (may be empty)
	x = 199
	y = 89
	view = 540
	cel = 2
	priority = 8
	signal = 16400
	
	@classmethod
	def doVerb():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		fountain._send('doVerb:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class spray(Prop):
	#property vars (may be empty)
	x = 198
	y = 89
	view = 540
	loop = 1
	cel = 2
	priority = 8
	signal = 16
	
	@classmethod
	def doVerb():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		fountain._send('doVerb:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class gate(Prop):
	#property vars (may be empty)
	x = 72
	y = 62
	view = 5402
	signal = 16384
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		gateFeat._send('doVerb:', param1, &rest)
	#end:method

#end:class or instance

@SCI.instance
class castle(Feature):
	#property vars (may be empty)
	noun = 6
	onMeCheck = 8
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				if proc913_0(43):
					global91._send('say:', noun, param1, 4, 1)
				else:
					global91._send('say:', noun, param1, 3, 1)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class hedge(Feature):
	#property vars (may be empty)
	noun = 7
	onMeCheck = 2
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				if proc913_0(43):
					global91._send('say:', noun, param1, 4, 1)
				else:
					global91._send('say:', noun, param1, 3, 1)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class fountain(Feature):
	#property vars (may be empty)
	x = 198
	y = 127
	noun = 5
	onMeCheck = 16
	approachX = 196
	approachY = 115
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc999_5(param1, 57, 58, 59, 60, 96, 56):
			if proc913_0(77):
				global91._send('say:', noun, param1, 8)
			else:
				global91._send('say:', noun, param1, 9)
			#endif
		else:
			match param1
				case 5:
					global1._send('handsOff:')
					global2._send('setScript:', getWater, 0, 0)
				#end:case
				case 43:
					(cond
						case (global161 & 0x0001):
							global91._send('say:', noun, 43, 5)
						#end:case
						case (not proc913_0(43)):
							global91._send('say:', noun, param1, 3, 1)
						#end:case
						case (not proc913_0(77)):
							global91._send('say:', 5, 43, 9, 0)
						#end:case
						case 
							(or
								(not (global161 & 0x0004))
								(not (global161 & 0x0002))
							):
							global91._send('say:', noun, param1, 10)
						#end:case
						else:
							global1._send('handsOff:')
							global2._send('setScript:', getWater, 0, 43)
						#end:else
					)
				#end:case
				case 44:
					(cond
						case (not proc913_0(43)):
							global91._send('say:', noun, 43, 3, 1)
						#end:case
						case proc913_0(77):
							global91._send('say:', noun, 56, 8)
						#end:case
						else:
							global91._send('say:', noun, 56, 9)
						#end:else
					)
				#end:case
				case 24:
					if (not proc913_0(43)):
						global91._send('say:', noun, 43, 3, 1)
					else:
						global91._send('say:', noun, 26, 0)
					#endif
				#end:case
				case 0:
					if proc913_0(43):
						global91._send('say:', noun, param1, 4, 1)
					else:
						global91._send('say:', noun, param1, 3, 1)
					#endif
				#end:case
				else:
					super._send('doVerb:', param1, &rest)
				#end:else
			#end:match
		#endif
	#end:method

#end:class or instance

@SCI.instance
class beastPath(Feature):
	#property vars (may be empty)
	noun = 4
	onMeCheck = 32
	
#end:class or instance

@SCI.instance
class gateFeat(Feature):
	#property vars (may be empty)
	noun = 8
	onMeCheck = 4
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				if proc913_0(43):
					global91._send('say:', noun, param1, 4, 1)
				else:
					global91._send('say:', noun, param1, 3, 1)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class beastScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				kernel.Load(128, 543)
				gate._send('hide:')
				beast._send(
					'posn:', 72, 62,
					'view:', 533,
					'setLoop:', 0,
					'ignoreActors:', 1,
					'setCycle:', End, self
				)
			#end:case
			case 1:
				beast._send(
					'view:', 5406,
					'posn:', 96, 98,
					'setLoop:', 0,
					'cel:', 0,
					'setCycle:', End, self
				)
				gateFx._send('number:', 542, 'play:')
			#end:case
			case 2:
				gateFx._send('number:', 543, 'play:')
				gate._send('show:')
				global0._send('setMotion:', MoveTo, 107, 130, self)
				beast._send(
					'view:', 542,
					'setScale:', Scaler, 100, 68, 190, 100,
					'setCycle:', Walk,
					'setStep:', 4, 3,
					'setLoop:', 2,
					'y:', (beast._send('y:') + 3),
					'setMotion:', MoveTo, 69, 129, self
				)
			#end:case
			case 3: 0#end:case
			case 4:
				beast._send('view:', 543, 'setLoop:', 3, 'cel:', 0)
				cycles = 2
			#end:case
			case 5:
				proc913_4(global0, beast, self)
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				myConv._send(
					'add:', -1, 1, 0, 1, 1,
					'add:', -1, 1, 0, 1, 2,
					'add:', -1, 1, 0, 1, 3,
					'add:', -1, 1, 0, 1, 4,
					'add:', -1, 1, 0, 1, 5,
					'init:', self
				)
			#end:case
			case 8:
				beast._send('setCycle:', End, self)
			#end:case
			case 9:
				myConv._send('add:', -1, 1, 0, 1, 6, 'add:', -1, 1, 0, 1, 7, 'init:', self)
			#end:case
			case 10:
				beast._send('setCycle:', Beg, self)
			#end:case
			case 11:
				myConv._send(
					'add:', -1, 1, 0, 1, 8,
					'add:', -1, 1, 0, 1, 9,
					'add:', -1, 1, 0, 1, 10,
					'add:', -1, 1, 0, 1, 11,
					'add:', -1, 1, 0, 1, 12,
					'add:', -1, 1, 0, 1, 13,
					'add:', -1, 1, 0, 1, 14,
					'add:', -1, 1, 0, 1, 15,
					'add:', -1, 1, 0, 1, 16,
					'init:', self
				)
			#end:case
			case 12:
				myConv._send(
					'add:', -1, 1, 0, 1, 17,
					'add:', -1, 1, 0, 1, 18,
					'add:', -1, 1, 0, 1, 19,
					'init:', self
				)
			#end:case
			case 13:
				global0._send('hide:')
				beast._send('setLoop:', 2, 'setCycle:', End, self)
			#end:case
			case 14:
				myConv._send(
					'add:', -1, 1, 0, 1, 20,
					'add:', -1, 1, 0, 1, 21,
					'add:', -1, 1, 0, 1, 22,
					'init:', self
				)
			#end:case
			case 15:
				global0._send('show:')
				beast._send('view:', 542, 'setLoop:', 0, 'setCycle:', Walk)
				cycles = 2
			#end:case
			case 16:
				myConv._send('add:', -1, 1, 0, 1, 23, 'init:', self)
			#end:case
			case 17:
				beast._send('setLoop:', 3, 'setMotion:', MoveTo, 96, 98, self)
				global0._send('setHeading:', 315)
			#end:case
			case 18:
				global0._send('setHeading:', 0)
				gate._send('hide:')
				beast._send(
					'view:', 532,
					'setScale:', 0,
					'setLoop:', 1,
					'cel:', 0,
					'setCycle:', End, self
				)
				gateFx._send('number:', 542, 'play:')
			#end:case
			case 19:
				beast._send('setLoop:', 2, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 20:
				gateFx._send('number:', 543, 'play:')
				gate._send('show:')
				beast._send(
					'setPri:', (gate._send('priority:') - 1),
					'posn:', 72, 62,
					'setLoop:', 3,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 21:
				global1._send('handsOn:')
				kernel.ScriptID(0, 5)._send('setReal:', global9._send('at:', 37), 0, 3, 0)
				proc913_1(46)
				global1._send('givePoints:', 1)
				global0._send('get:', 37)
				beast._send('dispose:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class beautyScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				cycles = 2
			#end:case
			case 1:
				gate._send('hide:')
				beast._send(
					'posn:', 72, 62,
					'view:', 533,
					'setLoop:', 0,
					'ignoreActors:', 1,
					'setCycle:', End, self
				)
				beauty._send('setScript:', beautyWalkScript, self)
			#end:case
			case 2:
				beast._send(
					'view:', 5406,
					'posn:', 96, 98,
					'setLoop:', 1,
					'cel:', 0,
					'setCycle:', End, self
				)
				gateFx._send('number:', 542, 'play:')
			#end:case
			case 3:
				gateFx._send('number:', 543, 'play:')
				gate._send('show:')
				beast._send(
					'view:', 542,
					'setScale:', Scaler, 100, 68, 190, 100,
					'setCycle:', Walk,
					'setStep:', 4, 3,
					'setLoop:', -1,
					'y:', (beast._send('y:') + 3),
					'setMotion:', MoveTo, 114, 134, self
				)
				kernel.UnLoad(128, 533)
				weasel._send('setScript:', weaselScript)
			#end:case
			case 4:#end:case
			case 5:
				beast._send('setLoop:', 4, 'cel:', 0)
				cycles = 2
			#end:case
			case 6:
				myConv._send(
					'add:', -1, 1, 0, 2, 1,
					'add:', -1, 1, 0, 2, 2,
					'add:', -1, 1, 0, 2, 3,
					'add:', -1, 1, 0, 2, 4,
					'add:', -1, 1, 0, 2, 5,
					'init:', self
				)
			#end:case
			case 7:
				beast._send('view:', 544, 'setLoop:', 2, 'cel:', 0, 'setCycle:', End, self)
				gateFx._send('number:', 546, 'play:')
				proc913_1(113)
			#end:case
			case 8:
				global91._send('say:', 1, 0, 2, 6, self)
			#end:case
			case 9:
				beauty._send('view:', 5405, 'setLoop:', 0, 'cel:', 0, 'setCycle:', End, self)
				kernel.UnLoad(128, 544)
			#end:case
			case 10:
				kernel.UnLoad(128, 252)
				global91._send('say:', 1, 0, 2, 7, self)
			#end:case
			case 11:
				global91._send('say:', 1, 0, 2, 8, self)
			#end:case
			case 12:
				beauty._send('setLoop:', 1, 'cel:', 0, 'setCycle:', End, self)
				gateFx._send('number:', 546, 'play:')
				proc913_1(43)
			#end:case
			case 13:
				beast._send(
					'view:', 547,
					'setLoop:', 4,
					'cel:', 0,
					'posn:', (beast._send('x:') - 1), (beast._send('y:') + 2)
				)
				global102._send('stop:')
				global102._send('number:', 544, 'loop:', -1, 'play:')
				seconds = 2
			#end:case
			case 14:
				beauty._send('view:', 546, 'setLoop:', 4, 'cel:', 2)
				cycles = 2
			#end:case
			case 15:
				myConv._send('add:', -1, 1, 0, 2, 9, 'add:', -1, 1, 0, 2, 10, 'init:', self)
			#end:case
			case 16:
				global0._send('setMotion:', MoveTo, (beauty._send('x:') + 30), beauty._send('y:'), self)
			#end:case
			case 17:
				proc913_4(global0, beauty, self)
			#end:case
			case 18:
				global91._send('say:', 1, 0, 2, 11, self)
			#end:case
			case 19:
				global91._send('say:', 1, 0, 2, 12, self)
			#end:case
			case 20:
				global0._send('get:', 5, 'hide:')
				if (not proc913_0(93)):
					proc913_1(112)
				#endif
				beauty._send(
					'view:', 549,
					'setLoop:', 2,
					'cel:', 0,
					'posn:', (beauty._send('x:') + 30), (beauty._send('y:') + 1),
					'setCycle:', End, self
				)
			#end:case
			case 21:
				beauty._send(
					'view:', 546,
					'posn:', (beauty._send('x:') - 30), (beauty._send('y:') - 1),
					'setLoop:', 4,
					'cel:', 0
				)
				kernel.UnLoad(128, 549)
				global0._send('show:')
				seconds = 1
			#end:case
			case 22:
				myConv._send('add:', -1, 1, 0, 2, 13, 'add:', -1, 1, 0, 2, 14, 'init:', self)
			#end:case
			case 23:
				global0._send(
					'ignoreActors:', 1,
					'ignoreHorizon:', 1,
					'setPri:', (beauty._send('priority:') - 1),
					'setMotion:', MoveTo, (beast._send('x:') + 32), beast._send('y:'), self
				)
			#end:case
			case 24:
				beast._send(
					'view:', 5403,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', (beast._send('x:') + 18), (beast._send('y:') + 1)
				)
				global0._send(
					'normal:', 0,
					'view:', 541,
					'setLoop:', 1,
					'cel:', 0,
					'posn:', (global0._send('x:') - 10), (global0._send('y:') + 4)
				)
				beauty._send('cel:', 3)
				cycles = 1
			#end:case
			case 25:
				beast._send('cel:', 1)
				cycles = 1
			#end:case
			case 26:
				beauty._send('cel:', 1)
				beast._send('setCycle:', End, self)
				global0._send('setCycle:', End, self)
			#end:case
			case 27: 0#end:case
			case 28:
				beast._send(
					'view:', 548,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', (beast._send('x:') - 16), (beast._send('y:') + 1)
				)
				global0._send(
					'get:', 24,
					'posn:', (global0._send('x:') + 10), (global0._send('y:') - 4),
					'reset:',
					'setPri:', (beauty._send('priority:') - 1)
				)
				cycles = 3
			#end:case
			case 29:
				kernel.UnLoad(128, 541)
				kernel.UnLoad(128, 5403)
				myConv._send('add:', -1, 1, 0, 2, 15, 'init:', self)
			#end:case
			case 30:
				global0._send(
					'setCycle:', Rev,
					'setLoop:', 1,
					'setMotion:', PolyPath, (global0._send('x:') + 20), global0._send('y:'), self
				)
			#end:case
			case 31:
				global0._send('reset:', 1)
				beast._send('setCycle:', End, self)
				beauty._send('view:', 548, 'setLoop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 32: 0#end:case
			case 33:
				global91._send('say:', 1, 0, 2, 16, self)
			#end:case
			case 34:
				beauty._send('hide:')
				beast._send(
					'view:', 5441,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', (beast._send('x:') + 22), beast._send('y:'),
					'setCycle:', End, self
				)
			#end:case
			case 35:
				beast._send('setLoop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 36:
				global0._send('setHeading:', 315)
				beast._send(
					'view:', 547,
					'setLoop:', -1,
					'setCycle:', Walk,
					'setLoop:', 3,
					'setPri:',
					'posn:', (beast._send('x:') - 9), (beast._send('y:') - 1),
					'setMotion:', MoveTo, 84, 102, self
				)
				beauty._send(
					'view:', 546,
					'setLoop:', 3,
					'posn:', (beast._send('x:') + 17), (beast._send('y:') + 1),
					'setPri:', (beast._send('priority:') - 1),
					'show:',
					'setCycle:', Walk,
					'setMotion:', PolyPath, 108, 104
				)
				kernel.UnLoad(128, 548)
			#end:case
			case 37:
				gate._send('hide:')
				beast._send(
					'view:', 534,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', 96, 98,
					'setScale:', 0,
					'setPri:', -1,
					'setCycle:', End, self
				)
				beauty._send('setPri:', -1)
				gateFx._send('number:', 542, 'play:')
				weaselScript._send('register:', 1)
			#end:case
			case 38:
				beauty._send('setMotion:', MoveTo, 87, 97, self)
			#end:case
			case 39:
				beauty._send('setMotion:', MoveTo, 98, 94, self)
			#end:case
			case 40:
				beast._send('view:', 5407, 'setLoop:', 0, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 41:
				gateFx._send('number:', 543, 'play:')
				beauty._send('dispose:')
				beast._send(
					'view:', 5408,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', 72, 62,
					'setCycle:', End, self
				)
			#end:case
			case 42:
				gate._send('show:')
				beast._send('dispose:')
				global1._send('givePoints:', 2)
				proc913_3()
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class beautyWalkScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				beauty._send('setMotion:', MoveTo, 157, 139, self)
			#end:case
			case 1:
				beauty._send('setLoop:', 1)
				ticks = 1
			#end:case
			case 2:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class weaselScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				weasel._send('setMotion:', MoveTo, 259, 165, self)
			#end:case
			case 1:
				weasel._send('cel:', 0)
				cycles = 1
			#end:case
			case 2:
				seconds = 5
			#end:case
			case 3:
				glint._send(
					'show:',
					'posn:', (weasel._send('x:') - 14), weasel._send('y:'), 5,
					'setCycle:', End, self
				)
			#end:case
			case 4:
				glint._send('setCycle:', Beg, self)
			#end:case
			case 5:
				if (not register):
					self._send('start:', 2, 'init:')
				else:
					glint._send('hide:')
					cycles = 1
				#endif
			#end:case
			case 6:
				weasel._send('setMotion:', MoveTo, 175, 183, self)
			#end:case
			case 7:
				glint._send(
					'show:',
					'posn:', (weasel._send('x:') - 13), weasel._send('y:'), 5,
					'setCycle:', End, self
				)
			#end:case
			case 8:
				glint._send('setCycle:', Beg, self)
			#end:case
			case 9:
				glint._send('dispose:')
				weasel._send('setMotion:', MoveTo, 90, 210, self)
			#end:case
			case 10:
				global1._send('handsOn:')
				weasel._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getWater(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if register:
					global0._send('setMotion:', PolyPath, 163, 122, self)
				else:
					global0._send('setMotion:', PolyPath, 165, 121, self)
				#endif
			#end:case
			case 1:
				global0._send(
					'normal:', 0,
					'setCel:', 0,
					'cycleSpeed:', 9,
					'view:', 5404,
					'setLoop:', (5 if register else 2),
					'setCycle:', End, self
				)
			#end:case
			case 2:
				global0._send('reset:', 6)
				cycles = 4
			#end:case
			case 3:
				if register:
					if (not proc913_0(14)):
						global1._send('givePoints:', 1)
					#endif
					(global161 |= 0x0001)
					global91._send('say:', 5, 43, 6, 0, self)
				else:
					global91._send('say:', 5, 5, 0, 0, self)
				#endif
			#end:case
			case 4:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

