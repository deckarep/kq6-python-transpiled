#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1016
import sci_sh
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	Dogwood = 69,
)

@SCI.instance
class Dogwood(Kq6Talker):
	#property vars (may be empty)
	x = 11
	y = 16
	view = 470
	loop = 2
	talkWidth = 200
	textX = 76
	textY = 8
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: tBust 0 tMouth &rest)
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 470
	loop = 2
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	view = 470
	loop = 2
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	view = 470
	loop = 2
	
#end:class or instance

