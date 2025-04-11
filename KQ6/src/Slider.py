#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 934
import sci_sh
import IconBar
import System

class Slider(IconI):
	#property vars (may be empty)
	sliderView = 0
	sliderLoop = 0
	sliderCel = 0
	sTop = 0
	sLeft = 0
	sRight = 0
	maxY = 0
	minY = 0
	underBits = 0
	yStep = 1
	theObj = 0
	selector = 0
	bottomValue = 0
	topValue = 0
	
	@classmethod
	def show():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super show: &rest)
		if (not sRight):
			sLeft = nsLeft
			sRight = nsRight
			maxY = (nsBottom - (CelHigh sliderView sliderLoop sliderCel))
			minY = nsTop
		#endif
		sTop = (self valueToPosn:)
		(DrawCel sliderView sliderLoop sliderCel sLeft sTop -1)
		(Graph 12 (nsTop - 1) (nsLeft - 1) (2 + nsBottom) (2 + nsRight) 1)
	#end:method

	@classmethod
	def select(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (argc and param1):
			while ((temp0 = (Event new:) type:) != 2):

				(temp0 localize:)
				(cond
					case ((temp0 y:) < (sTop - yStep)):
						(self move: yStep (not (signal & 0x0200)))
					#end:case
					case ((temp0 y:) > (sTop + yStep)):
						(self move: (- yStep) (not (signal & 0x0200)))
					#end:case
				)
				(temp0 dispose:)
			#end:loop
			if (signal & 0x0200):
				(self doit: (self posnToValue: sTop))
			#endif
			(temp0 dispose:)
		else:
			return 1
		#endif
	#end:method

	@classmethod
	def highlight():#end:method

	@classmethod
	def move(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp7 = ((not argc) or param2)
		temp5 = (proc999_0 param1)
		temp4 = param1
		while (yStep <= (Abs temp4)): # inline for
			temp0 = (sTop - (temp5 * yStep))
			temp1 = (CelHigh sliderView sliderLoop sliderCel)
			(= sTop
				(cond
					case (temp0 < minY): minY#end:case
					case (temp0 > maxY): maxY#end:case
					else: temp0#end:else
				)
			)
			temp2 = (PicNotValid)
			(PicNotValid 1)
			(DrawCel view loop cel nsLeft nsTop -1)
			(DrawCel sliderView sliderLoop sliderCel sLeft sTop -1)
			(Graph 12 (nsTop - 1) (nsLeft - 1) (2 + nsBottom) (2 + nsRight) 1)
			(PicNotValid temp2)
			temp3 = (self posnToValue: sTop)
			(= temp6
				if temp7:
					(self doit: temp3)
				else:
					(self doit:)
				#endif
			)
			# for:reinit
			(temp4 -= (yStep * temp5))
		#end:loop
		return temp6
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if theObj:
			(proc999_7 theObj selector &rest)
		#endif
	#end:method

	@classmethod
	def posnToValue(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(+
				bottomValue
				(((maxY - param1) * (topValue - bottomValue)) / (maxY - minY))
			)
		)
	#end:method

	@classmethod
	def valueToPosn(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(cond
				case 
					(and
						(<
							(= temp0
								if argc:
									param1
								else:
									(self doit:)
								#endif
							)
							topValue
						)
						(temp0 < bottomValue)
					):
					(maxY if (bottomValue < topValue) else minY)
				#end:case
				case ((temp0 > topValue) and (temp0 > bottomValue)):
					(minY if (bottomValue < topValue) else maxY)
				#end:case
				else:
					(+
						minY
						(/
							((Abs (topValue - temp0)) * (maxY - minY))
							(Abs (topValue - bottomValue))
						)
					)
				#end:else
			)
		)
	#end:method

	@classmethod
	def advance():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self
			move:
				(proc999_3
					yStep
					(-
						sTop
						(self
							valueToPosn:
								(+
									(self doit:)
									(proc999_0 (topValue - bottomValue))
								)
						)
					)
				)
				(not (signal & 0x0200))
		)
		if (signal & 0x0200):
			(self doit: (self posnToValue: sTop))
		#endif
	#end:method

	@classmethod
	def retreat():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self
			move:
				(proc999_2
					(- yStep)
					(-
						sTop
						(self
							valueToPosn:
								(-
									(self doit:)
									(proc999_0 (topValue - bottomValue))
								)
						)
					)
				)
				(not (signal & 0x0200))
		)
		if (signal & 0x0200):
			(self doit: (self posnToValue: sTop))
		#endif
	#end:method

#end:class or instance

