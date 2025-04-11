#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 95
import sci_sh
import kernel
import System

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


class Audio(Obj):
	#property vars (may be empty)
	number = 0
	loop = 1
	paused = 0
	doNotStop = 0
	stopped = 1
	
	@classmethod
	def play(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		local0 = 0
		(cond
			case kernel.DoAudio(2, number):
				stopped = 0
				if kernel.IsObject(param1):
					local0 = param1
				#endif
				(self check:)
			#end:case
			case (kernel.IsObject(param1) and (local0 = param1 != 0)):
				(local0 cue:)
			#end:case
		)
	#end:method

	@classmethod
	def stop():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		stopped = 1
		kernel.DoAudio(3)
	#end:method

	@classmethod
	def pause():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not paused):
			kernel.DoAudio(4)
			(self paused: 1)
		#endif
	#end:method

	@classmethod
	def resume():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if paused:
			kernel.DoAudio(5)
			(self paused: 0)
		#endif
	#end:method

	@classmethod
	def setLoop(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self loop: param1)
	#end:method

	@classmethod
	def setRate(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if argc:
			kernel.DoAudio(7, param1)
		#endif
	#end:method

	@classmethod
	def check():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (and (not stopped) (kernel.DoAudio(6) == -1) (loop == 1)):
			doNotStop = 0
			stopped = 1
			if (local0 != 0):
				temp0 = local0
				local0 = 0
				(temp0 cue:)
			#endif
		#endif
		if (and (not stopped) (kernel.DoAudio(6) == -1) ((loop > 1) or (loop == -1))):
			(self play:)
		#endif
	#end:method

#end:class or instance

