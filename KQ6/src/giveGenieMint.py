#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 753
import sci_sh
import kernel
import Main
import rm750
import Scaler
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	giveGenieMint = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = [14, 77, 37, 13, 71, 16, 9, 259, 44, 10, 33, 79, 9, 138, 104, -1, -1, -1]
local18 = None


@SCI.instance
class giveGenieMint(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(752)
		kernel.UnLoad(128, 7501)
		kernel.UnLoad(128, 7503)
		kernel.UnLoad(128, 702)
		kernel.DisposeScript(1012)
		kernel.DisposeScript(753)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global91._send('say:', 5, 67, 0, 1, self)
			#end:case
			case 1:
				global1._send('givePoints:', 1)
				if global0._send('looper:'):
					global0._send('looper:')._send('dispose:')
				#endif
				global0._send(
					'view:', 7500,
					'setLoop:', 2,
					'normal:', 0,
					'setScale:', 0,
					'cel:', 0,
					'cycleSpeed:', 8,
					'looper:', 0,
					'setCycle:', CT, 4, 1, self
				)
			#end:case
			case 2:
				kernel.ScriptID(750, 4)._send(
					'view:', 702,
					'loop:', 6,
					'cel:', 0,
					'cycleSpeed:', 7,
					'setCycle:', CT, 4, 1, self
				)
			#end:case
			case 3:
				kernel.ScriptID(750, 4)._send('setCycle:', Beg, self)
			#end:case
			case 4:
				global91._send('say:', 5, 67, 0, 2, self)
			#end:case
			case 5:
				kernel.ScriptID(750, 2)._send('cel:', 1, 'forceUpd:')
				cycles = 4
			#end:case
			case 6:
				global91._send('say:', 5, 67, 0, 3, self)
			#end:case
			case 7:
				self._send('setScript:', kernel.ScriptID(752, 2), self, kernel.ScriptID(750, 4))
			#end:case
			case 8:
				global0._send('setCel:', 255)
				kernel.ScriptID(750, 2)._send('cel:', 2, 'forceUpd:')
				kernel.ScriptID(750, 4)._send(
					'view:', 752,
					'loop:', 1,
					'cel:', 0,
					'cycleSpeed:', 8,
					'posn:', 170, 137
				)
				ticks = 60
			#end:case
			case 9:
				self._send('setScript:', kernel.ScriptID(752, 1), self, kernel.ScriptID(750, 4))
			#end:case
			case 10:
				kernel.ScriptID(750, 4)._send('setCycle:', CT, 1, 1, self)
			#end:case
			case 11:
				cycles = 2
			#end:case
			case 12:
				if global0._send('looper:'):
					global0._send('looper:')._send('dispose:')
				#endif
				global0._send(
					'normal:', 0,
					'view:', 7500,
					'setLoop:', 3,
					'setCycle:', 0,
					'looper:', 0,
					'setScale:', Scaler, 102, 76, 189, 139
				)
				kernel.ScriptID(750, 4)._send('setCycle:', End, self)
			#end:case
			case 13:
				global91._send('say:', 5, 67, 0, 4, self)
			#end:case
			case 14:
				global91._send('say:', 5, 67, 0, 5, self)
			#end:case
			case 15:
				global91._send('say:', 5, 67, 0, 6, self)
			#end:case
			case 16:
				kernel.ScriptID(750, 4)._send(
					'loop:', 2,
					'cel:', 8,
					'cycleSpeed:', 4,
					'setCycle:', CT, 2, 1, self
				)
			#end:case
			case 17:
				cycles = 10
			#end:case
			case 18:
				kernel.ScriptID(750, 4)._send('cel:', 3)
				cycles = 8
			#end:case
			case 19:
				kernel.ScriptID(750, 4)._send('setCycle:', CT, 5, 1, self)
			#end:case
			case 20:
				cycles = 10
			#end:case
			case 21:
				global91._send('say:', 5, 67, 0, 7, self)
			#end:case
			case 22:
				global91._send('say:', 5, 67, 0, 8, self)
			#end:case
			case 23:
				kernel.ScriptID(750, 4)._send('cycleSpeed:', 6, 'setCycle:', End, self)
			#end:case
			case 24:
				global103._send('number:', 707, 'setLoop:', 1, 'play:')
				kernel.ScriptID(750, 4)._send(
					'view:', 702,
					'loop:', 7,
					'cel:', 1,
					'x:', (kernel.ScriptID(750, 4)._send('x:') - 13),
					'cycleSpeed:', 8,
					'setCycle:', End, self
				)
			#end:case
			case 25:
				global103._send('number:', 708, 'setLoop:', 1, 'play:')
				dazzleBall._send('init:', 'setCycle:', Fwd)
				cycles = 2
			#end:case
			case 26:
				global91._send('say:', 5, 67, 0, 9, self)
			#end:case
			case 27:
				if (local0[local18] != -1):
					state.post('--')
					dazzleBall._send(
						'loop:', local0[local18],
						'setMotion:', MoveTo, local0[(local18 + 1)], [local0
								(local18 + 2)
							], self
					)
					if (local18 >= 3):
						global103._send('number:', 709, 'loop:', 1, 'play:')
					#endif
					(local18 += 3)
				else:
					cycles = 1
				#endif
			#end:case
			case 28:
				global91._send('say:', 5, 67, 0, 11, self)
			#end:case
			case 29:
				dazzleBall._send('setMotion:', MoveTo, 160, 111, self)
			#end:case
			case 30:
				dazzleBall._send('loop:', 15, 'cel:', 0, 'cycleSpeed:', 7, 'setCycle:', End, self)
				global103._send('number:', 0, 'stop:')
				global103._send('number:', 753, 'setLoop:', 1, 'play:', self)
			#end:case
			case 31:
				kernel.ScriptID(750, 4)._send('dispose:')
				dazzleBall._send('dispose:')
			#end:case
			case 32:
				global91._send('say:', 5, 67, 0, 12, self)
			#end:case
			case 33:
				kernel.ScriptID(750, 2)._send('dispose:')
				if global169:
					global2._send('drawPic:', 750, 15)
				else:
					global2._send('drawPic:', 750, 100)
				#endif
				kernel.ScriptID(750, 9)._send('addToPic:')
				kernel.ScriptID(750, 3)._send(
					'view:', 751,
					'loop:', 8,
					'cel:', 0,
					'signal:', 16384,
					'init:',
					'setCycle:', CT, 4, 1, self
				)
			#end:case
			case 34:
				global103._send('number:', 652, 'setLoop:', 1, 'play:')
				kernel.ScriptID(750, 3)._send('setCycle:', End, self)
			#end:case
			case 35:
				global91._send('say:', 5, 67, 0, 13, self)
			#end:case
			case 36:
				global91._send('say:', 5, 67, 0, 14, self)
			#end:case
			case 37:
				proc750_5()
				if ((not global87) or (not kernel.HaveMouse())):
					seconds = 15
				else:
					seconds = 8
				#endif
			#end:case
			case 38:
				global2._send('setScript:', kernel.ScriptID(754, 1))
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class dazzleBall(Actor):
	#property vars (may be empty)
	x = 150
	y = 100
	yStep = 7
	view = 702
	loop = 14
	priority = 15
	signal = 26640
	cycleSpeed = 3
	illegalBits = 0
	xStep = 7
	moveSpeed = 0
	
#end:class or instance

