#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1058
import sci_sh
import kernel
import Main
import Kq6Talker
import Kq6Window
import Actor

# Public Export Declarations
SCI.public_exports(
	tlkWaiter = 49,
)

@SCI.instance
class tlkWaiter(Kq6Talker):
	#property vars (may be empty)
	y = 10
	view = 735
	loop = 5
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		font = global22
		keepWindow = 1
		color = (Kq6Window color:)
		back = (Kq6Window back:)
		if (global90 == 2):
			x = 100
			y = 104
			textX = -58
			(super init: 0 0 waiterMouth &rest)
		else:
			x = -1
			textY = textX = y = 10
			(super init: &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class waiterMouth(Actor):
	#property vars (may be empty)
	view = 735
	loop = 4
	
#end:class or instance

