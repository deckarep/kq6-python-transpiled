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
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		font = global22
		keepWindow = 1
		color = (Kq6Window color:)
		back = (Kq6Window back:)
		if (global11 == 260):
			x = 110
		#endif
		(super init: &rest)
	#end:method

#end:class or instance

