#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 969
import sci_sh
import kernel
import Motion

class Rev(Cycle):
	#property vars (may be empty)
	cycleDir = -1
	
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (temp0 = self._send('nextCel:') < 0):
			self._send('cycleDone:')
		else:
			client._send('cel:', temp0)
		#endif
	#end:method

	@classmethod
	def cycleDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		client._send('cel:', client._send('lastCel:'))
	#end:method

#end:class or instance

