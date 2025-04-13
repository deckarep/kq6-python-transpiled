#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1004
import sci_sh
import kernel
import Kq6Talker
import n913
import Actor

# Public Export Declarations
SCI.public_exports(
	Caliphim = 11,
)

@SCI.instance
class Caliphim(Kq6Talker):
	#property vars (may be empty)
	x = 5
	y = 5
	view = 899
	talkWidth = 213
	textY = 12
	raveName = r"""CALIPHIM"""
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc913_0(91):
			view = 8991
			tBust._send('view:', 8991)
			tEyes._send('view:', 8991, 'nsLeft:', 31, 'nsTop:', 34)
			tMouth._send('view:', 8991, 'nsLeft:', 33, 'nsTop:', 43)
			raveName = r"""CALIPHID"""
		else:
			view = 899
			tBust._send('view:', 899)
			tEyes._send('view:', 899, 'nsLeft:', 28, 'nsTop:', 29)
			tMouth._send('view:', 899, 'nsLeft:', 29, 'nsTop:', 38)
			raveName = r"""CALIPHIM"""
		#endif
		super._send('init:', tBust, tEyes, tMouth, &rest)
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	loop = 2
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	loop = 1
	
#end:class or instance

