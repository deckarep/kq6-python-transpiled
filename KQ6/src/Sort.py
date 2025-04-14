#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 966
import sci_sh
import kernel
import System

# Public Export Declarations
SCI.public_exports(
	proc966_0 = 0,
)

@SCI.procedure
def proc966_0(param1 = None, param2 = None, *rest):
	temp3 = List._send('new:')
	while temp1 = kernel.FirstNode(param1._send('elements:')):

		temp2 = kernel.NodeValue(temp1)
		while temp1:

			if param2._send('doit:', temp0 = kernel.NodeValue(temp1), temp2, &rest):
				temp2 = temp0
			#endif
			temp1 = kernel.NextNode(temp1)
		#end:loop
		TE._send('doit:', temp2, param1, temp3)
	#end:loop
	temp3._send('eachElementDo:', #perform, TE, temp3, param1, 'dispose:')
#end:procedure

@SCI.instance
class TE(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, param2 = None, param3 = None, *rest):
		param3._send('addToEnd:', param1)
		param2._send('delete:', param1)
	#end:method

#end:class or instance

