#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 165
import sci_sh
import kernel
import KQ6Room

# Public Export Declarations
SCI.public_exports(
	rm165 = 0,
)

@SCI.instance
class rm165(KQ6Room):
	#property vars (may be empty)
	picture = 165
	autoLoad = 0
	
	@classmethod
	def init():
		super._send('init:', &rest)
	#end:method

#end:class or instance

