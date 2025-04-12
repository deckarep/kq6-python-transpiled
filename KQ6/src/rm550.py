#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 550
import sci_sh
import kernel
import Main
import KQ6Room
import n913
import Conversation
import Scaler
import Osc
import PolyPath
import Polygon
import Feature
import StopWalk
import Sound
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm550 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = 1
local1
local3 = 1
local4 = None
local5 = None
local6 = None
local7 = None
local8 = None
local9 = None


@SCI.procedure
def localproc_0(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	if param1:
		local7 = (global89 x:)
		local8 = (global89 talkWidth:)
		(global89 x: 20 talkWidth: 100)
	else:
		(global89 x: local7 talkWidth: local8)
	#endif
#end:procedure

@SCI.procedure
def localproc_1(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	if param1:
		local7 = (global89 x:)
		local8 = (global89 talkWidth:)
		(global89 x: 200 talkWidth: 100)
	else:
		(global89 x: local7 talkWidth: local8)
	#endif
#end:procedure

@SCI.procedure
def localproc_2():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(return
		(cond
			case (((global0 heading:) > 45) and ((global0 heading:) < 135)): 0#end:case
			case (((global0 heading:) > 134) and ((global0 heading:) < 225)): 2#end:case
			case (((global0 heading:) > 224) and ((global0 heading:) < 315)): 1#end:case
			case (((global0 heading:) > 314) or ((global0 heading:) < 45)): 3#end:case
		)
	)
#end:procedure

@SCI.instance
class rm550Messager(Kq6Messager):
	#property vars (may be empty)
	@classmethod
	def findTalker(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if 
			(= temp0
				match param1
					case 59: global89#end:case
					case 60: global89#end:case
				#end:match
			)
			return
		else:
			(super findTalker: param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class oceanSound(Sound):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class rm550(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 550
	horizon = 0
	west = 560
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(global1 handsOff:)
		local6 = global91
		global91 = rm550Messager
		(global2
			addObstacle:
				((Polygon new:)
					type: 2
					init:
						319
						106
						259
						107
						224
						84
						222
						92
						189
						86
						170
						95
						168
						89
						171
						83
						133
						87
						130
						83
						143
						78
						165
						68
						155
						63
						142
						60
						124
						48
						140
						0
						319
						0
					yourself:
				)
				((Polygon new:)
					type: 2
					init:
						260
						127
						237
						129
						217
						132
						186
						128
						181
						119
						218
						112
						233
						101
						255
						121
					yourself:
				)
				((Polygon new:)
					type: 2
					init:
						152
						112
						140
						112
						139
						120
						118
						120
						108
						118
						100
						111
						85
						110
						86
						106
						115
						101
						129
						103
						153
						109
					yourself:
				)
				((Polygon new:)
					type: 2
					init:
						93
						76
						81
						70
						65
						71
						57
						67
						30
						68
						20
						58
						0
						58
						0
						0
						93
						0
						110
						51
						132
						59
						143
						67
					yourself:
				)
				((Polygon new:)
					type: 2
					init:
						132
						144
						164
						170
						119
						189
						0
						189
						0
						132
						50
						126
						75
						129
						96
						135
					yourself:
				)
				((Polygon new:)
					type: 2
					init:
						319
						165
						291
						165
						282
						169
						247
						168
						229
						162
						243
						158
						294
						149
						319
						153
					yourself:
				)
				((Polygon new:)
					type: 2
					init: 240 189 136 189 166 185 206 185
					yourself:
				)
		)
		(water1 init: setCycle: Fwd)
		(water2 init: setCycle: Fwd)
		(water3 init: setCycle: Fwd)
		(water4 init: setCycle: Fwd)
		(oceanSound number: 915 loop: -1 flags: 1 play:)
		(global103 number: 550 flags: 1 loop: -1 play:)
		(ocean1 init:)
		(ocean2 init:)
		(trees1 init:)
		(trees2 init:)
		(rocks init:)
		(nePath init:)
		(nwPath init:)
		(global0 actions: egoDoVerb setScale: Scaler 100 70 190 53 setPri: -1)
		if (proc913_0(25) and (not proc913_0(14))):
			(druid1 init: setScale: -1 global0)
			(druid2 init: setScale: -1 global0 setScript: waitForCapture)
			local5 = 1
		#endif
		if proc999_5(global12, 560, 580):
			(self setScript: egoEnters)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (global0 onControl: 1)
		(cond
			case script: 0#end:case
			case (temp0 & 0x2000):
				(global1 handsOff:)
				(global2 setScript: walkNorthScript)
			#end:case
			case (temp0 & 0x0010):
				if ((global0 view:) != 308):
					temp1 = localproc_2()
					(global0
						ignoreActors: 1
						illegalBits: 0
						view: 308
						setPri: 15
						setLoop: temp1
						setLoop: -1
					)
					local0 = 0
				#endif
			#end:case
			case (temp0 & 0x0020):
				if (not local9):
					local9 = 1
					(global104 number: 922 loop: -1 flags: 1 play:)
				#endif
				if local3:
					local0 = 0
					local3 = 0
					(global91 say: 4 3 6)
					(global0 setMotion: 0)
				#endif
			#end:case
			case (temp0 & 0x0040):
				if ((global0 view:) != 3081):
					temp1 = localproc_2()
					(global0
						ignoreActors: 1
						illegalBits: 0
						view: 3081
						setPri: 15
						setLoop: temp1
						setLoop: -1
					)
				#endif
			#end:case
			case (temp0 & 0x0100):
				if (not local4):
					(global0 setMotion: 0)
					while True: #repeat
						(global0 posn: ((global0 x:) - 1) ((global0 y:) - 1))
						(breakif ((global0 onControl: 1) & 0x0080))
					#end:loop
					(global91 say: 4 3 6)
					local0 = 0
					local4 = 1
				else:
					(global1 handsOff:)
					(self setScript: wateryDeathScr)
				#endif
			#end:case
			case 
				(and
					(not (temp0 & 0x01f0))
					((global0 view:) == 308)
					(not local0)
				):
				(global104 fade:)
				local9 = 0
				(global0 reset: 3)
				local4 = 0
				local0 = 1
			#end:case
		)
		(super doit: &rest)
	#end:method

	@classmethod
	def newRoom(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not proc999_5(param1, 560, 580)):
			(global103 stop: number: 0)
		#endif
		(super newRoom: param1)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		global91 = local6
		(super dispose:)
		kernel.DisposeScript(939)
	#end:method

#end:class or instance

@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class trees2(Feature):
	#property vars (may be empty)
	noun = 5
	onMeCheck = 7680
	
#end:class or instance

@SCI.instance
class ocean1(Feature):
	#property vars (may be empty)
	noun = 4
	onMeCheck = 240
	
#end:class or instance

@SCI.instance
class ocean2(Feature):
	#property vars (may be empty)
	noun = 4
	onMeCheck = 256
	
#end:class or instance

@SCI.instance
class trees1(Feature):
	#property vars (may be empty)
	noun = 5
	onMeCheck = 2
	
#end:class or instance

@SCI.instance
class rocks(Feature):
	#property vars (may be empty)
	noun = 2
	onMeCheck = 12
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (param1 == 1):
				(global91 say: noun param1 10 0 0 0)
			#end:case
			case proc999_5(param1, 2, 5):
				(global91 say: noun param1 0 0 0 0)
			#end:case
			else:
				(global91 say: noun 0 0 0 0 0)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class nePath(Feature):
	#property vars (may be empty)
	noun = 7
	onMeCheck = 8192
	
#end:class or instance

@SCI.instance
class nwPath(Feature):
	#property vars (may be empty)
	noun = 8
	onMeCheck = 16384
	
#end:class or instance

@SCI.instance
class druid1(Actor):
	#property vars (may be empty)
	x = 68
	y = 105
	view = 553
	signal = 16384
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self setCycle: StopWalk -1)
	#end:method

#end:class or instance

@SCI.instance
class druid2(Actor):
	#property vars (may be empty)
	x = 131
	y = 82
	view = 553
	loop = 2
	signal = 16384
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self setCycle: StopWalk -1)
	#end:method

#end:class or instance

@SCI.instance
class water1(Prop):
	#property vars (may be empty)
	x = 217
	y = 136
	noun = 4
	view = 550
	signal = 16384
	cycleSpeed = 10
	detailLevel = 3
	
#end:class or instance

@SCI.instance
class water2(Prop):
	#property vars (may be empty)
	x = 278
	y = 172
	noun = 4
	view = 550
	loop = 1
	signal = 16384
	cycleSpeed = 10
	detailLevel = 3
	
#end:class or instance

@SCI.instance
class water3(Prop):
	#property vars (may be empty)
	x = 291
	y = 89
	noun = 4
	view = 550
	loop = 2
	signal = 16384
	cycleSpeed = 10
	detailLevel = 3
	
#end:class or instance

@SCI.instance
class water4(Prop):
	#property vars (may be empty)
	x = 279
	y = 110
	noun = 4
	view = 550
	loop = 3
	signal = 16384
	cycleSpeed = 10
	detailLevel = 3
	
#end:class or instance

@SCI.instance
class walkNorthScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 setMotion: PolyPath 138 58 self)
			#end:case
			case 1:
				(global0 setMotion: PolyPath 122 47 self)
			#end:case
			case 2:
				(global0 setHeading: 45 self)
			#end:case
			case 3:
				(global2 newRoom: 580)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoEnters(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				match global12
					case 580:
						(global0
							init:
							posn: 126 55
							setMotion: PolyPath 127 87 self
						)
					#end:case
					else:
						(global0
							init:
							posn: 1 95
							setMotion: PolyPath 40 95 self
						)
					#end:else
				#end:match
			#end:case
			case 1:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class waitForCapture(Script):
	#property vars (may be empty)
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super doit:)
		if ((not state) and (not (global2 script:))):
			(global1 handsOff:)
			(global2 setScript: captured)
		#endif
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0: 0#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class captured(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 setHeading: 315 self)
			#end:case
			case 1:
				localproc_0(1)
				(global91 say: 1 0 2 1 self)
				localproc_0(0)
			#end:case
			case 2:
				localproc_1(1)
				(global91 say: 1 0 2 2 self)
				localproc_1(0)
			#end:case
			case 3:
				localproc_0(1)
				(global91 say: 1 0 2 3 self)
				localproc_0(0)
			#end:case
			case 4:
				(druid1
					setMotion:
						MoveTo
						((global0 x:) - 25)
						((global0 y:) + 3)
						self
					setCycle: Walk
				)
				(druid2
					setMotion:
						MoveTo
						((global0 x:) + 24)
						((global0 y:) + 4)
						self
					setCycle: Walk
				)
			#end:case
			case 5:
				(druid1 dispose:)
				(druid2 dispose:)
				(global0
					normal: 0
					view: 554
					cycleSpeed: 10
					cel: 0
					setLoop: 0
					setCycle: End self
				)
			#end:case
			case 6:
				(global91 say: 1 0 2 4 self)
			#end:case
			case 7:
				localproc_0(1)
				(global91 say: 1 0 2 5 self)
				localproc_0(0)
			#end:case
			case 8:
				(global0
					view: 5806
					setLoop: 0
					cycleSpeed: 6
					setCycle: Walk
					setMotion: PolyPath 126 85 self
				)
			#end:case
			case 9:
				(global0 setMotion: PolyPath 150 66 self)
			#end:case
			case 10:
				(global2 newRoom: 580)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class wateryDeathScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91 say: 4 3 9 0 self)
			#end:case
			case 1:
				(global2 walkOffEdge: 1)
				(global104 stop: number: 921 loop: 1 play:)
				(global0
					normal: 0
					view: 269
					setLoop: 1
					cel: 0
					cycleSpeed: 6
					setCycle: Osc
				)
				if ((global0 y:) > 137):
					(global0 setMotion: PolyPath 267 220 self)
				else:
					(global0 setMotion: PolyPath 340 118 self)
				#endif
			#end:case
			case 2:
				(global2 newRoom: 135)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoDoVerb(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 12:
				(global2 setScript: 130)
				return 1
			#end:case
			else:
				return 0
			#end:else
		#end:match
	#end:method

#end:class or instance

