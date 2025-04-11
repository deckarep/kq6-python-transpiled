#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 440
import sci_sh
import Main
import minoTrigger
import KQ6Room
import n913
import Conversation
import RandCycle
import PolyPath
import Polygon
import Feature
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm440 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None


@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class rm440(KQ6Room):
	#property vars (may be empty)
	picture = 440
	style = 10
	walkOffEdge = 1
	autoLoad = 0
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((not (proc913_0 1)) and (not ((ScriptID 30 0) seenByMino:))):
			(proc441_0)
		#endif
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (proc913_0 1):
			(global2
				addObstacle:
					((Polygon new:)
						type: 2
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
		else:
			(Load 130 441)
			(global2
				addObstacle:
					((Polygon new:)
						type: 2
						init: 295 0 40 179 0 179 0 0
						yourself:
					)
					((Polygon new:)
						type: 2
						init: 0 185 152 185 151 189 0 189
						yourself:
					)
			)
		#endif
		(super init: &rest)
		((ScriptID 30 0) cue:)
		(flames setCycle: RandCycle init:)
		(global32
			add: alter toLabExit exitSkull alterSkulls toCliffsExit
			eachElementDo: #init
		)
		if (proc913_0 1):
			local0 = 7
		else:
			(proc441_1)
			local2 = 8
			local0 = 6
		#endif
		(global0 init: reset: actions: egoDoMinotaurCode)
		(self setScript: walkIn)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(actTimer dispose:)
		(DisposeScript 441)
		(super dispose:)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (self script:):#end:case
			case 
				(and
					(not ((ScriptID 30 0) seenByMino:))
					(not (proc913_0 1))
					((global0 onControl: 1) == 4)
				):
				(proc441_2)
			#end:case
			case ((global0 onControl: 1) == 256):
				(self setScript: fallInPit)
			#end:case
			case ((global0 onControl: 1) == 16384):
				(global2 setScript: walkOut 0 0)
			#end:case
			case ((global0 onControl: 1) == 8192):
				if (proc913_0 1):
					(global2 setScript: walkOut 0 1)
				else:
					(global0 setMotion: 0 posn: ((global0 x:) + 2) (global0 y:))
					(global91 say: 11 3 8 1)
				#endif
			#end:case
		)
		(super doit: &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			match param1
				case 1:
					(global91 say: 2 1 local0 1)
					1
				#end:case
				case 5:
					(global91 say: 2 5 local0 1)
					1
				#end:case
				case 2:
					(cond
						case (proc913_0 1):
							(global91 say: 2 2 7 1)
						#end:case
						case ((ScriptID 30 0) seenByMino:):
							(global91 say: 2 2 9 1)
						#end:case
						else:
							(global91 say: 2 2 8 0 self)
						#end:else
					)
					1
				#end:case
				else:
					(global91 say: 2 0 local0 1 self)
					1
				#end:else
			#end:match
		)
	#end:method

#end:class or instance

@SCI.instance
class alter(Feature):
	#property vars (may be empty)
	x = 60
	y = 110
	noun = 12
	onMeCheck = 4096
	
#end:class or instance

@SCI.instance
class toLabExit(Feature):
	#property vars (may be empty)
	x = 10
	y = 170
	noun = 11
	onMeCheck = 1024
	
#end:class or instance

@SCI.instance
class toCliffsExit(Feature):
	#property vars (may be empty)
	x = 330
	y = 140
	noun = 9
	onMeCheck = 8192
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				(global91 say: 9 1 local0 1 0 440)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class alterSkulls(Feature):
	#property vars (may be empty)
	x = 60
	y = 110
	noun = 13
	onMeCheck = 2048
	
#end:class or instance

@SCI.instance
class exitSkull(Feature):
	#property vars (may be empty)
	x = 330
	y = 140
	noun = 10
	onMeCheck = 512
	
#end:class or instance

@SCI.instance
class flames(Prop):
	#property vars (may be empty)
	x = 203
	y = 147
	noun = 6
	view = 445
	priority = 1
	signal = 16400
	cycleSpeed = 8
	detailLevel = 3
	
#end:class or instance

@SCI.instance
class walkIn(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				if (global12 == 340):
					(global0 posn: 310 160 setMotion: PolyPath 230 160 self)
				else:
					(global0 posn: -5 187 setMotion: MoveTo 38 184 self)
				#endif
			#end:case
			case 1:
				if (proc913_0 1):
					(self cue:)
				else:
					(global102 number: 440 setLoop: -1 play:)
					(global0 setHeading: 0)
					(proc913_1 161)
					(global105 number: 433 setLoop: 1 play:)
					cycles = 10
				#endif
			#end:case
			case 2:
				if (not (proc913_0 1)):
					if (proc913_0 142):
						(global91 say: 1 0 19 0 self 440)
					else:
						(global91 say: 1 0 1 0 self 440)
					#endif
				else:
					(self cue:)
				#endif
			#end:case
			case 3:
				(global1 handsOn:)
				if (not (proc913_0 1)):
					((ScriptID 30 0) setScript: actTimer)
				#endif
				(self dispose:)
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
				if register:
					(global0 setMotion: PolyPath 315 (global0 y:) self)
				else:
					(global0 setMotion: MoveTo -15 (global0 y:) self)
				#endif
			#end:case
			case 1:
				(global1 handsOn:)
				if register:
					(global2 newRoom: 340)
				else:
					((ScriptID 30 0) prevEdgeHit: 4)
					(global2 newRoom: 409)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class fallInPit(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					view: 441
					normal: 0
					setLoop: (5 if ((global0 x:) < 185) else 4)
					cel: 0
					setMotion: 0
					cycleSpeed: 2
				)
				cycles = 6
			#end:case
			case 1:
				(global91 say: 6 3 0 1 self)
			#end:case
			case 2:
				(global91 say: 6 3 0 2 self)
			#end:case
			case 3:
				(global0
					setPri: (2 if ((global0 x:) < 185) else -1)
					setCycle: End
				)
				(global102 stop:)
				(global105 number: 442 setLoop: 1 play: self)
			#end:case
			case 4:
				ticks = 4
			#end:case
			case 5:
				seconds = 2
			#end:case
			case 6:
				(proc0_1 15)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class actTimer(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				seconds = 20
			#end:case
			case 1:
				(global91 say: 1 0 18 1 self)
			#end:case
			case 2:
				(proc441_0)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoDoMinotaurCode(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				return 0
			#end:case
			case 1:
				return 0
			#end:case
			case 2:
				return 0
			#end:case
			case 17:
				if (proc913_0 1):
					(global91 say: 3 17 7 1)
				else:
					(global91 say: 3 17 6 1)
				#endif
				return 1
			#end:case
			case 72:
				if ((global2 script:) == (ScriptID 441 3)):
					((ScriptID 30 0) scarfOnMino: 1)
					(global0 view: 441 normal: 0 setLoop: 0 cel: 0)
					(UnLoad 128 900)
					((ScriptID 441 4) cycleSpeed: 6 setCycle: Fwd)
					((ScriptID 441 3) state: 19 register: 72 cue:)
					(global1 handsOff:)
					(global1 givePoints: 3)
				#endif
			#end:case
			else:
				if (not (proc913_0 1)):
					(global91 say: 3 0 6 1)
					return 1
				else:
					(global91 say: 0 0 184 1 0 899)
					return 1
				#endif
			#end:else
		#end:match
	#end:method

#end:class or instance

