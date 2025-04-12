#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 929
import sci_sh
import kernel
import Main
import Timer
import Motion
import System

class Sync(Obj):
	#property vars (may be empty)
	syncTime = -1
	syncCue = -1
	prevCue = -1
	syncNum = -1
	
	@classmethod
	def syncStart(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.DoSync(0, self, param1, param2, param3, param4, param5)
		if (syncCue != -1):
			prevCue = syncCue
			syncTime = 0
		#endif
	#end:method

	@classmethod
	def syncCheck():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				(syncCue != -1)
				((u<= syncTime global81) or (syncTime <= kernel.DoAudio(6)))
			)
			if ((0xfff0 & syncCue) == 0):
				prevCue = (| (prevCue & 0xfff0) syncCue)
			else:
				prevCue = syncCue
			#endif
			kernel.DoSync(1, self)
		#endif
	#end:method

	@classmethod
	def syncStop():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		prevCue = -1
		kernel.DoSync(2)
	#end:method

#end:class or instance

class ScriptSync(Obj):
	#property vars (may be empty)
	prevSignal = -1
	playing = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if global82:
			(self cue:)
		#endif
		(global82 = (Sync new:)
			init:
			syncStart: param1 param2 param3 param4 param5
		)
		if ((global82 prevCue:) != -1):
			playing = 1
			(global6 add: self)
		#endif
		(Timer setTicks: self kernel.DoAudio(1, param1, param2, param3, param4, param5))
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((global82 prevCue:) != -1):
			while True: #repeat
				if ((global82 prevCue:) == -1):
					(break)
				#endif
				temp0 = (global82 syncTime:)
				(global82 syncCheck:)
				if (temp0 == (global82 syncTime:)):
					(break)
				#endif
			#end:loop
			prevSignal = (global82 prevCue:)
		#endif
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.Animate((global5 elements:), 0)
		playing = 0
		prevSignal = 32767
		(global6 delete: self)
		if global82:
			(global82 syncStop: dispose:)
			global82 = 0
		#endif
	#end:method

#end:class or instance

class MouthSync(Cycle):
	#property vars (may be empty)
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, param6 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: param1)
		if kernel.IsObject(global82):
			(global82 syncStop: dispose:)
		#endif
		(global82 = (Sync new:) syncStart: param2 param3 param4 param5 param6)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super doit:)
		if ((global82 prevCue:) != -1):
			temp2 = (global82 syncTime:)
			temp3 = 0
			while True: #repeat
				temp1 = (global82 syncTime:)
				(global82 syncCheck:)
				if (temp1 == (global82 syncTime:)):
					(break)
				#endif
			#end:loop
			if 
				(and
					(temp2 != (global82 syncTime:))
					((client cel:) != temp0 = (0x000f & (global82 prevCue:)))
				)
				(client cel: temp0)
			#endif
		else:
			completed = 1
			(self cycleDone:)
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super dispose:)
		if global82:
			(global82 dispose:)
			global82 = 0
		#endif
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if global82:
			(global82 syncStop: dispose:)
			global82 = 0
			if caller:
				(caller cue:)
				caller = 0
			#endif
		#endif
	#end:method

#end:class or instance

