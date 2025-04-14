#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 301
import sci_sh
import kernel
import Main
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	proc301_0 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


@SCI.procedure
def proc301_0():
	global2._send('setScript:', flyIn)
#end:procedure

@SCI.instance
class guard1(Actor):
	#property vars (may be empty)
	yStep = 8
	signal = 24576
	cycleSpeed = 3
	illegalBits = 0
	xStep = 12
	
#end:class or instance

@SCI.instance
class guard2(Actor):
	#property vars (may be empty)
	yStep = 8
	signal = 24576
	cycleSpeed = 3
	illegalBits = 0
	xStep = 12
	
#end:class or instance

@SCI.instance
class dummyEgo(Actor):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class flyIn(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('hide:')
				global69._send('disable:')
				dummyEgo._send(
					'view:', 3511,
					'setStep:', 12, 8,
					'ignoreHorizon:', 1,
					'posn:', 340, -40,
					'init:',
					'setCycle:', Fwd,
					'setMotion:', MoveTo, 228, 56, self
				)
			#end:case
			case 1:
				dummyEgo._send('view:', 3512, 'cel:', 0, 'posn:', 195, 91, 'setCycle:', End, self)
				kernel.UnLoad(128, 3511)
			#end:case
			case 2:
				kernel.UnLoad(128, 3512)
				guard1._send('view:', 3013, 'loop:', 0, 'cel:', 1, 'posn:', 169, 128, 'init:', 'stopUpd:')
				guard2._send(
					'view:', 3013,
					'loop:', 0,
					'cel:', 0,
					'posn:', 173, 132,
					'setPri:', (guard1._send('priority:') - 2),
					'init:',
					'stopUpd:'
				)
				global0._send(
					'reset:', 1,
					'cel:', 4,
					'posn:', 162, 129,
					'setPri:', (guard1._send('priority:') - 1),
					'show:',
					'setMotion:', MoveTo, 145, 129, self
				)
				dummyEgo._send('dispose:')
				global102._send('fade:')
			#end:case
			case 3:
				global0._send('setHeading:', 180, self)
			#end:case
			case 4:
				guard1._send(
					'view:', 344,
					'loop:', 1,
					'setCycle:', Walk,
					'setMotion:', MoveTo, (guard1._send('x:') + 15), guard1._send('y:')
				)
				guard2._send(
					'view:', 343,
					'loop:', 1,
					'setCycle:', Walk,
					'setMotion:', MoveTo, (guard2._send('x:') + 15), guard2._send('y:'), self
				)
			#end:case
			case 5:
				global102._send(
					'number:', 915,
					'setLoop:', -1,
					'setVol:', 0,
					'play:',
					'fade:', 127, 10, 10
				)
				global0._send('setHeading:', 90, self)
			#end:case
			case 6:
				global0._send('view:', 3013, 'loop:', 0, 'cel:', 2)
				kernel.UnLoad(128, 900)
				cycles = 8
			#end:case
			case 7:
				guard1._send('view:', 349, 'loop:', 0, 'cel:', 0, 'setCycle:', End)
				kernel.UnLoad(128, 344)
				guard2._send('view:', 348, 'loop:', 0, 'cel:', 0, 'setCycle:', End, self)
				kernel.UnLoad(128, 343)
			#end:case
			case 8:
				guard1._send(
					'view:', 3491,
					'loop:', 0,
					'cel:', 0,
					'posn:', 195, 74,
					'setCycle:', Fwd,
					'setStep:', 12, 8,
					'cycleSpeed:', 3,
					'setMotion:', MoveTo, 345, -15, self
				)
				kernel.UnLoad(128, 349)
				guard2._send(
					'view:', 3481,
					'loop:', 0,
					'cel:', 0,
					'posn:', 219, 80,
					'setCycle:', Fwd,
					'setStep:', 12, 8,
					'cycleSpeed:', 3,
					'setMotion:', MoveTo, 375, -15
				)
				kernel.UnLoad(128, 348)
			#end:case
			case 9:
				if (not (global12 == 380)):
					Cursor._send('showCursor:', 1)
				#endif
				global0._send('reset:', 0)
				guard1._send('setCycle:', 0, 'setMotion:', 0, 'delete:', 'dispose:')
				guard2._send('setCycle:', 0, 'setMotion:', 0, 'delete:', 'dispose:')
				global69._send('enable:')
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

