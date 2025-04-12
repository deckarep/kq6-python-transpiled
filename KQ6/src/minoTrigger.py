#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 441
import sci_sh
import kernel
import Main
import n913
import Print
import Conversation
import Scaler
import RandCycle
import PolyPath
import Polygon
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	proc441_0 = 0,
	proc441_1 = 1,
	proc441_2 = 2,
	minoTrigger = 3,
	minotaur = 4,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None


@SCI.procedure
def proc441_0(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	(global1 handsOff:)
	local0 = 9
	(kernel.ScriptID(30, 0) setScript: 0)
	if (not local2):
		local2 = 1
		(global2 setScript: minoTrigger 0 param1)
	#endif
#end:procedure

@SCI.procedure
def proc441_1():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	(minotaur init:)
	(celeste init:)
	local0 = 8
	local1 = 6
#end:procedure

@SCI.procedure
def proc441_2():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	(global2 setScript: stepInFurther)
#end:procedure

@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class minotaur(Actor):
	#property vars (may be empty)
	x = 114
	y = 147
	noun = 4
	yStep = 3
	view = 4445
	signal = 16384
	cycleSpeed = 18
	xStep = 5
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not (kernel.ScriptID(30, 0) seenByMino:)):
			proc441_0(0)
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 2:
				(global91 say: 4 2 local0 0 self 440)
			#end:case
			case 5:
				if (kernel.ScriptID(30, 0) seenByMino:):
					(global2 setScript: minotaurCharging 0 5)
				else:
					(global2 setScript: handToHand)
				#endif
			#end:case
			case 72:
				if ((global2 script:) == minoTrigger):
					(kernel.ScriptID(30, 0) scarfOnMino: 1)
					(global0 view: 441 normal: 0 setLoop: 0 cel: 0)
					kernel.UnLoad(128, 900)
					(minotaur cycleSpeed: 6 setCycle: Fwd)
					(minoTrigger state: 19 register: 72 cue:)
					(global1 handsOff:)
					(global1 givePoints: 3)
				else:
					(global91 say: 4 0 8 1 self 440)
				#endif
			#end:case
			case 1:
				(global91 say: 4 1 0 1 0 440)
			#end:case
			else:
				if (not (kernel.ScriptID(30, 0) seenByMino:)):
					(global91 say: 4 0 8 1 self 440)
				else:
					(global91 say: 4 0 9 1 self 440)
				#endif
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self setCycle: RandCycle)
		(super init:)
	#end:method

#end:class or instance

@SCI.instance
class celeste(Actor):
	#property vars (may be empty)
	x = 103
	y = 124
	noun = 5
	view = 4421
	cycleSpeed = 24
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self setCycle: RandCycle)
		(super init:)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not (kernel.ScriptID(30, 0) seenByMino:)):
			proc441_0(0)
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				(global91 say: 5 1 local0 1 0 440)
			#end:case
			case 2:
				(global91 say: 5 2 local0 0 self 440)
			#end:case
			case 5:
				(global91 say: 5 5 local0 1 self 440)
			#end:case
			else:
				(global91 say: 5 0 local1 1 0 440)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class stepInFurther(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(myConv add: 440 2 3 8 1 add: 440 2 3 8 2 init: self)
			#end:case
			case 1:
				proc441_0(0)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class handToHand(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(myConv add: 440 4 5 8 1 add: 440 4 5 8 2 init: self)
			#end:case
			case 1:
				proc441_0(5)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class minoTrigger(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global0 setMotion: PolyPath 111 174 self)
			#end:case
			case 1:
				(global0 setHeading: 0)
				cycles = 8
			#end:case
			case 2:
				(global91 say: 1 0 3 1 self 440)
			#end:case
			case 3:
				(kernel.ScriptID(30, 0) seenByMino: 1)
				(minotaur view: 443 setCycle: 0 setLoop: 1 cel: 0 posn: 110 148)
				kernel.UnLoad(128, 444)
				cycles = 2
			#end:case
			case 4:
				(global102 number: 441 setLoop: -1 play:)
				(global105 number: 433 setLoop: 1 play: self)
				(minotaur setLoop: 2 cel: 5 posn: 90 151)
			#end:case
			case 5:
				(myConv add: 440 1 0 3 2 add: 440 1 0 3 3 init: self)
			#end:case
			case 6:
				(global105 number: 433 setLoop: 1 play: self)
			#end:case
			case 7:
				(myConv add: 440 1 0 3 4 add: 440 1 0 3 5 init: self)
			#end:case
			case 8:
				(minotaur
					view: 443
					setLoop: 2
					setCycle: Walk
					illegalBits: 0
					cycleSpeed: 3
					setMotion: MoveTo 59 177 self
				)
				cycles = 4
			#end:case
			case 9:
				(self setScript: backup self)
			#end:case
			case 10:
				(minotaur setLoop: 0)
				cycles = 2
			#end:case
			case 11:
				(minotaur view: 4441)
				kernel.UnLoad(128, 443)
				ticks = 5
			#end:case
			case 12:#end:case
			case 13:
				(global0 setLoop: 2 setMotion: MoveTo 145 151 self)
			#end:case
			case 14:
				(global0 setHeading: 210)
				ticks = 6
			#end:case
			case 15:
				(global91 say: 1 0 3 6 self 440)
			#end:case
			case 16:
				(global0
					view: 441
					normal: 0
					setLoop: 1
					x: ((global0 x:) + 10)
					y: ((global0 y:) + 5)
					cel: 0
				)
				kernel.UnLoad(128, 900)
				ticks = 6
			#end:case
			case 17:
				(minotaur cycleSpeed: 6 setCycle: Fwd)
				ticks = 8
			#end:case
			case 18:
				if (kernel.ScriptID(30, 0) scarfOnMino:):
					(self cue:)
				else:
					(global91 say: 1 0 3 7 self 440)
				#endif
			#end:case
			case 19:
				(global1 handsOn:)
				(global69 disable: 0)
				seconds = 2
			#end:case
			case 20:
				cycles = 8
			#end:case
			case 21:
				if (kernel.ScriptID(30, 0) scarfOnMino:):
					(global91 say: 4 38 11 1 self 440)
				else:
					(self cue:)
				#endif
			#end:case
			case 22:
				(cond
					case (register == 5):
						(global91 say: 4 5 9 1 self 440)
					#end:case
					case (kernel.ScriptID(30, 0) scarfOnMino:):
						(global91 say: 4 38 11 2 self 440)
					#end:case
					else:
						(self cue:)
					#end:else
				)
			#end:case
			case 23:
				seconds = 2
			#end:case
			case 24:
				if (kernel.ScriptID(30, 0) scarfOnMino:):
					(global91 say: 4 38 11 3 self 440)
				else:
					(self cue:)
				#endif
			#end:case
			case 25:
				seconds = 2
			#end:case
			case 26:
				(global105 number: 433 setLoop: 1 play: self)
			#end:case
			case 27:
				if (kernel.ScriptID(30, 0) scarfOnMino:):
					(global91 say: 4 38 11 4 self 440)
				else:
					ticks = 8
				#endif
			#end:case
			case 28:
				(global91 say: 1 0 5 1 self 440)
			#end:case
			case 29:
				(client setScript: minotaurCharging 0 register)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class minotaurCharging(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if (global1 isHandsOn:):
					(global1 handsOff:)
				#endif
				cycles = 12
			#end:case
			case 1:
				if (kernel.ScriptID(30, 0) scarfOnMino:):
					(global0 view: 441 setLoop: 0)
					kernel.UnLoad(128, 900)
				#endif
				if (register == 5):
					(global91 say: 4 5 9 1 self 440)
				else:
					(self cue:)
				#endif
			#end:case
			case 2:
				(global105 number: 433 setLoop: 1 play:)
				(minotaur view: 4441 cel: 7 setPri: 14)
				ticks = 2
			#end:case
			case 3:
				(minotaur
					view: 4442
					cel: 1
					posn: ((minotaur x:) + 7) ((minotaur y:) - 6)
				)
				kernel.UnLoad(128, 4441)
				ticks = 2
			#end:case
			case 4:
				(minotaur cel: 2 posn: ((minotaur x:) + 19) ((minotaur y:) - 9))
				ticks = 2
			#end:case
			case 5:
				(minotaur cel: 3 posn: ((minotaur x:) + 18) ((minotaur y:) + 5))
				ticks = 2
			#end:case
			case 6:
				(minotaur cel: 4 posn: ((minotaur x:) + 8) (minotaur y:))
				ticks = 2
			#end:case
			case 7:
				(minotaur cel: 5 posn: ((minotaur x:) + 13) ((minotaur y:) - 8))
				ticks = 2
			#end:case
			case 8:
				if (kernel.ScriptID(30, 0) scarfOnMino:):
					(global0 cel: 0 setScript: 0 setCycle: End)
					(minotaur cel: 6 posn: ((minotaur x:) + 14) (minotaur y:))
					ticks = 2
				else:
					(global2 setScript: hornSwaggled 0 register)
				#endif
			#end:case
			case 9:
				(celeste setCycle: 0 stopUpd:)
				(global105 number: 433 setLoop: 1 play:)
				(minotaur
					view: 4444
					cel: 0
					cycleSpeed: 1
					posn: ((minotaur x:) + 22) ((minotaur y:) + 1)
					setCycle: End self
				)
				kernel.UnLoad(128, 4442)
				cycles = 2
			#end:case
			case 10:
				(global102 number: 442 setLoop: 1 play: self)
			#end:case
			case 11:#end:case
			case 12:
				(global0 reset: 0 posn: ((global0 x:) - 28) ((global0 y:) - 5))
				((global2 obstacles:) dispose:)
				ticks = 6
			#end:case
			case 13:
				if (kernel.ScriptID(30, 0) scarfOnMino:):
					(global91 say: 4 38 11 5 self 440)
				else:
					(self cue:)
				#endif
			#end:case
			case 14:
				(global102 number: 443 setLoop: -1 play:)
				(global2
					addObstacle:
						((Polygon new:)
							type: 3
							init:
								178
								157
								208
								157
								241
								151
								239
								157
								319
								157
								319
								0
								0
								0
								0
								181
								43
								181
								86
								151
								75
								151
								83
								148
								125
								145
								128
								151
								168
								147
							yourself:
						)
						((Polygon new:)
							type: 2
							init:
								0
								185
								296
								185
								265
								173
								248
								163
								319
								163
								319
								186
								0
								189
							yourself:
						)
				)
				local1 = 7
				proc913_1(1)
				(minotaur dispose:)
				(global2 setScript: freeCeleste)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class hornSwaggled(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global0
					setLoop: 1
					posn: ((global0 x:) + 10) (global0 y:)
					cycleSpeed: 0
					setCycle: CT 2 1 self
				)
				(minotaur
					view: 4443
					cel: 4
					cycleSpeed: 0
					setCycle: 0
					posn: ((minotaur x:) + 10) ((minotaur y:) + 3)
				)
				kernel.UnLoad(128, 4442)
				(global102 number: 402 setLoop: 1 play:)
			#end:case
			case 1:
				if (register == 5):
					(global91 say: 4 5 9 2 self 440)
				else:
					(global91 say: 1 0 5 2 self 440)
				#endif
			#end:case
			case 2:
				(global0 setCycle: End self)
				(minotaur setCycle: End self)
			#end:case
			case 3:#end:case
			case 4:
				if (global90 == 2):
					(global91 say: 4 5 9 3 self 440)
				else:
					(self cue:)
				#endif
			#end:case
			case 5:
				if (global90 != 2):
					(Print addText: 4 5 9 3 posn: -1 10 init:)
				#endif
				(global105 number: 442 setLoop: 1 play: self)
				(minotaur view: 443 setLoop: 0 cel: 0)
				kernel.UnLoad(128, 4443)
			#end:case
			case 6:
				if global25:
					(global25 dispose:)
				#endif
				proc0_1(25)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoTwin(Actor):
	#property vars (may be empty)
	view = 900
	signal = 16384
	illegalBits = 0
	
#end:class or instance

@SCI.instance
class backup(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global0 hide:)
				(egoTwin
					setLoop: 3
					cel: 1
					posn: 111 174
					setScale: Scaler 100 99 190 0
					init:
				)
				ticks = 8
			#end:case
			case 1:
				(egoTwin cel: 3)
				ticks = 8
			#end:case
			case 2:
				(egoTwin setLoop: 7 cel: 1 posn: 109 172)
				ticks = 8
			#end:case
			case 3:
				(egoTwin cel: 0 posn: 116 174)
				ticks = 8
			#end:case
			case 4:
				(egoTwin setLoop: 1 cel: 4 posn: 118 174)
				ticks = 8
			#end:case
			case 5:
				(egoTwin cel: 5 posn: 128 177)
				ticks = 8
			#end:case
			case 6:
				(egoTwin setLoop: 5 cel: 2 posn: 132 176)
				ticks = 8
			#end:case
			case 7:
				(egoTwin cel: 4 posn: 133 176)
				ticks = 8
			#end:case
			case 8:
				(egoTwin cel: 5 posn: 137 174)
				ticks = 8
			#end:case
			case 9:
				(egoTwin cel: 0 posn: 140 173)
				ticks = 8
			#end:case
			case 10:
				(egoTwin setLoop: 2 cel: 2 posn: 144 171)
				ticks = 8
			#end:case
			case 11:
				(global0
					setLoop: (egoTwin loop:)
					cel: (egoTwin cel:)
					x: (egoTwin x:)
					y: (egoTwin y:)
					show:
				)
				(egoTwin dispose:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class freeCeleste(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global0 setMotion: PolyPath 118 149 self)
			#end:case
			case 1:
				ticks = 4
			#end:case
			case 2:
				(myConv
					add: 440 4 38 11 6
					add: 440 4 38 11 7
					add: 440 4 38 11 8
					add: 440 4 38 11 9
					add: 440 4 38 11 10
					init: self
				)
			#end:case
			case 3:
				(global0
					view: 441
					normal: 0
					setLoop: 2
					cycleSpeed: 12
					posn: 110 150
					setCycle: End self
				)
			#end:case
			case 4:
				(global91 say: 4 38 11 11 self 440)
			#end:case
			case 5:
				(global105 number: 445 setLoop: -1 play:)
				(global0 setLoop: 3 setCycle: Fwd)
				proc913_2(161)
				seconds = 5
			#end:case
			case 6:
				(global105 stop:)
				(celeste
					view: 4421
					setLoop: 1
					cel: 0
					cycleSpeed: 6
					setCycle: CT 2 1
				)
				(global0
					posn: 119 149
					reset: 1
					get: 8
					setMotion:
						MoveTo
						((global0 x:) - 20)
						((global0 y:) + 12)
						self
				)
			#end:case
			case 7:
				(global0 setHeading: 45)
				seconds = 1
			#end:case
			case 8:
				(global0 setHeading: 90)
				(celeste setCycle: End self)
			#end:case
			case 9:
				(myConv
					add: 440 4 38 11 12
					add: 440 4 38 11 13
					add: 440 4 38 11 14
					init: self
				)
			#end:case
			case 10:
				(celeste
					view: 364
					setLoop: 2
					setCycle: Walk
					cycleSpeed: (global0 cycleSpeed:)
					moveSpeed: (global0 moveSpeed:)
					posn: (celeste x:) ((celeste y:) + 20)
					setMotion: MoveTo 105 154 self
				)
				kernel.UnLoad(128, 4421)
			#end:case
			case 11:
				(celeste setLoop: 0 setMotion: PolyPath 165 165 self)
			#end:case
			case 12:
				(celeste setMotion: PolyPath 255 160 self)
			#end:case
			case 13:
				(global102 fade: 0 6 6)
				(celeste setMotion: PolyPath 340 160 self)
				(global0 setMotion: PolyPath 300 160 self)
			#end:case
			case 14:#end:case
			case 15:
				proc913_3()
				(global0 put: 41 440)
				(global69 curIcon: (global69 at: 0))
				(global2 newRoom: 340)
			#end:case
		#end:match
	#end:method

#end:class or instance

