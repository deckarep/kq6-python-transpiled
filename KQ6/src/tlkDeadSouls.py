#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1025
import sci_sh
import kernel
import Main
import Kq6Window
import Talker

# Public Export Declarations
SCI.public_exports(
	tlkDeadSouls = 79,
)

@SCI.instance
class tlkDeadSouls(Narrator):
	#property vars (may be empty)
	x = 175
	y = 160
	
	@classmethod
	def init():
		if (kernel.Random(0, 100) > 50):
			self._send('x:', 10)
		#endif
		font = global22
		keepWindow = 1
		color = Kq6Window._send('color:')
		back = Kq6Window._send('back:')
		super._send('init:', &rest)
	#end:method

#end:class or instance

