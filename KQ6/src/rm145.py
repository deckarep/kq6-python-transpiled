#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 145
import sci_sh
import Main
import KQ6Room
import n913
import Conversation
import TimedCue
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm145 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


@SCI.instance
class rm145(KQ6Room):
	#property vars (may be empty)
	picture = 98
	style = 9
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global69 disable:)
		(super init: &rest)
		(global2 setScript: seqScr)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global69 enable:)
		(proc913_2 133)
		(DisposeScript 960)
		(super dispose:)
	#end:method

#end:class or instance

@SCI.instance
class roomConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class eyeCue(TimedCue):
	#property vars (may be empty)
	register = 1
	
	@classmethod
	def init(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: param1 0 0)
		ticks = param2
	#end:method

#end:class or instance

class GlintingEye(Prop):
	#property vars (may be empty)
	view = 902
	priority = 15
	signal = 16400
	caller = 0
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not argc):
			(self setScript: eyeCue 12)
		else:
			if caller:
				(caller cue:)
			#endif
			(self dispose:)
		#endif
	#end:method

	@classmethod
	def init(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if argc:
			caller = param1
		#endif
		(super init: &rest)
		(self setCycle: End self)
	#end:method

#end:class or instance

@SCI.instance
class hiEye1(GlintingEye):
	#property vars (may be empty)
	x = 188
	y = 61
	
#end:class or instance

@SCI.instance
class lowEye(GlintingEye):
	#property vars (may be empty)
	x = 179
	y = 126
	
#end:class or instance

@SCI.instance
class hiEye2(GlintingEye):
	#property vars (may be empty)
	x = 180
	y = 62
	
#end:class or instance

@SCI.instance
class seqScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				cycles = 2
			#end:case
			case 1:
				(global2
					drawPic: 98 (9 if ((global87 == 0) or global169) else 12)
				)
				if (proc913_0 41):
					(global102 number: 150)
					local0 = 1
					register = 3
					(proc913_2 41)
				else:
					(global102 number: 145)
					if (proc913_0 72):
						register = 1
					else:
						register = 2
					#endif
					(proc913_1 41)
				#endif
				(global102 loop: -1 play:)
				(Message 0 145 1 0 4 1 @temp1)
				(Display @temp1 100 82 85 102 14 105 0)
				seconds = 5
			#end:case
			case 2:
				if local0:
					(bottle init:)
				#endif
				(genie init:)
				(vizier init:)
				(global2
					drawPic: 145 (9 if ((global87 == 0) or global169) else 11)
				)
				cycles = 1
			#end:case
			case 3:
				(cond
					case (register == 3):
						(roomConv
							add: -1 1 0 3 1
							add: eyeGlintScr
							add: -1 1 0 3 2
							add: eyeGlintScr
							add: -1 1 0 3 3
							add: eyeGlintScr
							add: -1 1 0 3 4
							add: eyeGlintScr
							add: -1 1 0 3 5
							add: eyeGlintScr
							add: -1 1 0 3 6
							add: eyeGlintScr
							add: -1 1 0 3 7
							add: eyeGlintScr
							add: -1 1 0 3 8
							add: eyeGlintScr
							add: -1 1 0 3 9
							add: eyeGlintScr
							add: -1 1 0 3 10
							add: genieBottleScr
							init: self
						)
						state++
					#end:case
					case (register == 1):
						(roomConv
							add: -1 1 0 1 1
							add: genieFallScr
							add: -1 1 0 1 2
							add: genieFallScr
							add: -1 1 0 1 3
							add: eyeGlintScr
							add: -1 1 0 1 4
							add: eyeGlintScr
							add: -1 1 0 1 5
							add: eyeGlintScr
							add: -1 1 0 1 6
							add: eyeGlintScr
							add: -1 1 0 1 7
							init: self
						)
						state++
					#end:case
					else:
						(roomConv
							add: -1 1 0 2 1
							add: genieFallScr
							add: -1 1 0 2 2
							add: genieFallScr
							add: -1 1 0 2 3
							add: eyeGlintScr
							add: -1 1 0 2 4
							add: eyeGlintScr
							add: -1 1 0 2 5
							add: eyeGlintScr
							add: -1 1 0 2 6
							add: eyeGlintScr
							init: self
						)
					#end:else
				)
			#end:case
			case 4:
				(roomConv
					add: -1 1 0 2 7
					add: eyeGlintScr
					add: -1 1 0 2 8
					add: eyeGlintScr
					add: -1 1 0 2 9
					add: eyeGlintScr
					add: -1 1 0 2 10
					add: eyeGlintScr
					add: -1 1 0 2 11
					add: eyeGlintScr
					add: -1 1 0 2 12
					add: eyeGlintScr
					add: -1 1 0 2 13
					init: self
				)
			#end:case
			case 5:
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global102 fade:)
		(super dispose:)
		(genie dispose:)
		(vizier dispose:)
		if (global5 contains: bottle):
			(bottle dispose:)
		#endif
		(global2 drawPic: 98 9)
		(global2 newRoom: 280)
	#end:method

#end:class or instance

@SCI.instance
class vizier(Prop):
	#property vars (may be empty)
	x = 62
	y = 115
	view = 1464
	signal = 1
	
#end:class or instance

@SCI.instance
class genie(Prop):
	#property vars (may be empty)
	x = 157
	y = 139
	view = 1461
	signal = 1
	
#end:class or instance

@SCI.instance
class genieFallScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(proc913_1 133)
				(DisposeScript 1013)
				(genie
					view: 1461
					loop: 1
					cel: 0
					cycleSpeed: 15
					setCycle: End self
				)
			#end:case
			case 1:
				(global102 pause:)
				(global103 number: 147 loop: 1 play:)
				(vizier cycleSpeed: 15 setCycle: End)
				(genie view: 1462 loop: 0 cel: 0 setCycle: End self)
			#end:case
			case 2:
				(global103 number: 960 loop: 1 play:)
				(genie hide:)
				(vizier setCycle: Beg)
				(ScriptID 1013)
				seconds = 3
			#end:case
			case 3:
				(self dispose:)
			#end:case
			case 4:
				(genie show: view: 1463 cel: 0 x: 205 y: 137 setCycle: End self)
			#end:case
			case 5:
				(global102 pause: 0 setVol: 0 fade: 127 10 15 0)
				(genie stopUpd:)
				(vizier stopUpd:)
				cycles = 2
			#end:case
			case 6:
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
		start = (state + 1)
	#end:method

#end:class or instance

@SCI.instance
class genieBottleScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global103 number: 943 loop: 1 play:)
				(genie view: 1465 posn: 186 99 loop: 0 cycleSpeed: 8)
				if register:
					(genie cel: 6 setCycle: Beg self)
				else:
					(genie cel: 0 setCycle: End self)
				#endif
			#end:case
			case 1:
				ticks = 60
			#end:case
			case 2:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class eyeGlintScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				if ((Random 0 1) and (global5 contains: genie)):
					(cond
						case (proc913_0 133):
							(lowEye init: self)
						#end:case
						case (Random 0 1):
							(hiEye1 init: self)
						#end:case
						else:
							(hiEye2 init: self)
						#end:else
					)
				else:
					(self dispose:)
				#endif
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class bottle(View):
	#property vars (may be empty)
	x = 218
	y = 151
	view = 1465
	loop = 1
	
#end:class or instance

