#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 913
import sci_sh
import kernel
import Main

# Public Export Declarations
SCI.public_exports(
	proc913_0 = 0,
	proc913_1 = 1,
	proc913_2 = 2,
	proc913_3 = 3,
	proc913_4 = 4,
)

@SCI.procedure
def proc913_0(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	return (global137[(param1 / 16)] & (0x8000 >> (mod param1 16)))
#end:procedure

@SCI.procedure
def proc913_1(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	temp0 = proc913_0(param1)
	(global137[(param1 / 16)] |= (0x8000 >> (mod param1 16)))
	return temp0
#end:procedure

@SCI.procedure
def proc913_2(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	temp0 = proc913_0(param1)
	(global137[(param1 / 16)] &= (~ (0x8000 >> (mod param1 16))))
	return temp0
#end:procedure

@SCI.procedure
def proc913_3():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	global153.post('++')
	proc913_2(27)
	proc913_2(28)
	proc913_2(18)
#end:procedure

@SCI.procedure
def proc913_4(param1 = None, param2 = None, param3 = None, param4 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	temp3 = 0
	if kernel.IsObject(param2):
		temp1 = (param2 x:)
		temp2 = (param2 y:)
		if (argc == 3):
			temp3 = param3
		#endif
	else:
		temp1 = param2
		temp2 = param3
		if (argc == 4):
			temp3 = param4
		#endif
	#endif
	temp0 = kernel.GetAngle((param1 x:), (param1 y:), temp1, temp2)
	(param1 setHeading: temp0 (kernel.IsObject(temp3) and temp3))
#end:procedure

