#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 370
import sci_sh
import Main
import AnimatePrint
import KQ6Room
import CartoonScript
import n913
import Conversation
import Scaler
import RandCycle
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm370 = 0,
)

@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class rm370(KQ6Room):
	#property vars (may be empty)
	picture = 370
	horizon = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(global72 add: self)
		(global69
			enable:
			disable: 0 1 2 3 4 5 6
			height: -100
			activateHeight: -100
		)
		(Cursor showCursor: 0)
		(global102 number: 370 setLoop: -1 play:)
		(egoLegs addToPic:)
		(lHand init: stopUpd:)
		(rHand init: stopUpd:)
		(myHead init:)
		(global0 view: 374 normal: 0 loop: 0 cel: 0 posn: 155 147 init:)
		(kingarm init: stopUpd:)
		(queenHand init:)
		(candle1 init: setCycle: Fwd)
		(candle2 init: setCycle: Fwd)
		(cond
			case ((proc913_0 1) and (not (proc913_0 3))):
				if (global90 == 2):
					(global2 setScript: savedCelesteCD)
				else:
					(global2 setScript: savedCelesteTXT)
				#endif
			#end:case
			case (global90 == 2):
				(global2 setScript: caughtAtGateCD)
			#end:case
			else:
				(global2 setScript: caughtAtGateTXT)
			#end:else
		)
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (((param1 type:) & 0x0004) and ((param1 message:) == 27)):
			(param1 message: 114)
		#endif
		return 0
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global69 height: 0 activateHeight: 0)
		(Cursor showCursor: 1)
		(global0 setScale: 0)
		(global69 enable: 6)
		(global1 setCursor: global21)
		(global72 delete: self)
		(DisposeScript 371)
		(super dispose:)
	#end:method

#end:class or instance

@SCI.instance
class AlexPrint(AnimatePrint):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		myMouth = alexHead
		x = -1
		y = 140
		(super init:)
	#end:method

#end:class or instance

@SCI.instance
class AzurePrint(AnimatePrint):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		myMouth = azureMouth
		myEyes = azureEyes
		x = 10
		y = 110
		(super init:)
	#end:method

#end:class or instance

@SCI.instance
class AerielPrint(AnimatePrint):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		myMouth = aerielMouth
		myEyes = aerielEyes
		x = 70
		y = 110
		(super init:)
	#end:method

#end:class or instance

@SCI.instance
class mouthScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(client setCycle: RandCycle)
				if (seconds = (register + 1) < 1):
					seconds = 1
				#endif
			#end:case
			case 1:
				(client dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class alexHead(Prop):
	#property vars (may be empty)
	x = 142
	y = 50
	view = 374
	loop = 4
	priority = 15
	signal = 24592
	cycleSpeed = 8
	
	@classmethod
	def init(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(myHead hide:)
		(super init:)
		(self setScript: mouthScr 0 param1)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(myHead show:)
		(super dispose:)
	#end:method

#end:class or instance

@SCI.instance
class eyeScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				seconds = (Random 2 4)
			#end:case
			case 1:
				(client show: setCycle: End self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				(client setCycle: Beg self)
			#end:case
			case 4:
				cycles = 2
			#end:case
			case 5:
				(client hide:)
				state = -1
				(self cue:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class azureMouth(Prop):
	#property vars (may be empty)
	x = 115
	y = 41
	view = 370
	loop = 4
	priority = 15
	signal = 24592
	
	@classmethod
	def init(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init:)
		(self setScript: mouthScr 0 param1)
	#end:method

#end:class or instance

@SCI.instance
class azureEyes(Prop):
	#property vars (may be empty)
	x = 108
	y = 36
	view = 370
	loop = 6
	priority = 15
	signal = 24592
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init:)
		(self hide: setScript: eyeScr)
	#end:method

#end:class or instance

@SCI.instance
class aerielMouth(Prop):
	#property vars (may be empty)
	x = 207
	y = 45
	view = 370
	loop = 5
	priority = 15
	signal = 24592
	
	@classmethod
	def init(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init:)
		(self setScript: mouthScr 0 param1)
	#end:method

#end:class or instance

@SCI.instance
class aerielEyes(Prop):
	#property vars (may be empty)
	x = 201
	y = 42
	view = 370
	loop = 7
	priority = 15
	signal = 24592
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init:)
		(self hide: setScript: eyeScr)
	#end:method

#end:class or instance

@SCI.instance
class flyer(Actor):
	#property vars (may be empty)
	view = 353
	signal = 24576
	
#end:class or instance

@SCI.instance
class caughtAtGateCD(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				seconds = 2
			#end:case
			case 1:
				(myConv
					add: -1 1 0 1 1
					add: -1 1 0 1 2
					add: -1 1 0 1 3
					add: -1 1 0 1 4
					add: -1 1 0 1 5
					add: -1 1 0 1 6
					add: -1 1 0 1 7
					add: -1 1 0 1 8
					add: -1 1 0 1 9
					add: -1 1 0 1 10
					init: self
				)
			#end:case
			case 2:
				(proc913_1 2)
				(cond
					case 
						(and
							(global0 has: 2)
							(global0 has: 18)
							(global0 has: 48)
							(global0 has: 41)
						):
						(global0 setScript: toLabyrinth)
					#end:case
					case (global90 == 2):
						(global0 setScript: toBeachCD)
					#end:case
					else:
						(global0 setScript: toBeachTXT)
					#end:else
				)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class caughtAtGateTXT(CartoonScript):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				seconds = 2
			#end:case
			case 1:
				(kingarm setLoop: 2 setCycle: End)
				(AzurePrint addText: 1 0 1 1 init:)
			#end:case
			case 2:
				(kingarm setCycle: Beg)
				cycles = 2
			#end:case
			case 3:
				(AlexPrint addText: 1 0 1 2 init:)
			#end:case
			case 4:
				cycles = 2
			#end:case
			case 5:
				(AerielPrint addText: 1 0 1 3 init:)
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				(AzurePrint addText: 1 0 1 4 init:)
			#end:case
			case 8:
				cycles = 2
			#end:case
			case 9:
				(kingarm setLoop: 1 setCycle: End)
				(AzurePrint addText: 1 0 1 5 init:)
			#end:case
			case 10:
				(kingarm setCycle: Beg)
				cycles = 2
			#end:case
			case 11:
				(queenHand cel: 1)
				(AerielPrint addText: 1 0 1 6 init:)
			#end:case
			case 12:
				(queenHand cel: 0)
				cycles = 2
			#end:case
			case 13:
				(AerielPrint addText: 1 0 1 7 init:)
			#end:case
			case 14:
				cycles = 2
			#end:case
			case 15:
				(kingarm setLoop: 2 setCycle: End)
				(AzurePrint addText: 1 0 1 8 init:)
			#end:case
			case 16:
				(kingarm setCycle: Beg)
				cycles = 2
			#end:case
			case 17:
				(AlexPrint addText: 1 0 1 9 init:)
			#end:case
			case 18:
				cycles = 2
			#end:case
			case 19:
				(kingarm setLoop: 2 setCycle: End)
				(AzurePrint addText: 1 0 1 10 init:)
			#end:case
			case 20:
				(kingarm setCycle: Beg)
				(proc913_1 2)
				(cond
					case 
						(and
							(global0 has: 2)
							(global0 has: 18)
							(global0 has: 48)
							(global0 has: 41)
						):
						(global2 setScript: toLabyrinth)
					#end:case
					case (global90 == 2):
						(global2 setScript: toBeachCD)
					#end:case
					else:
						(global2 setScript: toBeachTXT)
					#end:else
				)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class toLabyrinth(CartoonScript):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				cycles = 2
			#end:case
			case 1:
				if (global90 == 2):
					(global91 say: 1 0 2 1 self)
				else:
					(AlexPrint addText: 1 0 2 1 init:)
				#endif
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				if (global90 == 2):
					(global91 say: 1 0 2 2 self)
				else:
					(kingarm setLoop: 2 setCycle: End)
					(AzurePrint addText: 1 0 2 2 init:)
				#endif
			#end:case
			case 4:
				(global0 hide:)
				(egoLegs dispose:)
				(lHand dispose:)
				(rHand dispose:)
				(myHead dispose:)
				(kingarm dispose:)
				(queenHand dispose:)
				(candle1 dispose:)
				(candle2 dispose:)
				(global2 setScript: flyToCliff)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class toBeachCD(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
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
			#end:case
			case 1:
				(global0 hide:)
				(egoLegs dispose:)
				(lHand dispose:)
				(rHand dispose:)
				(myHead dispose:)
				(kingarm dispose:)
				(queenHand dispose:)
				(candle1 dispose:)
				(candle2 dispose:)
				(global2 setScript: flyToBeach)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class toBeachTXT(CartoonScript):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(queenHand cel: 2)
				(AerielPrint addText: 1 0 3 1 init:)
			#end:case
			case 1:
				(queenHand cel: 0)
				cycles = 2
			#end:case
			case 2:
				(kingarm setLoop: 2 setCycle: End)
				(AzurePrint addText: 1 0 3 2 init:)
			#end:case
			case 3:
				(kingarm setCycle: Beg)
				cycles = 2
			#end:case
			case 4:
				(kingarm setLoop: 1 setCycle: End)
				(AzurePrint addText: 1 0 3 3 init:)
			#end:case
			case 5:
				(kingarm setCycle: Beg)
				cycles = 2
			#end:case
			case 6:
				(AlexPrint addText: 1 0 3 4 init:)
			#end:case
			case 7:
				cycles = 2
			#end:case
			case 8:
				(queenHand cel: 2)
				(AerielPrint addText: 1 0 3 5 init:)
			#end:case
			case 9:
				cycles = 2
			#end:case
			case 10:
				(queenHand cel: 0)
				(AerielPrint addText: 1 0 3 6 init:)
			#end:case
			case 11:
				cycles = 2
			#end:case
			case 12:
				(AlexPrint addText: 1 0 3 7 init:)
			#end:case
			case 13:
				(global0 hide:)
				(egoLegs dispose:)
				(lHand dispose:)
				(rHand dispose:)
				(myHead dispose:)
				(kingarm dispose:)
				(queenHand dispose:)
				(candle1 dispose:)
				(candle2 dispose:)
				(global2 setScript: flyToBeach)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class savedCelesteCD(CartoonScript):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				seconds = 2
			#end:case
			case 1:
				(myConv
					add: -1 1 0 4 1
					add: -1 1 0 4 2
					add: -1 1 0 4 3
					add: -1 1 0 4 4
					add: -1 1 0 4 5
					add: -1 1 0 4 6
					add: -1 1 0 4 7
					init: self
				)
			#end:case
			case 2:
				(global2 setScript: flyToOracle)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class savedCelesteTXT(CartoonScript):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				seconds = 2
			#end:case
			case 1:
				(kingarm setLoop: 1 setCycle: End)
				(AzurePrint addText: 1 0 4 1 init:)
			#end:case
			case 2:
				(kingarm setCycle: Beg)
				cycles = 2
			#end:case
			case 3:
				(AzurePrint addText: 1 0 4 2 init:)
			#end:case
			case 4:
				cycles = 2
			#end:case
			case 5:
				(AzurePrint addText: 1 0 4 3 init:)
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				(kingarm setLoop: 1 setCycle: End)
				(AzurePrint addText: 1 0 4 4 init:)
			#end:case
			case 8:
				(kingarm setCycle: Beg)
				cycles = 2
			#end:case
			case 9:
				(AzurePrint addText: 1 0 4 5 init:)
			#end:case
			case 10:
				cycles = 2
			#end:case
			case 11:
				(kingarm setLoop: 1 setCycle: End)
				(AzurePrint addText: 1 0 4 6 init:)
			#end:case
			case 12:
				(kingarm setCycle: Beg)
				cycles = 2
			#end:case
			case 13:
				(AlexPrint addText: 1 0 4 7 init:)
			#end:case
			case 14:
				(global2 setScript: flyToOracle)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class flyToOracle(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 hide:)
				(egoLegs dispose:)
				(lHand dispose:)
				(rHand dispose:)
				(myHead dispose:)
				(kingarm dispose:)
				(queenHand dispose:)
				(candle1 dispose:)
				(candle2 dispose:)
				(global2 drawPic: 350 10)
				seconds = 3
			#end:case
			case 1:
				(flyer
					posn: 139 11
					setLoop: 1
					setScale: Scaler 50 49 190 0
					init:
					setCycle: Fwd
					setMotion: MoveTo 174 14 self
				)
			#end:case
			case 2:
				(flyer dispose:)
				cycles = 2
			#end:case
			case 3:
				(global2 drawPic: 98)
				seconds = 3
			#end:case
			case 4:
				(global102 fade: 0 15 15)
				(global2 newRoom: 380)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class flyToCliff(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global2 drawPic: 350 10)
				(flyer
					posn: 139 11
					setLoop: 1
					setScale: Scaler 50 49 190 0
					init:
					setCycle: Fwd
					setMotion: MoveTo 280 -15 self
				)
			#end:case
			case 1:
				(global102 fade: 0 15 15)
				(global2 newRoom: 340)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class flyToBeach(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global2 drawPic: 350 10)
				(flyer
					posn: 139 11
					setLoop: 1
					setScale: Scaler 50 49 190 0
					init:
					setCycle: Fwd
					setMotion: MoveTo 280 -15 self
				)
			#end:case
			case 1:
				(global102 fade: 0 15 15)
				(global2 newRoom: 300)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoLegs(View):
	#property vars (may be empty)
	x = 152
	y = 189
	view = 374
	loop = 1
	priority = 14
	signal = 16400
	
#end:class or instance

@SCI.instance
class lHand(View):
	#property vars (may be empty)
	x = 123
	y = 137
	view = 374
	loop = 2
	priority = 13
	signal = 16400
	
#end:class or instance

@SCI.instance
class rHand(View):
	#property vars (may be empty)
	x = 183
	y = 138
	view = 374
	loop = 3
	priority = 13
	signal = 16400
	
#end:class or instance

@SCI.instance
class myHead(View):
	#property vars (may be empty)
	x = 145
	y = 50
	view = 374
	loop = 5
	cel = 1
	priority = 15
	signal = 16400
	
#end:class or instance

@SCI.instance
class candle1(Prop):
	#property vars (may be empty)
	x = 34
	y = 68
	view = 371
	cel = 1
	signal = 16384
	
#end:class or instance

@SCI.instance
class candle2(Prop):
	#property vars (may be empty)
	x = 285
	y = 69
	view = 371
	loop = 1
	cel = 2
	signal = 16384
	
#end:class or instance

@SCI.instance
class kingarm(Actor):
	#property vars (may be empty)
	x = 103
	y = 56
	view = 370
	signal = 16384
	cycleSpeed = 20
	
#end:class or instance

@SCI.instance
class queenHand(Actor):
	#property vars (may be empty)
	x = 173
	y = 78
	view = 370
	loop = 3
	signal = 16384
	
#end:class or instance

