#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1035
import sci_sh
import kernel
import Main
import Kq6Window
import Talker

# Public Export Declarations
SCI.public_exports(
	tlkGoldMan = 34,
)

@SCI.instance
class tlkGoldMan(Narrator):
	#property vars (may be empty)
	x = 10
	y = 10
	
	@classmethod
	def init():
		font = global22
		keepWindow = 1
		color = Kq6Window._send('color:')
		back = Kq6Window._send('back:')
		super._send('init:', &rest)
	#end:method

#end:class or instance

