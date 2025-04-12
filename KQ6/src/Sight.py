#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 982
import sci_sh
import kernel
import Main

# Public Export Declarations
SCI.public_exports(
	proc982_0 = 0,
	proc982_1 = 1,
	proc982_2 = 2,
)

@SCI.procedure
def proc982_0(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	(return
		(not
			((<= 0 (param1 x:) 319) and (<= 0 ((param1 y:) - (param1 z:)) 189))
		)
	)
#end:procedure

@SCI.procedure
def proc982_1(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	temp0 = param2
	temp1 = param3
	temp2 = param4
	if (argc < 4):
		temp2 = 32767
		if (argc < 3):
			if (argc < 2):
				temp0 = global0
			#endif
			(= temp1
				(-
					360
					if (temp0 == global0):
						(2 * (temp0 sightAngle:))
					#endif
				)
			)
		#endif
	#endif
	temp3 = (param1 x:)
	temp4 = (param1 y:)
	temp5 = (temp0 x:)
	temp6 = (temp0 y:)
	(return
		(and
			(param1 != temp0)
			(or
				(<
					(temp1 / 2)
					kernel.Abs(proc982_2(kernel.GetAngle(temp5, temp6, temp3, temp4), (temp0
						heading:
					)))
				)
				(temp2 < kernel.GetDistance(temp5, temp6, temp3, temp4, global31))
			)
		)
	)
#end:procedure

@SCI.procedure
def proc982_2(param1 = None, param2 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	if (argc >= 2):
		(param1 -= param2)
	#endif
	(return
		(cond
			case (param1 <= -180):
				(param1 + 360)
			#end:case
			case (param1 > 180):
				(param1 - 360)
			#end:case
			else: param1#end:else
		)
	)
#end:procedure

