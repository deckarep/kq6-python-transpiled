#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1022
import sci_sh
import kernel
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	Minotaur = 3,
)

@SCI.instance
class Minotaur(Kq6Talker):
	#property vars (may be empty)
	x = 5
	y = 5
	view = 890
	cel = 1
	talkWidth = 213
	textX = 76
	textY = 8
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: 0 0 0 &rest)
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 896
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = 25
	nsLeft = 26
	view = 896
	loop = 1
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 21
	nsLeft = 24
	view = 896
	loop = 2
	
#end:class or instance

