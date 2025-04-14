#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1024
import sci_sh
import kernel
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	Lord_of_the_Dead = 78,
)

@SCI.instance
class Lord_of_the_Dead(Kq6Talker):
	#property vars (may be empty)
	name = r"""Lord of the Dead"""
	x = 168
	y = 53
	view = 2002
	cel = 1
	talkWidth = 213
	textX = -118
	textY = 25
	
	@classmethod
	def init():
		super._send('init:', 0, 0, tMouth, &rest)
		self._send('setPri:', 13)
	#end:method

#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	view = 692
	loop = 2
	
#end:class or instance

