#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1012
import sci_sh
import kernel
import Main
import Kq6Talker
import Kq6Window
import Actor

# Public Export Declarations
SCI.public_exports(
	tlkGeniePage = 32,
)

@SCI.instance
class tlkGeniePage(Kq6Talker):
	#property vars (may be empty)
	y = 10
	view = 890
	cel = 1
	talkWidth = 213
	textX = 78
	textY = 8
	
	@classmethod
	def init():
		font = global22
		keepWindow = 1
		color = Kq6Window._send('color:')
		back = Kq6Window._send('back:')
		if (global2._send('curPic:') == 160):
			self._send('cel:', 1, 'x:', 80, 'y:', 48, 'textX:', 1, 'textY:', -35, 'talkWidth:', 213)
			super._send('init:', 0, 0, tMouth, &rest)
		else:
			self._send('cel:', 1, 'x:', 5, 'y:', 5, 'textX:', 76, 'textY:', 8, 'talkWidth:', 213)
			super._send('init:', 0, 0, 0, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class tMouth(Prop):
	#property vars (may be empty)
	view = 160
	loop = 8
	
#end:class or instance

