#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 13
import sci_sh
import kernel
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	windScr = 0,
)

class windScr(Script):
	#property vars (may be empty)
	curWindSpeed = 0
	minWindSpeed = 0
	intervalDuration = 0
	loopDir = 1
	
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				seconds = kernel.Random(2, 10)
			#end:case
			case 1:
				(client startUpd:)
				cycles = 1
			#end:case
			case 2:
				minWindSpeed = kernel.Random(3, 12)
				curWindSpeed = minWindSpeed
				intervalDuration = kernel.Random(10, 30)
				(client cycleSpeed: curWindSpeed setCycle: Fwd)
				(self cue:)
			#end:case
			case 3:
				cycles = intervalDuration
			#end:case
			case 4:
				if loopDir:
					curWindSpeed.post('--')
					if (curWindSpeed == -1):
						loopDir = 0
					else:
						(client cycleSpeed: curWindSpeed)
					#endif
				else:
					curWindSpeed.post('++')
					if (curWindSpeed == (minWindSpeed + 1)):
						loopDir = 1
					else:
						(client cycleSpeed: curWindSpeed)
					#endif
				#endif
				(self cue:)
			#end:case
			case 5:
				cycles = intervalDuration
			#end:case
			case 6:
				(client setCycle: 0)
				(client stopUpd:)
				state = -1
				cycles = 2
			#end:case
		#end:match
	#end:method

#end:class or instance

