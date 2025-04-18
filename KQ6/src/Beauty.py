#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1003
import sci_sh
import kernel
import Kq6Talker
import n913
import Actor

# Public Export Declarations
SCI.public_exports(
	Beauty = 17,
)

@SCI.instance
class Beauty(Kq6Talker):
	#property vars (may be empty)
	x = 248
	y = 5
	view = 895
	talkWidth = 213
	textX = -239
	textY = 8
	raveName = r"""BEAUTPEA"""
	
	@classmethod
	def init():
		(cond
			case proc913_0(59):
				tBust._send('cel:', 1)
				cel = 1
				super._send('init:', tBust, 0, 0, &rest)
			#end:case
			case proc913_0(43):
				view = 8951
				tBust._send('view:', 8951)
				tMouth._send('view:', 8951, 'nsTop:', 33, 'nsLeft:', 28)
				tEyes._send('view:', 8951, 'nsTop:', 26, 'nsLeft:', 28)
				raveName = r"""BEAUTESS"""
				super._send('init:', tBust, tEyes, tMouth, &rest)
			#end:case
			else:
				super._send('init:', tBust, tEyes, tMouth, &rest)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 895
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = 25
	nsLeft = 27
	view = 895
	loop = 2
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 32
	nsLeft = 27
	view = 895
	loop = 1
	
#end:class or instance

