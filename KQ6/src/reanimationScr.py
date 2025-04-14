#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 282
import sci_sh
import kernel
import Main
import KQ6Print
import rm280
import pawnShopGenie
import n913
import PolyPath
import StopWalk
import Grooper
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	reanimationScr = 0,
	drinkPotionGenieScr = 1,
	genieTakeMintScr = 2,
	genieMirrorScr = 3,
	genieBadgerOwnerScr = 4,
	drinkPotionNoGenieScr = 5,
	givePeppermintScr = 6,
)

@SCI.instance
class reanimationScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('hide:')
				kernel.ScriptID(280, 2)._send(
					'posn:', 113, 144,
					'view:', 282,
					'loop:', 6,
					'cel:', 0,
					'setScript:', 0
				)
				ticks = 120
			#end:case
			case 1:
				global105._send('number:', 927, 'loop:', 1, 'play:', self)
				ticks = 30
			#end:case
			case 2:
				global91._send('say:', 1, 0, 8, 1, self)
			#end:case
			case 3: 0#end:case
			case 4:
				global105._send('client:', 0)
				kernel.ScriptID(280, 2)._send('setCycle:', End, self)
			#end:case
			case 5:
				kernel.ScriptID(280, 2)._send('setCycle:', Beg, self)
			#end:case
			case 6:
				kernel.ScriptID(280, 2)._send('loop:', 2, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 7:
				global91._send('say:', 1, 0, 8, 2, self)
			#end:case
			case 8:
				global91._send('say:', 1, 0, 8, 3, self)
			#end:case
			case 9:
				global91._send('say:', 1, 0, 8, 4, self)
			#end:case
			case 10:
				global102._send('number:', 240, 'loop:', -1, 'fade:', 70, 10, 20, 0)
				global0._send('show:', 'posn:', 123, 140, 'reset:', 3)
				kernel.ScriptID(280, 2)._send(
					'posn:', 135, 136,
					'loop:', 7,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 11:
				cycles = 2
			#end:case
			case 12:
				kernel.ScriptID(280, 2)._send(
					'view:', 2841,
					'loop:', 0,
					'cel:', 0,
					'posn:', 236, 127,
					'stopUpd:',
					'setScript:', kernel.ScriptID(280, 9)
				)
				global1._send('handsOn:')
				global102._send('number:', 240, 'loop:', -1, 'play:', 0, 'fade:', 70, 25, 10, 0)
				self._send('dispose:')
				kernel.DisposeScript(282)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class drinkPotionNoGenieScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('put:', 33, global11)
				global1._send('handsOff:')
				proc280_10(self)
			#end:case
			case 1:
				global0._send('setMotion:', PolyPath, 156, 136, self)
				global102._send('fade:', 0, 25, 10, 0)
			#end:case
			case 2:
				global0._send(
					'normal:', 0,
					'setSpeed:', 6,
					'posn:', 146, 140,
					'view:', 934,
					'loop:', 0,
					'cel:', 0,
					'setCycle:', CT, 2, 1, self
				)
			#end:case
			case 3:
				global105._send('number:', 925, 'loop:', 1, 'play:', self)
			#end:case
			case 4:
				global0._send('setCycle:', End, self)
			#end:case
			case 5:
				ticks = 30
			#end:case
			case 6:
				global0._send('posn:', 147, 141, 'loop:', 1, 'cel:', 0, 'setCycle:', End, self)
				global104._send('number:', 926, 'loop:', 1, 'play:')
			#end:case
			case 7:
				global91._send('say:', 2, 14, 10, 1, self)
			#end:case
			case 8:
				kernel.ScriptID(280, 2)._send(
					'posn:', 236, 127,
					'view:', 282,
					'loop:', 3,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 9:
				kernel.ScriptID(280, 2)._send(
					'posn:', 171, 110,
					'loop:', 4,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 10:
				ticks = 30
			#end:case
			case 11:
				if (global104._send('prevSignal:') != -1):
					state.post('--')
				#endif
				cycles = 2
			#end:case
			case 12:
				kernel.ScriptID(280, 2)._send(
					'posn:', 171, 110,
					'loop:', 5,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 13:
				global91._send('say:', 2, 14, 10, 2, self)
			#end:case
			case 14:
				ticks = 45
			#end:case
			case 15:
				global104._send('number:', 927, 'loop:', 1, 'play:', self)
			#end:case
			case 16:
				global104._send('client:', 0)
				global0._send('hide:')
				kernel.ScriptID(280, 2)._send(
					'posn:', 113, 144,
					'loop:', 6,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 17:
				global91._send('say:', 2, 14, 10, 3, self)
			#end:case
			case 18:
				kernel.ScriptID(280, 2)._send('loop:', 2, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 19:
				global91._send('say:', 2, 14, 10, 4, self, 'oneOnly:', 0)
			#end:case
			case 20:
				global102._send('number:', 240, 'loop:', -1, 'play:', 0, 'fade:', 70, 25, 10, 0)
				global0._send('show:', 'posn:', 123, 140, 'reset:', 3)
				kernel.ScriptID(280, 2)._send(
					'posn:', 135, 136,
					'loop:', 7,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 21:
				cycles = 2
			#end:case
			case 22:
				kernel.ScriptID(280, 2)._send(
					'view:', 2841,
					'loop:', 0,
					'cel:', 0,
					'posn:', 236, 127,
					'stopUpd:',
					'setScript:', kernel.ScriptID(280, 9)
				)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(282)
	#end:method

#end:class or instance

@SCI.instance
class drinkPotionGenieScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('put:', 33, global11)
				global1._send('handsOff:')
				global1._send('givePoints:', 3)
				proc280_10(self)
			#end:case
			case 1:
				proc913_1(41)
				proc913_1(82)
				global91._send('say:', 2, 14, 9, 1, self, 280)
				global102._send('fade:')
			#end:case
			case 2:
				global0._send('setMotion:', PolyPath, 156, 136, self)
				global103._send('number:', 281, 'loop:', -1, 'play:')
			#end:case
			case 3:
				global91._send('say:', 2, 14, 9, 2, self, 280)
			#end:case
			case 4:
				global91._send('say:', 2, 14, 9, 3, self, 280)
			#end:case
			case 5:
				proc281_1(self)
			#end:case
			case 6:
				kernel.ScriptID(281, 0)._send(
					'view:', 289,
					'posn:', 88, 129,
					'setLoop:', Grooper,
					'loop:', 3
				)
				cycles = 2
			#end:case
			case 7:
				kernel.ScriptID(281, 0)._send('setHeading:', 90, self)
			#end:case
			case 8:
				global0._send(
					'normal:', 0,
					'setSpeed:', 6,
					'posn:', 146, 140,
					'view:', 2821,
					'loop:', 0,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 9:
				global91._send('say:', 2, 14, 9, 4, self, 280)
			#end:case
			case 10:
				global91._send('say:', 2, 14, 9, 5, self, 280)
			#end:case
			case 11:
				global0._send('loop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 12:
				global0._send(
					'normal:', 0,
					'setSpeed:', 6,
					'posn:', 146, 140,
					'view:', 934,
					'loop:', 0,
					'cel:', 0,
					'setCycle:', CT, 2, 1, self
				)
			#end:case
			case 13:
				global105._send('number:', 925, 'loop:', 1, 'play:', self)
			#end:case
			case 14:
				global0._send('setCycle:', End, self)
			#end:case
			case 15:
				global103._send('fade:')
				ticks = 30
			#end:case
			case 16:
				global91._send('say:', 2, 14, 9, 6, self, 280)
			#end:case
			case 17:
				global0._send('posn:', 147, 141, 'loop:', 1, 'cel:', 0, 'setCycle:', End, self)
				global104._send('number:', 926, 'loop:', 1, 'play:')
			#end:case
			case 18:
				kernel.ScriptID(280, 2)._send(
					'setPri:', -1,
					'posn:', 236, 127,
					'view:', 282,
					'loop:', 3,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 19:
				ticks = 120
			#end:case
			case 20:
				kernel.ScriptID(280, 2)._send(
					'posn:', 171, 110,
					'setPri:', 14,
					'loop:', 4,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 21:
				if (global104._send('prevSignal:') != -1):
					state.post('--')
				#endif
				cycles = 2
			#end:case
			case 22:
				global91._send('say:', 2, 14, 9, 7, self, 280)
			#end:case
			case 23:
				kernel.ScriptID(280, 2)._send('loop:', 5, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 24:
				global91._send('say:', 2, 14, 9, 8, self, 280)
			#end:case
			case 25:
				proc280_8(0)
				kernel.ScriptID(281, 0)._send('view:', 2833, 'loop:', 0, 'cel:', 0, 'setCycle:', Fwd)
				ticks = 90
			#end:case
			case 26:
				kernel.ScriptID(281, 0)._send('setCycle:', End, self)
			#end:case
			case 27:
				kernel.ScriptID(281, 0)._send('view:', 289, 'loop:', 0, 'cel:', 0, 'setHeading:', 270, self)
			#end:case
			case 28:
				self._send('setScript:', genieExitScr, self)
			#end:case
			case 29:
				ticks = 45
			#end:case
			case 30:
				global2._send('newRoom:', 145)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genieMirrorScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global91._send('say:', 5, 13, 0, 1, self)
			#end:case
			case 1:
				global0._send('setMotion:', PolyPath, 138, 132, self)
			#end:case
			case 2:
				global0._send('setHeading:', 270, self)
				proc281_1(self)
			#end:case
			case 3: 0#end:case
			case 4:
				(cond
					case (kernel.ScriptID(281, 0)._send('cel:') > 3):
						kernel.ScriptID(281, 0)._send('setCycle:', CT, 3, -1, self)
					#end:case
					case (kernel.ScriptID(281, 0)._send('cel:') < 3):
						kernel.ScriptID(281, 0)._send('setCycle:', CT, 3, 1, self)
					#end:case
					else:
						ticks = 1
					#end:else
				)
			#end:case
			case 5:
				global0._send(
					'setSpeed:', 6,
					'normal:', 0,
					'view:', 283,
					'loop:', 5,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 6:
				global91._send('say:', 5, 13, 0, 2, self)
			#end:case
			case 7:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 8:
				cycles = 2
			#end:case
			case 9:
				global0._send('reset:', 7)
				cycles = 2
			#end:case
			case 10:
				proc280_8(0)
				self._send('setScript:', genieExitScr, self)
			#end:case
			case 11:
				global91._send('say:', 5, 13, 0, 3, self, 'oneOnly:', 0)
			#end:case
			case 12:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(282)
	#end:method

#end:class or instance

@SCI.instance
class genieExitScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				kernel.ScriptID(281, 0)._send(
					'signal:', 16384,
					'cycleSpeed:', 3,
					'moveSpeed:', 3,
					'view:', 289,
					'setCycle:', StopWalk, -1,
					'setMotion:', PolyPath, 51, 124, self
				)
			#end:case
			case 1:
				kernel.ScriptID(280, 3)._send('setPri:', 14, 'setCycle:', End, self)
				global105._send('number:', 901, 'loop:', 1, 'play:')
			#end:case
			case 2:
				kernel.ScriptID(281, 0)._send('setMotion:', MoveTo, 35, 124, self)
			#end:case
			case 3:
				kernel.ScriptID(281, 0)._send('dispose:')
				kernel.ScriptID(280, 3)._send('setPri:', -1, 'setCycle:', Beg, self)
			#end:case
			case 4:
				global105._send('number:', 902, 'loop:', 1, 'play:')
				cycles = 2
			#end:case
			case 5:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genieTakeMintScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				proc280_8(0)
				proc281_1(self)
			#end:case
			case 1:
				kernel.ScriptID(281, 0)._send(
					'signal:', 16384,
					'view:', 289,
					'setCycle:', Walk,
					'setMotion:', PolyPath, 183, 132, self
				)
			#end:case
			case 2:
				global91._send('say:', 4, 70, 19, 10, self)
			#end:case
			case 3:
				kernel.ScriptID(281, 0)._send(
					'view:', 2834,
					'setPri:', 1,
					'loop:', 0,
					'cel:', 0,
					'posn:', 187, 134,
					'setCycle:', End, self
				)
			#end:case
			case 4:
				kernel.UnLoad(128, 289)
				kernel.ScriptID(281, 0)._send('loop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 5:
				kernel.ScriptID(281, 0)._send('cel:', 0, 'setCycle:', End, self)
			#end:case
			case 6:
				kernel.ScriptID(281, 0)._send('setCycle:', Beg, self)
			#end:case
			case 7:
				kernel.ScriptID(281, 0)._send(
					'cel:', kernel.ScriptID(281, 0)._send('lastCel:'),
					'setCycle:', Beg, self
				)
			#end:case
			case 8:
				cycles = 2
			#end:case
			case 9:
				global91._send('say:', 4, 70, 19, 11, self)
			#end:case
			case 10:
				kernel.ScriptID(281, 0)._send(
					'view:', 2835,
					'loop:', 2,
					'cel:', 0,
					'posn:', 190, 134,
					'setCycle:', End, self
				)
			#end:case
			case 11:
				kernel.UnLoad(128, 2834)
				kernel.ScriptID(281, 0)._send(
					'posn:', 168, 133,
					'setLoop:', 3,
					'cel:', 0,
					'setStep:', 4, 3,
					'setCycle:', Walk
				)
				cycles = 2
			#end:case
			case 12:
				kernel.ScriptID(281, 0)._send('setMotion:', PolyPath, 51, 124, self)
			#end:case
			case 13:
				kernel.ScriptID(281, 0)._send('view:', 289, 'setLoop:', -1, 'loop:', 1, 'posn:', 51, 124)
				kernel.ScriptID(280, 3)._send('setPri:', 14, 'setCycle:', End)
				global105._send('number:', 901, 'loop:', 1, 'play:')
				ticks = 12
			#end:case
			case 14:
				kernel.UnLoad(128, 2835)
				kernel.ScriptID(281, 0)._send('setMotion:', MoveTo, 35, 124, self)
			#end:case
			case 15:
				kernel.ScriptID(281, 0)._send('dispose:')
				kernel.ScriptID(280, 3)._send('setCycle:', Beg, self)
			#end:case
			case 16:
				kernel.UnLoad(128, 289)
				global105._send('number:', 902, 'loop:', 1, 'play:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genieBadgerOwnerScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				proc280_8(0)
				kernel.ScriptID(281, 0)._send(
					'view:', 289,
					'loop:', 0,
					'setLoop:', Grooper,
					'cycleSpeed:', 6,
					'setCycle:', StopWalk, -1,
					'ignoreActors:',
					'posn:', 192, 138
				)
				register = 0
				cycles = 1
			#end:case
			case 1:
				global0._send('setMotion:', MoveTo, 80, 145, self)
			#end:case
			case 2:
				global0._send('setHeading:', 90, self)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				KQ6Print._send(
					'font:', global22,
					'posn:', 120, 40,
					'width:', 175,
					'say:', 0, 1, 0, 3, 1,
					'init:', self
				)
			#end:case
			case 5:
				global91._send('say:', 1, 0, 3, 2, self, 280)
			#end:case
			case 6:
				KQ6Print._send(
					'font:', global22,
					'posn:', 120, 40,
					'width:', 175,
					'say:', 0, 1, 0, 3, 3,
					'init:', self
				)
			#end:case
			case 7:
				global91._send('say:', 1, 0, 3, 4, self, 280)
			#end:case
			case 8:
				KQ6Print._send(
					'font:', global22,
					'posn:', 120, 40,
					'width:', 175,
					'say:', 0, 1, 0, 3, 5,
					'init:', self
				)
			#end:case
			case 9:
				kernel.ScriptID(281, 0)._send('setHeading:', 270, self)
			#end:case
			case 10:
				self._send('setScript:', genieExitScr, self)
			#end:case
			case 11:
				cycles = 2
			#end:case
			case 12:
				kernel.ScriptID(280, 2)._send('setScript:', kernel.ScriptID(280, 9))
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(282)
	#end:method

#end:class or instance

@SCI.instance
class givePeppermintScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				proc281_1(self)
			#end:case
			case 1:
				global91._send('say:', 5, 67, 0, 1, self)
			#end:case
			case 2:
				global0._send('setMotion:', PolyPath, 118, 133, self)
			#end:case
			case 3:
				global0._send('view:', 2832, 'loop:', 0, 'cel:', 0, 'setSpeed:', 6, 'normal:', 0)
				cycles = 2
			#end:case
			case 4:
				global0._send('setCycle:', End, self)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				global91._send('say:', 5, 67, 0, 2, self)
			#end:case
			case 7:
				global91._send('say:', 5, 67, 0, 3, self)
			#end:case
			case 8:
				kernel.ScriptID(281, 0)._send(
					'view:', 2834,
					'loop:', 0,
					'cel:', 0,
					'cycleSpeed:', 9,
					'posn:', 92, 134
				)
				cycles = 2
			#end:case
			case 9:
				kernel.ScriptID(281, 0)._send('setCycle:', End, self)
			#end:case
			case 10:
				global0._send('setCycle:', Beg)
				kernel.ScriptID(281, 0)._send('loop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 11:
				global0._send('reset:', 1)
				kernel.ScriptID(281, 0)._send('cel:', 0, 'setCycle:', End, self)
			#end:case
			case 12:
				kernel.ScriptID(281, 0)._send('setCycle:', Beg, self)
			#end:case
			case 13:
				kernel.ScriptID(281, 0)._send(
					'cel:', kernel.ScriptID(281, 0)._send('lastCel:'),
					'setCycle:', Beg, self
				)
			#end:case
			case 14:
				global91._send('say:', 5, 67, 0, 4, self)
			#end:case
			case 15:
				kernel.ScriptID(281, 0)._send('view:', 2835, 'loop:', 2, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 16:
				proc280_8(0)
				kernel.ScriptID(281, 0)._send(
					'setLoop:', 3,
					'setCycle:', Walk,
					'posn:', 70, 133,
					'setMotion:', PolyPath, 51, 124, self
				)
			#end:case
			case 17:
				kernel.ScriptID(281, 0)._send('view:', 289, 'setLoop:', -1, 'loop:', 1, 'posn:', 51, 124)
				kernel.ScriptID(280, 3)._send('setPri:', 14, 'setCycle:', End)
				global105._send('number:', 901, 'loop:', 1, 'play:')
				ticks = 12
			#end:case
			case 18:
				kernel.ScriptID(281, 0)._send('setMotion:', MoveTo, 35, 124, self)
			#end:case
			case 19:
				kernel.ScriptID(281, 0)._send('dispose:')
				kernel.ScriptID(280, 3)._send('setCycle:', Beg, self)
			#end:case
			case 20:
				global105._send('number:', 902, 'loop:', 1, 'play:')
				cycles = 2
			#end:case
			case 21:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(282)
	#end:method

#end:class or instance

