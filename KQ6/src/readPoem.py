#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 97
import sci_sh
import kernel
import Main
import System

# Public Export Declarations
SCI.public_exports(
	readPoem = 0,
)

@SCI.instance
class readPoem(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(97)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global91._send('say:', 30, 5, 0, 0, self, 907)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

