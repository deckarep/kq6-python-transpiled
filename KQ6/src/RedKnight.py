#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1055
import sci_sh
import kernel
import Kq6Talker
import Actor

# Public Export Declarations
SCI.public_exports(
	RedKnight = 75,
	WhiteKnight = 76,
)

@SCI.instance
class WhiteKnight(Kq6Talker):
	#property vars (may be empty)
	x = 126
	y = 83
	view = 492
	loop = 4
	talkWidth = 213
	textX = -112
	textY = -73
	
	@classmethod
	def init():
		super._send('init:', 0, 0, tWhtMouth, &rest)
	#end:method

#end:class or instance

@SCI.instance
class RedKnight(Kq6Talker):
	#property vars (may be empty)
	x = 174
	y = 83
	view = 493
	loop = 4
	talkWidth = 213
	textX = -87
	textY = -73
	
	@classmethod
	def init():
		super._send('init:', 0, 0, tRedMouth, &rest)
	#end:method

#end:class or instance

@SCI.instance
class tWhtBust(Prop):
	#property vars (may be empty)
	view = 492
	loop = 4
	
#end:class or instance

@SCI.instance
class tRedBust(Prop):
	#property vars (may be empty)
	view = 493
	loop = 4
	
#end:class or instance

@SCI.instance
class tWhtMouth(Prop):
	#property vars (may be empty)
	view = 492
	loop = 4
	
#end:class or instance

@SCI.instance
class tRedMouth(Prop):
	#property vars (may be empty)
	view = 493
	loop = 4
	
#end:class or instance

