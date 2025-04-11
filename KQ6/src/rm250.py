#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 250
import sci_sh
import Main
import walkEgoInScr
import KQ6Room
import n913
import Conversation
import Scaler
import PolyPath
import Polygon
import Feature
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm250 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = -1
local1
local3 = None
local4 = None


@SCI.procedure
def localproc_0():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	return ((beauty script:) == roseTendingScr)
#end:procedure

@SCI.procedure
def localproc_1():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(return
		if (localproc_0):
			(10 if (proc913_0 37) else 12)
		else:
			11
		#endif
	)
#end:procedure

@SCI.instance
class rm250(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 250
	horizon = 0
	east = 240
	south = 240
	west = 260
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global2
			addObstacle:
				((Polygon new:)
					type: 2
					init: 369 -60 369 169 319 169 65 110 0 110 0 -60
					yourself:
				)
				((Polygon new:)
					type: 0
					init: -40 125 40 125 201 189 201 229 -40 229
					yourself:
				)
				((Polygon new:)
					type: 2
					init: 0 161 84 162 103 186 176 186 176 189 0 189
					yourself:
				)
		)
		(global0 init: setScale: Scaler 100 67 153 109)
		(super init: &rest)
		if (global12 == 260):
			(proc12_1 8 116)
		else:
			(proc12_1 272 187 -50)
		#endif
		(houseDoor init:)
		(gate init:)
		(genericFeatures init:)
		(houseRoses init:)
		(palmTrees init:)
		(featureToBeIgnored init:)
		((ScriptID 10 4) onMeCheck: 8 init:)
		(leaves init:)
		if ((global1 _detailLevel:) >= 2):
			(leaves setScript: (ScriptID 13 0))
		#endif
		(cond
			case ((global0 has: 37) and (not (proc913_0 43))):
				(beauty init: 1)
			#end:case
			case 
				(and
					(global154 != global153)
					(global155 <= 3)
					(not (proc913_0 43))
				):
				(beauty
					init: 0
					setScript:
						if (proc999_5 global155++ 3 4):
							rmAct3and4Scr
						else:
							rmAct1and2Scr
						#endif
				)
			#end:case
		)
		(global102 number: 250 loop: -1 play:)
	#end:method

	@classmethod
	def edgeToRoom(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 1
		match param1
			case 3:
				(proc12_0 param1 -50)
				return 0
			#end:case
			case 2:
				(proc12_0 3 -50)
				return 0
			#end:case
			case 4:
				(proc12_0 param1)
				return 0
			#end:case
			else:
				temp0 = 0
				(super edgeToRoom: param1 &rest)
			#end:else
		#end:match
		(return
			if temp0:
				(beauty setScript: 0)
				(global102 fade:)
			#endif
		)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			if (param1 == 1):
				(global91 say: noun param1 (26 if (global153 < 5) else 27))
				1
			else:
				(super doVerb: param1 &rest)
			#endif
		)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		global154 = global153
		(proc913_2 59)
		(super dispose: &rest)
		(DisposeScript 964)
		(DisposeScript 13)
	#end:method

	@classmethod
	def scriptCheck(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 0
		match param1
			case 87:
				if (global5 contains: beauty):
					(global91 say: 0 0 2 0 0 899)
				else:
					temp0 = 1
				#endif
			#end:case
			case 85:
				(cond
					case 
						(temp1 = (global5 contains: beauty) and (localproc_0)):
						(CueObj state: 0 cycles: 0 client: beauty theVerb: 31)
						(global0
							setMotion:
								PolyPath
								(beauty approachX:)
								(beauty approachY:)
								CueObj
						)
					#end:case
					case temp1:
						(beauty doVerb: 31 &rest)
					#end:case
					else:
						temp0 = 1
					#end:else
				)
			#end:case
			case 93:
				if (global5 contains: beauty):
					(global91 say: 7 0 16 0 0 0)
				else:
					temp0 = 1
				#endif
			#end:case
			else:
				temp0 = 1
			#end:else
		#end:match
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class roomConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class rmAct1and2Scr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(proc913_1 59)
				(client
					view: 253
					loop: 2
					cel: 0
					posn: 213 81
					setCycle: End self
				)
			#end:case
			case 1:
				(client loop: 3 cel: 0 setCycle: End self)
			#end:case
			case 2:
				(client cel: 0 posn: 202 88 setCycle: End self)
			#end:case
			case 3:
				(client cel: 0 posn: 194 94 setCycle: End self)
			#end:case
			case 4:
				(client loop: 4 cel: 0 posn: 191 96 setCycle: End self)
			#end:case
			case 5:
				seconds = register = (Random 1 9)
			#end:case
			case 6:
				(client loop: 5 cel: 0 posn: 174 97 setCycle: End self)
			#end:case
			case 7:
				(client loop: 6 cel: 0)
				seconds = (10 - register)
			#end:case
			case 8:
				(houseDoor noun: 23 view: 255 loop: 0 cel: 0 setCycle: End self)
				(global105 number: 901 loop: 1 play:)
			#end:case
			case 9:
				ticks = 12
			#end:case
			case 10:
				(houseDoor loop: 1 cel: 0 setCycle: End self)
			#end:case
			case 11:
				cycles = 2
			#end:case
			case 12:
				(houseDoor loop: 2 cel: 0)
				cycles = 2
			#end:case
			case 13:
				if (global155 == 1):
					register = 4
				else:
					register = 5
				#endif
				(global91 say: 1 0 register 1 self)
			#end:case
			case 14:
				(global91 say: 1 0 register 2 self)
			#end:case
			case 15:
				if (register != 4):
					(houseDoor setCycle: End self)
				else:
					state++
					ticks = 1
				#endif
			#end:case
			case 16:
				cycles = 2
			#end:case
			case 17:
				(global91 say: 1 0 register 3 self)
			#end:case
			case 18:
				if (register == 4):
					(houseDoor setCycle: End self)
				else:
					state++
					ticks = 1
				#endif
			#end:case
			case 19:
				cycles = 2
			#end:case
			case 20:
				(global91 say: 1 0 register 4 self)
			#end:case
			case 21:
				if (register != 4):
					cycles = 1
				else:
					(global91 say: 1 0 register 5 self)
				#endif
			#end:case
			case 22:
				(client setScript: rmEndofScriptsScr)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class rmAct3and4Scr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(proc913_1 59)
				(client view: 253 loop: 4 cel: 7 posn: 191 96)
				cycles = 1
			#end:case
			case 1:
				seconds = register = (Random 1 9)
			#end:case
			case 2:
				(client loop: 5 cel: 0 posn: 174 97 setCycle: End self)
			#end:case
			case 3:
				(client loop: 6 cel: 0)
				seconds = (10 - register)
			#end:case
			case 4:
				(houseDoor noun: 23 view: 255 loop: 0 cel: 0 setCycle: End self)
				(global105 number: 901 loop: 1 play:)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				if (global155 == 3):
					register = 6
					(houseDoor loop: 1 cel: 0 setCycle: End self)
				else:
					register = 7
					(state += 2)
					ticks = 1
				#endif
			#end:case
			case 7:
				cycles = 2
			#end:case
			case 8:
				(houseDoor loop: 2 cel: 0)
				cycles = 2
			#end:case
			case 9:
				(global91 say: 1 0 register 0 self)
			#end:case
			case 10:
				(client setScript: rmEndofScriptsScr)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class rmGiveRoseScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 put: 38 global11)
				(global1 handsOff:)
				((ScriptID 10 0) setIt: 128)
				if (proc913_1 37):
					register = 20
				else:
					register = 19
					(global1 givePoints: 2)
					(proc913_2 47)
				#endif
				(beauty setScript: 0)
				(global91 say: 6 71 register 1 self)
			#end:case
			case 1:
				if (register == 19):
					(global91 say: 6 71 register 2 self)
				else:
					(self cue:)
				#endif
			#end:case
			case 2:
				(global0
					setSpeed: 6
					view: 251
					loop: 0
					cel: 0
					posn: 250 154
					normal: 0
					setCycle: CT 4 1 self
				)
			#end:case
			case 3:
				(beauty view: 251 loop: 1 cel: 0 setCycle: CT 3 1 self)
			#end:case
			case 4:
				(beauty setCycle: End self)
				(global0 cel: 5)
			#end:case
			case 5:
				(global0
					reset: 0
					setSpeed: 6
					posn: (beauty approachX:) (beauty approachY:)
				)
				seconds = 2
			#end:case
			case 6:
				(beauty loop: 2 cel: 0 setCycle: End self)
			#end:case
			case 7:
				(global91
					say: 6 71 register (3 if (register == 19) else 2) self
					oneOnly: 0
				)
			#end:case
			case 8:
				(beauty setScript: roseTendingScr)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class roseTendingScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(client view: 251 loop: 4 cel: 0)
				cycles = 1
			#end:case
			case 1:
				seconds = (Random 2 5)
			#end:case
			case 2:
				(client setCycle: End self)
			#end:case
			case 3:
				seconds = (Random 2 5)
			#end:case
			case 4:
				(client setCycle: Beg self)
			#end:case
			case 5:
				state = 0
				cycles = 1
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class turnScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0: 0#end:case
			case 1:
				register = 1
				(global0 setHeading: register self)
			#end:case
			case 2:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class rmGiveRingScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 put: 37)
				(global1 handsOff:)
				(global1 givePoints: 2)
				(beauty
					setScript: 0
					setPri: 2
					view: 252
					posn: 290 158
					setHeading: 270 self
				)
				register = 0
			#end:case
			case 1:
				(roomConv
					add: -1 6 69 10 1
					add: -1 6 69 10 2
					add: -1 6 69 10 3
					add: -1 6 69 10 4
					add: -1 6 69 10 5
					add: -1 6 69 10 6
					add: -1 6 69 10 7
					add: -1 6 69 10 8
					add: -1 6 69 10 9
					add: -1 6 69 10 10
					add: -1 6 69 10 11
					add: -1 6 69 10 12
					add: -1 6 69 10 13
					add: -1 6 69 10 14
					add: -1 6 69 10 15
					init: self
				)
			#end:case
			case 2:
				(beauty view: 252 setCycle: Walk setMotion: MoveTo 147 122 self)
				(self setScript: turnScr 0 90)
				(global0 setMotion: MoveTo 121 154 turnScr)
			#end:case
			case 3:
				(beauty hide:)
				(global105 number: 906 loop: 1 play:)
				(gate view: 253 loop: 1 cel: 0 setCycle: CT 5 1 self)
			#end:case
			case 4:
				(gate setCycle: End)
				(beauty
					show:
					setPri: -1
					posn: 110 131
					setMotion: MoveTo 159 158 self
				)
			#end:case
			case 5:
				if (not (turnScr register:)):
					(turnScr caller: self)
				else:
					cycles = 2
				#endif
			#end:case
			case 6:
				(beauty loop: 1)
				(global0 loop: 0)
				cycles = 2
			#end:case
			case 7:
				(roomConv
					add: -1 6 69 10 16
					add: -1 6 69 10 17
					add: -1 6 69 10 18
					init: self
				)
			#end:case
			case 8:
				(global0
					normal: 0
					setSpeed: 6
					view: 253
					loop: 10
					posn: 127 157
					setCycle: CT 4 1 self
				)
			#end:case
			case 9:
				(beauty
					view: 253
					loop: 0
					cel: 0
					posn: 158 157
					setCycle: CT 3 1 self
				)
			#end:case
			case 10:
				(beauty setCycle: End self)
				(global0 setCycle: End self)
			#end:case
			case 11: 0#end:case
			case 12:
				(global91 say: 6 69 10 19 self)
			#end:case
			case 13:
				(beauty
					view: 252
					setCycle: Walk
					cycleSpeed: 5
					moveSpeed: 5
					setMotion: MoveTo 320 180
				)
				(global0
					reset: 0
					posn: 121 154
					setSpeed: 9
					setMotion: MoveTo 300 190 self
				)
				ticks = 60
			#end:case
			case 14:
				(houseDoor view: 255 loop: 2 cel: 0 setCycle: End self)
			#end:case
			case 15:
				(global91 say: 6 69 10 20 self)
			#end:case
			case 16:
				cycles = 10
			#end:case
			case 17:
				(global91 say: 6 69 10 21 self)
			#end:case
			case 18:
				(global102 fade:)
				(global2 newRoom: 540)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class rmEndofScriptsScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(houseDoor
					noun: 19
					view: 255
					loop: 0
					cel: (houseDoor lastCel:)
					setCycle: Beg houseDoor
				)
				(client posn: 174 97 loop: 7 cel: 0 setCycle: End self)
			#end:case
			case 1:
				(client
					setLoop: 8
					posn: 189 85
					setCycle: Walk
					setMotion: MoveTo 216 66 self
				)
			#end:case
			case 2:
				(houseDoor setCycle: End self)
				(global105 number: 901 loop: 1 play:)
			#end:case
			case 3:
				(client setLoop: -1 loop: 9 cel: 0 setCycle: End self)
			#end:case
			case 4:
				(houseDoor setCycle: Beg self)
			#end:case
			case 5:
				(global105 number: 902 loop: 1 play:)
				(proc913_2 59)
				(client dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class useFluteOnBeautyScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				register = (localproc_1)
				if (register != 11):
					state++
				#endif
				cycles = 2
			#end:case
			case 1:
				(self setScript: (ScriptID 85) self)
			#end:case
			case 2:
				match register
					case 11:
						(global91 say: 1 31 0 0 self 0)
					#end:case
					case 10:
						(global91 say: 6 31 12 1 self)
					#end:case
					else:
						state++
						(global91 say: 6 31 register 0 self)
					#end:else
				#end:match
			#end:case
			case 3:
				(global91
					say: (6 if (register == 10) else 2) 31 register 0 self
				)
			#end:case
			case 4:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class giveAllScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				register = (localproc_1)
				(global91
					say: 6 0 (10 if (register == 12) else register) 1 self
				)
			#end:case
			case 1:
				if (register != 11):
					(global91
						say: 6 0 register (1 if (register == 12) else 2) self
					)
				else:
					cycles = 2
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
class scriptToBeIgnored(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(client view: 255 loop: 0 cel: 0)
				cycles = 2
			#end:case
			case 1:
				(client setCycle: End self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				(client view: 257 loop: 0 cel: 0 setCycle: End self)
			#end:case
			case 4:
				cycles = 2
			#end:case
			case 5:
				(client loop: 1 cel: 0 setCycle: Fwd)
				ticks = 300
			#end:case
			case 6:
				(client loop: 0 cel: 10 setCycle: Beg self)
			#end:case
			case 7:
				cycles = 2
			#end:case
			case 8:
				(client view: 255 loop: 0 cel: 3 setCycle: Beg self)
			#end:case
			case 9:
				(client view: 250 loop: 1 cel: 0)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class beauty(Actor):
	#property vars (may be empty)
	x = 214
	y = 81
	noun = 6
	sightAngle = 45
	view = 252
	signal = 20480
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case ((proc999_5 param1 42 27 28 7 32 12 65 33) and (localproc_0)):
				(global91 say: noun param1 18)
			#end:case
			case ((proc999_5 param1 57 58 59 60 96 43 56) and (localproc_0)):
				(global91 say: noun 43 (10 if (proc913_0 37) else 12))
			#end:case
			case ((proc999_5 param1 66 70) and (localproc_0)):
				(global91 say: noun 66 (10 if (proc913_0 37) else 12))
			#end:case
			case (param1 == 31):
				(global2 setScript: useFluteOnBeautyScr)
			#end:case
			case ((proc999_5 param1 74 73 55) and (localproc_0)):
				(global91 say: noun 55 18)
			#end:case
			case ((param1 == 71) and (localproc_0)):
				(global2 setScript: rmGiveRoseScr)
			#end:case
			case (param1 == 69):
				if (proc913_0 37):
					(global2 setScript: rmGiveRingScr)
				else:
					(global91 say: noun param1 12)
				#endif
			#end:case
			case (param1 == 2):
				(global91
					say:
						noun
						param1
						if (localproc_0):
							(cond
								case (proc913_0 37):
									(+
										22
										if (local0 < 3):
											local0++
										else:
											local0
										#endif
									)
								#end:case
								case (proc913_0 47): 14#end:case
								else: 13#end:else
							)
						else:
							11
						#endif
				)
				(proc913_1 47)
			#end:case
			case (param1 == 1):
				(global91
					say:
						noun
						param1
						if (proc913_1 70):
							(10 if (proc913_0 37) else 9)
						else:
							21
						#endif
				)
			#end:case
			case (param1 == 5):
				(global91 say: noun param1 (18 if (localproc_0) else 11))
			#end:case
			else:
				(global2 setScript: giveAllScr)
			#end:else
		)
	#end:method

	@classmethod
	def init(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		if param1:
			(self
				view: 251
				posn: 285 156
				loop: 4
				setPri: 5
				approachX: 247
				approachY: 153
				approachVerbs: 2 71
				setScale: Scaler 100 67 153 109
				setScript: roseTendingScr
			)
		else:
			(self setCycle: Walk)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class gate(Prop):
	#property vars (may be empty)
	x = 118
	y = 108
	noun = 7
	sightAngle = 90
	view = 250
	signal = 16384
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 == 2):
			local4++
		#endif
		(super doVerb: param1 &rest)
	#end:method

#end:class or instance

@SCI.instance
class houseDoor(Prop):
	#property vars (may be empty)
	x = 221
	y = 68
	noun = 19
	sightAngle = 90
	view = 250
	loop = 1
	priority = 1
	signal = 16
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self view: 250 loop: 1 cel: 0)
		(global105 number: 902 loop: 1 play:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (and (local4 == 3) (local3 == 7) (param1 == 2)):
			local4 = 0
			local3 = 0
			(self setScript: scriptToBeIgnored)
		else:
			(super doVerb: param1 &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class leaves(Prop):
	#property vars (may be empty)
	x = 60
	y = 181
	view = 256
	priority = 15
	signal = 20496
	
	@classmethod
	def onMe():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		return 0
	#end:method

#end:class or instance

@SCI.instance
class featureToBeIgnored(Feature):
	#property vars (may be empty)
	x = 100
	y = 320
	noun = 3
	nsLeft = 3
	nsBottom = 7
	nsRight = 9
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (local4 == 3):
			match param1
				case 5:
					(local3 |= 0x0001)
				#end:case
				case 2:
					(local3 |= 0x0002)
				#end:case
				case 1:
					(local3 |= 0x0004)
				#end:case
			#end:match
		#endif
		(super doVerb: param1 &rest)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		sightAngle = 26505
	#end:method

#end:class or instance

@SCI.instance
class palmTrees(Feature):
	#property vars (may be empty)
	noun = 15
	onMeCheck = 4
	
#end:class or instance

@SCI.instance
class houseRoses(Feature):
	#property vars (may be empty)
	noun = 22
	onMeCheck = 4096
	
#end:class or instance

@SCI.instance
class genericFeatures(Feature):
	#property vars (may be empty)
	sightAngle = 40
	
	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(= noun
				match temp0 = (OnControl 4 (param1 x:) (param1 y:))
					case 2: 8#end:case
					case 1024: 21#end:case
					case 16: 12#end:case
					case 32: 11#end:case
					case 64: 17#end:case
					case 128: 14#end:case
					case 256: 13#end:case
					case 512: 18#end:case
					else: 0#end:else
				#end:match
			)
		)
	#end:method

#end:class or instance

