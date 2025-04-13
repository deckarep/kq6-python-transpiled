#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 944
import sci_sh
import kernel
import Dialog

@SCI.procedure
def localproc_0(param1 = None, param2 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	temp0 = (param2 - 1)
	while (temp0 > 0): # inline for
		temp15 = 0
		temp1 = 0
		while (temp1 < temp0): # inline for
			temp17 = (temp16 = (param1 + (temp1 * 13)) + 13)
			if (kernel.StrCmp(temp17, temp16) < 0):
				kernel.StrCpy(@temp2, temp16)
				kernel.StrCpy(temp16, temp17)
				kernel.StrCpy(temp17, @temp2)
				temp15 = 1
			#endif
			# for:reinit
			temp1.post('++')
		#end:loop
		(breakif (not temp15))
		# for:reinit
		temp0.post('--')
	#end:loop
#end:procedure

class FileSelector(DSelector):
	#property vars (may be empty)
	x = 13
	mask = 0
	nFiles = 0
	sort = 1
	
	@classmethod
	def readFiles(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (argc > 0):
			mask = param1
		#endif
		if (not mask):
			mask = r"""*.*"""
		#endif
		if text:
			kernel.Memory(3, text)
			text = 0
		#endif
		nFiles = 0
		temp9 = kernel.FileIO(8, mask, @temp0, 0)
		while temp9: # inline for
			nFiles.post('++')
			# for:reinit
			temp9 = kernel.FileIO(9, @temp0)
		#end:loop
		if (not text = kernel.Memory(2, ((nFiles * 13) + 1))):
			return 0
		#endif
		temp7 = 0
		temp8 = text
		
			(temp9 = kernel.FileIO(8, mask, @temp0, 0))
			(temp9 and (temp7 < nFiles))
			(temp9 = kernel.FileIO(9, @temp0))
			
			kernel.StrCpy(temp8, @temp0)
			temp7.post('++')
			(temp8 += 13)
			# for:reinit
			temp9 = kernel.FileIO(9, @temp0)
		#end:loop
		kernel.StrAt(text, (nFiles * 13), 0)
		if sort:
			localproc_0(text, nFiles)
		#endif
		return 1
	#end:method

	@classmethod
	def setSize():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('setSize:')
		kernel.TextSize(@temp0[0], r"""M""", font)
		nsRight = (nsLeft + (temp0[3] * x))
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if text:
			kernel.Memory(3, text)
			text = 0
		#endif
		super._send('dispose:')
	#end:method

#end:class or instance

