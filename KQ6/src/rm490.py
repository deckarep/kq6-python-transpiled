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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 71, 124, 8, 189, 0, 189, 0, 0, 319, 0, 319, 189, 300, 189, 243, 124,
					'yourself:'
				)
		)
		super._send('init:', &rest)
		global102._send('number:', 490, 'setLoop:', -1, 'play:')
		global32._send('add:', theSky, thePath, theSteps, 'eachElementDo:', #init)
		redKnight._send('addToPic:')
		whiteKnight._send('addToPic:')
		if (proc913_0(39) and (global9._send('at:', 41)._send('owner:') == global11)):
			redScarf._send('init:')
		#endif
		global2._send('setScript:', egoEnters)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match local3.post('++')
			case 1:
				global1._send('handsOff:')
				global91._send('say:', 1, 0, 10, 0, self)
			#end:case
			case 2:
				global2._send('setScript:', queensLeave, 0, 0)
			#end:case
		#end:match
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		roomTimer._send('dispose:', 'delete:')
		super._send('newRoom:', param1)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case global2._send('script:'):#end:case
			case (global0._send('edgeHit:') == 3):
				global2._send('walkOffEdge:', 1, 'setScript:', walkOut)
			#end:case
			case (global0._send('y:') <= 128):
				if ((not local3) and local52):
					global0._send('setMotion:', 0)
					global2._send('cue:')
				else:
					global0._send('posn:', global0._send('x:'), (global0._send('y:') + 1), 'setMotion:', 0)
					global2._send('setScript:', knightBlock, 0, 3)
				#endif
			#end:case
		)
		super._send('doit:')
	#end:method

	@classmethod
	def scriptCheck():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 0
		if local52:
			global91._send('say:', 0, 0, 234, 0, 0, 899)
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
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if global5._send('contains:', whiteQueen):
			global91._send('say:', 7, 0, 11, 1)
		else:
			local0 = 8
			match param1
				case 5:
					global2._send('setScript:', knightBlock, 0, param1)
				#end:case
				case 2:
					global2._send('setScript:', knightBlock, 0, param1)
				#end:case
				case 46:
					global2._send('setScript:', knightBlock, 0, param1)
				#end:case
				case 72:
					global2._send('setScript:', knightBlock, 0, param1)
				#end:case
				case 1:
					super._send('doVerb:', param1, &rest)
				#end:case
				else:
					global2._send('setScript:', knightBlock, 0, 0)
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
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if global5._send('contains:', redQueen):
			global91._send('say:', 7, 0, 11, 1)
		else:
			local0 = 7
			match param1
				case 5:
					global2._send('setScript:', knightBlock, 0, param1)
				#end:case
				case 2:
					global2._send('setScript:', knightBlock, 0, param1)
				#end:case
				case 46:
					global2._send('setScript:', knightBlock, 0, param1)
				#end:case
				case 72:
					global2._send('setScript:', knightBlock, 0, param1)
				#end:case
				case 1:
					if ((not local53.post('--')) and (global12 == 99)):
						global0._send('get:', 6)
					#endif
					super._send('doVerb:', param1, &rest)
				#end:case
				else:
					global2._send('setScript:', knightBlock, 0, 0)
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
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 46:
				global91._send('say:', 5, 46, 0, 1)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case 
				(and
					(not global105._send('handle:'))
					(cel == 2)
					(loop == 3)
					(view == 494)
				):
				global105._send('number:', 493, 'setLoop:', 1, 'play:')
			#end:case
			case 
				(and
					(not global105._send('handle:'))
					(cel == 2)
					(loop == 1)
					(view == 495)
				):
				global105._send('number:', 493, 'setLoop:', 1, 'play:')
			#end:case
		)
		super._send('doit:', &rest)
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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('doit:', &rest)
		(cond
			case 
				(and
					(not global105._send('handle:'))
					(cel == 2)
					(loop == 3)
					(view == 496)
				):
				global105._send('number:', 493, 'setLoop:', 1, 'play:')
			#end:case
			case 
				(and
					(not global105._send('handle:'))
					(cel == 2)
					(loop == 1)
					(view == 497)
				):
				global105._send('number:', 493, 'setLoop:', 1, 'play:')
			#end:case
		)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 46:
				global2._send('setScript:', coalToQueen)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if global5._send('contains:', redQueen):
			self._send('setCycle:', End, self)
		else:
			self._send('view:', 4900, 'setLoop:', 0, 'cel:', 3, 'stopUpd:')
		#endif
		super._send('init:')
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('view:', 4900, 'setLoop:', 0, 'cel:', 3, 'stopUpd:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global2._send('setScript:', getScarf)
			#end:case
			else:
				super._send('doVerb:', param1)
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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('setOnMeCheck:', 1, 16)
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class knightBlock(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				(cond
					case ((register == 3) or (register == 5)):
						global0._send('setMotion:', PolyPath, 150, 140, self)
					#end:case
					case (local0 == 8):
						global0._send('setMotion:', PolyPath, 130, 145, self)
					#end:case
					else:
						global0._send('setMotion:', PolyPath, 178, 145, self)
					#end:else
				)
				self._send('setScript:', knightBoundForward, self)
			#end:case
			case 1:
				global0._send('setHeading:', 0, self)
			#end:case
			case 2:#end:case
			case 3:
				redKnight._send('view:', 493, 'setLoop:', 0, 'cel:', 2)
				whiteKnight._send('view:', 492, 'setLoop:', 0, 'cel:', 2)
				ticks = 30
			#end:case
			case 4:
				match register
					case 3:
						global91._send('say:', 3, 3, 5, 0, self)
					#end:case
					case 5:
						global91._send('say:', 3, 3, 5, 0, self)
					#end:case
					case 2:
						if (proc913_0(39) and proc913_0(69)):
							global91._send('say:', 7, 2, 9, 0, self)
						else:
							proc913_1(69)
							global91._send('say:', 7, 2, 7, 0, self)
						#endif
					#end:case
					case 46:
						global91._send('say:', 7, 46, 0, 0, self)
					#end:case
					case 72:
						global91._send('say:', local0, 72, 0, 0, self)
					#end:case
					case 0:
						global91._send('say:', 7, 0, 0, 0, self)
					#end:case
					else:
						global1._send('handsOn:')
						self._send('dispose:')
					#end:else
				#end:match
			#end:case
			case 5:
				hoofSound._send('number:', 492, 'setLoop:', 1, 'play:')
				client._send('setScript:', knightBoundBack)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class queensEnter(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global102._send('pause:', 1)
				global2._send('drawPic:', 490, (15 if global169 else 100))
				global103._send('number:', 491, 'setLoop:', -1, 'play:', 10, 'setVol:', 10)
				whiteKnight._send(
					'signal:', 18432,
					'view:', 4900,
					'cel:', 0,
					'setLoop:', 0,
					'addToPic:'
				)
				redKnight._send('signal:', 18432, 'view:', 4900, 'setLoop:', 0, 'cel:', 1, 'addToPic:')
				kernel.UnLoad(128, 492)
				kernel.UnLoad(128, 493)
				cycles = 2
			#end:case
			case 1:
				global0._send('setHeading:', 0, self)
			#end:case
			case 2:
				global103._send('fade:', 127, 10, 5, 0)
				global0._send('normal:', 0, 'view:', 4900, 'cel:', 2, 'setCycle:', 0, 'setLoop:', 0)
				cycles = 2
			#end:case
			case 3:
				self._send('setScript:', miniQueenPolka, self)
			#end:case
			case 4:
				seconds = 3
			#end:case
			case 5:
				self._send('setScript:', queensJumpUp, self)
			#end:case
			case 6:
				redQueen._send('stopUpd:')
				whiteQueen._send('stopUpd:')
				cycles = 2
			#end:case
			case 7:
				global2._send('drawPic:', 490, (15 if global169 else 100))
				whiteKnight._send(
					'signal:', 18432,
					'view:', 4901,
					'setLoop:', 0,
					'cel:', 0,
					'init:',
					'setCycle:', End, self
				)
				redKnight._send(
					'signal:', 18432,
					'view:', 4901,
					'setLoop:', 1,
					'cel:', 0,
					'init:',
					'setCycle:', End, self
				)
			#end:case
			case 8:#end:case
			case 9:
				whiteKnight._send('view:', 4900, 'setLoop:', 2, 'cel:', 0, 'addToPic:')
				redKnight._send('view:', 4900, 'setLoop:', 2, 'cel:', 1, 'addToPic:')
				kernel.UnLoad(128, 492)
				kernel.UnLoad(128, 493)
				cycles = 2
			#end:case
			case 10:
				redQueen._send('view:', 495, 'setLoop:', 1, 'cel:', 0, 'setCycle:', End, self)
				whiteQueen._send('view:', 497, 'setLoop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 11:#end:case
			case 12:
				redQueen._send('view:', 494, 'setLoop:', 0, 'cel:', 1)
				whiteQueen._send('view:', 496, 'setLoop:', 0, 'cel:', 0)
				ticks = 12
			#end:case
			case 13:
				global2._send('drawPic:', 490, (15 if global169 else 100))
				whiteKnight._send(
					'signal:', 18432,
					'view:', 4901,
					'setLoop:', 0,
					'cel:', 3,
					'init:',
					'setCycle:', Beg, self
				)
				redKnight._send(
					'signal:', 18432,
					'view:', 4901,
					'setLoop:', 1,
					'cel:', 3,
					'init:',
					'setCycle:', Beg, self
				)
				kernel.UnLoad(128, 492)
				kernel.UnLoad(128, 493)
			#end:case
			case 14:#end:case
			case 15:
				whiteKnight._send('view:', 4900, 'setLoop:', 1, 'cel:', 0, 'addToPic:')
				redKnight._send('view:', 4900, 'setLoop:', 1, 'cel:', 1, 'addToPic:')
				kernel.UnLoad(128, 492)
				kernel.UnLoad(128, 493)
				cycles = 2
			#end:case
			case 16:
				if (proc913_0(39) and global0._send('has:', 6)):
					global2._send('setScript:', coalQueenTalk)
				else:
					global2._send('setScript:', firstQueenTalk)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class firstQueenTalk(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				proc913_1(59)
				myConv._send(
					'add:', -1, 1, 0, 2, 1,
					'add:', -1, 1, 0, 2, 2,
					'add:', -1, 1, 0, 2, 3,
					'add:', -1, 1, 0, 2, 4,
					'add:', -1, 1, 0, 2, 5,
					'add:', -1, 1, 0, 2, 6,
					'init:', self
				)
			#end:case
			case 1:
				seconds = 2
			#end:case
			case 2:
				proc913_2(59)
				redQueen._send('view:', 495, 'setLoop:', 2, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 3:
				redQueen._send('view:', 495, 'setLoop:', 1, 'cel:', 3, 'setCycle:', Beg, self)
				whiteQueen._send('view:', 497, 'setLoop:', 1, 'cel:', 3, 'setCycle:', Beg, self)
			#end:case
			case 4:#end:case
			case 5:
				redQueen._send('view:', 494, 'setLoop:', 0, 'cel:', 2)
				whiteQueen._send('view:', 496, 'setLoop:', 0, 'cel:', 2)
				ticks = 30
			#end:case
			case 6:
				myConv._send('add:', -1, 1, 0, 2, 7, 'add:', -1, 1, 0, 2, 8, 'init:', self)
			#end:case
			case 7:
				proc913_1(59)
				redQueen._send('view:', 495, 'setLoop:', 1, 'cel:', 0, 'setCycle:', End, self)
				if (not global105._send('handle:')):
					global105._send('number:', 493, 'setLoop:', 1, 'play:')
				#endif
			#end:case
			case 8:
				global91._send('say:', 1, 0, 2, 9, self)
			#end:case
			case 9:
				redQueen._send('cel:', 3, 'setCycle:', Beg, self)
			#end:case
			case 10:
				ticks = 30
			#end:case
			case 11:
				redQueen._send('view:', 494, 'setLoop:', 0, 'cel:', 2)
				ticks = 30
			#end:case
			case 12:
				global0._send(
					'view:', 491,
					'normal:', 0,
					'setLoop:', 2,
					'cel:', 0,
					'cycleSpeed:', 0,
					'setCycle:', CT, 4, 1, self
				)
			#end:case
			case 13:
				proc913_2(59)
				global91._send('say:', 1, 0, 2, 10, self)
			#end:case
			case 14:
				global0._send('view:', 4900, 'setLoop:', 0, 'cel:', 2)
				cycles = 3
			#end:case
			case 15:
				myConv._send('add:', -1, 1, 0, 2, 11, 'add:', -1, 1, 0, 2, 12, 'init:', self)
			#end:case
			case 16:
				redQueen._send('view:', 495, 'setLoop:', 1, 'cel:', 0, 'setCycle:', End, self)
				whiteQueen._send('view:', 497, 'setLoop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 17:#end:case
			case 18:
				proc913_1(59)
				redQueen._send('view:', 494, 'setLoop:', 0, 'cel:', 1)
				whiteQueen._send('view:', 496, 'setLoop:', 0, 'cel:', 0)
				ticks = 30
			#end:case
			case 19:
				myConv._send('add:', -1, 1, 0, 2, 13, 'add:', -1, 1, 0, 2, 14, 'init:', self)
			#end:case
			case 20:
				proc913_1(39)
				local50 = 1
				global2._send('setScript:', queensLeave, 0, 1)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class coalQueenTalk(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				proc913_1(59)
				if proc913_0(89):
					myConv._send(
						'add:', -1, 1, 0, 4, 1,
						'add:', -1, 1, 0, 4, 2,
						'add:', -1, 1, 0, 4, 3,
						'add:', -1, 1, 0, 4, 4,
						'add:', -1, 1, 0, 4, 5,
						'add:', -1, 1, 0, 4, 6,
						'init:', self
					)
				else:
					myConv._send(
						'add:', -1, 1, 0, 3, 1,
						'add:', -1, 1, 0, 3, 2,
						'add:', -1, 1, 0, 3, 3,
						'add:', -1, 1, 0, 3, 4,
						'add:', -1, 1, 0, 3, 5,
						'add:', -1, 1, 0, 3, 6,
						'add:', -1, 1, 0, 3, 7,
						'init:', self
					)
				#endif
			#end:case
			case 1:
				redQueen._send('view:', 4951, 'setLoop:', 1, 'cel:', 3, 'setCycle:', Beg, self)
				whiteQueen._send('view:', 497, 'setLoop:', 1, 'cel:', 3, 'setCycle:', Beg, self)
				kernel.UnLoad(128, 494)
				kernel.UnLoad(128, 496)
			#end:case
			case 2:#end:case
			case 3:
				redQueen._send('view:', 4951, 'setLoop:', 0, 'cel:', 0)
				whiteQueen._send('view:', 496, 'setLoop:', 0, 'cel:', 2)
				kernel.UnLoad(128, 497)
				cycles = 4
			#end:case
			case 4:
				proc913_2(59)
				if proc913_0(89):
					global91._send('say:', 1, 0, 4, 7, self)
				else:
					proc913_1(89)
					global91._send('say:', 1, 0, 3, 8, self)
				#endif
			#end:case
			case 5:
				global1._send('handsOn:')
				global0._send('reset:', 3)
				local3 = 0
				local52 = 1
				roomTimer._send('setReal:', global2, 15)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getScarf(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('illegalBits:', 0, 'setMotion:', PolyPath, 163, 136, self)
			#end:case
			case 1:
				global0._send('loop:', 6)
				ticks = 12
			#end:case
			case 2:
				global91._send('say:', 4, 5, 0, 1, self)
			#end:case
			case 3:
				global0._send(
					'view:', 491,
					'normal:', 0,
					'loop:', 4,
					'cel:', 0,
					'posn:', 172, 140,
					'cycleSpeed:', 10,
					'setCycle:', CT, 3, 1, self
				)
			#end:case
			case 4:
				global1._send('givePoints:', 1)
				redScarf._send('dispose:')
				global0._send('setCycle:', End, self)
			#end:case
			case 5:
				global0._send(
					'reset:', 6,
					'get:', 41,
					'posn:', 163, 136,
					'setMotion:', PolyPath, 150, 170, self
				)
			#end:case
			case 6:
				global1._send('handsOn:')
				global0._send('setHeading:', 180)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoEnters(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send(
					'posn:', 160, 255,
					'setScale:', Scaler, 100, 99, 190, 0,
					'init:',
					'reset:',
					'setMotion:', MoveTo, 144, 183, self
				)
			#end:case
			case 1:
				if (proc913_0(39) and global0._send('has:', 6)):
					cycles = 2
				else:
					global1._send('handsOn:')
					self._send('dispose:')
				#endif
			#end:case
			case 2:
				if (global102._send('prevSignal:') == 10):
					global102._send('prevSignal:', 0)
					global69._send('disable:', 6)
					global2._send('setScript:', queensEnter)
					self._send('dispose:')
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
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global102._send('fade:')
				global103._send('fade:')
				global0._send('setMotion:', MoveTo, global0._send('x:'), 255, self)
			#end:case
			case 1:
				global2._send('newRoom:', 480)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class queensJumpUp(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if global0._send('has:', 6):
					redQueen._send(
						'view:', 4952,
						'setLoop:', 0,
						'cel:', 0,
						'setPri:', 7,
						'posn:', 177, 148,
						'setCycle:', End
					)
				else:
					redQueen._send(
						'view:', 494,
						'setLoop:', 1,
						'cel:', 0,
						'setPri:', 7,
						'posn:', 177, 148,
						'setCycle:', End
					)
				#endif
				whiteQueen._send(
					'view:', 496,
					'setLoop:', 1,
					'cel:', 0,
					'setPri:', 7,
					'posn:', 143, 148,
					'setCycle:', End, self
				)
			#end:case
			case 1:
				redQueen._send('posn:', 177, 138, 'cel:', 0, 'setCycle:', End, self)
				whiteQueen._send('posn:', 143, 138, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 2:#end:case
			case 3:
				redQueen._send('posn:', 177, 116, 'cel:', 0, 'setCycle:', End, self)
				whiteQueen._send('posn:', 143, 116, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 4:#end:case
			case 5:
				redQueen._send('posn:', 177, 116, 'cel:', 0, 'setPri:', 9, 'setCycle:', End, self)
				whiteQueen._send('posn:', 143, 116, 'cel:', 0, 'setPri:', 9, 'setCycle:', End, self)
			#end:case
			case 6:#end:case
			case 7:
				if global0._send('has:', 6):
					redQueen._send('view:', 4951, 'setLoop:', 0, 'cel:', 0, 'posn:', 177, 124)
				else:
					redQueen._send('view:', 494, 'setLoop:', 0, 'cel:', 2, 'posn:', 177, 124)
				#endif
				whiteQueen._send('posn:', 143, 124, 'setLoop:', 0, 'cel:', 2)
				seconds = 2
			#end:case
			case 8:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class miniQueenSplit(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				whiteQueen._send('setLoop:', 4, 'setPri:', 7, 'posn:', 186, 112, 'show:')
				redQueen._send('setLoop:', 5, 'setPri:', 7, 'posn:', 197, 110, 'show:')
				ticks = 8
			#end:case
			case 1:
				whiteQueen._send('posn:', 186, 113)
				redQueen._send('posn:', 197, 111)
				ticks = 8
			#end:case
			case 2:
				whiteQueen._send('posn:', 185, 108)
				redQueen._send('posn:', 196, 107)
				ticks = 8
			#end:case
			case 3:
				whiteQueen._send('posn:', 184, 110)
				redQueen._send('posn:', 194, 108)
				ticks = 8
			#end:case
			case 4:
				whiteQueen._send('posn:', 183, 105)
				redQueen._send('posn:', 193, 105)
				ticks = 8
			#end:case
			case 5:
				whiteQueen._send('posn:', 182, 106)
				redQueen._send('posn:', 191, 106)
				ticks = 8
			#end:case
			case 6:
				whiteQueen._send('posn:', 181, 102)
				redQueen._send('posn:', 189, 102)
				ticks = 8
			#end:case
			case 7:
				whiteQueen._send('posn:', 179, 103)
				redQueen._send('posn:', 186, 103)
				ticks = 8
			#end:case
			case 8:
				whiteQueen._send('posn:', 178, 99)
				redQueen._send('posn:', 184, 99)
				ticks = 8
			#end:case
			case 9:
				whiteQueen._send('posn:', 176, 100)
				redQueen._send('posn:', 182, 100)
				ticks = 8
			#end:case
			case 10:
				whiteQueen._send('posn:', 174, 96)
				redQueen._send('posn:', 178, 96)
				ticks = 8
			#end:case
			case 11:
				whiteQueen._send('posn:', 172, 97)
				redQueen._send('posn:', 176, 97)
				ticks = 8
			#end:case
			case 12:
				whiteQueen._send('posn:', 168, 93)
				redQueen._send('posn:', 172, 93)
				ticks = 8
			#end:case
			case 13:
				whiteQueen._send('posn:', 168, 94)
				redQueen._send('posn:', 170, 94)
				ticks = 8
			#end:case
			case 14:
				whiteQueen._send('posn:', 164, 91)
				redQueen._send('posn:', 166, 91)
				ticks = 8
			#end:case
			case 15:
				whiteQueen._send('posn:', 161, 91)
				redQueen._send('posn:', 163, 91)
				ticks = 8
			#end:case
			case 16:
				whiteQueen._send('posn:', 158, 88)
				redQueen._send('posn:', 160, 88)
				ticks = 8
			#end:case
			case 17:
				whiteQueen._send('setPri:', 5, 'posn:', 154, 93)
				redQueen._send('setPri:', 5, 'posn:', 156, 93)
				ticks = 8
			#end:case
			case 18:
				whiteQueen._send('posn:', 154, 92)
				redQueen._send('posn:', 156, 92)
				ticks = 8
			#end:case
			case 19:
				whiteQueen._send('posn:', 154, 95)
				redQueen._send('posn:', 156, 95)
				ticks = 8
			#end:case
			case 20:
				whiteQueen._send('dispose:')
				redQueen._send('dispose:')
				global69._send('enable:', 6)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class hopOut(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				redQueen._send(
					'view:', 494,
					'setLoop:', 3,
					'cel:', 0,
					'posn:', 176, 124,
					'cycleSpeed:', 10,
					'setCycle:', End
				)
				whiteQueen._send(
					'view:', 496,
					'setLoop:', 3,
					'cel:', 0,
					'posn:', 143, 124,
					'cycleSpeed:', 10,
					'setCycle:', End, self
				)
			#end:case
			case 1:
				if local50:
					local50 = 0
					redScarf._send('init:')
				#endif
				redQueen._send('setLoop:', 2, 'cel:', 0, 'posn:', 176, 124)
				whiteQueen._send('setLoop:', 2, 'cel:', 0, 'posn:', 143, 124)
				ticks = 8
			#end:case
			case 2:
				redQueen._send('cel:', 1, 'posn:', 176, 124)
				whiteQueen._send('cel:', 1, 'posn:', 143, 124)
				ticks = 8
			#end:case
			case 3:
				redQueen._send('cel:', 2, 'posn:', 176, 122)
				whiteQueen._send('cel:', 2, 'posn:', 143, 122)
				ticks = 8
			#end:case
			case 4:
				redQueen._send('cel:', 3, 'posn:', 176, 120)
				whiteQueen._send('cel:', 3, 'posn:', 143, 120)
				ticks = 8
			#end:case
			case 5:
				redQueen._send('cel:', 4, 'posn:', 176, 119)
				whiteQueen._send('cel:', 4, 'posn:', 143, 119)
				ticks = 8
			#end:case
			case 6:
				redQueen._send('cel:', 5, 'posn:', 176, 118)
				whiteQueen._send('cel:', 5, 'posn:', 143, 118)
				ticks = 8
			#end:case
			case 7:
				redQueen._send('cel:', 0)
				whiteQueen._send('cel:', 0)
				ticks = 8
			#end:case
			case 8:
				redQueen._send('cel:', 1)
				whiteQueen._send('cel:', 1)
				ticks = 8
			#end:case
			case 9:
				redQueen._send('cel:', 2, 'posn:', 176, 116)
				whiteQueen._send('cel:', 2, 'posn:', 143, 116)
				ticks = 8
			#end:case
			case 10:
				redQueen._send('cel:', 3, 'posn:', 176, 114, 'setPri:', 7)
				whiteQueen._send('cel:', 3, 'posn:', 143, 114, 'setPri:', 7)
				ticks = 8
			#end:case
			case 11:
				redQueen._send('cel:', 4, 'posn:', 176, 118)
				whiteQueen._send('cel:', 4, 'posn:', 143, 118)
				ticks = 8
			#end:case
			case 12:
				redQueen._send('cel:', 5, 'posn:', 176, 120)
				whiteQueen._send('cel:', 5, 'posn:', 143, 120)
				ticks = 8
			#end:case
			case 13:
				redQueen._send('cel:', 0, 'posn:', 176, 124)
				whiteQueen._send('cel:', 0, 'posn:', 143, 124)
				ticks = 8
			#end:case
			case 14:
				redQueen._send('cel:', 1, 'posn:', 176, 125)
				whiteQueen._send('cel:', 1, 'posn:', 143, 125)
				ticks = 8
			#end:case
			case 15:
				redQueen._send('cel:', 2, 'posn:', 176, 130)
				whiteQueen._send('cel:', 2, 'posn:', 143, 130)
				ticks = 8
			#end:case
			case 16:
				redQueen._send('cel:', 3, 'posn:', 176, 134)
				whiteQueen._send('cel:', 3, 'posn:', 143, 134)
				ticks = 8
			#end:case
			case 17:
				redQueen._send('cel:', 4, 'posn:', 176, 138)
				whiteQueen._send('cel:', 4, 'posn:', 143, 138)
				ticks = 8
			#end:case
			case 18:
				redQueen._send('cel:', 5, 'posn:', 176, 130)
				whiteQueen._send('cel:', 5, 'posn:', 143, 130)
				ticks = 8
			#end:case
			case 19:
				redQueen._send('cel:', 0, 'posn:', 176, 145)
				whiteQueen._send('cel:', 0, 'posn:', 143, 145)
				ticks = 8
			#end:case
			case 20:
				redQueen._send('cel:', 1, 'posn:', 176, 148)
				whiteQueen._send('cel:', 1, 'posn:', 143, 148)
				ticks = 8
			#end:case
			case 21:
				redQueen._send('cel:', 2, 'posn:', 176, 148)
				whiteQueen._send('cel:', 2, 'posn:', 143, 148)
				ticks = 8
			#end:case
			case 22:
				redQueen._send('cel:', 3, 'posn:', 176, 152)
				whiteQueen._send('cel:', 3, 'posn:', 143, 152)
				ticks = 8
			#end:case
			case 23:
				redQueen._send('cel:', 4, 'posn:', 176, 157)
				whiteQueen._send('cel:', 4, 'posn:', 143, 157)
				ticks = 8
			#end:case
			case 24:
				redQueen._send('cel:', 0, 'posn:', 176, 150)
				whiteQueen._send('cel:', 0, 'posn:', 143, 150)
				ticks = 8
			#end:case
			case 25:
				redQueen._send('hide:')
				whiteQueen._send('hide:')
				ticks = 8
			#end:case
			case 26:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class knightBoundForward(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				register = 0
				global2._send('drawPic:', 490, (15 if global169 else 100))
				redKnight._send(
					'signal:', 18432,
					'view:', 493,
					'cel:', 0,
					'setLoop:', 2,
					'init:',
					'setCycle:', End, self
				)
				whiteKnight._send(
					'signal:', 18432,
					'view:', 492,
					'cel:', 0,
					'setLoop:', 2,
					'init:',
					'setCycle:', End, self
				)
			#end:case
			case 1:#end:case
			case 2:
				seconds = 2
			#end:case
			case 3:
				hoofSound._send('number:', 492, 'setLoop:', 1, 'play:')
				redKnight._send('view:', 493, 'cel:', 0, 'setLoop:', 1)
				whiteKnight._send('view:', 492, 'cel:', 0, 'setLoop:', 1)
				cycles = 3
			#end:case
			case 4:
				redKnight._send('cel:', register, 'posn:', local34[register], 124)
				whiteKnight._send('cel:', register, 'posn:', local41[register], 124)
				if (register.post('++') <= 6):
					state.post('--')
				#endif
				ticks = 10
			#end:case
			case 5:
				redKnight._send('setLoop:', 0, 'cel:', 2, 'stopUpd:')
				whiteKnight._send('setLoop:', 0, 'cel:', 2, 'stopUpd:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class knightBoundBack(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				register = 6
				global2._send('drawPic:', 490, (15 if global169 else 100))
				redKnight._send('signal:', 18432, 'view:', 493, 'setLoop:', 1, 'init:')
				whiteKnight._send('signal:', 18432, 'view:', 492, 'setLoop:', 1, 'init:')
				cycles = 2
			#end:case
			case 1:
				redKnight._send('cel:', register, 'posn:', local34[register], 124)
				whiteKnight._send('cel:', register, 'posn:', local41[register], 124)
				if (register.post('--') >= 0):
					state.post('--')
				#endif
				ticks = 10
			#end:case
			case 2:
				global0._send('setMotion:', MoveTo, global0._send('x:'), 160, self)
			#end:case
			case 3:
				whiteKnight._send('view:', 4900, 'setLoop:', 0, 'cel:', 0, 'addToPic:')
				redKnight._send('view:', 4900, 'setLoop:', 0, 'cel:', 1, 'addToPic:')
				kernel.UnLoad(128, 492)
				kernel.UnLoad(128, 493)
				cycles = 2
			#end:case
			case 4:
				if (not proc913_0(39)):
					global69._send('disable:', 6)
					global2._send('setScript:', queensEnter)
				else:
					global1._send('handsOn:')
				#endif
				self._send('dispose:')
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
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				whiteQueen._send('view:', 496, 'setLoop:', 4, 'setPri:', 5, 'posn:', 154, 93, 'init:')
				redQueen._send('view:', 494, 'setLoop:', 5, 'setPri:', 5, 'posn:', 156, 93, 'init:')
				ticks = 8
			#end:case
			case 1:
				whiteQueen._send('posn:', 158, 88)
				redQueen._send('posn:', 160, 88)
				ticks = 8
			#end:case
			case 2:
				whiteQueen._send('setPri:', 7, 'posn:', 161, 91)
				redQueen._send('setPri:', 7, 'posn:', 163, 91)
				ticks = 8
			#end:case
			case 3:
				whiteQueen._send('posn:', 164, 91)
				redQueen._send('posn:', 166, 91)
				ticks = 8
			#end:case
			case 4:
				whiteQueen._send('posn:', 168, 94)
				redQueen._send('posn:', 170, 94)
				ticks = 8
			#end:case
			case 5:
				whiteQueen._send('posn:', 168, 93)
				redQueen._send('posn:', 172, 93)
				ticks = 8
			#end:case
			case 6:
				whiteQueen._send('posn:', 172, 97)
				redQueen._send('posn:', 176, 97)
				ticks = 8
			#end:case
			case 7:
				whiteQueen._send('posn:', 174, 96)
				redQueen._send('posn:', 178, 96)
				ticks = 8
			#end:case
			case 8:
				whiteQueen._send('posn:', 176, 100)
				redQueen._send('posn:', 182, 100)
				ticks = 8
			#end:case
			case 9:
				whiteQueen._send('posn:', 178, 99)
				redQueen._send('posn:', 184, 99)
				ticks = 8
			#end:case
			case 10:
				whiteQueen._send('posn:', 179, 103)
				redQueen._send('posn:', 186, 103)
				ticks = 8
			#end:case
			case 11:
				whiteQueen._send('posn:', 181, 102)
				redQueen._send('posn:', 189, 102)
				ticks = 8
			#end:case
			case 12:
				whiteQueen._send('posn:', 182, 106)
				redQueen._send('posn:', 191, 106)
				ticks = 8
			#end:case
			case 13:
				whiteQueen._send('posn:', 183, 105)
				redQueen._send('posn:', 193, 105)
				ticks = 8
			#end:case
			case 14:
				whiteQueen._send('posn:', 184, 110)
				redQueen._send('posn:', 194, 108)
				ticks = 8
			#end:case
			case 15:
				whiteQueen._send('posn:', 185, 108)
				redQueen._send('posn:', 196, 107)
				ticks = 8
			#end:case
			case 16:
				whiteQueen._send('posn:', 186, 113)
				redQueen._send('posn:', 197, 111)
				ticks = 8
			#end:case
			case 17:
				whiteQueen._send('posn:', 186, 112)
				redQueen._send('posn:', 197, 110)
				ticks = 8
			#end:case
			case 18:
				whiteQueen._send('posn:', 186, 118)
				redQueen._send('posn:', 197, 118)
				ticks = 8
			#end:case
			case 19:
				self._send('dispose:')
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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc913_0(59):
			(cond
				case ((redQueen._send('loop:') == 0) and (redQueen._send('view:') == 494)):
					self._send('view:', 495, 'loop:', 4, 'x:', 173, 'y:', 82, 'textX:', -89, 'textY:', -72)
					super._send('init:', 0, 0, tRMouth2, &rest)
				#end:case
				case 
					(and
						(redQueen._send('cel:') == 3)
						(redQueen._send('loop:') == 1)
						(redQueen._send('view:') == 495)
					):
					self._send('view:', 495, 'loop:', 4, 'x:', 171, 'y:', 82, 'textX:', -89, 'textY:', -72)
					super._send('init:', 0, 0, tRMouth2, &rest)
				#end:case
				else:
					self._send(
						'view:', 890,
						'loop:', 0,
						'cel:', 1,
						'x:', 309,
						'y:', 5,
						'textX:', -223,
						'textY:', 6
					)
					super._send('init:', 0, 0, 0, &rest)
				#end:else
			)
		else:
			self._send('view:', 495, 'loop:', 3, 'x:', 174, 'y:', 80, 'textX:', -89, 'textY:', -72)
			super._send('init:', 0, 0, tRMouth, &rest)
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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc913_0(59):
			if 
				(and
					(not whiteQueen._send('cel:'))
					(not whiteQueen._send('loop:'))
					(whiteQueen._send('view:') == 496)
				)
				self._send('view:', 497, 'setLoop:', 4, 'x:', 146, 'y:', 82, 'textX:', -127, 'textY:', -73)
				super._send('init:', 0, 0, tWMouth2, &rest)
			else:
				self._send('view:', 890, 'setLoop:', 0, 'cel:', 1, 'x:', 5, 'y:', 5, 'textX:', 10, 'textY:', 6)
				super._send('init:', 0, 0, 0, &rest)
			#endif
		else:
			self._send('view:', 497, 'loop:', 3, 'x:', 135, 'y:', 76, 'textX:', -127, 'textY:', -63)
			super._send('init:', 0, 0, tWMouth, &rest)
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
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				local3 = 99
				global0._send('put:', 6, 490)
				global0._send('illegalBits:', 0, 'setMotion:', MoveTo, 176, 136, self)
			#end:case
			case 1:
				global0._send('setHeading:', 335, self)
			#end:case
			case 2:
				global0._send('view:', 491, 'loop:', 3, 'cel:', 0, 'normal:', 0, 'cycleSpeed:', 10)
				cycles = 4
			#end:case
			case 3:
				global0._send('setCycle:', CT, 4, 1, self)
				whiteQueen._send('view:', 497, 'setLoop:', 0, 'cel:', 0, 'setCycle:', CT, 3, 1)
			#end:case
			case 4:
				global1._send('givePoints:', 1)
				global91._send('say:', 6, 46, 0, 1, self)
			#end:case
			case 5:
				global0._send('setCycle:', End, self)
			#end:case
			case 6:
				global0._send('reset:', 7)
				whiteQueen._send('setCycle:', Beg, self)
			#end:case
			case 7:
				global91._send('say:', 6, 46, 0, 2, self)
			#end:case
			case 8:
				whiteQueen._send('view:', 497, 'setLoop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 9:
				proc913_1(59)
				whiteQueen._send('view:', 496, 'setLoop:', 0, 'cel:', 0)
				cycles = 4
			#end:case
			case 10:
				global91._send('say:', 6, 46, 0, 3, self)
			#end:case
			case 11:
				redQueen._send('view:', 4951, 'setLoop:', 1, 'cel:', 0, 'setCycle:', End, self)
				if (not global105._send('handle:')):
					global105._send('number:', 493, 'setLoop:', 1, 'play:')
				#endif
			#end:case
			case 12:
				redQueen._send('view:', 494, 'setLoop:', 0, 'cel:', 1)
				cycles = 4
			#end:case
			case 13:
				global91._send('say:', 6, 46, 0, 4, self)
			#end:case
			case 14:
				redQueen._send('view:', 4951, 'setLoop:', 1, 'cel:', 3, 'setCycle:', Beg, self)
				whiteQueen._send('view:', 497, 'setLoop:', 1, 'cel:', 3, 'setCycle:', Beg, self)
			#end:case
			case 15:#end:case
			case 16:
				proc913_2(59)
				redQueen._send('view:', 4951, 'setLoop:', 0, 'cel:', 0)
				whiteQueen._send('view:', 497, 'setLoop:', 0, 'cel:', 0)
				cycles = 4
			#end:case
			case 17:
				global91._send('say:', 6, 46, 0, 5, self)
			#end:case
			case 18:
				global0._send(
					'view:', 491,
					'loop:', 3,
					'cel:', 0,
					'normal:', 0,
					'cycleSpeed:', 10,
					'setCycle:', CT, 4, 1, self
				)
				whiteQueen._send('view:', 497, 'setLoop:', 0, 'cel:', 0, 'setCycle:', CT, 3, 1, self)
			#end:case
			case 19:#end:case
			case 20:
				whiteQueen._send('setCycle:', Beg, self)
				global0._send('setCycle:', End, self)
			#end:case
			case 21:#end:case
			case 22:
				global0._send('reset:', 7, 'get:', 10)
				cycles = 6
			#end:case
			case 23:
				global91._send('say:', 6, 46, 0, 6, self)
			#end:case
			case 24:
				proc913_1(59)
				global2._send('setScript:', queensLeave, 0, 46)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class queensLeave(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				ticks = 8
			#end:case
			case 1:
				self._send('setScript:', hopOut, self)
			#end:case
			case 2:
				global2._send('drawPic:', 490, (15 if global169 else 100))
				redKnight._send('signal:', 18432, 'view:', 4900, 'setLoop:', 0, 'cel:', 1, 'init:')
				whiteKnight._send('signal:', 18432, 'view:', 4900, 'setLoop:', 0, 'cel:', 0, 'init:')
				ticks = 12
			#end:case
			case 3:
				match register
					case 1:
						global91._send('say:', 1, 0, 2, 15, self)
					#end:case
					case 46:
						global91._send('say:', 6, 46, 0, 7, self)
					#end:case
					else:
						self._send('cue:')
					#end:else
				#end:match
			#end:case
			case 4:
				seconds = 3
			#end:case
			case 5:
				global103._send('fade:', 40, 10, 2, 0)
				whiteQueen._send('setScript:', miniQueenSplit)
				ticks = 60
			#end:case
			case 6:
				match register
					case 1:
						global91._send('say:', 1, 0, 2, 16, self)
					#end:case
					case 46:
						myConv._send(
							'add:', -1, 6, 46, 0, 8,
							'add:', -1, 6, 46, 0, 9,
							'add:', -1, 6, 46, 0, 10,
							'add:', -1, 6, 46, 0, 11,
							'init:', self
						)
					#end:case
					else:
						self._send('cue:')
					#end:else
				#end:match
			#end:case
			case 7:
				if (register == 46):
					register = global0._send('cycleSpeed:')
					global0._send(
						'view:', 499,
						'cel:', 0,
						'normal:', 0,
						'cycleSpeed:', 8,
						'setCycle:', End, self
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
					global0._send('cycleSpeed:', register, 'setCycle:', Beg, self)
				else:
					cycles = 2
				#endif
				global103._send('fade:', 0, 15, 10, 1)
			#end:case
			case 10:
				if (global0._send('y:') < 153):
					global0._send(
						'reset:', 2,
						'setLoop:', -1,
						'setMotion:', PolyPath, 150, 170, self
					)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 11:
				global0._send('reset:', 2, 'setLoop:', -1, 'setHeading:', 180, self)
			#end:case
			case 12:
				seconds = 4
			#end:case
			case 13:
				global103._send('number:', 0, 'stop:')
				global102._send('pause:', 0)
				proc913_2(59)
				local52 = 0
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

