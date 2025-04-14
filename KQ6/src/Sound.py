#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 989
import sci_sh
import kernel
import Main
import System

class Sound(Obj):
	#property vars (may be empty)
	nodePtr = 0
	handle = 0
	flags = 0
	number = 0
	vol = 127
	priority = 0
	loop = 1
	signal = 0
	prevSignal = 0
	dataInc = 0
	min = 0
	sec = 0
	frame = 0
	client = 0
	owner = 0
	
	@classmethod
	def new(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('new:')._send('owner:', (param1 if argc else 0), 'yourself:')
	#end:method

	@classmethod
	def init():
		prevSignal = signal = 0
		global8._send('add:', self)
		kernel.DoSound(6, self)
	#end:method

	@classmethod
	def play(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = argc
		if (argc and kernel.IsObject(param1[(argc - 1)])):
			client = param1[temp0 = (argc - 1)]
		else:
			client = 0
		#endif
		if (not global8._send('contains:', self)):
			self._send('init:')
		#endif
		if (not loop):
			loop = 1
		#endif
		if temp0:
			vol = param1
		else:
			vol = 127
		#endif
		kernel.DoSound(8, self, 0)
	#end:method

	@classmethod
	def stop():
		if handle:
			kernel.DoSound(17, self)
			kernel.DoSound(9, self)
		#endif
	#end:method

	@classmethod
	def pause(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not argc):
			param1 = 1
		#endif
		kernel.DoSound(10, (self if self._send('isMemberOf:', Sound) else 0), param1)
	#end:method

	@classmethod
	def hold(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not argc):
			param1 = 1
		#endif
		kernel.DoSound(12, self, param1)
	#end:method

	@classmethod
	def release():
		kernel.DoSound(12, self, 0)
	#end:method

	@classmethod
	def fade(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = argc
		if (argc and kernel.IsObject(param1[(argc - 1)])):
			client = param1[temp0 = (argc - 1)]
		#endif
		if temp0:
			kernel.DoSound(11, self, param1, param2, param3, param4)
		else:
			kernel.DoSound(11, self, 0, 25, 10, 1)
		#endif
	#end:method

	@classmethod
	def mute(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not argc):
			temp1 = 1
		else:
			temp1 = param1
		#endif
		if (argc < 2):
			temp0 = 1
			while (temp0 < 17): # inline for
				kernel.DoSound(18, self, temp0, 176, 78, temp1)
				# for:reinit
				temp0.post('++')
			#end:loop
		else:
			kernel.DoSound(18, self, param2, 176, 78, temp1)
		#endif
	#end:method

	@classmethod
	def setVol(param1 = None, *rest):
		kernel.DoSound(14, self, param1)
	#end:method

	@classmethod
	def setPri(param1 = None, *rest):
		kernel.DoSound(15, self, param1)
	#end:method

	@classmethod
	def setLoop(param1 = None, *rest):
		kernel.DoSound(16, self, param1)
	#end:method

	@classmethod
	def send(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
		if (<= 1 param1 15):
			if (param2 < 128):
				kernel.DoSound(18, self, param1, 176, param2, param3)
			else:
				kernel.DoSound(18, self, param1, param2, param3, param4)
			#endif
		#endif
	#end:method

	@classmethod
	def check():
		if handle:
			kernel.DoSound(17, self)
		#endif
		if signal:
			prevSignal = signal
			signal = 0
			if kernel.IsObject(client):
				client._send('cue:', self)
			#endif
		#endif
	#end:method

	@classmethod
	def clean(param1 = None, *rest):
		if ((not owner) or (owner == param1)):
			self._send('dispose:')
		#endif
	#end:method

	@classmethod
	def dispose():
		global8._send('delete:', self)
		if nodePtr:
			kernel.DoSound(7, self)
			nodePtr = 0
		#endif
		super._send('dispose:')
	#end:method

	@classmethod
	def playBed(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = argc
		if (argc and kernel.IsObject(param1[(argc - 1)])):
			client = param1[temp0 = (argc - 1)]
		else:
			client = 0
		#endif
		self._send('init:')
		if (not loop):
			loop = 1
		#endif
		if temp0:
			vol = param1
		else:
			vol = 127
		#endif
		kernel.DoSound(8, self, 1)
	#end:method

	@classmethod
	def changeState():
		kernel.DoSound(20, self)
	#end:method

#end:class or instance

