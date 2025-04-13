#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 342
import sci_sh
import kernel
import Main
import Conversation
import Scaler
import PolyPath
import StopWalk
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	proc342_0 = 0,
	proc342_1 = 1,
	proc342_2 = 2,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.procedure
def proc342_0():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	shieldGuard._send('posn:', 62, 113, 'loop:', 2, 'init:', 'stopUpd:', 'setCycle:', StopWalk, -1)
	spearGuard._send('posn:', 134, 108, 'loop:', 2, 'init:', 'stopUpd:', 'setCycle:', StopWalk, -1)
	bird._send('init:', 'stopUpd:')
	global2._send('setScript:', celesteRescue)
#end:procedure

@SCI.procedure
def proc342_1():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	global2._send('setScript:', flyIn)
#end:procedure

@SCI.procedure
def proc342_2():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	shieldGuard._send(
		'posn:', 285, 155,
		'loop:', 1,
		'init:',
		'setStep:', 3, 2,
		'cycleSpeed:', 0,
		'moveSpeed:', 0,
		'setCycle:', StopWalk, -1
	)
	spearGuard._send(
		'posn:', 135, 155,
		'loop:', 0,
		'init:',
		'setStep:', 3, 2,
		'cycleSpeed:', 0,
		'moveSpeed:', 0,
		'setCycle:', StopWalk, -1
	)
	global1._send('handsOff:')
	global2._send('setScript:', toGehenna)
#end:procedure

@SCI.instance
class cliffTalk(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class celeste(Actor):
	#property vars (may be empty)
	yStep = 3
	signal = 28672
	illegalBits = 0
	xStep = 5
	
#end:class or instance

@SCI.instance
class shieldGuard(Actor):
	#property vars (may be empty)
	yStep = 3
	view = 344
	signal = 28672
	illegalBits = 0
	xStep = 5
	
#end:class or instance

@SCI.instance
class spearGuard(Actor):
	#property vars (may be empty)
	yStep = 3
	view = 343
	signal = 28672
	illegalBits = 0
	xStep = 5
	
#end:class or instance

@SCI.instance
class bird(Actor):
	#property vars (may be empty)
	x = 141
	y = 142
	yStep = 8
	view = 342
	priority = 14
	signal = 28688
	illegalBits = 0
	xStep = 14
	
#end:class or instance

@SCI.instance
class eyeGlint(Prop):
	#property vars (may be empty)
	view = 902
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('setPri:', 15, 'cycleSpeed:', 6)
		super._send('init:')
	#end:method

#end:class or instance

@SCI.instance
class flyer(Actor):
	#property vars (may be empty)
	x = 230
	y = -15
	view = 353
	signal = 24576
	
#end:class or instance

@SCI.instance
class glintScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				seconds = 1
			#end:case
			case 1:
				client._send('show:', 'setCycle:', End, self)
			#end:case
			case 2:
				client._send('setCycle:', Beg, self)
			#end:case
			case 3:
				client._send('hide:')
				seconds = kernel.Random(2, 5)
			#end:case
			case 4:
				self._send('start:', 1, 'init:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class celesteRescue(Script):
	#property vars (may be empty)
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if local0:
			shieldGuard._send('x:', (spearGuard._send('x:') - 26), 'y:', (spearGuard._send('y:') - 10))
			global0._send('x:', (shieldGuard._send('x:') + 16), 'y:', (shieldGuard._send('y:') + 35))
		#endif
		super._send('doit:')
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				seconds = 4
			#end:case
			case 1:
				eyeGlint._send(
					'init:',
					'posn:', (bird._send('x:') + 2), (bird._send('y:') - 11),
					'setScript:', glintScript
				)
				global91._send('say:', 1, 0, 11, 1, self, 340)
			#end:case
			case 2:
				shieldGuard._send('stopUpd:')
				spearGuard._send('stopUpd:')
				global105._send('number:', 909, 'setLoop:', 1, 'play:')
				kernel.ScriptID(340, 2)._send('setMotion:', MoveTo, 0, 149, self)
			#end:case
			case 3:
				kernel.ScriptID(340, 2)._send('addToPic:', 'dispose:')
				seconds = 2
			#end:case
			case 4:
				kernel.UnLoad(128, 340)
				celeste._send(
					'view:', 361,
					'setLoop:', 2,
					'cel:', 0,
					'posn:', 5, 138,
					'setPri:', 8,
					'init:',
					'setCycle:', 0,
					'setMotion:', MoveTo, 20, 138, self
				)
				ticks = 6
			#end:case
			case 5:
				celeste._send('cel:', 1, 'posn:', 22, 138)
				ticks = 6
			#end:case
			case 6:
				celeste._send('cel:', 2, 'posn:', 26, 138)
				ticks = 6
			#end:case
			case 7:
				celeste._send('cel:', 3, 'posn:', 32, 138)
				ticks = 6
			#end:case
			case 8:
				celeste._send('cel:', 4, 'posn:', 36, 139)
				ticks = 6
			#end:case
			case 9:
				celeste._send('cel:', 5, 'posn:', 38, 139)
				ticks = 6
			#end:case
			case 10:
				celeste._send(
					'view:', 364,
					'setLoop:', -1,
					'setCycle:', Walk,
					'setMotion:', MoveTo, 39, 139, self
				)
				kernel.UnLoad(128, 361)
			#end:case
			case 11:
				celeste._send('setMotion:', MoveTo, 89, 139, self)
			#end:case
			case 12:
				spearGuard._send(
					'startUpd:',
					'view:', 363,
					'setLoop:', 1,
					'setCycle:', CT, 3, 1, self
				)
				shieldGuard._send('startUpd:', 'view:', 363, 'setLoop:', 0, 'setCycle:', CT, 3, 1)
			#end:case
			case 13:
				shieldGuard._send('stopUpd:')
				spearGuard._send('stopUpd:')
				celeste._send('setPri:', 15)
				global0._send('show:', 'ignoreActors:', 1, 'setPri:', 8, 'setCycle:', End, self)
			#end:case
			case 14:
				global0._send('reset:', 0, 'posn:', 22, 138, 'setMotion:', MoveTo, 63, 148, self)
			#end:case
			case 15:
				spearGuard._send('startUpd:', 'view:', 363, 'setCycle:', End, self)
				shieldGuard._send('startUpd:', 'view:', 363, 'setCycle:', End)
			#end:case
			case 16:
				ticks = 12
			#end:case
			case 17:
				cliffTalk._send(
					'add:', 340, 1, 0, 11, 2,
					'add:', 340, 1, 0, 11, 3,
					'add:', 340, 1, 0, 11, 4,
					'add:', 340, 1, 0, 11, 5,
					'init:', self
				)
			#end:case
			case 18:
				shieldGuard._send('stopUpd:')
				spearGuard._send('stopUpd:')
				global0._send('stopUpd:')
				celeste._send(
					'view:', 365,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', 96, 69,
					'setCycle:', End, self
				)
				kernel.UnLoad(128, 364)
			#end:case
			case 19:
				celeste._send(
					'view:', 3651,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', 103, 109,
					'setStep:', 10, 5,
					'setCycle:', Fwd,
					'setMotion:', MoveTo, 228, 82, self
				)
				kernel.UnLoad(128, 365)
			#end:case
			case 20:
				global105._send('number:', 344, 'setLoop:', 1, 'play:')
				eyeGlint._send('dispose:')
				bird._send(
					'setLoop:', 1,
					'setSpeed:', 3,
					'xStep:', 10,
					'setCycle:', Fwd,
					'setMotion:', MoveTo, 335, 100, self
				)
				celeste._send(
					'setLoop:', -1,
					'setScale:', Scaler, 100, 10, 69, 40,
					'y:', (celeste._send('y:') - 12),
					'setMotion:', MoveTo, 246, 40, self
				)
			#end:case
			case 21: 0#end:case
			case 22:
				celeste._send('dispose:')
				global0._send('setMotion:', PolyPath, 149, 136, self)
			#end:case
			case 23:
				bird._send('dispose:')
				global0._send('setHeading:', 0)
				cycles = 8
			#end:case
			case 24:
				shieldGuard._send(
					'view:', 344,
					'setCycle:', StopWalk, -1,
					'setLoop:', -1,
					'setMotion:', MoveTo, (global0._send('x:') - 26), (-
							global0._send('y:')
							2
						), self
				)
				spearGuard._send(
					'view:', 343,
					'setCycle:', StopWalk, -1,
					'setLoop:', 2,
					'setMotion:', MoveTo, (global0._send('x:') + 29), (-
							global0._send('y:')
							2
						), self
				)
			#end:case
			case 25: 0#end:case
			case 26:
				shieldGuard._send('dispose:')
				spearGuard._send('dispose:')
				global0._send(
					'normal:', 0,
					'view:', 3510,
					'setLoop:', 0,
					'cel:', 0,
					'setPri:', 13,
					'posn:', global0._send('x:'), (global0._send('y:') + 4),
					'setCycle:', End, self
				)
				kernel.UnLoad(128, 900)
			#end:case
			case 27:
				global0._send(
					'view:', 352,
					'setStep:', 15, 12,
					'cycleSpeed:', 6,
					'moveSpeed:', 6,
					'setLoop:', 0,
					'cel:', 0,
					'setCycle:', End, self
				)
				kernel.UnLoad(128, 3510)
			#end:case
			case 28:
				global0._send(
					'view:', 353,
					'setCycle:', Fwd,
					'posn:', global0._send('x:'), (global0._send('y:') - 40),
					'setMotion:', MoveTo, global0._send('x:'), -50, self
				)
				kernel.UnLoad(128, 3512)
			#end:case
			case 29:
				global102._send('fade:', 0, 20, 15)
				global2._send('newRoom:', 370, -32758)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class toGehenna(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global0._send(
					'view:', 3011,
					'setLoop:', 6,
					'setPri:', 15,
					'cel:', 0,
					'normal:', 0,
					'posn:', 257, 237,
					'cycleSpeed:', 8,
					'setCycle:', End, self
				)
			#end:case
			case 1:
				global0._send('cel:', 0, 'posn:', 228, 223, 'setCycle:', End, self)
			#end:case
			case 2:
				global0._send('cel:', 0, 'posn:', 199, 209, 'setCycle:', End, self)
			#end:case
			case 3:
				global0._send('cel:', 0, 'posn:', 175, 195, 'setCycle:', End, self)
			#end:case
			case 4:
				global0._send(
					'view:', 3011,
					'setLoop:', 1,
					'cel:', 5,
					'posn:', 164, 194,
					'cycleSpeed:', 8,
					'setCycle:', End, self
				)
			#end:case
			case 5:
				global0._send('view:', 301, 'setLoop:', 0, 'cel:', 2, 'normal:', 0, 'posn:', 161, 185)
				cycles = 4
			#end:case
			case 6:
				global0._send('cel:', 3, 'posn:', 161, 185)
				cycles = 4
			#end:case
			case 7:
				global0._send('cel:', 4, 'posn:', 161, 185)
				cycles = 4
			#end:case
			case 8:
				global0._send(
					'posn:', 162, 169,
					'reset:', 6,
					'setScale:', Scaler, 100, 5, 105, 65,
					'setPri:', -1,
					'setMotion:', MoveTo, 214, 167, self
				)
			#end:case
			case 9:
				global0._send('setHeading:', 0, self)
			#end:case
			case 10:
				cycles = 6
			#end:case
			case 11:
				global91._send('say:', 1, 0, 2, 1, self, 340)
			#end:case
			case 12:
				shieldGuard._send('setCycle:', StopWalk, -1, 'setMotion:', MoveTo, 235, 162)
				spearGuard._send(
					'setCycle:', StopWalk, -1,
					'setMotion:', MoveTo, 196, 162, self
				)
			#end:case
			case 13:
				seconds = 2
			#end:case
			case 14:
				client._send('setScript:', tossEmIn, 0, 0)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class flyIn(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				local1 = 1
				global0._send(
					'view:', 3511,
					'setPri:', 14,
					'setLoop:', 0,
					'setStep:', 12, 8,
					'posn:', 340, -40,
					'setCycle:', Fwd,
					'setMotion:', MoveTo, 245, 53, self
				)
			#end:case
			case 1:
				global0._send('view:', 3512, 'cel:', 0, 'posn:', 212, 88, 'setCycle:', End, self)
				kernel.UnLoad(128, 3511)
			#end:case
			case 2:
				global0._send(
					'reset:', 1,
					'cel:', 4,
					'posn:', 170, 128,
					'setMotion:', MoveTo, 145, 128, self
				)
				kernel.UnLoad(128, 3512)
				shieldGuard._send(
					'view:', 344,
					'posn:', 186, 126,
					'loop:', 1,
					'init:',
					'setCycle:', Walk,
					'illegalBits:', 0,
					'setMotion:', MoveTo, 181, 126
				)
				spearGuard._send(
					'view:', 343,
					'posn:', 193, 129,
					'loop:', 1,
					'init:',
					'setCycle:', Walk,
					'illegalBits:', 0,
					'setMotion:', MoveTo, 188, 129
				)
			#end:case
			case 3:
				global2._send('setScript:', tossEmIn, 0, 1)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class tossEmIn(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				shieldGuard._send(
					'view:', 344,
					'setLoop:', -1,
					'setStep:', 3, 2,
					'setSpeed:', 4,
					'setCycle:', StopWalk, -1,
					'setMotion:', MoveTo, 139, 109, self
				)
				kernel.UnLoad(128, 349)
				global0._send('setLoop:', -1, 'setSpeed:', 4, 'setMotion:', MoveTo, 111, 110)
				spearGuard._send(
					'view:', 343,
					'setLoop:', -1,
					'setStep:', 3, 2,
					'setSpeed:', 4,
					'setCycle:', StopWalk, -1,
					'setMotion:', MoveTo, 85, 109, self
				)
				kernel.UnLoad(128, 348)
			#end:case
			case 1:
				shieldGuard._send('setHeading:', 270)
			#end:case
			case 2:
				global0._send('setHeading:', 0)
				spearGuard._send('setHeading:', 90)
				seconds = 2
			#end:case
			case 3:
				spearGuard._send(
					'view:', 362,
					'setPri:', 13,
					'setLoop:', 1,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 4:
				spearGuard._send('setCycle:', Beg)
				global105._send('number:', 342, 'setLoop:', 1, 'play:')
				kernel.ScriptID(340, 1)._send('setCycle:', End, self)
			#end:case
			case 5:
				if register:
					global91._send('say:', 1, 0, 9, 0, self, 340)
				else:
					cliffTalk._send(
						'add:', 340, 1, 0, 9, 2,
						'add:', 340, 1, 0, 9, 3,
						'add:', 340, 1, 0, 9, 4,
						'add:', 340, 1, 0, 9, 5,
						'init:', self
					)
				#endif
			#end:case
			case 6:
				spearGuard._send('hide:')
				shieldGuard._send('hide:')
				global0._send(
					'view:', 362,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', 111, 115,
					'normal:', 0,
					'cycleSpeed:', 12,
					'setCycle:', End, self
				)
			#end:case
			case 7:
				global0._send('hide:')
				spearGuard._send('show:')
				shieldGuard._send('show:')
				kernel.ScriptID(340, 1)._send('setCycle:', Beg, self)
			#end:case
			case 8:
				global105._send('number:', 403, 'setLoop:', 1, 'play:', self)
			#end:case
			case 9:
				if (global12 == 370):
					Cursor._send('showCursor:', 1)
				#endif
				global2._send('newRoom:', 405)
			#end:case
		#end:match
	#end:method

#end:class or instance

