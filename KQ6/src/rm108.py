#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 108
import sci_sh
import Main
import KQ6Room
import System

# Public Export Declarations
SCI.public_exports(
	rm108 = 0,
)

@SCI.instance
class rm108(KQ6Room):
	#property vars (may be empty)
	picture = 98
	autoLoad = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global1 handsOff:)
		(global69 disable: height: -100 activateHeight: -100)
		(global74 addToFront: self)
		(global72 addToFront: self)
		(global73 addToFront: self)
		(super init: &rest)
		(self setScript: sShowMovieWin)
	#end:method

	@classmethod
	def handleEvent():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(ShowMovie 3)
		(ShowMovie 6)
		(global69 disable: height: 0 activateHeight: 0)
		(global1 restart: 1)
	#end:method

	@classmethod
	def newRoom():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global74 delete: self)
		(global72 delete: self)
		(global73 delete: self)
		(global69 disable: height: 0 activateHeight: 0)
		(super newRoom: &rest)
	#end:method

#end:class or instance

@SCI.instance
class sShowMovieWin(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				cycles = 10
			#end:case
			case 1:
				if (not (ShowMovie 0 r"""toon.avi""")):
					(ShowMovie 1 0 0)
					(ShowMovie 2 0 self)
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				(ShowMovie 6)
				cycles = 1
			#end:case
			case 3:
				(global2 newRoom: 200)
			#end:case
		#end:match
	#end:method

#end:class or instance

