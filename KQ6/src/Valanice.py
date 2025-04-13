#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1066
import sci_sh
import kernel
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	Valanice = 12,
)

@SCI.instance
class Valanice(Kq6Talker):
	#property vars (may be empty)
	x = 5
	y = 5
	view = 8982
	talkWidth = 213
	textX = 78
	textY = 8
	raveName = r"""VALANICE"""
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', tBust, tEyes, tMouth, &rest)
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 8982
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 36
	nsLeft = 27
	view = 8982
	loop = 1
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = 25
	nsLeft = 27
	view = 8982
	loop = 2
	
#end:class or instance

