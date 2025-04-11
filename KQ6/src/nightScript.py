#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 93
import sci_sh
import Main
import LoadMany
import Sound
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	nightScript = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.instance
class nightScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff: killSound: 1)
				(localMusic4 number: 930 loop: 1 play:)
				local1 = (global0 cel:)
				(global0
					normal: 0
					view: 883
					ignoreActors: 1
					illegalBits: 0
					ignoreHorizon: 1
					cycleSpeed: 10
				)
				if (proc999_5 (global0 cel:) 0 2 4 6):
					local0 = 1
					(global0 setLoop: 1)
				else:
					(global0 setLoop: 0)
				#endif
				(global0 setCycle: End self)
			#end:case
			case 1:
				(global91 say: 1 37 0 0 self 0)
			#end:case
			case 2:
				(localMusic4 number: 931 loop: 1 play: self)
				if local0:
					(global0 setLoop: 7 setCycle: Fwd)
				else:
					(global0 setLoop: 6 setCycle: Fwd)
				#endif
			#end:case
			case 3:
				(global1 killSound: 0)
				cycles = 2
			#end:case
			case 4:
				(global1 handsOn:)
				(localMusic4 stop: dispose:)
				(global0 reset: local1)
				cycles = 1
			#end:case
			case 5:
				(self dispose:)
				(proc958_0 0 93)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class localMusic4(Sound):
	#property vars (may be empty)
#end:class or instance

