#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1056
import sci_sh
import kernel
import Kq6Talker
import n913
import Actor

# Public Export Declarations
SCI.public_exports(
	The_Genie_Gardener = 55,
)

@SCI.instance
class The_Genie_Gardener(Kq6Talker):
	#property vars (may be empty)
	name = r"""The Genie Gardener"""
	view = 2002
	loop = 1
	cel = 1
	talkWidth = 213
	textX = -180
	textY = 18
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if proc913_0(163):
			x = 204
			y = 74
		else:
			x = 202
			y = 98
		#endif
		(super init: 0 0 tMouth1 &rest)
	#end:method

#end:class or instance

@SCI.instance
class tMouth1(Prop):
	#property vars (may be empty)
	view = 2002
	loop = 1
	
#end:class or instance

