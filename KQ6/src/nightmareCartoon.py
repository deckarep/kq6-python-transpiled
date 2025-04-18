#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 202
import sci_sh
import kernel
import Main
import Scaler
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	nightmareCartoon = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = [180, 127, 180, 128, 180, 128, 178, 131, 181, 131, 196, 124, 207, 129, 207, 129, 207, 129, 217, 131, -1]
local21 = -1


@SCI.instance
class nightmare(Actor):
	#property vars (may be empty)
	x = 146
	y = 119
	view = 203
	
#end:class or instance

@SCI.instance
class nightmareCartoon(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				Cursor._send('showCursor:', 1)
				global0._send('hide:')
				nightmare._send('init:', 'setCycle:', End, self)
				global105._send('number:', 346, 'loop:', 1, 'play:')
			#end:case
			case 1:
				ticks = 120
			#end:case
			case 2:
				nightmare._send('posn:', 180, 126, 'view:', 203, 'loop:', 2, 'cel:', 0)
				global0._send(
					'show:',
					'setScale:', 0,
					'normal:', 0,
					'view:', 203,
					'loop:', 1,
					'cel:', 0,
					'setSpeed:', 6,
					'setPri:', 15,
					'posn:', 180, 80,
					'setCycle:', End, self
				)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				global0._send(
					'reset:', 7,
					'ignoreActors:',
					'setPri:', 15,
					'posn:', 199, 126,
					'setScale:', Scaler, 100, 50, 112, 57
				)
				global102._send('number:', 915, 'loop:', -1, 'play:')
				cycles = 2
			#end:case
			case 5:
				register = -1
				global91._send('say:', 1, 0, 2, 0, self)
			#end:case
			case 6:
				global0._send('setMotion:', MoveTo, 169, 137, self)
			#end:case
			case 7:
				global0._send('setHeading:', 45, self)
			#end:case
			case 8:
				nightmare._send(
					'view:', 2031,
					'loop:', 0,
					'cel:', 0,
					'posn:', 174, 123,
					'setCycle:', End, self
				)
				global105._send('number:', 346, 'loop:', 1, 'play:')
			#end:case
			case 9:
				if (local0[(local21 + 1)] != -1):
					nightmare._send(
						'view:', 2031,
						'loop:', 1,
						'cel:', register.post('++'),
						'posn:', local0[local21.post('++')], local0[local21.post('++')]
					)
					state.post('--')
				#endif
				ticks = 10
			#end:case
			case 10:
				nightmare._send('dispose:')
				global0._send('setPri:', -1, 'ignoreActors:', 0)
				cycles = 2
			#end:case
			case 11:
				global1._send('handsOn:')
				global69._send('enable:', 6)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(202)
	#end:method

#end:class or instance

