#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 92
import sci_sh
import kernel
import Main
import n913
import LoadMany
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	inkScript = 0,
)

@SCI.instance
class inkScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				proc913_1(151)
				cycles = 1
			#end:case
			case 1:
				(global91 say: 1 83 0 1 self 0)
			#end:case
			case 2:
				seconds = 2
			#end:case
			case 3:
				(global0
					normal: 0
					view: 906
					setCel: 0
					setLoop: 0
					cycleSpeed: 10
					setCycle: CT 4 1 self
				)
			#end:case
			case 4:
				(global91 say: 1 83 0 2 self 0)
			#end:case
			case 5:
				(global0 setCycle: End self)
			#end:case
			case 6:
				(global91 say: 1 83 0 3 self 0)
			#end:case
			case 7:
				(global0 setCel: 0 setLoop: 1)
				seconds = 4
			#end:case
			case 8:
				(global91 say: 1 83 0 4 self 0)
			#end:case
			case 9:
				seconds = 2
			#end:case
			case 10:
				(global0 setCycle: End self)
			#end:case
			case 11:
				(global91 say: 1 83 0 5 self 0)
			#end:case
			case 12:
				proc913_1(116)
				(global1 handsOn:)
				(global0 reset: 2)
				(self dispose:)
				proc958_0(0, 92)
			#end:case
		#end:match
	#end:method

#end:class or instance

