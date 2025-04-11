#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 973
import sci_sh
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
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = client
		client = 0
		if (IsObject temp0):
			if (temp0 respondsTo: #timer):
				(temp0 timer: 0)
			#endif
			if (temp0 respondsTo: #cue):
				(temp0 cue:)
			#endif
		#endif
	#end:method

	@classmethod
	def new():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			if (self == Timer):
				(super new:)
			else:
				self
			#endif
		)
	#end:method

	@classmethod
	def init(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		client = param1
		(global7 add: self)
		if (param1 respondsTo: #timer):
			if (IsObject (param1 timer:)):
				((param1 timer:) dispose:)
			#endif
			(param1 timer: self)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (cycleCnt != -1):
				if (not cycleCnt--):
					(localproc_0)
				#endif
			#end:case
			case (seconds != -1):
				if (lastTime != temp0 = (GetTime 1)):
					lastTime = temp0
					if (not seconds--):
						(localproc_0)
					#endif
				#endif
			#end:case
			case ((global88 - ticks) > 0):
				(localproc_0)
			#end:case
		)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((IsObject client) and (client respondsTo: #timer)):
			(client timer: 0)
		#endif
		client = 0
	#end:method

	@classmethod
	def delete():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (client == 0):
			(global7 delete: self)
			(super dispose:)
		#endif
	#end:method

	@classmethod
	def setCycle(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(= temp0
			if (-info- & 0x8000):
				(self new:)
			else:
				self
			#endif
		)
		(temp0 init: param1 cycleCnt: param2)
		return temp0
	#end:method

	@classmethod
	def set(param1 = None, param2 = None, param3 = None, param4 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

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
				(self new:)
			else:
				self
			#endif
		)
		(temp0 init: param1 cycleCnt: temp1)
		return temp0
	#end:method

	@classmethod
	def setReal(param1 = None, param2 = None, param3 = None, param4 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp1 = param2
		if (argc > 2):
			(temp1 += (param3 * 60))
		#endif
		if (argc > 3):
			(temp1 += (param4 * 3600))
		#endif
		(= temp0
			if (-info- & 0x8000):
				(self new:)
			else:
				self
			#endif
		)
		(temp0 init: param1 seconds: temp1)
		return temp0
	#end:method

	@classmethod
	def setTicks(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(= temp0
			if (-info- & 0x8000):
				(self new:)
			else:
				self
			#endif
		)
		(temp0 ticks: (global88 + param1) init: param2)
		return temp0
	#end:method

#end:class or instance

class TO(Obj):
	#property vars (may be empty)
	timeLeft = 0
	
	@classmethod
	def set(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		timeLeft = param1
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if timeLeft:
			timeLeft--
		#endif
	#end:method

#end:class or instance

