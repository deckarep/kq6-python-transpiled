#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 984
import sci_sh
import kernel
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
	def init(param1 = None, param2 = None, param3 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

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
					theOldBits = client._send('illegalBits:')
					theOldSignal = client._send('signal:')
					savedOldStuff = 1
				#endif
				if (endType & 0x0002):
					self._send('findPathend:', 'next:')
					client._send('posn:', x, y)
				else:
					self._send('value:', 0, 'nextRoom:')
				#endif
				initialized = 1
				client._send('illegalBits:', 0, 'ignoreActors:', 'ignoreHorizon:')
			#endif
			completed = 0
			self._send('next:')
		#endif
		super._send('init:')
		self._send('curRoomCheck:')
	#end:method

	@classmethod
	def curRoomCheck():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = client._send('z:')
		if (currentRoom == global11):
			client._send(
				'z:', if (temp0 >= 1000):
						(temp0 - 1000)
					else:
						temp0
					#endif,
				'illegalBits:', theOldBits,
				'signal:', theOldSignal
			)
		else:
			client._send(
				'z:', if (temp0 < 1000):
						(temp0 + 1000)
					else:
						temp0
					#endif,
				'illegalBits:', 0,
				'ignoreActors:', 1,
				'ignoreHorizon:'
			)
		#endif
	#end:method

	@classmethod
	def next():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		x = self._send('at:', self._send('nextValue:', 1))
		y = self._send('at:', (value + 1))
	#end:method

	@classmethod
	def nextRoom():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (endType & 0x0002):
			self._send('findPrevroom:')
		else:
			currentRoom = self._send('at:', (value + 1))
		#endif
		self._send('next:', 'curRoomCheck:')
		client._send('posn:', x, y)
	#end:method

	@classmethod
	def moveDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		completed = 1
		if self._send('atEnd:'):
			self._send('value:', -1, 'initialized:', 0)
			if (endType & 0x0001):
				self._send('init:')
			else:
				super._send('moveDone:')
			#endif
		else:
			if intermediate:
				intermediate._send('cue:', (value / 2))
			#endif
			if (self._send('at:', self._send('nextValue:')) == 32767):
				self._send('next:', 'nextRoom:')
			#endif
			self._send('init:')
		#endif
	#end:method

	@classmethod
	def atEnd():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(or
				((endType & 0x0002) and ((value - 2) <= 0))
				(self._send('at:', (value + 2)) == -32768)
			)
		)
	#end:method

	@classmethod
	def at():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		proc921_1(r"""%s needs an 'at:' method.""", name)
		return 0
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if theRegion:
			if (not kernel.ScriptID(theRegion)._send('keep:')):
				super._send('dispose:')
			#endif
		else:
			proc921_1(r"""%s theRegion: not defined.""", name)
		#endif
	#end:method

	@classmethod
	def nextValue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		value = 0
		while (self._send('at:', value) != -32768): # inline for
			if (self._send('at:', value) == 32767):
				currentRoom = self._send('at:', (value + 1))
			#endif
			# for:reinit
			value.post('++')
		#end:loop
	#end:method

	@classmethod
	def findPrevroom():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 0
		while (temp0 < value): # inline for
			if (self._send('at:', temp0) == 32767):
				currentRoom = self._send('at:', (temp0 + 1))
			#endif
			# for:reinit
			temp0.post('++')
		#end:loop
	#end:method

#end:class or instance

