#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 435
import sci_sh
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
	trapFloor = 0,
)

@SCI.instance
class trapFloor(LabRoom):
	#property vars (may be empty)
	north = 400
	west = 400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(proc401_2)
		(super init: &rest)
		((ScriptID 30 0) initCrypt: 2)
		((ScriptID 30 5) addToPic:)
		((ScriptID 30 9) addToPic:)
		((ScriptID 30 8) addToPic:)
		(self setScript: fallTrapFloor)
	#end:method

#end:class or instance

@SCI.instance
class fallTrapFloor(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global69 disable: 6)
				(global0 posn: 36 164 init: setMotion: PolyPath 120 164 self)
			#end:case
			case 1:
				cycles = 8
			#end:case
			case 2:
				(westHalfTrapFloor init: stopUpd:)
				(eastHalfTrapFloor init: stopUpd:)
				(eastTrapLedge init: stopUpd:)
				(westTrapLedge init: stopUpd:)
				(northTrapLedge init: stopUpd:)
				cycles = 2
			#end:case
			case 3:
				(global102 stop:)
				(global103 number: 909 setLoop: 1 play: self)
			#end:case
			case 4:
				(global102 number: 409 setLoop: -1 play:)
				cycles = 4
			#end:case
			case 5:
				if (proc913_0 1):
					(global91 say: 1 0 30 0 self 400)
				else:
					(global91 say: 1 0 29 1 self 400)
				#endif
			#end:case
			case 6:
				(global0
					setLoop: (global0 cel:)
					normal: 0
					cycleSpeed: 1
					setCycle: Fwd
				)
				seconds = 3
			#end:case
			case 7:
				(global102 stop:)
				(global103 number: 404 setLoop: 1 play:)
				(global0
					setCycle: 0
					setStep: 40 30
					setMotion: MoveTo (global0 x:) 250 self
				)
			#end:case
			case 8:
				(global69 enable: 6)
				(global2 style: -32758 newRoom: 406)
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
	priority = 2
	signal = 16400
	
#end:class or instance

@SCI.instance
class westTrapLedge(View):
	#property vars (may be empty)
	x = 104
	y = 140
	view = 409
	loop = 3
	priority = 2
	signal = 16400
	
#end:class or instance

