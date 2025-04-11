#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 221
import sci_sh
import Main
import n913
import Scaler
import DPath
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	seenVizierScr = 0,
)

@SCI.instance
class egoScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0
					setSpeed: 6
					ignoreActors:
					posn: 75 100
					setPri: 2
					show:
					setMotion: MoveTo 107 94 self
				)
			#end:case
			case 1:
				(global0
					setPri: -1
					setScale: Scaler 100 94 189 95
					setMotion: DPath 118 107 120 111 123 121 self
				)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				(global0 setHeading: 0 self)
			#end:case
			case 4:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class seenVizierScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 hide:)
				(proc913_1 72)
				((ScriptID 220 5) setCycle: End self)
			#end:case
			case 1:
				(self setScript: egoScr)
				ticks = 30
			#end:case
			case 2:
				((ScriptID 220 6) init: setMotion: MoveTo 105 94 self)
			#end:case
			case 3:
				((ScriptID 220 6)
					setPri: -1
					setScale: Scaler 100 94 189 95
					setMotion: DPath 115 107 117 111 118 115 self
				)
			#end:case
			case 4:
				((ScriptID 220 6) setHeading: 180 self)
			#end:case
			case 5:
				if script:
					state--
				#endif
				cycles = 2
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				(global91 say: 1 0 5 1 self)
			#end:case
			case 8:
				(global91 say: 1 0 5 2 self)
			#end:case
			case 9:
				((ScriptID 220 6) setMotion: MoveTo 117 111 self)
			#end:case
			case 10:
				cycles = 2
			#end:case
			case 11:
				(global91 say: 1 0 5 3 self)
			#end:case
			case 12:
				((ScriptID 220 6) setMotion: DPath 115 107 105 94 self)
			#end:case
			case 13:
				((ScriptID 220 6) cue: self)
			#end:case
			case 14:
				((ScriptID 220 6) dispose:)
				(self setScript: (ScriptID 220 2) self)
			#end:case
			case 15:
				(global91 say: 1 0 5 4 self)
			#end:case
			case 16:
				(global0 reset: 3)
				(global1 handsOn:)
				((ScriptID 220 5) stopUpd:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
		(DisposeScript 221)
	#end:method

#end:class or instance

