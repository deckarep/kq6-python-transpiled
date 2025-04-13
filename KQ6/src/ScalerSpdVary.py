#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 211
import sci_sh
import kernel
import Print
import System

# Public Export Declarations
SCI.public_exports(
	ScalerSpdVary = 0,
)

class ScalerSpdVary(Code):
	#property vars (may be empty)
	client = 0
	frontY = 190
	backY = 0
	frontSize = 100
	backSize = 0
	slopeNum = 0
	slopeNumSpd = 0
	slopeNumStp = 0
	slopeDen = 0
	const = 0
	constSpd = 0
	constStp = 0
	frontSpeed = 6
	backSpeed = 5
	frontStep = 3
	backStep = 2
	whichSel = 1
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, param6 = None, param7 = None, param8 = None, param9 = None, param10 = None, *rest):
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
		if (argc > 5):
			whichSel = param6
			if (argc > 6):
				frontSpeed = param7
				backSpeed = param8
				slopeNumSpd = (frontSpeed - backSpeed)
				constSpd = (backSpeed - ((slopeNumSpd * backY) / slopeDen))
				if (argc > 8):
					frontStep = param9
					backStep = param10
					slopeNumStp = (frontStep - backStep)
					constStp = (backStep - ((slopeNumStp * backY) / slopeDen))
				#endif
			#endif
		#endif
		const = (backSize - ((slopeNum * backY) / slopeDen))
		self._send('doit:')
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case 
				(<
					(= temp0
						if (not whichSel):
							client._send('y:')
						else:
							client._send('x:')
						#endif
					)
					backY
				):
				temp1 = backSize
				temp2 = backSpeed
				temp3 = backStep
			#end:case
			case (temp0 > frontY):
				temp1 = frontSize
				temp2 = frontSpeed
				temp3 = frontStep
			#end:case
			else:
				temp1 = (((slopeNum * temp0) / slopeDen) + const)
				if constSpd:
					temp2 = (((slopeNumSpd * temp0) / slopeDen) + constSpd)
					if constStp:
						(= temp3
							(((slopeNumStp * temp0) / slopeDen) + constStp)
						)
					#endif
				#endif
			#end:else
		)
		if constSpd:
			client._send('moveSpeed:', temp2)
			if 
				(and
					constStp
					(not
						(and
							(client._send('xStep:') == temp3)
							(client._send('yStep:') == temp3)
						)
					)
				)
				client._send('setStep:', temp3, temp3, 1)
			#endif
		#endif
		temp1 = ((temp1 * 128) / 100)
		client._send('scaleX:', temp1, 'scaleY:', temp1)
	#end:method

#end:class or instance

