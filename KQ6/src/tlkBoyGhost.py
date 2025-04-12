#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1050
import sci_sh
import kernel
import Main
import Kq6Window
import Talker

# Public Export Declarations
SCI.public_exports(
	tlkBoyGhost = 77,
)

@SCI.instance
class tlkBoyGhost(Narrator):
	#property vars (may be empty)
	y = 10
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		font = global22
		keepWindow = 1
		color = (Kq6Window color:)
		back = (Kq6Window back:)
		(super init: &rest)
	#end:method

#end:class or instance

