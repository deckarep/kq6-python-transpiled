#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 754
import sci_sh
import kernel
import Main
import rm750
import Jump
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	useLamp = 0,
	stabEgo = 1,
)

@SCI.instance
class useLamp(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
		kernel.DisposeScript(752)
		kernel.UnLoad(128, 7501)
		kernel.UnLoad(128, 7503)
		kernel.UnLoad(128, 7504)
		kernel.UnLoad(128, 702)
		kernel.DisposeScript(1012)
		kernel.DisposeScript(991)
		kernel.DisposeScript(754)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global1 givePoints: 5)
				(global0
					view: 7503
					normal: 0
					setScale: 0
					loop: 0
					cel: 0
					cycleSpeed: 8
					setCycle: End self
				)
			#end:case
			case 1:
				(kernel.ScriptID(750, 1)
					add: -1 5 92 0 1
					add: -1 5 92 0 2
					add: -1 5 92 0 3
					init: self
				)
			#end:case
			case 2:
				(self setScript: kernel.ScriptID(752, 2) self kernel.ScriptID(750, 4))
			#end:case
			case 3:
				(kernel.ScriptID(750, 4) posn: 165 137)
				ticks = 60
			#end:case
			case 4:
				(self setScript: kernel.ScriptID(752, 1) self kernel.ScriptID(750, 4))
			#end:case
			case 5:
				(kernel.ScriptID(750, 4)
					view: 7503
					loop: 1
					cel: 0
					ignoreActors: 1
					x: ((kernel.ScriptID(750, 4) x:) + 32)
					y: ((kernel.ScriptID(750, 4) y:) - 8)
					setCycle: End self
				)
			#end:case
			case 6:
				(kernel.ScriptID(1012, 32)
					x: 50
					y: 59
					talkWidth: ((kernel.ScriptID(750, 4) x:) - 50)
				)
				(kernel.ScriptID(750, 4) dispose:)
				cycles = 3
			#end:case
			case 7:
				(global91 say: 5 92 0 4 self)
			#end:case
			case 8:
				(global0 setCycle: CT 1 -1)
				(kernel.ScriptID(750, 2) dispose:)
				if global169:
					(global2 drawPic: 750 15)
				else:
					(global2 drawPic: 750 100)
				#endif
				(kernel.ScriptID(750, 9) addToPic:)
				(kernel.ScriptID(750, 3)
					view: 7504
					loop: 0
					cel: 0
					signal: 16384
					init:
					setCycle: Walk
					setMotion: MoveTo 167 139 self
				)
			#end:case
			case 9:
				(kernel.ScriptID(750, 3)
					view: 7504
					setLoop: 0
					cel: 0
					setCycle: Walk
					setSpeed: 4
					setMotion: MoveTo 168 141 self
				)
			#end:case
			case 10:
				(kernel.ScriptID(750, 3)
					view: 7504
					setLoop: 1
					cel: 0
					x: 164
					y: 140
					setCycle: CT 8 1 self
				)
				(global103 number: 0 stop:)
				(global103 number: 652 setLoop: 1 play:)
			#end:case
			case 11:
				(global0 view: 703 setLoop: 0 cel: 0 setCycle: End)
				(kernel.ScriptID(750, 3) setCycle: End)
				(jar init: setCycle: Walk)
				(self setScript: jarGoesFlying self)
			#end:case
			case 12:
				(global0 setCycle: Beg self)
			#end:case
			case 13:
				if (global0 looper:):
					((global0 looper:) dispose:)
				#endif
				(global0
					normal: 0
					view: 7500
					setLoop: 3
					setCycle: 0
					looper: 0
					scaleSignal: 1
					scaleX: 96
					scaleY: 96
				)
				cycles = 2
			#end:case
			case 14:
				(global91 say: 5 92 0 5 self oneOnly: 0)
			#end:case
			case 15:
				(kernel.ScriptID(755, 0) register: 1)
				cycles = 4
			#end:case
			case 16:
				(global0 put: 25 740)
				proc750_5()
				(global69 disable: 5)
				if ((not global87) or (not kernel.HaveMouse())):
					seconds = 15
				else:
					seconds = 8
				#endif
			#end:case
			case 17:
				(self setScript: stabEgo)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class stabEgo(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				proc750_5(1)
				cycles = 1
			#end:case
			case 1:
				(global1 handsOff:)
				if (((global9 at: 25) owner:) == 740):
					cycles = 2
				else:
					(kernel.ScriptID(750, 3)
						view: 7504
						setLoop: 5
						setCycle: Walk
						setScale: 0
						posn: 120 138
						setStep: 6 6
						setMotion: MoveTo 180 144 self
					)
				#endif
			#end:case
			case 2:
				(global0 hide:)
				(kernel.ScriptID(750, 3)
					view: 755
					setLoop: 0
					cel: 0
					posn: 187 140
					scaleSignal: 1
					scaleX: 132
					scaleY: 132
					setCycle: CT 3 1 self
				)
			#end:case
			case 3:
				(kernel.ScriptID(750, 3) setCycle: End self)
				(global103 number: 756 setLoop: 1 play:)
			#end:case
			case 4:
				(kernel.ScriptID(750, 3) setLoop: 1 cel: 0 setCycle: End self)
				(global103 number: 756 setLoop: 1 play:)
			#end:case
			case 5:
				ticks = 30
			#end:case
			case 6:
				(kernel.ScriptID(750, 3) setLoop: 2 cel: 0 setCycle: CT 3 1 self)
			#end:case
			case 7:
				(global103 number: 971 setLoop: 1 play:)
				(global102 number: 705 setLoop: 1 play:)
				cycles = 2
			#end:case
			case 8:
				(global91 say: 6 23 16 3 self)
			#end:case
			case 9:
				(kernel.ScriptID(750, 3) setCycle: End self)
				(global103 number: 652 setLoop: 1 play:)
			#end:case
			case 10:
				proc0_1(41)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class jarGoesFlying(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(jar setMotion: JumpTo 255 134 self)
			#end:case
			case 1:
				(jar priority: 2 setMotion: JumpTo 271 148 self)
			#end:case
			case 2:
				(jar setMotion: JumpTo 287 168 self)
			#end:case
			case 3:
				(jar dispose:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class jar(Actor):
	#property vars (may be empty)
	x = 194
	y = 106
	view = 7504
	loop = 2
	cel = 1
	priority = 9
	signal = 16400
	
#end:class or instance

