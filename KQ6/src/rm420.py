#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 420
import sci_sh
import kernel
import Main
import rLab
import KQ6Room
import Conversation
import Scaler
import PolyPath
import Polygon
import Feature
import LoadMany
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm420 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class rm420(KQ6Room):
	#property vars (may be empty)
	noun = 2
	picture = 420
	style = 10
	walkOffEdge = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global2
			addObstacle:
				((Polygon new:)
					type: 3
					init:
						194
						120
						122
						120
						116
						122
						54
						122
						50
						125
						110
						125
						96
						130
						96
						150
						221
						150
						220
						132
						204
						125
						245
						125
						243
						122
						198
						122
					yourself:
				)
		)
		(super init: &rest)
		proc958_0(128, 421)
		(global0 init: setScale: Scaler 100 60 128 100 actions: egoDoCrushCode)
		(kernel.ScriptID(30, 0) cue:)
		(global32 add: floor walls exits eachElementDo: #init)
		if local0 = (((global9 at: 2) owner:) == global11):
			local1 = 5
			(theBrick addToPic:)
			(gears addToPic:)
			(ceiling addToPic:)
		else:
			local1 = 4
			(eastDoor init:)
			(westDoor init:)
			(gears init: stopUpd:)
			(ceiling init: stopUpd:)
		#endif
		if (not (rLab prevEdgeHit:)):
			(rLab prevEdgeHit: 2)
		#endif
		(self setScript: walkIn)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (self script:):#end:case
			case ((global0 onControl: 1) == 16384):
				(kernel.ScriptID(30, 0) prevEdgeHit: 2)
				(self setScript: walkOut)
			#end:case
			case ((global0 onControl: 1) == 8192):
				(kernel.ScriptID(30, 0) prevEdgeHit: 4)
				(self setScript: walkOut)
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
					(global91 say: 2 1 local1 1)
					1
				#end:case
				case 2:
					if local0:
						(global91 say: 2 2 local1 1)
						1
					else:
						(myConv add: -1 2 2 local1 1 add: -1 2 2 local1 2 init:)
						1
					#endif
				#end:case
				case 5:
					(global91 say: 2 5 local1 1)
					1
				#end:case
				else:
					(global91 say: 2 0 local1 1)
					1
				#end:else
			#end:match
		)
	#end:method

	@classmethod
	def scriptCheck():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 1
		if (not local0):
			(global91 say: 0 0 164 1 0 899)
			temp0 = 0
		#endif
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class floor(Feature):
	#property vars (may be empty)
	noun = 8
	onMeCheck = 2048
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global91 say: 8 5 local1 1)
			#end:case
			case 1:
				(global91 say: 8 1 0 1)
			#end:case
			case 2:
				(global91 say: 8 2 local1 0)
			#end:case
			else:
				(global91 say: 2 0 local1 1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walls(Feature):
	#property vars (may be empty)
	noun = 7
	onMeCheck = 1024
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				(global91 say: 7 1 local1 1)
			#end:case
			case 5:
				(global91 say: 7 5 local1 1)
			#end:case
			case 2:
				if local0:
					(global91 say: 2 2 local1 0)
				else:
					(global91 say: 7 2 local1 0)
				#endif
			#end:case
			else:
				(global91 say: 2 0 local1 1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class exits(Feature):
	#property vars (may be empty)
	onMeCheck = 4096
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(westDoor doVerb: param1 &rest)
	#end:method

#end:class or instance

@SCI.instance
class gears(Prop):
	#property vars (may be empty)
	x = 160
	y = 118
	noun = 6
	view = 424
	loop = 1
	signal = 16400
	cycleSpeed = 18
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				(global91 say: 6 1 local1 1)
			#end:case
			case 5:
				(global91 say: 6 5 local1 1)
			#end:case
			case 2:
				(global91 say: 6 2 local1 1)
			#end:case
			case 39:
				(global2 setScript: useBrick)
			#end:case
			case 51:
				if local0:
					(global91 say: 6 0 local1 1)
				else:
					(global2 setScript: throwSkull)
				#endif
			#end:case
			case 17:
				if local0:
					(global91 say: 6 0 local1 1)
				else:
					(global91 say: 6 17 local1 1)
				#endif
			#end:case
			case 28:
				if local0:
					(global91 say: 6 0 local1 1)
				else:
					(global91 say: 6 28 local1 1)
				#endif
			#end:case
			case 36:
				if local0:
					(global91 say: 6 0 local1 1)
				else:
					(global91 say: 6 36 local1 1)
				#endif
			#end:case
			case 42:
				if local0:
					(global91 say: 6 0 local1 1)
				else:
					(global91 say: 6 42 local1 1)
				#endif
			#end:case
			case 20:
				if local0:
					(global91 say: 6 0 local1 1)
				else:
					(global91 say: 6 20 local1 1)
				#endif
			#end:case
			case 34:
				if local0:
					(global91 say: 6 0 local1 1)
				else:
					(global91 say: 6 34 local1 1)
				#endif
			#end:case
			case 94:
				if local0:
					(global91 say: 6 0 local1 1)
				else:
					(global91 say: 6 94 local1 1)
				#endif
			#end:case
			else:
				(global91 say: 6 0 local1 1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class ceiling(Prop):
	#property vars (may be empty)
	x = 162
	y = 71
	noun = 4
	view = 424
	priority = 7
	signal = 20496
	cycleSpeed = 12
	
	@classmethod
	def addToPic():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self
			y: (kernel.ScriptID(30, 0) crushCeilingY:)
			cel: (kernel.ScriptID(30, 0) crushCeilingCel:)
		)
		(super addToPic:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				(global91 say: 4 1 local1 1)
			#end:case
			case 5:
				(global91 say: 4 5 local1 1)
			#end:case
			case 2:
				(global91 say: 4 2 local1 1)
			#end:case
			case 51:
				if local0:
					(global91 say: 4 0 local1 1)
				else:
					(global91 say: 4 51 local1 1)
				#endif
			#end:case
			case 17:
				if local0:
					(global91 say: 4 0 local1 1)
				else:
					(global91 say: 4 17 local1 1)
				#endif
			#end:case
			case 28:
				if local0:
					(global91 say: 4 0 local1 1)
				else:
					(global91 say: 4 28 local1 1)
				#endif
			#end:case
			case 94:
				if local0:
					(global91 say: 4 0 local1 1)
				else:
					(global91 say: 4 94 local1 1)
				#endif
			#end:case
			case 12:
				(global91 say: 4 12 0 1)
			#end:case
			else:
				(global91 say: 4 0 local1 1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class westDoor(Prop):
	#property vars (may be empty)
	x = 101
	y = 71
	noun = 5
	view = 424
	loop = 2
	signal = 20480
	cycleSpeed = 4
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				(global91 say: 5 1 local1 1)
			#end:case
			case 5:
				(global91 say: 5 5 local1 1)
			#end:case
			case 2:
				(super doVerb: param1 &rest)
			#end:case
			else:
				(global91 say: 5 0 local1 1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class eastDoor(Prop):
	#property vars (may be empty)
	x = 211
	y = 70
	noun = 5
	view = 424
	loop = 3
	signal = 20480
	cycleSpeed = 3
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(westDoor doVerb: param1 &rest)
	#end:method

#end:class or instance

@SCI.instance
class theBrick(Prop):
	#property vars (may be empty)
	noun = 10
	view = 424
	loop = 5
	signal = 16384
	cycleSpeed = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (((global9 at: 2) owner:) == global11):
			(self x: 169 y: 119 z: 32)
		else:
			(self x: 169 y: 118)
		#endif
		(super init:)
	#end:method

#end:class or instance

@SCI.instance
class theSkull(Prop):
	#property vars (may be empty)
	x = 166
	y = 118
	view = 424
	loop = 4
	cycleSpeed = 1
	
#end:class or instance

@SCI.instance
class cog(Prop):
	#property vars (may be empty)
	x = 182
	y = 133
	view = 423
	signal = 16384
	cycleSpeed = 5
	
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
				(global69 disable: 6)
				match (rLab prevEdgeHit:)
					case 2:
						(global0 edgeHit: 2 setMotion: MoveTo 232 123 self)
					#end:case
					case 4:
						(global0 edgeHit: 4 setMotion: MoveTo 82 123 self)
					#end:case
				#end:match
			#end:case
			case 1:
				(global2 newRoom: 400)
			#end:case
		#end:match
	#end:method

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
				match (rLab prevEdgeHit:)
					case 4:
						(global0 posn: 232 123 setMotion: PolyPath 194 123 self)
					#end:case
					case 2:
						(global0 posn: 82 123 setMotion: PolyPath 122 123 self)
					#end:case
				#end:match
			#end:case
			case 1:
				if local0:
					(global1 handsOn:)
					(self dispose:)
				else:
					(global0 setPri: 14 setMotion: PolyPath 152 134 self)
				#endif
			#end:case
			case 2:
				(global0 setHeading: 90)
				(eastDoor setCycle: End)
				(westDoor setCycle: End self)
				(global105 number: 426 setLoop: 1 play:)
			#end:case
			case 3:
				(global1 handsOn:)
				(global69 enable: 6 disable: 0)
				(global102 number: 420 setLoop: -1 play: self)
				(global103 number: 421 setLoop: -1 play: self)
				ticks = 4
			#end:case
			case 4:
				(eastDoor stopUpd:)
				(westDoor stopUpd:)
				(global91 say: 1 0 1 1 self)
			#end:case
			case 5:
				(ceiling startUpd: y: ((ceiling y:) + 1))
				(gears setCycle: Fwd)
				cycles = 4
			#end:case
			case 6:
				(global91 say: 1 0 1 2 self)
			#end:case
			case 7:
				(self setScript: dropCeiling self 1)
			#end:case
			case 8:
				(ceiling stopUpd:)
				seconds = 1
			#end:case
			case 9:
				(global2 setScript: sqwishEm)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class dropCeiling(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(ceiling startUpd: y: ((ceiling y:) + 1))
				seconds = 2
			#end:case
			case 1:
				if (register == 1):
					temp0 = 85
				else:
					temp0 = 91
				#endif
				if ((ceiling y:) < temp0):
					(self changeState: 0)
				else:
					(self dispose:)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class throwSkull(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91 say: 6 51 4 1 self)
			#end:case
			case 1:
				(global0 view: 421 normal: 0 setLoop: 1 cel: 4 posn: 162 146)
				ticks = 4
			#end:case
			case 2:
				(global0 cel: 5)
				(theSkull init:)
				ticks = 4
			#end:case
			case 3:
				(global0 cel: 6)
				ticks = 4
			#end:case
			case 4:
				(global0 cel: 7)
				(theSkull posn: 161 124)
				(theSkull posn: ((theSkull x:) - 8) ((theSkull y:) + 6))
				ticks = 4
			#end:case
			case 5:
				(global0 cel: 8)
				(theSkull
					setPri: 11
					posn: ((theSkull x:) - 10) ((theSkull y:) - 3)
				)
				ticks = 4
			#end:case
			case 6:
				(global0 cel: 9)
				(theSkull
					setPri: -1
					posn: ((theSkull x:) + 26) ((theSkull y:) - 3)
				)
				ticks = 4
			#end:case
			case 7:
				(global0 cel: 10)
				(theSkull posn: ((theSkull x:) - 5) ((theSkull y:) - 18))
				ticks = 2
			#end:case
			case 8:
				(theSkull cel: 1 posn: ((theSkull x:) + 1) ((theSkull y:) - 6))
				ticks = 2
			#end:case
			case 9:
				(theSkull cel: 2 posn: ((theSkull x:) + 1) ((theSkull y:) - 5))
				ticks = 2
			#end:case
			case 10:
				(theSkull cel: 3 posn: ((theSkull x:) + 1) ((theSkull y:) - 7))
				ticks = 2
			#end:case
			case 11:
				(theSkull cel: 0 posn: ((theSkull x:) + 1) ((theSkull y:) - 5))
				ticks = 2
			#end:case
			case 12:
				(theSkull cel: 1 posn: ((theSkull x:) + 1) ((theSkull y:) + 2))
				ticks = 2
			#end:case
			case 13:
				(theSkull cel: 2 posn: ((theSkull x:) + 1) ((theSkull y:) + 2))
				ticks = 2
			#end:case
			case 14:
				(theSkull cel: 3 posn: ((theSkull x:) + 1) ((theSkull y:) + 1))
				ticks = 2
			#end:case
			case 15:
				(global102 stop:)
				(global103 stop:)
				(global105 number: 422 setLoop: 1 play: self)
				(global104 number: 424 setLoop: 1 play:)
				(theSkull cel: 0 posn: ((theSkull x:) + 1) ((theSkull y:) + 4))
			#end:case
			case 16:
				(theSkull posn: ((theSkull x:) - 1) ((theSkull y:) - 1))
				(global91 say: 6 51 4 2 self)
			#end:case
			case 17:
				(gears setCycle: 0 stopUpd:)
				(global0 reset: 0 posn: 155 134)
				(global91 say: 6 51 4 3 self)
			#end:case
			case 18:
				(global91 say: 6 51 4 4 self)
			#end:case
			case 19:
				seconds = 2
			#end:case
			case 20:
				(theSkull setLoop: 6 setCycle: End self)
				(global105 number: 423 setLoop: 1 play: self)
			#end:case
			case 21:
				(global102 number: 420 setLoop: -1 play: self)
				(global103 number: 421 setLoop: -1 play: self)
			#end:case
			case 22:
				(gears setCycle: Fwd)
				(global91 say: 6 51 4 5 self)
			#end:case
			case 23:
				(theSkull dispose:)
				(global69 disable: 0)
				(global0 put: 11 global11)
				(ceiling y: 84)
				seconds = 2
			#end:case
			case 24:
				(global2 setScript: sqwishEm 0 1)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class sqwishEm(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91 say: 1 0 3 1 self)
			#end:case
			case 1:
				(ceiling setPri: 12 setCycle: CT 3 1 self)
				(global0
					view: 421
					normal: 0
					setLoop: 2
					cel: 0
					cycleSpeed: 6
					setPri: 14
					posn: ((global0 x:) - 2) ((global0 y:) + 4)
					setCycle: End self
				)
			#end:case
			case 2:
				(ceiling cel: ((ceiling cel:) + 1))
				(global0 setPri: 13 setLoop: 3 cel: 0 setCycle: End self)
			#end:case
			case 3:
				(ceiling cel: ((ceiling cel:) + 1))
				(global0 setLoop: 4 cel: 0 setCycle: CT 4 1 self)
			#end:case
			case 4:
				(global91 say: 1 0 3 2 self)
			#end:case
			case 5:
				(ceiling setPri: 14 cel: ((ceiling cel:) + 1))
				(global0 setCycle: CT 7 1 self)
			#end:case
			case 6:
				(ceiling cel: ((ceiling cel:) + 1))
				(global0 setCycle: CT 8 1 self)
			#end:case
			case 7:
				(global91 say: 1 0 3 3 self)
			#end:case
			case 8:
				(ceiling setCycle: End self)
			#end:case
			case 9:
				(global102 stop:)
				(global103 stop:)
				(global105 number: 425 setLoop: 1 play:)
				cycles = 6
			#end:case
			case 10:
				(ceiling stopUpd:)
				if register:
					(global91 say: 6 51 4 6 self)
				else:
					(self cue:)
				#endif
			#end:case
			case 11:
				(global1 handsOn:)
				proc0_1(9)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class useBrick(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91 say: 6 39 0 1 self)
			#end:case
			case 1:
				(global0 view: 421 normal: 0 setLoop: 0 cel: 4 posn: 162 146)
				ticks = 2
			#end:case
			case 2:
				(global0 cel: 5)
				(theBrick init:)
				ticks = 2
			#end:case
			case 3:
				(global0 cel: 6)
				(theBrick posn: ((theBrick x:) - 2) ((theBrick y:) - 4))
				ticks = 2
			#end:case
			case 4:
				(global0 cel: 7)
				(theBrick posn: ((theBrick x:) - 10) ((theBrick y:) + 8))
				ticks = 2
			#end:case
			case 5:
				(global0 cel: 8)
				(theBrick
					setPri: 11
					posn: ((theBrick x:) - 7) ((theBrick y:) - 3)
				)
				ticks = 2
			#end:case
			case 6:
				(global0 cel: 9)
				(theBrick
					setPri: -1
					posn: ((theBrick x:) + 24) ((theBrick y:) - 1)
				)
				ticks = 2
			#end:case
			case 7:
				(global0 cel: 10)
				(theBrick posn: ((theBrick x:) - 4) ((theBrick y:) - 19))
				ticks = 2
			#end:case
			case 8:
				(theBrick cel: 1 posn: ((theBrick x:) + 1) ((theBrick y:) - 6))
				ticks = 2
			#end:case
			case 9:
				(theBrick cel: 2 posn: (theBrick x:) ((theBrick y:) - 5))
				ticks = 2
			#end:case
			case 10:
				(theBrick cel: 3 posn: (theBrick x:) ((theBrick y:) - 6))
				ticks = 2
			#end:case
			case 11:
				(theBrick cel: 0 posn: (theBrick x:) ((theBrick y:) - 4))
				ticks = 2
			#end:case
			case 12:
				(theBrick cel: 1 posn: (theBrick x:) ((theBrick y:) + 3))
				ticks = 2
			#end:case
			case 13:
				(theBrick cel: 2 posn: (theBrick x:) ((theBrick y:) + 3))
				ticks = 2
			#end:case
			case 14:
				(theBrick cel: 3 posn: (theBrick x:) ((theBrick y:) + 2))
				ticks = 2
			#end:case
			case 15:
				(global102 stop:)
				(global103 stop:)
				(global105 number: 422 setLoop: 1 play: self)
				(global104 number: 424 setLoop: 1 play:)
				(theBrick cel: 0 posn: (theBrick x:) ((theBrick y:) + 2))
			#end:case
			case 16:
				(theBrick x: 169 y: 119 z: 32 stopUpd:)
				(global91 say: 6 39 0 2 self)
			#end:case
			case 17:
				(gears setCycle: 0 stopUpd:)
				(cog init: setCycle: End self)
				(global0 reset: 0 posn: 155 134)
			#end:case
			case 18:
				(global91 say: 6 39 0 3 self)
			#end:case
			case 19:
				(global1 givePoints: 2)
				(cog dispose:)
				(global105 number: 426 setLoop: 1 play:)
				(eastDoor setCycle: Beg)
				(westDoor setCycle: Beg self)
			#end:case
			case 20:
				(global91 say: 6 39 0 4 self)
			#end:case
			case 21:
				(kernel.ScriptID(30, 0) crushCeilingCel: (ceiling cel:))
				(kernel.ScriptID(30, 0) crushCeilingY: (ceiling y:))
				local0 = 1
				local1 = 5
				(ceiling stopUpd:)
				(global102 number: 400 play:)
				(global1 handsOn:)
				(global0 put: 2 global11)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoDoCrushCode(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 17:
				(global91 say: 3 17 local1 1)
				return 1
			#end:case
			case 12:
				(global91 say: 3 12 0 1)
				return 1
			#end:case
			else:
				return 0
			#end:else
		#end:match
	#end:method

#end:class or instance

