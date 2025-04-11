#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 1015
import sci_sh
import Main
import Kq6Window
import Talker
import System

# Public Export Declarations
SCI.public_exports(
	tlkGuardDog1 = 6,
	tlkGuardDog2 = 7,
	tlkGuardDog = 8,
)

@SCI.instance
class tlkGuardDog(Narrator):
	#property vars (may be empty)
	y = 10
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		font = global22
		keepWindow = 1
		color = (Kq6Window color:)
		back = (Kq6Window back:)
		(super init: &rest)
	#end:method

#end:class or instance

@SCI.instance
class tlkGuardDog1(Narrator):
	#property vars (may be empty)
	y = 10
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		font = global22
		keepWindow = 1
		color = (Kq6Window color:)
		back = (Kq6Window back:)
		(cond
			case (global11 == 800):
				x = 100
				y = 119
				talkWidth = 190
			#end:case
			case (proc999_5 global11 850 880 820 180 860 730): 0#end:case
			else:
				x = -1
				y = 10
			#end:else
		)
		(super init: &rest)
	#end:method

#end:class or instance

@SCI.instance
class tlkGuardDog2(Narrator):
	#property vars (may be empty)
	y = 10
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		font = global22
		keepWindow = 1
		color = (Kq6Window color:)
		back = (Kq6Window back:)
		(cond
			case (global11 == 800):
				x = 10
				y = 65
				talkWidth = 96
			#end:case
			case (proc999_5 global11 850 880 820): 0#end:case
			else:
				x = -1
				y = 10
			#end:else
		)
		(super init: &rest)
	#end:method

#end:class or instance

