#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1065
import sci_sh
import kernel
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	Graham = 94,
)

@SCI.instance
class Graham(Kq6Talker):
	#property vars (may be empty)
	x = 5
	y = 5
	view = 8981
	talkWidth = 213
	textX = 78
	textY = 8
	raveName = r"""GRAHAM"""
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: tBust tEyes tMouth &rest)
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 8981
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 37
	nsLeft = 26
	view = 8981
	loop = 1
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = 26
	nsLeft = 26
	view = 8981
	loop = 2
	
#end:class or instance

