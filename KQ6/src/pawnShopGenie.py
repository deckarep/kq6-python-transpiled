#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 281
import sci_sh
import kernel
import Main
import n913
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	pawnShopGenie = 0,
	proc281_1 = 1,
)

@SCI.procedure
def proc281_1(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	if (global5 contains: eye):
		(eye dispose:)
	#endif
	(pawnShopGenie cycleSpeed: 6)
	(genieBrowseScr caller: param1 dispose:)
#end:procedure

@SCI.instance
class pawnShopGenie(Actor):
	#property vars (may be empty)
	x = 85
	y = 131
	noun = 5
	approachX = 117
	approachY = 133
	view = 2831
	signal = 16384
	cycleSpeed = 75
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 13:
				(global2 setScript: kernel.ScriptID(282, 3))
			#end:case
			case 67:
				(global0 put: 31 -1)
				(global2 setScript: kernel.ScriptID(282, 6))
			#end:case
			case 2:
				if proc999_5(global153, 4, 5):
					(global91 say: noun param1 (68 if proc913_1(122) else 1))
				else:
					(super doVerb: param1 &rest)
				#endif
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		(self approachVerbs: 2 0)
		if param1:
			(self setScript: genieBrowseScr)
		else:
			(global2 setScript: kernel.ScriptID(282, 4))
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super dispose:)
		(self delete:)
		kernel.DisposeScript(281)
	#end:method

#end:class or instance

@SCI.instance
class eye(Prop):
	#property vars (may be empty)
	x = 92
	y = 92
	view = 902
	priority = 10
	signal = 16
	
#end:class or instance

@SCI.instance
class genieBrowseScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(pawnShopGenie view: 2831 loop: 0 cel: 0)
				(self cue:)
			#end:case
			case 1:
				(pawnShopGenie cycleSpeed: kernel.Random(30, 75) setCycle: CT 3 1 self)
			#end:case
			case 2:
				ticks = kernel.Random(60, 120)
			#end:case
			case 3:
				if (((global0 x:) > 67) and proc999_5(kernel.Random(0, 2), 0, 1)):
					(eye init: cel: 0 cycleSpeed: 12 setCycle: End self)
				else:
					(self cue:)
				#endif
			#end:case
			case 4:
				ticks = 6
			#end:case
			case 5:
				(eye dispose:)
				ticks = kernel.Random(60, 120)
			#end:case
			case 6:
				(pawnShopGenie setCycle: End self)
			#end:case
			case 7:
				state = -1
				ticks = 25
			#end:case
		#end:match
	#end:method

#end:class or instance

