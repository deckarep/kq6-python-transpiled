#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 938
import sci_sh
import kernel
import Motion

class ROsc(Cycle):
	#property vars (may be empty)
	cycles = -1
	firstC = 0
	lastC = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (argc >= 2):
			cycles = param2
		#endif
		if (argc >= 5):
			caller = param5
		#endif
		super._send('init:', param1)
		if (argc >= 3):
			firstC = param3
			if (argc >= 4):
				if param4:
					lastC = param4
				else:
					lastC = client._send('lastCel:')
				#endif
			else:
				lastC = client._send('lastCel:')
			#endif
		#endif
		client._send('cel:', firstC)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((temp0 = self._send('nextCel:') > lastC) or (temp0 < firstC)):
			cycleDir = -cycleDir
			self._send('cycleDone:')
		else:
			client._send('cel:', temp0)
		#endif
	#end:method

	@classmethod
	def cycleDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if cycles:
			client._send('cel:', self._send('nextCel:'))
			if (cycles > 0):
				cycles.post('--')
			#endif
		else:
			completed = 1
			self._send('motionCue:')
		#endif
	#end:method

#end:class or instance

