#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 160
import sci_sh
import kernel
import KQ6Room

# Public Export Declarations
SCI.public_exports(
	rm160 = 0,
)

@SCI.instance
class rm160(KQ6Room):
	#property vars (may be empty)
	picture = 160
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
	#end:method

#end:class or instance

