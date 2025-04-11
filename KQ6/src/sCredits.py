#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 52
import sci_sh
import Main
import Timer
import System

# Public Export Declarations
SCI.public_exports(
	sCredits = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = 1
local1 = None
local2 = None
local3 = None
local4 = None
local5 = None
local6 = None


@SCI.instance
class sCredits(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not register):
			(global5 eachElementDo: #addToPic)
			(global69 disable:)
			(Cursor showCursor: 0)
			(Load 135 2207 3110)
			(Load 143 194)
			(Load 129 98 99)
			(songTimer setReal: self 240)
			if ((global90 == 2) and (DoAudio 10 10)):
				(DoAudio 10 2 2 0 236)
			else:
				(global102 number: 24 loop: 1 play: self)
			#endif
			register++
		#endif
		(super init: &rest)
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				if local1:
					(Message 0 194 3 0 0 local0 @temp0)
					(Message 0 194 3 0 0 local0++ @temp50)
				else:
					(Message 0 194 0 0 0 local0 @temp0)
					(Message 0 194 0 0 0 local0++ @temp50)
				#endif
				if (local0++ >= 32):
					local1 = 1
					local0 = 1
				#endif
				(= local2
					(Display @temp0 102 0 100 64 61 106 200 105 3110 101 1 107)
				)
				(= local3
					(Display @temp50 102 0 100 64 81 106 200 105 2207 101 1 107)
				)
				(= local4
					(Display @temp0 102 7 100 63 60 106 200 105 3110 101 1 107)
				)
				(= local5
					(Display @temp50 102 7 100 63 80 106 200 105 2207 101 1 107)
				)
				seconds = 6
			#end:case
			case 1:
				(Display 52 0 108 local5)
				(Display 52 0 108 local4)
				(Display 52 0 108 local3)
				(Display 52 0 108 local2)
				if ((not local1) and (local0 == 15)):
					temp550 = 100
					while (temp550 > 0): # inline for
						(Palette 4 0 255 temp550)
						temp551 = 0
						while (temp551 < 10): # inline for
						#end:loop
						# for:reinit
						temp550--
					#end:loop
					if global169:
						(DrawPic 98 15)
					else:
						(DrawPic 98)
					#endif
				#endif
				cycles = 2
			#end:case
			case 2:
				if ((not local1) and (local0 == 15)):
					(Palette 4 0 231 100)
				#endif
				if (and local1 (local0 == 1) local6):
					cycles = 2
				else:
					if local1:
						local6 = 1
					#endif
					(self init:)
				#endif
			#end:case
			case 3:
				if (global15 == global16):
					(Format
						@temp50
						r"""You received %d out of %d points. You've completed %d percent of the main-path puzzles in King's Quest VI."""
						global15
						global16
						((global15 * 100) / global16)
					)
				else:
					(Format
						@temp50
						r"""You received %d out of %d points. You've completed approximately %d percent of the main-path puzzles in King's Quest VI."""
						global15
						global16
						((global15 * 100) / global16)
					)
				#endif
				(= local2
					(Display @temp50 102 7 100 64 60 106 200 105 3110 101 1 107)
				)
				seconds = 9
			#end:case
			case 4:
				(Display 52 0 108 local2)
				cycles = 2
			#end:case
			case 5:
				if (global15 <= 230):
					(Message 0 194 0 0 1 2 @temp50)
				else:
					(Message 0 194 0 0 1 3 @temp50)
				#endif
				(Display @temp50 102 7 100 64 60 106 200 105 global23 101 1)
				seconds = 20
			#end:case
			case 6:
				if global169:
					(DrawPic 99 15)
				else:
					(DrawPic 99)
				#endif
				(Cursor showCursor: 1)
			#end:case
			case 7:
				temp550 = 100
				while (temp550 > 0): # inline for
					(Palette 4 0 255 temp550)
					temp551 = 0
					while (temp551 < 10): # inline for
					#end:loop
					# for:reinit
					temp550--
				#end:loop
				cycles = 5
			#end:case
			case 8:
				global4 = 1
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class songTimer(Timer):
	#property vars (may be empty)
#end:class or instance

