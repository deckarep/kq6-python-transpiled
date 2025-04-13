#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 933
import sci_sh
import kernel
import Main
import System

class PseudoMouse(Code):
	#property vars (may be empty)
	cursorInc = 2
	minInc = 2
	maxInc = 20
	prevDir = 0
	joyInc = 5
	
	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = param1._send('type:')
		temp1 = param1._send('message:')
		temp2 = param1._send('modifiers:')
		if (temp0 & 0x0040):
			prevDir = temp1
			(= cursorInc
				if (temp0 & 0x0004):
					(minInc if (temp2 & 0x0003) else maxInc)
				else:
					joyInc
				#endif
			)
			(cond
				case (temp0 & 0x0004):
					if prevDir:
						self._send('doit:')
					else:
						param1._send('claimed:', 0)
						return
					#endif
				#end:case
				case prevDir:
					self._send('start:')
				#end:case
				else:
					self._send('stop:')
				#end:else
			)
			param1._send('claimed:', 1)
			return
		#endif
	#end:method

	@classmethod
	def start(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			prevDir = param1
		#endif
		global78._send('add:', self)
	#end:method

	@classmethod
	def stop():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		prevDir = 0
		global78._send('delete:', self)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = global24._send('x:')
		temp1 = global24._send('y:')
		match prevDir
			case 1:
				(temp1 -= cursorInc)
			#end:case
			case 2:
				(temp0 += cursorInc)
				(temp1 -= cursorInc)
			#end:case
			case 3:
				(temp0 += cursorInc)
			#end:case
			case 4:
				(temp0 += cursorInc)
				(temp1 += cursorInc)
			#end:case
			case 5:
				(temp1 += cursorInc)
			#end:case
			case 6:
				(temp0 -= cursorInc)
				(temp1 += cursorInc)
			#end:case
			case 7:
				(temp0 -= cursorInc)
			#end:case
			case 8:
				(temp0 -= cursorInc)
				(temp1 -= cursorInc)
			#end:case
		#end:match
		global1._send('setCursor:', global19, 1, temp0, temp1)
	#end:method

#end:class or instance

