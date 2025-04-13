#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 993
import sci_sh
import kernel
import System

class File(Obj):
	#property vars (may be empty)
	handle = 0
	
	@classmethod
	def open(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(= handle
			match argc
				case 0:
					kernel.FileIO(0, name, 0)
				#end:case
				case 1:
					kernel.FileIO(0, name, param1)
				#end:case
				else: 0#end:else
			#end:match
		)
		if (handle == -1):
			handle = 0
		#endif
		return (self if handle else 0)
	#end:method

	@classmethod
	def write(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not handle):
			self._send('open:')
		#endif
		(return
			if handle:
				kernel.FileIO(3, handle, param1, param2)
			else:
				0
			#endif
		)
	#end:method

	@classmethod
	def writeString(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not handle):
			self._send('open:')
		#endif
		if handle:
			temp0 = 0
			while (temp0 < argc): # inline for
				if (not kernel.FileIO(6, handle, param1[temp0])):
					return 0
				#endif
				# for:reinit
				temp0.post('++')
			#end:loop
		#endif
		return 1
	#end:method

	@classmethod
	def read(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (argc != 2):
			return 0
		#endif
		if (not handle):
			self._send('open:', 1)
		#endif
		(return
			if handle:
				kernel.FileIO(2, handle, param1, param2)
			else:
				0
			#endif
		)
	#end:method

	@classmethod
	def readString(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (argc != 2):
			return 0
		#endif
		if (not handle):
			self._send('open:', 1)
		#endif
		(return
			if handle:
				kernel.FileIO(5, param1, param2, handle)
			else:
				0
			#endif
		)
	#end:method

	@classmethod
	def rename(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not temp0 = kernel.FileIO(11, name, param1)):
			name = param1
		#endif
		return temp0
	#end:method

	@classmethod
	def seek(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = (param2 if (argc >= 2) else 0)
		if (not handle):
			self._send('open:', 1)
		#endif
		(return
			if handle:
				kernel.FileIO(7, handle, param1, temp0)
			else:
				0
			#endif
		)
	#end:method

	@classmethod
	def close():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if handle:
			kernel.FileIO(1, handle)
			handle = 0
		#endif
	#end:method

	@classmethod
	def delete():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if handle:
			self._send('close:')
		#endif
		kernel.FileIO(4, name)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('close:')
		super._send('dispose:')
	#end:method

	@classmethod
	def showStr(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.Format(param1, r"""File: %s""", name)
	#end:method

#end:class or instance

