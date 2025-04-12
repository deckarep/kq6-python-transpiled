#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 482
import sci_sh
import kernel
import Main
import PolyPath
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	proc482_0 = 0,
	proc482_1 = 1,
	proc482_2 = 2,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


@SCI.procedure
def proc482_0():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	(kernel.ScriptID(480, 5) register: 1)
	(global0 setScript: grabForHole)
#end:procedure

@SCI.procedure
def proc482_1():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	(global0 setScript: getHole)
#end:procedure

@SCI.procedure
def proc482_2():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	(kernel.ScriptID(480, 5) register: 1)
	(global0 setScript: lookThruHole)
#end:procedure

@SCI.instance
class getHole(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global69 disable: 6)
				seconds = 2
			#end:case
			case 1:
				if ((kernel.ScriptID(480, 1) x:) > 280):
					(global105 number: 483 setLoop: 1 play:)
					(kernel.ScriptID(480, 1)
						setLoop: 5
						setCycle: Walk
						setMotion: MoveTo 263 47
					)
					local0 = 1
				#endif
				(global0 setMotion: PolyPath 302 92 self)
			#end:case
			case 2:
				(global0 setMotion: PolyPath 273 87 self)
			#end:case
			case 3:
				if (local0 == 1):
					(self cue:)
				else:
					(global105 number: 483 setLoop: 1 play:)
					(kernel.ScriptID(480, 1)
						setLoop: 5
						setCycle: Walk
						setMotion: MoveTo 256 64 self
					)
				#endif
			#end:case
			case 4:
				if (local0 == 1):
					local0 = 0
					(kernel.ScriptID(480, 1)
						setLoop: 4
						cel: 5
						posn: 254 50
						cycleSpeed: 3
						setCycle: Beg
					)
				#endif
				(global0
					normal: 0
					view: 482
					setLoop: 3
					cel: 0
					posn: 258 90
					setCycle: CT 3 1 self
				)
			#end:case
			case 5:
				(global1 givePoints: 1)
				(global105 stop:)
				(kernel.ScriptID(480, 1) dispose:)
				(global0 get: 18 setCycle: End self)
			#end:case
			case 6:
				(global0 posn: 273 87 reset: 7)
				cycles = 6
			#end:case
			case 7:
				(global91 say: 21 5 10 1 self 480)
			#end:case
			case 8:
				(global0 setMotion: PolyPath 197 116 self)
			#end:case
			case 9:
				(global0 setHeading: 135 self)
			#end:case
			case 10:
				cycles = 2
			#end:case
			case 11:
				(kernel.ScriptID(480, 5) register: 1)
				(global69 enable: 6)
				(global1 handsOn:)
				(self dispose:)
				kernel.DisposeScript(482)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class grabForHole(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91 say: 21 5 8 1 self 480)
			#end:case
			case 1:
				(global0 setMotion: PolyPath 300 97 self)
			#end:case
			case 2:
				(global0 setMotion: PolyPath 294 81 self)
			#end:case
			case 3:
				(global91 say: 21 5 8 2 self 480)
			#end:case
			case 4:
				(kernel.ScriptID(480, 1) hide:)
				(global105 number: 483 setLoop: 1 play:)
				(global0
					view: 482
					setLoop: 0
					cel: 0
					normal: 0
					setPri: 5
					posn: 280 83
					cycleSpeed: 8
					setCycle: End self
				)
			#end:case
			case 5:
				(kernel.ScriptID(480, 1) posn: 238 70 show:)
				(global0 posn: 294 81 reset: 7)
				ticks = 6
			#end:case
			case 6:
				(global91 say: 21 5 8 3 self 480)
			#end:case
			case 7:
				(global0 setMotion: PolyPath 197 116 self)
			#end:case
			case 8:
				(global0 setHeading: 135)
				(global1 handsOn:)
				(self dispose:)
				kernel.DisposeScript(482)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lookThruHole(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				if (kernel.ScriptID(40, 0) holeLooks:):
					(self cue:)
				else:
					(global91 say: 21 1 5 1 self 480)
				#endif
			#end:case
			case 1:
				(global0 setMotion: PolyPath 283 94 self)
			#end:case
			case 2:
				(global0 setHeading: 0)
				ticks = 6
			#end:case
			case 3:
				if (kernel.ScriptID(40, 0) holeLooks:):
					(global91 say: 21 1 6 1 self 480)
				else:
					(self cue:)
				#endif
			#end:case
			case 4:
				(holeInset init:)
				seconds = 3
			#end:case
			case 5:
				(holeInset dispose:)
				if (kernel.ScriptID(40, 0) holeLooks:):
					(global91 say: 21 1 6 2 self 480)
				else:
					(global91 say: 21 1 5 2 self 480)
				#endif
			#end:case
			case 6:
				(global0
					setLoop: 3
					setMotion: MoveTo ((global0 x:) + 5) ((global0 y:) + 5) self
				)
			#end:case
			case 7:
				if (kernel.ScriptID(40, 0) holeLooks:):
					(self cue:)
				else:
					(global105 number: 483 setLoop: 1 play:)
					(kernel.ScriptID(480, 1)
						setMotion:
							MoveTo
							((kernel.ScriptID(480, 1) x:) - 5)
							(kernel.ScriptID(480, 1) y:)
							self
					)
				#endif
			#end:case
			case 8:
				if (kernel.ScriptID(40, 0) holeLooks:):
					(self cue:)
				else:
					(kernel.ScriptID(480, 1)
						setMotion:
							MoveTo
							((kernel.ScriptID(480, 1) x:) + 5)
							(kernel.ScriptID(480, 1) y:)
							self
					)
				#endif
			#end:case
			case 9:
				if (kernel.ScriptID(40, 0) holeLooks:):
					(self cue:)
				else:
					(global91 say: 21 1 5 3 self 480)
				#endif
			#end:case
			case 10:
				(global1 handsOn:)
				(global0 reset: 3)
				(kernel.ScriptID(40, 0) holeLooks: 1)
				(self dispose:)
				kernel.DisposeScript(482)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class holeInset(View):
	#property vars (may be empty)
	x = 162
	y = 98
	view = 487
	priority = 15
	signal = 16400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(fields init:)
		(super init:)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(fields dispose:)
		(super dispose:)
	#end:method

#end:class or instance

@SCI.instance
class fields(View):
	#property vars (may be empty)
	x = 164
	y = 93
	view = 490
	priority = 14
	signal = 16400
	
#end:class or instance

