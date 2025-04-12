#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1052
import sci_sh
import kernel
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	TomatoVines = 51,
)

@SCI.instance
class TomatoVines(Kq6Talker):
	#property vars (may be empty)
	x = 119
	y = 118
	view = 4802
	talkWidth = 183
	textX = -108
	textY = -107
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: 0 0 tMouth &rest)
	#end:method

#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	view = 4802
	
#end:class or instance

