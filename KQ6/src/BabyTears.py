#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1039
import sci_sh
import kernel
import Kq6Talker
import n913
import Actor

# Public Export Declarations
SCI.public_exports(
	BabyTears = 71,
)

@SCI.instance
class BabyTears(Kq6Talker):
	#property vars (may be empty)
	view = 4803
	talkWidth = 213
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc913_0(59):
			(self loop: 7 x: 0 y: 135 textX: 10 textY: -125)
			(super init: tWimpBust 0 tWimpMouth &rest)
		else:
			(self loop: 13 x: 44 y: 140 textX: -36 textY: -130)
			(super init: 0 0 tMouth &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 4803
	loop = 4
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	view = 4803
	loop = 4
	
#end:class or instance

@SCI.instance
class tWimpBust(Prop):
	#property vars (may be empty)
	view = 4803
	loop = 1
	
#end:class or instance

@SCI.instance
class tWimpMouth(Prop):
	#property vars (may be empty)
	view = 4803
	loop = 1
	
#end:class or instance

