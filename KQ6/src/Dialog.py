#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 922
import sci_sh
import kernel
import Main
import Interface
import System

class DIcon(Class_255_0):
	#property vars (may be empty)
	type = 4
	view = 0
	loop = 0
	cel = 0
	
	@classmethod
	def setSize():
		nsRight = (nsLeft + kernel.CelWide(view, loop, cel))
		nsBottom = (nsTop + kernel.CelHigh(view, loop, cel))
	#end:method

#end:class or instance

class DButton(Class_255_0):
	#property vars (may be empty)
	type = 1
	state = 3
	text = 0
	font = 0
	
	@classmethod
	def dispose(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (text and ((not argc) or (not param1))):
			kernel.Memory(3, self._send('text:'))
		#endif
		super._send('dispose:')
	#end:method

	@classmethod
	def setSize():
		kernel.TextSize(@temp0[0], text, font, 0, 0)
		(temp0[2] += 2)
		(temp0[3] += 2)
		nsBottom = (nsTop + temp0[2])
		temp0[3] = (((temp0[3] + 15) / 16) * 16)
		nsRight = (temp0[3] + nsLeft)
	#end:method

#end:class or instance

class DEdit(Class_255_0):
	#property vars (may be empty)
	type = 3
	state = 1
	text = 0
	font = 0
	max = 0
	cursor = 0
	
	@classmethod
	def track(param1 = None, *rest):
		kernel.EditControl(self, param1)
		return self
	#end:method

	@classmethod
	def setSize():
		font = global85
		kernel.TextSize(@temp0[0], r"""M""", font, 0, 0)
		nsBottom = (nsTop + temp0[2])
		nsRight = (nsLeft + ((* temp0[3] max 3) / 4))
		cursor = kernel.StrLen(text)
	#end:method

#end:class or instance

class DSelector(Class_255_0):
	#property vars (may be empty)
	type = 6
	font = 0
	x = 20
	y = 6
	text = 0
	cursor = 0
	topString = 0
	mark = 0
	
	@classmethod
	def indexOf(param1 = None, *rest):
		temp0 = text
		temp1 = 0
		while (temp1 < 300): # inline for
			if (0 == kernel.StrLen(temp0)):
				return -1
			#endif
			if (not kernel.StrCmp(param1, temp0)):
				return temp1
			#endif
			(temp0 += x)
			# for:reinit
			temp1.post('++')
		#end:loop
	#end:method

	@classmethod
	def at(param1 = None, *rest):
		return (text + (x * param1))
	#end:method

	@classmethod
	def setSize():
		kernel.TextSize(@temp0[0], r"""M""", font, 0, 0)
		nsBottom = (+ nsTop 20 (temp0[2] * y))
		nsRight = (nsLeft + ((* temp0[3] x 3) / 4))
		topString = cursor = text
		mark = 0
	#end:method

	@classmethod
	def retreat(param1 = None, *rest):
		temp0 = 0
		while param1:

			if (cursor != text):
				temp0 = 1
				(cursor -= x)
				if mark:
					mark.post('--')
				else:
					(topString -= x)
				#endif
			else:
				(break)
			#endif
			param1.post('--')
		#end:loop
		(return
			if temp0:
				self._send('draw:')
				1
			#endif
		)
	#end:method

	@classmethod
	def advance(param1 = None, *rest):
		if (not kernel.StrAt(cursor, 0)):
			return
		#endif
		temp0 = 0
		while param1:

			if kernel.StrAt(cursor, x):
				temp0 = 1
				(cursor += x)
				if ((mark + 1) < y):
					mark.post('++')
				else:
					(topString += x)
				#endif
			else:
				(break)
			#endif
			param1.post('--')
		#end:loop
		(return
			if temp0:
				self._send('draw:')
				1
			#endif
		)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		if param1._send('claimed:'):
			return 0
		#endif
		temp0 = 0
		match param1._send('type:')
			case 4:
				param1._send(
					'claimed:', match param1._send('message:')
							case 18176:
								self._send('retreat:', 50)
							#end:case
							case 20224:
								self._send('advance:', 50)
							#end:case
							case 20736:
								self._send('advance:', (y - 1))
							#end:case
							case 18688:
								self._send('retreat:', (y - 1))
							#end:case
							case 20480:
								self._send('advance:', 1)
							#end:case
							case 18432:
								self._send('retreat:', 1)
							#end:case
							else: 0#end:else
						#end:match
				)
			#end:case
			case 1:
				if self._send('check:', param1):
					param1._send('claimed:', 1)
					(cond
						case (param1._send('y:') < (nsTop + 10)):
							while True: #repeat
								self._send('retreat:', 1)
								(breakif (not proc255_0()))
							#end:loop
						#end:case
						case (param1._send('y:') > (nsBottom - 10)):
							while True: #repeat
								self._send('advance:', 1)
								(breakif (not proc255_0()))
							#end:loop
						#end:case
						else:
							kernel.TextSize(@temp5[0], r"""M""", font, 0, 0)
							if 
								(>
									(= temp4
										(/
											(param1._send('y:') - (nsTop + 10))
											temp5[2]
										)
									)
									mark
								)
								self._send('advance:', (temp4 - mark))
							else:
								self._send('retreat:', (mark - temp4))
							#endif
						#end:else
					)
				#endif
			#end:case
		#end:match
		(self if (param1._send('claimed:') and (state & 0x0002)) else 0)
	#end:method

#end:class or instance

class Controls(List):
	#property vars (may be empty)
	@classmethod
	def draw():
		self._send('eachElementDo:', #setSize)
		self._send('eachElementDo:', #draw)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		if param1._send('claimed:'):
			return 0
		#endif
		if 
			(and
				temp0 = self._send('firstTrue:', #handleEvent, param1)
				(not temp0._send('checkState:', 2))
			)
			temp0._send('doit:')
			temp0 = 0
		#endif
		return temp0
	#end:method

#end:class or instance

