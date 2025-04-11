#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1045
import sci_sh
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	Oxymoron = 44,
)

@SCI.instance
class Oxymoron(Kq6Talker):
	#property vars (may be empty)
	x = 290
	y = 54
	view = 890
	cel = 1
	talkWidth = 150
	textX = -173
	textY = -16
	
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
	view = 460
	loop = 15
	
#end:class or instance

