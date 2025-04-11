#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1061
import sci_sh
import kernel
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	Gate = 58,
)

@SCI.instance
class Gate(Kq6Talker):
	#property vars (may be empty)
	x = 202
	y = 59
	view = 2002
	talkWidth = 170
	textX = -190
	textY = -40
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: 0 0 tMouth &rest)
	#end:method

#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	view = 676
	
#end:class or instance

