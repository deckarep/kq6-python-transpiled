#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 908
import sci_sh
import kernel
import Main
import LoadMany
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	eggScript = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


@SCI.instance
class eggScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91 say: 1 19 0 1 self 0)
			#end:case
			case 1:
				seconds = 3
			#end:case
			case 2:
				local0 = (global0 cel:)
				(global0
					normal: 0
					view: 907
					cel: 0
					setLoop: 0
					cycleSpeed: 10
					setCycle: End self
				)
			#end:case
			case 3:
				(global91 say: 1 19 0 2 self 0)
			#end:case
			case 4:
				(global91 say: 1 19 0 3 self 0)
			#end:case
			case 5:
				(global0 put: 10 reset: local0)
				(global1 handsOn:)
				(self dispose:)
				proc958_0(0, 908)
			#end:case
		#end:match
	#end:method

#end:class or instance

