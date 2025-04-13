#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1046
import sci_sh
import kernel
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	Dipthong = 45,
)

@SCI.instance
class Dipthong(Kq6Talker):
	#property vars (may be empty)
	x = 244
	y = 44
	view = 890
	cel = 1
	talkWidth = 150
	textX = -200
	textY = -20
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', 0, 0, tMouth, &rest)
	#end:method

#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	view = 463
	loop = 6
	
#end:class or instance

