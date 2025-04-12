#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 180
import sci_sh
import kernel
import Main
import KQ6Room
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm180 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0


@SCI.instance
class rm180(KQ6Room):
	#property vars (may be empty)
	picture = 180
	autoLoad = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		if (global12 == 99):
			(global102 number: 752 setLoop: -1 play:)
		#endif
		(global0 init: view: 180 normal: 0 cel: 0 posn: 86 94 setPri: 14)
		(self setScript: sKissStuff)
	#end:method

#end:class or instance

@SCI.instance
class sKissStuff(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				seconds = 2
			#end:case
			case 1:
				(global0 setCycle: CT 2 1 self)
			#end:case
			case 2:
				ticks = 60
			#end:case
			case 3:
				(global0 cel: 3)
				ticks = 30
			#end:case
			case 4:
				(global0 cel: 2)
				ticks = 30
			#end:case
			case 5:
				(global0 cel: 3)
				ticks = 30
			#end:case
			case 6:
				(kernel.ScriptID(1015, 6) talkWidth: 100 x: 170 y: 140)
				seconds = 5
			#end:case
			case 7:
				(global91 say: 1 0 3 1 self)
			#end:case
			case 8:
				(global0 setCycle: Beg self)
				(kernel.ScriptID(1015, 6) talkWidth: 150 x: 70 y: 40)
			#end:case
			case 9:
				seconds = 2
			#end:case
			case 10:
				(global0
					view: 758
					setLoop: 0
					cel: 3
					posn: 29 179
					scaleSignal: 1
					scaleX: 128
					scaleY: 128
					signal: 26624
				)
				(body init: setLoop: 0 cel: 0)
				(leftGuard init: cel: 2)
				(rightGuard init:)
				(sword init: setPri: 1 ignoreActors: 1 addToPic:)
				(global2 drawPic: 750 10)
				(global69 disable: 6)
				cycles = 2
			#end:case
			case 11:
				(body setCycle: End self)
			#end:case
			case 12:
				(global0 setCycle: Beg self)
			#end:case
			case 13:
				(global0
					reset: 0
					scaleSignal: 1
					scaleX: 115
					scaleY: 115
					setPri: 13
					posn: 21 177
				)
				(cassima init: setPri: 14 setCycle: Beg self)
			#end:case
			case 14:
				(cassima view: 784 setLoop: 0 posn: 29 188 addToPic:)
				(global0 addToPic:)
				cycles = 2
			#end:case
			case 15:
				(global91 say: 1 0 2 1 self)
			#end:case
			case 16:
				(cassima dispose:)
				(global0 dispose:)
				(body setCycle: End self)
			#end:case
			case 17:
				(global91 say: 1 0 2 2 self)
			#end:case
			case 18:
				(body setCycle: End self)
			#end:case
			case 19:
				(global91 say: 1 0 2 3 self)
			#end:case
			case 20:
				(body setCycle: End self)
				(rightGuard cel: 3)
			#end:case
			case 21:
				(global91 say: 1 0 2 4 self)
			#end:case
			case 22:
				(leftGuard cel: 0)
				(body setLoop: 1 cel: 0 setCycle: End self)
			#end:case
			case 23:
				(body setLoop: 2 cel: 0 setCycle: End self)
			#end:case
			case 24:
				ticks = 30
			#end:case
			case 25:
				(body setCycle: CT 1 -1 self)
			#end:case
			case 26:
				(body setCycle: End self)
			#end:case
			case 27:
				(body setCycle: Beg self)
			#end:case
			case 28:
				(rightGuard
					setLoop: 3
					setCycle: Walk
					setMotion: MoveTo 233 133 self
				)
			#end:case
			case 29:
				(rightGuard setLoop: 0 setPri: 1 setMotion: MoveTo 249 135 self)
			#end:case
			case 30:
				(rightGuard setLoop: 2 setMotion: MoveTo 289 184 rightGuard)
				(body
					view: 145
					scaleSignal: 1
					scaleX: 95
					scaleY: 95
					setStep: 4 4
					posn: 169 149
					setLoop: 0
					setCycle: Walk
					setMotion: MoveTo 233 133 self
				)
			#end:case
			case 31:
				(body setPri: 1 setMotion: MoveTo 249 135 self)
				(leftGuard
					view: 765
					setLoop: 0
					cel: 0
					posn: 115 150
					setCycle: End
				)
				(global103 number: 0 stop:)
				(global103 number: 652 setLoop: 1 play:)
			#end:case
			case 32:
				(body setLoop: 2 setMotion: MoveTo 289 184 body)
				(leftGuard
					view: 7651
					posn: 127 150
					setLoop: 0
					setCycle: Walk
					setMotion: MoveTo 233 133 self
				)
			#end:case
			case 33:
				(leftGuard setPri: 1 setMotion: MoveTo 249 135 self)
			#end:case
			case 34:
				(leftGuard setLoop: 2 setMotion: MoveTo 289 184 self)
			#end:case
			case 35:
				(leftGuard dispose:)
				cycles = 2
			#end:case
			case 36:
				(global2 drawPic: 98 9)
				(global69 enable: 6)
				(global102 fade:)
				seconds = 4
			#end:case
			case 37:
				kernel.Message(0, 180, 1, 0, 2, 5, @local0)
				(global2 drawPic: 98 12)
				kernel.Display(@local0, 100, 85, 85, 102, 14, 105, 0)
				(global102 number: 743 setLoop: -1 play:)
				seconds = 3
			#end:case
			case 38:
				(global2 newRoom: 740)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class cassima(Actor):
	#property vars (may be empty)
	x = 29
	y = 178
	view = 753
	loop = 4
	cel = 3
	signal = 16384
	illegalBits = 0
	
#end:class or instance

@SCI.instance
class leftGuard(Actor):
	#property vars (may be empty)
	x = 115
	y = 150
	view = 724
	loop = 4
	
#end:class or instance

@SCI.instance
class rightGuard(Actor):
	#property vars (may be empty)
	x = 204
	y = 161
	view = 726
	loop = 4
	cel = 1
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super cue:)
		(self dispose:)
	#end:method

#end:class or instance

@SCI.instance
class body(Actor):
	#property vars (may be empty)
	x = 159
	y = 150
	view = 757
	loop = 2
	cel = 1
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super cue:)
		(self dispose:)
	#end:method

#end:class or instance

@SCI.instance
class sword(View):
	#property vars (may be empty)
	x = 157
	y = 143
	view = 757
	loop = 3
	
#end:class or instance

