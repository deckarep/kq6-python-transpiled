#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1057
import sci_sh
import Kq6Talker
import n913
import Actor

# Public Export Declarations
SCI.public_exports(
	Beast = 56,
)

@SCI.instance
class Beast(Kq6Talker):
	#property vars (may be empty)
	x = 5
	y = 5
	view = 896
	talkWidth = 213
	textX = 78
	textY = 8
	raveName = r"""BEAST"""
	winPosn = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (proc913_0 113):
			view = 8961
			(tBust view: 8961)
			(tMouth view: 8961 nsTop: 32 nsLeft: 30)
			(tEyes view: 8961 nsTop: 21 nsLeft: 30)
			raveName = r"""PRINCE"""
		#endif
		(super init: tBust tEyes tMouth &rest)
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 896
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 31
	nsLeft = 34
	view = 896
	loop = 1
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = 27
	nsLeft = 32
	view = 896
	loop = 2
	
#end:class or instance

