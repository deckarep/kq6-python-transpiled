#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1011
import sci_sh
import kernel
import Kq6Talker
import n913
import Actor

# Public Export Declarations
SCI.public_exports(
	Genie = 27,
)

@SCI.instance
class Genie(Kq6Talker):
	#property vars (may be empty)
	x = 5
	y = 5
	view = 893
	talkWidth = 213
	textX = 76
	textY = 8
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc913_0(59):
			cel = 1
			(super init: 0 0 0 &rest)
		else:
			(super init: tBust tEyes tMouth &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 893
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = 36
	nsLeft = 27
	view = 893
	loop = 2
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 43
	nsLeft = 25
	view = 893
	loop = 1
	
#end:class or instance

