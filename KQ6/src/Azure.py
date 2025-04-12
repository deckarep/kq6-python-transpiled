#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1002
import sci_sh
import kernel
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	Azure = 20,
)

@SCI.instance
class Azure(Kq6Talker):
	#property vars (may be empty)
	x = 109
	y = 41
	view = 370
	loop = 4
	talkWidth = 213
	textX = -99
	textY = 70
	winPosn = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: 0 tEyes tMouth &rest)
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 370
	loop = 4
	signal = 24576
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	view = 370
	loop = 4
	signal = 24576
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = -5
	nsLeft = -1
	view = 370
	loop = 6
	signal = 24576
	
#end:class or instance

