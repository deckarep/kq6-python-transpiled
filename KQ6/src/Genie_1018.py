#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1018
import sci_sh
import kernel
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	Genie = 1,
)

@SCI.instance
class Genie(Kq6Talker):
	#property vars (may be empty)
	x = 80
	y = 111
	view = 890
	cel = 1
	talkWidth = 213
	textX = -10
	textY = -100
	
	@classmethod
	def init():
		super._send('init:', 0, 0, tMouth, &rest)
	#end:method

#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	view = 425
	
#end:class or instance

