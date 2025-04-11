#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 320
import sci_sh
import Main
import rCliffs
import n913
import Feature
import LoadMany
import Motion
import User
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm320 = 0,
	dieHard = 1,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = [54, 54, 54, 54, 54, 54, 54, 54, 54, 68, 68, 68, 68, 68, 68, 82, 82, 82, 82, 82, 96, 96, 96, 96, 96, 96, 96, 96]
local29 = [100, 114, 126, 143, 155, 164, 176, 188, 202, 117, 131, 143, 161, 173, 187, 126, 140, 155, 167, 179, 109, 121, 136, 150, 162, 175, 187, 199]
local57 = [68, 68, 68, 68, 68, 68, 68, 68, 68, 82, 82, 82, 82, 82, 82, 96, 96, 96, 96, 96, 110, 110, 110, 110, 110, 110, 110, 110]
local85 = [114, 126, 138, 155, 164, 176, 188, 202, 215, 131, 143, 157, 173, 187, 199, 140, 155, 167, 179, 191, 121, 136, 150, 162, 175, 187, 199, 212]
local113 = [103, 117, 129, 146, 158, 167, 179, 191, 205, 120, 134, 146, 164, 176, 190, 129, 143, 158, 170, 182, 112, 124, 139, 153, 165, 178, 190, 202]
local141 = [61, 61, 61, 61, 61, 61, 61, 61, 61, 75, 75, 75, 75, 75, 75, 89, 89, 89, 89, 89, 103, 103, 103, 103, 103, 103, 103, 103]
local169 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4]
local197 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 6, 7]
local225 = [1, 0, 0, 2, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0]
local253 = [54, 67, 67, 67, 67, 62, 80, 80, 80, 80, 94, 94, 94, 94, 94, 94, 94, 108, 108, 109, 109, 109, 122, 119, 135, 144]
local279 = [65, 78, 78, 78, 78, 73, 91, 91, 91, 91, 105, 105, 105, 105, 105, 105, 105, 119, 119, 120, 120, 120, 133, 130, 146, 155]
local305 = [168, 117, 133, 150, 168, 188, 101, 117, 133, 150, 109, 126, 143, 160, 177, 194, 211, 109, 126, 143, 161, 227, 161, 191, 161, 180]
local331 = [181, 130, 146, 163, 181, 201, 114, 130, 146, 163, 122, 139, 156, 173, 190, 207, 224, 122, 139, 156, 174, 240, 174, 204, 174, 193]
local357 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
local383 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
local409 = [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0]
local435 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 4, 0, 0, 0, 0]
local461 = [76, 77, 76, 76]
local465 = [160, 97, 190, 129]
local469 = [97, 97, 97, 97]
local473 = [187, 124, 217, 156]
local477 = [1, 1, 1, 1]
local481 = [2, 0, 3, 1]
local485 = [169, 106, 199, 138]
local489 = [76, 76, 76, 76]
local493 = [0, 2, 1, 3]
local497 = [1, 0, 0, 0]
local501


@SCI.instance
class rm320(CliffRoom):
	#property vars (may be empty)
	picture = 320
	horizon = 0
	walkOffEdge = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global1 handsOff:)
		if (global12 == 300):
			(self style: 14)
		else:
			(self style: -32758)
			if ((global102 number:) != 915):
				(global102 number: 915 setLoop: -1 play:)
			#endif
		#endif
		(proc958_0 128 322 325)
		(super init: &rest)
		(rCliffs stepDirection: 3)
		if (proc913_0 123):
			(global2 allRocksOut: 0)
		else:
			(global2 constantRocks:)
		#endif
		(writ x: 230 init: stopUpd:)
		(theRoom init:)
		(global0
			view: 301
			normal: 0
			cycleSpeed: 14
			setLoop: 2
			posn: 101 182
			setPri: 10
			init:
			actions: egoStepVerb
		)
		((ScriptID 21 0) notify:)
		(global74 add: self)
		(global1 handsOn:)
	#end:method

	@classmethod
	def notify():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global2 setScript: insetDispose)
	#end:method

	@classmethod
	def cue(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				(global0 signal: 8192)
				(rCliffs cheatCount: 1)
				(global2 setScript: nextCliffUp)
			#end:case
			case 0:
				(rCliffs cheatCount: 15)
				(global2 setScript: nextCliffDown)
			#end:case
			case -1:
				(global2 setScript: downToBeach)
			#end:case
		#end:match
	#end:method

#end:class or instance

class PuzzleBackup(View):
	#property vars (may be empty)
	lookMsg = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(global72 addToFront: self)
		(global73 addToFront: self)
		(global74 addToFront: self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global72 delete: self)
		(global73 delete: self)
		(global74 delete: self)
		(super dispose:)
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if 
			(and
				(User canInput:)
				(or
					(((param1 message:) == 13) and ((param1 type:) == 4))
					((param1 type:) == 1)
				)
				((param1 type:) != 16384)
				(not (param1 modifiers:))
			)
			(cond
				case 
					(and
						(or
							((param1 type:) & 0x0001)
							(and
								((param1 type:) & 0x0004)
								((param1 message:) == 13)
							)
						)
						(self onMe: param1)
						((global69 curIcon:) == (global69 at: 2))
					):
					(param1 claimed: 1)
					(cond
						case (global5 contains: puzzle3):
							(global91 say: 2 1 0 1 0 21)
						#end:case
						case (global5 contains: puzzle1):
							(global91 say: 1 1 0 1 0 21)
						#end:case
						else:
							(global91 say: lookMsg 1 0 1 0 21)
						#end:else
					)
				#end:case
				case 
					(and
						(or
							((param1 type:) & 0x0001)
							(and
								((param1 type:) & 0x0004)
								((param1 message:) == 13)
							)
						)
						(self onMe: param1)
						((global69 curIcon:) == (global69 at: 1))
					):
					(param1 claimed: 1)
					0
				#end:case
				else:
					(super handleEvent: param1)
				#end:else
			)
		else:
			(super handleEvent: param1)
		#endif
		(param1 claimed:)
	#end:method

#end:class or instance

@SCI.instance
class puzzle1(PuzzleInset):
	#property vars (may be empty)
	x = 157
	y = 39
	z = -45
	view = 322
	maxButtons = 4
	buttNumber = 26
	buttView = 322
	lookMsg = 1
	puzzNumber = 2
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self
			buttTop: @local253
			buttLeft: @local305
			buttRight: @local331
			buttBottom: @local279
			buttLoop: @local357
			buttCel: @local383
			buttX: @local305
			buttY: @local253
			buttVal: @local435
			buttKill: @local501
		)
		(super init:)
		(headStone init:)
		(headStoneWords loop: 1 init:)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(headStone dispose:)
		(headStoneWords dispose:)
		(super dispose:)
		(global0 view: 301 setLoop: 6 cel: 0)
		(UnLoad 128 3012)
	#end:method

#end:class or instance

@SCI.instance
class puzzle2(PuzzleInset):
	#property vars (may be empty)
	x = 163
	y = 59
	z = -28
	view = 320
	maxButtons = 3
	buttNumber = 4
	buttView = 323
	lookMsg = 3
	puzzNumber = 3
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self
			buttTop: @local461
			buttLeft: @local465
			buttRight: @local473
			buttBottom: @local469
			buttLoop: @local477
			buttCel: @local481
			buttX: @local485
			buttY: @local489
			buttVal: @local493
			buttKill: @local497
		)
		(super init:)
		(rollos init: stopUpd:)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(rollos dispose:)
		(super dispose:)
		(global0 view: 301 setLoop: 1)
		(UnLoad 128 3012)
	#end:method

#end:class or instance

@SCI.instance
class puzzle3(PuzzleInset):
	#property vars (may be empty)
	x = 157
	y = 39
	z = -45
	view = 322
	maxButtons = 4
	buttNumber = 26
	buttView = 322
	lookMsg = 2
	puzzNumber = 4
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self
			buttTop: @local253
			buttLeft: @local305
			buttRight: @local331
			buttBottom: @local279
			buttLoop: @local357
			buttCel: @local383
			buttX: @local305
			buttY: @local253
			buttVal: @local409
			buttKill: @local501
		)
		(super init:)
		(headStone init:)
		(headStoneWords loop: 2 init:)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(headStone dispose:)
		(headStoneWords dispose:)
		(super dispose:)
		(global0 view: 301 setLoop: 6 cel: 0)
		(UnLoad 128 3012)
	#end:method

#end:class or instance

@SCI.instance
class puzzle4(PuzzleInset):
	#property vars (may be empty)
	x = 157
	y = 39
	z = -45
	view = 320
	maxButtons = 6
	buttNumber = 28
	buttView = 324
	lookMsg = 5
	puzzNumber = 5
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self
			buttTop: @local1
			buttLeft: @local29
			buttRight: @local85
			buttBottom: @local57
			buttLoop: @local169
			buttCel: @local197
			buttX: @local113
			buttY: @local141
			buttVal: @local225
			buttKill: @local501
		)
		(super init:)
		(words init: stopUpd:)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(words dispose:)
		(super dispose:)
		(global0 view: 301 setLoop: 1)
		(UnLoad 128 3012)
	#end:method

#end:class or instance

@SCI.instance
class words(View):
	#property vars (may be empty)
	x = 211
	y = 62
	z = -45
	view = 324
	priority = 13
	signal = 16400
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(puzzle4 doVerb: param1 &rest)
	#end:method

#end:class or instance

@SCI.instance
class rollos(View):
	#property vars (may be empty)
	x = 98
	y = 66
	z = -12
	view = 323
	priority = 13
	signal = 16400
	
#end:class or instance

@SCI.instance
class headStone(PuzzleBackup):
	#property vars (may be empty)
	x = 150
	y = 7
	view = 325
	priority = 3
	signal = 16400
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (global5 contains: puzzle1):
			(puzzle1 doVerb: param1 &rest)
		else:
			(puzzle3 doVerb: param1 &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class headStoneWords(PuzzleBackup):
	#property vars (may be empty)
	x = 148
	y = 17
	view = 325
	priority = 4
	signal = 16400
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (global5 contains: puzzle1):
			(puzzle1 doVerb: param1 &rest)
		else:
			(puzzle3 doVerb: param1 &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class theRoom(Feature):
	#property vars (may be empty)
	noun = 3
	nsBottom = 190
	nsRight = 320
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(global93 add: self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global93 delete: self)
		(super dispose:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 3:
				(proc913_1 59)
				(global2 setScript: dieHard)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class writ(View):
	#property vars (may be empty)
	y = 189
	z = 135
	noun = 4
	view = 326
	priority = 9
	signal = 16400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(global72 add: self)
		(global73 add: self)
		(global74 add: self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global72 delete: self)
		(global73 delete: self)
		(global74 delete: self)
		(super dispose:)
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if 
			(and
				(not ((ScriptID 21 0) puzzleIsUp:))
				(or
					((global69 curIcon:) == (global69 at: 1))
					((global69 curIcon:) == (global69 at: 2))
				)
				(or
					(((param1 message:) == 13) and ((param1 type:) == 4))
					((param1 type:) == 1)
				)
				(User canInput:)
				((param1 type:) != 16384)
				(self onMe: param1)
				(not (param1 modifiers:))
			)
			(param1 claimed: 1)
			if (((global0 y:) < 110) or ((global0 y:) > 120)):
				(global91 say: 4 1 13 1)
			else:
				if ((global0 loop:) == 6):
					(global0 view: 3012 setLoop: 0 cel: 1)
				else:
					(global0 view: 3012 setLoop: 0 cel: 0)
				#endif
				(UnLoad 128 301)
				match ((ScriptID 21 0) cliffFace:)
					case 0:
						if (proc913_0 123):
							(puzzle1 puzzSolved:)
						else:
							(global2 setScript: insetInit 0 puzzle1)
						#endif
					#end:case
					case 1:
						if (proc913_0 124):
							(puzzle2 puzzSolved:)
						else:
							(global2 setScript: insetInit 0 puzzle2)
						#endif
					#end:case
					case 2:
						if (proc913_0 125):
							(puzzle3 puzzSolved:)
						else:
							(global2 setScript: insetInit 0 puzzle3)
						#endif
					#end:case
					case 3:
						if (proc913_0 126):
							(puzzle4 puzzSolved:)
						else:
							(global2 setScript: insetInit 0 puzzle4)
						#endif
					#end:case
				#end:match
			#endif
		else:
			(super handleEvent: param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class insetDispose(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				ticks = 6
			#end:case
			case 1:
				if (mod ((ScriptID 21 0) cliffFace:) 2):
					(global2 flipRocks: 1 callForRocks:)
				else:
					(global2 flipRocks: 0 callForRocks:)
				#endif
			#end:case
			case 2:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class nextCliffUp(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				if (((ScriptID 21 0) cliffFace:) == 3):
					(global102 fade: 0 10 10)
					(global105 stop:)
					(global2 newRoom: 340)
				else:
					(global2 dumpRocks:)
					(self cue:)
				#endif
			#end:case
			case 1:
				(rCliffs cliffFace: ((rCliffs cliffFace:) + 1))
				if ((rCliffs cliffFace:) > 3):
					(rCliffs cliffFace: 3)
				#endif
				match ((ScriptID 21 0) cliffFace:)
					case 1:
						(UnLoad 128 322)
						(UnLoad 128 325)
						if (proc913_0 124):
							(global2 allRocksOut: 1)
						else:
							(global2 constantRocks: 1)
						#endif
						(proc958_0 128 320 323)
					#end:case
					case 2:
						(UnLoad 128 320)
						(UnLoad 128 323)
						if (proc913_0 125):
							(global2 allRocksOut: 0)
						else:
							(global2 constantRocks:)
						#endif
						(proc958_0 128 322 325)
					#end:case
					case 3:
						(UnLoad 128 322)
						(UnLoad 128 325)
						if (proc913_0 126):
							(global2 allRocksOut: 1)
						else:
							(global2 constantRocks: 1)
						#endif
						(proc958_0 128 320 324)
					#end:case
				#end:match
				(global2 drawPic: 320 14)
				if (mod ((ScriptID 21 0) cliffFace:) 2):
					(writ
						loop: (1 if (((ScriptID 21 0) cliffFace:) == 1) else 0)
						x: 90
						stopUpd:
					)
					(global0 posn: 238 182 setLoop: 6 cel: 0 setPri: 10 show:)
				else:
					(writ loop: 0 x: 230 stopUpd:)
					(global0 posn: 101 182 setLoop: 2 cel: 0 setPri: 10 show:)
				#endif
				(global1 handsOn:)
				((ScriptID 21 0) notify:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class downToBeach(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(proc21_1)
				(global0
					view: 301
					setLoop: 7
					cel: 0
					posn: ((global0 x:) + 2) ((global0 y:) + 2)
					cycleSpeed: 16
				)
				cycles = 8
			#end:case
			case 1:
				(global0 cel: 1 posn: (global0 x:) (global0 y:))
				cycles = 8
			#end:case
			case 2:
				(global0 cel: 2 posn: (global0 x:) (global0 y:))
				cycles = 8
			#end:case
			case 3:
				(global0 cel: 3 posn: (global0 x:) ((global0 y:) - 1))
				cycles = 8
			#end:case
			case 4:
				(global0 cel: 4 posn: ((global0 x:) - 4) ((global0 y:) - 4))
				cycles = 8
			#end:case
			case 5:
				(global0 cel: 5 posn: (global0 x:) (global0 y:))
				cycles = 8
			#end:case
			case 6:
				(global0 cel: 6 posn: (global0 x:) (global0 y:))
				cycles = 8
			#end:case
			case 7:
				(global0
					setLoop: 5
					cel: 0
					cycleSpeed: 12
					posn: ((global0 x:) - 7) ((global0 y:) + 19)
					setCycle: End self
				)
				(rCliffs stepDirection: 1)
			#end:case
			case 8:
				(global2 dumpRocks:)
				(global2 newRoom: 300)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class nextCliffDown(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				((ScriptID 21 0) cue:)
				if ((rCliffs stepDirection:) == 2):
					temp0 = 5
					temp1 = 18
					temp2 = 6
					(rCliffs stepDirection: 1)
				else:
					temp0 = 4
					temp1 = -19
					temp2 = 7
					(rCliffs stepDirection: 2)
				#endif
				(global0
					setLoop: temp0
					cel: 0
					cycleSpeed: 12
					posn: ((global0 x:) + temp1) ((global0 y:) + temp2)
					setCycle: End self
				)
			#end:case
			case 1:
				(proc21_1)
				if ((rCliffs stepDirection:) == 2):
					temp0 = 7
					temp1 = -14
					temp2 = -6
				else:
					temp0 = 8
					temp1 = 14
					temp2 = -5
				#endif
				(global0
					view: 301
					setLoop: temp0
					cel: 0
					posn: ((global0 x:) + temp1) ((global0 y:) + temp2)
					cycleSpeed: 16
				)
				cycles = 8
			#end:case
			case 2:
				(global0 cel: 1 posn: (global0 x:) (global0 y:))
				cycles = 8
			#end:case
			case 3:
				(global0 cel: 2 posn: (global0 x:) (global0 y:))
				cycles = 8
			#end:case
			case 4:
				if ((rCliffs stepDirection:) == 2):
					temp2 = 0
				else:
					temp2 = -3
				#endif
				(global0 cel: 3 posn: (global0 x:) ((global0 y:) + temp2))
				cycles = 8
			#end:case
			case 5:
				if ((rCliffs stepDirection:) == 2):
					temp1 = -4
					temp2 = 0
				else:
					temp1 = 4
					temp2 = -1
				#endif
				(global0
					cel: 4
					posn: ((global0 x:) + temp1) ((global0 y:) + temp2)
				)
				cycles = 8
			#end:case
			case 6:
				(global0 cel: 5 posn: (global0 x:) (global0 y:))
				cycles = 8
			#end:case
			case 7:
				if ((rCliffs stepDirection:) == 2):
					temp2 = -2
				else:
					temp2 = 0
				#endif
				(global0 cel: 6 posn: (global0 x:) ((global0 y:) + temp2))
				cycles = 8
			#end:case
			case 8:
				if ((rCliffs stepDirection:) == 2):
					temp0 = 6
					temp1 = -25
					temp2 = 11
				else:
					temp0 = 1
					temp1 = 27
					temp2 = 12
				#endif
				(global0
					view: 301
					setLoop: temp0
					cel: 0
					posn: ((global0 x:) + temp1) ((global0 y:) + temp2)
				)
				cycles = 8
			#end:case
			case 9:
				((ScriptID 21 0) cliffFace: (((ScriptID 21 0) cliffFace:) - 1))
				(global2 dumpRocks:)
				(global2 drawPic: 320 13)
				match ((ScriptID 21 0) cliffFace:)
					case 0:
						(UnLoad 128 320)
						(UnLoad 128 323)
						(proc958_0 128 322 325)
						(global2 allRocksOut: 0)
						(writ loop: 0 x: 230 stopUpd:)
						(global0 view: 301 setLoop: 6 cel: 0 posn: 210 4)
					#end:case
					case 1:
						(UnLoad 128 322)
						(UnLoad 128 325)
						(proc958_0 128 320 323)
						(global2 allRocksOut: 1)
						(writ
							loop:
								if (((ScriptID 21 0) cliffFace:) == 1):
									1
								else:
									0
								#endif
							x: 90
							stopUpd:
						)
						(global0 view: 301 setLoop: 1 cel: 0 posn: 127 4)
					#end:case
					case 2:
						(UnLoad 128 320)
						(UnLoad 128 324)
						(proc958_0 128 322 325)
						(global2 allRocksOut: 0)
						(writ loop: 0 x: 230 stopUpd:)
						(global0 view: 301 setLoop: 6 cel: 0 posn: 210 4)
					#end:case
				#end:match
				cycles = 8
			#end:case
			case 10:
				(proc21_1)
				if ((rCliffs stepDirection:) == 2):
					temp0 = 7
					temp1 = 1
					temp2 = 1
				else:
					temp0 = 8
					temp1 = 1
					temp2 = 0
				#endif
				(global0
					view: 301
					setLoop: temp0
					cel: 0
					cycleSpeed: 16
					posn: ((global0 x:) + temp1) ((global0 y:) + temp2)
				)
				cycles = 8
			#end:case
			case 11:
				(global0 cel: 1 posn: (global0 x:) (global0 y:))
				cycles = 8
			#end:case
			case 12:
				(global0 cel: 2 posn: (global0 x:) (global0 y:))
				cycles = 8
			#end:case
			case 13:
				if ((rCliffs stepDirection:) == 2):
					temp1 = 1
					temp2 = -2
				else:
					temp1 = 0
					temp2 = 0
				#endif
				(global0
					cel: 3
					posn: ((global0 x:) + temp1) ((global0 y:) + temp2)
				)
				cycles = 8
			#end:case
			case 14:
				if ((rCliffs stepDirection:) == 2):
					temp1 = -4
				else:
					temp1 = 1
				#endif
				(global0 cel: 4 posn: ((global0 x:) + temp1) (global0 y:))
				cycles = 8
			#end:case
			case 15:
				if ((rCliffs stepDirection:) == 2):
					temp1 = 0
				else:
					temp1 = -1
				#endif
				(global0 cel: 5 posn: ((global0 x:) + temp1) (global0 y:))
				cycles = 8
			#end:case
			case 16:
				if ((rCliffs stepDirection:) == 2):
					temp1 = 0
				else:
					temp1 = -1
				#endif
				(global0 cel: 6 posn: ((global0 x:) + temp1) (global0 y:))
				cycles = 8
			#end:case
			case 17:
				if ((rCliffs stepDirection:) == 2):
					temp0 = 6
					temp1 = -27
					temp2 = 13
				else:
					temp0 = 1
					temp1 = 29
					temp2 = 12
				#endif
				(global0
					view: 301
					setLoop: temp0
					cel: 0
					posn: ((global0 x:) + temp1) ((global0 y:) + temp2)
				)
				if (local0 == 3):
					(self cue:)
				else:
					seconds = 2
				#endif
			#end:case
			case 18:
				if (local0 < 3):
					local0++
					(state -= 9)
				else:
					local0 = 0
				#endif
				(self cue:)
			#end:case
			case 19:
				if ((rCliffs stepDirection:) == 2):
					temp0 = 5
					temp1 = 18
					temp2 = 7
					(rCliffs stepDirection: 3)
				else:
					temp0 = 4
					temp1 = -19
					temp2 = 7
					(rCliffs stepDirection: 4)
				#endif
				(global0
					setLoop: temp0
					cel: 0
					cycleSpeed: 12
					posn: ((global0 x:) + temp1) ((global0 y:) + temp2)
					setCycle: End self
				)
			#end:case
			case 20:
				if ((global0 loop:) == 4):
					temp0 = 6
					temp1 = -15
					temp2 = -7
				else:
					temp0 = 1
					temp1 = 17
					temp2 = -7
				#endif
				(global0
					setLoop: temp0
					cel: 0
					posn: ((global0 x:) + temp1) ((global0 y:) + temp2)
				)
				ticks = 4
			#end:case
			case 21:
				(global1 handsOn:)
				((ScriptID 21 0) cheatCount: 10)
				((ScriptID 21 0) notify:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class insetInit(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				((ScriptID 21 0) cue:)
				(global91 say: 4 1 12 1 self)
			#end:case
			case 1:
				(register init:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class dieHard(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global69 disable: 6)
				((ScriptID 21 0) cue:)
				if ((global0 loop:) < 6):
					(global0
						posn: ((global0 x:) - 8) ((global0 y:) - 3)
						view: 900
						setLoop: 0
						cel: 0
					)
				else:
					(global0
						posn: ((global0 x:) + 6) ((global0 y:) - 3)
						view: 900
						setLoop: 1
						cel: 0
					)
				#endif
				cycles = 6
			#end:case
			case 1:
				(proc913_2 59)
				(global0
					x:
						if ((global0 loop:) == 1):
							((global0 x:) - 18)
						else:
							((global0 x:) + 18)
						#endif
					y:
						if ((global0 loop:) == 1):
							((global0 y:) + 2)
						else:
							((global0 y:) + 2)
						#endif
					view: 4011
					normal: 0
					cycleSpeed: 6
					setLoop: (1 if ((global0 loop:) == 1) else 0)
					setCycle: CT 10 1 self
				)
			#end:case
			case 2:
				(global104 number: 306 setLoop: 1 play: self)
				(global0 setCycle: End)
			#end:case
			case 3:
				(global0 y: 280)
				seconds = 2
			#end:case
			case 4:
				(global104 number: 307 setLoop: 1 play:)
				(ShakeScreen 2 2)
				ticks = 4
			#end:case
			case 5:
				(global91 say: 9 3 38 3 self)
			#end:case
			case 6:
				(global105 fade: 0 5 5)
				(proc0_1 8)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoStepVerb(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				return 0
			#end:case
			case 5:
				return 0
			#end:case
			case 2:
				return 0
			#end:case
			else:
				(global91 say: 0 0 64 1 0 899)
				return 1
			#end:else
		#end:match
	#end:method

#end:class or instance

