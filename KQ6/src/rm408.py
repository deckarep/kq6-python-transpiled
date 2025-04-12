#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 408
import sci_sh
import kernel
import Main
import rLab
import n402
import PolyPath
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm408 = 0,
)

@SCI.instance
class rm408(LabRoom):
	#property vars (may be empty)
	north = 400
	south = 400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		proc402_0()
		(super init: &rest)
		if (((global9 at: 43) owner:) == 408):
			(theShield init:)
		#endif
		(global2 setScript: kernel.ScriptID(30, 1))
		(kernel.ScriptID(30, 7) addToPic:)
		(kernel.ScriptID(30, 0) initCrypt: 2)
	#end:method

	@classmethod
	def notify():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(kernel.ScriptID(30, 7) addToPic:)
		(kernel.ScriptID(30, 3) show:)
	#end:method

#end:class or instance

@SCI.instance
class theShield(View):
	#property vars (may be empty)
	x = 66
	y = 150
	z = 40
	noun = 15
	modNum = 400
	view = 400
	loop = 4
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				(global2 setScript: getShield)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getShield(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: PolyPath 84 149 self)
			#end:case
			case 1:
				(theShield hide:)
				(global0
					normal: 0
					view: 401
					setLoop: 0
					posn: 75 152
					cycleSpeed: 8
					setCycle: End self
				)
			#end:case
			case 2:
				(global91 say: 15 5 0 1 self 400)
			#end:case
			case 3:
				(global1 givePoints: 1)
				(theShield dispose:)
				(global0 posn: 84 149 get: 43 reset: 1)
				cycles = 2
			#end:case
			case 4:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

