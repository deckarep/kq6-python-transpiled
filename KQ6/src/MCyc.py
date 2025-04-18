#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 942
import sci_sh
import kernel
import Main
import Motion
import System

class MCyc(Cycle):
	#property vars (may be empty)
	value = 0
	points = 0
	size = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		client = param1
		points = param2
		if (argc >= 3):
			(cond
				case (argc >= 4):
					cycleDir = param4
					caller = param3
				#end:case
				case kernel.IsObject(param3):
					caller = param3
				#end:case
				else:
					cycleDir = param3
				#end:else
			)
		#endif
		size = 0
		while (proc999_6(points, size) != -32768): # inline for
		#end:loop
		if (cycleDir == 1):
			value = 0
		else:
			value = (size - 4)
		#endif
		super._send('init:')
	#end:method

	@classmethod
	def doit():
		if (kernel.Abs((global88 - cycleCnt)) >= client._send('cycleSpeed:')):
			cycleCnt = global88
			self._send('nextCel:')
		#endif
	#end:method

	@classmethod
	def nextCel():
		client._send(
			'loop:', proc999_6(points, value),
			'cel:', proc999_6(points, (value + 1)),
			'x:', proc999_6(points, (value + 2)),
			'y:', proc999_6(points, (value + 3))
		)
		(value += (cycleDir * 4))
		if 
			(or
				((cycleDir == 1) and (value >= size))
				((cycleDir == -1) and (value < 0))
			)
			self._send('cycleDone:')
		#endif
	#end:method

	@classmethod
	def cycleDone():
		completed = 1
		value = 0
		if caller:
			global37 = 1
		else:
			self._send('motionCue:')
		#endif
	#end:method

#end:class or instance

