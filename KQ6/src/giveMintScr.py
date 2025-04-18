#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 278
import sci_sh
import kernel
import Main
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	giveMintScr = 0,
	genieSpyScr = 1,
	offerItemScr = 2,
)

@SCI.instance
class genieLookScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				kernel.ScriptID(271, 0)._send('setScript:', 0)
				if (kernel.ScriptID(271, 0)._send('loop:') and (kernel.ScriptID(271, 0)._send('cel:') > 3)):
					state.post('++')
					kernel.ScriptID(271, 0)._send('setCycle:', End, self)
				else:
					kernel.ScriptID(271, 0)._send('loop:', 1, 'cel:', 0)
					ticks = 10
				#endif
			#end:case
			case 1:
				kernel.ScriptID(271, 0)._send('cel:', 4, 'setCycle:', End, self)
			#end:case
			case 2:
				client._send('cue:')
			#end:case
			case 3:
				kernel.ScriptID(271, 0)._send('setCycle:', Beg, self)
			#end:case
			case 4:
				kernel.ScriptID(271, 0)._send('setScript:', kernel.ScriptID(271, 1))
				if caller:
					caller._send('cycles:', 2)
					caller = 0
				#endif
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genieSpyScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				kernel.ScriptID(271, 0)._send(
					'setScript:', 0,
					'setMotion:', MoveTo, (kernel.ScriptID(271, 0)._send('x:') + 10), kernel.ScriptID(271, 0)._send(
							'y:'
						), self
				)
			#end:case
			case 1:
				kernel.ScriptID(271, 0)._send('loop:', 1, 'cel:', 0)
				start = 2
				self._send('dispose:')
			#end:case
			case 2:
				kernel.ScriptID(271, 0)._send(
					'setMotion:', MoveTo, (kernel.ScriptID(271, 0)._send('x:') - 10), kernel.ScriptID(271, 0)._send(
							'y:'
						), self
				)
			#end:case
			case 3:
				kernel.ScriptID(271, 0)._send('loop:', 1, 'cel:', 0, 'setScript:', kernel.ScriptID(271, 1))
				start = 0
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		if (start == 0):
			kernel.DisposeScript(278)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class giveMintScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('put:', 23, global11)
				global1._send('handsOff:')
				self._send('setScript:', genieLookScr, self)
			#end:case
			case 1:
				global91._send('say:', 9, 63, 0, 1, self, 270)
			#end:case
			case 2:
				global91._send('say:', 9, 63, 0, 2, self, 270)
			#end:case
			case 3:
				global0._send(
					'normal:', 0,
					'setSpeed:', 6,
					'view:', 2832,
					'loop:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 4:
				ticks = 15
			#end:case
			case 5:
				kernel.ScriptID(271, 0)._send(
					'view:', 2834,
					'loop:', 0,
					'cel:', 0,
					'posn:', 185, 118,
					'setCycle:', End, self
				)
			#end:case
			case 6:
				ticks = 30
			#end:case
			case 7:
				global91._send('say:', 9, 63, 0, 3, self, 270)
			#end:case
			case 8:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 9:
				global0._send('reset:', 7)
				kernel.ScriptID(271, 0)._send(
					'loop:', 1,
					'cel:', 0,
					'posn:', 185, 118,
					'cycleSpeed:', 14,
					'setCycle:', End, self
				)
			#end:case
			case 10:
				ticks = 15
			#end:case
			case 11:
				kernel.ScriptID(271, 0)._send('cel:', 0, 'setCycle:', End, self)
			#end:case
			case 12:
				ticks = 15
			#end:case
			case 13:
				kernel.ScriptID(271, 0)._send('setCycle:', Beg, self)
			#end:case
			case 14:
				ticks = 15
			#end:case
			case 15:
				kernel.ScriptID(271, 0)._send('setCycle:', Beg, self)
			#end:case
			case 16:
				ticks = 45
			#end:case
			case 17:
				global91._send('say:', 9, 63, 0, 4, self, 270)
			#end:case
			case 18:
				kernel.ScriptID(271, 0)._send('view:', 275, 'loop:', 1, 'cel:', 0, 'posn:', 179, 117)
				script._send('cue:')
			#end:case
			case 19:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(278)
	#end:method

#end:class or instance

@SCI.instance
class offerItemScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				self._send('setScript:', genieLookScr, self)
			#end:case
			case 1:
				global91._send('say:', 9, 0, 0, 0, self)
			#end:case
			case 2:
				script._send('cue:')
			#end:case
			case 3:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(278)
	#end:method

#end:class or instance

