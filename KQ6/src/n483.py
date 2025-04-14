#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 483
import sci_sh
import kernel
import Main
import n913
import Conversation
import PolyPath
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	proc483_0 = 0,
	proc483_1 = 1,
	proc483_2 = 2,
	proc483_3 = 3,
	proc483_4 = 4,
)

@SCI.procedure
def proc483_0(param1 = None, *rest):
	kernel.ScriptID(480, 5)._send('register:', 1)
	global0._send('setScript:', getBottle, 0, param1)
#end:procedure

@SCI.procedure
def proc483_1():
	kernel.ScriptID(480, 5)._send('register:', 1)
	global0._send('setScript:', getGrapes)
#end:procedure

@SCI.procedure
def proc483_2(param1 = None, *rest):
	kernel.ScriptID(480, 5)._send('register:', 1)
	global0._send('setScript:', getTomato, 0, param1)
#end:procedure

@SCI.procedure
def proc483_3(param1 = None, *rest):
	kernel.ScriptID(480, 5)._send('register:', 1)
	global0._send('setScript:', pickLettuce, 0, param1)
#end:procedure

@SCI.procedure
def proc483_4(param1 = None, *rest):
	kernel.ScriptID(480, 5)._send('register:', 1)
	global0._send('setScript:', chokeDie, 0, param1)
#end:procedure

@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class getGrapes(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global91._send('say:', 12, 5, 0, 1, self, 480)
			#end:case
			case 1:
				global0._send('setMotion:', PolyPath, 16, 95, self)
			#end:case
			case 2:
				global0._send('setHeading:', 0)
				ticks = 6
			#end:case
			case 3:
				myConv._send('add:', 480, 12, 5, 0, 2, 'add:', 480, 12, 5, 0, 3, 'init:', self)
			#end:case
			case 4:
				global1._send('handsOn:')
				global0._send('setHeading:', 180)
				self._send('dispose:')
				kernel.DisposeScript(483)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getTomato(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 170, 157, self)
			#end:case
			case 1:
				global0._send('setPri:', 12, 'setMotion:', PolyPath, 154, 157, self)
			#end:case
			case 2:
				global1._send('givePoints:', 1)
				global0._send(
					'view:', 481,
					'setLoop:', 3,
					'cel:', 0,
					'posn:', 151, 157,
					'normal:', 0,
					'cycleSpeed:', 12,
					'setCycle:', CT, 2, 1, self
				)
			#end:case
			case 3:
				global91._send('say:', 6, 5, 0, 1, self, 480)
			#end:case
			case 4:
				register._send('dispose:')
				if global169:
					kernel.DrawPic(480, 15)
				else:
					kernel.DrawPic(480)
				#endif
				kernel.ScriptID(480, 7)._send('cel:', 0, 'init:', 'addToPic:')
				global0._send('setCycle:', End, self)
			#end:case
			case 5:
				global91._send('say:', 6, 5, 0, 2, self, 480)
			#end:case
			case 6:
				global1._send('handsOn:')
				global0._send('posn:', 154, 157, 'reset:', 7)
				self._send('dispose:')
				kernel.DisposeScript(483)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class pickLettuce(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				if (not proc913_0(119)):
					proc913_1(119)
					global1._send('givePoints:', 1)
				#endif
				if global0._send('has:', 21):
					global91._send('say:', 10, 5, 31, 1, self, 480)
				else:
					global91._send('say:', 10, 5, 0, 1, self, 480)
				#endif
			#end:case
			case 1:
				global0._send('setMotion:', PolyPath, 180, 133, self)
			#end:case
			case 2:
				global0._send('setHeading:', 335)
				ticks = 6
			#end:case
			case 3:
				global0._send(
					'view:', 481,
					'posn:', 170, 136,
					'setLoop:', 2,
					'cel:', 0,
					'normal:', 0,
					'cycleSpeed:', 12,
					'get:', 21,
					'setCycle:', End, self
				)
			#end:case
			case 4:
				global91._send('say:', 10, 5, 0, 2, self, 480)
			#end:case
			case 5:
				global1._send('handsOn:')
				global0._send('posn:', 180, 133, 'reset:', 7)
				global9._send('at:', 21)._send(
					'state:', 0,
					'noun:', 20,
					'message:', 52,
					'cel:', 4,
					'setCursor:', 990, 1, 4
				)
				kernel.ScriptID(0, 7)._send('setReal:', global9._send('at:', 21), 30, 2)
				self._send('dispose:')
				kernel.DisposeScript(483)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class chokeDie(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				if (register == 5):
					global91._send('say:', 13, 5, 0, 1, self, 480)
				else:
					global91._send('say:', 13, 3, 0, 1, self, 480)
				#endif
			#end:case
			case 1:
				if (register == 5):
					global0._send('setMotion:', PolyPath, 60, 98, self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 2:
				global0._send('setHeading:', 0)
				cycles = 8
			#end:case
			case 3:
				global0._send('normal:', 0, 'view:', 486, 'setLoop:', 0, 'cel:', 0)
				global102._send('number:', 487, 'setLoop:', 1, 'play:')
				cycles = 6
			#end:case
			case 4:
				global91._send('say:', 13, 5, 0, 2, self, 480)
			#end:case
			case 5:
				global0._send('cycleSpeed:', 12, 'setCycle:', CT, 3, 1, self)
			#end:case
			case 6:
				myConv._send(
					'add:', 480, 13, 5, 0, 3,
					'add:', 480, 13, 5, 0, 4,
					'add:', 480, 13, 5, 0, 5,
					'add:', 480, 13, 5, 0, 6,
					'init:', self
				)
			#end:case
			case 7:
				global0._send('cel:', 4)
				ticks = 6
			#end:case
			case 8:
				global91._send('say:', 13, 5, 0, 7, self, 480)
			#end:case
			case 9:
				global0._send('setCycle:', End, self)
			#end:case
			case 10:
				global91._send('say:', 13, 5, 0, 8, self, 480)
			#end:case
			case 11:
				global91._send('say:', 13, 5, 0, 9, self, 480)
			#end:case
			case 12:
				proc0_1(22)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getBottle(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				if (register == 0):
					global0._send(
						'ignoreActors:', 1,
						'illegalBits:', 0,
						'setMotion:', PolyPath, 215, 155, self
					)
				else:
					global0._send(
						'ignoreActors:', 1,
						'illegalBits:', 0,
						'setMotion:', PolyPath, 286, 79, self
					)
				#endif
			#end:case
			case 1:
				if (register == 1):
					global0._send(
						'normal:', 0,
						'view:', 488,
						'setLoop:', 0,
						'cel:', 0,
						'cycleSpeed:', 12,
						'setCycle:', CT, 2, 1, self,
						'posn:', 292, 78
					)
				else:
					global0._send(
						'normal:', 0,
						'view:', 4811,
						'setLoop:', 2,
						'cel:', 0,
						'cycleSpeed:', 12,
						'setCycle:', CT, 1, 1, self,
						'posn:', 227, 161
					)
				#endif
			#end:case
			case 2:
				if (not register):
					kernel.ScriptID(480, 3)._send('dispose:')
				else:
					kernel.ScriptID(480, 4)._send('dispose:')
				#endif
				global0._send('setCycle:', End, self)
			#end:case
			case 3:
				if (register == 1):
					global91._send('say:', 22, 5, 0, 1, self, 480)
				else:
					global91._send('say:', 8, 5, 0, 1, self, 480)
				#endif
			#end:case
			case 4:
				if (register == 1):
					global0._send('reset:', 0, 'setMotion:', PolyPath, 197, 116, self, 'get:', 46)
				else:
					global0._send(
						'posn:', (global0._send('x:') - 15), (global0._send('y:') - 6),
						'get:', 33,
						'reset:', 0
					)
					cycles = 2
				#endif
			#end:case
			case 5:
				global1._send('handsOn:')
				self._send('dispose:')
				kernel.DisposeScript(483)
			#end:case
		#end:match
	#end:method

#end:class or instance

