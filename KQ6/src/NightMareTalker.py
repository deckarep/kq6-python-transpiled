#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1062
import sci_sh
import kernel
import Kq6Talker

# Public Export Declarations
SCI.public_exports(
	NightMareTalker = 80,
)

@SCI.instance
class NightMareTalker(Kq6Talker):
	#property vars (may be empty)
	x = 5
	y = 5
	view = 890
	cel = 1
	talkWidth = 213
	textX = 5
	textY = 6
	
	@classmethod
	def init():
		super._send('init:', 0, 0, 0, &rest)
	#end:method

#end:class or instance

