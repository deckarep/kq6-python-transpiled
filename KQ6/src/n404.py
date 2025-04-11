#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 404
import sci_sh
import kernel
import Main
import n913
import PolyPath
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	proc404_0 = 0,
	proc404_1 = 1,
	proc404_2 = 2,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None


@SCI.procedure
def proc404_0(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(global0 setScript: holeOnWall 0 param1)
#end:procedure

@SCI.procedure
def proc404_1():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(kernel.ScriptID(30, 0) holeIsUp: 1)
	match (kernel.ScriptID(30, 0) holeWall:)
		case 2:
			(aHole posn: 281 222 setPri: 13 init:)
		#end:case
		case 1:
			(aHole posn: 159 191 setLoop: 7 setPri: 10 init:)
		#end:case
		case 4:
			(aHole posn: 36 223 setPri: 13 init:)
		#end:case
	#end:match
#end:procedure

@SCI.procedure
def proc404_2():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	if (global5 contains: aHole):
		(aHole dispose: delete:)
	#endif
	kernel.DisposeScript(404)
#end:procedure

@SCI.instance
class aHole(Actor):
	#property vars (may be empty)
	z = 100
	noun = 17
	modNum = 400
	sightAngle = 45
	view = 232
	loop = 6
	signal = 26640
	illegalBits = 0
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				(global0 setScript: lookInHole)
			#end:case
			case 2:
				(global91 say: 17 2 0 1 0 400)
			#end:case
			case 5:
				(global0 setScript: getHole)
			#end:case
			else:
				(global91 say: 17 0 0 1 0 400)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class holeInset(View):
	#property vars (may be empty)
	x = 157
	y = 105
	view = 487
	priority = 15
	signal = 24592
	
#end:class or instance

@SCI.instance
class wall1(View):
	#property vars (may be empty)
	x = 160
	y = 139
	view = 414
	priority = 12
	signal = 24592
	
#end:class or instance

@SCI.instance
class wall2(View):
	#property vars (may be empty)
	x = 149
	y = 139
	view = 414
	priority = 12
	signal = 24592
	
#end:class or instance

@SCI.instance
class wall3(View):
	#property vars (may be empty)
	x = 139
	y = 139
	view = 414
	priority = 12
	signal = 24592
	
#end:class or instance

@SCI.instance
class wall4(View):
	#property vars (may be empty)
	x = 129
	y = 139
	view = 414
	priority = 12
	signal = 24592
	
#end:class or instance

@SCI.instance
class sDoor(Prop):
	#property vars (may be empty)
	x = 205
	y = 96
	view = 414
	loop = 4
	priority = 13
	signal = 24592
	
#end:class or instance

@SCI.instance
class dirt(Prop):
	#property vars (may be empty)
	x = 159
	y = 100
	view = 490
	priority = 13
	signal = 24592
	
#end:class or instance

@SCI.instance
class holeOnWall(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 put: 18 global11)
				(global1 handsOff:)
				(kernel.ScriptID(30, 0) holeIsUp: 1 holeWall: register)
				if (global11 == 400):
					(kernel.ScriptID(30, 0) holeCoords: (kernel.ScriptID(30, 0) labCoords:))
				else:
					(kernel.ScriptID(30, 0) holeCoords: global11)
				#endif
				match register
					case 2:
						local1 = 259
						local2 = 173
					#end:case
					case 1:
						local1 = 157
						local2 = 144
					#end:case
					case 4:
						local1 = 59
						local2 = 173
					#end:case
				#end:match
				(global0 setMotion: PolyPath local1 local2 self)
			#end:case
			case 1:
				match register
					case 2:
						(global0 setHeading: 45)
					#end:case
					case 1:
						(global0 setHeading: 0)
					#end:case
					case 4:
						(global0 setHeading: 270)
					#end:case
				#end:match
				cycles = 10
			#end:case
			case 2:
				match register
					case 2:
						local1 = 271
						local2 = 173
						(global0 setLoop: 0)
					#end:case
					case 1:
						local1 = 157
						local2 = 146
						(global0 setLoop: 2)
					#end:case
					case 4:
						local1 = 48
						local2 = 173
						(global0 setLoop: 1)
					#end:case
				#end:match
				(global0
					view: 232
					normal: 0
					cel: 0
					posn: local1 local2
					cycleSpeed: 6
				)
				if (register == 1):
					(global0 setCycle: CT 4 1 self)
				else:
					(global0 setCycle: CT 5 1 self)
				#endif
			#end:case
			case 3:
				match register
					case 2:
						(aHole posn: 281 222 setPri: 13 init:)
					#end:case
					case 1:
						(aHole posn: 159 191 setLoop: 7 setPri: 10 init:)
					#end:case
					case 4:
						(aHole posn: 36 223 setPri: 13 init:)
					#end:case
				#end:match
				(global0 cel: 6)
				seconds = 1
			#end:case
			case 4:
				if ((global11 == 409) and ((aHole x:) > 250)):
					(global91 say: 19 25 55 1 self 400)
				else:
					(global91 say: 6 25 0 1 self 400)
				#endif
			#end:case
			case 5:
				if 
					(and
						(global11 == 409)
						(not proc913_0(1))
						((aHole x:) > 250)
					)
					(self cue:)
				else:
					(global91 say: 6 25 0 2 self 400)
				#endif
			#end:case
			case 6:
				match register
					case 2:
						(global0 posn: 259 173 reset: 6)
					#end:case
					case 1:
						(global0 posn: 157 144 reset: 3)
					#end:case
					case 4:
						(global0 posn: 59 173 reset: 1)
					#end:case
				#end:match
				cycles = 6
			#end:case
			case 7:
				match register
					case 2:
						local1 = 236
						local2 = 173
					#end:case
					case 1:
						local1 = 157
						local2 = 158
					#end:case
					case 4:
						local1 = 79
						local2 = 173
					#end:case
				#end:match
				(global0
					setLoop: (global0 cel:)
					setMotion: MoveTo local1 local2 self
				)
			#end:case
			case 8:
				cycles = 8
			#end:case
			case 9:
				if 
					(and
						(global11 == 409)
						(not proc913_0(1))
						((aHole x:) > 250)
					)
					(global105 number: 483 setLoop: 1 play:)
					(aHole
						yStep: 6
						setCycle: Fwd
						setMotion: MoveTo (aHole x:) 5 self
					)
				else:
					(self cue:)
				#endif
			#end:case
			case 10:
				if 
					(and
						(global11 == 409)
						(not proc913_0(1))
						((aHole x:) > 250)
					)
					(global91 say: 19 25 55 2 self 400)
				else:
					(self cue:)
				#endif
			#end:case
			case 11:
				if 
					(and
						(global11 == 409)
						(not proc913_0(1))
						((aHole x:) > 250)
					)
					(global91 say: 19 25 55 3 self 400)
				else:
					(self cue:)
				#endif
			#end:case
			case 12:
				(global1 handsOn:)
				(global0 setLoop: -1)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lookInHole(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(cond
					case ((aHole x:) < 82):
						register = 4
						local1 = 58
						local2 = 172
					#end:case
					case ((aHole x:) < 233):
						register = 1
						local1 = 157
						local2 = 144
					#end:case
					else:
						register = 2
						local1 = 259
						local2 = 170
					#end:else
				)
				(global0 setMotion: PolyPath local1 local2 self)
			#end:case
			case 1:
				match register
					case 4:
						(global0 setHeading: 270)
					#end:case
					case 1:
						(global0 setHeading: 0)
					#end:case
					case 2:
						(global0 setHeading: 90)
					#end:case
				#end:match
				cycles = 12
			#end:case
			case 2:
				match register
					case 4:
						local1 = 47
						local2 = 172
						(global0 setPri: 14 setLoop: 4)
					#end:case
					case 1:
						local1 = 157
						local2 = 146
						(global0 setPri: 11 setLoop: 5)
					#end:case
					case 2:
						local1 = 268
						local2 = 171
						(global0 setPri: 14 setLoop: 3)
					#end:case
				#end:match
				(global0
					view: 232
					cel: 0
					normal: 0
					posn: local1 local2
					cycleSpeed: 6
					setCycle: End self
				)
			#end:case
			case 3:
				(global91 say: 17 1 0 0 self 400)
			#end:case
			case 4:
				(global0 setCycle: Beg self)
			#end:case
			case 5:
				match register
					case 4:
						(global0 posn: 58 172 reset: 1)
					#end:case
					case 1:
						(global0 posn: 157 144 reset: 3)
					#end:case
					case 2:
						(global0 posn: 259 170 reset: 0)
					#end:case
				#end:match
				cycles = 6
			#end:case
			case 6:
				match register
					case 4:
						local1 = 78
						local2 = 172
					#end:case
					case 1:
						local1 = 157
						local2 = 159
					#end:case
					case 2:
						local1 = 239
						local2 = 170
					#end:case
				#end:match
				(global0
					setLoop: (global0 cel:)
					setMotion: PolyPath local1 local2 self
				)
			#end:case
			case 7:
				(global1 handsOn:)
				(global0 reset:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getHole(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(cond
					case ((aHole x:) < 82):
						register = 4
						local1 = 59
						local2 = 173
					#end:case
					case ((aHole x:) < 233):
						register = 1
						local1 = 157
						local2 = 144
					#end:case
					else:
						register = 2
						local1 = 256
						local2 = 173
					#end:else
				)
				(global0 setMotion: PolyPath local1 local2 self)
			#end:case
			case 1:
				match register
					case 4:
						(global0 setHeading: 270)
					#end:case
					case 1:
						(global0 setHeading: 0)
					#end:case
					case 2:
						(global0 setHeading: 45)
					#end:case
				#end:match
				cycles = 10
			#end:case
			case 2:
				(global91 say: 17 5 0 1 self 400)
			#end:case
			case 3:
				match register
					case 2:
						(global0 posn: 268 173 setLoop: 0)
					#end:case
					case 1:
						(global0 posn: 157 146 setLoop: 2)
					#end:case
					case 4:
						local1 = 48
						local2 = 173
						(global0 posn: 48 173 setLoop: 1)
					#end:case
				#end:match
				(global0 view: 232 normal: 0 cel: 6)
				cycles = 3
			#end:case
			case 4:
				(aHole dispose:)
				(global0 cycleSpeed: 6 setCycle: Beg self)
			#end:case
			case 5:
				match register
					case 2:
						(global0 posn: 259 170 reset: 6)
					#end:case
					case 1:
						(global0 posn: 157 144 reset: 3)
					#end:case
					case 4:
						(global0 posn: 58 172 reset: 1)
					#end:case
				#end:match
				cycles = 6
			#end:case
			case 6:
				match register
					case 2:
						local1 = 239
						local2 = 170
					#end:case
					case 1:
						local1 = 157
						local2 = 156
					#end:case
					case 4:
						local1 = 78
						local2 = 172
					#end:case
				#end:match
				ticks = 6
			#end:case
			case 7:
				(global0
					setLoop: (global0 cel:)
					setMotion: MoveTo local1 local2 self
				)
			#end:case
			case 8:
				(global1 handsOn:)
				(global0 setLoop: -1 get: 18)
				(kernel.ScriptID(30, 0) holeCoords: 0)
				(kernel.ScriptID(30, 0) holeWall: 0)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

