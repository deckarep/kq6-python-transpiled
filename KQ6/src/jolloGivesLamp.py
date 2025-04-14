#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 751
import sci_sh
import kernel
import Main
import rm750
import DPath
import Grooper
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	jolloGivesLamp = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = [0, 239, 135, 2, 1, 233, 136, 2, 2, 229, 137, 2, 3, 225, 137, 2, 4, 223, 138, 10, 5, 218, 138, 10, -1, -1, -1, -1, 6, 220, 138, 2, 7, 224, 136, 2, 8, 230, 138, 2, 9, 237, 138, 2, 10, 241, 137, 2, -1]


@SCI.instance
class jolloGivesLamp(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.UnLoad(128, 717)
		kernel.UnLoad(128, 754)
		kernel.DisposeScript(964)
		kernel.DisposeScript(1020)
		kernel.DisposeScript(751)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				kernel.ScriptID(750, 6)._send('setScript:', 0, 'setCycle:', 0, 'addToPic:')
				kernel.ScriptID(750, 4)._send('addToPic:')
				cycles = 2
			#end:case
			case 1:
				jollo._send(
					'init:',
					'view:', 717,
					'setPri:', 2,
					'setLoop:', 3,
					'setLoop:', Grooper,
					'posn:', 294, 198,
					'setStep:', 5, 3,
					'setSpeed:', 3,
					'setScale:',
					'scaleX:', 110,
					'scaleY:', 110,
					'setCycle:', Walk,
					'setMotion:', DPath, 281, 178, 263, 150, self
				)
			#end:case
			case 2:
				jollo._send(
					'view:', 754,
					'setLoop:', -1,
					'scaleX:', 94,
					'scaleY:', 94,
					'loop:', 1,
					'cel:', 0,
					'posn:', 247, 150,
					'setCycle:', End, self
				)
			#end:case
			case 3:
				if global0._send('looper:'):
					global0._send('looper:')._send('dispose:')
				#endif
				global0._send('normal:', 0, 'view:', 7500, 'setLoop:', 3, 'setCycle:', 0, 'looper:', 0)
				cycles = 2
			#end:case
			case 4:
				global91._send('say:', 1, 0, 3, 1, self)
			#end:case
			case 5:
				jollo._send('loop:', 2, 'cel:', 0, 'posn:', 239, 135)
				ticks = 10
			#end:case
			case 6:
				if (local0[register] != -1):
					state.post('--')
					jollo._send(
						'cel:', local0[register],
						'x:', local0[(register + 1)],
						'y:', local0[(register + 2)],
						'priority:', local0[(register + 3)]
					)
				#endif
				(register += 4)
				cycles = 5
			#end:case
			case 7:
				global0._send('get:', 25)
				global1._send('givePoints:', 1)
				global9._send('at:', 25)._send('message:', 92, 'noun:', 66)
				global1._send('handsOff:')
				global0._send(
					'setScale:', 0,
					'normal:', 0,
					'view:', 703,
					'setLoop:', 0,
					'cel:', 0,
					'cycleSpeed:', 8,
					'setCycle:', CT, 1, 1, self
				)
			#end:case
			case 8:
				global91._send('say:', 1, 0, 3, 2, self, 'oneOnly:', 0)
			#end:case
			case 9:
				global0._send('setCycle:', End)
				ticks = 3
			#end:case
			case 10:
				if (local0[register] != -1):
					state.post('--')
					jollo._send(
						'cel:', local0[register],
						'x:', local0[(register + 1)],
						'y:', local0[(register + 2)],
						'priority:', local0[(register + 3)]
					)
				#endif
				(register += 4)
				cycles = 5
			#end:case
			case 11:
				if global0._send('looper:'):
					global0._send('looper:')._send('dispose:')
				#endif
				global0._send(
					'normal:', 0,
					'view:', 7500,
					'setLoop:', 3,
					'setCycle:', 0,
					'looper:', 0,
					'scaleSignal:', 1,
					'scaleX:', 96,
					'scaleY:', 96
				)
				jollo._send(
					'view:', 717,
					'setLoop:', 2,
					'setLoop:', Grooper,
					'posn:', 250, 135,
					'scaleX:', 110,
					'scaleY:', 110,
					'setSpeed:', 3,
					'setCycle:', Walk,
					'setMotion:', DPath, 275, 157, 286, 189, self
				)
			#end:case
			case 12:
				jollo._send('dispose:')
				if global169:
					global2._send('drawPic:', 750, 15)
				else:
					global2._send('drawPic:', 750, 100)
				#endif
				kernel.ScriptID(750, 9)._send('addToPic:')
				kernel.ScriptID(750, 6)._send(
					'setScript:', kernel.ScriptID(750, 8),
					'signal:', 16384,
					'init:'
				)
				kernel.ScriptID(750, 3)._send('addToPic:')
				kernel.ScriptID(750, 4)._send('signal:', 16384, 'init:')
				cycles = 2
			#end:case
			case 13:
				proc750_5()
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class jollo(Actor):
	#property vars (may be empty)
	x = 274
	y = 197
	view = 754
	signal = 16384
	
#end:class or instance

