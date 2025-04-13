#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1023
import sci_sh
import kernel
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	Oracle = 19,
)

@SCI.instance
class Oracle(Kq6Talker):
	#property vars (may be empty)
	x = 153
	y = 57
	view = 382
	talkWidth = 253
	textX = -124
	textY = 77
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', 0, tEyes, tMouth, &rest)
	#end:method

#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	view = 382
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = -10
	nsLeft = -6
	view = 382
	loop = 1
	
#end:class or instance

