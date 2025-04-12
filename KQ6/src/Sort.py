#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 966
import sci_sh
import kernel
import System

# Public Export Declarations
SCI.public_exports(
	proc966_0 = 0,
)

@SCI.procedure
def proc966_0(param1 = None, param2 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	temp3 = (List new:)
	while temp1 = kernel.FirstNode((param1 elements:)):

		temp2 = kernel.NodeValue(temp1)
		while temp1:

			if (param2 doit: temp0 = kernel.NodeValue(temp1) temp2 &rest):
				temp2 = temp0
			#endif
			temp1 = kernel.NextNode(temp1)
		#end:loop
		(TE doit: temp2 param1 temp3)
	#end:loop
	(temp3 eachElementDo: #perform TE temp3 param1 dispose:)
#end:procedure

@SCI.instance
class TE(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, param2 = None, param3 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(param3 addToEnd: param1)
		(param2 delete: param1)
	#end:method

#end:class or instance

