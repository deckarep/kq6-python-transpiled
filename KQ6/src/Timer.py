#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 973
import sci_sh
import kernel
import Main
import System

class Timer(Obj):
	#property vars (may be empty)
	cycleCnt = -1
	seconds = -1
	ticks = -1
	lastTime = -1
	client = 0
	
	(procedure (localproc_0):
		temp0 = client
		client = 0
		if kernel.IsObject(temp0):
			if temp0._send('respondsTo:', #timer):
				temp0._send('timer:', 0)
			#endif
			if temp0._send('respondsTo:', #cue):
				temp0._send('cue:')
			#endif
		#endif
	#end:method

	@classmethod
	def new():
		(return
			if (self == Timer):
				super._send('new:')
			else:
				self
			#endif
		)
	#end:method

	@classmethod
	def init(param1 = None, *rest):
		client = param1
		global7._send('add:', self)
		if param1._send('respondsTo:', #timer):
			if kernel.IsObject(param1._send('timer:')):
				param1._send('timer:')._send('dispose:')
			#endif
			param1._send('timer:', self)
		#endif
	#end:method

	@classmethod
	def doit():
		(cond
			case (cycleCnt != -1):
				if (not cycleCnt.post('--')):
					localproc_0()
				#endif
			#end:case
			case (seconds != -1):
				if (lastTime != temp0 = kernel.GetTime(1)):
					lastTime = temp0
					if (not seconds.post('--')):
						localproc_0()
					#endif
				#endif
			#end:case
			case ((global88 - ticks) > 0):
				localproc_0()
			#end:case
		)
	#end:method

	@classmethod
	def dispose():
		if (kernel.IsObject(client) and client._send('respondsTo:', #timer)):
			client._send('timer:', 0)
		#endif
		client = 0
	#end:method

	@classmethod
	def delete():
		if (client == 0):
			global7._send('delete:', self)
			super._send('dispose:')
		#endif
	#end:method

	@classmethod
	def setCycle(param1 = None, param2 = None, *rest):
		(= temp0
			if (-info- & 0x8000):
				self._send('new:')
			else:
				self
			#endif
		)
		temp0._send('init:', param1, 'cycleCnt:', param2)
		return temp0
	#end:method

	@classmethod
	def set(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (temp2 = 6 == 0):
			temp2 = 1
		#endif
		temp1 = ((param2 * 60) / temp2)
		if (argc > 2):
			(temp1 += ((param3 * 3600) / temp2))
		#endif
		if (argc > 3):
			(temp1 += (((param4 * 3600) / temp2) * 60))
		#endif
		(= temp0
			if (-info- & 0x8000):
				self._send('new:')
			else:
				self
			#endif
		)
		temp0._send('init:', param1, 'cycleCnt:', temp1)
		return temp0
	#end:method

	@classmethod
	def setReal(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp1 = param2
		if (argc > 2):
			(temp1 += (param3 * 60))
		#endif
		if (argc > 3):
			(temp1 += (param4 * 3600))
		#endif
		(= temp0
			if (-info- & 0x8000):
				self._send('new:')
			else:
				self
			#endif
		)
		temp0._send('init:', param1, 'seconds:', temp1)
		return temp0
	#end:method

	@classmethod
	def setTicks(param1 = None, param2 = None, *rest):
		(= temp0
			if (-info- & 0x8000):
				self._send('new:')
			else:
				self
			#endif
		)
		temp0._send('ticks:', (global88 + param1), 'init:', param2)
		return temp0
	#end:method

#end:class or instance

class TO(Obj):
	#property vars (may be empty)
	timeLeft = 0
	
	@classmethod
	def set(param1 = None, *rest):
		timeLeft = param1
	#end:method

	@classmethod
	def doit():
		if timeLeft:
			timeLeft.post('--')
		#endif
	#end:method

#end:class or instance

