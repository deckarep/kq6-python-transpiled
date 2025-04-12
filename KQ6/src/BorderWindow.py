#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 936
import sci_sh
import kernel
import Window

@SCI.procedure
def localproc_0(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, param6 = None, param7 = None, param8 = None, param9 = None, param10 = None, param11 = None, param12 = None, param13 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	temp0 = kernel.GetPort()
	kernel.SetPort(0)
	kernel.Graph(11, param1, param2, (param3 + 1), (param4 + 1), param13, param5, param12)
	(param1 -= param10)
	(param2 -= param10)
	(param4 += param10)
	(param3 += param10)
	kernel.Graph(11, param1, param2, (param1 + param10), param4, param13, param6, param12)
	kernel.Graph(11, (param3 - param10), param2, param3, param4, param13, param8, param12)
	temp1 = 0
	while (temp1 < param10): # inline for
		kernel.Graph(4, (param1 + temp1), (param2 + temp1), (-
			param3
			(temp1 + 1)
		), (param2 + temp1), param7, param12, -1)
		kernel.Graph(4, (param1 + temp1), (param4 - (temp1 + 1)), (-
			param3
			(temp1 + 1)
		), (param4 - (temp1 + 1)), param9, param12, -1)
		# for:reinit
		temp1.post('++')
	#end:loop
	if param11:
		kernel.Graph(11, (param1 + param11), param4, (param3 + param11), (+
			param4
			param11
		), param13, 0, param12)
		kernel.Graph(11, param3, (param2 + param11), (param3 + param11), param4, param13, 0, param12)
	#endif
	kernel.SetPort(temp0)
#end:procedure

@SCI.procedure
def localproc_1(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	(= temp1
		(cond
			case ((param1 bottom:) > 185):
				(185 - (param1 bottom:))
			#end:case
			case ((param1 top:) < 10):
				(10 - (param1 top:))
			#end:case
			else: 0#end:else
		)
	)
	(= temp0
		(cond
			case ((param1 right:) > 315):
				(315 - (param1 right:))
			#end:case
			case ((param1 left:) < 5):
				(5 - (param1 left:))
			#end:case
			else: 0#end:else
		)
	)
	(param1
		top: ((param1 top:) + temp1)
		bottom: ((param1 bottom:) + temp1)
		left: ((param1 left:) + temp0)
		right: ((param1 right:) + temp0)
	)
#end:procedure

class BorderWindow(SysWindow):
	#property vars (may be empty)
	back = 5
	topBordColor = 7
	lftBordColor = 6
	rgtBordColor = 4
	botBordColor = 3
	bevelWid = 3
	shadowWid = 2
	
	@classmethod
	def open():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.SetPort(0)
		temp1 = 1
		if (priority != -1):
			(temp1 |= 0x0002)
		#endif
		lsTop = (top - bevelWid)
		lsLeft = (left - bevelWid)
		lsRight = (+ right bevelWid shadowWid)
		lsBottom = (+ bottom bevelWid shadowWid)
		type = 128
		(super open:)
		localproc_0(top, left, bottom, right, back, topBordColor, lftBordColor, botBordColor, rgtBordColor, bevelWid, shadowWid, priority, temp1)
		temp0 = kernel.GetPort()
		kernel.SetPort(0)
		kernel.Graph(12, lsTop, lsLeft, lsBottom, lsRight, 1)
		kernel.SetPort(temp0)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super dispose:)
		kernel.SetPort(0)
	#end:method

#end:class or instance

class InsetWindow(BorderWindow):
	#property vars (may be empty)
	topBordColor = 5
	lftBordColor = 4
	rgtBordColor = 2
	botBordColor = 1
	ck = 3
	insideColor = 2
	topBordColor2 = 0
	lftBordColor2 = 1
	botBordColor2 = 5
	rgtBordColor2 = 4
	topBordHgt = 10
	botBordHgt = 24
	sideBordWid = 2
	shadWid = 0
	bevWid = 2
	xOffset = 0
	yOffset = 0
	
	@classmethod
	def open():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 1
		if (priority != -1):
			(temp0 |= 0x0002)
		#endif
		temp2 = top
		temp3 = left
		temp4 = bottom
		temp5 = right
		(top -= (bevelWid + topBordHgt))
		(left -= (bevelWid + sideBordWid))
		(bottom += (bevelWid + botBordHgt))
		(right += (bevelWid + sideBordWid))
		xOffset = (bevelWid + sideBordWid)
		yOffset = (bevelWid + topBordHgt)
		(super open:)
		localproc_0(temp2, temp3, temp4, temp5, insideColor, topBordColor2, lftBordColor2, botBordColor2, rgtBordColor2, bevWid, shadWid, priority, temp0)
		temp1 = kernel.GetPort()
		kernel.SetPort(0)
		kernel.Graph(12, (temp2 - bevWid), (temp3 - bevWid), (temp4 + bevWid), (+
			temp5
			bevWid
		), 1)
		kernel.SetPort(temp1)
	#end:method

#end:class or instance

