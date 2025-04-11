#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 490
import sci_sh
import kernel
import Main
import Kq6Sound
import KQ6Room
import Kq6Talker
import n913
import Conversation
import Scaler
import PolyPath
import Polygon
import Feature
import Timer
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm490 = 0,
	White_Queen = 52,
	Red_Queen = 53,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1
local3 = None
local4
local34 = [222, 211, 205, 197, 191, 185, 179]
local41 = [89, 93, 99, 109, 116, 124, 131, 0, 0]
local50 = None
local51 = None
local52 = None
local53 = 3


@SCI.instance
class rm490(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 490
	walkOffEdge = 1
	autoLoad = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self
			addObstacle:
				((Polygon new:)
					type: 2
					init: 71 124 8 189 0 189 0 0 319 0 319 189 300 189 243 124
					yourself:
				)
		)
		(super init: &rest)
		(global102 number: 490 setLoop: -1 play:)
		(global32 add: theSky thePath theSteps eachElementDo: #init)
		(redKnight addToPic:)
		(whiteKnight addToPic:)
		if (proc913_0(39) and (((global9 at: 41) owner:) == global11)):
			(redScarf init:)
		#endif
		(global2 setScript: egoEnters)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match local3.post('++')
			case 1:
				(global1 handsOff:)
				(global91 say: 1 0 10 0 self)
			#end:case
			case 2:
				(global2 setScript: queensLeave 0 0)
			#end:case
		#end:match
	#end:method

	@classmethod
	def newRoom(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(roomTimer dispose: delete:)
		(super newRoom: param1)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (global2 script:):#end:case
			case ((global0 edgeHit:) == 3):
				(global2 walkOffEdge: 1 setScript: walkOut)
			#end:case
			case ((global0 y:) <= 128):
				if ((not local3) and local52):
					(global0 setMotion: 0)
					(global2 cue:)
				else:
					(global0 posn: (global0 x:) ((global0 y:) + 1) setMotion: 0)
					(global2 setScript: knightBlock 0 3)
				#endif
			#end:case
		)
		(super doit:)
	#end:method

	@classmethod
	def scriptCheck():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 0
		if local52:
			(global91 say: 0 0 234 0 0 899)
		else:
			temp0 = 1
		#endif
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class whiteKnight(Actor):
	#property vars (may be empty)
	x = 89
	y = 124
	noun = 8
	view = 492
	signal = 18432
	illegalBits = 0
	xStep = 8
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (global5 contains: whiteQueen):
			(global91 say: 7 0 11 1)
		else:
			local0 = 8
			match param1
				case 5:
					(global2 setScript: knightBlock 0 param1)
				#end:case
				case 2:
					(global2 setScript: knightBlock 0 param1)
				#end:case
				case 46:
					(global2 setScript: knightBlock 0 param1)
				#end:case
				case 72:
					(global2 setScript: knightBlock 0 param1)
				#end:case
				case 1:
					(super doVerb: param1 &rest)
				#end:case
				else:
					(global2 setScript: knightBlock 0 0)
				#end:else
			#end:match
		#endif
	#end:method

#end:class or instance

@SCI.instance
class redKnight(Actor):
	#property vars (may be empty)
	x = 222
	y = 124
	noun = 7
	view = 493
	cel = 1
	signal = 18432
	illegalBits = 0
	xStep = 8
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (global5 contains: redQueen):
			(global91 say: 7 0 11 1)
		else:
			local0 = 7
			match param1
				case 5:
					(global2 setScript: knightBlock 0 param1)
				#end:case
				case 2:
					(global2 setScript: knightBlock 0 param1)
				#end:case
				case 46:
					(global2 setScript: knightBlock 0 param1)
				#end:case
				case 72:
					(global2 setScript: knightBlock 0 param1)
				#end:case
				case 1:
					if ((not local53.post('--')) and (global12 == 99)):
						(global0 get: 6)
					#endif
					(super doVerb: param1 &rest)
				#end:case
				else:
					(global2 setScript: knightBlock 0 0)
				#end:else
			#end:match
		#endif
	#end:method

#end:class or instance

@SCI.instance
class redQueen(Actor):
	#property vars (may be empty)
	noun = 5
	view = 494
	priority = 6
	signal = 18448
	cycleSpeed = 9
	illegalBits = 0
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 46:
				(global91 say: 5 46 0 1)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case 
				(and
					(not (global105 handle:))
					(cel == 2)
					(loop == 3)
					(view == 494)
				):
				(global105 number: 493 setLoop: 1 play:)
			#end:case
			case 
				(and
					(not (global105 handle:))
					(cel == 2)
					(loop == 1)
					(view == 495)
				):
				(global105 number: 493 setLoop: 1 play:)
			#end:case
		)
		(super doit: &rest)
	#end:method

#end:class or instance

@SCI.instance
class whiteQueen(Actor):
	#property vars (may be empty)
	noun = 6
	view = 496
	priority = 6
	signal = 18448
	cycleSpeed = 9
	illegalBits = 0
	
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super doit: &rest)
		(cond
			case 
				(and
					(not (global105 handle:))
					(cel == 2)
					(loop == 3)
					(view == 496)
				):
				(global105 number: 493 setLoop: 1 play:)
			#end:case
			case 
				(and
					(not (global105 handle:))
					(cel == 2)
					(loop == 1)
					(view == 497)
				):
				(global105 number: 493 setLoop: 1 play:)
			#end:case
		)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 46:
				(global2 setScript: coalToQueen)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class redScarf(Prop):
	#property vars (may be empty)
	x = 177
	y = 134
	noun = 4
	view = 494
	loop = 4
	signal = 24576
	cycleSpeed = 10
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (global5 contains: redQueen):
			(self setCycle: End self)
		else:
			(self view: 4900 setLoop: 0 cel: 3 stopUpd:)
		#endif
		(super init:)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self view: 4900 setLoop: 0 cel: 3 stopUpd:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global2 setScript: getScarf)
			#end:case
			else:
				(super doVerb: param1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class thePath(Feature):
	#property vars (may be empty)
	noun = 9
	onMeCheck = 2
	
#end:class or instance

@SCI.instance
class theSteps(Feature):
	#property vars (may be empty)
	noun = 11
	onMeCheck = 4
	
#end:class or instance

@SCI.instance
class theSky(Feature):
	#property vars (may be empty)
	noun = 10
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self setOnMeCheck: 1 16)
		(super init: &rest)
	#end:method

#end:class or instance

@SCI.instance
class knightBlock(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(cond
					case ((register == 3) or (register == 5)):
						(global0 setMotion: PolyPath 150 140 self)
					#end:case
					case (local0 == 8):
						(global0 setMotion: PolyPath 130 145 self)
					#end:case
					else:
						(global0 setMotion: PolyPath 178 145 self)
					#end:else
				)
				(self setScript: knightBoundForward self)
			#end:case
			case 1:
				(global0 setHeading: 0 self)
			#end:case
			case 2:#end:case
			case 3:
				(redKnight view: 493 setLoop: 0 cel: 2)
				(whiteKnight view: 492 setLoop: 0 cel: 2)
				ticks = 30
			#end:case
			case 4:
				match register
					case 3:
						(global91 say: 3 3 5 0 self)
					#end:case
					case 5:
						(global91 say: 3 3 5 0 self)
					#end:case
					case 2:
						if (proc913_0(39) and proc913_0(69)):
							(global91 say: 7 2 9 0 self)
						else:
							proc913_1(69)
							(global91 say: 7 2 7 0 self)
						#endif
					#end:case
					case 46:
						(global91 say: 7 46 0 0 self)
					#end:case
					case 72:
						(global91 say: local0 72 0 0 self)
					#end:case
					case 0:
						(global91 say: 7 0 0 0 self)
					#end:case
					else:
						(global1 handsOn:)
						(self dispose:)
					#end:else
				#end:match
			#end:case
			case 5:
				(hoofSound number: 492 setLoop: 1 play:)
				(client setScript: knightBoundBack)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class queensEnter(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global102 pause: 1)
				(global2 drawPic: 490 (15 if global169 else 100))
				(global103 number: 491 setLoop: -1 play: 10 setVol: 10)
				(whiteKnight
					signal: 18432
					view: 4900
					cel: 0
					setLoop: 0
					addToPic:
				)
				(redKnight signal: 18432 view: 4900 setLoop: 0 cel: 1 addToPic:)
				kernel.UnLoad(128, 492)
				kernel.UnLoad(128, 493)
				cycles = 2
			#end:case
			case 1:
				(global0 setHeading: 0 self)
			#end:case
			case 2:
				(global103 fade: 127 10 5 0)
				(global0 normal: 0 view: 4900 cel: 2 setCycle: 0 setLoop: 0)
				cycles = 2
			#end:case
			case 3:
				(self setScript: miniQueenPolka self)
			#end:case
			case 4:
				seconds = 3
			#end:case
			case 5:
				(self setScript: queensJumpUp self)
			#end:case
			case 6:
				(redQueen stopUpd:)
				(whiteQueen stopUpd:)
				cycles = 2
			#end:case
			case 7:
				(global2 drawPic: 490 (15 if global169 else 100))
				(whiteKnight
					signal: 18432
					view: 4901
					setLoop: 0
					cel: 0
					init:
					setCycle: End self
				)
				(redKnight
					signal: 18432
					view: 4901
					setLoop: 1
					cel: 0
					init:
					setCycle: End self
				)
			#end:case
			case 8:#end:case
			case 9:
				(whiteKnight view: 4900 setLoop: 2 cel: 0 addToPic:)
				(redKnight view: 4900 setLoop: 2 cel: 1 addToPic:)
				kernel.UnLoad(128, 492)
				kernel.UnLoad(128, 493)
				cycles = 2
			#end:case
			case 10:
				(redQueen view: 495 setLoop: 1 cel: 0 setCycle: End self)
				(whiteQueen view: 497 setLoop: 1 cel: 0 setCycle: End self)
			#end:case
			case 11:#end:case
			case 12:
				(redQueen view: 494 setLoop: 0 cel: 1)
				(whiteQueen view: 496 setLoop: 0 cel: 0)
				ticks = 12
			#end:case
			case 13:
				(global2 drawPic: 490 (15 if global169 else 100))
				(whiteKnight
					signal: 18432
					view: 4901
					setLoop: 0
					cel: 3
					init:
					setCycle: Beg self
				)
				(redKnight
					signal: 18432
					view: 4901
					setLoop: 1
					cel: 3
					init:
					setCycle: Beg self
				)
				kernel.UnLoad(128, 492)
				kernel.UnLoad(128, 493)
			#end:case
			case 14:#end:case
			case 15:
				(whiteKnight view: 4900 setLoop: 1 cel: 0 addToPic:)
				(redKnight view: 4900 setLoop: 1 cel: 1 addToPic:)
				kernel.UnLoad(128, 492)
				kernel.UnLoad(128, 493)
				cycles = 2
			#end:case
			case 16:
				if (proc913_0(39) and (global0 has: 6)):
					(global2 setScript: coalQueenTalk)
				else:
					(global2 setScript: firstQueenTalk)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class firstQueenTalk(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				proc913_1(59)
				(myConv
					add: -1 1 0 2 1
					add: -1 1 0 2 2
					add: -1 1 0 2 3
					add: -1 1 0 2 4
					add: -1 1 0 2 5
					add: -1 1 0 2 6
					init: self
				)
			#end:case
			case 1:
				seconds = 2
			#end:case
			case 2:
				proc913_2(59)
				(redQueen view: 495 setLoop: 2 cel: 0 setCycle: End self)
			#end:case
			case 3:
				(redQueen view: 495 setLoop: 1 cel: 3 setCycle: Beg self)
				(whiteQueen view: 497 setLoop: 1 cel: 3 setCycle: Beg self)
			#end:case
			case 4:#end:case
			case 5:
				(redQueen view: 494 setLoop: 0 cel: 2)
				(whiteQueen view: 496 setLoop: 0 cel: 2)
				ticks = 30
			#end:case
			case 6:
				(myConv add: -1 1 0 2 7 add: -1 1 0 2 8 init: self)
			#end:case
			case 7:
				proc913_1(59)
				(redQueen view: 495 setLoop: 1 cel: 0 setCycle: End self)
				if (not (global105 handle:)):
					(global105 number: 493 setLoop: 1 play:)
				#endif
			#end:case
			case 8:
				(global91 say: 1 0 2 9 self)
			#end:case
			case 9:
				(redQueen cel: 3 setCycle: Beg self)
			#end:case
			case 10:
				ticks = 30
			#end:case
			case 11:
				(redQueen view: 494 setLoop: 0 cel: 2)
				ticks = 30
			#end:case
			case 12:
				(global0
					view: 491
					normal: 0
					setLoop: 2
					cel: 0
					cycleSpeed: 0
					setCycle: CT 4 1 self
				)
			#end:case
			case 13:
				proc913_2(59)
				(global91 say: 1 0 2 10 self)
			#end:case
			case 14:
				(global0 view: 4900 setLoop: 0 cel: 2)
				cycles = 3
			#end:case
			case 15:
				(myConv add: -1 1 0 2 11 add: -1 1 0 2 12 init: self)
			#end:case
			case 16:
				(redQueen view: 495 setLoop: 1 cel: 0 setCycle: End self)
				(whiteQueen view: 497 setLoop: 1 cel: 0 setCycle: End self)
			#end:case
			case 17:#end:case
			case 18:
				proc913_1(59)
				(redQueen view: 494 setLoop: 0 cel: 1)
				(whiteQueen view: 496 setLoop: 0 cel: 0)
				ticks = 30
			#end:case
			case 19:
				(myConv add: -1 1 0 2 13 add: -1 1 0 2 14 init: self)
			#end:case
			case 20:
				proc913_1(39)
				local50 = 1
				(global2 setScript: queensLeave 0 1)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class coalQueenTalk(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				proc913_1(59)
				if proc913_0(89):
					(myConv
						add: -1 1 0 4 1
						add: -1 1 0 4 2
						add: -1 1 0 4 3
						add: -1 1 0 4 4
						add: -1 1 0 4 5
						add: -1 1 0 4 6
						init: self
					)
				else:
					(myConv
						add: -1 1 0 3 1
						add: -1 1 0 3 2
						add: -1 1 0 3 3
						add: -1 1 0 3 4
						add: -1 1 0 3 5
						add: -1 1 0 3 6
						add: -1 1 0 3 7
						init: self
					)
				#endif
			#end:case
			case 1:
				(redQueen view: 4951 setLoop: 1 cel: 3 setCycle: Beg self)
				(whiteQueen view: 497 setLoop: 1 cel: 3 setCycle: Beg self)
				kernel.UnLoad(128, 494)
				kernel.UnLoad(128, 496)
			#end:case
			case 2:#end:case
			case 3:
				(redQueen view: 4951 setLoop: 0 cel: 0)
				(whiteQueen view: 496 setLoop: 0 cel: 2)
				kernel.UnLoad(128, 497)
				cycles = 4
			#end:case
			case 4:
				proc913_2(59)
				if proc913_0(89):
					(global91 say: 1 0 4 7 self)
				else:
					proc913_1(89)
					(global91 say: 1 0 3 8 self)
				#endif
			#end:case
			case 5:
				(global1 handsOn:)
				(global0 reset: 3)
				local3 = 0
				local52 = 1
				(roomTimer setReal: global2 15)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getScarf(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 illegalBits: 0 setMotion: PolyPath 163 136 self)
			#end:case
			case 1:
				(global0 loop: 6)
				ticks = 12
			#end:case
			case 2:
				(global91 say: 4 5 0 1 self)
			#end:case
			case 3:
				(global0
					view: 491
					normal: 0
					loop: 4
					cel: 0
					posn: 172 140
					cycleSpeed: 10
					setCycle: CT 3 1 self
				)
			#end:case
			case 4:
				(global1 givePoints: 1)
				(redScarf dispose:)
				(global0 setCycle: End self)
			#end:case
			case 5:
				(global0
					reset: 6
					get: 41
					posn: 163 136
					setMotion: PolyPath 150 170 self
				)
			#end:case
			case 6:
				(global1 handsOn:)
				(global0 setHeading: 180)
				(self dispose:)
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
				(global1 handsOff:)
				(global0
					posn: 160 255
					setScale: Scaler 100 99 190 0
					init:
					reset:
					setMotion: MoveTo 144 183 self
				)
			#end:case
			case 1:
				if (proc913_0(39) and (global0 has: 6)):
					cycles = 2
				else:
					(global1 handsOn:)
					(self dispose:)
				#endif
			#end:case
			case 2:
				if ((global102 prevSignal:) == 10):
					(global102 prevSignal: 0)
					(global69 disable: 6)
					(global2 setScript: queensEnter)
					(self dispose:)
				else:
					state.post('--')
					cycles = 1
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walkOut(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global102 fade:)
				(global103 fade:)
				(global0 setMotion: MoveTo (global0 x:) 255 self)
			#end:case
			case 1:
				(global2 newRoom: 480)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class queensJumpUp(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				if (global0 has: 6):
					(redQueen
						view: 4952
						setLoop: 0
						cel: 0
						setPri: 7
						posn: 177 148
						setCycle: End
					)
				else:
					(redQueen
						view: 494
						setLoop: 1
						cel: 0
						setPri: 7
						posn: 177 148
						setCycle: End
					)
				#endif
				(whiteQueen
					view: 496
					setLoop: 1
					cel: 0
					setPri: 7
					posn: 143 148
					setCycle: End self
				)
			#end:case
			case 1:
				(redQueen posn: 177 138 cel: 0 setCycle: End self)
				(whiteQueen posn: 143 138 cel: 0 setCycle: End self)
			#end:case
			case 2:#end:case
			case 3:
				(redQueen posn: 177 116 cel: 0 setCycle: End self)
				(whiteQueen posn: 143 116 cel: 0 setCycle: End self)
			#end:case
			case 4:#end:case
			case 5:
				(redQueen posn: 177 116 cel: 0 setPri: 9 setCycle: End self)
				(whiteQueen posn: 143 116 cel: 0 setPri: 9 setCycle: End self)
			#end:case
			case 6:#end:case
			case 7:
				if (global0 has: 6):
					(redQueen view: 4951 setLoop: 0 cel: 0 posn: 177 124)
				else:
					(redQueen view: 494 setLoop: 0 cel: 2 posn: 177 124)
				#endif
				(whiteQueen posn: 143 124 setLoop: 0 cel: 2)
				seconds = 2
			#end:case
			case 8:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class miniQueenSplit(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(whiteQueen setLoop: 4 setPri: 7 posn: 186 112 show:)
				(redQueen setLoop: 5 setPri: 7 posn: 197 110 show:)
				ticks = 8
			#end:case
			case 1:
				(whiteQueen posn: 186 113)
				(redQueen posn: 197 111)
				ticks = 8
			#end:case
			case 2:
				(whiteQueen posn: 185 108)
				(redQueen posn: 196 107)
				ticks = 8
			#end:case
			case 3:
				(whiteQueen posn: 184 110)
				(redQueen posn: 194 108)
				ticks = 8
			#end:case
			case 4:
				(whiteQueen posn: 183 105)
				(redQueen posn: 193 105)
				ticks = 8
			#end:case
			case 5:
				(whiteQueen posn: 182 106)
				(redQueen posn: 191 106)
				ticks = 8
			#end:case
			case 6:
				(whiteQueen posn: 181 102)
				(redQueen posn: 189 102)
				ticks = 8
			#end:case
			case 7:
				(whiteQueen posn: 179 103)
				(redQueen posn: 186 103)
				ticks = 8
			#end:case
			case 8:
				(whiteQueen posn: 178 99)
				(redQueen posn: 184 99)
				ticks = 8
			#end:case
			case 9:
				(whiteQueen posn: 176 100)
				(redQueen posn: 182 100)
				ticks = 8
			#end:case
			case 10:
				(whiteQueen posn: 174 96)
				(redQueen posn: 178 96)
				ticks = 8
			#end:case
			case 11:
				(whiteQueen posn: 172 97)
				(redQueen posn: 176 97)
				ticks = 8
			#end:case
			case 12:
				(whiteQueen posn: 168 93)
				(redQueen posn: 172 93)
				ticks = 8
			#end:case
			case 13:
				(whiteQueen posn: 168 94)
				(redQueen posn: 170 94)
				ticks = 8
			#end:case
			case 14:
				(whiteQueen posn: 164 91)
				(redQueen posn: 166 91)
				ticks = 8
			#end:case
			case 15:
				(whiteQueen posn: 161 91)
				(redQueen posn: 163 91)
				ticks = 8
			#end:case
			case 16:
				(whiteQueen posn: 158 88)
				(redQueen posn: 160 88)
				ticks = 8
			#end:case
			case 17:
				(whiteQueen setPri: 5 posn: 154 93)
				(redQueen setPri: 5 posn: 156 93)
				ticks = 8
			#end:case
			case 18:
				(whiteQueen posn: 154 92)
				(redQueen posn: 156 92)
				ticks = 8
			#end:case
			case 19:
				(whiteQueen posn: 154 95)
				(redQueen posn: 156 95)
				ticks = 8
			#end:case
			case 20:
				(whiteQueen dispose:)
				(redQueen dispose:)
				(global69 enable: 6)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class hopOut(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(redQueen
					view: 494
					setLoop: 3
					cel: 0
					posn: 176 124
					cycleSpeed: 10
					setCycle: End
				)
				(whiteQueen
					view: 496
					setLoop: 3
					cel: 0
					posn: 143 124
					cycleSpeed: 10
					setCycle: End self
				)
			#end:case
			case 1:
				if local50:
					local50 = 0
					(redScarf init:)
				#endif
				(redQueen setLoop: 2 cel: 0 posn: 176 124)
				(whiteQueen setLoop: 2 cel: 0 posn: 143 124)
				ticks = 8
			#end:case
			case 2:
				(redQueen cel: 1 posn: 176 124)
				(whiteQueen cel: 1 posn: 143 124)
				ticks = 8
			#end:case
			case 3:
				(redQueen cel: 2 posn: 176 122)
				(whiteQueen cel: 2 posn: 143 122)
				ticks = 8
			#end:case
			case 4:
				(redQueen cel: 3 posn: 176 120)
				(whiteQueen cel: 3 posn: 143 120)
				ticks = 8
			#end:case
			case 5:
				(redQueen cel: 4 posn: 176 119)
				(whiteQueen cel: 4 posn: 143 119)
				ticks = 8
			#end:case
			case 6:
				(redQueen cel: 5 posn: 176 118)
				(whiteQueen cel: 5 posn: 143 118)
				ticks = 8
			#end:case
			case 7:
				(redQueen cel: 0)
				(whiteQueen cel: 0)
				ticks = 8
			#end:case
			case 8:
				(redQueen cel: 1)
				(whiteQueen cel: 1)
				ticks = 8
			#end:case
			case 9:
				(redQueen cel: 2 posn: 176 116)
				(whiteQueen cel: 2 posn: 143 116)
				ticks = 8
			#end:case
			case 10:
				(redQueen cel: 3 posn: 176 114 setPri: 7)
				(whiteQueen cel: 3 posn: 143 114 setPri: 7)
				ticks = 8
			#end:case
			case 11:
				(redQueen cel: 4 posn: 176 118)
				(whiteQueen cel: 4 posn: 143 118)
				ticks = 8
			#end:case
			case 12:
				(redQueen cel: 5 posn: 176 120)
				(whiteQueen cel: 5 posn: 143 120)
				ticks = 8
			#end:case
			case 13:
				(redQueen cel: 0 posn: 176 124)
				(whiteQueen cel: 0 posn: 143 124)
				ticks = 8
			#end:case
			case 14:
				(redQueen cel: 1 posn: 176 125)
				(whiteQueen cel: 1 posn: 143 125)
				ticks = 8
			#end:case
			case 15:
				(redQueen cel: 2 posn: 176 130)
				(whiteQueen cel: 2 posn: 143 130)
				ticks = 8
			#end:case
			case 16:
				(redQueen cel: 3 posn: 176 134)
				(whiteQueen cel: 3 posn: 143 134)
				ticks = 8
			#end:case
			case 17:
				(redQueen cel: 4 posn: 176 138)
				(whiteQueen cel: 4 posn: 143 138)
				ticks = 8
			#end:case
			case 18:
				(redQueen cel: 5 posn: 176 130)
				(whiteQueen cel: 5 posn: 143 130)
				ticks = 8
			#end:case
			case 19:
				(redQueen cel: 0 posn: 176 145)
				(whiteQueen cel: 0 posn: 143 145)
				ticks = 8
			#end:case
			case 20:
				(redQueen cel: 1 posn: 176 148)
				(whiteQueen cel: 1 posn: 143 148)
				ticks = 8
			#end:case
			case 21:
				(redQueen cel: 2 posn: 176 148)
				(whiteQueen cel: 2 posn: 143 148)
				ticks = 8
			#end:case
			case 22:
				(redQueen cel: 3 posn: 176 152)
				(whiteQueen cel: 3 posn: 143 152)
				ticks = 8
			#end:case
			case 23:
				(redQueen cel: 4 posn: 176 157)
				(whiteQueen cel: 4 posn: 143 157)
				ticks = 8
			#end:case
			case 24:
				(redQueen cel: 0 posn: 176 150)
				(whiteQueen cel: 0 posn: 143 150)
				ticks = 8
			#end:case
			case 25:
				(redQueen hide:)
				(whiteQueen hide:)
				ticks = 8
			#end:case
			case 26:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class knightBoundForward(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				register = 0
				(global2 drawPic: 490 (15 if global169 else 100))
				(redKnight
					signal: 18432
					view: 493
					cel: 0
					setLoop: 2
					init:
					setCycle: End self
				)
				(whiteKnight
					signal: 18432
					view: 492
					cel: 0
					setLoop: 2
					init:
					setCycle: End self
				)
			#end:case
			case 1:#end:case
			case 2:
				seconds = 2
			#end:case
			case 3:
				(hoofSound number: 492 setLoop: 1 play:)
				(redKnight view: 493 cel: 0 setLoop: 1)
				(whiteKnight view: 492 cel: 0 setLoop: 1)
				cycles = 3
			#end:case
			case 4:
				(redKnight cel: register posn: local34[register] 124)
				(whiteKnight cel: register posn: local41[register] 124)
				if (register.post('++') <= 6):
					state.post('--')
				#endif
				ticks = 10
			#end:case
			case 5:
				(redKnight setLoop: 0 cel: 2 stopUpd:)
				(whiteKnight setLoop: 0 cel: 2 stopUpd:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class knightBoundBack(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				register = 6
				(global2 drawPic: 490 (15 if global169 else 100))
				(redKnight signal: 18432 view: 493 setLoop: 1 init:)
				(whiteKnight signal: 18432 view: 492 setLoop: 1 init:)
				cycles = 2
			#end:case
			case 1:
				(redKnight cel: register posn: local34[register] 124)
				(whiteKnight cel: register posn: local41[register] 124)
				if (register.post('--') >= 0):
					state.post('--')
				#endif
				ticks = 10
			#end:case
			case 2:
				(global0 setMotion: MoveTo (global0 x:) 160 self)
			#end:case
			case 3:
				(whiteKnight view: 4900 setLoop: 0 cel: 0 addToPic:)
				(redKnight view: 4900 setLoop: 0 cel: 1 addToPic:)
				kernel.UnLoad(128, 492)
				kernel.UnLoad(128, 493)
				cycles = 2
			#end:case
			case 4:
				if (not proc913_0(39)):
					(global69 disable: 6)
					(global2 setScript: queensEnter)
				else:
					(global1 handsOn:)
				#endif
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class roomTimer(Timer):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class miniQueenPolka(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(whiteQueen view: 496 setLoop: 4 setPri: 5 posn: 154 93 init:)
				(redQueen view: 494 setLoop: 5 setPri: 5 posn: 156 93 init:)
				ticks = 8
			#end:case
			case 1:
				(whiteQueen posn: 158 88)
				(redQueen posn: 160 88)
				ticks = 8
			#end:case
			case 2:
				(whiteQueen setPri: 7 posn: 161 91)
				(redQueen setPri: 7 posn: 163 91)
				ticks = 8
			#end:case
			case 3:
				(whiteQueen posn: 164 91)
				(redQueen posn: 166 91)
				ticks = 8
			#end:case
			case 4:
				(whiteQueen posn: 168 94)
				(redQueen posn: 170 94)
				ticks = 8
			#end:case
			case 5:
				(whiteQueen posn: 168 93)
				(redQueen posn: 172 93)
				ticks = 8
			#end:case
			case 6:
				(whiteQueen posn: 172 97)
				(redQueen posn: 176 97)
				ticks = 8
			#end:case
			case 7:
				(whiteQueen posn: 174 96)
				(redQueen posn: 178 96)
				ticks = 8
			#end:case
			case 8:
				(whiteQueen posn: 176 100)
				(redQueen posn: 182 100)
				ticks = 8
			#end:case
			case 9:
				(whiteQueen posn: 178 99)
				(redQueen posn: 184 99)
				ticks = 8
			#end:case
			case 10:
				(whiteQueen posn: 179 103)
				(redQueen posn: 186 103)
				ticks = 8
			#end:case
			case 11:
				(whiteQueen posn: 181 102)
				(redQueen posn: 189 102)
				ticks = 8
			#end:case
			case 12:
				(whiteQueen posn: 182 106)
				(redQueen posn: 191 106)
				ticks = 8
			#end:case
			case 13:
				(whiteQueen posn: 183 105)
				(redQueen posn: 193 105)
				ticks = 8
			#end:case
			case 14:
				(whiteQueen posn: 184 110)
				(redQueen posn: 194 108)
				ticks = 8
			#end:case
			case 15:
				(whiteQueen posn: 185 108)
				(redQueen posn: 196 107)
				ticks = 8
			#end:case
			case 16:
				(whiteQueen posn: 186 113)
				(redQueen posn: 197 111)
				ticks = 8
			#end:case
			case 17:
				(whiteQueen posn: 186 112)
				(redQueen posn: 197 110)
				ticks = 8
			#end:case
			case 18:
				(whiteQueen posn: 186 118)
				(redQueen posn: 197 118)
				ticks = 8
			#end:case
			case 19:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class Red_Queen(Kq6Talker):
	#property vars (may be empty)
	name = r"""Red Queen"""
	disposeWhenDone = 1
	talkWidth = 213
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if proc913_0(59):
			(cond
				case (((redQueen loop:) == 0) and ((redQueen view:) == 494)):
					(self view: 495 loop: 4 x: 173 y: 82 textX: -89 textY: -72)
					(super init: 0 0 tRMouth2 &rest)
				#end:case
				case 
					(and
						((redQueen cel:) == 3)
						((redQueen loop:) == 1)
						((redQueen view:) == 495)
					):
					(self view: 495 loop: 4 x: 171 y: 82 textX: -89 textY: -72)
					(super init: 0 0 tRMouth2 &rest)
				#end:case
				else:
					(self
						view: 890
						loop: 0
						cel: 1
						x: 309
						y: 5
						textX: -223
						textY: 6
					)
					(super init: 0 0 0 &rest)
				#end:else
			)
		else:
			(self view: 495 loop: 3 x: 174 y: 80 textX: -89 textY: -72)
			(super init: 0 0 tRMouth &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class tRMouth(Prop):
	#property vars (may be empty)
	view = 495
	loop = 3
	
#end:class or instance

@SCI.instance
class tRMouth2(Prop):
	#property vars (may be empty)
	view = 495
	loop = 4
	
#end:class or instance

@SCI.instance
class White_Queen(Kq6Talker):
	#property vars (may be empty)
	name = r"""White Queen"""
	x = 142
	y = 82
	view = 890
	cel = 1
	disposeWhenDone = 1
	talkWidth = 213
	textX = -127
	textY = -79
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if proc913_0(59):
			if 
				(and
					(not (whiteQueen cel:))
					(not (whiteQueen loop:))
					((whiteQueen view:) == 496)
				)
				(self view: 497 setLoop: 4 x: 146 y: 82 textX: -127 textY: -73)
				(super init: 0 0 tWMouth2 &rest)
			else:
				(self view: 890 setLoop: 0 cel: 1 x: 5 y: 5 textX: 10 textY: 6)
				(super init: 0 0 0 &rest)
			#endif
		else:
			(self view: 497 loop: 3 x: 135 y: 76 textX: -127 textY: -63)
			(super init: 0 0 tWMouth &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class tWMouth(Prop):
	#property vars (may be empty)
	view = 497
	loop = 3
	
#end:class or instance

@SCI.instance
class tWMouth2(Prop):
	#property vars (may be empty)
	view = 497
	loop = 4
	
#end:class or instance

@SCI.instance
class hoofSound(Kq6Sound):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class coalToQueen(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				local3 = 99
				(global0 put: 6 490)
				(global0 illegalBits: 0 setMotion: MoveTo 176 136 self)
			#end:case
			case 1:
				(global0 setHeading: 335 self)
			#end:case
			case 2:
				(global0 view: 491 loop: 3 cel: 0 normal: 0 cycleSpeed: 10)
				cycles = 4
			#end:case
			case 3:
				(global0 setCycle: CT 4 1 self)
				(whiteQueen view: 497 setLoop: 0 cel: 0 setCycle: CT 3 1)
			#end:case
			case 4:
				(global1 givePoints: 1)
				(global91 say: 6 46 0 1 self)
			#end:case
			case 5:
				(global0 setCycle: End self)
			#end:case
			case 6:
				(global0 reset: 7)
				(whiteQueen setCycle: Beg self)
			#end:case
			case 7:
				(global91 say: 6 46 0 2 self)
			#end:case
			case 8:
				(whiteQueen view: 497 setLoop: 1 cel: 0 setCycle: End self)
			#end:case
			case 9:
				proc913_1(59)
				(whiteQueen view: 496 setLoop: 0 cel: 0)
				cycles = 4
			#end:case
			case 10:
				(global91 say: 6 46 0 3 self)
			#end:case
			case 11:
				(redQueen view: 4951 setLoop: 1 cel: 0 setCycle: End self)
				if (not (global105 handle:)):
					(global105 number: 493 setLoop: 1 play:)
				#endif
			#end:case
			case 12:
				(redQueen view: 494 setLoop: 0 cel: 1)
				cycles = 4
			#end:case
			case 13:
				(global91 say: 6 46 0 4 self)
			#end:case
			case 14:
				(redQueen view: 4951 setLoop: 1 cel: 3 setCycle: Beg self)
				(whiteQueen view: 497 setLoop: 1 cel: 3 setCycle: Beg self)
			#end:case
			case 15:#end:case
			case 16:
				proc913_2(59)
				(redQueen view: 4951 setLoop: 0 cel: 0)
				(whiteQueen view: 497 setLoop: 0 cel: 0)
				cycles = 4
			#end:case
			case 17:
				(global91 say: 6 46 0 5 self)
			#end:case
			case 18:
				(global0
					view: 491
					loop: 3
					cel: 0
					normal: 0
					cycleSpeed: 10
					setCycle: CT 4 1 self
				)
				(whiteQueen view: 497 setLoop: 0 cel: 0 setCycle: CT 3 1 self)
			#end:case
			case 19:#end:case
			case 20:
				(whiteQueen setCycle: Beg self)
				(global0 setCycle: End self)
			#end:case
			case 21:#end:case
			case 22:
				(global0 reset: 7 get: 10)
				cycles = 6
			#end:case
			case 23:
				(global91 say: 6 46 0 6 self)
			#end:case
			case 24:
				proc913_1(59)
				(global2 setScript: queensLeave 0 46)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class queensLeave(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				ticks = 8
			#end:case
			case 1:
				(self setScript: hopOut self)
			#end:case
			case 2:
				(global2 drawPic: 490 (15 if global169 else 100))
				(redKnight signal: 18432 view: 4900 setLoop: 0 cel: 1 init:)
				(whiteKnight signal: 18432 view: 4900 setLoop: 0 cel: 0 init:)
				ticks = 12
			#end:case
			case 3:
				match register
					case 1:
						(global91 say: 1 0 2 15 self)
					#end:case
					case 46:
						(global91 say: 6 46 0 7 self)
					#end:case
					else:
						(self cue:)
					#end:else
				#end:match
			#end:case
			case 4:
				seconds = 3
			#end:case
			case 5:
				(global103 fade: 40 10 2 0)
				(whiteQueen setScript: miniQueenSplit)
				ticks = 60
			#end:case
			case 6:
				match register
					case 1:
						(global91 say: 1 0 2 16 self)
					#end:case
					case 46:
						(myConv
							add: -1 6 46 0 8
							add: -1 6 46 0 9
							add: -1 6 46 0 10
							add: -1 6 46 0 11
							init: self
						)
					#end:case
					else:
						(self cue:)
					#end:else
				#end:match
			#end:case
			case 7:
				if (register == 46):
					register = (global0 cycleSpeed:)
					(global0
						view: 499
						cel: 0
						normal: 0
						cycleSpeed: 8
						setCycle: End self
					)
					local51 = 1
				else:
					cycles = 2
				#endif
			#end:case
			case 8:
				seconds = 2
			#end:case
			case 9:
				if local51:
					(global0 cycleSpeed: register setCycle: Beg self)
				else:
					cycles = 2
				#endif
				(global103 fade: 0 15 10 1)
			#end:case
			case 10:
				if ((global0 y:) < 153):
					(global0
						reset: 2
						setLoop: -1
						setMotion: PolyPath 150 170 self
					)
				else:
					(self cue:)
				#endif
			#end:case
			case 11:
				(global0 reset: 2 setLoop: -1 setHeading: 180 self)
			#end:case
			case 12:
				seconds = 4
			#end:case
			case 13:
				(global103 number: 0 stop:)
				(global102 pause: 0)
				proc913_2(59)
				local52 = 0
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

