#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 20
import sci_sh
import Game
import System

# Public Export Declarations
SCI.public_exports(
	rSacred = 0,
)

class rSacred(Rgn):
	#property vars (may be empty)
	geniePresent = 0
	marePresent = 0
	
	@classmethod
	def newRoom(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		keep = (proc999_5 param1 300 310 320 330 340 350 370 380 390)
		initialized = 0
		(super newRoom: param1 &rest)
	#end:method

#end:class or instance

