#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 461
import sci_sh
import kernel
import Main
import KQ6Room
import n913
import Conversation
import Feature
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	blackWidowInset = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None


@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class blackWidowInset(KQ6Room):
	#property vars (may be empty)
	modNum = 460
	picture = 465
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		(global69 disable: 6)
		(global102 fade: 0 10 10)
		(global103 number: 465 setLoop: -1 setVol: 0 play: fade: 127 10 10)
		(global32 add: roomAtLarge web eachElementDo: #init)
		if (not proc913_0(160)):
			(looseThread init:)
		#endif
		if (not proc913_0(136)):
			(parchment init:)
		#endif
		(spider init:)
		(self setScript: helloScript)
	#end:method

	@classmethod
	def newRoom():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global69 enable: 6)
		(super newRoom: &rest)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		proc913_2(59)
		(super dispose:)
	#end:method

#end:class or instance

@SCI.instance
class looseThread(Prop):
	#property vars (may be empty)
	x = 190
	y = 169
	noun = 13
	modNum = 460
	sightAngle = 180
	view = 465
	loop = 3
	priority = 15
	signal = 16400
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				if (not proc913_0(160)):
					(global1 handsOff:)
					(global2 setScript: unravelWeb)
				else:
					(super doVerb: param1 &rest)
				#endif
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class parchment(Prop):
	#property vars (may be empty)
	x = 104
	y = 93
	noun = 12
	modNum = 460
	sightAngle = 180
	view = 465
	loop = 1
	signal = 16384
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				if local0:
					(global1 handsOff:)
					(kernel.ScriptID(40, 0) gotParchment: 1)
					(global2 newRoom: 460)
				else:
					(global2 setScript: bitParchment)
				#endif
			#end:case
			else:
				(super doVerb: param1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class love(Actor):
	#property vars (may be empty)
	x = 146
	y = 97
	noun = 12
	modNum = 460
	yStep = 15
	view = 465
	loop = 4
	priority = 15
	signal = 18448
	xStep = 20
	
#end:class or instance

@SCI.instance
class spider(Actor):
	#property vars (may be empty)
	x = 196
	y = 137
	noun = 11
	modNum = 460
	sightAngle = 180
	yStep = 10
	view = 466
	loop = 1
	illegalBits = 0
	xStep = 14
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				(global2 setScript: touchSpider)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self sightAngle: 180 setCycle: Fwd)
		(super init: &rest)
	#end:method

#end:class or instance

@SCI.instance
class roomAtLarge(Feature):
	#property vars (may be empty)
	modNum = 460
	onMeCheck = 32
	
	@classmethod
	def doVerb():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global1 handsOn:)
		(global2 newRoom: 460)
	#end:method

#end:class or instance

@SCI.instance
class web(Feature):
	#property vars (may be empty)
	noun = 9
	modNum = 460
	onMeCheck = 2
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				(global91 say: 9 1 0 1 0 460)
			#end:case
			case 5:
				local1 = global70
				if (local2 = global71 > 150):
					local2 = 150
				#endif
				(global2 setScript: spiderRush)
			#end:case
			case 2:
				(global91 say: 9 2 0 1 0 460)
			#end:case
			else:
				(global91 say: 9 0 0 1 0 460)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class spiderRush(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91 say: 9 5 0 1 self 460)
			#end:case
			case 1:
				(kernel.ScriptID(40, 0) spiderBit: 1)
				(global1 handsOn:)
				(global2 newRoom: 460)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class bitParchment(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global91 say: 12 5 11 1 self 460)
			#end:case
			case 1:
				(kernel.ScriptID(40, 0) parchmentBit: 1)
				(global2 newRoom: 460)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class touchSpider(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global91 say: 11 5 0 1 self 460)
			#end:case
			case 1:
				(kernel.ScriptID(40, 0) spiderBit: 1)
				(global1 handsOn:)
				(global2 newRoom: 460)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class unravelWeb(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 givePoints: 1)
				proc913_1(160)
				local0 = 1
				(global91 say: 13 5 0 1 self 460)
			#end:case
			case 1:
				(global105 number: 467 setLoop: 1 play:)
				(looseThread setCycle: End self)
			#end:case
			case 2:
				(global1 handsOn:)
				(spider setLoop: 2 setMotion: MoveTo 196 137 self)
				seconds = 2
			#end:case
			case 3:
				(looseThread dispose:)
			#end:case
			case 4:
				(spider setCycle: 0)
				(global69 disable: 0)
				seconds = 5
			#end:case
			case 5:
				(spider setCycle: Walk setLoop: 1 setMotion: MoveTo 167 76 self)
			#end:case
			case 6:
				(global91 say: 13 5 0 3 self 460)
				local0 = 0
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class helloScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(spider
					setCycle: Walk
					setLoop: 1
					ignoreActors:
					ignoreHorizon:
					setMotion: MoveTo 167 76 self
				)
			#end:case
			case 1:
				if proc913_0(56):
					(global91 say: 8 1 10 1 self 460)
				else:
					(myConv
						add: 460 8 1 9 1
						add: 460 8 1 9 2
						add: 460 8 1 9 3
						add: 460 8 1 9 4
						init: self
					)
				#endif
			#end:case
			case 2:
				if proc913_0(56):
					(self cue:)
				else:
					(myConv
						add: 460 8 1 9 5
						add: 460 8 1 9 6
						add: 460 8 1 9 7
						init: self
					)
				#endif
			#end:case
			case 3:
				proc913_1(56)
				(global1 handsOn:)
				(global69 disable: 0)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

