#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 82
import sci_sh
import kernel
import Main
import n913
import Inset
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	keyHoleScr = 0,
	keyHoleView = 1,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


@SCI.instance
class keyHoleScr(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		proc913_1(49)
		(super init: &rest)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		proc913_2(49)
		register = 0
		(super dispose:)
		(global1 handsOn:)
		kernel.DisposeScript(82)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				local0 = (global0 loop:)
				(global0
					view: 701
					normal: 0
					cycleSpeed: 8
					loop:
						(cond
							case (<= 225 (global0 heading:) 315): 1#end:case
							case (<= 45 (global0 heading:) 135): 0#end:case
							else: 2#end:else
						)
					cel: 0
					setCycle: End self
				)
			#end:case
			case 1:
				(global1 handsOn:)
				(global69 disable: 0 1 3 4 5 6)
				(keyHole init: 0 global2)
				if register:
					(self setScript: register self)
				else:
					seconds = 5
				#endif
			#end:case
			case 2:
				(global1 handsOff:)
				if (not register):
					(keyHole dispose:)
				#endif
				cycles = 1
			#end:case
			case 3:
				(global0 setCycle: Beg self)
			#end:case
			case 4:
				(global1 handsOn:)
				(global69 enable: 6)
				(global0 reset: local0)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class keyHole(Inset):
	#property vars (may be empty)
	view = 796
	priority = 15
	disposeNotOnMe = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global0 stopUpd:)
		x = (160 - (kernel.CelWide(view, loop, cel) / 2))
		y = (100 - (kernel.CelHigh(view, loop, cel) / 2))
		(super init: &rest)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if script:
			(script doit:)
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(keyHoleView dispose:)
		((keyHoleScr script:) dispose:)
		(super dispose:)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(not
				(and
					(keyHoleView actions:)
					((keyHoleView actions:) doVerb: param1)
				)
			)
			(super doVerb: param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class keyHoleView(View):
	#property vars (may be empty)
	@classmethod
	def init(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		x = ((keyHole x:) + 92)
		y = ((keyHole y:) + 54)
		view = param1[loop = cel = 0]
		if (argc > 1):
			loop = param1[1]
			if (argc > 2):
				cel = param1[2]
				if (argc > 3):
					x = (param1[3] + (keyHole x:))
					if (argc > 4):
						y = (param1[4] + (keyHole y:))
					#endif
				#endif
			#endif
		#endif
		(super init: &rest)
		(keyHole noun: noun)
		(self setPri: 13 sightAngle: 180 stopUpd:)
	#end:method

#end:class or instance

