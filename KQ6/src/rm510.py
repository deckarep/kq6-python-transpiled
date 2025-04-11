#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 510
import sci_sh
import Main
import KQ6Room
import n913
import Conversation
import Scaler
import PolyPath
import Polygon
import Feature
import Sound
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm510 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = -1
local4 = [0, 189, 0, 0, 187, 0, 187, 135, 211, 155, 216, 164, 209, 172, 121, 189]
local20 = [155, 189, 248, 182, 257, 174, 254, 165, 234, 152, 202, 136, 202, 0, 319, 0, 319, 189]
local38 = [0, 189, 0, 0, 50, 0, 82, 85, 41, 85, 68, 123, 159, 123, 176, 130, 209, 154, 218, 162, 211, 172, 120, 189]
local62 = [163, 189, 248, 177, 255, 167, 189, 131, 189, 123, 241, 123, 241, 105, 197, 97, 147, 86, 100, 86, 71, 0, 319, 0, 319, 189]
local88 = [0, 189, 0, 0, 319, 0, 319, 189, 165, 189, 177, 185, 232, 177, 252, 175, 253, 165, 229, 147, 180, 125, 243, 125, 243, 105, 210, 100, 145, 85, 37, 85, 67, 123, 160, 123, 179, 130, 216, 158, 216, 167, 205, 173, 125, 189]


@SCI.instance
class rm510(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 510
	horizon = 0
	north = 540
	south = 520
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (proc913_0 8):
			(self
				addObstacle:
					(poly1After type: 2 points: @local38 size: 12 yourself:)
					(poly2After type: 2 points: @local62 size: 13 yourself:)
			)
		else:
			(self
				addObstacle:
					(poly1Before type: 2 points: @local4 size: 8 yourself:)
					(poly2Before type: 2 points: @local20 size: 9 yourself:)
			)
		#endif
		(super init: &rest)
		if (global12 == north):
			(global0 init: reset: 2 posn: 102 99)
			(global103 number: 917 flags: 1 loop: -1 play:)
		else:
			(global0 init: reset: 3 posn: 146 187)
		#endif
		if (((global9 at: 2) owner:) == global11):
			(brick init:)
		#endif
		(archer init: ignoreActors: 1 setPri: 10)
		if (proc913_0 8):
			(archer setLoop: 6 ignoreActors: 1 addToPic:)
		#endif
		(statue2 init:)
		(wall init:)
		(roseFeature init:)
		(trees init:)
		(garden init:)
		(gazebo init:)
		(path init:)
		(rocks init:)
		(global0 setScale: Scaler 100 67 190 86 actions: egoUseShieldCode)
		(roses init: setPri: 5)
		if (proc913_0 9):
			(roses setLoop: 0 cel: 7 noun: 16 ignoreActors: 1 addToPic:)
		else:
			(roses setLoop: 2 cel: 0)
		#endif
		if (not (proc913_0 98)):
			(proc913_1 98)
			(genie init: setScript: genieSummoning)
			(glint1 init: hide:)
			(glint2 init: hide:)
			(genieSong play:)
		else:
			(global1 handsOn:)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case 
				(and
					(not (proc913_0 8))
					((global0 onControl: 1) == 2)
					(script != walkPastArcher)
					(script != walkPastArcherGenie)
					(not (global12 == north))
				):
				(global1 handsOff:)
				if (global5 contains: genie):
					(genie setScript: 0)
					(self setScript: walkPastArcherGenie)
				else:
					(self setScript: walkPastArcher 0 0)
				#endif
			#end:case
			case script: 0#end:case
			case (((global0 onControl: 1) == 128) and ((roses loop:) == 2)):
				(global1 handsOff:)
				(self setScript: rosesClose)
			#end:case
			case (((global0 onControl: 1) == 128) and ((roses loop:) == 0)):
				(global2 newRoom: north)
			#end:case
		)
		(super doit: &rest)
	#end:method

	@classmethod
	def newRoom(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (and (param1 == south) (not script) (global5 contains: genie)):
			(global1 handsOff:)
			(genie setScript: 0)
			(self setScript: genieMadScript 0 1)
		else:
			(super newRoom: param1)
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 == 1):
			if (global5 contains: genie):
				(theConv add: -1 noun param1 add: -1 noun param1 9 init:)
				return 1
			else:
				(super doVerb: param1 &rest)
			#endif
		else:
			(super doVerb: param1 &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class glint1(Prop):
	#property vars (may be empty)
	view = 902
	signal = 16384
	
#end:class or instance

@SCI.instance
class glint2(Prop):
	#property vars (may be empty)
	view = 902
	signal = 16384
	
#end:class or instance

@SCI.instance
class brick(View):
	#property vars (may be empty)
	x = 254
	y = 156
	noun = 5
	view = 510
	signal = 16384
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 == 5):
			(global0 setScript: getBrick)
		else:
			(super doVerb: param1 &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class genie(Actor):
	#property vars (may be empty)
	x = 214
	y = 101
	noun = 7
	view = 514
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 67:
				(global1 handsOff:)
				(genie setScript: 0)
				(global2 setScript: genieEatsPeppermint)
			#end:case
			case 2:
				if local0:
					(global1 handsOff:)
					(global2 setScript: interruptGenieScript 0 2)
				else:
					(global1 handsOff:)
					(global2 setScript: interruptGenieScript 0 1)
					local0++
				#endif
			#end:case
			case 5:
				(super doVerb: param1 &rest)
			#end:case
			case 1:
				(super doVerb: param1 &rest)
			#end:case
			else:
				(global1 handsOff:)
				(global2 setScript: interruptGenieScript 0 param1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class archer(Prop):
	#property vars (may be empty)
	x = 238
	y = 137
	z = 79
	noun = 10
	view = 510
	loop = 1
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (proc999_5 param1 1 5 2):
				if (proc913_0 8):
					(global91 say: noun param1 13 0)
				else:
					(global91 say: noun param1 14 0)
				#endif
			#end:case
			case (param1 == 17):
				(global1 handsOff:)
				(global2 setScript: walkPastArcher 0 1)
			#end:case
			case (param1 == 39):
				(global91 say: noun param1 0 0)
			#end:case
			case (proc913_0 8):
				(global91 say: noun 0 13 0)
			#end:case
			else:
				(global91 say: noun 0 14 0)
			#end:else
		)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super doit: &rest)
		if ((loop != 6) and (not (global2 script:))):
			(self
				cel:
					(-
						8
						(((GetAngle x y (global0 x:) (global0 y:)) - 105) / 17)
					)
			)
			if (cel != local3):
				(creak play:)
				local3 = cel
			#endif
		#endif
	#end:method

#end:class or instance

@SCI.instance
class fx(Sound):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class genieSong(Sound):
	#property vars (may be empty)
	flags = 1
	number = 510
	loop = -1
	
#end:class or instance

@SCI.instance
class creak(Sound):
	#property vars (may be empty)
	number = 513
	
#end:class or instance

@SCI.instance
class statue2(Feature):
	#property vars (may be empty)
	noun = 11
	onMeCheck = 4
	
#end:class or instance

@SCI.instance
class wall(Feature):
	#property vars (may be empty)
	noun = 4
	onMeCheck = 16
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (proc999_5 param1 1 5 2):
			(super doVerb: param1)
		else:
			(global91 say: 4 0 0 1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class path(Feature):
	#property vars (may be empty)
	noun = 6
	onMeCheck = 34
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (or (param1 == 1) (param1 == 5) (param1 == 2)):
			(super doVerb: param1)
		else:
			(global91 say: 6 0 0 1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class roses(Prop):
	#property vars (may be empty)
	x = 85
	y = 80
	noun = 15
	view = 513
	priority = 14
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (proc999_5 param1 1 2 5):
				(cond
					case 
						(not
							(or
								((roses loop:) == 0)
								(((roses loop:) == 2) and ((roses cel:) == 0))
							)
						):
						(global91 say: noun param1 0)
					#end:case
					case (noun == 16):
						(global91 say: noun param1 0)
					#end:case
					else:
						(gazebo doVerb: param1 &rest)
					#end:else
				)
			#end:case
			case (proc999_5 param1 28 39 8 30 25 12 94 70 71 26 20 34):
				(cond
					case 
						(not
							(or
								((roses loop:) == 0)
								(((roses loop:) == 2) and ((roses cel:) == 0))
							)
						):
						(global91 say: noun param1 0 0)
					#end:case
					case (noun == 16):
						(global91 say: noun 0 0)
					#end:case
					else:
						(gazebo doVerb: param1 &rest)
					#end:else
				)
			#end:case
			case (param1 == 16):
				(cond
					case 
						(not
							(or
								((roses loop:) == 0)
								(((roses loop:) == 2) and ((roses cel:) == 0))
							)
						):
						(global1 handsOff:)
						(global2 setScript: cutEmBaby)
					#end:case
					case (noun == 16):
						(global91 say: noun 0 0)
					#end:case
					else:
						(gazebo doVerb: param1 &rest)
					#end:else
				)
			#end:case
			case 
				(not
					(or
						((roses loop:) == 0)
						(((roses loop:) == 2) and ((roses cel:) == 0))
					)
				):
				(global91 say: noun 0 0)
			#end:case
			case (noun == 16):
				(global91 say: noun 0 0)
			#end:case
			else:
				(gazebo doVerb: param1 &rest)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class gazebo(Feature):
	#property vars (may be empty)
	noun = 13
	onMeCheck = 2048
	
#end:class or instance

@SCI.instance
class roseFeature(Feature):
	#property vars (may be empty)
	noun = 9
	onMeCheck = 64
	approachX = 51
	approachY = 89
	
	@classmethod
	def onMe():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (proc913_0 8):
			(self approachVerbs: 1 5)
		#endif
		return (super onMe: &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (param1 == 5):
				(cond
					case (global0 has: 38):
						(global91 say: noun param1 20)
					#end:case
					case (proc913_0 8):
						(global1 handsOff:)
						(global2 setScript: pickRoseScript)
					#end:case
					else:
						(global91 say: noun param1 14)
					#end:else
				)
			#end:case
			case (param1 == 16):
				if 
					(or
						((roses loop:) == 0)
						(((roses loop:) == 2) and ((roses cel:) == 0))
					)
					(global91 say: noun param1 17)
				else:
					(global91 say: noun param1 18)
				#endif
			#end:case
			case (proc999_5 param1 1 71 2):
				(super doVerb: param1 &rest)
			#end:case
			case (not (proc913_0 8)):
				(global91 say: noun 0 14)
			#end:case
			case (((roses loop:) == 2) and ((roses cel:) == (roses lastCel:))):
				(global91 say: noun 0 18)
			#end:case
			else:
				(global91 say: noun 0 17)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class garden(Feature):
	#property vars (may be empty)
	noun = 14
	onMeCheck = 256
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				if (proc913_0 8):
					(global91 say: noun param1 13)
				else:
					(global91 say: noun param1 14)
				#endif
			#end:case
			case 1:
				if (global5 contains: genie):
					(global91 say: noun param1 9)
				else:
					(global91 say: noun param1 8)
				#endif
			#end:case
			case 2:
				(super doVerb: param1 &rest)
			#end:case
			case 71:
				(global91 say: noun param1 0)
			#end:case
			else:
				if (proc913_0 8):
					(global91 say: noun 0 13)
				else:
					(global91 say: noun 0 14)
				#endif
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class trees(Feature):
	#property vars (may be empty)
	noun = 12
	onMeCheck = 512
	
#end:class or instance

@SCI.instance
class rocks(Feature):
	#property vars (may be empty)
	noun = 2
	onMeCheck = 1024
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (param1 == 1):
				(global91 say: noun param1 2 0 0 0)
			#end:case
			case (proc999_5 param1 1 2 5):
				(global91 say: noun param1 0 0 0 0)
			#end:case
			else:
				(global91 say: noun 0 0 0 0 0)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class interruptGenieScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				local1 = (genie script:)
				(genie script: 0)
				seconds = 2
			#end:case
			case 1:
				local2 = (genie loop:)
				(genie x: ((genie x:) - 9) y: ((genie y:) + 12) setLoop: 6)
				ticks = 1
			#end:case
			case 2:
				match register
					case 1:
						(global91 say: 7 2 15 0 self)
					#end:case
					case 2:
						(global91 say: 7 2 16 0 self)
					#end:case
					case 3:
						(global91 say: 1 0 3 0 self)
					#end:case
					case 4:
						(global91 say: 1 0 4 0 self)
					#end:case
					case 5:
						(global91 say: 1 0 5 1 self)
					#end:case
					case 6:
						(global91 say: 1 0 2 0 self)
					#end:case
					else:
						if (register == 43):
							(global91 say: 7 register 0 0 self)
						else:
							(global91 say: 7 0 0 0 self)
						#endif
					#end:else
				#end:match
			#end:case
			case 3:
				(glint1
					show:
					setPri: ((genie priority:) + 1)
					posn: ((genie x:) - 3) ((genie y:) - 17)
				)
				(glint2
					show:
					setPri: ((genie priority:) + 1)
					posn: ((genie x:) - 1) ((genie y:) - 17)
				)
				ticks = 1
			#end:case
			case 4:
				(glint1 setCycle: End self)
				(glint2 setCycle: End self)
			#end:case
			case 5: 0#end:case
			case 6:
				(glint1 setCycle: Beg self)
				(glint2 setCycle: Beg self)
			#end:case
			case 7: 0#end:case
			case 8:
				(glint1 hide:)
				(glint2 hide:)
				seconds = 2
			#end:case
			case 9:
				if (global5 contains: genie):
					(genie
						loop: local2
						x: ((genie x:) + 9)
						y: ((genie y:) - 12)
						script: local1
					)
				#endif
				local1 = 0
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genieMadScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(genie x: ((genie x:) - 9) y: ((genie y:) + 12) setLoop: 6)
				ticks = 1
			#end:case
			case 1:
				(global91 say: 1 0 5 1 self)
			#end:case
			case 2:
				(glint1
					show:
					setPri: ((genie priority:) + 1)
					posn: ((genie x:) - 3) ((genie y:) - 17)
				)
				(glint2
					show:
					setPri: ((genie priority:) + 1)
					posn: ((genie x:) - 1) ((genie y:) - 17)
				)
				ticks = 1
			#end:case
			case 3:
				(glint1 setCycle: End self)
				(glint2 setCycle: End self)
			#end:case
			case 4: 0#end:case
			case 5:
				(glint1 setCycle: Beg self)
				(glint2 setCycle: Beg self)
			#end:case
			case 6: 0#end:case
			case 7:
				(glint1 hide:)
				(glint2 hide:)
				seconds = 1
			#end:case
			case 8:
				(self setScript: genieOuttaHere self)
			#end:case
			case 9:
				(global91 say: 1 0 5 2 self)
			#end:case
			case 10:
				if register:
					(global2 newRoom: (global2 south:))
				else:
					(global1 handsOn:)
					(self dispose:)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getBrick(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 setMotion: PolyPath 251 160 self)
			#end:case
			case 1:
				cycles = 1
			#end:case
			case 2:
				(global0
					view: 511
					setLoop: 0
					cel: 0
					cycleSpeed: 10
					setHeading: 0
					normal: 0
					setCycle: CT 2 1 self
				)
			#end:case
			case 3:
				(brick dispose:)
				(global1 givePoints: 1)
				(global0 get: 2 setCycle: End self)
			#end:case
			case 4:
				(global0 setHeading: 180 reset:)
				seconds = 2
			#end:case
			case 5:
				(global1 handsOn:)
				(global91 say: 5 5)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walkPastArcher(Script):
	#property vars (may be empty)
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super doit:)
		if 
			(and
				register
				((global0 y:) < 160)
				(state == 1)
				((global0 view:) != 511)
			)
			(global0 normal: 0 view: 511 setLoop: 4)
		#endif
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				if register:
					(global91 say: 2 17 8 1 self)
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				if register:
					if ((global0 y:) < 160):
						(global0 normal: 0 view: 511 setLoop: 4)
					#endif
					(global0 setMotion: PolyPath 205 150 self)
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				(global0 view: 511 normal: 0 cycleSpeed: 10 cel: 0)
				if register:
					(global0 setLoop: 2)
				else:
					(global0
						setPri: 11
						posn: ((global0 x:) + 2) ((global0 y:) + 4)
						setLoop: 1
					)
				#endif
				cycles = 1
			#end:case
			case 3:
				if register:
					seconds = 2
				else:
					cycles = 1
				#endif
			#end:case
			case 4:
				(fx number: 511 loop: 1 play: self)
				(archer setCel: 0 cycleSpeed: 10 setLoop: 2 setCycle: End)
			#end:case
			case 5:
				if register:
					(fx number: 514 loop: 1 play:)
				else:
					(fx number: 512 loop: 1 play:)
				#endif
				(global0 setCycle: End self)
			#end:case
			case 6:
				if register:
					(global0 reset: 7 setCycle: Walk)
				#endif
				cycles = 1
			#end:case
			case 7:
				if register:
					(global91 say: 2 17 8 3 self)
				else:
					(global91 say: 1 0 7 4 self)
				#endif
			#end:case
			case 8:
				if register:
					(global1 givePoints: 3)
					(proc913_1 8)
					(global0 put: 43 510)
					(archer view: 510 setLoop: 6 setCel: 0)
					cycles = 1
					((global2 obstacles:)
						delete: poly1Before
						delete: poly2Before
						add:
							(poly1After
								type: 2
								points: @local38
								size: 12
								yourself:
							)
							(poly2After
								type: 2
								points: @local62
								size: 13
								yourself:
							)
					)
				else:
					(global1 handsOn:)
					(proc0_1 1)
				#endif
			#end:case
			case 9:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walkPastArcherGenie(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(proc913_1 163)
				(genie x: ((genie x:) - 9) y: ((genie y:) + 12) setLoop: 6)
				(global0
					view: 511
					normal: 0
					cycleSpeed: 10
					cel: 0
					setPri: 11
					posn: ((global0 x:) + 2) ((global0 y:) + 4)
					setLoop: 1
				)
				cycles = 1
			#end:case
			case 1:
				(fx number: 511 loop: 1 play: self)
				(archer setCel: 0 cycleSpeed: 10 setLoop: 2 setCycle: End)
			#end:case
			case 2:
				(fx number: 512 loop: 1 play:)
				(global0 setCycle: End self)
			#end:case
			case 3:
				(genie cycleSpeed: 15 setLoop: 7 setCycle: End self)
			#end:case
			case 4:
				(genie setLoop: 8 cel: 0 setCycle: End self)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				(genie setCycle: Beg self)
			#end:case
			case 7:
				cycles = 2
			#end:case
			case 8:
				(genie setCycle: End self)
			#end:case
			case 9:
				cycles = 2
			#end:case
			case 10:
				(genie setCycle: Beg self)
			#end:case
			case 11:
				cycles = 2
			#end:case
			case 12:
				(genie setCycle: End self)
			#end:case
			case 13:
				cycles = 2
			#end:case
			case 14:
				(genie setCycle: Beg self)
			#end:case
			case 15:
				cycles = 2
			#end:case
			case 16:
				(glint1
					show:
					setPri: ((genie priority:) + 1)
					posn: ((genie x:) + 1) ((genie y:) - 41)
					setCycle: End self
				)
				(glint2
					show:
					setPri: ((genie priority:) + 1)
					posn: ((genie x:) - 1) ((genie y:) - 41)
					setCycle: End self
				)
			#end:case
			case 17: 0#end:case
			case 18:
				(glint1 setCycle: Beg self)
				(glint2 setCycle: Beg self)
			#end:case
			case 19: 0#end:case
			case 20:
				(glint1 hide:)
				(glint2 hide:)
				cycles = 2
			#end:case
			case 21:
				(global91 say: 1 0 6 5 self)
			#end:case
			case 22:
				(global1 handsOn:)
				(proc0_1 1)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genieEatsPeppermint(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(genie setLoop: 7 setCel: 0 setCycle: End self)
			#end:case
			case 1:
				(genie setLoop: 8 setCel: 0)
				cycles = 2
			#end:case
			case 2:
				(theConv add: -1 7 67 0 1 init: self)
			#end:case
			case 3:
				(glint1
					show:
					setPri: ((genie priority:) + 1)
					posn: ((genie x:) - 1) ((genie y:) - 41)
				)
				(glint2
					show:
					setPri: ((genie priority:) + 1)
					posn: ((genie x:) + 1) ((genie y:) - 41)
				)
				ticks = 1
			#end:case
			case 4:
				(glint1 setCycle: End self)
				(glint2 setCycle: End self)
			#end:case
			case 5: 0#end:case
			case 6:
				(glint1 setCycle: Beg self)
				(glint2 setCycle: Beg self)
			#end:case
			case 7: 0#end:case
			case 8:
				(glint1 hide:)
				(glint2 hide:)
				seconds = 2
			#end:case
			case 9:
				(theConv
					add: -1 7 67 0 2
					add: -1 7 67 0 3
					add: -1 7 67 0 4
					init: self
				)
			#end:case
			case 10:
				(fx number: 943 loop: 1 play:)
				(genie cycleSpeed: 3 setLoop: 5 setCycle: End self)
			#end:case
			case 11:
				(genie
					posn: ((global0 x:) + 33) ((global0 y:) - 5)
					setCycle: Beg self
				)
				(fx number: 943 loop: 1 play:)
			#end:case
			case 12:
				(proc913_4 global0 genie self)
			#end:case
			case 13:
				(global0 normal: 0 view: 514 setLoop: 11 cel: 0)
				cycles = 2
			#end:case
			case 14:
				(theConv add: -1 7 67 0 5 add: -1 7 67 0 6 init: self)
			#end:case
			case 15:
				(genie cycleSpeed: 15 setLoop: 10 cel: 0 setCycle: CT 2 1 self)
				(global0 cel: 1)
			#end:case
			case 16:
				(genie setCycle: End self)
				(global0 put: 31 0 cel: 0)
			#end:case
			case 17:
				(genie cycleSpeed: 3 setLoop: 5 setCycle: End self)
				(fx number: 943 loop: 1 play:)
			#end:case
			case 18:
				(genie dispose:)
				(genieSong fade:)
				(global0 normal: 1 reset:)
				ticks = 1
			#end:case
			case 19:
				(theConv add: -1 7 67 0 7 init: self)
			#end:case
			case 20:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genieDigging(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(genie setLoop: 0 cycleSpeed: 10 setCycle: Fwd)
				seconds = 4
			#end:case
			case 1:
				(genie setCycle: End self)
			#end:case
			case 2:
				(genie setLoop: 1 setCycle: Fwd)
				seconds = 4
			#end:case
			case 3:
				(genie setCycle: End self)
			#end:case
			case 4:
				(genie setLoop: 2 setCycle: Fwd)
				seconds = 4
			#end:case
			case 5:
				(genie setCycle: End self)
			#end:case
			case 6:
				(self init:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genieSummoning(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(self setScript: genieDigging)
				(global1 handsOff:)
				(global2 setScript: interruptGenieScript self 6)
			#end:case
			case 1:
				seconds = 30
			#end:case
			case 2:
				(global1 handsOff:)
				(global2 setScript: interruptGenieScript self 3)
			#end:case
			case 3:
				seconds = 30
			#end:case
			case 4:
				(global1 handsOff:)
				(global2 setScript: interruptGenieScript self 4)
			#end:case
			case 5:
				seconds = 30
			#end:case
			case 6:
				if (not (global2 script:)):
					(global1 handsOff:)
					(genie setScript: 0)
					(global2 setScript: genieMadScript 0 0)
				else:
					cycles = 1
				#endif
			#end:case
			case 7:
				(self start: 6 init:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genieOuttaHere(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(genie cycleSpeed: 15 setLoop: 7 setCycle: End self)
			#end:case
			case 1:
				(genie setLoop: 8 cel: 0 setCycle: End self)
			#end:case
			case 2:
				(genie setCycle: Beg self)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				(genie setCycle: End self)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				(genie setCycle: Beg self)
			#end:case
			case 7:
				cycles = 2
			#end:case
			case 8:
				(genie setCycle: End self)
			#end:case
			case 9:
				cycles = 2
			#end:case
			case 10:
				(fx number: 943 loop: 1 play:)
				(genie cycleSpeed: 3 setLoop: 5 setCycle: End self)
			#end:case
			case 11:
				(genieSong fade:)
				(genie dispose:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class rosesClose(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global91 say: 1 0 21 1 self)
			#end:case
			case 1:
				(fx number: 484 loop: 1 play:)
				(roses setCycle: CT 11 1 self)
			#end:case
			case 2:
				(roses setLoop: 1)
				((global2 obstacles:)
					delete: poly1After
					delete: poly2After
					add: (polyHedge type: 2 points: @local88 size: 23 yourself:)
				)
				(global91 say: 1 0 21 2 self)
			#end:case
			case 3:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class cutEmBaby(Script):
	#property vars (may be empty)
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super doit:)
		if 
			(and
				(proc999_5 state 2 4 5 7 8)
				(register != (global0 cel:))
				(proc999_5 (global0 cel:) 0 2 4 6)
			)
			register = (global0 cel:)
			(fx play:)
		#endif
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				register = -1
				(fx number: 516 loop: 1)
				(global1 givePoints: 3)
				(global0 setMotion: PolyPath 90 88 self)
			#end:case
			case 1:
				(global91 say: 15 16 0 1 self)
			#end:case
			case 2:
				(roses cycleSpeed: 50 setLoop: 0 cel: 0 setCycle: CT 8 1)
				(global0
					view: 531
					normal: 0
					setLoop: 0
					cel: 0
					cycleSpeed: 12
					setCycle: End self
				)
			#end:case
			case 3:
				(global91 say: 15 16 0 2 self)
			#end:case
			case 4:
				(global0 setLoop: 1 setCycle: End self)
			#end:case
			case 5:
				(global0 setLoop: 0 setCycle: End self)
			#end:case
			case 6:
				(global91 say: 15 16 0 3 self)
			#end:case
			case 7:
				(global0 setLoop: 1 setCycle: End self)
			#end:case
			case 8:
				(global0 setLoop: 0 setCycle: End self)
			#end:case
			case 9:
				cycles = 7
			#end:case
			case 10:
				(global91 say: 15 16 0 4 self)
			#end:case
			case 11:
				(global0 reset: 3)
				(proc913_1 9)
				cycles = 1
			#end:case
			case 12:
				(global0
					ignoreHorizon: 1
					ignoreActors: 1
					setMotion:
						MoveTo
						((global0 x:) - 10)
						((global0 y:) - 10)
						self
				)
			#end:case
			case 13:
				(global0 setMotion: MoveTo ((global0 x:) - 5) (global0 y:) self)
			#end:case
			case 14:
				(global2 newRoom: 540)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class pickRoseScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0
					view: 531
					normal: 0
					setLoop: 2
					cel: 0
					setCycle: End self
				)
			#end:case
			case 1:
				(global0 get: 38 reset: 5)
				cycles = 1
			#end:case
			case 2:
				if (not (proc913_1 137)):
					(global1 givePoints: 1)
				#endif
				(global1 handsOn:)
				(global91 say: 9 5 13)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class theConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class egoUseShieldCode(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 17:
				(global1 handsOff:)
				(global2 setScript: walkPastArcher 0 1)
				return 1
			#end:case
		#end:match
		return 0
	#end:method

#end:class or instance

@SCI.instance
class poly1Before(Polygon):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class poly2Before(Polygon):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class poly1After(Polygon):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class poly2After(Polygon):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class polyHedge(Polygon):
	#property vars (may be empty)
#end:class or instance

