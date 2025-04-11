#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 456
import sci_sh
import Main
import rm450
import n913
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	soundGnome = 0,
)

@SCI.instance
class soundGnome(Gnome):
	#property vars (may be empty)
	x = 191
	noun = 15
	view = 456
	EOLx = 99
	FOLx = 146
	startPoint = 2
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self gnomeScript: soundScript setScript: soundInit stopUpd:)
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 == 1):
			(global91 say: noun param1 22 1 0 450)
		else:
			((ScriptID 450 6) setScript: soundScript 0 param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class soundInit(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				seconds = 1
			#end:case
			case 1:
				(global91 say: 15 0 12 1 self 450)
			#end:case
			case 2:
				(((ScriptID 450 6) script:) cue:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class soundScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				match register
					case 37:
						(global91 say: 15 37 12 1 self 450)
					#end:case
					case 83:
						(self cue:)
					#end:case
					case 31:
						(proc913_1 59)
						(global91 say: 15 31 12 1 self 450)
					#end:case
					else:
						(global91 say: 15 0 12 2 self 450)
					#end:else
				#end:match
			#end:case
			case 1:
				(self setScript: (ScriptID 450 2) self register)
			#end:case
			case 2:
				if (register == 37):
					(soundGnome setLoop: 4 cel: 0 setCycle: End self)
				else:
					(self setScript: failScript 0 register)
				#endif
			#end:case
			case 3:
				(soundGnome setLoop: 3 cycleSpeed: 6)
				(soundGnome cel: (soundGnome lastCel:) setCycle: Beg self)
			#end:case
			case 4:
				(soundGnome setLoop: 0 cel: 0)
				(global0 setCycle: End self)
			#end:case
			case 5:
				if ((ScriptID 40 0) alexX:):
					(global0
						posn: ((ScriptID 40 0) alexX:) ((ScriptID 40 0) alexY:)
					)
				#endif
				if ((global0 view:) != 900):
					(global0 reset: 1)
				#endif
				cycles = 6
			#end:case
			case 6:
				(global91 say: 15 37 12 2 self 450)
			#end:case
			case 7:
				((ScriptID 450 6) setScript: (ScriptID 450 3) 0 soundGnome)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class failScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(cond
					case (((ScriptID 40 0) alexInvisible:) or (register == 31)):
						(self state: (state + 1) cue:)
					#end:case
					case register:
						(global0 setCycle: End self)
					#end:case
					else:
						cycles = 1
					#end:else
				)
			#end:case
			case 1:
				if ((ScriptID 40 0) alexX:):
					(global0
						posn: ((ScriptID 40 0) alexX:) ((ScriptID 40 0) alexY:)
					)
				#endif
				if ((global0 view:) != 900):
					(global0 reset: 1)
				#endif
				cycles = 2
			#end:case
			case 2:
				(soundGnome setLoop: 2 cel: 0 setCycle: End self)
			#end:case
			case 3:
				(soundGnome setCycle: Beg self)
			#end:case
			case 4:
				(proc913_1 59)
				(cond
					case (not register):
						(global91 say: 16 0 34 1 self 450)
					#end:case
					case (register == 31):
						(global91 say: 15 31 12 2 self 450)
					#end:case
					else:
						(global91 say: 15 0 12 3 self 450)
					#end:else
				)
			#end:case
			case 5:
				(soundGnome setLoop: 3 cycleSpeed: 6)
				(soundGnome cel: (soundGnome lastCel:) setCycle: Beg self)
				(proc913_2 59)
			#end:case
			case 6:
				(self setScript: (ScriptID 450 4) self register)
			#end:case
			case 7:
				(global91 say: 16 0 30 1 self 450)
			#end:case
			case 8:
				(soundGnome addToPic: delete: dispose:)
				cycles = 10
			#end:case
			case 9:
				((ScriptID 450 6) setScript: (ScriptID 450 5))
			#end:case
		#end:match
	#end:method

#end:class or instance

