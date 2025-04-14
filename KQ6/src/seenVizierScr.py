#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 221
import sci_sh
import kernel
import Main
import n913
import Scaler
import DPath
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	seenVizierScr = 0,
)

@SCI.instance
class egoScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send(
					'setSpeed:', 6,
					'ignoreActors:',
					'posn:', 75, 100,
					'setPri:', 2,
					'show:',
					'setMotion:', MoveTo, 107, 94, self
				)
			#end:case
			case 1:
				global0._send(
					'setPri:', -1,
					'setScale:', Scaler, 100, 94, 189, 95,
					'setMotion:', DPath, 118, 107, 120, 111, 123, 121, self
				)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				global0._send('setHeading:', 0, self)
			#end:case
			case 4:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class seenVizierScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('hide:')
				proc913_1(72)
				kernel.ScriptID(220, 5)._send('setCycle:', End, self)
			#end:case
			case 1:
				self._send('setScript:', egoScr)
				ticks = 30
			#end:case
			case 2:
				kernel.ScriptID(220, 6)._send('init:', 'setMotion:', MoveTo, 105, 94, self)
			#end:case
			case 3:
				kernel.ScriptID(220, 6)._send(
					'setPri:', -1,
					'setScale:', Scaler, 100, 94, 189, 95,
					'setMotion:', DPath, 115, 107, 117, 111, 118, 115, self
				)
			#end:case
			case 4:
				kernel.ScriptID(220, 6)._send('setHeading:', 180, self)
			#end:case
			case 5:
				if script:
					state.post('--')
				#endif
				cycles = 2
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				global91._send('say:', 1, 0, 5, 1, self)
			#end:case
			case 8:
				global91._send('say:', 1, 0, 5, 2, self)
			#end:case
			case 9:
				kernel.ScriptID(220, 6)._send('setMotion:', MoveTo, 117, 111, self)
			#end:case
			case 10:
				cycles = 2
			#end:case
			case 11:
				global91._send('say:', 1, 0, 5, 3, self)
			#end:case
			case 12:
				kernel.ScriptID(220, 6)._send('setMotion:', DPath, 115, 107, 105, 94, self)
			#end:case
			case 13:
				kernel.ScriptID(220, 6)._send('cue:', self)
			#end:case
			case 14:
				kernel.ScriptID(220, 6)._send('dispose:')
				self._send('setScript:', kernel.ScriptID(220, 2), self)
			#end:case
			case 15:
				global91._send('say:', 1, 0, 5, 4, self)
			#end:case
			case 16:
				global0._send('reset:', 3)
				global1._send('handsOn:')
				kernel.ScriptID(220, 5)._send('stopUpd:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(221)
	#end:method

#end:class or instance

