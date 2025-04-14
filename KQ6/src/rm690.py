#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 690
import sci_sh
import kernel
import Main
import rgDead
import KQ6Print
import KQ6Room
import Conversation
import MCyc
import Feature
import LoadMany
import Window
import Sound
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm690 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None
local4 = None
local5 = [2, 0, 8, 55, 2, 1, 17, 58, 2, 2, 21, 59, 2, 3, 32, 58, 2, 4, 43, 53, 2, 5, 53, 50, 2, 6, 59, 51, 2, 7, 65, 52, 2, 8, 73, 53, 2, 9, 85, 56, 2, 10, 87, 61, 2, 11, 89, 72, 3, 0, 282, 55, 3, 1, 291, 56, 3, 1, 291, 56, 3, 1, 291, 56, 3, 2, 302, 57, 3, 3, 313, 57, 3, 4, 318, 57, 3, 5, 318, 59, -32768]
local86 = [4, 0, 311, 105, 4, 1, 302, 107, 4, 2, 293, 111, 4, 3, 278, 112, 4, 4, 269, 123, 5, 0, 83, 108, 5, 1, 75, 111, 5, 2, 66, 113, 5, 3, 54, 113, 5, 4, 44, 118, 5, 5, 33, 117, 5, 6, 22, 118, 5, 7, 10, 119, 5, 8, 3, 115, -32768]


@SCI.instance
class rm690(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 690
	south = 680
	
	@classmethod
	def init():
		kernel.Load(128, 691)
		flame._send('init:', 'setCycle:', Fwd)
		alex._send('init:')
		lord._send('init:')
		leftarm._send('init:')
		rightarm._send('init:')
		deadHand._send('init:')
		deadFist._send('init:')
		deadEyes._send('init:', 'setScript:', eyeScript)
		global1._send('handsOff:')
		global69._send('disable:', 0)
		self._send('setScript:', introScript)
		super._send('init:', &rest)
	#end:method

	@classmethod
	def newRoom():
		introGhost._send('setCycle:', 0)
		proc958_0(0, 942)
		super._send('newRoom:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class sfx(Sound):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class alex(Actor):
	#property vars (may be empty)
	x = 127
	y = 144
	noun = 2
	view = 691
	priority = 2
	signal = 16
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 31:
				global91._send('say:', noun, param1, 0)
			#end:case
			case 1:
				global91._send('say:', noun, param1, 0)
			#end:case
			case 5:
				global91._send('say:', noun, param1, 0)
			#end:case
			else:
				global91._send('say:', noun, 0, 0)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class flame(Actor):
	#property vars (may be empty)
	x = 22
	y = 84
	view = 690
	loop = 1
	cycleSpeed = 10
	
#end:class or instance

@SCI.instance
class lord(Feature):
	#property vars (may be empty)
	noun = 4
	onMeCheck = 6
	
	@classmethod
	def doVerb(param1 = None, *rest):
		if proc999_5(param1, 28, 8, 14, 30, 31, 47, 50, 1, 32, 65, 68, 33, 70, 16, 37):
			global91._send('say:', noun, param1)
		else:
			match param1
				case 5:
					global1._send('handsOff:')
					global2._send('setScript:', alexHand)
				#end:case
				case 48:
					global1._send('handsOff:')
					global1._send('givePoints:', 2)
					global2._send('setScript:', issueChallenge)
				#end:case
				case 13:
					if local0:
						global91._send('say:', noun, param1, 5)
					else:
						global1._send('handsOff:')
						global1._send('givePoints:', 4)
						global2._send('setScript:', holdUpMirror)
					#endif
				#end:case
				case 42:
					if local0:
						global91._send('say:', noun, param1, 5)
					else:
						global91._send('say:', noun, param1, 6)
					#endif
				#end:case
				case 2:
					if local0:
						global91._send('say:', noun, param1, 5)
					else:
						global91._send('say:', noun, param1, 6)
					#endif
				#end:case
				else:
					if local0:
						global91._send('say:', noun, 0, 5)
					else:
						global91._send('say:', noun, 0, 6)
					#endif
				#end:else
			#end:match
		#endif
	#end:method

#end:class or instance

@SCI.instance
class introScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cycles = 5
			#end:case
			case 1:
				global91._send('say:', 1, 0, 1, 0, self)
			#end:case
			case 2:
				local0 = 1
				introGhost._send('init:', 'setCycle:', MCyc, @local5, introGhost)
				global1._send('handsOn:')
				global69._send('disable:', 0)
				seconds = 15
			#end:case
			case 3:
				global1._send('handsOff:')
				local0 = 0
				global91._send('say:', 1, 0, 2, 0, self)
			#end:case
			case 4:
				cycles = 1
			#end:case
			case 5:
				rgDead._send('stateOf690:', 1)
				client._send('setScript:', deadTouch, 0, 1)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class rightarm(Actor):
	#property vars (may be empty)
	x = 145
	y = 144
	view = 691
	loop = 1
	priority = 2
	signal = 16400
	cycleSpeed = 1
	
#end:class or instance

@SCI.instance
class leftarm(Actor):
	#property vars (may be empty)
	x = 110
	y = 147
	view = 691
	loop = 2
	priority = 2
	signal = 16400
	
#end:class or instance

@SCI.instance
class deadTouch(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global102._send('number:', 682, 'loop:', 1, 'play:')
				deadHand._send('setCycle:', End, self)
			#end:case
			case 1:
				seconds = 1
			#end:case
			case 2:
				if register:
					global91._send('say:', 1, 0, 4, 0, self)
				else:
					global91._send('say:', 4, 5, 0, 0, self)
				#endif
			#end:case
			case 3:
				deadHand._send('setCycle:', Beg, self)
			#end:case
			case 4:
				leftarm._send('hide:')
				rightarm._send('hide:')
				alex._send(
					'view:', 691,
					'setLoop:', 7,
					'cel:', 0,
					'posn:', 120, 139,
					'cycleSpeed:', 6,
					'setCycle:', End, self
				)
			#end:case
			case 5:
				alex._send('hide:')
			#end:case
			case 6:
				global69._send('disable:')
				match rgDead._send('stateOf690:')
					case 1:
						global2._send('setScript:', deadInHereScript, 0, 24)
					#end:case
					else:
						global2._send('setScript:', deadInHereScript, 0, 23)
					#end:else
				#end:match
			#end:case
		#end:match
	#end:method

	@classmethod
	def doit():
		super._send('doit:')
		if ((state == 5) and (global102._send('prevSignal:') == -1)):
			self._send('cue:')
		#endif
	#end:method

#end:class or instance

@SCI.instance
class deadInHereScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cycles = 1
			#end:case
			case 1:
				global102._send('number:', 970, 'loop:', 1, 'play:')
				global5._send('eachElementDo:', #dispose)
				global2._send('drawPic:', 98, 10)
				kernel.Message(0, 916, 0, 0, register, 1, @temp1)
				kernel.Display(@temp1, 100, 29, 40, 106, 260, 102, 47, 105, global22, 101, 1)
				global0._send(
					'init:',
					'view:', 8902,
					'loop:', 0,
					'cel:', 0,
					'normal:', 0,
					'setScale:', 0,
					'cycleSpeed:', 25,
					'scaleX:', 128,
					'scaleY:', 128,
					'posn:', 159, 125,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				global1._send('setCursor:', global20)
				while True: #repeat
					match
						(= temp0
							KQ6Print._send(
								'window:', DeathWindow,
								'addText:', r"""Please select:""", 62, 0,
								'posn:', 63, 130,
								'addButton:', 1, r"""Restore""", 0, 15,
								'addButton:', 2, r"""Restart""", 70, 15,
								'addButton:', 3, r"""Quit""", 140, 15,
								'init:'
							)
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
class DeathWindow(SysWindow):
	#property vars (may be empty)
	@classmethod
	def open():
		color = 47
		back = 0
		super._send('open:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class issueChallenge(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				local0 = 0
				rightarm._send('view:', 691, 'setLoop:', 3, 'setCycle:', End, self)
			#end:case
			case 1:
				global91._send('say:', 4, 48, 0, 1, self)
			#end:case
			case 2:
				rightarm._send('setLoop:', 4, 'setCycle:', End, self)
				global0._send('put:', 15, 690)
			#end:case
			case 3:
				sfx._send('number:', 683, 'loop:', 1, 'play:')
				rightarm._send('setLoop:', 1)
				cycles = 2
			#end:case
			case 4:
				theConv._send(
					'add:', -1, 4, 48, 0, 2,
					'add:', -1, 4, 48, 0, 3,
					'add:', -1, 4, 48, 0, 4,
					'add:', -1, 4, 48, 0, 5,
					'init:', self
				)
			#end:case
			case 5:
				deadFist._send('setCycle:', CT, 5, 1, self)
			#end:case
			case 6:
				sfx._send('number:', 681, 'loop:', 1, 'play:')
				deadFist._send('cel:', 6)
				cycles = 2
			#end:case
			case 7:
				theConv._send(
					'add:', -1, 4, 48, 0, 6,
					'add:', -1, 4, 48, 0, 7,
					'add:', -1, 4, 48, 0, 8,
					'add:', -1, 4, 48, 0, 9,
					'add:', -1, 4, 48, 0, 10,
					'init:', self
				)
			#end:case
			case 8:
				theConv._send(
					'add:', -1, 4, 48, 0, 11,
					'add:', -1, 4, 48, 0, 12,
					'add:', -1, 4, 48, 0, 13,
					'add:', -1, 4, 48, 0, 14,
					'add:', -1, 4, 48, 0, 15,
					'add:', -1, 4, 48, 0, 16,
					'add:', -1, 4, 48, 0, 17,
					'add:', -1, 4, 48, 0, 18,
					'add:', -1, 4, 48, 0, 19,
					'init:', self
				)
			#end:case
			case 9:
				global1._send('handsOn:')
				global69._send('disable:', 0)
				local1 = 1
				introGhost._send('init:', 'setCycle:', MCyc, @local86, introGhost)
				seconds = 20
			#end:case
			case 10:
				global1._send('handsOff:')
				local1 = 0
				global91._send('say:', 1, 0, 3, 0, self)
			#end:case
			case 11:
				cycles = 1
			#end:case
			case 12:
				rgDead._send('stateOf690:', 2)
				client._send('setScript:', deadTouch, 0, 1)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class holdUpMirror(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cycles = 5
			#end:case
			case 1:
				local2 = global89._send('x:')
				local3 = global89._send('y:')
				local4 = global89._send('talkWidth:')
				global89._send('x:', 10, 'y:', 10, 'talkWidth:', 100)
				theConv._send('add:', -1, 4, 13, 6, 1, 'init:', self)
			#end:case
			case 2:
				global102._send('fade:')
				local1 = 0
				leftarm._send('hide:')
				rightarm._send(
					'setLoop:', 5,
					'cycleSpeed:', 7,
					'posn:', 149, 148,
					'setCycle:', End, self
				)
			#end:case
			case 3:
				sfx._send('number:', 684, 'loop:', -1, 'play:')
				lookMirror._send('init:')
				seconds = 2
			#end:case
			case 4:
				theConv._send(
					'add:', -1, 4, 13, 6, 2,
					'add:', -1, 4, 13, 6, 3,
					'add:', -1, 4, 13, 6, 4,
					'add:', -1, 4, 13, 6, 5,
					'add:', -1, 4, 13, 6, 6,
					'add:', -1, 4, 13, 6, 7,
					'add:', -1, 4, 13, 6, 8,
					'add:', -1, 4, 13, 6, 9,
					'add:', -1, 4, 13, 6, 10,
					'init:', self
				)
			#end:case
			case 5:
				sfx._send('number:', 685, 'loop:', 1, 'play:', self)
			#end:case
			case 6:
				sfx._send('number:', 741, 'loop:', 1, 'play:', self)
			#end:case
			case 7:
				lookMirror._send('dispose:')
				sfx._send('number:', 686, 'loop:', 1, 'play:')
				tear._send('init:', 'setCycle:', End, self)
			#end:case
			case 8:
				cycles = 30
			#end:case
			case 9:
				theConv._send('add:', -1, 4, 13, 6, 11, 'init:', self)
			#end:case
			case 10:
				rightarm._send('setCycle:', Beg, self)
			#end:case
			case 11:
				theConv._send(
					'add:', -1, 4, 13, 6, 12,
					'add:', -1, 4, 13, 6, 13,
					'add:', -1, 4, 13, 6, 14,
					'init:', self
				)
			#end:case
			case 12:
				global102._send('number:', 688, 'loop:', -1, 'play:')
				leftarm._send('show:')
				rightarm._send('setLoop:', 1, 'posn:', 145, 144)
				seconds = 2
				global89._send('x:', local2, 'y:', local3, 'talkWidth:', local4)
			#end:case
			case 13:
				global0._send('put:', 24, 690)
				rgDead._send('stateOf690:', 0)
				global2._send('newRoom:', 680)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class alexHand(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cycles = 1
			#end:case
			case 1:
				rgDead._send('stateOf690:', 1)
				client._send('setScript:', deadTouch, 0, 0)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class eyeScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				seconds = 5
			#end:case
			case 1:
				client._send('cel:', 2)
				cycles = 2
			#end:case
			case 2:
				client._send('cel:', 0)
				self._send('init:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class deadHand(Actor):
	#property vars (may be empty)
	x = 110
	y = 121
	view = 691
	loop = 6
	priority = 12
	signal = 16
	
#end:class or instance

@SCI.instance
class deadFist(Actor):
	#property vars (may be empty)
	x = 224
	y = 107
	view = 692
	cycleSpeed = 1
	
#end:class or instance

@SCI.instance
class theConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class tear(Actor):
	#property vars (may be empty)
	x = 187
	y = 44
	view = 692
	loop = 1
	cycleSpeed = 10
	
#end:class or instance

@SCI.instance
class lookMirror(Actor):
	#property vars (may be empty)
	x = 177
	y = 44
	view = 692
	loop = 3
	
#end:class or instance

@SCI.instance
class introGhost(Actor):
	#property vars (may be empty)
	view = 690
	
	@classmethod
	def init():
		self._send('ignoreActors:', 1, 'ignoreHorizon:', 1, 'illegalBits:', 0)
		super._send('init:', &rest)
	#end:method

	@classmethod
	def cue():
		self._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class deadEyes(Prop):
	#property vars (may be empty)
	x = 179
	y = 43
	noun = 4
	view = 692
	loop = 4
	signal = 24576
	
	@classmethod
	def doVerb(param1 = None, *rest):
		lord._send('doVerb:', param1, &rest)
	#end:method

#end:class or instance

