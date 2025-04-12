#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 965
import sci_sh
import kernel

# Public Export Declarations
SCI.public_exports(
	proc965_0 = 0,
)

@SCI.procedure
def proc965_0(param1 = None, param2 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	temp1 = kernel.FirstNode((param1 elements:))
	temp0 = 0
	while temp1:

		if (param2 doit: kernel.NodeValue(temp1) &rest):
			temp0.post('++')
		#endif
		temp1 = kernel.NextNode(temp1)
	#end:loop
	return temp0
#end:procedure

