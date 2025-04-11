#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 455
import sci_sh
import Main
import rm450
import n913
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	smellGnome = 0,
)

@SCI.instance
class smellGnome(Gnome):
	#property vars (may be empty)
	x = 197
	noun = 14
	view = 455
	EOLx = 105
	FOLx = 157
	startPoint = 4
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self gnomeScript: smellScript setScript: smellInit stopUpd:)
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 == 1):
			(global91 say: noun param1 22 1 0 450)
		else:
			((ScriptID 450 6) setScript: smellScript 0 param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class smellInit(Script):
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
				(global91 say: 14 0 24 1 self 450)
			#end:case
			case 2:
				(((ScriptID 450 6) script:) cue:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class smellScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				cycles = 6
			#end:case
			case 1:
				match register
					case 47:
						(global91 say: 14 47 24 1 self 450)
					#end:case
					case 83:
						(self cue:)
					#end:case
					case 31:
						(self cue:)
					#end:case
					case 37:
						(global91 say: 2 37 42 1 self 450)
					#end:case
					else:
						(global91 say: 14 0 24 2 self 450)
					#end:else
				#end:match
			#end:case
			case 2:
				(self setScript: (ScriptID 450 2) self register)
			#end:case
			case 3:
				(global104 number: 453 setLoop: 1 play:)
				(smellGnome setLoop: 1 cel: 0 setCycle: End self)
			#end:case
			case 4:
				if (register == 47):
					(smellGnome
						setLoop: 4
						cel: 0
						cycleSpeed: 12
						setCycle: End self
					)
				else:
					(self setScript: failScript 0 register)
				#endif
			#end:case
			case 5:
				(smellGnome setLoop: 3 cycleSpeed: 6)
				(smellGnome cel: (smellGnome lastCel:) setCycle: Beg self)
			#end:case
			case 6:
				(smellGnome cycleSpeed: 6 setLoop: 0 cel: 0)
				(global0 setCycle: End self)
			#end:case
			case 7:
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
			case 8:
				(global91 say: 14 47 24 2 self 450)
			#end:case
			case 9:
				((ScriptID 450 6) setScript: (ScriptID 450 3) 0 smellGnome)
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
				if (not register):
					(smellGnome setLoop: 1 cel: 0 setCycle: End self)
					(global104 number: 453 setLoop: 1 play:)
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				(smellGnome setLoop: 2 cel: 0 setCycle: End self)
			#end:case
			case 3:
				(proc913_1 59)
				if (not register):
					(global91 say: 16 0 33 1 self 450)
				else:
					(global91 say: 14 0 24 3 self 450)
				#endif
			#end:case
			case 4:
				(smellGnome setLoop: 3 cycleSpeed: 6)
				(smellGnome cel: (smellGnome lastCel:) setCycle: Beg self)
				(proc913_2 59)
			#end:case
			case 5:
				(self setScript: (ScriptID 450 4) self register)
			#end:case
			case 6:
				(global91 say: 16 0 29 1 self 450)
			#end:case
			case 7:
				(smellGnome addToPic: delete: dispose:)
				cycles = 10
			#end:case
			case 8:
				((ScriptID 450 6) setScript: (ScriptID 450 5))
			#end:case
		#end:match
	#end:method

#end:class or instance

