#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 951
import sci_sh
import kernel
import PolyPath

class MoveFwd(PolyPath):
	#property vars (may be empty)
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			super._send(
				'init:', param1, (+
						param1._send('x:')
						kernel.SinMult(param1._send('heading:'), param2)
					), (param1._send('y:') - kernel.CosMult(param1._send('heading:'), param2)), (and
						(argc >= 3)
						param3
					)
			)
		else:
			super._send('init:')
		#endif
	#end:method

#end:class or instance

