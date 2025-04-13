#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 985
import sci_sh
import kernel
import System

class Flags(Obj):
	#property vars (may be empty)
	size = 0
	array = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (size and (not array)):
			self._send('setSize:', size)
		#endif
	#end:method

	@classmethod
	def setSize(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = (param1 / 16)
		if (mod param1 16):
			temp0.post('++')
		#endif
		size = (temp0 * 16)
		array = kernel.Memory(1, (temp0 * 2))
		temp1 = 0
		while (temp1 < temp0): # inline for
			kernel.Memory(6, (array + (temp1 * 2)), 0)
			# for:reinit
			temp1.post('++')
		#end:loop
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if array:
			kernel.Memory(3, array)
			array = 0
		#endif
		super._send('dispose:')
	#end:method

	@classmethod
	def set(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		while argc:

			temp1 = ((param1[argc.post('--')] / 16) * 2)
			(= temp0
				(|
					temp0 = kernel.Memory(5, (array + temp1))
					(0x8000 >> (mod param1[argc] 16))
				)
			)
			kernel.Memory(6, (array + temp1), temp0)
		#end:loop
	#end:method

	@classmethod
	def clear(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		while argc:

			temp1 = ((param1[argc.post('--')] / 16) * 2)
			(= temp0
				(&
					temp0 = kernel.Memory(5, (array + temp1))
					~(0x8000 >> (mod param1[argc] 16))
				)
			)
			kernel.Memory(6, (array + temp1), temp0)
		#end:loop
	#end:method

	@classmethod
	def test(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp1 = ((param1 / 16) * 2)
		(return
			(temp0 = kernel.Memory(5, (array + temp1)) & (0x8000 >> (mod param1 16)))
		)
	#end:method

#end:class or instance

