#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 12
import sci_sh
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
def proc12_1(param1 = None, param2 = None, param3 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	temp0 = 0
	match global12
		case (global2 north:):
			(global0 posn: param1 -60)
		#end:case
		case (global2 south:):
			(global0 posn: param1 250)
		#end:case
		case (global2 east:):
			(global0 posn: 370 param2)
		#end:case
		case (global2 west:):
			(global0 posn: -20 param2)
		#end:case
		else:
			temp0 = 1
			(global0 posn: param1 param2)
		#end:else
	#end:match
	if (argc > 2):
		temp1 = ((global0 x:) - param1)
		temp2 = ((global0 y:) - param2)
		(localproc_0 @temp1 @temp2 param3)
		(global0 reset: posn: (param1 + temp1) (param2 + temp2))
	#endif
	if (not temp0):
		local0 = param1
		local1 = param2
		(global2 setScript: walkEgoInScr)
	else:
		(DisposeScript 12)
	#endif
#end:procedure

@SCI.procedure
def proc12_0(param1 = None, param2 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(global1 handsOff:)
	match param1
		case 1:
			temp0 = 0
			temp1 = -70
			temp2 = (global2 north:)
		#end:case
		case 3:
			temp0 = 0
			temp1 = 70
			temp2 = (global2 south:)
		#end:case
		case 2:
			temp0 = 20
			temp1 = 0
			temp2 = (global2 east:)
		#end:case
		case 4:
			temp0 = -20
			temp1 = 0
			temp2 = (global2 west:)
		#end:case
	#end:match
	if (argc > 1):
		(localproc_0 @temp0 @temp1 param2)
	#endif
	local0 = ((global0 x:) + temp0)
	local1 = ((global0 y:) + temp1)
	(global2 setScript: walkEgoOutScr 0 temp2)
#end:procedure

@SCI.procedure
def localproc_0(param1 = None, param2 = None, param3 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	temp0 = temp2 = (Memory 5 param1)
	temp1 = (Memory 5 param2)
	temp0 = ((CosMult param3 temp0) - (SinMult param3 temp1))
	temp1 = ((SinMult param3 temp2) + (CosMult param3 temp1))
	(Memory 6 param1 temp0)
	(Memory 6 param2 temp1)
#end:procedure

@SCI.procedure
def proc12_2(param1 = None, param2 = None, param3 = None, param4 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	temp3 = 0
	if (IsObject param2):
		temp1 = (param2 x:)
		temp2 = (param2 y:)
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
	temp0 = (GetAngle (param1 x:) (param1 y:) temp1 temp2)
	(param1 setHeading: temp0 ((IsObject temp3) and temp3))
	(DisposeScript 12)
#end:procedure

@SCI.instance
class walkEgoInScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 reset: setMotion: PolyPath local0 local1 self)
			#end:case
			case 1:
				((ScriptID 10 0) setIt: 4096)
				if (not script):
					cycles = 1
				#endif
			#end:case
			case 2:
				((ScriptID 10 0) clrIt: 4096)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
		register = 0
		(DisposeScript 12)
	#end:method

#end:class or instance

@SCI.instance
class walkEgoOutScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 setMotion: 0)
				cycles = 1
			#end:case
			case 1:
				(global0 setMotion: PolyPath local0 local1 self)
			#end:case
			case 2:
				(global2 newRoom: register)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose: &rest)
		(DisposeScript 12)
	#end:method

#end:class or instance

