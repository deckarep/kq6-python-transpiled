#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 301
import sci_sh
import kernel
import Main
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	proc301_0 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


@SCI.procedure
def proc301_0():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	(global2 setScript: flyIn)
#end:procedure

@SCI.instance
class guard1(Actor):
	#property vars (may be empty)
	yStep = 8
	signal = 24576
	cycleSpeed = 3
	illegalBits = 0
	xStep = 12
	
#end:class or instance

@SCI.instance
class guard2(Actor):
	#property vars (may be empty)
	yStep = 8
	signal = 24576
	cycleSpeed = 3
	illegalBits = 0
	xStep = 12
	
#end:class or instance

@SCI.instance
class dummyEgo(Actor):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class flyIn(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global0 hide:)
				(global69 disable:)
				(dummyEgo
					view: 3511
					setStep: 12 8
					ignoreHorizon: 1
					posn: 340 -40
					init:
					setCycle: Fwd
					setMotion: MoveTo 228 56 self
				)
			#end:case
			case 1:
				(dummyEgo view: 3512 cel: 0 posn: 195 91 setCycle: End self)
				kernel.UnLoad(128, 3511)
			#end:case
			case 2:
				kernel.UnLoad(128, 3512)
				(guard1 view: 3013 loop: 0 cel: 1 posn: 169 128 init: stopUpd:)
				(guard2
					view: 3013
					loop: 0
					cel: 0
					posn: 173 132
					setPri: ((guard1 priority:) - 2)
					init:
					stopUpd:
				)
				(global0
					reset: 1
					cel: 4
					posn: 162 129
					setPri: ((guard1 priority:) - 1)
					show:
					setMotion: MoveTo 145 129 self
				)
				(dummyEgo dispose:)
				(global102 fade:)
			#end:case
			case 3:
				(global0 setHeading: 180 self)
			#end:case
			case 4:
				(guard1
					view: 344
					loop: 1
					setCycle: Walk
					setMotion: MoveTo ((guard1 x:) + 15) (guard1 y:)
				)
				(guard2
					view: 343
					loop: 1
					setCycle: Walk
					setMotion: MoveTo ((guard2 x:) + 15) (guard2 y:) self
				)
			#end:case
			case 5:
				(global102
					number: 915
					setLoop: -1
					setVol: 0
					play:
					fade: 127 10 10
				)
				(global0 setHeading: 90 self)
			#end:case
			case 6:
				(global0 view: 3013 loop: 0 cel: 2)
				kernel.UnLoad(128, 900)
				cycles = 8
			#end:case
			case 7:
				(guard1 view: 349 loop: 0 cel: 0 setCycle: End)
				kernel.UnLoad(128, 344)
				(guard2 view: 348 loop: 0 cel: 0 setCycle: End self)
				kernel.UnLoad(128, 343)
			#end:case
			case 8:
				(guard1
					view: 3491
					loop: 0
					cel: 0
					posn: 195 74
					setCycle: Fwd
					setStep: 12 8
					cycleSpeed: 3
					setMotion: MoveTo 345 -15 self
				)
				kernel.UnLoad(128, 349)
				(guard2
					view: 3481
					loop: 0
					cel: 0
					posn: 219 80
					setCycle: Fwd
					setStep: 12 8
					cycleSpeed: 3
					setMotion: MoveTo 375 -15
				)
				kernel.UnLoad(128, 348)
			#end:case
			case 9:
				if (not (global12 == 380)):
					(Cursor showCursor: 1)
				#endif
				(global0 reset: 0)
				(guard1 setCycle: 0 setMotion: 0 delete: dispose:)
				(guard2 setCycle: 0 setMotion: 0 delete: dispose:)
				(global69 enable:)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

