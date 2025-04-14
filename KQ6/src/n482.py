#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 482
import sci_sh
import kernel
import Main
import PolyPath
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	proc482_0 = 0,
	proc482_1 = 1,
	proc482_2 = 2,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


@SCI.procedure
def proc482_0():
	kernel.ScriptID(480, 5)._send('register:', 1)
	global0._send('setScript:', grabForHole)
#end:procedure

@SCI.procedure
def proc482_1():
	global0._send('setScript:', getHole)
#end:procedure

@SCI.procedure
def proc482_2():
	kernel.ScriptID(480, 5)._send('register:', 1)
	global0._send('setScript:', lookThruHole)
#end:procedure

@SCI.instance
class getHole(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global69._send('disable:', 6)
				seconds = 2
			#end:case
			case 1:
				if (kernel.ScriptID(480, 1)._send('x:') > 280):
					global105._send('number:', 483, 'setLoop:', 1, 'play:')
					kernel.ScriptID(480, 1)._send(
						'setLoop:', 5,
						'setCycle:', Walk,
						'setMotion:', MoveTo, 263, 47
					)
					local0 = 1
				#endif
				global0._send('setMotion:', PolyPath, 302, 92, self)
			#end:case
			case 2:
				global0._send('setMotion:', PolyPath, 273, 87, self)
			#end:case
			case 3:
				if (local0 == 1):
					self._send('cue:')
				else:
					global105._send('number:', 483, 'setLoop:', 1, 'play:')
					kernel.ScriptID(480, 1)._send(
						'setLoop:', 5,
						'setCycle:', Walk,
						'setMotion:', MoveTo, 256, 64, self
					)
				#endif
			#end:case
			case 4:
				if (local0 == 1):
					local0 = 0
					kernel.ScriptID(480, 1)._send(
						'setLoop:', 4,
						'cel:', 5,
						'posn:', 254, 50,
						'cycleSpeed:', 3,
						'setCycle:', Beg
					)
				#endif
				global0._send(
					'normal:', 0,
					'view:', 482,
					'setLoop:', 3,
					'cel:', 0,
					'posn:', 258, 90,
					'setCycle:', CT, 3, 1, self
				)
			#end:case
			case 5:
				global1._send('givePoints:', 1)
				global105._send('stop:')
				kernel.ScriptID(480, 1)._send('dispose:')
				global0._send('get:', 18, 'setCycle:', End, self)
			#end:case
			case 6:
				global0._send('posn:', 273, 87, 'reset:', 7)
				cycles = 6
			#end:case
			case 7:
				global91._send('say:', 21, 5, 10, 1, self, 480)
			#end:case
			case 8:
				global0._send('setMotion:', PolyPath, 197, 116, self)
			#end:case
			case 9:
				global0._send('setHeading:', 135, self)
			#end:case
			case 10:
				cycles = 2
			#end:case
			case 11:
				kernel.ScriptID(480, 5)._send('register:', 1)
				global69._send('enable:', 6)
				global1._send('handsOn:')
				self._send('dispose:')
				kernel.DisposeScript(482)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class grabForHole(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global91._send('say:', 21, 5, 8, 1, self, 480)
			#end:case
			case 1:
				global0._send('setMotion:', PolyPath, 300, 97, self)
			#end:case
			case 2:
				global0._send('setMotion:', PolyPath, 294, 81, self)
			#end:case
			case 3:
				global91._send('say:', 21, 5, 8, 2, self, 480)
			#end:case
			case 4:
				kernel.ScriptID(480, 1)._send('hide:')
				global105._send('number:', 483, 'setLoop:', 1, 'play:')
				global0._send(
					'view:', 482,
					'setLoop:', 0,
					'cel:', 0,
					'normal:', 0,
					'setPri:', 5,
					'posn:', 280, 83,
					'cycleSpeed:', 8,
					'setCycle:', End, self
				)
			#end:case
			case 5:
				kernel.ScriptID(480, 1)._send('posn:', 238, 70, 'show:')
				global0._send('posn:', 294, 81, 'reset:', 7)
				ticks = 6
			#end:case
			case 6:
				global91._send('say:', 21, 5, 8, 3, self, 480)
			#end:case
			case 7:
				global0._send('setMotion:', PolyPath, 197, 116, self)
			#end:case
			case 8:
				global0._send('setHeading:', 135)
				global1._send('handsOn:')
				self._send('dispose:')
				kernel.DisposeScript(482)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lookThruHole(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				if kernel.ScriptID(40, 0)._send('holeLooks:'):
					self._send('cue:')
				else:
					global91._send('say:', 21, 1, 5, 1, self, 480)
				#endif
			#end:case
			case 1:
				global0._send('setMotion:', PolyPath, 283, 94, self)
			#end:case
			case 2:
				global0._send('setHeading:', 0)
				ticks = 6
			#end:case
			case 3:
				if kernel.ScriptID(40, 0)._send('holeLooks:'):
					global91._send('say:', 21, 1, 6, 1, self, 480)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 4:
				holeInset._send('init:')
				seconds = 3
			#end:case
			case 5:
				holeInset._send('dispose:')
				if kernel.ScriptID(40, 0)._send('holeLooks:'):
					global91._send('say:', 21, 1, 6, 2, self, 480)
				else:
					global91._send('say:', 21, 1, 5, 2, self, 480)
				#endif
			#end:case
			case 6:
				global0._send(
					'setLoop:', 3,
					'setMotion:', MoveTo, (global0._send('x:') + 5), (global0._send('y:') + 5), self
				)
			#end:case
			case 7:
				if kernel.ScriptID(40, 0)._send('holeLooks:'):
					self._send('cue:')
				else:
					global105._send('number:', 483, 'setLoop:', 1, 'play:')
					kernel.ScriptID(480, 1)._send(
						'setMotion:', MoveTo, (kernel.ScriptID(480, 1)._send('x:') - 5), kernel.ScriptID(480, 1)._send(
								'y:'
							), self
					)
				#endif
			#end:case
			case 8:
				if kernel.ScriptID(40, 0)._send('holeLooks:'):
					self._send('cue:')
				else:
					kernel.ScriptID(480, 1)._send(
						'setMotion:', MoveTo, (kernel.ScriptID(480, 1)._send('x:') + 5), kernel.ScriptID(480, 1)._send(
								'y:'
							), self
					)
				#endif
			#end:case
			case 9:
				if kernel.ScriptID(40, 0)._send('holeLooks:'):
					self._send('cue:')
				else:
					global91._send('say:', 21, 1, 5, 3, self, 480)
				#endif
			#end:case
			case 10:
				global1._send('handsOn:')
				global0._send('reset:', 3)
				kernel.ScriptID(40, 0)._send('holeLooks:', 1)
				self._send('dispose:')
				kernel.DisposeScript(482)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class holeInset(View):
	#property vars (may be empty)
	x = 162
	y = 98
	view = 487
	priority = 15
	signal = 16400
	
	@classmethod
	def init():
		fields._send('init:')
		super._send('init:')
	#end:method

	@classmethod
	def dispose():
		fields._send('dispose:')
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class fields(View):
	#property vars (may be empty)
	x = 164
	y = 93
	view = 490
	priority = 14
	signal = 16400
	
#end:class or instance

