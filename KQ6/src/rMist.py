#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 60
import sci_sh
import Main
import n913
import Game
import System

# Public Export Declarations
SCI.public_exports(
	rMist = 0,
)

class rMist(Rgn):
	#property vars (may be empty)
	seenFirstMessage = 0
	musicPlaying = 0
	
	@classmethod
	def newRoom(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		keep = (proc999_5 param1 550 560 570 580)
		initialized = 0
		(super newRoom: param1 &rest)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		if (((global11 == 550) or (global11 == 560)) and (not (proc913_0 14))):
			if (not musicPlaying):
				(global102 number: 551 loop: -1 play:)
				musicPlaying = 1
			#endif
			(self setScript: hintDrums)
		#endif
		if (global11 == 580):
			(global102 stop:)
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global102 stop:)
		(proc913_1 25)
		(super dispose:)
	#end:method

#end:class or instance

@SCI.instance
class hintDrums(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				seconds = 3
			#end:case
			case 1:
				(cond
					case (proc913_0 74):
						(self dispose:)
					#end:case
					case (global2 script:):
						(self init:)
					#end:case
					case (global11 == 550):
						(global91 say: 1 0 5 1 self)
					#end:case
					case (global11 == 560):
						(global91 say: 1 0 1 1 self)
					#end:case
				)
			#end:case
			case 2:
				seconds = 27
			#end:case
			case 3:
				(self init:)
			#end:case
		#end:match
	#end:method

#end:class or instance

