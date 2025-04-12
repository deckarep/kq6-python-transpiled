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
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global1 handsOff:)
		start = 1
		(super init: &rest)
	#end:method

	@classmethod
	def changeState():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp5 = 0
		value = (self at: state)
		state.post('++')
		match value
			case -4095:
				temp0 = (self getValue:)
				temp1 = (self getValue:)
				(global0 setCycle: CT temp0 temp1 self)
			#end:case
			case -4092:
				(global0 setCycle: Beg self)
			#end:case
			case -4094:
				(global0 setCycle: End self)
			#end:case
			case -4088:
				(global0 setCycle: Fwd)
			#end:case
			case -4080:
				(global0 setCycle: Rev)
			#end:case
			case -4064:
				cycles = (self getValue:)
			#end:case
			case -4032:
				seconds = (self getValue:)
			#end:case
			case -3968:
				temp0 = (self getValue:)
				temp1 = (self getValue:)
				temp2 = (self getValue:)
				(self play: temp0 temp1 temp2)
			#end:case
			case -14:
				(global1 handsOn:)
				(self cue:)
			#end:case
			case -15:
				(global1 handsOff:)
				(self cue:)
			#end:case
			case -3840:
				if (temp0 = (self getValue:) == -1):
					temp0 = global11
				#endif
				temp1 = (self getValue:)
				temp2 = (self getValue:)
				temp3 = (self getValue:)
				temp4 = (self getValue:)
				(global91 say: temp1 temp2 temp3 temp4 self temp0)
			#end:case
			case -16:
				temp0 = (self getValue:)
				temp1 = (self getValue:)
				kernel.UnLoad(temp0, temp1)
				(self cue:)
			#end:case
			case -14:
				(global1 handsOn:)
				(self cue:)
			#end:case
			case -15:
				(global1 handsOff:)
				(self cue:)
			#end:case
			case -1:
				(self dispose:)
			#end:case
			else:
				state.post('--')
				(global0 view: (self getValue:) loop: (self getValue:))
				if (temp0 = (self getValue:) != -1):
					(global0 cel: temp0)
				#endif
				(global0 x: (self getValue:) y: (self getValue:))
				(self cue:)
			#end:else
		#end:match
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self changeState: state)
	#end:method

	@classmethod
	def getValue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		value = (self at: state)
		state.post('++')
		return value
	#end:method

	@classmethod
	def play():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		proc921_0(r"""Need play: method""")
		cycles = 1
	#end:method

	@classmethod
	def at():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		proc921_0(r"""Need at: method""")
		kernel.SetDebug()
		global4 = 1
	#end:method

#end:class or instance

