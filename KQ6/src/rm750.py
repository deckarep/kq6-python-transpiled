#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 750
import sci_sh
import kernel
import Main
import rgCastle
import Kq6IconBar
import Print
import Conversation
import Scaler
import Polygon
import Feature
import LoadMany
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm750 = 0,
	roomConv = 1,
	vizHead = 2,
	vizier = 3,
	genie = 4,
	proc750_5 = 5,
	cassima = 6,
	vizierTimer = 7,
	tiedUpRightNow = 8,
	sword = 9,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = [1, 275, 161, 2, 273, 161, 3, 270, 161, 4, 268, 160, 5, 267, 159, 5, 264, 156, 6, 262, 157, 7, 260, 157, 8, 256, 158, 9, 254, 158, -1]
local31 = [7, 3, 0, 0, 6, 2, 4, 1, 6, 3, 4, 1, 6, 4, 4, 1, 6, 5, 4, 1, 6, 6, 4, 1, 6, 7, 4, 1, 7, 4, 1, 0, 7, 0, 1, 0, 7, 1, 1, 0, 7, 2, 2, -1, -32768]
local76 = None
local77 = None
local78 = None
local79 = None
local80 = None
local81 = None
local82 = 1
local83 = None
local84 = None


@SCI.procedure
def proc750_5(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	if (argc and param1 and local81):
		global69._send(
			'delete:', global69._send('at:', 0),
			'addToFront:', local81,
			'curIcon:', local81,
			'walkIconItem:', local81
		)
		local81 = 0
		global1._send('oldCurIcon:', global69._send('at:', 0))
	#endif
	global1._send('handsOn:')
	if global69._send('contains:', swordIcon):
		global69._send('disable:', 4, 5)
	else:
		global69._send('disable:', 0)
	#endif
#end:procedure

@SCI.instance
class rm750(CastleRoom):
	#property vars (may be empty)
	noun = 2
	picture = 750
	style = 10
	vanishingY = -10000
	autoLoad = 0
	minScaleSize = 73
	maxScaleSize = 102
	minScaleY = 139
	maxScaleY = 189
	
	@classmethod
	def init():
		if (global100 and (global12 == 99) and kernel.FileIO(10, r"""g""")):
			global102._send('number:', 742, 'setLoop:', -1, 'play:')
			global0._send('get:', 31)
		#endif
		temp1 = global19
		global1._send('setCursor:', 999, 1)
		if 
			(and
				global100
				(global12 == 99)
				kernel.FileIO(10, r"""g""")
				Print._send(
					'addText:', r"""Does Jollo have lamp?""",
					'addButton:', 0, r"""No""", 0, 12,
					'addButton:', 1, r"""Yes""", 0, 26,
					'init:'
				)
			)
			global9._send('at:', 25)._send('owner:', 750)
		#endif
		if 
			(and
				global100
				(global12 == 99)
				kernel.FileIO(10, r"""g""")
				Print._send(
					'addText:', r"""Does Cassima have dagger?""",
					'addButton:', 0, r"""No""", 0, 12,
					'addButton:', 1, r"""Yes""", 0, 26,
					'init:'
				)
			)
			global9._send('at:', 8)._send('owner:', 870)
		#endif
		global1._send('setCursor:', temp1, 1)
		if (global9._send('at:', 25)._send('owner:') == 750):
			kernel.Load(130, 751)
			proc958_0(128, 717, 754)
		#endif
		self._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 319, -10, 319, 161, 266, 157, 240, 139, 251, 139, 269, 152, 278, 153, 259, 134, 219, 130, 109, 130, 48, 139, 23, 145, 0, 154, 0, -10,
					'yourself:'
				)
		)
		super._send('init:', &rest)
		global32._send('add:', door, theWindows, stairs, 'eachElementDo:', #init)
		global0._send('init:', 'actions:', egoDoVerb)
		sword._send('addToPic:')
		vizier._send('addToPic:')
		cassima._send('init:', 'setScript:', tiedUpRightNow)
		self._send('setScript:', enterRoom)
		kernel.UnLoad(129, 750)
	#end:method

	@classmethod
	def doit():
		temp0 = global0._send('onControl:', 1)
		(cond
			case script: 0#end:case
			case (temp0 & 0x4000):
				global2._send('newRoom:', 790)
			#end:case
		)
		super._send('doit:', &rest)
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(751)
		kernel.DisposeScript(752)
		kernel.DisposeScript(753)
		kernel.DisposeScript(754)
		kernel.DisposeScript(755)
		kernel.DisposeScript(759)
	#end:method

#end:class or instance

@SCI.instance
class enterRoom(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send(
					'view:', 751,
					'normal:', 0,
					'setScale:', 0,
					'scaleX:', 128,
					'scaleY:', 128,
					'setLoop:', 1,
					'setPri:', 2,
					'cel:', 1,
					'posn:', 275, 161,
					'ignoreHorizon:',
					'ignoreActors:', 1
				)
				cycles = 2
			#end:case
			case 1:
				if (local0[(local80 + 3)] != -1):
					state.post('--')
					global0._send(
						'cel:', local0[local80],
						'x:', local0[(local80 + 1)],
						'y:', local0[(local80 + 2)]
					)
					(local80 += 3)
					cycles = 8
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				global0._send(
					'oldScaleSignal:', 0,
					'view:', 900,
					'loop:', 9,
					'cel:', 7,
					'setLoop:', -1,
					'setPri:', -1,
					'posn:', 241, 134,
					'setScale:', Scaler, 102, 76, 189, 139,
					'setSpeed:', 6,
					'setCycle:', 0
				)
				cycles = 2
				kernel.UnLoad(128, 751)
			#end:case
			case 3:
				global0._send(
					'setLoop:', -1,
					'setCycle:', Walk,
					'setMotion:', MoveTo, 201, 134, self
				)
			#end:case
			case 4:
				if global0._send('looper:'):
					global0._send('looper:')._send('dispose:')
				#endif
				global0._send('normal:', 0, 'view:', 7500, 'setLoop:', 3, 'setCycle:', 0, 'looper:', 0)
				cycles = 2
			#end:case
			case 5:
				self._send('setScript:', startScr, self)
			#end:case
			case 6:
				kernel.DisposeScript(1005)
				vizier._send('stopUpd:')
				if (global9._send('at:', 25)._send('owner:') == global11):
					genie._send('setScript:', 0, 'view:', 703, 'setLoop:', 1, 'cel:', 0)
					self._send('setScript:', kernel.ScriptID(751, 0), self)
				else:
					genie._send('setScript:', continuedWindup)
					cycles = 2
				#endif
			#end:case
			case 7:
				if (not genie._send('script:')):
					genie._send('view:', 702, 'setScript:', continuedWindup)
				#endif
				proc750_5()
				if ((not global87) or (not kernel.HaveMouse())):
					seconds = 15
				else:
					seconds = 8
				#endif
			#end:case
			case 8:
				global1._send('handsOff:')
				continuedWindup._send('caller:', self)
				local79 = 1
			#end:case
			case 9:
				cassima._send('setScript:', 0, 'stopUpd:')
				global91._send('say:', 1, 0, 4, 1, self)
			#end:case
			case 10:
				global106 = global0
				if (global103._send('number:') != 707):
					global103._send('number:', 707, 'setLoop:', -1, 'play:')
				#endif
				self._send('setScript:', kernel.ScriptID(752, 0), self, genie)
			#end:case
			case 11:
				global91._send('say:', 1, 0, 4, 2, self, 'oneOnly:', 0)
			#end:case
			case 12:
				proc0_1(18)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class continuedWindup(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		local76 = genie._send('x:')
		local77 = genie._send('y:')
		super._send('init:', &rest)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if (local31[local78] == -32768):
					local78 = 0
				#endif
				genie._send(
					'loop:', local31[local78],
					'cel:', local31[(local78 + 1)],
					'x:', (local31[(local78 + 2)] + local76),
					'y:', (local31[(local78 + 3)] + local77)
				)
				state.post('--')
				if (local79 and (genie._send('loop:') == 6)):
					state.post('++')
				#endif
				(local78 += 4)
				cycles = 8
			#end:case
			case 1:
				local79 = 0
				genie._send('setCycle:', Beg, self)
			#end:case
			case 2:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class startScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cycles = 2
			#end:case
			case 1:
				roomConv._send('add:', -1, 1, 0, 1, 1, 'init:', self)
			#end:case
			case 2:
				vizHead._send('cel:', 1, 'forceUpd:')
				cycles = 4
			#end:case
			case 3:
				roomConv._send('add:', -1, 1, 0, 1, 2, 'init:', self)
			#end:case
			case 4:
				vizHead._send('cel:', 2, 'forceUpd:')
				ticks = 60
			#end:case
			case 5:
				self._send('setScript:', kernel.ScriptID(752, 1), self, genie)
			#end:case
			case 6:
				vizHead._send('cel:', 1, 'forceUpd:')
				cycles = 4
			#end:case
			case 7:
				roomConv._send(
					'add:', -1, 1, 0, 1, 3,
					'add:', -1, 1, 0, 1, 4,
					'add:', -1, 1, 0, 1, 5,
					'add:', -1, 1, 0, 1, 6,
					'init:', self
				)
			#end:case
			case 8:
				vizHead._send('cel:', 2, 'forceUpd:')
				cycles = 4
			#end:case
			case 9:
				global91._send('say:', 1, 0, 1, 7, self)
			#end:case
			case 10:
				genie._send(
					'view:', 702,
					'loop:', 6,
					'cel:', 0,
					'cycleSpeed:', 7,
					'setCycle:', CT, 4, 1, self
				)
			#end:case
			case 11:
				genie._send('setCycle:', Beg, self)
			#end:case
			case 12:
				roomConv._send('add:', -1, 1, 0, 1, 8, 'init:', self)
			#end:case
			case 13:
				kernel.DisposeScript(1005)
				kernel.DisposeScript(1029)
				kernel.DisposeScript(1012)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getSword(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global69._send('disable:', 6)
				global0._send(
					'oldScaleSignal:', 0,
					'view:', 900,
					'loop:', 9,
					'cel:', 2,
					'setPri:', -1,
					'setLoop:', -1,
					'scaleSignal:', 1,
					'scaleX:', 96,
					'scaleY:', 96,
					'cycleSpeed:', 6,
					'moveSpeed:', 6,
					'ignoreActors:', 1,
					'normal:', 0,
					'setCycle:', 0
				)
				cycles = 2
			#end:case
			case 1:
				global1._send('givePoints:', 1)
				global0._send(
					'setLoop:', -1,
					'setCycle:', Walk,
					'setMotion:', MoveTo, 229, 137, self
				)
			#end:case
			case 2:
				ticks = 30
			#end:case
			case 3:
				if global0._send('looper:'):
					global0._send('looper:')._send('dispose:')
				#endif
				global0._send('normal:', 0, 'view:', 7500, 'setLoop:', 3, 'setCycle:', 0, 'looper:', 0)
				cycles = 2
			#end:case
			case 4:
				global91._send('say:', 4, 5, 8, 1, self)
			#end:case
			case 5:
				global0._send(
					'normal:', 0,
					'posn:', 234, 142,
					'view:', 751,
					'setLoop:', 0,
					'cel:', 0,
					'cycleSpeed:', 8,
					'setScale:', 0,
					'setPri:', 2,
					'scaleX:', 128,
					'scaleY:', 128,
					'setCycle:', CT, 2, 1, self
				)
			#end:case
			case 6:
				sword._send('dispose:')
				if global169:
					global2._send('drawPic:', 750, 15)
				else:
					global2._send('drawPic:', 750, 100)
				#endif
				global0._send('setCycle:', End, self)
			#end:case
			case 7:
				global0._send(
					'posn:', 205, 149,
					'setLoop:', 2,
					'cel:', 0,
					'cycleSpeed:', 6,
					'setCycle:', End, self
				)
			#end:case
			case 8:
				global103._send('number:', 750, 'setLoop:', 1, 'play:')
				global0._send(
					'posn:', 195, 152,
					'setLoop:', 3,
					'cel:', 0,
					'cycleSpeed:', 10,
					'setCycle:', End, self
				)
			#end:case
			case 9:
				global91._send('say:', 4, 5, 8, 2, self, 'oneOnly:', 0)
			#end:case
			case 10:
				global69._send('enable:', 6)
				local81 = global69._send('at:', 0)
				global69._send(
					'delete:', global69._send('at:', 0),
					'addToFront:', swordIcon._send('init:', 'cursor:', swordCursor, 'yourself:'),
					'curIcon:', swordIcon,
					'walkIconItem:', swordIcon
				)
				global1._send('oldCurIcon:', swordIcon)
				kernel.DisposeScript(1005)
				kernel.DisposeScript(1029)
				kernel.DisposeScript(1012)
				kernel.DisposeScript(1020)
				kernel.DisposeScript(1001)
				proc750_5()
				if ((not global87) or (not kernel.HaveMouse())):
					seconds = 15
				else:
					seconds = 8
				#endif
			#end:case
			case 11:
				proc750_5(1)
				cycles = 1
			#end:case
			case 12:
				global1._send('handsOff:')
				if (global9._send('at:', 25)._send('owner:') == 740):
					cycles = 2
				else:
					vizier._send(
						'view:', 7504,
						'posn:', 120, 138,
						'setLoop:', 5,
						'setStep:', 6, 6,
						'setCycle:', Walk,
						'setMotion:', MoveTo, 189, 145, self
					)
				#endif
			#end:case
			case 13:
				global0._send('hide:')
				vizier._send(
					'view:', 7504,
					'posn:', 203, 151,
					'setLoop:', 6,
					'cel:', 0,
					'setCycle:', CT, 2, 1, self
				)
				global102._send('number:', 705, 'setLoop:', 1, 'play:')
			#end:case
			case 14:
				global103._send('number:', 0, 'stop:')
				global103._send('number:', 756, 'setLoop:', 1, 'play:', self)
				vizier._send('setCycle:', End, self)
			#end:case
			case 15:#end:case
			case 16:
				global103._send('number:', 0, 'stop:')
				global103._send('number:', 971, 'setLoop:', 1, 'play:', self)
			#end:case
			case 17:
				global103._send('number:', 0, 'stop:')
				global103._send('number:', 652, 'setLoop:', 1, 'play:')
				vizier._send(
					'view:', 7513,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', 198, 139,
					'setCycle:', End, self
				)
			#end:case
			case 18:
				global91._send('say:', 6, 23, 16, 3, self)
			#end:case
			case 19:
				vizier._send('setLoop:', 1, 'cel:', 0, 'setCycle:', CT, 5, 1, self)
			#end:case
			case 20:
				global103._send('number:', 652, 'setLoop:', 1, 'play:')
				vizier._send('setCycle:', End, self)
			#end:case
			case 21:
				proc0_1(41)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class tiedUpRightNow(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cassima._send('cycleSpeed:', 12)
				cycles = 1
			#end:case
			case 1:
				while (register == cassima._send('cel:')):

					register = kernel.Random(0, 7)
				#end:loop
				if (register < cassima._send('cel:')):
					cassima._send('setCycle:', CT, register, -1, self)
				else:
					cassima._send('setCycle:', CT, register, 1, self)
				#endif
			#end:case
			case 2:
				if (kernel.ScriptID(755, 3)._send('state:') < 340):
					(state -= 2)
				#endif
				cycles = kernel.Random(10, 40)
			#end:case
			case 3:
				if (global9._send('at:', 8)._send('owner:') == 870):
					next = untieSelfAndStand
					self._send('dispose:')
				else:
					kernel.ScriptID(755, 3)._send('next:', kernel.ScriptID(755, 1))
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class untieSelfAndStand(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				register = 1
				cycles = 2
			#end:case
			case 1:
				cassima._send(
					'view:', 782,
					'loop:', register,
					'cel:', 0,
					'cycleSpeed:', 8,
					'setCycle:', End, self
				)
				if (register < 4):
					state.post('--')
					register.post('++')
				#endif
			#end:case
			case 2:
				next = kernel.ScriptID(755, 2)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class sword(View):
	#property vars (may be empty)
	x = 210
	y = 111
	noun = 4
	sightAngle = 180
	view = 7500
	
	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('ignoreActors:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				if global5._send('contains:', genie):
					global91._send('say:', noun, param1, 7)
				else:
					global2._send('setScript:', getSword)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class vizier(Actor):
	#property vars (may be empty)
	x = 110
	y = 136
	noun = 6
	view = 7500
	loop = 1
	signal = 16384
	
	@classmethod
	def addToPic():
		super._send('addToPic:', &rest)
		vizHead._send('init:', 'posn:', (x - 2), y, 31)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		(cond
			case (script and (script == vizierTimer) and proc999_5(param1, 23, 1)):
				match param1
					case 23: 0#end:case
					case 1: 0#end:case
				#end:match
			#end:case
			case proc999_5(param1, 28, 8, 5, 14, 16, 10):
				temp0 = (7 if global5._send('contains:', genie) else 8)
				global91._send('say:', noun, param1, temp0)
			#end:case
			case (param1 == 1):
				if global5._send('contains:', genie):
					global91._send('say:', 6, 1, 7)
				else:
					global91._send('say:', 6, 1, 9)
				#endif
			#end:case
			case (param1 == 23):
				global1._send('handsOff:')
				global1._send('givePoints:', 1)
				global2._send('setScript:', kernel.ScriptID(755, 0))
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class vizierTimer(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		super._send('init:', &rest)
		if ((not script) and (not register)):
			if ((not global87) or (not kernel.HaveMouse())):
				register = 12
			else:
				register = 6
			#endif
		#endif
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if (not script):
					seconds = register
				#endif
			#end:case
			case 1:
				global1._send('handsOff:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class vizHead(View):
	#property vars (may be empty)
	view = 7500
	loop = 1
	cel = 2
	signal = 24576
	
#end:class or instance

@SCI.instance
class genie(Actor):
	#property vars (may be empty)
	x = 91
	y = 147
	noun = 5
	view = 702
	loop = 8
	cel = 6
	scaleSignal = 1
	scaleX = 112
	scaleY = 112
	
	@classmethod
	def init():
		super._send('init:', &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 63:
				global0._send('put:', 23)
				global1._send('handsOff:')
				script._send('caller:', kernel.ScriptID(753, 0))
				local79 = 1
				kernel.ScriptID(753, 0)._send('start:', -1)
				global2._send('setScript:', kernel.ScriptID(753, 0))
			#end:case
			case 67:
				global0._send('put:', 31)
				global1._send('handsOff:')
				script._send('caller:', kernel.ScriptID(753, 0))
				local79 = 1
				kernel.ScriptID(753, 0)._send('start:', -1)
				global2._send('setScript:', kernel.ScriptID(753, 0))
			#end:case
			case 92:
				global1._send('handsOff:')
				script._send('caller:', kernel.ScriptID(754, 0))
				local79 = 1
				kernel.ScriptID(754, 0)._send('start:', -1)
				global2._send('setScript:', kernel.ScriptID(754, 0))
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class cassima(Actor):
	#property vars (may be empty)
	x = 21
	y = 161
	noun = 7
	view = 7820
	
	@classmethod
	def cue():
		super._send('cue:')
		match local84.post('++')
			case 1:
				self._send(
					'setLoop:', 3,
					'setCycle:', Walk,
					'posn:', 131, 160,
					'setMotion:', MoveTo, 32, 175, self
				)
			#end:case
			case 2:
				self._send('setLoop:', 4, 'setCycle:', End)
			#end:case
		#end:match
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		if local82:
			match param1
				case 1:
					global91._send('say:', noun, param1, 17)
				#end:case
				case 2:
					if local83:
						global91._send('say:', noun, param1, 20)
					else:
						local83.post('++')
						global91._send('say:', noun, param1, 19)
					#endif
				#end:case
				else:
					super._send('doVerb:', param1)
				#end:else
			#end:match
		else:
			match param1
				case 1:
					global91._send('say:', noun, param1, 18)
				#end:case
				else:
					super._send('doVerb:', param1, &rest)
				#end:else
			#end:match
		#endif
	#end:method

#end:class or instance

@SCI.instance
class door(Feature):
	#property vars (may be empty)
	noun = 3
	onMeCheck = 2
	
#end:class or instance

@SCI.instance
class theWindows(Feature):
	#property vars (may be empty)
	noun = 8
	onMeCheck = 8
	
#end:class or instance

@SCI.instance
class stairs(Feature):
	#property vars (may be empty)
	noun = 9
	onMeCheck = 16388
	
	@classmethod
	def init():
		super._send('init:', &rest)
		global93._send('add:', self)
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		global93._send('delete:', self)
	#end:method

#end:class or instance

@SCI.instance
class roomConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class egoDoVerb(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		if proc999_5(param1, 1, 2, 4):
			super._send('doVerb:', param1)
		else:
			global91._send('say:', 1, 0, 0, 0, 0, 0)
			return 1
		#endif
	#end:method

#end:class or instance

@SCI.instance
class swordCursor(Cursor):
	#property vars (may be empty)
	view = 7506
	
#end:class or instance

@SCI.instance
class swordIcon(Kq6IconItem):
	#property vars (may be empty)
	view = 7502
	loop = 0
	cel = 0
	message = 23
	signal = 65
	maskView = 7502
	maskCel = 2
	lowlightColor = 19
	hrView = 7505
	
	@classmethod
	def init():
		if 
			(= temp0
				if (global169 and (not kernel.Platform(5))):
					kernel.Platform(6)
				#endif
			)
			maskView = 7505
		#endif
		super._send('init:', &rest)
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:', &rest)
		if 
			(= temp0
				if (global169 and (not kernel.Platform(5))):
					kernel.Platform(6)
				#endif
			)
			maskLoop = 1
			maskView = 7502
		#endif
	#end:method

#end:class or instance

