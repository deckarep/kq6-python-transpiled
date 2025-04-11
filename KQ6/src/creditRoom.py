#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 94
import sci_sh
import Main
import rm100
import KQ6Print
import KQ6Room
import User
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	creditRoom = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0
local50
local250 = [1, 1, 1, 2, 3, 4, 1, 2, 3, 4, 4, 1, 3, 4, 1, 3, 3, 4, 1, 2, 3, 4, 1, 2, 1, -1]
local276 = [98, 100, 380, 240, 150, 480, 650, 520, 450, 580, 160, 490, 730, 690, 790, 770, 260, 750, 220, 470, 410, 510, 210, 290, 660, -1]
local302 = None
local303 = 1
local304 = None
local305 = None
local306 = 1


@SCI.instance
class creditRoom(KQ6Room):
	#property vars (may be empty)
	picture = 98
	horizon = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init:)
		(global102 number: 10 loop: -1 play: buttonScript)
		(global69 disable:)
		(global2 setScript: creditsScript)
	#end:method

	@classmethod
	def doVerb():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global91 say: 2 0 0 0)
		return 1
	#end:method

#end:class or instance

@SCI.instance
class creditsScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(DrawPic local276[local302] 9)
				if (local276[local302] == 98):
					cycles = 2
				else:
					(setUpRoom doit: self)
				#endif
			#end:case
			case 1:
				if ((local276[local302] == 98) and local306):
					local306 = 0
					(self setScript: showScore self)
				else:
					cycles = 2
				#endif
			#end:case
			case 2:
				if (local276[local302] == 98):
					state = 3
				#endif
				cycles = 1
			#end:case
			case 3:
				if local304:
					(Message 0 94 1 0 0 local303 @local0)
					(Message 0 94 1 0 0 local303++ @local50)
				else:
					(Message 0 94 0 0 0 local303 @local0)
					(Message 0 94 0 0 0 local303++ @local50)
				#endif
				if (local303++ >= 32):
					local304 = 1
					local303 = 1
				#endif
				match local250[local302]
					case 1:
						(Display @local0 102 0 100 64 11 106 200 105 3110 101 1)
						(Display @local50 102 0 100 64 31 106 200 105 2207 101 1)
						(Display @local0 102 7 100 63 10 106 200 105 3110 101 1)
						(Display @local50 102 7 100 63 30 106 200 105 2207 101 1)
					#end:case
					case 2:
						(Display @local0 102 0 100 194 11 106 200 105 3110 101 1)
						(Display
							@local50
							102
							0
							100
							194
							31
							106
							200
							105
							2207
							101
							1
						)
						(Display @local0 102 7 100 194 10 106 200 105 3110 101 1)
						(Display
							@local50
							102
							7
							100
							194
							30
							106
							200
							105
							2207
							101
							1
						)
					#end:case
					case 3:
						(Display @local0 102 0 100 136 88 106 200 105 3110 101 1)
						(Display
							@local50
							102
							0
							100
							136
							118
							106
							200
							105
							2207
							101
							1
						)
						(Display @local0 102 7 100 135 87 106 200 105 3110 101 1)
						(Display
							@local50
							102
							7
							100
							135
							117
							106
							200
							105
							2207
							101
							1
						)
					#end:case
					case 4:
						(Display @local0 102 0 100 11 98 106 200 105 3110 101 1)
						(Display
							@local50
							102
							0
							100
							11
							128
							106
							200
							105
							2207
							101
							1
						)
						(Display @local0 102 7 100 10 97 106 200 105 3110 101 1)
						(Display
							@local50
							102
							7
							100
							10
							127
							106
							200
							105
							2207
							101
							1
						)
					#end:case
				#end:match
				if (not local305):
					seconds = 8
				else:
					(client setScript: buttonScript)
				#endif
			#end:case
			case 4:
				if (local276[local302++] == -1):
					local302 = 0
					local303 = 1
					local304 = 0
					local305 = 1
				#endif
				(self init:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class buttonScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global69
					enable:
					disable: 0 1 2 3 4 5 6
					activateHeight: -100
					height: -100
				)
				(User canInput: 1)
				(global1 setCursor: global20)
				(quitBut init:)
				(replayBut init:)
				(restartBut init:)
				cycles = 10
			#end:case
			case 1:#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class showScore(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(KQ6Print
					font: global22
					addTextF:
						r"""You received %d out of %d points. You've completed approximately %d percent of the main-path puzzles in King's Quest VI."""
						global15
						global16
						((global15 * 100) / global16)
					init:
				)
				cycles = 1
			#end:case
			case 1:
				if (global15 <= 230):
					(global91 say: 0 0 1 2 self)
				else:
					(global91 say: 0 0 1 3 self)
				#endif
			#end:case
			case 2:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class quitBut(ButtonActor):
	#property vars (may be empty)
	x = 191
	y = 173
	view = 94
	loop = 2
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super cue: &rest)
		global4 = 1
	#end:method

#end:class or instance

@SCI.instance
class replayBut(ButtonActor):
	#property vars (may be empty)
	x = 77
	y = 173
	view = 94
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super cue: &rest)
		(global1 setCursor: global21)
		local302 = 0
		local303 = 1
		local304 = 0
		local305 = 0
		(quitBut dispose:)
		(restartBut dispose:)
		(global2 init:)
		(self dispose:)
	#end:method

#end:class or instance

@SCI.instance
class restartBut(ButtonActor):
	#property vars (may be empty)
	x = 134
	y = 173
	view = 94
	loop = 1
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super cue: &rest)
		(global1 restart: 1)
	#end:method

#end:class or instance

@SCI.instance
class setUpRoom(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = param1
		param1 = 0
		match local276[local302]
			case 100:
				(temp1 = (Prop new:)
					view: 101
					loop: 0
					cel: 11
					x: 113
					y: 74
					init:
					addToPic:
					dispose:
				)
			#end:case
			case 380:
				(temp1 = (Prop new:)
					view: 383
					loop: 0
					cel: 0
					x: 94
					y: 87
					init:
					addToPic:
					dispose:
				)
				(temp2 = (Prop new:)
					view: 382
					loop: 1
					cel: 0
					x: 158
					y: 49
					init:
					addToPic:
					dispose:
				)
			#end:case
			case 240:
				(temp1 = (Prop new:)
					view: 240
					loop: 0
					cel: 0
					x: 254
					y: 99
					init:
					addToPic:
					dispose:
				)
				(temp2 = (Prop new:)
					view: 240
					loop: 1
					cel: 0
					x: 186
					y: 86
					init:
					addToPic:
					dispose:
				)
			#end:case
			case 150:
				(temp1 = (Prop new:)
					view: 150
					loop: 7
					cel: 0
					x: 291
					y: 120
					init:
					addToPic:
					dispose:
				)
			#end:case
			case 480:
				(temp1 = (Prop new:)
					view: 4801
					loop: 0
					cel: 0
					x: 142
					y: 76
					init:
					addToPic:
					dispose:
				)
				(temp2 = (Prop new:)
					view: 4801
					loop: 1
					x: 277
					y: 129
					init:
					addToPic:
					dispose:
				)
				(temp3 = (Prop new:)
					view: 4851
					loop: 0
					x: 215
					y: 91
					init:
					addToPic:
					dispose:
				)
				(temp4 = (Prop new:)
					view: 4851
					loop: 1
					x: 229
					y: 93
					init:
					addToPic:
					dispose:
				)
				(temp5 = (Prop new:)
					view: 4851
					loop: 2
					x: 252
					y: 84
					init:
					addToPic:
					dispose:
				)
				(temp6 = (Prop new:)
					view: 4851
					loop: 3
					x: 253
					y: 85
					init:
					addToPic:
					dispose:
				)
			#end:case
			case 650:
				(temp1 = (Prop new:)
					view: 650
					loop: 0
					cel: 0
					x: 159
					y: 51
					init:
					addToPic:
					dispose:
				)
				(temp2 = (Prop new:)
					view: 650
					loop: 1
					cel: 0
					x: 299
					y: 61
					init:
					addToPic:
					dispose:
				)
				(temp3 = (Prop new:)
					view: 650
					loop: 2
					cel: 0
					x: 65
					y: 89
					init:
					addToPic:
					dispose:
				)
			#end:case
			case 160:
				(temp1 = (Prop new:)
					view: 160
					loop: 7
					cel: 0
					x: 5
					y: 79
					init:
					addToPic:
					dispose:
				)
			#end:case
			case 690:
				(temp1 = (Prop new:)
					view: 690
					loop: 1
					cel: 0
					x: 22
					y: 82
					init:
					addToPic:
					dispose:
				)
				(temp2 = (Prop new:)
					view: 691
					loop: 6
					cel: 0
					x: 111
					y: 119
					init:
					addToPic:
					dispose:
				)
				(temp3 = (Prop new:)
					view: 692
					loop: 0
					cel: 0
					x: 224
					y: 107
					init:
					addToPic:
					dispose:
				)
			#end:case
			case 730:
				(temp1 = (Prop new:)
					view: 730
					loop: 0
					cel: 0
					x: 160
					y: 100
					init:
					addToPic:
					dispose:
				)
				(temp2 = (Prop new:)
					view: 730
					loop: 1
					cel: 0
					x: 70
					y: 143
					z: 28
					init:
					addToPic:
					dispose:
				)
				(temp3 = (Prop new:)
					view: 730
					loop: 2
					cel: 0
					x: 250
					y: 119
					init:
					addToPic:
					dispose:
				)
			#end:case
			case 260:
				(temp1 = (Prop new:)
					view: 260
					loop: 0
					cel: 0
					x: 22
					y: 80
					init:
					addToPic:
					dispose:
				)
			#end:case
			case 220:
				(temp1 = (Prop new:)
					view: 220
					loop: 0
					cel: 0
					x: 107
					y: 94
					init:
					addToPic:
					dispose:
				)
			#end:case
			case 510:
				(temp1 = (Prop new:)
					view: 510
					loop: 1
					cel: 0
					x: 236
					y: 58
					init:
					addToPic:
					dispose:
				)
			#end:case
			case 290:
				(temp1 = (Prop new:)
					view: 290
					loop: 3
					cel: 0
					x: 136
					y: 80
					init:
					addToPic:
					dispose:
				)
			#end:case
			case 750:
				(temp1 = (Prop new:)
					view: 7500
					loop: 0
					cel: 0
					x: 210
					y: 115
					init:
					addToPic:
					dispose:
				)
			#end:case
			case 470:
				(temp1 = (Prop new:)
					view: 475
					loop: 2
					cel: 2
					x: 273
					y: 119
					init:
					addToPic:
					dispose:
				)
			#end:case
			else: 1#end:else
		#end:match
		(temp0 cue:)
	#end:method

#end:class or instance

