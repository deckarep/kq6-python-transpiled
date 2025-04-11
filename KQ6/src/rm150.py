#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 150
import sci_sh
import Main
import KQ6Room
import Conversation
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm150 = 0,
	genie = 1,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None


@SCI.instance
class rm150(KQ6Room):
	#property vars (may be empty)
	picture = 150
	style = 6
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global2 newRoom: 220)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global69 disable: 6)
		(super init: &rest)
		(global1 givePoints: 2)
		(self setScript: roomScr)
		(swordArm init:)
		(global102 number: 150 loop: -1 play: self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global69 enable: 6)
		(super dispose:)
	#end:method

#end:class or instance

@SCI.instance
class roomConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class genieHeadScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(genie init:)
				cycles = 2
			#end:case
			case 1:
				start = (state + 1)
				(self dispose:)
			#end:case
			case 2:
				(genie hide:)
				if (((Random 0 3) - 1) and (not local1)):
					local1 = 1
					local2 = 1
					if (Random 0 1):
						(eye1 init: cel: 0 setCycle: End self)
						local0 = 1
					else:
						(eye2 init: cel: 0 setCycle: End self)
						local0 = 0
					#endif
				else:
					local1 = 0
					(state += 2)
					cycles = 2
				#endif
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				if local0:
					(eye1 dispose:)
				else:
					(eye2 dispose:)
				#endif
				cycles = 2
			#end:case
			case 5:
				start = (state + 1)
				(self dispose:)
			#end:case
			case 6:
				(genie show:)
				cycles = 2
			#end:case
			case 7:
				start = (state - 5)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genie(Prop):
	#property vars (may be empty)
	x = 161
	y = 82
	view = 150
	
#end:class or instance

@SCI.instance
class swordArm(Prop):
	#property vars (may be empty)
	x = 291
	y = 120
	view = 150
	loop = 7
	signal = 1
	
#end:class or instance

@SCI.instance
class eye1(Prop):
	#property vars (may be empty)
	x = 166
	y = 71
	view = 902
	
#end:class or instance

@SCI.instance
class eye2(Prop):
	#property vars (may be empty)
	x = 159
	y = 71
	view = 902
	
#end:class or instance

@SCI.instance
class saladineyes(Prop):
	#property vars (may be empty)
	x = 293
	y = 4
	view = 150
	loop = 10
	cel = 2
	
#end:class or instance

@SCI.instance
class roomScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				cycles = 3
			#end:case
			case 1:
				(roomConv
					add: -1 1 0 1 1
					add: genieHeadScr
					add: -1 1 0 1 2
					add: genieHeadScr
					add: -1 1 0 1 3
					add: genieHeadScr
					add: -1 1 0 1 4
					add: genieHeadScr
					add: -1 1 0 1 5
					add: genieHeadScr
					add: -1 1 0 1 6
					add: genieHeadScr
					add: -1 1 0 1 7
					init: self
				)
			#end:case
			case 2:
				(roomConv
					add: genieHeadScr
					add: -1 1 0 1 8
					add: -1 1 0 1 9
					add: -1 1 0 1 10
					add: -1 1 0 1 11
					add: genieHeadScr
					add: -1 1 0 1 12
					add: genieHeadScr
					add: -1 1 0 1 13
					add: genieHeadScr
					add: -1 1 0 1 14
					add: genieHeadScr
					add: -1 1 0 1 15
					add: -1 1 0 1 16
					add: genieHeadScr
					init: self
				)
			#end:case
			case 3:
				if (not local2):
					if (global5 contains: genie):
						(genie dispose:)
					#endif
					(eye1 init: cel: 0 setCycle: End self)
				else:
					state++
					cycles = 1
				#endif
			#end:case
			case 4:
				(eye1 dispose:)
				cycles = 2
			#end:case
			case 5:
				(global105 number: 756 loop: 1 play:)
				(swordArm setCycle: End)
				(global102 fade:)
			#end:case
		#end:match
	#end:method

#end:class or instance

