#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 820
import sci_sh
import kernel
import Main
import rgCastle
import Print
import Conversation
import Scaler
import RandCycle
import PolyPath
import Polygon
import Feature
import LoadMany
import Window
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm820 = 0,
	noWayOut = 1,
	roomConv = 2,
	dungeonDoor = 3,
	flame = 4,
	wallReflection = 5,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.instance
class rm820(CastleRoom):
	#property vars (may be empty)
	noun = 3
	picture = 820
	style = 10
	horizon = 0
	vanishingX = 186
	vanishingY = 92
	minScaleSize = 89
	maxScaleSize = 113
	minScaleY = 130
	maxScaleY = 144
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		proc958_0(128, 825, 822)
		global2._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 3,
					'init:', 10, 166, 10, 174, 301, 174, 301, 161, 280, 147, 147, 147, 147, 132, 95, 132,
					'yourself:'
				)
		)
		kernel.ScriptID(1015, 6)._send('x:', 19, 'y:', 41)
		kernel.ScriptID(1015, 7)._send('x:', 19, 'y:', 77)
		global32._send('add:', bed, torch, gargoyle, 'eachElementDo:', #init)
		super._send('init:', &rest)
		flame._send('setCycle:', Fwd, 'init:')
		wallReflection._send('setCycle:', RandCycle, 'init:')
		dungeonDoor._send('cel:', 3, 'setPri:', 10, 'init:', 'stopUpd:')
		extraView._send('addToPic:')
		ant._send('init:', 'setScript:', antScript)
		global0._send(
			'init:',
			'reset:', 0,
			'posn:', 43, 143,
			'setPri:', 9,
			'setScale:', Scaler, maxScaleSize, minScaleSize, maxScaleY, minScaleY
		)
		global0._send('scaler:')._send('doit:')
		if kernel.ScriptID(80, 0)._send('tstFlag:', 709, 8192):
			if global5._send('contains:', kernel.ScriptID(80, 5)):
				kernel.ScriptID(81, 0)._send('resetGuard:', kernel.ScriptID(80, 5), 1)
				kernel.ScriptID(80, 5)._send('dispose:')
			#endif
			if global5._send('contains:', kernel.ScriptID(80, 6)):
				kernel.ScriptID(81, 0)._send('resetGuard:', kernel.ScriptID(80, 6), 2)
				kernel.ScriptID(80, 6)._send('dispose:')
			#endif
			kernel.ScriptID(81, 0)._send('clrFlag:', 709, 1, 2)
			self._send('setScript:', kernel.ScriptID(821, 0))
			global102._send('fadeTo:', 824, -1)
			local0 = 1
		else:
			self._send('setScript:', enterDungeon)
			if 
				(and
					proc999_5(kernel.ScriptID(80, 0)._send('dungeonEntered:'), 1, 2)
					(not kernel.ScriptID(80, 0)._send('tstFlag:', 709, -32768))
				)
				global102._send('fadeTo:', 820, -1)
				if (not global0._send('has:', 17)):
					dungeonDoor._send('approachX:', 111)
				#endif
				enterDungeon._send('next:', kernel.ScriptID(822, 0))
			else:
				global102._send('fadeTo:', 824, -1)
			#endif
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				(param1 == 2)
				proc999_5(kernel.ScriptID(80, 0)._send('dungeonEntered:'), 1, 2)
				(not kernel.ScriptID(80, 0)._send('tstFlag:', 709, -32768))
			)
			global91._send('say:', 3, 2, 20, 1)
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global0._send('setPri:', -1)
		super._send('dispose:', &rest)
		kernel.DisposeScript(991)
		kernel.DisposeScript(964)
	#end:method

#end:class or instance

@SCI.instance
class enterDungeon(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				cycles = 1
			#end:case
			case 1:
				global0._send(
					'setMotion:', MoveTo, dungeonDoor._send('approachX:'), dungeonDoor._send(
							'approachY:'
						), self
				)
			#end:case
			case 2:
				dungeonDoor._send('setCycle:', Beg, self)
			#end:case
			case 3:
				global105._send('number:', 822, 'loop:', 1, 'play:')
				dungeonDoor._send('setPri:', -1, 'stopUpd:')
				if 
					(or
						kernel.ScriptID(81, 0)._send('tstFlag:', 709, 1)
						kernel.ScriptID(81, 0)._send('tstFlag:', 709, 2)
					)
					global91._send('say:', 1, 0, 7, 1, self)
				else:
					cycles = 2
				#endif
				if global5._send('contains:', kernel.ScriptID(80, 5)):
					kernel.ScriptID(81, 0)._send('resetGuard:', kernel.ScriptID(80, 5), 1)
					kernel.ScriptID(80, 5)._send('dispose:')
				#endif
				if global5._send('contains:', kernel.ScriptID(80, 6)):
					kernel.ScriptID(81, 0)._send('resetGuard:', kernel.ScriptID(80, 6), 2)
					kernel.ScriptID(80, 6)._send('dispose:')
				#endif
				kernel.ScriptID(81, 0)._send('clrFlag:', 709, 1, 2)
			#end:case
			case 4:
				if (not next):
					global1._send('handsOn:')
				else:
					next = 0
					kernel.ScriptID(822, 1)._send('init:')
				#endif
				global0._send('reset:', 0)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class exitDungeon(Script):
	#property vars (may be empty)
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = global0._send('onControl:', 1)
		if ((state == 1) and (temp0 & 0x4000)):
			self._send('cue:')
		#endif
		super._send('doit:', &rest)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				dungeonDoor._send('hide:')
				global0._send(
					'normal:', 0,
					'setScale:', 0,
					'scaleX:', 128,
					'scaleY:', 128,
					'view:', 821,
					'loop:', 4,
					'cel:', 0,
					'posn:', 56, 109,
					'setCycle:', CT, 2, 1, self
				)
			#end:case
			case 1:
				global105._send('number:', 821, 'loop:', 1, 'play:')
				dungeonDoor._send('setPri:', 10, 'cel:', 3)
				global0._send('setCycle:', End, self)
			#end:case
			case 2:
				dungeonDoor._send('show:', 'stopUpd:')
				global105._send('stop:')
				global0._send(
					'posn:', dungeonDoor._send('approachX:'), dungeonDoor._send('approachY:'),
					'reset:', 1,
					'setPri:', 9,
					'setMotion:', MoveTo, 0, 143, self
				)
			#end:case
			case 3:
				global0._send('hide:')
				dungeonDoor._send('setCycle:', Beg, self)
			#end:case
			case 4:
				global105._send('number:', 822, 'loop:', 1, 'play:', self)
				global0._send('setPri:', -1)
			#end:case
			case 5:
				global2._send('newRoom:', 710)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class antScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				register = 0
				(state += (kernel.Random(0, 1) * 3))
				ant._send('hide:', 'setPri:', 15, 'ignoreActors:', 'setCycle:', Walk)
				seconds = kernel.Random(7, 25)
			#end:case
			case 1:
				ant._send('show:')
				if register = kernel.Random(0, 1):
					ant._send(
						'setLoop:', 6,
						'posn:', 220, 201, 0,
						'setMotion:', MoveTo, 172, 167, self
					)
				else:
					ant._send(
						'setLoop:', 5,
						'posn:', 106, 195, 0,
						'setMotion:', MoveTo, 155, 169, self
					)
				#endif
			#end:case
			case 2:
				seconds = kernel.Random(1, 10)
			#end:case
			case 3:
				state = -1
				ant._send('setPri:', 14)
				if register:
					ant._send(
						'setLoop:', 8,
						'posn:', 164, 195, 28,
						'setMotion:', MoveTo, 164, 213, self
					)
				else:
					ant._send(
						'setLoop:', 7,
						'posn:', 162, 195, 24,
						'setMotion:', MoveTo, 162, 209, self
					)
				#endif
			#end:case
			case 4:
				ant._send(
					'show:',
					'setLoop:', 5,
					'posn:', 0, 189, 0,
					'setMotion:', MoveTo, 44, 172, self
				)
			#end:case
			case 5:
				seconds = kernel.Random(2, 10)
			#end:case
			case 6:
				state = -1
				ant._send('loop:', 7, 'setMotion:', MoveTo, 88, 197, self)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class noWayOut(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				ant._send('setScript:', 0)
				global1._send('handsOff:')
				global102._send('fadeTo:', 823, 1)
				cycles = 2
			#end:case
			case 1:
				global0._send('setMotion:', PolyPath, 90, 144, self)
			#end:case
			case 2:
				global0._send(
					'view:', 821,
					'normal:', 0,
					'setPri:', 12,
					'setScale:', 0,
					'scaleX:', 128,
					'scaleY:', 128,
					'posn:', 93, 144,
					'loop:', 5,
					'cel:', 0,
					'cycleSpeed:', 8,
					'setCycle:', End, self
				)
			#end:case
			case 3:
				global105._send('number:', 825, 'setLoop:', -1, 'play:')
				global0._send('loop:', 6, 'cel:', 0, 'setCycle:', Fwd)
				seconds = 4
			#end:case
			case 4:
				global105._send('stop:')
				global0._send('setCycle:', 0)
				cycles = 3
			#end:case
			case 5:
				global91._send('say:', 1, 0, 2, 1, self)
			#end:case
			case 6:
				global91._send('say:', 1, 0, 2, 2, self)
			#end:case
			case 7:
				global5._send('eachElementDo:', #hide)
				global2._send('drawPic:', 98, 10)
				kernel.Message(1, @temp1)
				kernel.Display(@temp1, 100, 30, 11, 106, 260, 102, 16, 105, global22, 101, 1)
				kernel.Display(@temp1, 100, 29, 10, 106, 260, 102, 47, 105, global22, 101, 1)
				global0._send(
					'view:', 8901,
					'loop:', 0,
					'cel:', 0,
					'normal:', 0,
					'setScale:', 0,
					'scaleX:', 128,
					'scaleY:', 128,
					'posn:', 160, 43,
					'setMotion:', 0,
					'show:'
				)
				global102._send('number:', 970, 'loop:', 1, 'play:')
				cycles = 2
			#end:case
			case 8:
				global1._send('setCursor:', global20)
				while True: #repeat
					match
						(= temp0
							Print._send(
								'window:', DeathWindow,
								'addText:', r"""Please select:""", 60, 0,
								'posn:', 70, 130,
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
class doorLocked(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 90, 144, self)
			#end:case
			case 1:
				global0._send(
					'view:', 821,
					'normal:', 0,
					'setPri:', 12,
					'setScale:', 0,
					'scaleX:', 128,
					'scaleY:', 128,
					'posn:', 93, 144,
					'loop:', 5,
					'cel:', 0,
					'cycleSpeed:', 8,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				global0._send('loop:', 6, 'cel:', 0, 'setCycle:', Fwd)
				seconds = 4
			#end:case
			case 3:
				global0._send('setCycle:', 0)
				cycles = 3
			#end:case
			case 4:
				global91._send('say:', 5, 5, 15, 0, self)
			#end:case
			case 5:
				global0._send('loop:', 5, 'cel:', 2, 'cycleSpeed:', 8, 'setCycle:', Beg, self)
			#end:case
			case 6:
				global0._send('reset:', 1, 'posn:', 90, 144)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class unlockDoor(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				dungeonDoor._send('hide:')
				global0._send(
					'normal:', 0,
					'setScale:', 0,
					'view:', 823,
					'loop:', 0,
					'cel:', 0,
					'cycleSpeed:', 8,
					'posn:', 56, 109,
					'setCycle:', CT, 5, 1, self
				)
			#end:case
			case 1:
				cycles = 50
			#end:case
			case 2:
				global0._send('cel:', 6)
				global104._send('number:', 781, 'loop:', 1, 'play:', self)
			#end:case
			case 3:
				global91._send('say:', 5, 35, 15, 0, self)
			#end:case
			case 4:
				global0._send('loop:', 1, 'cel:', 0, 'setCycle:', End, self)
				global104._send('number:', 821, 'loop:', 1, 'play:')
			#end:case
			case 5:
				kernel.ScriptID(80, 0)._send('setFlag:', 709, 4096)
				global2._send('newRoom:', 710)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lookOutDoor(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 90, 144, self)
			#end:case
			case 1:
				global0._send(
					'view:', 821,
					'normal:', 0,
					'setPri:', 12,
					'setScale:', 0,
					'scaleX:', 128,
					'scaleY:', 128,
					'posn:', 93, 144,
					'loop:', 5,
					'cel:', 0,
					'cycleSpeed:', 8,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				global91._send('say:', 7, 1, 0, 0, self)
			#end:case
			case 3:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 4:
				global1._send('handsOn:')
				global0._send('reset:', 1, 'posn:', 90, 144)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class extraView(View):
	#property vars (may be empty)
	onMeCheck = 0
	view = 821
	loop = 3
	signal = 16400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match kernel.ScriptID(80, 0)._send('dungeonEntered:')
			case 3:
				self._send('cel:', 1, 'x:', 211, 'y:', 125, 'noun:', 8)
			#end:case
			else:
				self._send('cel:', 0, 'x:', 159, 'y:', 108, 'noun:', 9, 'onMeCheck:', 26505)
			#end:else
		#end:match
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class flame(Prop):
	#property vars (may be empty)
	x = 116
	y = 76
	noun = 11
	view = 821
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		torch._send('doVerb:', param1)
	#end:method

#end:class or instance

@SCI.instance
class wallReflection(Prop):
	#property vars (may be empty)
	x = 115
	y = 72
	onMeCheck = 0
	view = 821
	loop = 1
	signal = 16400
	cycleSpeed = 12
	
#end:class or instance

@SCI.instance
class dungeonDoor(Prop):
	#property vars (may be empty)
	x = 56
	y = 109
	noun = 5
	sightAngle = 45
	approachX = 91
	approachY = 145
	approachDist = 2
	view = 821
	loop = 2
	signal = 16384
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('approachVerbs:', 5, 35, 2)
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = param1._send('x:')
		temp1 = param1._send('y:')
		if 
			(and
				(global69._send('curIcon:') == global69._send('at:', 4))
				(global69._send('curInvIcon:') == global9._send('at:', 44))
			)
			approachX = 82
			approachY = 144
		else:
			approachX = 91
			approachY = 145
		#endif
		(temp0 -= nsLeft)
		(temp1 -= nsTop)
		if ((<= 5 temp0 15) and (<= 11 temp1 24)):
			noun = 7
		else:
			noun = 5
		#endif
		return super._send('onMe:', param1)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (noun == 5):
			match param1
				case 35:
					(cond
						case (not local0):
							global91._send('say:', noun, param1, 14)
						#end:case
						case kernel.ScriptID(80, 0)._send('tstFlag:', 709, 8192):
							kernel.ScriptID(80, 0)._send('setFlag:', 709, 4096)
							local0 = 0
							global2._send('setScript:', unlockDoor)
						#end:case
					)
				#end:case
				case 5:
					if (not local0):
						global2._send('setScript:', exitDungeon)
					else:
						global2._send('setScript:', doorLocked)
					#endif
				#end:case
				case 2:
					global91._send(
						'say:', noun, param1, (+
								14
								kernel.ScriptID(80, 0)._send('tstFlag:', 709, 8192)
							)
					)
				#end:case
				else:
					if (global66._send('doit:', param1) == -32768):
						global91._send(
							'say:', noun, 0, (+
									14
									kernel.ScriptID(80, 0)._send('tstFlag:', 709, 8192)
								)
						)
					else:
						super._send('doVerb:', param1)
					#endif
				#end:else
			#end:match
		else:
			match param1
				case 2:
					if local0:
						global91._send('say:', noun, param1, 15)
					else:
						global91._send('say:', noun, param1, 14)
					#endif
				#end:case
				case 1:
					global2._send('setScript:', lookOutDoor)
				#end:case
				else:
					noun = 5
					self._send('doVerb:', param1)
				#end:else
			#end:match
		#endif
	#end:method

#end:class or instance

@SCI.instance
class ant(Actor):
	#property vars (may be empty)
	x = 149
	y = 185
	noun = 13
	view = 820
	loop = 8
	
#end:class or instance

@SCI.instance
class bed(Feature):
	#property vars (may be empty)
	noun = 8
	onMeCheck = 2
	
#end:class or instance

@SCI.instance
class torch(Feature):
	#property vars (may be empty)
	noun = 11
	onMeCheck = 4
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global91._send('say:', noun, param1, (14 + local0))
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class gargoyle(Feature):
	#property vars (may be empty)
	x = 56
	y = 144
	noun = 12
	onMeCheck = 8
	
#end:class or instance

@SCI.instance
class roomConv(Conversation):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('dispose:', &rest)
		caller = 0
	#end:method

#end:class or instance

@SCI.instance
class DeathWindow(SysWindow):
	#property vars (may be empty)
	@classmethod
	def open():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		color = 47
		back = 0
		super._send('open:', &rest)
	#end:method

#end:class or instance

