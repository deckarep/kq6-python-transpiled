#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1013
import sci_sh
import kernel
import Main
import Kq6Talker
import n913
import Actor

# Public Export Declarations
SCI.public_exports(
	Genie = 29,
)

@SCI.instance
class Genie(Kq6Talker):
	#property vars (may be empty)
	x = 5
	y = 5
	view = 893
	talkWidth = 213
	textX = 76
	textY = 8
	
	@classmethod
	def init():
		if (global11 == 145):
			self._send('view:', 1466, 'loop:', 3, 'talkWidth:', 175)
			if proc913_0(133):
				self._send('x:', 173, 'y:', 134, 'textX:', -73, 'textY:', -114)
				temp0 = tMouthLo
			else:
				self._send('x:', 182, 'y:', 68, 'textX:', -107, 'textY:', 20)
				temp0 = tMouthHi
			#endif
			super._send('init:', 0, 0, temp0, &rest)
		else:
			super._send('init:', tBust, tEyes, tMouth, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 893
	loop = 1
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = 21
	nsLeft = 18
	view = 893
	loop = 2
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 32
	nsLeft = 16
	view = 893
	
#end:class or instance

@SCI.instance
class tMouthHi(Prop):
	#property vars (may be empty)
	view = 1466
	loop = 1
	
#end:class or instance

@SCI.instance
class tMouthLo(Prop):
	#property vars (may be empty)
	view = 1466
	
#end:class or instance

