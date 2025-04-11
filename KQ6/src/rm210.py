#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 210
import sci_sh
import Main
import rgCrown
import walkEgoInScr
import KQ6Print
import KQ6Room
import CartoonScript
import n913
import Print
import Scaler
import PolyPath
import Polygon
import Feature
import LoadMany
import StopWalk
import DPath
import Path
import Motion
import Game
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm210 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = [295, 71, 283, 65, 277, 64, -32768, -32768]
local9 = [292, 71, 280, 65, 268, 61, 262, 61, 258, 56, 270, 55, 285, 55, 290, 53, 298, 47, -32768, -32768]
local29 = None
local30 = None
local31 = None
local32 = None
local33 = 4660
local34 = None
local35 = -1


@SCI.procedure
def localproc_0(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	if (singSing script:):
		local29 = param1
		if (proc999_5 (singSingScr state:) 3 9):
			(singSing setScript: 0)
		#endif
	else:
		(param1 cue:)
	#endif
#end:procedure

@SCI.instance
class rm210(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 210
	horizon = 0
	south = 200
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global2
			addObstacle:
				((Polygon new:)
					type: 2
					init: 39 -10 263 -10 250 78 232 104 139 139 76 113 39 82
					yourself:
				)
				((Polygon new:)
					type: 0
					init: 0 189 0 120 65 120 117 148 68 189
					yourself:
				)
				((Polygon new:)
					type: 2
					init: 29 138 94 138 94 156 31 162
					yourself:
				)
				((Polygon new:)
					type: 2
					init: 0 -10 27 -10 27 84 64 119 0 119
					yourself:
				)
				((Polygon new:)
					type: 2
					init: 115 189 151 145 244 108 266 79 319 79 319 189
					yourself:
				)
		)
		(super init: &rest)
		(global0 init: setScale: Scaler 100 84 134 81)
		(global32 add: genericFeatures tree holeInTree eachElementDo: #init)
		((ScriptID 10 4) onMeCheck: 2 setOnMeCheck: 1 2 init:)
		(proc958_0 132 214 215 216)
		match global12
			case 220:
				(global2 setScript: enterFromCastleScr 0 global0)
			#end:case
			case 240:
				(global2 setScript: enterFromVillageScr)
			#end:case
			case 140:
				(global104 fade: 0 30 8 1)
				(global0
					posn: (singSing approachX:) (singSing approachY:)
					loop: 6
				)
			#end:case
			else:
				if (global12 != 200):
					((ScriptID 10 0) setIt: 2)
				#endif
				local34 = 1
				(proc12_1 91 185 30)
			#end:else
		#end:match
		temp2 = ((global9 at: 39) owner:)
		temp3 = ((global9 at: 38) owner:)
		if ((proc913_0 94) and (temp3 != 140)):
			temp3 = global11
		#endif
		temp1 = ((global9 at: 47) owner:)
		if (((global9 at: 35) owner:) == -1):
			(theRibbon init:)
		#endif
		if (((global9 at: 32) owner:) == -1):
			(letter init:)
		#endif
		if (temp2 == 140):
			((global9 at: 39) owner: global11)
		#endif
		if (temp3 == 140):
			((global9 at: 38) owner: global11)
		#endif
		if (temp1 == 140):
			((global9 at: 47) owner: global11)
		#endif
		(= temp0
			(not
				(and
					(proc999_5 temp1 global11 140)
					(proc999_5 temp2 global11 140)
					(proc999_5 temp3 global11 140)
				)
			)
		)
		if ((ScriptID 10 0) isSet: 2):
			((ScriptID 10 0) clrIt: 2)
			(clown init:)
		#endif
		(cond
			case 
				(and
					(global12 == 140)
					(temp3 == 140)
					(not ((temp1 == global11) and (temp2 == global11)))
				):
				(proc10_2 returnToBranch 18)
			#end:case
			case 
				(and
					(global12 == 140)
					(temp3 == 140)
					(temp1 == global11)
					(temp2 == global11)
				):
				(proc10_2 notReturnScr 20)
			#end:case
			case (and (global12 == 140) (temp1 == 140) (temp2 != global11)):
				(proc10_2 returnToBranch 12)
			#end:case
			case 
				(and
					(global12 == 140)
					((temp2 == 140) or ((temp1 == 140) and (temp2 == global11)))
				):
				local32 = 1
				(proc10_2 deliveryScr 13)
			#end:case
			case (proc913_0 62):
				(proc10_2 deliveryScr 5)
			#end:case
			case (proc913_0 63):
				(proc10_2 deliveryScr 6)
			#end:case
			else:
				if ((global0 has: 0) and temp0):
					if (proc913_0 21):
						(singSing init: 0)
					else:
						(singSing init: 1)
					#endif
					(global103 number: 210 loop: -1 play:)
					(musicScr client: musicScr cue:)
				#endif
				(proc913_2 62)
				(proc913_2 63)
			#end:else
		)
		(= temp5
			(or
				(proc999_5
					(global2 script:)
					enterFromCastleScr
					enterFromVillageScr
				)
				local34
			)
		)
		if 
			(and
				(global5 contains: singSing)
				(or
					(temp5 and (not ((global2 script:) script:)))
					((not temp5) and (not (global2 script:)))
				)
			)
			(singSing setScript: singSingScr)
		#endif
		if (global12 != 220):
			(global102 number: 917 loop: -1 play:)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (global0 onControl: 1)
		(cond
			case script: 0#end:case
			case (temp0 & 0x4000):
				(global0 setSpeed: 6)
				(global2 setScript: (Clone exitToCastleScr) 0 global0)
			#end:case
			case (temp0 & 0x2000):
				(global2 setScript: exitToVillageScr)
			#end:case
		)
		(super doit: &rest)
	#end:method

	@classmethod
	def newRoom(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((param1 == 220) and (global5 contains: clown)):
			((ScriptID 10 0) setIt: 2)
		#endif
		if (global5 contains: singSing):
			(global103 fade:)
			if (global78 contains: musicScr):
				(musicScr dispose:)
			#endif
		#endif
		(super newRoom: param1 &rest)
	#end:method

	@classmethod
	def scriptCheck(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 85:
				if (not (global5 contains: singSing)):
					temp0 = 1
				else:
					(self setScript: fluteScr)
					temp0 = 0
				#endif
			#end:case
			case 93:
				if (not (global5 contains: singSing)):
					temp0 = 1
				else:
					(singSing doVerb: 37)
					temp0 = 0
				#endif
			#end:case
		#end:match
		return temp0
	#end:method

	@classmethod
	def edgeToRoom(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (param1 == 3):
				(proc12_0 param1 30)
				return 0
			#end:case
			case argc:
				(super edgeToRoom: param1 &rest)
			#end:case
			else:
				(super edgeToRoom:)
			#end:else
		)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global102 fade:)
		(super dispose:)
		(DisposeScript 983)
		(DisposeScript 964)
	#end:method

#end:class or instance

@SCI.instance
class exitPath(Path):
	#property vars (may be empty)
	@classmethod
	def at(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (client == global0):
			return local1[param1]
		else:
			return local9[param1]
		#endif
	#end:method

#end:class or instance

@SCI.instance
class musicScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				if (not register):
					(global104 stop:)
				#endif
				register = 1
				(global78 add: self)
				while True: #repeat
					(breakif (register = (Random 0 2) != local33))
				#end:loop
				(global104
					number:
						match register
							case 0: 214#end:case
							case 1: 215#end:case
							case 2: 216#end:case
						#end:match
					loop: 1
					play: self
				)
			#end:case
			case 1:
				state = -1
				ticks = (Random 60 300)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
		if register:
			(global78 delete: self)
		#endif
		register = 0
	#end:method

#end:class or instance

@SCI.instance
class fluteScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(localproc_0 self)
			#end:case
			case 1:
				if (global5 contains: singSing):
					(global103 fade:)
					(musicScr dispose:)
				#endif
				(global102 fade:)
				(self setScript: (ScriptID 85) self)
			#end:case
			case 2:
				(global91 say: 14 31 9 0 self)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				(global102 play:)
				if (global5 contains: singSing):
					(global103 play:)
					(musicScr state: -1 client: musicScr cue:)
				#endif
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class enterFromVillageScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0
					setSpeed: 6
					posn: 23 70
					setScale: Scaler 86 20 88 70
					setMotion: MoveTo 38 88 self
				)
			#end:case
			case 1:
				(global0 reset: 2 setScale: Scaler 100 84 134 81)
				cycles = 1
			#end:case
			case 2:
				if (not script):
					cycles = 1
				#endif
			#end:case
			case 3:
				if (not (global5 contains: clown)):
					(global1 handsOn:)
				#endif
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class exitToVillageScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					setSpeed: 6
					setScale: Scaler 90 20 88 70
					setMotion: MoveTo 23 70 self
				)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				(global2 newRoom: 240)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class enterFromCastleScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0
					setSpeed: 6
					posn: 277 64
					setScale: Scaler 30 5 75 15
					setMotion: DPath 283 65 295 71 300 79 self
				)
			#end:case
			case 1:
				(global0 hide:)
				ticks = 150
			#end:case
			case 2:
				(global0
					show:
					setPri: 3
					posn: 271 130
					setLoop: 2
					scaleX: 108
					scaleY: 108
					setScale:
					setMotion: MoveTo 263 81 self
				)
			#end:case
			case 3:
				(global0 setPri: -1 setScale: Scaler 100 84 134 81)
				cycles = 1
			#end:case
			case 4:
				(global0 setMotion: MoveTo 260 85 self)
			#end:case
			case 5:
				(global0 reset: 2)
				if register:
					(register cue:)
				#endif
				if (not script):
					cycles = 1
				#endif
			#end:case
			case 6:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class exitToCastleScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				if (register == global0):
					(global1 handsOff:)
				#endif
				(register
					setLoop: 3
					setPri: 3
					setScale:
					setMotion: MoveTo 267 131 self
				)
			#end:case
			case 1:
				(register hide:)
				ticks = 150
				if (register != global0):
					(global1 handsOn:)
				#endif
			#end:case
			case 2:
				(register
					show:
					setLoop: -1
					setPri: -1
					setScale: Scaler 30 5 75 15
					posn: 300 79
				)
				(register setMotion: (Clone exitPath) self)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				if (register == global0):
					(global2 newRoom: 220)
				else:
					(self dispose:)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class clownScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(clown setMotion: PolyPath 138 144 self)
			#end:case
			case 1:
				(clown view: 718 setLoop: 5 setMotion: PolyPath 247 104 self)
			#end:case
			case 2:
				(clown view: 717 setLoop: -1 setMotion: PolyPath 261 85 self)
			#end:case
			case 3:
				(self setScript: (Clone exitToCastleScr) self clown)
			#end:case
			case 4:
				(clown hide:)
				seconds = 10
			#end:case
			case 5:
				(clown dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class returnToBranch(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(singSing
					init:
					z: 0
					setPri: 1
					posn: 305 30
					setScale: Scaler 100 5 51 30
					setLoop: 0
					setCycle: Fwd
					setMotion: MoveTo 272 52 self
				)
			#end:case
			case 1:
				(singSing
					setStep: 4 3
					setScale: 0
					setMotion: MoveTo 226 55 self
				)
			#end:case
			case 2:
				(singSing setLoop: 3 cel: 0 setCycle: End self)
			#end:case
			case 3:
				(singSing loop: 2 cel: 8 posn: 252 125 97 setPri: 14)
				cycles = 2
			#end:case
			case 4:
				(global91 say: 1 0 register 0 self)
			#end:case
			case 5:
				(global103 number: 210 loop: -1 play:)
				(musicScr client: musicScr cue:)
				(proc913_2 62)
				(proc913_2 63)
				(singSing setScript: singSingScr)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class notReturnScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				seconds = 5
			#end:case
			case 1:
				(global91 say: 1 0 register 0 self)
			#end:case
			case 2:
				(proc913_2 62)
				(proc913_2 63)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class deliveryScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				if (proc999_5 register 5 6):
					(singSing init: 0)
					(cond
						case (clown script:):
							seconds = 6
						#end:case
						case (client == enterFromCastleScr):
							(client register: self)
						#end:case
						else:
							seconds = 3
						#end:else
					)
				else:
					state = 2
					(singSing
						init:
						z: 0
						posn: 305 30
						setScale: Scaler 100 5 51 30
					)
					cycles = 2
				#endif
			#end:case
			case 1:
				(singSing z: 0 loop: 4 cel: 0 posn: 225 56 setCycle: End self)
			#end:case
			case 2:
				(singSing posn: 201 56)
				(self cue:)
			#end:case
			case 3:
				(singSing
					view: 214
					setLoop: (0 if (proc913_0 62) else 1)
					setCycle: Fwd
				)
				if (proc999_5 register 5 6):
					state = 4
				#endif
				(self cue:)
			#end:case
			case 4:
				(singSing setMotion: MoveTo 272 52 self)
			#end:case
			case 5:
				(singSing setScale: 0 setStep: 4 3)
				if (proc913_0 62):
					(singSing setMotion: MoveTo 156 79 self)
				else:
					(singSing setMotion: MoveTo 111 81 self)
				#endif
			#end:case
			case 6:
				if (proc913_0 62):
					(theRibbon init:)
				else:
					(letter init:)
				#endif
				if 
					(and
						(((global9 at: 39) owner:) == global11)
						(((global9 at: 38) owner:) == global11)
						(((global9 at: 47) owner:) == global11)
					)
					(singSing
						view: 213
						setLoop: 0
						setMotion: MoveTo -10 79 self
					)
				else:
					state++
					(self cue:)
				#endif
			#end:case
			case 7:
				(singSing dispose:)
				cycles = 2
				state = 10
			#end:case
			case 8:
				if (proc913_0 62):
					(singSing posn: 156 79)
				else:
					(singSing posn: 111 81)
				#endif
				(singSing view: 213 setLoop: 5 cel: 0 setCycle: End self)
			#end:case
			case 9:
				if (proc913_0 62):
					(singSing posn: 185 69)
				else:
					(singSing posn: 141 72)
				#endif
				(singSing
					setLoop: 1
					setCycle: Fwd
					setMotion: MoveTo 220 49 self
				)
			#end:case
			case 10:
				(singSing
					setLoop: -1
					loop: 6
					cel: 0
					posn: 225 56
					setCycle: End self
				)
			#end:case
			case 11:
				if (global5 contains: singSing):
					(global103 number: 210 loop: -1 play:)
					(musicScr state: -1 client: musicScr cue:)
				#endif
				(global91 say: 1 0 register 0 self)
			#end:case
			case 12:
				if (global5 contains: singSing):
					(singSing
						loop: 2
						cel: 8
						posn: 252 125 97
						setPri: 14
						setScript: singSingScr
					)
				#endif
				if local32:
					(global1 handsOn:)
				#endif
				(proc913_2 62)
				(proc913_2 63)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class giveItemToBirdScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 setMotion: MoveTo 138 142 self)
			#end:case
			case 1:
				(global0 setHeading: 90 self)
			#end:case
			case 2:
				(localproc_0 self)
			#end:case
			case 3:
				(global0
					view: 211
					posn: 147 143
					loop: 0
					cel: 0
					normal: 0
					setCycle: End self
				)
				if local31:
					(genieSnake init:)
				#endif
			#end:case
			case 4:
				if 
					(and
						(global5 contains: genieSnake)
						(((genieSnake script:) state:) <= 0)
					)
					state--
					ticks = 15
				else:
					(self cue:)
				#endif
			#end:case
			case 5:
				(client cue:)
			#end:case
			case 6:
				(global103 fade:)
				(musicScr dispose:)
				(singSing z: 0 loop: 4 posn: 225 56 setCycle: End self)
			#end:case
			case 7:
				(singSing
					setLoop: 0
					posn: 201 56
					setCycle: Fwd self
					setMotion: MoveTo 158 95 self
				)
			#end:case
			case 8:
				if ((global103 prevSignal:) != -1):
					(global103 stop:)
				#endif
				(global105 number: 212 play:)
				if (proc913_0 10):
					(global105 hold: 10)
				#endif
				(singSing setLoop: 5 cel: 0 setCycle: End self)
			#end:case
			case 9:
				(client cue:)
			#end:case
			case 10:
				(global0 setCycle: Beg self)
				(self cue:)
				register = 0
			#end:case
			case 11:
				(singSing
					view: 214
					setLoop:
						match register
							case 2: 2#end:case
							case 1: 3#end:case
							case 0: 4#end:case
						#end:match
					posn: 187 85
					setCycle: Fwd
					setMotion: MoveTo 272 52 self
				)
			#end:case
			case 12:
				(global0 posn: ((global0 x:) - 10) ((global0 y:) - 3) reset: 4)
			#end:case
			case 13:
				(client cue:)
			#end:case
			case 14:
				(singSing
					setScale: Scaler 100 5 51 30
					setMotion: MoveTo 305 30 self
				)
			#end:case
			case 15:
				(singSing dispose:)
				if (global5 contains: genieSnake):
					((genieSnake script:) caller: self ticks: 0 state: 2 cue:)
				else:
					(self cue:)
				#endif
			#end:case
			case 16:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class givePoemScr(CartoonScript):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 put: 47 140)
				(global1 handsOff:)
				if (temp0 = ((global9 at: 39) owner:) == 210):
					(global1 givePoints: 1)
				#endif
				temp1 = ((global9 at: 38) owner:)
				(= register
					(cond
						case 
							(and
								(temp0 != global11)
								(temp1 != global11)
								(((global9 at: 47) owner:) != global11)
							):
							local31 = 1
							(25 if (proc913_0 10) else 26)
						#end:case
						case ((temp0 != global11) and (temp1 == global11)): 32#end:case
						case (temp0 == global11):
							(proc913_1 63)
							14
						#end:case
					)
				)
				(self setScript: giveItemToBirdScr self 2)
			#end:case
			case 1:
				if (proc999_5 register 14 32 25):
					(KQ6Print posn: -1 80)
				else:
					(KQ6Print posn: -1 100)
				#endif
				(KQ6Print
					font: global22
					say: 0 4 32 register 1
					init: giveItemToBirdScr
				)
			#end:case
			case 2:
				if (proc999_5 register 25 26):
					(KQ6Print
						font: global22
						posn: -1 100
						say: 0 4 32 register 2
						init: giveItemToBirdScr
					)
				else:
					(giveItemToBirdScr cue:)
				#endif
			#end:case
			case 3:
				(KQ6Print
					font: global22
					posn: -1 100
					modeless: 1
					ticks: 0
					say:
						0
						4
						32
						register
						(3 if (proc999_5 register 25 26) else 2)
					init:
				)
				(giveItemToBirdScr cue:)
			#end:case
			case 4:
				if global25:
					if (global90 & 0x0002):
						(self cue:)
					else:
						state++
						(KQ6Print caller: self)
					#endif
				else:
					state++
					(self cue:)
				#endif
			#end:case
			case 5:
				if (not ((DoAudio 6) == -1)):
					state--
				#endif
				ticks = 10
			#end:case
			case 6:
				if (proc913_0 10):
					(global2 newRoom: 140)
				else:
					(global1 handsOn:)
					(self dispose:)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class giveRingScr(CartoonScript):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 put: 39 140)
				(global1 handsOff:)
				if (proc913_0 10):
					(global1 givePoints: 3)
				else:
					(global1 givePoints: 1)
				#endif
				(proc913_1 62)
				temp0 = ((global9 at: 47) owner:)
				temp1 = ((global9 at: 38) owner:)
				(= register
					(cond
						case 
							(and
								(temp0 != global11)
								(temp1 != global11)
								(((global9 at: 39) owner:) != global11)
							):
							local31 = 1
							(25 if (proc913_0 10) else 26)
						#end:case
						case ((temp0 == global11) and (temp1 != global11)): 36#end:case
						case ((temp0 == global11) and (temp1 == global11)): 38#end:case
						case ((temp1 == global11) and (temp0 != global11)): 34#end:case
						else:
							(proc921_0
								r"""Problem! In else state of giveRoseScr conditional."""
							)
						#end:else
					)
				)
				(self setScript: giveItemToBirdScr self 0)
			#end:case
			case 1:
				(cond
					case (register == 25):
						(KQ6Print posn: -1 100)
					#end:case
					case (proc999_5 register 36 34):
						(KQ6Print posn: -1 100)
					#end:case
					case (register == 38):
						(KQ6Print posn: -1 100)
					#end:case
					else:
						(KQ6Print posn: -1 100)
					#end:else
				)
				(KQ6Print
					font: global22
					say: 0 4 70 register 1
					init: giveItemToBirdScr
				)
			#end:case
			case 2:
				if (proc999_5 register 25 26):
					(KQ6Print
						font: global22
						posn: -1 100
						say: 0 4 70 register 2
						init: giveItemToBirdScr
					)
				else:
					(giveItemToBirdScr cue:)
				#endif
			#end:case
			case 3:
				if (proc999_5 register 36 38):
					register = 34
				#endif
				(KQ6Print
					font: global22
					posn: -1 100
					modeless: 1
					ticks: 0
					say:
						0
						4
						70
						register
						(3 if (proc999_5 register 25 26) else 2)
					init:
				)
				(giveItemToBirdScr cue:)
			#end:case
			case 4:
				if global25:
					if (global90 & 0x0002):
						(self cue:)
					else:
						state++
						(KQ6Print caller: self)
					#endif
				else:
					state++
					(self cue:)
				#endif
			#end:case
			case 5:
				if (not ((DoAudio 6) == -1)):
					state--
				#endif
				ticks = 10
			#end:case
			case 6:
				if (proc913_0 10):
					(global2 newRoom: 140)
				else:
					(global1 handsOn:)
					(self dispose:)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class giveRoseScr(CartoonScript):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 put: 38 140)
				(global1 handsOff:)
				temp0 = ((global9 at: 39) owner:)
				temp1 = ((global9 at: 47) owner:)
				if (temp0 == global11):
					(global1 givePoints: 1)
				#endif
				(= register
					(cond
						case 
							(and
								(temp0 != global11)
								(temp1 != global11)
								(((global9 at: 38) owner:) != global11)
							):
							local31 = 1
							(25 if (proc913_0 10) else 26)
						#end:case
						case ((temp0 != global11) and (temp1 == global11)): 41#end:case
						case ((temp0 == global11) and (temp1 != global11)): 23#end:case
						case ((temp0 == global11) and (temp1 == global11)): 24#end:case
						else:
							(proc921_0
								r"""Problem! In else state of giveRoseScr conditional."""
							)
						#end:else
					)
				)
				(self setScript: giveItemToBirdScr self 1)
			#end:case
			case 1:
				(cond
					case (register == 25):
						(KQ6Print posn: -1 80)
					#end:case
					case (proc999_5 register 23 41):
						(KQ6Print posn: -1 80)
					#end:case
					else:
						(KQ6Print posn: -1 100)
					#end:else
				)
				(KQ6Print
					font: global22
					say: 0 4 71 register 1
					init: giveItemToBirdScr
				)
			#end:case
			case 2:
				if (proc999_5 register 25 26):
					(KQ6Print
						font: global22
						posn: -1 100
						say: 0 4 71 register 2
						init: giveItemToBirdScr
					)
				else:
					(giveItemToBirdScr cue:)
				#endif
			#end:case
			case 3:
				if (proc999_5 register 41):
					register = 23
				#endif
				(KQ6Print
					font: global22
					posn: -1 100
					modeless: 1
					ticks: 0
					say:
						0
						4
						71
						register
						(3 if (proc999_5 register 25 26) else 2)
					init:
				)
				(giveItemToBirdScr cue:)
			#end:case
			case 4:
				if global25:
					if (global90 & 0x0002):
						(self cue:)
					else:
						state++
						(KQ6Print caller: self)
					#endif
				else:
					state++
					(self cue:)
				#endif
			#end:case
			case 5:
				if (not ((DoAudio 6) == -1)):
					state--
				#endif
				ticks = 10
			#end:case
			case 6:
				if (proc913_0 10):
					(global2 newRoom: 140)
				else:
					(global1 handsOn:)
					(self dispose:)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class windBirdHeader(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: PolyPath 120 141 self)
			#end:case
			case 1:
				(global0 setHeading: 90 self)
			#end:case
			case 2:
				(localproc_0 self)
			#end:case
			case 3:
				(KQ6Print
					font: global22
					posn: 10 10
					say: 0 4 37 register 1
					init: self
				)
			#end:case
			case 4:
				cycles = 2
			#end:case
			case 5:
				(global103 fade:)
				(musicScr dispose:)
				(global0
					setSpeed: 6
					view: 883
					loop: 1
					cel: 0
					posn: 120 142
					normal: 0
					setCycle: Fwd
					scaleX: 128
					scaleY: 128
					setScale:
				)
				(global105 number: 930 loop: -1 play:)
				ticks = 180
			#end:case
			case 6:
				(global105 stop:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class windUpBirdScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(self setScript: windBirdHeader self 10)
			#end:case
			case 1:
				(global105 number: 931 loop: -1 play:)
				(global0 loop: 7 cycleSpeed: 9 setCycle: Fwd)
				ticks = 180
			#end:case
			case 2:
				(KQ6Print
					font: global22
					posn: 10 10
					say: 0 4 37 10 2
					init: self
				)
			#end:case
			case 3:
				(KQ6Print
					font: global22
					posn: 10 10
					say: 0 4 37 10 3
					init: self
				)
			#end:case
			case 4:
				ticks = 30
			#end:case
			case 5:
				(global105 fade:)
				(global103 play: 0 fade: 127 25 10 0)
				(musicScr state: -1 client: musicScr cue:)
				(global0 reset: 0 posn: 126 139)
				cycles = 2
			#end:case
			case 6:
				(singSing setScript: singSingScr)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class befriendSSScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 givePoints: 4)
				(self setScript: windBirdHeader self 11)
			#end:case
			case 1:
				(global0 loop: 3 cel: 0 posn: 119 142 setCycle: End self)
			#end:case
			case 2:
				(windUpBird init:)
				(global105 number: 931 loop: -1 play:)
				(global0 posn: 120 141 reset: 0)
				cycles = 2
			#end:case
			case 3:
				ticks = 180
			#end:case
			case 4:
				(KQ6Print
					font: global22
					posn: 10 10
					say: 0 4 37 11 2
					init: self
				)
			#end:case
			case 5:
				(singSing posn: 252 125 97 loop: 2 cel: 0 setCycle: End self)
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				(KQ6Print
					font: global22
					posn: 10 10
					say: 0 4 37 11 3
					init: self
				)
			#end:case
			case 8:
				ticks = 48
			#end:case
			case 9:
				(global105 fade:)
				(windUpBird dispose:)
				(global0
					setSpeed: 6
					posn: 119 143
					view: 883
					loop: 3
					cel: 7
					normal: 0
					setCycle: CT 1 -1 self
				)
			#end:case
			case 10:
				(global103 play: 0 fade: 127 25 10 0)
				(musicScr state: -1 client: musicScr cue:)
				(global0 reset: 0 posn: 120 141 setScale: Scaler 100 84 134 81)
				(proc913_1 21)
				(singSing setScript: singSingScr)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class snakeScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(client setCycle: End self)
			#end:case
			case 1:
				(client loop: 1 cel: 0 setCycle: End self)
			#end:case
			case 2:
				if (local35++ < 2):
					(global104 number: 211 loop: 1 play:)
				#endif
				if ((not (Random 0 1)) and (not local30)):
					local30 = 1
					state = 5
					(self cue:)
				else:
					state = 0
					ticks = (Random 60 150)
				#endif
			#end:case
			case 3:
				if (not local30):
					local30 = register = 1
					state = 5
					(self cue:)
				else:
					register = 0
					if (global5 contains: eye):
						(eye dispose:)
					#endif
					(genieSnake loop: 2 cel: 0 setCycle: End self)
				#endif
			#end:case
			case 4:
				(genieSnake dispose:)
			#end:case
			case 5:
				if ((genieSnake cel:) != 6):
					(genieSnake setCycle: End self)
				else:
					(self cue:)
				#endif
			#end:case
			case 6:
				(eye init: setCycle: End self)
			#end:case
			case 7:
				ticks = 45
			#end:case
			case 8:
				(eye setCycle: Beg self)
			#end:case
			case 9:
				(eye dispose:)
				state = ((3 if register else 2) - 1)
				(self cue:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class showItemScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					setMotion:
						MoveTo
						(singSing approachX:)
						(singSing approachY:)
						self
				)
			#end:case
			case 1:
				(global0
					view: 211
					posn: 147 145
					loop: 0
					cel: 0
					normal: 0
					setCycle: End self
				)
			#end:case
			case 2:
				ticks = 30
			#end:case
			case 3:
				(global91 say: 4 0 11 1 self)
			#end:case
			case 4:
				if (proc913_0 21):
					(global91 say: 4 register 10 1 self)
				else:
					(global91 say: 4 register 11 2 self)
				#endif
			#end:case
			case 5:
				(global0 setCycle: Beg self)
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				(global0
					reset: 4
					posn: (singSing approachX:) (singSing approachY:)
				)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class singSingScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				register = (proc913_0 21)
				cycles = 1
			#end:case
			case 1:
				(= state
					match (Random 0 1)
						case 0: 4#end:case
						case 1: 10#end:case
					#end:match
				)
				state--
				if local29:
					(self dispose:)
				else:
					seconds = (Random 3 12)
				#endif
			#end:case
			case 2:
				if register:
					(singSing posn: 225 105 49)
				else:
					(singSing posn: 268 96 85)
				#endif
				cycles = 2
			#end:case
			case 3: 0#end:case
			case 4:
				(singSing loop: 7 cel: 0)
				(self changeState: 2)
				state = 4
			#end:case
			case 5:
				(singSing setCycle: End self)
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				(singSing setCycle: Beg self)
			#end:case
			case 8:
				state = 0
				ticks = 1
			#end:case
			case 9: 0#end:case
			case 10:
				(singSing loop: 8 cel: 0)
				(self changeState: 2)
				state = 10
			#end:case
			case 11:
				(singSing cycleSpeed: 8 setCycle: End self)
			#end:case
			case 12:
				(singSing cycleSpeed: 6 cel: 0)
				cycles = 2
			#end:case
			case 13:
				(self changeState: 8)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (local29 and (local29 != -1)):
			if (not global18):
				global18 = (Set new:)
			#endif
			(global18 add: ((Cue new:) cuee: local29 cuer: self yourself:))
		#endif
		(singSing cycleSpeed: 6)
		local29 = seconds = 0
		(super dispose:)
	#end:method

#end:class or instance

@SCI.instance
class getRibbonScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global1 givePoints: 1)
				cycles = 2
			#end:case
			case 1:
				(global0 get: 35 setHeading: 90 self)
			#end:case
			case 2:
				if (not (proc913_0 112)):
					(proc913_1 93)
				#endif
				cycles = 2
			#end:case
			case 3:
				(global0
					normal: 0
					setSpeed: 6
					posn: 142 149
					view: 215
					loop: 1
					cel: 0
				)
				cycles = 2
			#end:case
			case 4:
				(global0 setCycle: CT 3 1 self)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				(theRibbon dispose:)
				(global0 setCycle: End self)
			#end:case
			case 7:
				cycles = 2
			#end:case
			case 8:
				(global0 reset: 6 posn: 129 144)
				cycles = 2
			#end:case
			case 9:
				(UnLoad 128 215)
				(global91 say: 6 5 (22 if (proc913_0 10) else 21) 0 self)
			#end:case
			case 10:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getLetterScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global1 givePoints: 1)
				cycles = 2
			#end:case
			case 1:
				(global0 get: 32 setHeading: 270 self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				(global0
					normal: 0
					setSpeed: 6
					posn: 138 147
					view: 215
					loop: 0
					cel: 0
				)
				cycles = 2
			#end:case
			case 4:
				(global0 setCycle: CT 3 1 self)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				(letter dispose:)
				(global0 setCycle: End self)
			#end:case
			case 7:
				cycles = 2
			#end:case
			case 8:
				(global0 reset: 7 posn: 149 142)
				cycles = 2
			#end:case
			case 9:
				if (global5 contains: singSing):
					(global103 fade: 0 15 20 1)
					(musicScr dispose:)
				else:
					state++
				#endif
				(global91 say: 5 5 0 1 self)
			#end:case
			case 10:
				if ((global103 prevSignal:) != -1):
					state--
				#endif
				cycles = 2
			#end:case
			case 11:
				(global105 number: 213 loop: -1 play:)
				if (global90 & 0x0002):
					(global91 say: 5 5 0 2 self)
				else:
					(KQ6Print
						addText:
							r"""Dearest Alexander:\n\nI cannot believe you are here, my friend! Please, please be careful! Abdul isn't about to let anyone interfere with his plans. Watch out for Abdul's genie, Alexander, and do not do anything rash."""
						init: self
					)
				#endif
			#end:case
			case 12:
				if (global90 & 0x0002):
					cycles = 1
				else:
					(KQ6Print
						addText:
							r"""I am not without resources, and I will prevail if I can only find some small means of defense. Do nothing to try to get to me. You must not be endangered again for my sake.\n\nGreatly in your family's debt,\n\nCassima"""
						init: self
					)
				#endif
			#end:case
			case 13:
				(global91 say: 5 5 0 3 self oneOnly: 0)
			#end:case
			case 14:
				(global105 client: self fade: 0 15 20 1)
			#end:case
			case 15:
				if (global5 contains: singSing):
					(global103 play:)
					(musicScr state: -1 client: musicScr cue:)
				#endif
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class eye(Prop):
	#property vars (may be empty)
	x = 128
	y = 24
	view = 902
	priority = 14
	signal = 16
	
#end:class or instance

@SCI.instance
class singSing(Actor):
	#property vars (may be empty)
	x = 252
	y = 125
	z = 97
	noun = 4
	approachX = 138
	approachY = 142
	view = 213
	loop = 2
	priority = 14
	signal = 8208
	
	@classmethod
	def init(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self
			setScale: 0
			setStep: 4 3
			ignoreActors:
			cel: (8 if (not param1) else 0)
		)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (proc999_5 param1 1 5):
				(global91 say: noun param1 (10 if (proc913_0 21) else 11))
			#end:case
			case ((proc999_5 param1 29 46 44 66) and (proc913_0 21)):
				(global91 say: noun 29 10)
			#end:case
			case (param1 == 37):
				if (proc913_0 21):
					(global2 setScript: windUpBirdScr)
				else:
					(global2 setScript: befriendSSScr)
				#endif
			#end:case
			case (param1 == 2):
				(global91
					say:
						noun
						param1
						(cond
							case (not (proc913_0 21)): 11#end:case
							case (global0 has: 32): 19#end:case
							else: 43#end:else
						)
				)
			#end:case
			case (param1 == 31):
				(global2 setScript: fluteScr)
			#end:case
			case (not (proc913_0 21)):
				(global2 setScript: showItemScr 0 0)
			#end:case
			case (proc999_5 param1 15 18):
				(global91 say: noun 15 10)
			#end:case
			case (param1 == 32):
				(global2 setScript: givePoemScr)
			#end:case
			case (param1 == 71):
				if (proc913_0 94):
					(global91 say: noun param1 27)
				else:
					(proc913_1 94)
					(global2 setScript: giveRoseScr)
				#endif
			#end:case
			case (param1 == 70):
				(global2 setScript: giveRingScr)
			#end:case
			case (proc999_5 param1 42 27 28 45 8):
				(global91 say: noun 42 10)
			#end:case
			case (proc999_5 param1 33 65):
				(global91 say: noun 33)
			#end:case
			case (proc999_5 param1 63 67):
				(global2 setScript: showItemScr 0 63)
			#end:case
			case (proc999_5 param1 35 47 68 72):
				(global2 setScript: showItemScr 0 param1)
			#end:case
			else:
				(global2 setScript: showItemScr 0 0)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class letter(Actor):
	#property vars (may be empty)
	x = 119
	y = 89
	noun = 5
	sightAngle = 45
	approachX = 146
	approachY = 142
	yStep = 4
	view = 214
	loop = 7
	cel = 1
	priority = 1
	signal = 18448
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self posn: 112 136 setLoop: 8 cel: 0 stopUpd:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global2 setScript: getLetterScr)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 5)
		if (((global9 at: 32) owner:) != -1):
			((global9 at: 32) owner: -1)
			(self setMotion: MoveTo 120 137 self)
		else:
			(self cue:)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class theRibbon(Actor):
	#property vars (may be empty)
	x = 155
	y = 87
	noun = 6
	sightAngle = 45
	approachX = 133
	approachY = 143
	yStep = 4
	view = 214
	loop = 5
	priority = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 5 signal: 18448)
		if (((global9 at: 35) owner:) != -1):
			((global9 at: 35) owner: -1)
			(self setMotion: MoveTo 155 138 self)
		else:
			(self cue:)
		#endif
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self posn: 153 138 setLoop: 6 cel: 0 stopUpd:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global2 setScript: getRibbonScr)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genieSnake(Prop):
	#property vars (may be empty)
	x = 109
	y = 5
	view = 212
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self dispose:)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self setScript: snakeScr setPri: 14)
	#end:method

#end:class or instance

@SCI.instance
class clown(Actor):
	#property vars (may be empty)
	x = 62
	y = 102
	view = 717
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self
			setScale: Scaler 100 84 134 81
			setScript: clownScr
			ignoreActors:
			setStep: 4 3
			moveSpeed: 7
			cycleSpeed: 7
			setCycle: StopWalk 2741
		)
	#end:method

#end:class or instance

@SCI.instance
class windUpBird(Prop):
	#property vars (may be empty)
	x = 141
	y = 142
	view = 883
	loop = 5
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self setCycle: Fwd)
	#end:method

#end:class or instance

@SCI.instance
class tree(Feature):
	#property vars (may be empty)
	x = 160
	y = 30
	noun = 11
	sightAngle = 40
	onMeCheck = 32
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global91
					say:
						noun
						param1
						(cond
							case 
								(and
									(global5 contains: singSing)
									(proc913_0 21)
								):
								10
							#end:case
							case (global5 contains: singSing): 11#end:case
							else: 8#end:else
						)
				)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class holeInTree(Feature):
	#property vars (may be empty)
	x = 147
	y = 111
	noun = 12
	sightAngle = 40
	onMeCheck = 128
	approachX = 136
	approachY = 139
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 5 2)
	#end:method

#end:class or instance

@SCI.instance
class genericFeatures(Feature):
	#property vars (may be empty)
	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(= noun
				match temp0 = (OnControl 4 (param1 x:) (param1 y:))
					case 4: 8#end:case
					case 8: 9#end:case
					case 16: 10#end:case
					case 64: 13#end:case
					else:
						(13 if (proc999_5 temp0 64 16384) else 0)
					#end:else
				#end:match
			)
		)
	#end:method

#end:class or instance

