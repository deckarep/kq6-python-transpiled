#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1063
import sci_sh
import Kq6Talker
import n913
import Actor

# Public Export Declarations
SCI.public_exports(
	Allaria = 62,
)

@SCI.instance
class Allaria(Kq6Talker):
	#property vars (may be empty)
	x = 5
	y = 5
	view = 8992
	talkWidth = 213
	textX = 78
	textY = 8
	raveName = r"""ALLARIA"""
	winPosn = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (proc913_0 91):
			(self view: 8993)
			(tBust view: 8993)
			(tEyes view: 8993)
			raveName = r"""ALLARIAD"""
			(tMouth view: 8993)
		else:
			(self view: 8992)
			(tBust view: 8992)
			(tEyes view: 8992)
			(tMouth view: 8992)
			raveName = r"""ALLARIA"""
		#endif
		(super init: tBust tEyes tMouth &rest)
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = 29
	nsLeft = 24
	loop = 2
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 38
	nsLeft = 27
	loop = 1
	
#end:class or instance

