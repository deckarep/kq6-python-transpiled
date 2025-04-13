#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 70
import sci_sh
import kernel
import n913
import RandCycle
import Game
import System

# Public Export Declarations
SCI.public_exports(
	rgDead = 0,
	proc70_1 = 1,
)

@SCI.procedure
def proc70_1(param1 = None, param2 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	temp0 = -1
	while temp1 = proc999_6(param2, temp0.post('++')):

		kernel.Clone(param1)._send(
			'posn:', temp1, proc999_6(param2, temp0.post('++')),
			'loop:', proc999_6(param2, temp0.post('++')),
			'cel:', kernel.Random(0, 3),
			'setCycle:', RandCycle,
			'init:'
		)
	#end:loop
#end:procedure

class rgDead(Rgn):
	#property vars (may be empty)
	flag1 = 0
	stateOf690 = 0
	songWaiting = 0
	loopWaiting = 0
	
	@classmethod
	def isSet(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return (flag1 & param1)
	#end:method

	@classmethod
	def clrIt(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(flag1 &= (flag1 ^ param1))
	#end:method

	@classmethod
	def setIt(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = param1
		(flag1 |= param1)
		return (temp0 & param1)
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		keep = proc999_5(param1, 600, 605, 615, 620, 630, 640, 650, 660, 670, 680, 690)
		initialized = 0
		super._send('newRoom:', param1, &rest)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('cue:')
		proc913_1(121)
	#end:method

#end:class or instance

