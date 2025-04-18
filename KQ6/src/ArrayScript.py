#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 759
import sci_sh
import kernel
import Main
import Print
import Rev
import Motion
import System

class ArrayScript(Script):
	#property vars (may be empty)
	start = 1
	value = 0
	
	@classmethod
	def init():
		global1._send('handsOff:')
		start = 1
		super._send('init:', &rest)
	#end:method

	@classmethod
	def changeState():
		temp5 = 0
		value = self._send('at:', state)
		state.post('++')
		match value
			case -4095:
				temp0 = self._send('getValue:')
				temp1 = self._send('getValue:')
				global0._send('setCycle:', CT, temp0, temp1, self)
			#end:case
			case -4092:
				global0._send('setCycle:', Beg, self)
			#end:case
			case -4094:
				global0._send('setCycle:', End, self)
			#end:case
			case -4088:
				global0._send('setCycle:', Fwd)
			#end:case
			case -4080:
				global0._send('setCycle:', Rev)
			#end:case
			case -4064:
				cycles = self._send('getValue:')
			#end:case
			case -4032:
				seconds = self._send('getValue:')
			#end:case
			case -3968:
				temp0 = self._send('getValue:')
				temp1 = self._send('getValue:')
				temp2 = self._send('getValue:')
				self._send('play:', temp0, temp1, temp2)
			#end:case
			case -14:
				global1._send('handsOn:')
				self._send('cue:')
			#end:case
			case -15:
				global1._send('handsOff:')
				self._send('cue:')
			#end:case
			case -3840:
				if (temp0 = self._send('getValue:') == -1):
					temp0 = global11
				#endif
				temp1 = self._send('getValue:')
				temp2 = self._send('getValue:')
				temp3 = self._send('getValue:')
				temp4 = self._send('getValue:')
				global91._send('say:', temp1, temp2, temp3, temp4, self, temp0)
			#end:case
			case -16:
				temp0 = self._send('getValue:')
				temp1 = self._send('getValue:')
				kernel.UnLoad(temp0, temp1)
				self._send('cue:')
			#end:case
			case -14:
				global1._send('handsOn:')
				self._send('cue:')
			#end:case
			case -15:
				global1._send('handsOff:')
				self._send('cue:')
			#end:case
			case -1:
				self._send('dispose:')
			#end:case
			else:
				state.post('--')
				global0._send('view:', self._send('getValue:'), 'loop:', self._send('getValue:'))
				if (temp0 = self._send('getValue:') != -1):
					global0._send('cel:', temp0)
				#endif
				global0._send('x:', self._send('getValue:'), 'y:', self._send('getValue:'))
				self._send('cue:')
			#end:else
		#end:match
	#end:method

	@classmethod
	def cue():
		self._send('changeState:', state)
	#end:method

	@classmethod
	def getValue():
		value = self._send('at:', state)
		state.post('++')
		return value
	#end:method

	@classmethod
	def play():
		proc921_0(r"""Need play: method""")
		cycles = 1
	#end:method

	@classmethod
	def at():
		proc921_0(r"""Need at: method""")
		kernel.SetDebug()
		global4 = 1
	#end:method

#end:class or instance

