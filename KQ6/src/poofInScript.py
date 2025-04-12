#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 89
import sci_sh
import kernel
import Main
import Scaler
import Sound
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	poofInScript = 0,
)

@SCI.instance
class poofInScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				cycles = 15
			#end:case
			case 1:
				(global1 handsOff:)
				if (not (global0 x:)):
					(global0 posn: 200 127)
				#endif
				(localMusic2 loop: 1 number: 947 play:)
				(global0
					view: 207
					init:
					cycleSpeed: 10
					normal: 0
					setLoop: 1
					cel: 0
					setCycle: End self
				)
			#end:case
			case 2:
				(global0
					normal: 0
					cycleSpeed: 10
					view: 207
					setLoop: 2
					cel: 0
					lastCel:
					setCycle: Beg self
				)
			#end:case
			case 3:
				(global1 handsOn:)
				(global0 reset:)
				(localMusic2 stop: dispose:)
				(self dispose:)
				if (global11 == 450):
					(global0 setScale: Scaler 100 30 126 70)
				#endif
				kernel.DisposeScript(89)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class localMusic2(Sound):
	#property vars (may be empty)
#end:class or instance

