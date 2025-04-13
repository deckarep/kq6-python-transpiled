#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 991
import sci_sh
import kernel
import Main
import Motion

class Jump(Motion):
	#property vars (may be empty)
	x = 20000
	y = 20000
	gx = 0
	gy = 3
	xStep = 20000
	yStep = 0
	signal = 0
	illegalBits = 0
	waitApogeeX = 1
	waitApogeeY = 1
	
	@classmethod
	def init(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		client = param1
		if (argc == 2):
			caller = param2
		#endif
		illegalBits = client._send('illegalBits:')
		signal = client._send('signal:')
		client._send('illegalBits:', 0, 'setPri:')
		if (xStep == 20000):
			(= xStep
				(cond
					case 
						(or
							(temp0 = client._send('heading:') > 330)
							(temp0 < 30)
							(< 150 temp0 210)
						):
						0
					#end:case
					case (temp0 < 180):
						client._send('xStep:')
					#end:case
					else:
						-client._send('xStep:')
					#end:else
				)
			)
		#endif
		if (not (waitApogeeX and ((xStep * gx) < 0))):
			waitApogeeX = 0
		#endif
		if (not (waitApogeeY and ((yStep * gy) < 0))):
			waitApogeeY = 0
		#endif
		b-moveCnt = global88
		self._send('setTest:')
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (kernel.Abs((global88 - b-moveCnt)) >= client._send('moveSpeed:')):
			b-moveCnt = global88
			xLast = client._send('x:')
			yLast = client._send('y:')
			client._send('x:', (xLast + xStep), 'y:', (yLast + yStep))
			temp0 = xStep
			temp1 = yStep
			(xStep += gx)
			(yStep += gy)
			if 
				(and
					(not waitApogeeX)
					(x != 20000)
					(0 <= (dx * (client._send('x:') - x)))
				)
				client._send('x:', x)
				self._send('moveDone:')
				return
			#endif
			if 
				(and
					(not waitApogeeY)
					(y != 20000)
					(0 <= (dy * (client._send('y:') - y)))
				)
				client._send('y:', y)
				self._send('moveDone:')
				return
			#endif
			if ((temp0 * xStep) <= 0):
				waitApogeeX = 0
				self._send('setTest:')
			#endif
			if ((temp1 * yStep) <= 0):
				waitApogeeY = 0
				self._send('setTest:')
			#endif
		#endif
	#end:method

	@classmethod
	def moveDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		client._send('illegalBits:', illegalBits, 'signal:', signal)
		if caller:
			global37 = 1
			completed = 1
		#endif
	#end:method

	@classmethod
	def setTest():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(= dx
			if ((client._send('x:') > x) or ((client._send('x:') == x) and (xStep > 0))):
				-1
			else:
				1
			#endif
		)
		(= dy
			if ((client._send('y:') > y) or ((client._send('y:') == y) and (yStep > 0))):
				-1
			else:
				1
			#endif
		)
	#end:method

	@classmethod
	def motionCue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		client._send('mover:', 0)
		if (completed and kernel.IsObject(caller)):
			caller._send('cue:')
		#endif
		self._send('dispose:')
	#end:method

#end:class or instance

class JumpTo(Jump):
	#property vars (may be empty)
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		client = param1
		x = param2
		y = param3
		if ((x == param1._send('x:')) and (y == param1._send('y:'))):
			illegalBits = client._send('illegalBits:')
			signal = client._send('signal:')
			self._send('moveDone:')
			return
		#endif
		temp0 = (x - param1._send('x:'))
		temp1 = (y - param1._send('y:'))
		kernel.SetJump(self, temp0, temp1, gy)
		if (not temp0):
			x = 20000
		#endif
		if (not temp1):
			y = 20000
		#endif
		match argc
			case 3:
				super._send('init:', param1)
			#end:case
			case 4:
				super._send('init:', param1, param4)
			#end:case
		#end:match
	#end:method

	@classmethod
	def moveDone():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (x != 20000):
			client._send('x:', x)
		#endif
		if (y != 20000):
			client._send('y:', y)
		#endif
		super._send('moveDone:')
	#end:method

#end:class or instance

