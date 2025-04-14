#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1031
import sci_sh
import kernel
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	SnapDragons = 74,
)

@SCI.instance
class SnapDragons(Kq6Talker):
	#property vars (may be empty)
	x = 5
	y = 5
	view = 2002
	loop = 1
	talkWidth = 213
	textX = 76
	textY = 8
	
	@classmethod
	def init():
		super._send('init:', tBust, tEyes, tMouth, &rest)
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 2002
	loop = 1
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = 19
	nsLeft = 13
	view = 2002
	loop = 2
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 33
	nsLeft = 15
	view = 2002
	
#end:class or instance

