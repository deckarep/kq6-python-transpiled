#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 980
import sci_sh
import kernel
import Main
import Print
import System

class Tutorial(Script):
	#property vars (may be empty)
	nextItem = 0
	nextAction = 0
	numTries = 0
	
	@classmethod
	def waitFor(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, param6 = None, param7 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		nextItem = param1
		nextAction = param2
		(cond
			case (argc == 3):
				proc921_0(param3)
			#end:case
			case (argc > 3):
				global91._send('say:', param3, param4, param5, param6, param7)
			#end:case
		)
	#end:method

	@classmethod
	def report():#end:method

	@classmethod
	def cue():
		numTries = 0
		super._send('cue:', &rest)
	#end:method

#end:class or instance

