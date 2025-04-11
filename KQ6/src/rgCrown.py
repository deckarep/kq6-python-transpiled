#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 10
import sci_sh
import kernel
import Main
import Feature
import Game
import System

# Public Export Declarations
SCI.public_exports(
	rgCrown = 0,
	proc10_2 = 2,
	rocks = 4,
)

@SCI.procedure
def proc10_2(param1 = None, param2 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	if (global2 script:):
		((global2 script:)
			setScript: param1 (global2 script:) (param2 if (argc > 1) else 0)
		)
	else:
		(global2 setScript: param1 0 (param2 if (argc > 1) else 0))
	#endif
#end:procedure

class rgCrown(Rgn):
	#property vars (may be empty)
	flag1 = 0
	flag2 = 0
	singSingHas = 0
	
	@classmethod
	def isSet(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			if (argc < 2):
				(flag1 & param1)
			else:
				(flag2 & param2)
			#endif
		)
	#end:method

	@classmethod
	def clrIt(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (argc < 2):
			(flag1 &= (~ param1))
		else:
			(flag2 &= (~ param2))
		#endif
	#end:method

	@classmethod
	def setIt(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (argc < 2):
			(flag1 |= param1)
		else:
			(flag2 |= param2)
		#endif
	#end:method

	@classmethod
	def newRoom(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		keep = proc999_5(param1, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290)
		initialized = 0
		(super newRoom: param1 &rest)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
	#end:method

#end:class or instance

@SCI.instance
class rocks(Feature):
	#property vars (may be empty)
	noun = 2
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if proc999_5(param1, 1, 5, 2):
			(global91 say: noun param1 (1 if (param1 == 1) else 0) 0 0 0)
		else:
			(global91 say: noun 0 0 0 0 0)
		#endif
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		sightAngle = 26505
	#end:method

#end:class or instance

