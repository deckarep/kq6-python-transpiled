#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 274
import sci_sh
import kernel
import Main
import n913
import PolyPath
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	clown = 0,
	clownExitScr = 1,
	clownScr = 2,
)

@SCI.instance
class clown(Actor):
	#property vars (may be empty)
	x = 206
	y = 133
	noun = 10
	approachX = 231
	approachY = 140
	view = 2721
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case proc999_5(param1, 5, 1):
				(global91 say: noun param1 (7 if proc913_0(10) else 8) 0 0 270)
			#end:case
			case (param1 == 2):
				if (not proc913_0(10)):
					(global2 setScript: kernel.ScriptID(277, 0))
				else:
					(global2 setScript: kernel.ScriptID(277, 1))
				#endif
			#end:case
			case proc999_5(param1, 40, 70):
				(cond
					case (not proc913_0(78)):
						(global91 say: noun param1 10 0 0 270)
					#end:case
					case proc913_0(10):
						(global2 setScript: kernel.ScriptID(277, 2) 0 param1)
					#end:case
					else:
						(global1 givePoints: 4)
						proc913_1(10)
						(global2
							setScript:
								kernel.ScriptID(275, 0)
								0
								(1 if (param1 == 40) else 0)
						)
					#end:else
				)
			#end:case
			case proc999_5(param1, 69, 13):
				(super doVerb: param1 &rest)
			#end:case
			case 
				(or
					proc999_5(param1, 45, 8, 14, 30, 47, 15, 18)
					proc999_5(param1, 32, 12, 62, 63, 65, 66, 67)
				):
				if (param1 == 15):
					param1 = 18
				#endif
				if (param1 == 67):
					param1 = 63
				#endif
				(global2 setScript: kernel.ScriptID(277, 2) 0 param1)
			#end:case
			else:
				(global2 setScript: kernel.ScriptID(277, 2))
			#end:else
		)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self
			approachVerbs: 5 2 70
			illegalBits: 0
			ignoreActors:
			setScript: kernel.ScriptID(274, 2)
		)
	#end:method

#end:class or instance

@SCI.instance
class clownScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(client view: 2721 loop: 0)
				cycles = 1
			#end:case
			case 1:
				seconds = kernel.Random(5, 20)
			#end:case
			case 2:
				(client cel: 0 setCycle: End self)
			#end:case
			case 3:
				(client stopUpd:)
				state = 0
				(self cue:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class clownExitScr(Script):
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
				kernel.DisposeScript(275)
				(global0 stopUpd:)
				(clown
					posn: 201 137
					view: 2741
					setLoop: 0
					scaleX: 121
					scaleY: 121
					setStep: 5 3
					setScale:
					setCycle: Walk
					setSpeed: 4
					setMotion: PolyPath 107 135 self
				)
			#end:case
			case 2:
				(clown
					setPri: 1
					view: 274
					loop: 1
					cel: 0
					posn: 72 135
					cycleSpeed: 6
					setCycle: End
				)
				(global105 number: 901 loop: 1 play:)
				(kernel.ScriptID(270, 4) setCycle: End self)
			#end:case
			case 3:
				(kernel.ScriptID(270, 4) setCycle: Beg self)
			#end:case
			case 4:
				(clown dispose:)
				(global105 number: 902 loop: 1 play:)
				(global0 startUpd:)
				cycles = 2
			#end:case
			case 5:
				(kernel.ScriptID(270, 4) stopUpd:)
				(kernel.ScriptID(10, 0) setIt: 2)
				(global102 fade: 0 20 15 0)
				ticks = 45
			#end:case
			case 6:
				kernel.UnLoad(128, 2741)
				kernel.UnLoad(128, 274)
				(global102 number: 240 loop: -1 play: 0 fade: 70 10 15 0)
				(global1 handsOn:)
				(global69 curIcon: (global69 at: 0))
				(global1 setCursor: ((global69 curIcon:) cursor:))
				seconds = 13
			#end:case
			case 7:
				(kernel.ScriptID(270, 5) init:)
				(kernel.ScriptID(10, 0) clrIt: 2)
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
		proc913_2(53)
		if (not proc999_5(global153, 3, 4)):
			proc913_2(54)
		else:
			proc913_1(54)
		#endif
		(clown dispose:)
		(clown delete:)
		kernel.DisposeScript(274)
	#end:method

#end:class or instance

