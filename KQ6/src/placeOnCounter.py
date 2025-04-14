#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 287
import sci_sh
import kernel
import Main
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	placeOnCounter = 0,
	getFromCounter = 1,
)

@SCI.instance
class placeOnCounter(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send(
					'put:', match register
							case 0: 48#end:case
							case 3: 27#end:case
							case 1: 3#end:case
							case 2: 14#end:case
						#end:match, global11
				)
				self._send('setScript:', kernel.ScriptID(286, 2), 0, register)
			#end:case
			case 1:
				client._send('cue:')
			#end:case
			case 2:
				kernel.ScriptID(280, 2)._send(
					'posn:', 236, 116,
					'view:', 284,
					'loop:', 3,
					'cel:', 0,
					'cycleSpeed:', 9
				)
				ticks = 6
			#end:case
			case 3:
				kernel.ScriptID(280, 2)._send('setCycle:', CT, 1, 1, self)
			#end:case
			case 4:
				ticks = 6
			#end:case
			case 5:
				script._send('cue:')
				kernel.ScriptID(280, 2)._send(
					'setPri:', 14,
					'view:', (2842 if proc999_5(register, 3, 2) else 2843),
					'loop:', match register
							case 3: 0#end:case
							case 2: 1#end:case
							case 0: 0#end:case
							case 1: 1#end:case
						#end:match,
					'cel:', 0
				)
				ticks = 6
			#end:case
			case 6:
				kernel.ScriptID(280, 2)._send('setCycle:', CT, 3, 1, self)
			#end:case
			case 7:
				match register
					case 0:
						kernel.ScriptID(280, 5)._send('init:')
					#end:case
					case 2:
						kernel.ScriptID(280, 6)._send('init:')
					#end:case
					case 3:
						kernel.ScriptID(280, 4)._send('init:')
					#end:case
					case 1:
						kernel.ScriptID(280, 7)._send('init:')
					#end:case
				#end:match
				cycles = 2
			#end:case
			case 8:
				if (kernel.ScriptID(280, 2)._send('lastCel:') != kernel.ScriptID(280, 2)._send('cel:')):
					kernel.ScriptID(280, 2)._send('setCycle:', End, self)
				else:
					cycles = 2
				#endif
			#end:case
			case 9:
				ticks = 6
			#end:case
			case 10:
				kernel.ScriptID(280, 2)._send(
					'setPri:', -1,
					'posn:', 236, 127,
					'view:', 280,
					'loop:', 8,
					'cel:', 0,
					'cycleSpeed:', 6
				)
				cycles = 2
			#end:case
			case 11:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(287)
	#end:method

#end:class or instance

@SCI.instance
class getFromCounter(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				kernel.ScriptID(280, 2)._send(
					'view:', (2842 if proc999_5(register, 3, 2) else 2843),
					'posn:', 236, 116,
					'setPri:', 14,
					'loop:', match register
							case 3: 0#end:case
							case 2: 1#end:case
							case 0: 0#end:case
							case 1: 1#end:case
						#end:match,
					'cel:', 2
				)
				global0._send(
					'get:', match register
							case 0: 48#end:case
							case 3: 27#end:case
							case 1: 3#end:case
							case 2: 14#end:case
						#end:match
				)
				match register
					case 0:
						kernel.ScriptID(280, 5)._send('dispose:')
					#end:case
					case 2:
						kernel.ScriptID(280, 6)._send('dispose:')
					#end:case
					case 3:
						kernel.ScriptID(280, 4)._send('dispose:')
					#end:case
					case 1:
						kernel.ScriptID(280, 7)._send('dispose:')
					#end:case
				#end:match
				cycles = 3
			#end:case
			case 1:
				kernel.ScriptID(280, 2)._send('setCycle:', Beg, self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				self._send('setScript:', kernel.ScriptID(286, 2), self)
			#end:case
			case 4:
				script._send('register:', register, 'cue:')
				kernel.ScriptID(280, 2)._send(
					'view:', 284,
					'setPri:', -1,
					'loop:', 3,
					'cel:', 1,
					'setCycle:', Beg, self
				)
			#end:case
			case 5: 0#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				kernel.ScriptID(280, 2)._send('posn:', 236, 127, 'view:', 280, 'loop:', 8, 'cel:', 0)
				cycles = 2
			#end:case
			case 8:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(287)
	#end:method

#end:class or instance

