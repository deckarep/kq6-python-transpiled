#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 273
import sci_sh
import kernel
import Main
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	boringBook = 0,
	takeBoringBookScr = 1,
)

@SCI.instance
class takeBoringBookScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				register = (1 if ((kernel.ScriptID(270, 2) y:) < 140) else 0)
				(global0
					setSpeed: 6
					view: 278
					loop: 0
					cel: 0
					normal: 0
					setCycle: CT 2 1 self
				)
			#end:case
			case 1:
				(boringBook dispose:)
				cycles = 2
			#end:case
			case 2:
				(global0 setCycle: End self)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				(global91 say: 2 5 4 1 self)
			#end:case
			case 5:
				if register:
					(kernel.ScriptID(270, 2) view: 276 cel: 0 setCycle: CT 4 1 self)
				else:
					state.post('++')
					(self cue:)
				#endif
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				(global91 say: 2 5 4 2 self oneOnly: 0)
			#end:case
			case 8:
				if register:
					(kernel.ScriptID(270, 2) setCycle: Beg self)
				else:
					state.post('++')
					cycles = 1
				#endif
			#end:case
			case 9:
				(kernel.ScriptID(270, 2) view: 276 loop: 0 cel: 0)
				cycles = 1
			#end:case
			case 10:
				(global0 reset: get: 1)
				(global1 givePoints: 1)
				cycles = 2
			#end:case
			case 11:
				kernel.UnLoad(128, 278)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose: &rest)
		kernel.DisposeScript(273)
	#end:method

#end:class or instance

@SCI.instance
class boringBook(View):
	#property vars (may be empty)
	x = 112
	y = 135
	z = 14
	noun = 2
	sightAngle = 40
	approachX = 108
	approachY = 137
	view = 270
	loop = 2
	priority = 8
	signal = 17
	
	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if temp0 = (super onMe: param1 &rest):
			if ((param1 message:) == 1):
				approachX = 134
				approachY = 129
			else:
				approachX = 112
				approachY = 137
			#endif
		#endif
		return temp0
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(kernel.ScriptID(270, 1) doVerb: param1 &rest)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 5 1)
	#end:method

#end:class or instance

