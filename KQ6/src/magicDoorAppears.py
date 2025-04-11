#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 711
import sci_sh
import kernel
import Main
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	magicDoorAppears = 0,
)

@SCI.instance
class magicDoorAppears(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose: &rest)
		kernel.DisposeScript(711)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 posn: 36 156 reset: 0 hide:)
				(magicDoor init:)
				cycles = 2
			#end:case
			case 1:
				(global103 number: 231 setLoop: 1 play:)
				(magicDoor cycleSpeed: 8 setCycle: CT 6 1 self)
			#end:case
			case 2:
				(global0 show:)
				(magicDoor cel: 7 setCycle: End self)
			#end:case
			case 3:
				(magicDoor dispose:)
				(global91 say: 9 0 14 0 self)
			#end:case
			case 4:
				cycles = 3
			#end:case
			case 5:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class magicDoor(Prop):
	#property vars (may be empty)
	x = 27
	y = 131
	view = 714
	priority = 10
	signal = 16
	
#end:class or instance

