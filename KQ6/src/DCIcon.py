#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 967
import sci_sh
import kernel
import Dialog
import Motion

class DCIcon(DIcon):
	#property vars (may be empty)
	cycler = 0
	cycleSpeed = 6
	signal = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		cycler = Fwd._send('new:')._send('init:', self)
	#end:method

	@classmethod
	def cycle():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if cycler:
			temp0 = cel
			cycler._send('doit:')
			if (cel != temp0):
				self._send('draw:')
			#endif
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if cycler:
			cycler._send('dispose:')
		#endif
		super._send('dispose:')
	#end:method

	@classmethod
	def lastCel():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return (kernel.NumCels(self) - 1)
	#end:method

#end:class or instance

