#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1010
import sci_sh
import kernel
import Main
import Kq6Window
import Talker

# Public Export Declarations
SCI.public_exports(
	tlkCook = 57,
)

@SCI.instance
class tlkCook(Narrator):
	#property vars (may be empty)
	y = 10
	
	@classmethod
	def init():
		keepWindow = 1
		color = Kq6Window._send('color:')
		back = Kq6Window._send('back:')
		font = global22
		super._send('init:', &rest)
	#end:method

#end:class or instance

