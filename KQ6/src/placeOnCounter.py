#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 287
import sci_sh
import kernel
import Main
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	placeOnCounter = 0,
	getFromCounter = 1,
)

@SCI.instance
class placeOnCounter(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0
					put:
						match register
							case 0: 48#end:case
							case 3: 27#end:case
							case 1: 3#end:case
							case 2: 14#end:case
						#end:match
						global11
				)
				(self setScript: kernel.ScriptID(286, 2) 0 register)
			#end:case
			case 1:
				(client cue:)
			#end:case
			case 2:
				(kernel.ScriptID(280, 2)
					posn: 236 116
					view: 284
					loop: 3
					cel: 0
					cycleSpeed: 9
				)
				ticks = 6
			#end:case
			case 3:
				(kernel.ScriptID(280, 2) setCycle: CT 1 1 self)
			#end:case
			case 4:
				ticks = 6
			#end:case
			case 5:
				(script cue:)
				(kernel.ScriptID(280, 2)
					setPri: 14
					view: (2842 if proc999_5(register, 3, 2) else 2843)
					loop:
						match register
							case 3: 0#end:case
							case 2: 1#end:case
							case 0: 0#end:case
							case 1: 1#end:case
						#end:match
					cel: 0
				)
				ticks = 6
			#end:case
			case 6:
				(kernel.ScriptID(280, 2) setCycle: CT 3 1 self)
			#end:case
			case 7:
				match register
					case 0:
						(kernel.ScriptID(280, 5) init:)
					#end:case
					case 2:
						(kernel.ScriptID(280, 6) init:)
					#end:case
					case 3:
						(kernel.ScriptID(280, 4) init:)
					#end:case
					case 1:
						(kernel.ScriptID(280, 7) init:)
					#end:case
				#end:match
				cycles = 2
			#end:case
			case 8:
				if ((kernel.ScriptID(280, 2) lastCel:) != (kernel.ScriptID(280, 2) cel:)):
					(kernel.ScriptID(280, 2) setCycle: End self)
				else:
					cycles = 2
				#endif
			#end:case
			case 9:
				ticks = 6
			#end:case
			case 10:
				(kernel.ScriptID(280, 2)
					setPri: -1
					posn: 236 127
					view: 280
					loop: 8
					cel: 0
					cycleSpeed: 6
				)
				cycles = 2
			#end:case
			case 11:
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
		kernel.DisposeScript(287)
	#end:method

#end:class or instance

@SCI.instance
class getFromCounter(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(kernel.ScriptID(280, 2)
					view: (2842 if proc999_5(register, 3, 2) else 2843)
					posn: 236 116
					setPri: 14
					loop:
						match register
							case 3: 0#end:case
							case 2: 1#end:case
							case 0: 0#end:case
							case 1: 1#end:case
						#end:match
					cel: 2
				)
				(global0
					get:
						match register
							case 0: 48#end:case
							case 3: 27#end:case
							case 1: 3#end:case
							case 2: 14#end:case
						#end:match
				)
				match register
					case 0:
						(kernel.ScriptID(280, 5) dispose:)
					#end:case
					case 2:
						(kernel.ScriptID(280, 6) dispose:)
					#end:case
					case 3:
						(kernel.ScriptID(280, 4) dispose:)
					#end:case
					case 1:
						(kernel.ScriptID(280, 7) dispose:)
					#end:case
				#end:match
				cycles = 3
			#end:case
			case 1:
				(kernel.ScriptID(280, 2) setCycle: Beg self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				(self setScript: kernel.ScriptID(286, 2) self)
			#end:case
			case 4:
				(script register: register cue:)
				(kernel.ScriptID(280, 2)
					view: 284
					setPri: -1
					loop: 3
					cel: 1
					setCycle: Beg self
				)
			#end:case
			case 5: 0#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				(kernel.ScriptID(280, 2) posn: 236 127 view: 280 loop: 8 cel: 0)
				cycles = 2
			#end:case
			case 8:
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
		kernel.DisposeScript(287)
	#end:method

#end:class or instance

