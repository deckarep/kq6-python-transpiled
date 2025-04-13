#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1020
import sci_sh
import kernel
import Main
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	Jollo_the_Clown = 5,
)

@SCI.instance
class Jollo_the_Clown(Kq6Talker):
	#property vars (may be empty)
	name = r"""Jollo the Clown"""
	x = 5
	y = 5
	view = 894
	talkWidth = 213
	textX = 79
	textY = 8
	raveName = r"""JOLLO"""
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (global11 == 750):
			winPosn = 1
		else:
			winPosn = 0
		#endif
		super._send('init:', tBust, tEyes, tMouth, &rest)
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 894
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = 30
	nsLeft = 26
	view = 894
	loop = 2
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 36
	nsLeft = 20
	view = 894
	loop = 1
	
#end:class or instance

