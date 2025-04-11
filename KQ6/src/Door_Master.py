#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1060
import sci_sh
import Kq6Talker

# Public Export Declarations
SCI.public_exports(
	Door_Master = 83,
)

@SCI.instance
class Door_Master(Kq6Talker):
	#property vars (may be empty)
	name = r"""Door Master"""
	x = 190
	y = 200
	view = 2002
	loop = 1
	cel = 1
	talkWidth = 110
	textX = 0
	textY = -120
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: 0 0 0 &rest)
	#end:method

#end:class or instance

