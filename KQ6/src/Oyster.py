#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1038
import sci_sh
import kernel
import Kq6Talker
import n913
import Actor

# Public Export Declarations
SCI.public_exports(
	Oyster = 37,
)

@SCI.instance
class Oyster(Kq6Talker):
	#property vars (may be empty)
	talkWidth = 213
	
	@classmethod
	def init():
		if proc913_0(59):
			self._send('view:', 890, 'loop:', 0, 'cel:', 1, 'x:', 255, 'y:', 5, 'textX:', -239, 'textY:', 8)
			super._send('init:', 0, 0, 0, &rest)
		else:
			self._send('view:', 4531, 'loop:', 3, 'x:', 58, 'y:', 127, 'textX:', -40, 'textY:', -105)
			super._send('init:', 0, 0, tMouth, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	view = 4531
	loop = 3
	
#end:class or instance

