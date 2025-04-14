#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1021
import sci_sh
import kernel
import Kq6Talker
import n913
import Actor

# Public Export Declarations
SCI.public_exports(
	Lampseller = 16,
)

@SCI.instance
class Lampseller(Kq6Talker):
	#property vars (may be empty)
	x = 5
	y = 5
	view = 8973
	talkWidth = 213
	textX = 76
	textY = 8
	raveName = r"""LAMPSELL"""
	winPosn = 0
	
	@classmethod
	def init():
		if proc913_0(59):
			tBust._send('cel:', 1)
			cel = 1
			super._send('init:', tBust, 0, 0, &rest)
			textY = textX = 0
			y = x = 10
		else:
			tBust._send('cel:', 0)
			cel = 1
			textX = 76
			textY = 8
			y = x = 5
			super._send('init:', tBust, tEyes, tMouth, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 8973
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = 32
	nsLeft = 31
	view = 8973
	loop = 2
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 44
	nsLeft = 31
	view = 8973
	loop = 1
	
#end:class or instance

