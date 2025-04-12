#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 272
import sci_sh
import kernel
import Main
import Conversation
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	poemShelfScr = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = -1
local1 = None


@SCI.instance
class roomConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class turnPageScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global0 setCycle: CT 1 -1 self)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				(global0 setCycle: End self)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class poemShelfScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				if ((global0 loop:) != 3):
					(global0 loop: 3)
				#endif
				cycles = 2
			#end:case
			case 1:
				(global0
					setSpeed: 6
					view: 279
					loop: 2
					cel: 0
					normal: 0
					setCycle: End self
				)
			#end:case
			case 2:
				(global0 loop: 3 cel: 0 setCycle: End self)
			#end:case
			case 3:
				if (((global9 at: 47) owner:) != 270):
					register = 1
					(roomConv
						add: -1 13 5 18 1
						add: -1 13 5 18 2
						add: -1 13 5 18 3
						add: turnPageScr
						add: -1 13 5 18 4
						add: -1 13 5 18 5
						init: self
					)
				else:
					(roomConv
						add: -1 13 5 17 1
						add: -1 13 5 17 2
						add: -1 13 5 17 3
						add: turnPageScr
						add: -1 13 5 17 4
						add: -1 13 5 17 5
						add: turnPageScr
						add: -1 13 5 17 6
						add: turnPageScr
						add: -1 13 5 17 7
						add: turnPageScr
						add: -1 13 5 17 8
						add: -1 13 5 17 9
						add: -1 13 5 17 10
						init: self
					)
				#endif
			#end:case
			case 4:
				if (not register):
					((global9 at: 47) owner: -1)
					(poem
						init:
						posn: 303 92
						view: 279
						setLoop: 6
						cel: 0
						setCycle: Fwd
						setMotion: MoveTo 281 120 poem
					)
				#endif
				cycles = 2
			#end:case
			case 5:
				(global0 loop: 2 cel: (global0 lastCel:))
				cycles = 2
			#end:case
			case 6:
				(global0 setCycle: Beg self)
			#end:case
			case 7:
				(global0 reset: 3)
				if (not register):
					(global1 givePoints: 1)
				#endif
				cycles = 1
			#end:case
			case 8:
				if ((not local1) and (not register)):
					state.post('--')
					ticks = 12
				else:
					cycles = 2
				#endif
			#end:case
			case 9:
				kernel.UnLoad(128, 279)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		register = 0
		(super dispose:)
	#end:method

#end:class or instance

@SCI.instance
class takePoemScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global1 givePoints: 1)
				(global0
					setSpeed: 6
					view: 2701
					loop: 1
					cel: 0
					normal: 0
					setCycle: CT 3 1 self
				)
			#end:case
			case 1:
				(poem dispose:)
				(global0 get: 47)
				cycles = 2
			#end:case
			case 2:
				(global0 setCycle: End self)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				(global0 reset: 7)
				cycles = 2
			#end:case
			case 5:
				kernel.UnLoad(128, 2701)
				(global91 say: 6 5 0 1 self)
			#end:case
			case 6:
				(global91 say: 6 5 0 2 self)
			#end:case
			case 7:
				(global91 say: 6 5 0 3 self)
			#end:case
			case 8:
				(global0 setHeading: 180 self)
			#end:case
			case 9:
				cycles = 2
			#end:case
			case 10:
				(global91 say: 6 5 0 4 self)
			#end:case
			case 11:
				(global1 handsOn:)
				(self dispose:)
				kernel.DisposeScript(272)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class poem(Actor):
	#property vars (may be empty)
	x = 281
	y = 120
	noun = 6
	approachX = 292
	approachY = 128
	view = 270
	loop = 2
	cel = 1
	priority = 1
	signal = 18449
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not local0.post('++')):
			(self setCycle: End self)
		else:
			(self view: 270 setLoop: 2 cel: 1)
			local1 = 1
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				(global2 setScript: takePoemScr)
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

		(super init: &rest)
		(self approachVerbs: 5)
	#end:method

#end:class or instance

