#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1033
import sci_sh
import kernel
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	Priest = 26,
	Priest = 59,
	Priest = 60,
)

@SCI.instance
class Priest(Kq6Talker):
	#property vars (may be empty)
	x = 245
	y = 5
	view = 898
	talkWidth = 213
	textX = -239
	textY = 8
	raveName = r"""HEADDRU"""
	winPosn = 0
	
	@classmethod
	def init():
		super._send('init:', tBust, tEyes, tMouth, &rest)
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 898
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = 26
	nsLeft = 25
	view = 898
	loop = 2
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 29
	nsLeft = 26
	view = 898
	loop = 1
	
#end:class or instance

