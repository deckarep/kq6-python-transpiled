#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 731
import sci_sh
import kernel
import Main
import rm730
import n913
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	bypassingWaiter = 0,
)

@SCI.instance
class bypassingWaiter(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
		kernel.DisposeScript(731)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				proc913_1(59)
				cycles = 2
			#end:case
			case 1:
				(global91 say: 1 0 1 1 self)
			#end:case
			case 2:
				(self setScript: convScript self)
			#end:case
			case 3:
				(global91 say: 1 0 1 2 self)
			#end:case
			case 4:
				(self setScript: convScript self)
			#end:case
			case 5:
				(global91 say: 1 0 1 3 self)
			#end:case
			case 6:
				(self setScript: convScript self)
			#end:case
			case 7:
				(global91 say: 1 0 1 4 self)
			#end:case
			case 8:
				(self setScript: convScript self)
			#end:case
			case 9:
				cycles = 2
			#end:case
			case 10:
				(global1 handsOn:)
				proc913_2(59)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class convScript(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		start = (state + 1)
		(super dispose: &rest)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 setHeading: 315)
				(global105 number: 901 loop: 1 play:)
				(global104 number: 731 loop: -1 play:)
				(kernel.ScriptID(730, 1) setCycle: End self)
			#end:case
			case 1:
				(global105 stop:)
				(self dispose:)
			#end:case
			case 2:
				(waiter
					init:
					ignoreActors:
					illegalBits: 0
					cel: 0
					setCycle: CT 4 1 self
				)
			#end:case
			case 3:
				(kernel.ScriptID(730, 1) cel: 0 stopUpd:)
				(global104 stop:)
				(global105 number: 902 loop: 1 play:)
				(waiter cel: 5 setCycle: End self)
			#end:case
			case 4:
				(waiter
					posn: 104 143
					setLoop: ((waiter loop:) + 1)
					setCycle: CT 5 1 self
				)
			#end:case
			case 5:
				(self dispose:)
			#end:case
			case 6:
				(waiter setCycle: End self)
			#end:case
			case 7:
				(waiter
					setCycle: Walk
					posn: 106 143
					setLoop: ((waiter loop:) + 1)
					cel: 0
					setMotion: MoveTo 230 144 self
				)
			#end:case
			case 8:
				(waiter
					setLoop: ((waiter loop:) + 1)
					posn: 227 144
					cel: 0
					setCycle: End self
				)
				(global105 number: 901 loop: 1 play:)
				(kernel.ScriptID(730, 2) hide:)
			#end:case
			case 9:
				(waiter dispose: setCycle: 0)
				(kernel.ScriptID(730, 2) show: cel: 3 setCycle: Beg self)
			#end:case
			case 10:
				(global105 number: 902 loop: 1 play:)
				(kernel.ScriptID(730, 2) stopUpd:)
				(kernel.ScriptID(730, 1) stopUpd:)
				(self dispose:)
			#end:case
			case 11:
				(global0 setMotion: MoveTo 259 167 self)
			#end:case
			case 12:
				(global0 setHeading: 315 self)
			#end:case
			case 13:
				(global0
					view: 734
					normal: 0
					setScale: 0
					cycleSpeed: 9
					setLoop: 1
					cel: 0
					posn: 251 168
					setCycle: End self
				)
			#end:case
			case 14:
				(global0 setLoop: 2 cel: 0 posn: 253 169 setCycle: End self)
			#end:case
			case 15:
				(global0 setLoop: 3 cel: 0 posn: 264 169 setCycle: End self)
			#end:case
			case 16:
				(global0 reset: 0 posn: 260 165)
				(global0 put: 5)
				proc730_3()
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class waiter(Actor):
	#property vars (may be empty)
	x = 92
	y = 143
	view = 735
	xStep = 4
	
#end:class or instance

