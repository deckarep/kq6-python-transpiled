#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 344
import sci_sh
import kernel
import Main
import rSacred
import KQ6Print
import n913
import Conversation
import Scaler
import PolyPath
import Sound
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	proc344_0 = 0,
	proc344_1 = 1,
	nightMare = 2,
	blowinIt = 3,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None


@SCI.procedure
def proc344_0():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(nightMare init:)
#end:procedure

@SCI.procedure
def proc344_1():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	if (((global9 at: 11) state:) & 0x0008):
		(nightMare setScript: catchNiteMare)
	else:
		(nightMare setScript: coldEmbers)
	#endif
#end:procedure

@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class nightMare(Actor):
	#property vars (may be empty)
	x = 265
	y = 112
	noun = 10
	view = 335
	signal = 24576
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(rSacred marePresent: 1)
		(self cycleSpeed: 10 setCycle: Fwd)
		(super init:)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if 
			(and
				((global0 distanceTo: self) < 65)
				((self loop:) == 0)
				(not (self script:))
				((global2 script:) != mareFlyAway)
			)
			(global1 handsOff:)
			(global2 setScript: mareFlyAway 0 3)
		#endif
		(super doit:)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		proc913_2(59)
		(super dispose:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		local1 = (global0 x:)
		local2 = (global0 y:)
		match param1
			case 13:
				(self setScript: reflectMare)
			#end:case
			case 28:
				(global1 handsOff:)
				(global2 setScript: 190)
			#end:case
			case 31:
				(self setScript: blowinIt)
			#end:case
			case 5:
				(self setScript: grabForMare)
			#end:case
			case 51:
				(self setScript: alasPoorYorick)
			#end:case
			case 37:
				(self setScript: giveHorseBird)
			#end:case
			case 19:
				(super doVerb: param1 &rest)
			#end:case
			case 2:
				(super doVerb: param1 &rest)
			#end:case
			case 14:
				(super doVerb: param1 &rest)
			#end:case
			case 16:
				(super doVerb: param1 &rest)
			#end:case
			case 1:
				(super doVerb: param1 &rest)
			#end:case
			case 32:
				(super doVerb: param1 &rest)
			#end:case
			case 12:
				(super doVerb: param1 &rest)
			#end:case
			case 44:
				(self setScript: offerItem 0 param1)
			#end:case
			case 20:
				(self setScript: offerItem 0 param1)
			#end:case
			case 30:
				(self setScript: offerItem 0 param1)
			#end:case
			case 47:
				(self setScript: offerItem 0 param1)
			#end:case
			case 65:
				(self setScript: offerItem 0 param1)
			#end:case
			case 67:
				(self setScript: offerItem 0 param1)
			#end:case
			case 68:
				(self setScript: offerItem 0 param1)
			#end:case
			case 33:
				(self setScript: offerItem 0 param1)
			#end:case
			case 70:
				(self setScript: offerItem 0 param1)
			#end:case
			else:
				(self setScript: offerItem 0 0)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class smoke(Prop):
	#property vars (may be empty)
	x = 210
	y = 92
	view = 336
	loop = 9
	priority = 15
	signal = 16400
	cycleSpeed = 10
	
#end:class or instance

@SCI.instance
class theSkull(View):
	#property vars (may be empty)
	x = 220
	y = 126
	view = 336
	loop = 4
	priority = 1
	signal = 16400
	
#end:class or instance

@SCI.instance
class reflectMare(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					view: 336
					setLoop: 0
					cel: 0
					normal: 0
					posn: ((global0 x:) + 14) ((global0 y:) + 7)
					setCycle: CT 1 1 self
				)
			#end:case
			case 1:
				(global91 say: 10 13 0 1 self 340)
			#end:case
			case 2:
				(global105 number: 346 setLoop: 1 play:)
				(nightMare setLoop: 0 setCycle: Beg self)
			#end:case
			case 3:
				(nightMare cel: 5)
				ticks = 6
			#end:case
			case 4:
				(nightMare cel: 0)
				ticks = 6
			#end:case
			case 5:
				(nightMare cel: 5)
				ticks = 6
			#end:case
			case 6:
				(nightMare cel: 0)
				ticks = 6
			#end:case
			case 7:
				(global91 say: 10 13 0 2 self 340)
			#end:case
			case 8:
				(client setScript: mareFlyAway 0 13)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class alasPoorYorick(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					view: 336
					setLoop: 0
					cel: 0
					normal: 0
					cycleSpeed: 6
					posn: ((global0 x:) + 14) ((global0 y:) + 7)
					setCycle: CT 1 1 self
				)
			#end:case
			case 1:
				(global91 say: 10 51 0 1 self 340)
			#end:case
			case 2:
				(global0 setLoop: 8)
				(nightMare setCycle: Beg self)
			#end:case
			case 3:
				(global105 number: 346 setLoop: 1 play:)
				(nightMare setCycle: CT 5 1)
				seconds = 4
			#end:case
			case 4:
				(nightMare setCycle: Fwd)
				(global91 say: 10 51 0 2 self 340)
			#end:case
			case 5:
				(global0 setLoop: 0 cel: 2 setCycle: Beg self)
			#end:case
			case 6:
				(global0 posn: local1 local2 reset: 6)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class giveHorseBird(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					normal: 0
					view: 883
					posn: ((global0 x:) - 5) (global0 y:)
					loop: 0
					cel: 0
					cycleSpeed: 8
					setCycle: Fwd
				)
				(birdSound number: 930 loop: -1 play:)
				seconds = 5
			#end:case
			case 1:
				(birdSound stop:)
				(global91 say: 10 37 0 1 self 340)
			#end:case
			case 2:
				(global0 loop: 2 cel: 0 setCycle: End self)
			#end:case
			case 3:
				(birdSound number: 931 loop: -1 play:)
				seconds = 7
			#end:case
			case 4:
				(birdSound stop:)
				(global91 say: 10 37 0 2 self 340)
			#end:case
			case 5:
				(global0 loop: 2 cel: (global0 lastCel:) setCycle: Beg self)
			#end:case
			case 6:
				(global0 posn: local1 local2 reset: 1)
				cycles = 6
			#end:case
			case 7:
				(global0 setHeading: 45)
				cycles = 6
			#end:case
			case 8:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not ((birdSound prevSignal:) == -1)):
			(birdSound stop:)
		#endif
		(super dispose:)
	#end:method

#end:class or instance

@SCI.instance
class offerItem(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					view: 336
					setLoop: 0
					cel: 0
					normal: 0
					posn: ((global0 x:) + 14) ((global0 y:) + 7)
					setCycle: CT 1 1 self
				)
			#end:case
			case 1:
				(global91 say: 10 register 0 1 self 340)
			#end:case
			case 2:
				(global0 setCycle: Beg self)
			#end:case
			case 3:
				(global0 posn: local1 local2 reset: 6)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class blowinIt(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91 say: 10 31 0 1 self 340)
			#end:case
			case 1:
				(nightMare setCycle: Beg)
				(self setScript: kernel.ScriptID(85, 0) self)
			#end:case
			case 2:
				(global105 number: 346 setLoop: 1 play:)
				(nightMare setCycle: CT 5 1 self)
			#end:case
			case 3:
				seconds = 5
			#end:case
			case 4:
				(global91 say: 10 31 0 2 self 340)
			#end:case
			case 5:
				(global1 handsOn:)
				(nightMare setCycle: Fwd)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class grabForMare(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91 say: 10 5 0 1 self 340)
			#end:case
			case 1:
				(global105 number: 346 setLoop: 1 play:)
				(nightMare setCycle: Beg)
				(global0
					setMotion:
						PolyPath
						((nightMare x:) - 20)
						((nightMare y:) + 20)
						self
				)
			#end:case
			case 2:
				cycles = 4
			#end:case
			case 3:
				(global1 handsOn:)
				local1 = (global0 x:)
				local2 = (global0 y:)
				(client setScript: mareFlyAway 0 5)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class mareFlyAway(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				if (register == 3):
					(myConv add: 340 3 3 19 1 add: 340 3 3 19 2 init: self)
				else:
					(self cue:)
				#endif
			#end:case
			case 1:
				(global105 number: 346 setLoop: 1 play:)
				(nightMare
					view: 335
					setLoop: 1
					cel: 0
					cycleSpeed: 12
					setPri: 8
					setCycle: End self
				)
			#end:case
			case 2:
				match register
					case 13:
						(global91 say: 10 13 0 3 self 340)
					#end:case
					case 5:
						(myConv add: 340 10 5 0 2 add: 340 10 5 0 3 init: self)
					#end:case
					case 3:
						(global91 say: 3 3 19 3 self 340)
					#end:case
					else:
						(global91 say: 10 0 0 1 self 340)
					#end:else
				#end:match
			#end:case
			case 3:
				(global103 fade: 0 20 5)
				(global0 reset: 6)
				(rSacred marePresent: 0)
				(nightMare dispose:)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class coldEmbers(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: PolyPath 193 131 self)
			#end:case
			case 1:
				(global0 setHeading: 45)
				local1 = (global0 x:)
				local2 = (global0 y:)
				cycles = 6
			#end:case
			case 2:
				(global0
					view: 336
					normal: 0
					setLoop: 0
					cel: 0
					cycleSpeed: 18
					posn: ((global0 x:) + 14) ((global0 y:) + 7)
					setCycle: Fwd
				)
				seconds = 5
			#end:case
			case 3:
				(global91 say: 1 0 4 1 self 340)
			#end:case
			case 4:
				(KQ6Print
					say: 0 1 0 4 2
					posn: 10 10
					ticks: 120
					modeless: 1
					init:
				)
				(global0 setCycle: Beg self)
			#end:case
			case 5:
				(global0 setLoop: 1 cel: 0 setCycle: End self)
			#end:case
			case 6:
				(global0 setLoop: 1 cel: 0 setCycle: End self)
			#end:case
			case 7:
				(global0 setLoop: 1 cel: 0 setCycle: End self)
			#end:case
			case 8:
				(global0 setLoop: 7 cel: 0 setCycle: End self)
			#end:case
			case 9:
				(global0 setLoop: 8)
				seconds = 1
			#end:case
			case 10:
				(nightMare setCycle: Beg self)
				(global105 number: 346 setLoop: 1 play:)
			#end:case
			case 11:
				if global25:
					(global25 dispose:)
				#endif
				(global91 say: 1 0 30 1 self 340)
			#end:case
			case 12:
				(nightMare setCycle: Fwd)
				seconds = 3
			#end:case
			case 13:
				(global91 say: 1 0 30 2 self 340)
			#end:case
			case 14:
				(global0 posn: local1 local2 reset: 6)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class catchNiteMare(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 put: 11 340)
				(global1 handsOff:)
				(global69 disable: 6)
				(global0 setMotion: PolyPath 193 131 self)
			#end:case
			case 1:
				(global0 setHeading: 45)
				cycles = 6
			#end:case
			case 2:
				(global0
					view: 336
					normal: 0
					setLoop: 0
					cel: 0
					cycleSpeed: 6
					posn: ((global0 x:) + 14) ((global0 y:) + 7)
					setCycle: Fwd
				)
				seconds = 5
			#end:case
			case 3:
				(global91 say: 1 0 4 1 self 340)
			#end:case
			case 4:
				(KQ6Print
					say: 0 1 0 4 2
					posn: 10 10
					ticks: 120
					modeless: 1
					init:
				)
				(global0 setCycle: Beg self)
			#end:case
			case 5:
				(global0 setLoop: 1 cel: 0 cycleSpeed: 8 setCycle: Fwd)
				seconds = 12
			#end:case
			case 6:
				(global0 setCycle: End self)
			#end:case
			case 7:
				(global0 cel: 0)
				cycles = 4
			#end:case
			case 8:
				(global0 setLoop: 7 cel: 0)
				cycles = 6
			#end:case
			case 9:
				(global0 cel: 1)
				cycles = 6
			#end:case
			case 10:
				(global0 setLoop: 8)
				seconds = 1
			#end:case
			case 11:
				(smoke init: setCycle: End self)
			#end:case
			case 12:
				(global105 number: 346 setLoop: 1 play:)
				(nightMare setCycle: Beg)
				(smoke setLoop: 10 cel: 0 setCycle: Fwd)
				seconds = 5
			#end:case
			case 13:
				if global25:
					(global25 dispose:)
				#endif
				(global91 say: 1 0 4 3 self 340)
			#end:case
			case 14:
				(global0 view: 336 setLoop: 2 setCycle: End self)
				(smoke setLoop: 9 cel: 10 setCycle: Beg)
				(nightMare
					view: 337
					loop: 0
					cel: 0
					posn: 265 112
					setCycle: End self
				)
			#end:case
			case 15:
				(smoke dispose:)
			#end:case
			case 16:
				(global91 say: 1 0 4 4 self 340)
			#end:case
			case 17:
				(theSkull init: setPri: 1 stopUpd:)
				(global0 put: 11 340)
				(global69 curIcon: (global69 at: 0))
				(global0
					posn: ((global0 x:) - 14) ((global0 y:) - 7)
					ignoreActors:
					reset: 6
					setPri: 9
				)
				(nightMare
					setScale: Scaler 100 80 134 112
					posn: ((nightMare x:) - 5) ((nightMare y:) - 3)
					setLoop: 1
					setPri: 10
					setCycle: Walk
					illegalBits: 0
					setMotion: MoveTo 220 134 self
				)
			#end:case
			case 18:
				(global91 say: 1 0 4 5 self 340)
			#end:case
			case 19:
				(nightMare
					setScale: 0
					view: 336
					setLoop: 5
					cel: 0
					posn: 216 135
					setCycle: End
				)
				(global0 setMotion: PolyPath 167 122 self)
			#end:case
			case 20:
				(global0 setHeading: 135)
				cycles = 8
			#end:case
			case 21:
				(nightMare hide:)
				(global0
					view: 336
					normal: 0
					posn: 216 135
					setLoop: 3
					cel: 0
					cycleSpeed: 12
					setCycle: End self
				)
			#end:case
			case 22:
				(nightMare show: view: 335 setLoop: 1 cel: 0 posn: 216 135)
				(global0
					setScale: 0
					view: 336
					normal: 0
					setLoop: 6
					cel: 0
					setPri: ((nightMare priority:) + 1)
					posn: ((nightMare x:) + 35) ((nightMare y:) - 46)
				)
				(global1 givePoints: 2)
				cycles = 2
			#end:case
			case 23:
				(global91 say: 1 0 4 6 self 340)
			#end:case
			case 24:
				(global103 number: 155 setLoop: -1 play:)
				(global102 fade:)
				(global104 fade:)
				(global105 fade:)
				ticks = 4
			#end:case
			case 25:
				local0.post('++')
				(nightMare cel: ((nightMare cel:) + 1))
				(global0 cel: ((global0 cel:) + 1))
				ticks = 14
			#end:case
			case 26:
				if (local0 < 9):
					(state -= 2)
				#endif
				(self cue:)
			#end:case
			case 27:
				(global0 x: 1000)
				(nightMare cel: ((nightMare cel:) + 1))
				seconds = 2
			#end:case
			case 28:
				(global1 handsOn:)
				(global69 enable: 6)
				(global2 newRoom: 155)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class birdSound(Sound):
	#property vars (may be empty)
#end:class or instance

