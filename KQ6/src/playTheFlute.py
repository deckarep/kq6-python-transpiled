#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 85
import sci_sh
import kernel
import Main
import Sound
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	playTheFlute = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None
local4 = None
local5 = None


@SCI.instance
class playTheFlute(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('killSound:', 1)
				if (((global0._send('scaleY:') / 128) * 100) < 80):
					local5 = 1
				#endif
				if global1._send('isHandsOn:'):
					global1._send('handsOff:')
					local4 = 1
				#endif
				cycles = 2
			#end:case
			case 1:
				local0 = global0._send('cel:')
				ticks = 6
			#end:case
			case 2:
				global0._send('normal:', 0, 'view:', 920, 'cel:', 0, 'cycleSpeed:', 6)
				(cond
					case (global0._send('heading:') < 136):
						local3 = 0
						local2 = -2
						local1 = 0
						global0._send(
							'setLoop:', 0,
							'posn:', global0._send('x:'), (global0._send('y:') + 2)
						)
					#end:case
					case (global0._send('heading:') < 260):
						local3 = 2
						if local5:
							local2 = 0
							local1 = -3
							global0._send(
								'setLoop:', 2,
								'posn:', (global0._send('x:') + 3), global0._send('y:')
							)
						else:
							local1 = 0
							local2 = -1
							global0._send(
								'setLoop:', 2,
								'posn:', global0._send('x:'), (global0._send('y:') + 1)
							)
						#endif
					#end:case
					else:
						local3 = 1
						local1 = -2
						local2 = -1
						global0._send(
							'setLoop:', 1,
							'posn:', (global0._send('x:') + 2), (global0._send('y:') + 1)
						)
					#end:else
				)
				cycles = 4
			#end:case
			case 3:
				localMusic._send('number:', 942, 'setLoop:', 1, 'play:', self)
				global0._send('setCycle:', Fwd)
			#end:case
			case 4:
				global0._send(
					'reset:', local0,
					'posn:', (global0._send('x:') + local1), (global0._send('y:') + local2)
				)
				cycles = 4
			#end:case
			case 5:
				if local4:
					global91._send('say:', 1, 31, 0, 1, self, 0)
				else:
					cycles = 1
				#endif
			#end:case
			case 6:
				global1._send('handsOn:')
				localMusic._send('stop:', 'dispose:')
				global1._send('killSound:', 0)
				self._send('dispose:')
				kernel.DisposeScript(85)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class localMusic(Sound):
	#property vars (may be empty)
#end:class or instance

