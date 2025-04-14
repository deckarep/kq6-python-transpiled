#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1007
import sci_sh
import kernel
import Main
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	Participle = 9,
)

@SCI.instance
class Participle(Kq6Talker):
	#property vars (may be empty)
	@classmethod
	def init():
		match global11
			case 500:
				self._send(
					'view:', 479,
					'loop:', 5,
					'x:', 190,
					'y:', 38,
					'textX:', -70,
					'textY:', 76,
					'talkWidth:', 153
				)
				super._send('init:', 0, 0, tMouth, &rest)
			#end:case
			case 460:
				self._send(
					'view:', 468,
					'loop:', 2,
					'x:', 129,
					'y:', 130,
					'textX:', 0,
					'textY:', 0,
					'talkWidth:', 150
				)
				tMouth._send('view:', 468, 'loop:', 2)
				super._send('init:', 0, 0, tMouth, &rest)
			#end:case
			else:
				self._send(
					'view:', 970,
					'loop:', 5,
					'cel:', 0,
					'x:', 129,
					'y:', 130,
					'textX:', -60,
					'textY:', -100,
					'talkWidth:', 150
				)
				tMouth._send('view:', 970, 'loop:', 5, 'cel:', 0)
				super._send('init:', 0, 0, tMouth, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class tMouth(Actor):
	#property vars (may be empty)
	view = 479
	loop = 5
	
#end:class or instance

