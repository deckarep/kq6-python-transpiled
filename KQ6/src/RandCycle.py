#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 941
import sci_sh
import kernel
import Main
import Motion

class RandCycle(Cycle):
	#property vars (may be empty)
	count = -1
	reset = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', param1)
		if (argc >= 4):
			reset = param4
		#endif
		if reset:
			client._send('cel:', 0)
		#endif
		cycleCnt = kernel.GetTime()
		if (argc >= 2):
			if (param2 != -1):
				count = (kernel.GetTime() + param2)
			else:
				count = -1
			#endif
			if (argc >= 3):
				caller = param3
			#endif
		else:
			count = -1
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((count > temp0 = kernel.GetTime()) or (count == -1)):
			if ((temp0 - cycleCnt) > client._send('cycleSpeed:')):
				client._send('cel:', self._send('nextCel:'))
				cycleCnt = kernel.GetTime()
			#endif
		else:
			if reset:
				client._send('cel:', 0)
			#endif
			self._send('cycleDone:')
		#endif
	#end:method

	@classmethod
	def nextCel():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			if (kernel.NumCels(client) != 1):
				while (temp0 = kernel.Random(0, client._send('lastCel:')) == client._send('cel:')):

				#end:loop
				temp0
			#endif
		)
	#end:method

	@classmethod
	def cycleDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		completed = 1
		if caller:
			global37 = 1
		else:
			self._send('motionCue:')
		#endif
	#end:method

#end:class or instance

class RTRandCycle(RandCycle):
	#property vars (may be empty)
#end:class or instance

