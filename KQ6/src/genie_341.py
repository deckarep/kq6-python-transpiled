#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 341
import sci_sh
import Main
import rSacred
import n913
import Conversation
import PolyPath
import Polygon
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	proc341_0 = 0,
	proc341_1 = 1,
	proc341_2 = 2,
	proc341_3 = 3,
	genie = 4,
	poofAwayScript = 5,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None


@SCI.procedure
def proc341_0():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(genie init:)
#end:procedure

@SCI.procedure
def proc341_1():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(genie setScript: genieTrap)
#end:procedure

@SCI.procedure
def proc341_2():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(genie dispose:)
#end:procedure

@SCI.procedure
def proc341_3():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(genie addToPic:)
#end:procedure

@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class geniePoly(Polygon):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class eyeGlint(Prop):
	#property vars (may be empty)
	view = 902
	cycleSpeed = 15
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self setPri: 15 setCycle: End self)
		(super init:)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (cel == 2):
			(self setPri: 15 setCycle: Beg self)
		else:
			((genie script:) cue:)
			(self dispose:)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class genie(Actor):
	#property vars (may be empty)
	x = 260
	y = 116
	noun = 8
	modNum = 340
	yStep = 8
	view = 334
	signal = 24576
	xStep = 12
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global2
			addObstacle:
				(geniePoly
					type: 2
					init: 279 120 239 120 234 116 239 113 279 113 283 116
					yourself:
				)
		)
		(rSacred geniePresent: 1)
		(super init:)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global104 fade: 0 6 6)
		(eyeGlint dispose:)
		((global2 obstacles:) delete: geniePoly)
		(geniePoly dispose:)
		(rSacred geniePresent: 0)
		(super dispose:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 2:
				if local0:
					(myConv add: 340 8 2 26 1 add: 340 8 2 26 2 init:)
				else:
					local0 = 1
					(myConv add: 340 8 2 25 1 add: 340 8 2 25 2 init:)
				#endif
			#end:case
			case 63:
				(global0 setScript: 0)
				(global1 handsOff:)
				(global2 setScript: genieAsMintJunkie)
			#end:case
			case 43:
				(global91 say: noun param1 0 0)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class poofAwayScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(genie setScript: 0 setCycle: 0 setMotion: 0)
				(eyeGlint dispose:)
				cycles = 1
			#end:case
			case 1:
				(global91 say: 1 0 7 1 self 340)
			#end:case
			case 2:
				(global105 number: 943 setLoop: 1 play:)
				(genie setLoop: 2 cel: 0 setCycle: End self)
			#end:case
			case 3:
				(global91 say: 1 0 7 2 self 340)
			#end:case
			case 4:
				(rSacred geniePresent: 0)
				(self dispose:)
				(genie dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genieAsMintJunkie(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				if ((global0 x:) > (genie x:)):
					(global0 setMotion: PolyPath 249 118 self)
				else:
					(self cue:)
				#endif
			#end:case
			case 1:
				(global0 setHeading: 45)
				cycles = 8
			#end:case
			case 2:
				(myConv add: 340 8 63 0 1 add: 340 8 63 0 2 init: self)
			#end:case
			case 3:
				(genie
					setLoop: 3
					posn: ((genie x:) - 1) ((genie y:) - 25)
					setCycle: End self
				)
			#end:case
			case 4:
				(genie
					setCycle: 0
					setMotion:
						MoveTo
						((global0 x:) + 12)
						((global0 y:) - 27)
						self
				)
			#end:case
			case 5:
				(genie setCycle: Beg self)
			#end:case
			case 6:
				(genie
					setLoop: 5
					cel: 0
					posn: ((global0 x:) + 13) ((global0 y:) - 3)
				)
				(global0
					view: 334
					normal: 0
					setLoop: 6
					cel: 0
					setCycle: CT 2 1 self
				)
			#end:case
			case 7:
				(genie setCycle: End self)
				(global0 cel: 3)
			#end:case
			case 8:
				(myConv add: 340 8 63 0 3 add: 340 8 63 0 4 init: self)
			#end:case
			case 9:
				(global0 reset: 6 put: 23 340)
				(global105 number: 943 setLoop: 1 play:)
				(genie
					setLoop: 2
					cel: 0
					posn: ((global0 x:) + 13) ((global0 y:) - 2)
					setCycle: End self
				)
			#end:case
			case 10:
				local1 = 1
				(genie dispose:)
				cycles = 4
			#end:case
			case 11:
				(global91 say: 8 63 0 5 self 340)
			#end:case
			case 12:
				(global1 handsOn:)
				(self dispose:)
				(DisposeScript 341)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genieTrap(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(proc913_1 4)
				seconds = 2
				(global0 setHeading: 30)
			#end:case
			case 1:
				(eyeGlint posn: (genie x:) ((genie y:) - 44) init:)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				(global91 say: 1 0 1 2 0 340)
				seconds = 1
			#end:case
			case 4:
				(genie setLoop: 1 cel: 0 setCycle: End self)
			#end:case
			case 5:
				(genie setCycle: Beg self)
			#end:case
			case 6:
				(genie setCycle: End self)
			#end:case
			case 7:
				(genie setCycle: Beg self)
			#end:case
			case 8:
				seconds = 2
			#end:case
			case 9:
				(global91 say: 1 0 1 3 0 340)
				seconds = 1
			#end:case
			case 10:
				seconds = 2
			#end:case
			case 11:
				(genie setLoop: 1 cel: 0)
				cycles = 6
			#end:case
			case 12:
				(genie setLoop: 5 cel: 0 setCycle: End self)
				(global105 number: 348 setLoop: 1 play:)
			#end:case
			case 13:
				(genie setCycle: Beg self)
			#end:case
			case 14:
				(genie setLoop: 0 posn: 260 116)
				seconds = 2
			#end:case
			case 15:
				(eyeGlint posn: (genie x:) ((genie y:) - 44) init:)
			#end:case
			case 16:
				cycles = 2
			#end:case
			case 17:
				(genie setLoop: 3 cel: 0 posn: 259 89 setCycle: End self)
			#end:case
			case 18:
				(global105 number: 347 setLoop: -1 play:)
				(genie setCycle: Beg self)
			#end:case
			case 19:
				(genie
					setLoop: 4
					cel: 0
					setCycle: Fwd
					setMotion: MoveTo ((genie x:) - 30) ((genie y:) - 20) self
				)
			#end:case
			case 20:
				(genie
					setMotion: MoveTo ((genie x:) + 60) ((genie y:) - 20) self
				)
			#end:case
			case 21:
				(genie
					setMotion: MoveTo ((genie x:) - 60) ((genie y:) - 20) self
				)
			#end:case
			case 22:
				(genie
					setMotion: MoveTo ((genie x:) + 60) ((genie y:) - 20) self
				)
			#end:case
			case 23:
				(genie
					setMotion: MoveTo ((genie x:) - 60) ((genie y:) + 20) self
				)
			#end:case
			case 24:
				(genie
					setMotion: MoveTo ((genie x:) + 60) ((genie y:) + 20) self
				)
			#end:case
			case 25:
				(genie
					setMotion: MoveTo ((genie x:) - 30) ((genie y:) + 20) self
				)
			#end:case
			case 26:
				(genie setLoop: 3 cel: 3 posn: 259 89 setCycle: Beg self)
			#end:case
			case 27:
				(global105 stop:)
				(genie setLoop: 0 posn: 260 116)
				seconds = 2
			#end:case
			case 28:
				(eyeGlint posn: (genie x:) ((genie y:) - 44) init:)
			#end:case
			case 29:
				cycles = 2
			#end:case
			case 30:
				(global1 handsOn:)
				(global91 say: 1 0 1 4 0 340)
				seconds = 1
			#end:case
			case 31:
				(eyeGlint posn: (genie x:) ((genie y:) - 44) init:)
			#end:case
			case 32:
				seconds = 10
			#end:case
			case 33:
				if ((not (global2 script:)) and (not global25)):
					(global91 say: 1 0 5 1 0 340)
					seconds = 1
				else:
					(self cue:)
				#endif
			#end:case
			case 34:
				(eyeGlint posn: (genie x:) ((genie y:) - 44) init:)
			#end:case
			case 35:
				seconds = 10
			#end:case
			case 36:
				if ((not (global2 script:)) and (not global25)):
					(global91 say: 1 0 6 1 0 340)
					seconds = 1
				else:
					(self cue:)
				#endif
			#end:case
			case 37:
				(eyeGlint posn: (genie x:) ((genie y:) - 44) init:)
			#end:case
			case 38:
				seconds = 10
			#end:case
			case 39:
				if ((not (global2 script:)) and (not global25)):
					(global91 say: 1 0 7 1 0 340)
					seconds = 1
				else:
					(self cue:)
				#endif
			#end:case
			case 40:
				(global1 handsOff:)
				if (not (global2 script:)):
					(proc913_4 global0 genie)
				#endif
				(global105 number: 943 setLoop: 1 play:)
				(genie setLoop: 2 cel: 0 setCycle: End self)
			#end:case
			case 41:
				(global91 say: 1 0 7 2 0 340)
				seconds = 1
			#end:case
			case 42:
				(global1 handsOn:)
				(genie dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

