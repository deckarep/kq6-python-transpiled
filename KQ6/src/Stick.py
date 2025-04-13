#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1048
import sci_sh
import kernel
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	Stick = 47,
)

@SCI.instance
class Stick(Kq6Talker):
	#property vars (may be empty)
	x = 274
	y = 83
	view = 475
	loop = 12
	talkWidth = 213
	textX = -193
	textY = -70
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', 0, 0, tMouth, &rest)
	#end:method

#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	view = 475
	loop = 12
	
#end:class or instance

