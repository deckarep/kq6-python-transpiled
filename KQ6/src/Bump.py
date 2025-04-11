#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1049
import sci_sh
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	Bump = 48,
)

@SCI.instance
class Bump(Kq6Talker):
	#property vars (may be empty)
	x = 28
	y = 153
	view = 474
	loop = 1
	talkWidth = 213
	textX = -10
	textY = -144
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: 0 0 tMouth &rest)
	#end:method

#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	view = 474
	loop = 1
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	view = 474
	loop = 1
	
#end:class or instance

