#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1006
import sci_sh
import kernel
import Kq6Talker
import n913
import Actor

# Public Export Declarations
SCI.public_exports(
	Celeste = 4,
)

@SCI.instance
class Celeste(Kq6Talker):
	#property vars (may be empty)
	x = 245
	y = 5
	view = 8941
	talkWidth = 213
	textX = -232
	textY = 6
	raveName = r"""CELESTE"""
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc913_0(161):
			cel = 1
			super._send('init:', 0, 0, 0, &rest)
		else:
			super._send('init:', tBust, tEyes, tMouth, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 8941
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = 31
	nsLeft = 27
	view = 8941
	loop = 2
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 39
	nsLeft = 32
	view = 8941
	loop = 1
	
#end:class or instance

