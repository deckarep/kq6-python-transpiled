#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 430
import sci_sh
import Main
import rLab
import n401
import PolyPath
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm430 = 0,
)

@SCI.instance
class rm430(LabRoom):
	#property vars (may be empty)
	east = 400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(proc401_3)
		(super init: &rest)
		(theCorpseNorth init: stopUpd:)
		if (((global9 at: 7) owner:) == global11):
			(theGlint init:)
		#endif
		(global2 setScript: (ScriptID 30 1))
		((ScriptID 30 0) initCrypt: 4)
		((ScriptID 30 6) addToPic:)
		((ScriptID 30 10) addToPic:)
		((ScriptID 30 8) addToPic:)
	#end:method

	@classmethod
	def notify():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		((ScriptID 30 6) addToPic:)
		((ScriptID 30 10) addToPic:)
		((ScriptID 30 8) addToPic:)
		((ScriptID 30 3) show:)
	#end:method

#end:class or instance

@SCI.instance
class theGlint(Prop):
	#property vars (may be empty)
	x = 132
	y = 111
	modNum = 400
	view = 902
	priority = 9
	signal = 16400
	cycleSpeed = 3
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(theDeadMansCoin init:)
		(self setScript: glintCoinEyes)
		(super init: &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global0 setScript: getCoins)
			#end:case
			else:
				((ScriptID 30 4) doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class theDeadMansCoin(Prop):
	#property vars (may be empty)
	x = 133
	y = 170
	z = 58
	noun = 13
	modNum = 400
	view = 431
	loop = 6
	priority = 8
	signal = 16400
	cycleSpeed = 15
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global0 setScript: getCoins)
			#end:case
			case 1:
				(global91 say: 13 1 0 0 0 400)
			#end:case
			else:
				((ScriptID 30 4) doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class theCorpseNorth(View):
	#property vars (may be empty)
	x = 132
	y = 122
	z = 10
	approachX = 132
	approachY = 112
	view = 400
	loop = 1
	cel = 2
	priority = 7
	signal = 16400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (global5 contains: theDeadMansCoin):
			(self noun: 13)
		else:
			(self noun: 8)
		#endif
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 7:
				(global91 say: 13 7 0 1 0 400)
			#end:case
			case 5:
				if (global5 contains: theDeadMansCoin):
					(global0 setScript: getCoins)
				else:
					(global2 setScript: (ScriptID 30 11) 0 self)
				#endif
			#end:case
			else:
				if (global5 contains: theDeadMansCoin):
					(theDeadMansCoin doVerb: param1 &rest)
				else:
					((ScriptID 30 4) doVerb: param1 &rest)
				#endif
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getCoins(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: PolyPath 127 149 self)
			#end:case
			case 1:
				(global0
					view: 431
					normal: 0
					setLoop: 5
					cel: 0
					cycleSpeed: 10
					setCycle: End self
				)
			#end:case
			case 2:
				(global0 setLoop: 4 cel: 0 setCycle: End self)
			#end:case
			case 3:
				(global0 setCycle: Beg self)
			#end:case
			case 4:
				if (((global9 at: 7) owner:) != global11):
					(global91 say: 8 5 0 1 self 400)
				else:
					(global91 say: 13 5 0 1 self 400)
				#endif
			#end:case
			case 5:
				(global0 reset: 3)
				if (((global9 at: 7) owner:) == global11):
					(global1 givePoints: 1)
					(global0 get: 7)
					(theDeadMansCoin dispose:)
					(theGlint dispose:)
				#endif
				seconds = 1
			#end:case
			case 6:
				(global1 handsOn:)
				(global0 setHeading: 180)
				(theCorpseNorth noun: 8)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class glintCoinEyes(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(theGlint setCycle: Beg self)
			#end:case
			case 1:
				(theGlint hide:)
				seconds = 10
			#end:case
			case 2:
				(state -= 3)
				(theGlint show:)
				(self cue:)
			#end:case
		#end:match
	#end:method

#end:class or instance

