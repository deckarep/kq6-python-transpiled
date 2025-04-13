#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1005
import sci_sh
import kernel
import Main
import Kq6Talker
import n913
import Actor

# Public Export Declarations
SCI.public_exports(
	Cassima = 28,
)

@SCI.instance
class Cassima(Kq6Talker):
	#property vars (may be empty)
	x = 5
	y = 5
	view = 891
	talkWidth = 213
	textX = 79
	textY = 8
	raveName = r"""CASSIMA"""
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (proc913_0(59) and (global11 == 140)):
				cel = 1
				self._send('x:', 94, 'y:', 87, 'textX:', -60, 'textY:', 30)
				super._send('init:', 0, 0, tMouth140, &rest)
			#end:case
			case proc913_0(59):
				cel = 1
				super._send('init:', 0, 0, 0, &rest)
			#end:case
			case ((global2._send('curPic:') == 165) and (global11 == 740)):
				self._send('cel:', 1, 'x:', 214, 'y:', 78, 'textX:', -60, 'textY:', 50, 'talkWidth:', 120)
				super._send('init:', 0, tEyes740, tMouth740, &rest)
			#end:case
			case proc913_0(99):
				self._send('cel:', 1, 'x:', 172, 'y:', 54, 'talkWidth:', 135, 'textX:', -2, 'textY:', 58)
				super._send('init:', 0, 0, wedMouth, &rest)
			#end:case
			case proc913_0(102):
				self._send('cel:', 1, 'x:', 132, 'y:', 67, 'textX:', -112, 'textY:', -47, 'talkWidth:', 92)
				tEyes._send('view:', 7832, 'loop:', 10, 'cel:', 0, 'nsLeft:', 0, 'nsTop:', 0)
				tMouth._send('view:', 7832, 'loop:', 9, 'cel:', 0, 'nsLeft:', -4, 'nsTop:', 3)
				super._send('init:', 0, tEyes, tMouth, &rest)
			#end:case
			case (global11 == 870):
				self._send('cel:', 1, 'textX:', 58, 'textY:', 57, 'talkWidth:', 100)
				super._send('init:', 0, 0, 0, &rest)
			#end:case
			else:
				if ((global11 == 750) or (global11 == 740)):
					winPosn = 0
				#endif
				self._send(
					'view:', 891,
					'loop:', 0,
					'cel:', 0,
					'x:', 5,
					'y:', 5,
					'textX:', 79,
					'textY:', 8,
					'talkWidth:', 213
				)
				tEyes._send('view:', 891, 'loop:', 2, 'nsTop:', 30, 'nsLeft:', 26)
				tMouth._send('view:', 891, 'loop:', 1, 'nsTop:', 40, 'nsLeft:', 27)
				super._send('init:', tBust, tEyes, tMouth, &rest)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class tBust(Prop):
	#property vars (may be empty)
	view = 891
	
#end:class or instance

@SCI.instance
class tEyes(Prop):
	#property vars (may be empty)
	nsTop = 30
	nsLeft = 26
	view = 891
	loop = 2
	
#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	nsTop = 40
	nsLeft = 27
	view = 891
	loop = 1
	
#end:class or instance

@SCI.instance
class wedMouth(Prop):
	#property vars (may be empty)
	view = 161
	
#end:class or instance

@SCI.instance
class tMouth740(Prop):
	#property vars (may be empty)
	view = 165
	loop = 3
	
#end:class or instance

@SCI.instance
class tEyes740(Prop):
	#property vars (may be empty)
	nsTop = -11
	nsLeft = 2
	view = 165
	loop = 2
	
#end:class or instance

@SCI.instance
class tMouth140(Prop):
	#property vars (may be empty)
	view = 142
	loop = 3
	
#end:class or instance

@SCI.instance
class tEyes140(Prop):
	#property vars (may be empty)
	nsTop = -11
	nsLeft = 1
	view = 142
	loop = 4
	
#end:class or instance

