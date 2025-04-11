#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 405
import sci_sh
import Main
import rLab
import n402
import n913
import Conversation
import Scaler
import Polygon
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm405 = 0,
)

@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class rm405(LabRoom):
	#property vars (may be empty)
	north = 400
	west = 400
	
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
							149
							148
							102
							148
							83
							142
							83
							152
							74
							160
							0
							160
							0
							0
							149
							0
						yourself:
					)
					((Polygon new:)
						type: 2
						init:
							172
							148
							171
							0
							319
							0
							319
							189
							180
							189
							180
							185
							294
							185
							231
							142
							211
							148
						yourself:
					)
					((Polygon new:)
						type: 2
						init: 64 168 54 176 17 185 140 185 140 189 0 189 0 168
						yourself:
					)
			)
		else:
			(proc402_2)
		#endif
		((ScriptID 30 0) labCoords: 117)
		(super init: &rest)
		if ((not (proc913_0 1)) and (global12 != 400)):
			(self setScript: closeEntranceDoor)
		else:
			if (global12 != 400):
				((ScriptID 30 0) prevEdgeHit: 1)
			#endif
			(global2 setScript: (ScriptID 30 1))
		#endif
		((ScriptID 30 0) initCrypt: 2)
		((ScriptID 30 7) addToPic:)
		((ScriptID 30 5) addToPic:)
		((ScriptID 30 9) addToPic:)
		(door addToPic:)
		(lBlock addToPic:)
		(rBlock addToPic:)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (global2 script:):#end:case
			case ((global0 edgeHit:) == 3):
				((ScriptID 30 0) prevEdgeHit: 3)
				(global2 setScript: walkOut)
			#end:case
		)
		(super doit:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				if (proc913_0 1):
					(global91 say: 2 1 14 1 0 400)
				else:
					(global91 say: 2 1 15 1 0 400)
				#endif
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class door(Prop):
	#property vars (may be empty)
	y = 190
	noun = 11
	modNum = 400
	sightAngle = 45
	approachX = 160
	approachY = 178
	view = 400
	priority = 15
	signal = 16400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self approachVerbs: 5)
		if (proc913_0 1):
			(self x: 259)
		else:
			(self x: 160)
		#endif
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				if (not (proc913_0 1)):
					(global91 say: 11 5 15 1 0 400)
				else:
					(global91 say: 11 5 14 1 0 400)
				#endif
			#end:case
			case 1:
				if (proc913_0 1):
					(global91 say: 11 1 14 1 0 400)
				else:
					(global91 say: 11 1 15 1 0 400)
				#endif
			#end:case
			case 2:
				(super doVerb: param1 &rest)
			#end:case
			else:
				if (proc913_0 1):
					(global91 say: 11 0 14 1 0 400)
				else:
					(global91 say: 11 0 15 1 0 400)
				#endif
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lBlock(View):
	#property vars (may be empty)
	x = 123
	y = 189
	noun = 6
	modNum = 400
	view = 408
	loop = 1
	priority = 15
	signal = 20496
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				(myConv add: 400 6 1 9 1 add: 400 6 1 9 2 init:)
			#end:case
			else:
				(super doVerb: param1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class rBlock(View):
	#property vars (may be empty)
	x = 273
	y = 189
	noun = 6
	modNum = 400
	view = 408
	loop = 2
	priority = 15
	signal = 16400
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(lBlock doVerb: param1)
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
				(global0 setMotion: MoveTo (global0 x:) 250 self)
			#end:case
			case 1:
				(global2 newRoom: 340)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class closeEntranceDoor(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					posn: 158 250
					normal: 1
					init:
					reset:
					setScale: Scaler 100 99 190 0
					ignoreHorizon:
					setMotion: MoveTo 160 165 self
				)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				(global105 number: 434 setLoop: 1 play: self)
			#end:case
			case 3:
				if (not (proc913_0 1)):
					(global91 say: 1 0 11 0 self 400)
				else:
					(self cue:)
				#endif
			#end:case
			case 4:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

