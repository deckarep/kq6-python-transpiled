#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 922
import sci_sh
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
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		nsRight = (nsLeft + (CelWide view loop cel))
		nsBottom = (nsTop + (CelHigh view loop cel))
	#end:method

#end:class or instance

class DButton(Class_255_0):
	#property vars (may be empty)
	type = 1
	state = 3
	text = 0
	font = 0
	
	@classmethod
	def dispose(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (text and ((not argc) or (not param1))):
			(Memory 3 (self text:))
		#endif
		(super dispose:)
	#end:method

	@classmethod
	def setSize():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(TextSize @temp0[0] text font 0 0)
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
	def track(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(EditControl self param1)
		return self
	#end:method

	@classmethod
	def setSize():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		font = global85
		(TextSize @temp0[0] r"""M""" font 0 0)
		nsBottom = (nsTop + temp0[2])
		nsRight = (nsLeft + ((* temp0[3] max 3) / 4))
		cursor = (StrLen text)
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
	def indexOf(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = text
		temp1 = 0
		while (temp1 < 300): # inline for
			if (0 == (StrLen temp0)):
				return -1
			#endif
			if (not (StrCmp param1 temp0)):
				return temp1
			#endif
			(temp0 += x)
			# for:reinit
			temp1++
		#end:loop
	#end:method

	@classmethod
	def at(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		return (text + (x * param1))
	#end:method

	@classmethod
	def setSize():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(TextSize @temp0[0] r"""M""" font 0 0)
		nsBottom = (+ nsTop 20 (temp0[2] * y))
		nsRight = (nsLeft + ((* temp0[3] x 3) / 4))
		topString = cursor = text
		mark = 0
	#end:method

	@classmethod
	def retreat(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 0
		while param1:

			if (cursor != text):
				temp0 = 1
				(cursor -= x)
				if mark:
					mark--
				else:
					(topString -= x)
				#endif
			else:
				(break)
			#endif
			param1--
		#end:loop
		(return
			if temp0:
				(self draw:)
				1
			#endif
		)
	#end:method

	@classmethod
	def advance(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not (StrAt cursor 0)):
			return
		#endif
		temp0 = 0
		while param1:

			if (StrAt cursor x):
				temp0 = 1
				(cursor += x)
				if ((mark + 1) < y):
					mark++
				else:
					(topString += x)
				#endif
			else:
				(break)
			#endif
			param1--
		#end:loop
		(return
			if temp0:
				(self draw:)
				1
			#endif
		)
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 claimed:):
			return 0
		#endif
		temp0 = 0
		match (param1 type:)
			case 4:
				(param1
					claimed:
						match (param1 message:)
							case 18176:
								(self retreat: 50)
							#end:case
							case 20224:
								(self advance: 50)
							#end:case
							case 20736:
								(self advance: (y - 1))
							#end:case
							case 18688:
								(self retreat: (y - 1))
							#end:case
							case 20480:
								(self advance: 1)
							#end:case
							case 18432:
								(self retreat: 1)
							#end:case
							else: 0#end:else
						#end:match
				)
			#end:case
			case 1:
				if (self check: param1):
					(param1 claimed: 1)
					(cond
						case ((param1 y:) < (nsTop + 10)):
							while True: #repeat
								(self retreat: 1)
								(breakif (not (proc255_0)))
							#end:loop
						#end:case
						case ((param1 y:) > (nsBottom - 10)):
							while True: #repeat
								(self advance: 1)
								(breakif (not (proc255_0)))
							#end:loop
						#end:case
						else:
							(TextSize @temp5[0] r"""M""" font 0 0)
							if 
								(>
									(= temp4
										(/
											((param1 y:) - (nsTop + 10))
											temp5[2]
										)
									)
									mark
								)
								(self advance: (temp4 - mark))
							else:
								(self retreat: (mark - temp4))
							#endif
						#end:else
					)
				#endif
			#end:case
		#end:match
		(self if ((param1 claimed:) and (state & 0x0002)) else 0)
	#end:method

#end:class or instance

class Controls(List):
	#property vars (may be empty)
	@classmethod
	def draw():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self eachElementDo: #setSize)
		(self eachElementDo: #draw)
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 claimed:):
			return 0
		#endif
		if 
			(and
				temp0 = (self firstTrue: #handleEvent param1)
				(not (temp0 checkState: 2))
			)
			(temp0 doit:)
			temp0 = 0
		#endif
		return temp0
	#end:method

#end:class or instance

