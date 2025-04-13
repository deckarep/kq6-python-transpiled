#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 964
import sci_sh
import kernel
import Motion
import System

class DPath(Motion):
	#property vars (may be empty)
	points = 0
	value = 0
	
	@classmethod
	def init(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		points = (points or List._send('new:'))
		if argc:
			client = param1
			temp0 = 0
			while (temp0 <= (argc - 3)): # inline for
				points._send('add:', param2[temp0], param2[temp0.post('++')])
				# for:reinit
				temp0.post('++')
			#end:loop
			if (temp0 <= (argc - 2)):
				caller = param2[temp0]
			#endif
		#endif
		(points._send('contains:', -32768) or points._send('add:', -32768))
		self._send('setTarget:')
		super._send('init:')
		if (not argc):
			self._send('doit:')
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if kernel.IsObject(points):
			points._send('dispose:')
		#endif
		super._send('dispose:')
	#end:method

	@classmethod
	def setTarget():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (points._send('at:', value) != -32768):
			x = points._send('at:', value)
			y = points._send('at:', value.post('++'))
			value.post('++')
		#endif
	#end:method

	@classmethod
	def moveDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (points._send('at:', value) == -32768):
			super._send('moveDone:')
		else:
			self._send('init:')
		#endif
	#end:method

#end:class or instance

