#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1027
import sci_sh
import kernel
import Main
import Kq6Talker
import Kq6Window
import Actor

# Public Export Declarations
SCI.public_exports(
	tlkStepmother = 10,
)

@SCI.instance
class tlkStepmother(Kq6Talker):
	#property vars (may be empty)
	x = 100
	y = 16
	view = 255
	loop = 5
	
	@classmethod
	def init():
		font = global22
		keepWindow = 1
		color = Kq6Window._send('color:')
		back = Kq6Window._send('back:')
		textY = textX = 0
		if (global90 & 0x0002):
			x = 225
			y = 59
			super._send('init:', 0, 0, momsMouth, &rest)
		else:
			x = 20
			y = 16
			super._send('init:', &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class momsMouth(Prop):
	#property vars (may be empty)
	view = 255
	loop = 4
	
#end:class or instance

