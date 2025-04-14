#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 745
import sci_sh
import kernel
import Main
import n913
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	closeupWedding = 0,
)

@SCI.instance
class closeupWedding(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		super._send('init:', &rest)
		proc913_1(99)
		global2._send('noun:', 3)
		kernel.ScriptID(80, 0)._send('setFlag:', 710, 2048)
		global93._send('addToFront:', self)
		global74._send('addToFront:', self)
	#end:method

	@classmethod
	def setScript():
		seconds = 0
		super._send('setScript:', &rest)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		if 
			(and
				(global69._send('at:', 0) == global69._send('curIcon:'))
				(param1._send('type:') & 0x1040)
			)
			param1._send('claimed:', 1)
			next = kernel.ScriptID(744, 1)
			self._send('cue:')
		#endif
		param1._send('claimed:')
	#end:method

	@classmethod
	def dispose():
		global69._send('disable:')
		global93._send('delete:', self)
		global74._send('delete:', self)
		genieHead._send('dispose:', 'delete:')
		vizierHead._send('dispose:', 'delete:')
		saladinArm._send('dispose:', 'delete:')
		alexHead._send('dispose:', 'delete:')
		priestHead._send('dispose:', 'delete:')
		saladinHead._send('dispose:', 'delete:')
		glint1._send('dispose:', 'delete:')
		glint2._send('dispose:', 'delete:')
		global2._send('drawPic:', 740)
		proc913_2(99)
		global2._send('noun:', 3)
		global5._send('eachElementDo:', #show, 'eachElementDo:', #stopUpd)
		super._send('dispose:')
		global0._send('startUpd:')
		if proc913_0(156):
			global0._send('posn:', 149, 144)
		#endif
		kernel.UnLoad(128, 160)
		kernel.UnLoad(128, 161)
		kernel.UnLoad(128, 902)
		kernel.UnLoad(129, 160)
		kernel.UnLoad(143, 160)
		kernel.DisposeScript(1005)
		kernel.DisposeScript(745)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global5._send('eachElementDo:', #startUpd)
				global69._send('disable:')
				cycles = 1
			#end:case
			case 1:
				global5._send('eachElementDo:', #hide)
				global2._send('drawPic:', 160)
				global102._send('number:', 740, 'loop:', -1, 'play:')
				vizierHead._send('addToPic:')
				saladinArm._send('init:', 'stopUpd:')
				saladinHead._send('init:')
				alexHead._send('init:')
				priestHead._send('init:')
				seconds = cycles = 2
			#end:case
			case 2:
				global69._send('enable:')
			#end:case
			case 3:
				kernel.ScriptID(740, 7)._send(
					'add:', 160, 1, 0, 1, 1,
					'add:', 160, 1, 0, 1, 2,
					'add:', 160, 1, 0, 1, 3,
					'add:', 160, 1, 0, 1, 4,
					'add:', 160, 1, 0, 1, 5,
					'add:', 160, 1, 0, 1, 6,
					'init:', self
				)
			#end:case
			case 4:
				glint1._send('init:', 'setCycle:', End, self)
				glint2._send('init:', 'setCycle:', End)
			#end:case
			case 5:
				global102._send('number:', 746, 'loop:', -1, 'play:')
				glint1._send('setCycle:', Beg, self)
				glint2._send('setCycle:', Beg)
			#end:case
			case 6:
				kernel.ScriptID(740, 7)._send('add:', 160, 1, 0, 1, 7, 'add:', 160, 1, 0, 1, 8, 'init:', self)
			#end:case
			case 7:
				glint1._send('dispose:')
				glint2._send('dispose:')
				genieHead._send('init:', 'cel:', 0)
				cycles = 10
			#end:case
			case 8:
				kernel.DisposeScript(939)
				saladinArm._send('cel:', 2, 'startUpd:')
				if (not register = kernel.ScriptID(80, 0)._send('tstFlag:', 709, 128)):
					saladinArm._send('setCycle:', Beg, self)
				else:
					saladinArm._send('setScript:', drawSword, self)
					cycles = 1
				#endif
			#end:case
			case 9:
				if (not register):
					next = 0
					global91._send('say:', 1, 0, 2, 0, self, 160)
				else:
					global1._send('handsOn:')
					state.post('++')
				#endif
			#end:case
			case 10:
				saladinArm._send('setScript:', 0, 'setCycle:', End, self)
			#end:case
			case 11:
				cycles = 3
			#end:case
			case 12:
				global1._send('handsOff:')
				global69._send('disable:')
				if (not next):
					if (not register):
						kernel.UnLoad(128, 738)
						kernel.ScriptID(740, 5)._send('view:', 7424, 'loop:', 0, 'cel:', 0, 'setCycle:', 0)
						next = kernel.ScriptID(742, 3)
					else:
						kernel.ScriptID(744, 1)._send('register:', 29)
						next = kernel.ScriptID(744, 1)
					#endif
				#endif
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class showMirror(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		super._send('dispose:')
		saladinHead._send('dispose:', 'delete:')
		priestHead._send('dispose:', 'delete:')
		alexHead._send('dispose:', 'delete:')
		mirror._send('dispose:')
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				drawSword._send('caller:', 0)
				saladinArm._send('setScript:', 0)
				if saladinArm._send('cel:'):
					saladinArm._send('setCycle:', Beg, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				global91._send('say:', 4, 13, 0, 1, self, 160)
			#end:case
			case 2:
				genieHead._send('init:', 'cel:', 1, 'setCycle:', End)
				mirror._send('init:', 'cel:', 0, 'cycleSpeed:', 15, 'setCycle:', End, self)
			#end:case
			case 3:
				global1._send('givePoints:', 3)
				saladinArm._send('addToPic:')
				priestHead._send('cel:', 1, 'addToPic:')
				saladinHead._send('cel:', 1, 'addToPic:')
				alexHead._send('cel:', 1, 'addToPic:')
				genieHead._send('addToPic:')
				mirror._send('addToPic:')
				cycles = 18
			#end:case
			case 4:
				global91._send('say:', 4, 13, 0, 2, self, 160)
			#end:case
			case 5:
				client._send('seconds:', 0, 'next:', kernel.ScriptID(744, 0))
				kernel.ScriptID(740, 5)._send('view:', 7424, 'loop:', 0, 'cel:', 0, 'setCycle:', 0)
				global69._send('disable:')
				client._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class showReplicaLamp(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global91._send('say:', 7, 56, 0, 0, self, 160)
			#end:case
			case 1:
				closeupWedding._send('next:', kernel.ScriptID(744, 1), 'changeState:', 12)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class drawSword(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				seconds = 4
			#end:case
			case 1:
				if (saladinArm._send('cel:') > 0):
					saladinArm._send('cel:', (saladinArm._send('cel:') - 1), 'startUpd:')
					cycles = 2
				else:
					self._send('dispose:')
				#endif
			#end:case
			case 2:
				saladinArm._send('stopUpd:')
				state = -1
				cycles = 1
			#end:case
		#end:match
	#end:method

#end:class or instance

class CloseupProp(Prop):
	#property vars (may be empty)
	controlColor = 0
	
	@classmethod
	def onMe(param1 = None, *rest):
		(return
			(or
				super._send('onMe:', param1)
				(controlColor & kernel.OnControl(4, param1._send('x:'), param1._send('y:')))
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class genieHead(CloseupProp):
	#property vars (may be empty)
	x = 147
	y = 58
	noun = 4
	modNum = 160
	view = 160
	loop = 1
	cel = 1
	priority = 9
	signal = 16
	controlColor = 2
	
	@classmethod
	def doVerb(param1 = None, *rest):
		(cond
			case proc999_5(param1, 33, 18):
				global91._send('say:', noun, 18, 0, 0, 0, modNum)
			#end:case
			case proc999_5(param1, 57, 58, 59, 60, 43):
				kernel.ScriptID(740, 7)._send('add:', modNum, noun, 43, 0, 1)
				if (param1 != 43):
					kernel.ScriptID(740, 7)._send('add:', modNum, noun, 57, 0, 1)
				else:
					kernel.ScriptID(740, 7)._send('add:', modNum, noun, 43, 0, 2)
				#endif
				kernel.ScriptID(740, 7)._send('init:')
			#end:case
			case proc999_5(param1, 56, 2):
				global1._send('handsOff:')
				closeupWedding._send('seconds:', 0, 'next:', kernel.ScriptID(744, 1))
				global91._send('say:', noun, param1, 0, 0, closeupWedding, modNum)
			#end:case
			case proc999_5(param1, 67, 63):
				global1._send('handsOff:')
				proc913_1(156)
				closeupWedding._send('seconds:', 0, 'next:', kernel.ScriptID(744, 1))
				global91._send('say:', 4, 67, 0, 0, closeupWedding, 160)
			#end:case
			else:
				match param1
					case 13:
						closeupWedding._send('setScript:', showMirror)
					#end:case
					else:
						super._send('doVerb:', param1)
					#end:else
				#end:match
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class vizierHead(CloseupProp):
	#property vars (may be empty)
	x = 120
	y = 53
	noun = 7
	modNum = 160
	view = 160
	loop = 3
	controlColor = 4
	
	@classmethod
	def doVerb(param1 = None, *rest):
		(cond
			case proc999_5(param1, 33, 18):
				param1 = 65
				super._send('doVerb:', 65)
			#end:case
			case proc999_5(param1, 57, 58, 59, 60, 43):
				param1 = 43
				super._send('doVerb:', 43)
			#end:case
			case (param1 == 56):
				closeupWedding._send('setScript:', showReplicaLamp)
			#end:case
			else:
				super._send('doVerb:', param1)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class alexHead(CloseupProp):
	#property vars (may be empty)
	x = 51
	y = 50
	view = 160
	loop = 2
	controlColor = 8
	
	@classmethod
	def doVerb():
		global0._send('doVerb:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class priestHead(CloseupProp):
	#property vars (may be empty)
	x = 270
	y = 56
	noun = 8
	modNum = 160
	view = 160
	loop = 4
	controlColor = 32
	
#end:class or instance

@SCI.instance
class saladinArm(CloseupProp):
	#property vars (may be empty)
	x = 5
	y = 79
	noun = 5
	modNum = 160
	view = 160
	loop = 7
	cel = 3
	controlColor = 16
	
	@classmethod
	def doVerb(param1 = None, *rest):
		if proc999_5(param1, 33, 18):
			global91._send('say:', noun, 33, 0, 0, 0, modNum)
		else:
			super._send('doVerb:', param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class saladinHead(View):
	#property vars (may be empty)
	x = 10
	y = 24
	view = 160
	loop = 5
	
	@classmethod
	def doVerb():
		saladinArm._send('doVerb:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class mirror(Prop):
	#property vars (may be empty)
	x = 35
	y = 102
	view = 160
	cel = 2
	
#end:class or instance

@SCI.instance
class glint1(Prop):
	#property vars (may be empty)
	x = 179
	y = 47
	view = 902
	priority = 15
	signal = 24576
	cycleSpeed = 4
	
#end:class or instance

@SCI.instance
class glint2(Prop):
	#property vars (may be empty)
	x = 169
	y = 47
	view = 902
	priority = 15
	signal = 24576
	cycleSpeed = 4
	
#end:class or instance

