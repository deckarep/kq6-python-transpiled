#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1017
import sci_sh
import kernel
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	PussyWillows = 42,
)

@SCI.instance
class PussyWillows(Kq6Talker):
	#property vars (may be empty)
	x = 255
	y = 5
	view = 470
	loop = 1
	talkWidth = 213
	textX = -239
	textY = 8
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: 0 0 0 &rest)
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 2004
	loop = 1
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = 21
	nsLeft = 25
	view = 2004
	loop = 2
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 30
	nsLeft = 25
	view = 2004
	
#end:class or instance

