#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 40
import sci_sh
import kernel
import Game
import System

# Public Export Declarations
SCI.public_exports(
	rWonder = 0,
)

class rWonder(Rgn):
	#property vars (may be empty)
	spiderBit = 0
	parchmentBit = 0
	gotParchment = 0
	tomoTalk = 0
	stickTalk = 0
	grapeTalk = 0
	vineTalk = 0
	holeLooks = 0
	holeGrabs = 0
	oysterDozing = 0
	flowerDance = 0
	babyFed = 0
	lampMsg = 0
	bottleSucker = 0
	alexX = 0
	alexY = 0
	alexInvisible = 0
	grabAtHidingHole = 0
	
	@classmethod
	def newRoom(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		keep = proc999_5(param1, 450, 460, 461, 470, 475, 480, 490)
		initialized = 0
		super._send('newRoom:', param1, &rest)
	#end:method

#end:class or instance

