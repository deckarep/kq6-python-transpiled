#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 974
import sci_sh
import kernel
import System

# Public Export Declarations
SCI.public_exports(
	proc974_0 = 0,
)

@SCI.procedure
def proc974_0(param1 = None, param2 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	(param2 firstTrue: #perform NC param1)
#end:procedure

@SCI.instance
class NC(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return (0 == kernel.StrCmp((param1 name:), param2))
	#end:method

#end:class or instance

