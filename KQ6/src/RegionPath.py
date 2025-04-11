#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 918
import sci_sh
import Main
import Print
import Motion

class RegionPath(MoveTo):
	#property vars (may be empty)
	completed = 1
	currentRoom = 0
	value = -1
	endType = 1
	intermediate = 0
	initialized = 0
	savedOldStuff = 0
	theRegion = 0
	theOldBits = 0
	theOldSignal = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (argc >= 4):
			value = -1
			initialized = 0
			completed = 1
		#endif
		if completed:
			if argc:
				client = param1
				if (argc >= 2):
					caller = param2
					if (argc >= 3):
						intermediate = param3
					#endif
				#endif
			#endif
			if (not initialized):
				if (not savedOldStuff):
					theOldBits = (client illegalBits:)
					theOldSignal = (client signal:)
					savedOldStuff = 1
				#endif
				if (endType & 0x0002):
					(self findPathend: next:)
					(client posn: x y)
				else:
					(self value: 0 nextRoom:)
				#endif
				initialized = 1
				(client illegalBits: 0 ignoreActors: ignoreHorizon:)
			#endif
			completed = 0
			(self next:)
		#endif
		(super init:)
		(self curRoomCheck:)
	#end:method

	@classmethod
	def curRoomCheck():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (client z:)
		if (currentRoom == global11):
			(client
				z:
					if (temp0 >= 1000):
						(temp0 - 1000)
					else:
						temp0
					#endif
				illegalBits: theOldBits
				signal: theOldSignal
			)
		else:
			(client
				z:
					if (temp0 < 1000):
						(temp0 + 1000)
					else:
						temp0
					#endif
				illegalBits: 0
				ignoreActors: 1
				ignoreHorizon:
			)
		#endif
	#end:method

	@classmethod
	def next():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		x = (self at: (self nextValue: 1))
		y = (self at: (value + 1))
	#end:method

	@classmethod
	def nextRoom():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (endType & 0x0002):
			(self findPrevroom:)
		else:
			currentRoom = (self at: (value + 1))
		#endif
		(self next: curRoomCheck:)
		(client posn: x y)
	#end:method

	@classmethod
	def moveDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		completed = 1
		if (self atEnd:):
			(self value: -1 initialized: 0)
			if (endType & 0x0001):
				(self init:)
			else:
				(super moveDone:)
			#endif
		else:
			if intermediate:
				(intermediate cue: (value / 2))
			#endif
			if ((self at: (self nextValue:)) == 32767):
				(self next: nextRoom:)
			#endif
			(self init:)
		#endif
	#end:method

	@classmethod
	def atEnd():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(or
				((endType & 0x0002) and ((value - 2) <= 0))
				((self at: (value + 2)) == -32768)
			)
		)
	#end:method

	@classmethod
	def at():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(proc921_1 r"""%s needs an 'at:' method.""" name)
		return 0
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if theRegion:
			if (not ((ScriptID theRegion) keep:)):
				(super dispose:)
			#endif
		else:
			(proc921_1 r"""%s theRegion: not defined.""" name)
		#endif
	#end:method

	@classmethod
	def nextValue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (((not (endType & 0x0002)) * 4) - 2)
		if argc:
			return (value += temp0)
		else:
			return (value + temp0)
		#endif
	#end:method

	@classmethod
	def findPathend():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		value = 0
		while ((self at: value) != -32768): # inline for
			if ((self at: value) == 32767):
				currentRoom = (self at: (value + 1))
			#endif
			# for:reinit
			value++
		#end:loop
	#end:method

	@classmethod
	def findPrevroom():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 0
		while (temp0 < value): # inline for
			if ((self at: temp0) == 32767):
				currentRoom = (self at: (temp0 + 1))
			#endif
			# for:reinit
			temp0++
		#end:loop
	#end:method

#end:class or instance

