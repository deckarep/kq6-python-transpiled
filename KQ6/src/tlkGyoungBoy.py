#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1019
import sci_sh
import kernel
import Main
import Kq6Window
import Talker

# Public Export Declarations
SCI.public_exports(
	tlkGyoungBoy = 22,
)

@SCI.instance
class tlkGyoungBoy(Narrator):
	#property vars (may be empty)
	x = 10
	y = 10
	
	@classmethod
	def init():
		font = global22
		keepWindow = 1
		color = Kq6Window._send('color:')
		back = Kq6Window._send('back:')
		if (global11 == 260):
			x = 110
		#endif
		super._send('init:', &rest)
	#end:method

#end:class or instance

