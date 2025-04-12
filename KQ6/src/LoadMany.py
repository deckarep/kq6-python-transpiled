#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 958
import sci_sh
import kernel

# Public Export Declarations
SCI.public_exports(
	proc958_0 = 0,
)

@SCI.procedure
def proc958_0(param1 = None, param2 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	(argc -= 2)
	temp0 = 0
	while (temp0 <= argc): # inline for
		temp1 = param2[temp0]
		if param1:
			kernel.Load(param1, temp1)
		else:
			kernel.DisposeScript(temp1)
		#endif
		# for:reinit
		temp0.post('++')
	#end:loop
	kernel.DisposeScript(958)
#end:procedure

