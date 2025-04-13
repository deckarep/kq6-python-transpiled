#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 912
import sci_sh
import kernel
import Window

class Kq6Window(SysWindow):
	#property vars (may be empty)
	color = 16
	back = 19
	colorOne = 32
	colorFive = 18
	tlColorTwo = 17
	tlColorThree = 18
	tlColorFour = 17
	brColorTwo = 18
	brColorThree = 17
	brColorFour = 16
	
	@classmethod
	def open():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 1
		if (priority != -1):
			(temp0 |= 0x0002)
		#endif
		lsTop = (top - 5)
		lsLeft = (left - 5)
		lsRight = (right + 6)
		lsBottom = (bottom + 6)
		type = 128
		priority = 15
		super._send('open:')
		temp1 = kernel.GetPort()
		kernel.SetPort(0)
		self._send('drawEdgedWindow:', temp0)
		kernel.DrawCel(930, 0, 0, (left - 5), (top - 5), -1)
		kernel.DrawCel(930, 0, 1, (left - 5), (bottom - 1), -1)
		kernel.DrawCel(930, 0, 2, (right - 1), (top - 5), -1)
		kernel.DrawCel(930, 0, 3, (right - 1), (bottom - 1), -1)
		kernel.Graph(12, lsTop, lsLeft, lsBottom, lsRight, 1)
		kernel.SetPort(temp1)
	#end:method

	@classmethod
	def drawEdgedWindow(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.Graph(11, top, left, (bottom + 1), (right + 1), param1, back, priority)
		temp2 = 1
		while (temp2 < 6): # inline for
			(= temp3
				match temp2
					case 1: colorOne#end:case
					case 2: tlColorTwo#end:case
					case 3: tlColorThree#end:case
					case 4: tlColorFour#end:case
					case 5: colorFive#end:case
				#end:match
			)
			kernel.Graph(4, (top - temp2), (left - temp2), (top - temp2), (+
				right
				temp2
			), temp3, priority, -1)
			kernel.Graph(4, (top - temp2), (left - temp2), (bottom + temp2), (-
				left
				temp2
			), temp3, priority, -1)
			# for:reinit
			temp2.post('++')
		#end:loop
		temp2 = 1
		while (temp2 < 6): # inline for
			(= temp3
				match temp2
					case 1: colorOne#end:case
					case 2: brColorTwo#end:case
					case 3: brColorThree#end:case
					case 4: brColorFour#end:case
					case 5: colorFive#end:case
				#end:match
			)
			kernel.Graph(4, (bottom + temp2), (left - temp2), (bottom + temp2), (+
				right
				temp2
			), temp3, priority, -1)
			kernel.Graph(4, (top - temp2), (right + temp2), (bottom + temp2), (+
				right
				temp2
			), temp3, priority, -1)
			# for:reinit
			temp2.post('++')
		#end:loop
	#end:method

#end:class or instance

