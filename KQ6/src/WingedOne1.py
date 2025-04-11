#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1030
import sci_sh
import Main
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	WingedOne1 = 18,
	WingedOne2 = 31,
)

@SCI.instance
class WingedOne1(Kq6Talker):
	#property vars (may be empty)
	x = 5
	y = 5
	view = 8942
	talkWidth = 213
	textX = 81
	textY = 6
	raveName = r"""WINGG"""
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (global11 == 380):
			winPosn = 0
		#endif
		(super init: tBust1 tEyes1 tMouth1 &rest)
	#end:method

#end:class or instance

@SCI.instance
class tBust1(Prop):
	#property vars (may be empty)
	view = 8942
	
#end:class or instance

@SCI.instance
class tEyes1(Prop):
	#property vars (may be empty)
	nsTop = 29
	nsLeft = 27
	view = 8942
	loop = 2
	
#end:class or instance

@SCI.instance
class tMouth1(Prop):
	#property vars (may be empty)
	nsTop = 39
	nsLeft = 26
	view = 8942
	loop = 1
	
#end:class or instance

@SCI.instance
class WingedOne2(Kq6Talker):
	#property vars (may be empty)
	x = 245
	y = 5
	view = 8942
	talkWidth = 213
	textX = -233
	textY = 6
	raveName = r"""WINGG"""
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: tBust2 tEyes2 tMouth2 &rest)
	#end:method

#end:class or instance

@SCI.instance
class tBust2(Prop):
	#property vars (may be empty)
	view = 8942
	
#end:class or instance

@SCI.instance
class tEyes2(Prop):
	#property vars (may be empty)
	nsTop = 29
	nsLeft = 27
	view = 8942
	loop = 2
	
#end:class or instance

@SCI.instance
class tMouth2(Prop):
	#property vars (may be empty)
	nsTop = 39
	nsLeft = 26
	view = 8942
	loop = 1
	
#end:class or instance

