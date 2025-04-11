#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 50
import sci_sh
import kernel
import Game
import System

# Public Export Declarations
SCI.public_exports(
	rBeast = 0,
)

class rBeast(Rgn):
	#property vars (may be empty)
	@classmethod
	def newRoom(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		keep = proc999_5(param1, 500, 510, 520, 530, 540)
		initialized = 0
		(super newRoom: param1 &rest)
	#end:method

#end:class or instance

