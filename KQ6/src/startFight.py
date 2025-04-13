#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 755
import sci_sh
import kernel
import Main
import rm750
import ArrayScript
import LoadMany
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	startFight = 0,
	noDagger = 1,
	cassimaHasDagger = 2,
	fightPart1 = 3,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = [7504, 4, 0, 158, 136, -4095, 3, 1, -3968, 750, 1, 0, -4064, 2, -4095, 8, 1, -3968, 750, 1, 0, -4064, 2, -4094, -1]
local25 = [751, 4, 0, 136, 144, -4095, 2, 1, -3968, 750, 1, 0, -4064, 1, -4094, 751, 7, 0, 138, 137, -3968, 750, 1, 0, -4064, 1, -4095, 5, 1, -3968, 750, 1, 0, -4064, 1, -4094, -3840, -1, 6, 23, 15, 3, -3840, -1, 6, 23, 15, 4, -3840, -1, 6, 23, 15, 5, 7511, 0, 0, 101, 156, -4095, 3, 1, -16, 128, 751, -3968, 750, 1, 0, -4064, 1, -4094, 7511, 2, 0, 106, 147, -4095, 1, 1, -3968, 750, 1, 0, -4064, 1, -4094, 7511, 1, 0, 93, 151, -4095, 3, 1, -3968, 756, 1, 0, -4094, 7512, 2, 0, 100, 165, -4094, 7512, 0, 0, 131, 171, -4095, 1, 1, -3968, 756, 1, 0, -4094, 7515, 3, 0, 149, 162, -4095, 2, 1, -3968, 750, 1, 0, -4064, 1, -4095, 6, 1, -3968, 750, 1, 0, -4064, 1, -4094, 7515, 0, 0, 157, 170, -4095, 1, 1, -3968, 750, 1, 0, -4064, 1, -4094, 7515, 1, 0, 152, 171, -4095, 3, 1, -3968, 750, 1, 0, -4064, 1, -4095, 5, 1, -3968, 755, 1, 0, -4094, 7515, 2, 0, 152, 174, -4095, 3, 1, -3968, 755, 1, 0, -4095, 8, 1, -3968, 755, 1, 0, -4094, 7516, 0, 0, 143, 158, -4095, 2, 1, -3968, 756, 1, 0, -4094, 7516, 4, 0, 174, 151, -4094, 7516, 1, 0, 179, 152, -4095, 3, 1, -3968, 750, 1, 0, -4064, 1, -4094, 7517, 1, 0, 171, 131, -4095, 2, 1, -3968, 750, 1, 0, -4064, 1, -4094, 7517, 0, 0, 170, 139, -4095, 3, 1, -3968, 750, 1, 0, -4064, 1, -4094, 7511, 0, 0, 170, 158, -4095, 3, 1, -3968, 750, 1, 0, -4064, 1, -4094, 7511, 1, 0, 162, 143, -4095, 3, 1, -3968, 756, 1, 0, -4094, 7512, 0, 0, 169, 156, -4095, 1, 1, -3968, 756, 1, 0, -4094, 7515, 0, 0, 167, 156, -4095, 1, 1, -3968, 750, 1, 0, -4064, 1, -4094, 7515, 1, 0, 161, 158, -4095, 3, 1, -3968, 750, 1, 0, -4064, 1, -4095, 5, 1, -3968, 755, 1, 0, -4094, 7515, 2, 0, 159, 159, -4095, 3, 1, -3968, 755, 1, 0, -4095, 8, 1, -3968, 755, 1, 0, -4094, 7516, 0, 0, 150, 143, -4095, 2, 1, -3968, 756, 1, 0, -4094, 7516, 1, 0, 157, 145, -4095, 3, 1, -3968, 750, 1, 0, -4064, 1, -4094, 7517, 0, 0, 156, 144, -4095, 3, 1, -3968, 750, 1, 0, -4064, 1, -4094, 7511, 0, 0, 158, 163, -4095, 3, 1, -3968, 750, 1, 0, -4064, 1, -4094, -3840, -1, 6, 23, 15, 6, 7511, 1, 0, 152, 148, -4095, 3, 1, -3968, 756, 1, 0, -4094, 7512, 0, 0, 159, 162, -4095, 1, 1, -3968, 756, 1, 0, -4094, -3840, -1, 6, 23, 15, 7, -1, -3840, -1, 6, 23, 16, 1, 7512, 1, 0, 135, 171, -4095, 3, 1, -3968, 750, 1, 0, -4064, 1, -4094, -3840, -1, 6, 23, 16, 2, -3840, -1, 6, 23, 16, 3, 7513, 0, 0, 134, 161, -4094, 7513, 1, 0, 134, 161, -4094, -1]
local530 = [7514, 0, 0, 153, 150, -4095, 2, 1, -3968, 751, 1, 0, -4094, -1, -4092, -3840, -1, 1, 0, 6, 1, -3840, -1, 1, 0, 6, 2, 7513, 0, 7, 159, 151, -4094, -3840, -1, 1, 0, 6, 3, 7513, 1, 11, 159, 151, -4094, -3840, -1, 1, 0, 6, 4, -1]


@SCI.instance
class startFight(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if (not register):
					global0._send(
						'view:', 751,
						'loop:', 6,
						'cel:', 0,
						'posn:', 178, 132,
						'setCycle:', End, self
					)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 1:
				kernel.ScriptID(750, 1)._send(
					'add:', -1, 6, 23, 15, 1,
					'add:', -1, 6, 23, 15, 2,
					'init:', self
				)
			#end:case
			case 2:
				kernel.ScriptID(750, 3)._send('dispose:')
				if register:
					global69._send('disable:', 6)
					global2._send(
						'setScript:', lampStartScr._send('next:', fightPart1, 'yourself:')
					)
				else:
					next = fightPart1
					self._send('dispose:')
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class cassimaHasDagger(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		global73._send('add:', self)
		global72._send('add:', self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global73._send('delete:', self)
		global72._send('delete:', self)
		super._send('dispose:')
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((state == 11) and global80._send('canInput:') and global0._send('onMe:', param1)):
			param1._send('claimed:', 1)
			global1._send('handsOff:')
			self._send('state:', 25, 'seconds:', 0, 'cycles:', 2)
		#endif
		param1._send('claimed:')
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				kernel.ScriptID(750, 6)._send(
					'view:', 753,
					'setLoop:', 2,
					'setCycle:', Walk,
					'posn:', 28, 160,
					'setStep:', 5, 2,
					'setMotion:', MoveTo, 131, 160, self
				)
			#end:case
			case 1:
				if global2._send('script:'):
					state.post('--')
				#endif
				cycles = 2
			#end:case
			case 2:
				global0._send(
					'view:', 753,
					'loop:', 0,
					'cel:', 0,
					'posn:', 159, 149,
					'setCycle:', CT, 2, 1, self
				)
			#end:case
			case 3:
				global91._send('say:', 6, 23, 15, 8, self)
			#end:case
			case 4:
				kernel.ScriptID(750, 6)._send(
					'view:', 753,
					'loop:', 1,
					'cel:', 0,
					'posn:', 140, 153,
					'setCycle:', CT, 3, 1, self
				)
			#end:case
			case 5:
				global103._send('number:', 754, 'setLoop:', 1, 'play:')
				global0._send('cel:', 3)
				ticks = 3
			#end:case
			case 6:
				kernel.ScriptID(750, 1)._send(
					'add:', -1, 6, 23, 15, 9,
					'add:', -1, 6, 23, 15, 10,
					'init:', self
				)
			#end:case
			case 7:
				global0._send('setCycle:', End, self)
				kernel.ScriptID(750, 6)._send('setCycle:', End, kernel.ScriptID(750, 6))
			#end:case
			case 8:
				global91._send('say:', 6, 23, 15, 11, self)
			#end:case
			case 9:#end:case
			case 10:
				cycles = 4
			#end:case
			case 11:
				proc750_5()
				if ((not global87) or (not kernel.HaveMouse())):
					seconds = 15
				else:
					seconds = 8
				#endif
			#end:case
			case 12:
				proc750_5(1)
				cycles = 1
			#end:case
			case 13:
				global1._send('handsOff:')
				global0._send('setCycle:', Beg, self)
			#end:case
			case 14:
				global91._send('say:', 1, 0, 6, 1, self)
			#end:case
			case 15:
				global91._send('say:', 1, 0, 6, 2, self)
			#end:case
			case 16:
				global2._send('setScript:', noDagger, 0, 1)
				self._send('dispose:')
			#end:case
			case 26:
				proc750_5(1)
				global1._send('givePoints:', 5)
				cycles = 1
			#end:case
			case 27:
				global1._send('handsOff:')
				global0._send(
					'view:', 7514,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', 153, 150,
					'setCycle:', CT, 2, 1, self
				)
			#end:case
			case 28:
				global102._send('number:', 0, 'stop:')
				global103._send('number:', 0, 'stop:')
				global103._send('number:', 751, 'setLoop:', 1, 'play:')
				cycles = 3
			#end:case
			case 29:
				global102._send('number:', 752, 'setLoop:', -1, 'play:')
				global0._send('setCycle:', End, self)
			#end:case
			case 30:
				global0._send('setLoop:', 1, 'cel:', 0, 'setCycle:', CT, 7, 1, self)
			#end:case
			case 31:
				global0._send('setCycle:', End, self)
			#end:case
			case 32:
				kernel.ScriptID(750, 3)._send(
					'init:',
					'view:', 7514,
					'setLoop:', 2,
					'posn:', 153, 150,
					'ignoreActors:', 1,
					'addToPic:'
				)
				kernel.ScriptID(750, 2)._send('dispose:')
				global0._send(
					'oldScaleSignal:', 0,
					'view:', 900,
					'loop:', 9,
					'cel:', 2,
					'setLoop:', -1,
					'setPri:', -1,
					'scaleSignal:', 1,
					'scaleX:', 96,
					'scaleY:', 96,
					'posn:', 164, 146,
					'cycleSpeed:', 6,
					'moveSpeed:', 6,
					'ignoreActors:', 1,
					'normal:', 1,
					'setCycle:', 0
				)
				cycles = 2
			#end:case
			case 33:
				global0._send(
					'setLoop:', -1,
					'setCycle:', Walk,
					'setMotion:', MoveTo, 120, 143, self
				)
			#end:case
			case 34:
				global0._send(
					'setLoop:', 5,
					'setMotion:', MoveTo, kernel.ScriptID(750, 6)._send('x:'), (-
							kernel.ScriptID(750, 6)._send('y:')
							2
						), self
				)
			#end:case
			case 35:
				global0._send('setLoop:', 9, 'cel:', 2)
				ticks = 30
			#end:case
			case 36:
				global0._send(
					'view:', 758,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', kernel.ScriptID(750, 6)._send('x:'), kernel.ScriptID(750, 6)._send('y:'),
					'normal:', 0
				)
				kernel.ScriptID(750, 6)._send('hide:')
				ticks = 30
			#end:case
			case 37:
				kernel.ScriptID(750, 1)._send(
					'add:', -1, 6, 23, 10, 4,
					'add:', -1, 6, 23, 10, 5,
					'add:', -1, 6, 23, 10, 6,
					'add:', -1, 6, 23, 10, 7,
					'init:', self
				)
			#end:case
			case 38:
				global0._send('setCycle:', End, self)
			#end:case
			case 39:
				kernel.ScriptID(750, 1)._send(
					'add:', -1, 6, 23, 10, 8,
					'add:', -1, 6, 23, 10, 9,
					'add:', -1, 6, 23, 10, 10,
					'add:', -1, 6, 23, 10, 11,
					'init:', self
				)
			#end:case
			case 40:
				global0._send('setMotion:', 0, 'setCycle:', 0)
				global69._send('enable:', 6)
				global2._send('newRoom:', 180)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class startEndingCartoon(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global69._send('enable:', 6)
				cycles = 2
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				global2._send('newRoom:', 740)
			#end:case
		#end:match
	#end:method

#end:class or instance

class SwordArrayScript(ArrayScript):
	#property vars (may be empty)
	@classmethod
	def play(param1 = None, param2 = None, param3 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global104._send('number:', 0, 'stop:')
		global104._send('number:', param1, 'setLoop:', param2, 'play:')
		if param3:
			global104._send('client:', param3)
		else:
			cycles = 1
		#endif
	#end:method

#end:class or instance

@SCI.instance
class lampStartScr(SwordArrayScript):
	#property vars (may be empty)
	@classmethod
	def at(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return local0[param1]
	#end:method

#end:class or instance

@SCI.instance
class fightPart1(SwordArrayScript):
	#property vars (may be empty)
	@classmethod
	def at(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		proc958_0(0, 751, 7511, 7512, 7515, 7516, 7517)
		return local25[param1]
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global69._send('enable:', 6)
		super._send('dispose:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class knockOutVizier(SwordArrayScript):
	#property vars (may be empty)
	@classmethod
	def at(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return local530[param1]
	#end:method

#end:class or instance

@SCI.instance
class noDagger(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				proc750_5(1)
				global102._send('number:', 0, 'stop:')
				global102._send('number:', 705, 'setLoop:', 1, 'play:')
				cycles = 1
			#end:case
			case 1:
				global1._send('handsOff:')
				if (not register):
					global91._send('say:', 6, 23, 16, 1, self)
				else:
					cycles = 2
				#endif
			#end:case
			case 1:
				global0._send('view:', 755, 'posn:', 151, 154, 'setLoop:', 0, 'cel:', 6)
				cycles = 8
			#end:case
			case 2:
				global0._send('cel:', 5)
				cycles = 8
			#end:case
			case 3:
				global0._send(
					'posn:', 165, 163,
					'view:', 7504,
					'setLoop:', 6,
					'cel:', 0,
					'setCycle:', CT, 2, 1, self
				)
			#end:case
			case 4:
				global103._send('number:', 0, 'stop:')
				global103._send('number:', 756, 'setLoop:', 1, 'play:')
				global0._send('setCycle:', End, self)
			#end:case
			case 5:
				global103._send('number:', 0, 'stop:')
				global103._send('number:', 971, 'setLoop:', 1, 'play:', self)
			#end:case
			case 6:
				if (not register):
					kernel.ScriptID(750, 1)._send(
						'add:', -1, 6, 23, 16, 2,
						'add:', -1, 6, 23, 16, 3,
						'init:', self
					)
				else:
					cycles = 2
				#endif
			#end:case
			case 7:
				if register:
					global91._send('say:', 1, 0, 6, 3, self)
				else:
					cycles = 2
				#endif
			#end:case
			case 8:
				global0._send(
					'view:', 7513,
					'posn:', 161, 150,
					'setLoop:', 0,
					'cel:', 0,
					'setCycle:', End, self
				)
				global103._send('number:', 0, 'stop:')
				global103._send('number:', 652, 'setLoop:', 1, 'play:')
			#end:case
			case 9:
				global0._send('setLoop:', 1, 'cel:', 0, 'setCycle:', CT, 6, 1, self)
			#end:case
			case 10:
				global103._send('number:', 0, 'stop:')
				global103._send('number:', 652, 'setLoop:', 1, 'play:')
				global0._send('setCycle:', End, self)
			#end:case
			case 11:
				if register:
					global91._send('say:', 1, 0, 6, 4, self)
				else:
					cycles = 2
				#endif
			#end:case
			case 12:
				if (global9._send('at:', 8)._send('owner:') == 870):
					proc0_1(41)
				else:
					proc0_1(40)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

