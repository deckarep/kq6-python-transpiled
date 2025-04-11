#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 411
import sci_sh
import kernel
import Main
import rLab
import n401
import n913
import PolyPath
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm411 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


@SCI.instance
class rm411(LabRoom):
	#property vars (may be empty)
	north = 400
	east = 400
	south = 400
	west = 400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init:)
		if proc913_0(1):
			match (kernel.ScriptID(30, 0) prevEdgeHit:)
				case 1:
					proc401_1()
				#end:case
				case 3:
					proc401_0()
				#end:case
				case 4:
					proc401_3()
				#end:case
				case 2:
					proc401_2()
				#end:case
			#end:match
			(global2 setScript: kernel.ScriptID(30, 1))
		else:
			(global102 number: 409 setLoop: -1 play:)
			(westHalfTrapFloor init: stopUpd:)
			(eastHalfTrapFloor init: stopUpd:)
			(eastTrapLedge init: stopUpd:)
			(westTrapLedge init: stopUpd:)
			(northTrapLedge init: stopUpd:)
			(global2 setScript: dieAlready)
		#endif
		match (kernel.ScriptID(30, 0) prevEdgeHit:)
			case 1:
				(kernel.ScriptID(30, 0) initCrypt: 1)
			#end:case
			case 3:
				(kernel.ScriptID(30, 0) initCrypt: 4)
				(kernel.ScriptID(30, 7) addToPic:)
				(kernel.ScriptID(30, 8) addToPic:)
			#end:case
			case 4:
				(kernel.ScriptID(30, 0) initCrypt: 4)
				(kernel.ScriptID(30, 6) addToPic:)
				(kernel.ScriptID(30, 10) addToPic:)
				(kernel.ScriptID(30, 8) addToPic:)
			#end:case
			case 2:
				(kernel.ScriptID(30, 0) initCrypt: 2)
				(kernel.ScriptID(30, 5) addToPic:)
				(kernel.ScriptID(30, 9) addToPic:)
				(kernel.ScriptID(30, 8) addToPic:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class dieAlready(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global69 disable:)
				match (kernel.ScriptID(30, 0) prevEdgeHit:)
					case 4:
						(global0 posn: 282 164 loop: 1 init:)
					#end:case
					case 2:
						(global0 posn: 36 164 loop: 0 init:)
					#end:case
					case 3:
						(global0 posn: 158 135 loop: 2 init:)
					#end:case
					case 1:
						(global0 posn: 158 225 loop: 3 init:)
					#end:case
				#end:match
				seconds = 2
			#end:case
			case 1:
				if 
					(and
						(global12 == 425)
						(not proc913_0(1))
						((kernel.ScriptID(30, 0) timesGenieHasAppeared:) < 4)
					)
					(self cue:)
				else:
					(global91 say: 1 0 58 1 self 400)
				#endif
			#end:case
			case 2:
				match (kernel.ScriptID(30, 0) prevEdgeHit:)
					case 4:
						(global0 setMotion: PolyPath 215 164 self)
					#end:case
					case 2:
						(global0 setMotion: PolyPath 108 164 self)
					#end:case
					case 3:
						(global0 setMotion: PolyPath 158 156 self)
					#end:case
					case 1:
						(global0 setMotion: PolyPath 158 185 self)
					#end:case
				#end:match
			#end:case
			case 3:
				if 
					(and
						(global12 == 425)
						(not proc913_0(1))
						((kernel.ScriptID(30, 0) timesGenieHasAppeared:) < 4)
					)
					local0 = 1
					(global91 say: 1 0 3 1 self 400)
				else:
					(self cue:)
				#endif
			#end:case
			case 4:
				match (kernel.ScriptID(30, 0) prevEdgeHit:)
					case 1:
						temp0 = 3
						temp1 = 0
						temp2 = 0
					#end:case
					case 3:
						temp0 = 2
						temp1 = 0
						temp2 = 0
					#end:case
					case 4:
						temp0 = 1
						temp1 = -5
						temp2 = 0
					#end:case
					case 2:
						temp0 = 0
						temp1 = 7
						temp2 = 2
					#end:case
				#end:match
				(global0
					x: ((global0 x:) + temp1)
					y: ((global0 y:) + temp2)
					view: 4011
					normal: 0
					cycleSpeed: 6
					setLoop: temp0
					setCycle: CT 10 1 self
				)
			#end:case
			case 5:
				(global0 setCycle: End self)
			#end:case
			case 6:
				if local0:
					proc913_1(59)
					(global91 say: 1 0 3 2 self 400)
				else:
					(global91 say: 1 0 58 2 self 400)
				#endif
			#end:case
			case 7:
				(global102 number: 432 setLoop: 1 play: self)
			#end:case
			case 8:
				proc913_2(59)
				(global102 number: 307 setLoop: 1 play:)
				kernel.ShakeScreen(2, 2)
				ticks = 4
			#end:case
			case 9:
				(global2 drawPic: 98 100)
				(global5 eachElementDo: #hide)
				cycles = 4
			#end:case
			case 10:
				proc0_1(7)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class westHalfTrapFloor(View):
	#property vars (may be empty)
	x = 83
	y = 159
	view = 409
	priority = 1
	signal = 16400
	
#end:class or instance

@SCI.instance
class eastHalfTrapFloor(View):
	#property vars (may be empty)
	x = 233
	y = 158
	view = 409
	loop = 1
	priority = 1
	signal = 16400
	
#end:class or instance

@SCI.instance
class northTrapLedge(View):
	#property vars (may be empty)
	x = 108
	y = 148
	view = 409
	loop = 4
	priority = 2
	signal = 16400
	
#end:class or instance

@SCI.instance
class eastTrapLedge(View):
	#property vars (may be empty)
	x = 211
	y = 141
	view = 409
	loop = 2
	priority = 3
	signal = 16400
	
#end:class or instance

@SCI.instance
class westTrapLedge(View):
	#property vars (may be empty)
	x = 104
	y = 140
	view = 409
	loop = 3
	priority = 3
	signal = 16400
	
#end:class or instance

