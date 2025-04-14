#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 935
import sci_sh
import kernel
import Print
import System

class Scaler(Code):
	#property vars (may be empty)
	client = 0
	frontY = 190
	backY = 0
	frontSize = 100
	backSize = 0
	slopeNum = 0
	slopeDen = 0
	const = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			client = param1
			frontSize = param2
			backSize = param3
			frontY = param4
			backY = param5
		#endif
		slopeNum = (frontSize - backSize)
		if (not slopeDen = (frontY - backY)):
			proc921_0(r"""<Scaler> frontY cannot be equal to backY""")
			return 0
		#endif
		const = (backSize - ((slopeNum * backY) / slopeDen))
		self._send('doit:')
	#end:method

	@classmethod
	def doit():
		(cond
			case (temp0 = client._send('y:') < backY):
				temp1 = backSize
			#end:case
			case (temp0 > frontY):
				temp1 = frontSize
			#end:case
			else:
				temp1 = (((slopeNum * temp0) / slopeDen) + const)
			#end:else
		)
		temp1 = ((temp1 * 128) / 100)
		client._send('scaleX:', temp1, 'scaleY:', temp1)
	#end:method

#end:class or instance

