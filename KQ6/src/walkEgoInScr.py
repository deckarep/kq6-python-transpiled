#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 12
import sci_sh
import kernel
import Main
import PolyPath
import System

# Public Export Declarations
SCI.public_exports(
	proc12_0 = 0,
	proc12_1 = 1,
	proc12_2 = 2,
	walkEgoInScr = 3,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.procedure
def proc12_1(param1 = None, param2 = None, param3 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	temp0 = 0
	match global12
		case global2._send('north:'):
			global0._send('posn:', param1, -60)
		#end:case
		case global2._send('south:'):
			global0._send('posn:', param1, 250)
		#end:case
		case global2._send('east:'):
			global0._send('posn:', 370, param2)
		#end:case
		case global2._send('west:'):
			global0._send('posn:', -20, param2)
		#end:case
		else:
			temp0 = 1
			global0._send('posn:', param1, param2)
		#end:else
	#end:match
	if (argc > 2):
		temp1 = (global0._send('x:') - param1)
		temp2 = (global0._send('y:') - param2)
		localproc_0(@temp1, @temp2, param3)
		global0._send('reset:', 'posn:', (param1 + temp1), (param2 + temp2))
	#endif
	if (not temp0):
		local0 = param1
		local1 = param2
		global2._send('setScript:', walkEgoInScr)
	else:
		kernel.DisposeScript(12)
	#endif
#end:procedure

@SCI.procedure
def proc12_0(param1 = None, param2 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	global1._send('handsOff:')
	match param1
		case 1:
			temp0 = 0
			temp1 = -70
			temp2 = global2._send('north:')
		#end:case
		case 3:
			temp0 = 0
			temp1 = 70
			temp2 = global2._send('south:')
		#end:case
		case 2:
			temp0 = 20
			temp1 = 0
			temp2 = global2._send('east:')
		#end:case
		case 4:
			temp0 = -20
			temp1 = 0
			temp2 = global2._send('west:')
		#end:case
	#end:match
	if (argc > 1):
		localproc_0(@temp0, @temp1, param2)
	#endif
	local0 = (global0._send('x:') + temp0)
	local1 = (global0._send('y:') + temp1)
	global2._send('setScript:', walkEgoOutScr, 0, temp2)
#end:procedure

@SCI.procedure
def localproc_0(param1 = None, param2 = None, param3 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	temp0 = temp2 = kernel.Memory(5, param1)
	temp1 = kernel.Memory(5, param2)
	temp0 = (kernel.CosMult(param3, temp0) - kernel.SinMult(param3, temp1))
	temp1 = (kernel.SinMult(param3, temp2) + kernel.CosMult(param3, temp1))
	kernel.Memory(6, param1, temp0)
	kernel.Memory(6, param2, temp1)
#end:procedure

@SCI.procedure
def proc12_2(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	temp3 = 0
	if kernel.IsObject(param2):
		temp1 = param2._send('x:')
		temp2 = param2._send('y:')
		if (argc == 3):
			temp3 = param3
		#endif
	else:
		temp1 = param2
		temp2 = param3
		if (argc == 4):
			temp3 = param4
		#endif
	#endif
	temp0 = kernel.GetAngle(param1._send('x:'), param1._send('y:'), temp1, temp2)
	param1._send('setHeading:', temp0, (kernel.IsObject(temp3) and temp3))
	kernel.DisposeScript(12)
#end:procedure

@SCI.instance
class walkEgoInScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global0._send('reset:', 'setMotion:', PolyPath, local0, local1, self)
			#end:case
			case 1:
				kernel.ScriptID(10, 0)._send('setIt:', 4096)
				if (not script):
					cycles = 1
				#endif
			#end:case
			case 2:
				kernel.ScriptID(10, 0)._send('clrIt:', 4096)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('dispose:')
		register = 0
		kernel.DisposeScript(12)
	#end:method

#end:class or instance

@SCI.instance
class walkEgoOutScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global0._send('setMotion:', 0)
				cycles = 1
			#end:case
			case 1:
				global0._send('setMotion:', PolyPath, local0, local1, self)
			#end:case
			case 2:
				global2._send('newRoom:', register)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('dispose:', &rest)
		kernel.DisposeScript(12)
	#end:method

#end:class or instance

