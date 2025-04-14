#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 926
import sci_sh
import kernel
import Main
import System

# Public Export Declarations
SCI.public_exports(
	proc926_0 = 0,
	proc926_1 = 1,
)

@SCI.procedure
def proc926_0(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	(cond
		case (not argc):
			temp0 = global2._send('obstacles:')
		#end:case
		case param1._send('isKindOf:', Collect):
			temp0 = param1
		#end:case
		else:
			param1._send('perform:', flipPoly)
			return
		#end:else
	)
	temp0._send('eachElementDo:', #perform, flipPoly)
	kernel.DisposeScript(926)
#end:procedure

@SCI.procedure
def proc926_1(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	if (not argc):
		global32._send('eachElementDo:', #perform, flipFeature)
	else:
		temp0 = 0
		while (temp0 < argc): # inline for
			if param1[temp0]._send('isKindOf:', Collect):
				param1[temp0]._send('eachElementDo:', #perform, flipFeature)
			else:
				param1[temp0]._send('perform:', flipFeature)
			#endif
			# for:reinit
			temp0.post('++')
		#end:loop
	#endif
	kernel.DisposeScript(926)
#end:procedure

@SCI.instance
class flipPoly(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		temp1 = kernel.Memory(1, (4 * temp2 = param1._send('size:')))
		temp0 = 0
		while (temp0 < temp2): # inline for
			kernel.Memory(6, (temp1 + (4 * temp0)), (-
				320
				kernel.Memory(5, (-
					(param1._send('points:') + (4 * temp2))
					(4 + (4 * temp0))
				))
			))
			kernel.Memory(6, (+ temp1 (4 * temp0) 2), kernel.Memory(5, (-
				(param1._send('points:') + (4 * temp2))
				(2 + (4 * temp0))
			)))
			# for:reinit
			temp0.post('++')
		#end:loop
		if param1._send('dynamic:'):
			kernel.Memory(3, param1._send('points:'))
		#endif
		param1._send('points:', temp1, 'dynamic:', 1)
	#end:method

#end:class or instance

@SCI.instance
class flipFeature(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		if kernel.IsObject(param1._send('onMeCheck:')):
			proc926_0(param1._send('onMeCheck:'))
		else:
			temp0 = param1._send('nsLeft:')
			param1._send('nsLeft:', (320 - param1._send('nsRight:')), 'nsRight:', (320 - temp0))
		#endif
	#end:method

#end:class or instance

