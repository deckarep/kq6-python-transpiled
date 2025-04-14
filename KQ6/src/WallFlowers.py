#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1043
import sci_sh
import kernel
import Kq6Talker

# Public Export Declarations
SCI.public_exports(
	WallFlowers = 39,
)

@SCI.instance
class WallFlowers(Kq6Talker):
	#property vars (may be empty)
	x = 5
	y = 5
	view = 890
	cel = 1
	talkWidth = 183
	textX = 106
	textY = 10
	
	@classmethod
	def init():
		super._send('init:', 0, 0, 0, &rest)
	#end:method

#end:class or instance

