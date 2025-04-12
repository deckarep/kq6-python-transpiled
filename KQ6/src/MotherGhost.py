#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1064
import sci_sh
import kernel
import Kq6Talker

# Public Export Declarations
SCI.public_exports(
	MotherGhost = 40,
)

@SCI.instance
class MotherGhost(Kq6Talker):
	#property vars (may be empty)
	x = 5
	y = 5
	view = 2002
	cel = 1
	talkWidth = 213
	textX = 76
	textY = 8
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: 0 0 0 &rest)
	#end:method

#end:class or instance

