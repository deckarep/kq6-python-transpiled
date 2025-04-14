#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 52
import sci_sh
import kernel
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
		if (not register):
			global5._send('eachElementDo:', #addToPic)
			global69._send('disable:')
			Cursor._send('showCursor:', 0)
			kernel.Load(135, 2207, 3110)
			kernel.Load(143, 194)
			kernel.Load(129, 98, 99)
			songTimer._send('setReal:', self, 240)
			if ((global90 == 2) and kernel.DoAudio(10, 10)):
				kernel.DoAudio(10, 2, 2, 0, 236)
			else:
				global102._send('number:', 24, 'loop:', 1, 'play:', self)
			#endif
			register.post('++')
		#endif
		super._send('init:', &rest)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if local1:
					kernel.Message(0, 194, 3, 0, 0, local0, @temp0)
					kernel.Message(0, 194, 3, 0, 0, local0.post('++'), @temp50)
				else:
					kernel.Message(0, 194, 0, 0, 0, local0, @temp0)
					kernel.Message(0, 194, 0, 0, 0, local0.post('++'), @temp50)
				#endif
				if (local0.post('++') >= 32):
					local1 = 1
					local0 = 1
				#endif
				(= local2
					kernel.Display(@temp0, 102, 0, 100, 64, 61, 106, 200, 105, 3110, 101, 1, 107)
				)
				(= local3
					kernel.Display(@temp50, 102, 0, 100, 64, 81, 106, 200, 105, 2207, 101, 1, 107)
				)
				(= local4
					kernel.Display(@temp0, 102, 7, 100, 63, 60, 106, 200, 105, 3110, 101, 1, 107)
				)
				(= local5
					kernel.Display(@temp50, 102, 7, 100, 63, 80, 106, 200, 105, 2207, 101, 1, 107)
				)
				seconds = 6
			#end:case
			case 1:
				kernel.Display(52, 0, 108, local5)
				kernel.Display(52, 0, 108, local4)
				kernel.Display(52, 0, 108, local3)
				kernel.Display(52, 0, 108, local2)
				if ((not local1) and (local0 == 15)):
					temp550 = 100
					while (temp550 > 0): # inline for
						kernel.Palette(4, 0, 255, temp550)
						temp551 = 0
						while (temp551 < 10): # inline for
						#end:loop
						# for:reinit
						temp550.post('--')
					#end:loop
					if global169:
						kernel.DrawPic(98, 15)
					else:
						kernel.DrawPic(98)
					#endif
				#endif
				cycles = 2
			#end:case
			case 2:
				if ((not local1) and (local0 == 15)):
					kernel.Palette(4, 0, 231, 100)
				#endif
				if (local1 and (local0 == 1) and local6):
					cycles = 2
				else:
					if local1:
						local6 = 1
					#endif
					self._send('init:')
				#endif
			#end:case
			case 3:
				if (global15 == global16):
					kernel.Format(@temp50, r"""You received %d out of %d points. You've completed %d percent of the main-path puzzles in King's Quest VI.""", global15, global16, (/
						(global15 * 100)
						global16
					))
				else:
					kernel.Format(@temp50, r"""You received %d out of %d points. You've completed approximately %d percent of the main-path puzzles in King's Quest VI.""", global15, global16, (/
						(global15 * 100)
						global16
					))
				#endif
				(= local2
					kernel.Display(@temp50, 102, 7, 100, 64, 60, 106, 200, 105, 3110, 101, 1, 107)
				)
				seconds = 9
			#end:case
			case 4:
				kernel.Display(52, 0, 108, local2)
				cycles = 2
			#end:case
			case 5:
				if (global15 <= 230):
					kernel.Message(0, 194, 0, 0, 1, 2, @temp50)
				else:
					kernel.Message(0, 194, 0, 0, 1, 3, @temp50)
				#endif
				kernel.Display(@temp50, 102, 7, 100, 64, 60, 106, 200, 105, global23, 101, 1)
				seconds = 20
			#end:case
			case 6:
				if global169:
					kernel.DrawPic(99, 15)
				else:
					kernel.DrawPic(99)
				#endif
				Cursor._send('showCursor:', 1)
			#end:case
			case 7:
				temp550 = 100
				while (temp550 > 0): # inline for
					kernel.Palette(4, 0, 255, temp550)
					temp551 = 0
					while (temp551 < 10): # inline for
					#end:loop
					# for:reinit
					temp550.post('--')
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

