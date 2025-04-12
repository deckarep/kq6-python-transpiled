#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 99
import sci_sh
import kernel
import Main
import Motion
import Game
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	speedRoom = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.instance
class speedRoom(Rm):
	#property vars (may be empty)
	picture = 98
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init:)
		temp0 = kernel.FileIO(0, r"""version""", 1)
		kernel.FileIO(5, global27, 10, temp0)
		kernel.FileIO(1, temp0)
		if global100:
			(global69 enable:)
			(global1 handsOn:)
			proc911_1()
			(global1 handsOff:)
		else:
			(self setScript: speedTest)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super doit:)
		temp0 = 0
		while (temp0 < 500): # inline for
		#end:loop
	#end:method

#end:class or instance

@SCI.instance
class fred(Actor):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class speedTest(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				kernel.Load(128, 99)
				cycles = 1
			#end:case
			case 1:
				local1 = kernel.GetTime()
				(fred
					view: 99
					setLoop: 0
					illegalBits: 0
					posn: 20 99
					setStep: 1 1
					setSpeed: 0
					setCycle: Fwd
					init:
					setMotion: MoveTo 100 100 self
				)
			#end:case
			case 2:
				local0 = (kernel.GetTime() - local1)
				cycles = 1
			#end:case
			case 3:
				kernel.Message(0, 99, 0, 0, 0, 1, @temp0)
				kernel.Display(@temp0, 100, 10, 80, 106, 300, 102, 6, 105, 3110, 101, 1)
				seconds = 5
			#end:case
			case 4:
				(startGame doit:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class startGame(Code):
	#property vars (may be empty)
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(= global87
			(cond
				case 
					(>
						(= global87
							(cond
								case (local0 > 600): 0#end:case
								case (local0 > 550): 1#end:case
								case (local0 > 500): 2#end:case
								case (local0 > 450): 3#end:case
								case (local0 > 400): 4#end:case
								case (local0 > 350): 5#end:case
								case (local0 > 300): 6#end:case
								case (local0 > 275): 7#end:case
								case (local0 > 250): 8#end:case
								case (local0 > 225): 9#end:case
								case (local0 > 200): 10#end:case
								case (local0 > 100): 11#end:case
								case (local0 > 60): 12#end:case
								case (local0 > 40): 13#end:case
								case (local0 > 20): 14#end:case
								else: 15#end:else
							)
						)
						11
					):
					2
				#end:case
				case (global87 < 8): 0#end:case
				else: 1#end:else
			)
		)
		(global1
			detailLevel:
				match global87
					case 0: 0#end:case
					case 1: 2#end:case
					else: 3#end:else
				#end:match
		)
		(global2 newRoom: 100)
	#end:method

#end:class or instance

