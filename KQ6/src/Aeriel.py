#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1000
import sci_sh
import kernel
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	Aeriel = 21,
)

@SCI.instance
class Aeriel(Kq6Talker):
	#property vars (may be empty)
	x = 202
	y = 45
	view = 370
	loop = 5
	talkWidth = 213
	textX = -116
	textY = 74
	
	@classmethod
	def init():
		super._send('init:', 0, tEyes, tMouth, &rest)
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 370
	loop = 5
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	view = 370
	loop = 5
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = -3
	nsLeft = -1
	view = 370
	loop = 7
	
#end:class or instance

