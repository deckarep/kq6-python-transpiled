#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 741
import sci_sh
import kernel
import Main
import rgCastle
import System

# Public Export Declarations
SCI.public_exports(
	earlyGuest = 0,
)

@SCI.instance
class earlyGuest(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
		kernel.DisposeScript(741)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(kernel.ScriptID(80, 5) view: 724 loop: 4 cel: 0 x: 129 y: 155 init:)
				(kernel.ScriptID(80, 6) view: 726 loop: 4 cel: 1 x: 151 y: 153 init:)
				(kernel.ScriptID(80, 0) setupGuards:)
				cycles = 2
			#end:case
			case 1:
				(kernel.ScriptID(80, 6) setHeading: 180 self)
			#end:case
			case 2:
				(global91 say: 1 0 10 1 self)
			#end:case
			case 3:
				(global91 say: 1 0 10 2 self)
			#end:case
			case 4:
				(kernel.ScriptID(80, 5) setHeading: 180 self)
			#end:case
			case 5:
				(global91 say: 1 0 10 3 self)
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				(global2 moveOtherGuard: 1 spotEgo: proc80_7())
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

