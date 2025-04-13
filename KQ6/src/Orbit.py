#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 986
import sci_sh
import kernel
import Main
import Motion
import System

class Orbit(Motion):
	#property vars (may be empty)
	centerObj = 0
	radius = 50
	xTilt = 0
	yTilt = 0
	angleStep = 10
	winding = 1
	curAngle = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, param6 = None, param7 = None, param8 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (argc >= 1):
			client = param1
			if (argc >= 2):
				centerObj = param2
				if (argc >= 3):
					radius = param3
					if (argc >= 4):
						xTilt = param4
						if (argc >= 5):
							yTilt = param5
							if (argc >= 6):
								angleStep = param6
								if (argc >= 7):
									winding = param7
									if (argc >= 8):
										curAngle = param8
									#endif
								#endif
							#endif
						#endif
					#endif
				#endif
			#endif
		#endif
		if centerObj:
			temp0 = centerObj._send('x:')
			temp1 = centerObj._send('y:')
		else:
			temp0 = 160
			temp1 = 100
		#endif
		temp2 = kernel.SinMult(curAngle, radius)
		temp3 = kernel.CosMult((yTilt + global31), kernel.CosMult(curAngle, radius))
		if xTilt:
			temp2 = kernel.CosMult(xTilt, temp2)
			(temp3 += kernel.SinMult(xTilt, temp2))
		#endif
		x = (temp0 + temp2)
		y = (temp1 - temp3)
		curAngle = proc999_1((curAngle + (winding * angleStep)), 360)
		super._send('init:', client, x, y)
	#end:method

	@classmethod
	def moveDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('init:')
	#end:method

#end:class or instance

