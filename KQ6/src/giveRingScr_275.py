#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 275
import sci_sh
import kernel
import Main
import n913
import Conversation
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	giveRingScr = 0,
)

@SCI.instance
class roomConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class interactionScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(kernel.ScriptID(274, 0) view: 2722 loop: 3 cel: 0 setCycle: End self)
			#end:case
			case 1:
				(kernel.ScriptID(274, 0) stopUpd:)
				cycles = 2
			#end:case
			case 2:
				(self dispose:)
			#end:case
			case 3:
				(kernel.ScriptID(274, 0) view: 273 loop: 0 cel: 0 setCycle: End self)
			#end:case
			case 4:
				(kernel.ScriptID(274, 0) stopUpd:)
				cycles = 2
			#end:case
			case 5:
				(self dispose:)
			#end:case
			case 6:
				(kernel.ScriptID(274, 0) loop: 1 cel: 0 setCycle: End self)
			#end:case
			case 7:
				(kernel.ScriptID(274, 0) stopUpd:)
				cycles = 2
			#end:case
			case 8:
				(self dispose:)
			#end:case
			case 9:
				(kernel.ScriptID(274, 0) view: 2731 loop: 0 cel: 0 setCycle: End self)
			#end:case
			case 10:
				(kernel.ScriptID(274, 0) stopUpd:)
				cycles = 2
			#end:case
			case 11:
				(self dispose:)
			#end:case
			case 12:
				(kernel.ScriptID(274, 0) loop: 1 cel: 0 setCycle: End self)
			#end:case
			case 13:
				(kernel.ScriptID(274, 0) stopUpd:)
				cycles = 2
			#end:case
			case 14:
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose: &rest)
		start = (state + 1)
	#end:method

#end:class or instance

@SCI.instance
class giveRingScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(kernel.ScriptID(274, 0) setScript: 0)
				if register:
					(global91 say: 10 40 9 1 self)
				else:
					(global91 say: 10 70 11 1 self)
				#endif
			#end:case
			case 1:
				(global0
					setSpeed: 6
					normal: 0
					view: 272
					loop: 1
					cel: 0
					setCycle: End self
				)
			#end:case
			case 2:
				(global0 stopUpd:)
				cycles = 2
			#end:case
			case 3:
				kernel.UnLoad(128, 900)
				if register:
					(global91 say: 10 40 9 2 self)
				else:
					(global91 say: 10 70 11 2 self)
				#endif
			#end:case
			case 4:
				(kernel.ScriptID(274, 0) view: 2721 loop: 1 cel: 0 setCycle: End self)
			#end:case
			case 5:
				(kernel.ScriptID(274, 0) stopUpd:)
				cycles = 2
			#end:case
			case 6:
				if register:
					(global91 say: 10 40 9 3 self)
				else:
					(global91 say: 10 70 11 3 self)
				#endif
			#end:case
			case 7:
				(global0 setCycle: Beg self)
			#end:case
			case 8:
				(global0 stopUpd:)
				cycles = 2
			#end:case
			case 9:
				(roomConv
					add: -1 19 0 27 1
					add: interactionScr
					add: -1 19 0 27 2
					add: -1 19 0 27 3
					add: -1 19 0 27 4
					add: interactionScr
					add: -1 19 0 27 5
					add: -1 19 0 27 6
					add: -1 19 0 27 7
					add: -1 19 0 27 8
					add: -1 19 0 27 9
					add: -1 19 0 27 10
					add: interactionScr
					add: -1 19 0 27 11
					add: -1 19 0 27 12
					add: interactionScr
					add: -1 19 0 27 13
					add: -1 19 0 27 14
					add: interactionScr
					add: -1 19 0 27 15
					init: self
				)
			#end:case
			case 10:
				cycles = 2
			#end:case
			case 11:
				(cond
					case proc999_5(global153, 1, 2):
						(global91 say: 10 70 11 4 self oneOnly: 0)
					#end:case
					case (global153 == 3):
						(self setScript: giveRingAct3Scr self)
					#end:case
					case (global153 == 4):
						(self setScript: giveRingAct4Scr self)
					#end:case
				)
			#end:case
			case 12:
				kernel.DisposeScript(1020)
				kernel.DisposeScript(1001)
				cycles = 1
			#end:case
			case 13:
				(kernel.ScriptID(274, 0)
					view: 274
					loop: 0
					cel: 0
					setCycle: CT 3 1 self
				)
			#end:case
			case 14:
				kernel.UnLoad(128, 2721)
				kernel.UnLoad(128, 2722)
				kernel.UnLoad(128, 273)
				kernel.UnLoad(128, 2731)
				(kernel.ScriptID(270, 3) init:)
				cycles = 2
			#end:case
			case 15:
				(global0 startUpd:)
				cycles = 2
			#end:case
			case 16:
				(kernel.ScriptID(274, 0) setCycle: End self)
				(global0
					posn:
						(kernel.ScriptID(274, 0) approachX:)
						(kernel.ScriptID(274, 0) approachY:)
					reset: 1
				)
			#end:case
			case 17:
				kernel.UnLoad(128, 272)
				(client setScript: kernel.ScriptID(274, 1))
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
		register = 0
	#end:method

#end:class or instance

@SCI.instance
class giveRingAct3Scr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global91 say: 10 70 12 1 self)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				(global91 say: 19 0 28 0 self)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				(global91 say: 10 70 12 2 self oneOnly: 0)
			#end:case
			case 5:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class giveRingAct4Scr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global91 say: 10 70 13 0 self)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				proc913_1(52)
				(global91 say: 19 0 29 0 self)
			#end:case
			case 3:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

