#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1008
import sci_sh
import kernel
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	Ferryman = 23,
)

@SCI.instance
class Ferryman(Kq6Talker):
	#property vars (may be empty)
	x = 5
	y = 5
	view = 8972
	talkWidth = 213
	textX = 76
	textY = 8
	raveName = r"""FERRYM"""
	winPosn = 0
	
	@classmethod
	def init():
		super._send('init:', tBust, tEyes, tMouth, &rest)
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 8972
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = 27
	nsLeft = 26
	view = 8972
	loop = 2
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 37
	nsLeft = 29
	view = 8972
	loop = 1
	
#end:class or instance

