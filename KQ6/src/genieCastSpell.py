#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 744
import sci_sh
import kernel
import Main
import n913
import PolyPath
import Polygon
import LoadMany
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	genieCastSpell = 0,
	saladinKillEgo = 1,
)

@SCI.instance
class genieCastSpell(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if global2._send('obstacles:'):
					global2._send('obstacles:')._send('dispose:')
				#endif
				global2._send(
					'addObstacle:', Polygon._send('new:')._send(
							'type:', 2,
							'init:', 0, 189, 0, 0, 319, 0, 319, 189, 314, 189, 195, 189, 198, 161, 279, 161, 227, 120, 223, 120, 212, 129, 159, 129, 115, 162, 78, 189,
							'yourself:'
						), Polygon._send('new:')._send(
							'type:', 2,
							'init:', 165, 141, 238, 141, 246, 151, 159, 151,
							'yourself:'
						)
				)
				cycles = 2
			#end:case
			case 1:
				global69._send('enable:')
				global91._send('say:', 1, 0, 6, 1, self)
			#end:case
			case 2:
				self._send('setScript:', kernel.ScriptID(742, 4), self)
			#end:case
			case 3:
				global91._send('say:', 1, 0, 6, 2, self)
			#end:case
			case 4:
				global91._send('say:', 1, 0, 6, 3, self)
			#end:case
			case 5:
				global91._send('say:', 1, 0, 6, 4, self)
			#end:case
			case 6:
				global91._send('say:', 1, 0, 6, 5, self)
			#end:case
			case 7:
				global91._send('say:', 1, 0, 6, 6, self)
			#end:case
			case 8:
				proc958_0(0, 1004, 1063, 1029, 1001, 1026)
				kernel.UnLoad(128, 892)
				kernel.UnLoad(128, 899)
				kernel.UnLoad(128, 8921)
				kernel.UnLoad(128, 8992)
				kernel.UnLoad(128, 891)
				kernel.UnLoad(128, 890)
				self._send('setScript:', kernel.ScriptID(740, 23), self)
			#end:case
			case 9:
				global0._send('put:', 24)
				global1._send('handsOn:')
				kernel.ScriptID(740, 3)._send('setScript:', kernel.ScriptID(742, 5))
				self._send('dispose:')
				kernel.DisposeScript(744)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class saladinKillEgo(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				cycles = 2
			#end:case
			case 1:
				global69._send('enable:')
				if proc913_0(156):
					register = 999
					kernel.ScriptID(740, 2)._send('view:', 7415, 'setLoop:', 0, 'cel:', 3, 'setPri:', 9)
				else:
					state = 11
				#endif
				cycles = 2
			#end:case
			case 2:
				proc913_1(59)
				global91._send('say:', 1, 0, 38, 1, self)
			#end:case
			case 3:
				proc913_2(59)
				global91._send('say:', 1, 0, 38, 2, self)
			#end:case
			case 4:
				kernel.ScriptID(740, 2)._send('setCycle:', CT, 5, 1, self)
			#end:case
			case 5:
				ticks = 90
			#end:case
			case 6:
				kernel.ScriptID(740, 2)._send('setCycle:', CT, 10, 1, self)
			#end:case
			case 7:
				proc913_1(59)
				global91._send('say:', 1, 0, 38, 3, self)
			#end:case
			case 8:
				proc913_2(59)
				global91._send('say:', 1, 0, 38, 4, self)
			#end:case
			case 9:
				proc913_1(59)
				global91._send('say:', 1, 0, 38, 5, self)
			#end:case
			case 10:
				kernel.ScriptID(740, 2)._send('setCycle:', End, self)
			#end:case
			case 11:
				proc913_2(59)
				global91._send('say:', 1, 0, 38, 6, self)
			#end:case
			case 12:
				global102._send('number:', 0, 'stop:')
				global102._send('number:', 705, 'setLoop:', 1, 'play:')
				kernel.ScriptID(740, 5)._send('view:', 736, 'cycleSpeed:', 3, 'moveSpeed:', 3)
				proc913_4(kernel.ScriptID(740, 5), global0, self)
			#end:case
			case 13:
				if (not register):
					global91._send('say:', 1, 0, 5, 0, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 14:
				global0._send('setHeading:', 180)
				kernel.ScriptID(740, 5)._send(
					'setMotion:', PolyPath, (global0._send('x:') - 24), (+
							global0._send('y:')
							5
						), self
				)
			#end:case
			case 15:
				kernel.ScriptID(740, 5)._send('setHeading:', 0, self)
			#end:case
			case 16:
				global0._send('hide:')
				kernel.ScriptID(740, 5)._send(
					'view:', 738,
					'setLoop:', 2,
					'cel:', 0,
					'cycleSpeed:', 8,
					'setCycle:', CT, 2, 1, self
				)
				global103._send('number:', 0, 'stop:')
				global103._send('number:', 756, 'setLoop:', 1, 'play:')
			#end:case
			case 17:
				global103._send('number:', 0, 'stop:')
				global103._send('number:', 971, 'setLoop:', 1, 'play:', self)
			#end:case
			case 18:
				global103._send('number:', 0, 'stop:')
				global103._send('number:', 652, 'setLoop:', 1, 'play:')
				kernel.ScriptID(740, 5)._send('setCycle:', End, self)
			#end:case
			case 19:
				match register
					case 29:
						global91._send('say:', 1, 0, 29, 0, self)
					#end:case
					else:
						cycles = 2
					#end:else
				#end:match
			#end:case
			case 20:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:', &rest)
		proc0_1(33)
		kernel.DisposeScript(744)
	#end:method

#end:class or instance

