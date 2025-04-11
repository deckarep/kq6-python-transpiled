#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 224
import sci_sh
import kernel
import Main
import Scaler
import PolyPath
import StopWalk
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	clownScr = 0,
)

@SCI.instance
class clownScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(clown init: setMotion: PolyPath 124 119 self)
			#end:case
			case 1:
				(clown setHeading: 0 self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				(global91 say: 1 0 2 1 self)
			#end:case
			case 4:
				(global91 say: 1 0 2 2 self)
			#end:case
			case 5:
				(self setScript: kernel.ScriptID(220, 1) self 1)
			#end:case
			case 6:
				(clown setMotion: MoveTo 117 109 self)
			#end:case
			case 7:
				(clown setMotion: MoveTo 104 95 self)
			#end:case
			case 8:
				(clown
					setPri: 2
					setScale: Scaler 64 94 103 95
					setMotion: MoveTo 75 100 self
				)
			#end:case
			case 9:
				(kernel.ScriptID(10, 0) clrIt: 2)
				(clown dispose:)
				(script cue:)
			#end:case
			case 10:
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
		kernel.DisposeScript(224)
	#end:method

#end:class or instance

@SCI.instance
class ModStopWalk(StopWalk):
	#property vars (may be empty)
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (client isStopped:):
			(cond
				case ((vStopped == -1) and ((client loop:) != 4)):
					temp0 = (client loop:)
					if (temp1 = (client mover:) and (not (temp1 completed:))):
						(client setMotion: 0)
					#endif
					(super doit:)
					(client loop: 4 setCel: temp0)
				#end:case
				case ((vStopped != -1) and ((client view:) == vWalking)):
					(client view: vStopped)
					if (temp1 = (client mover:) and (not (temp1 completed:))):
						(client setMotion: 0)
					#endif
					(super doit:)
				#end:case
				case (vStopped != -1):
					(super doit:)
				#end:case
			)
		else:
			match vStopped
				case (client view:):
					(client view: vWalking)
				#end:case
				case -1:
					(client setLoop: -1 setCel: -1)
					if ((client loop:) == 4):
						(client loop: (client cel:) cel: 0)
					#endif
				#end:case
			#end:match
			(super doit:)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class clown(Actor):
	#property vars (may be empty)
	x = 166
	y = 172
	view = 717
	signal = 16384
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self setScale: setCycle: ModStopWalk -1)
	#end:method

#end:class or instance

