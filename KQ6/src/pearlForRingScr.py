#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 285
import sci_sh
import kernel
import Main
import rm280
import System

# Public Export Declarations
SCI.public_exports(
	pearlForRingScr = 0,
	pearlForMapScr = 1,
	mapForPearlOrRingScr = 2,
)

@SCI.instance
class pearlForRingScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global0 put: 30 global11 get: 39)
				(global1 handsOff:)
				proc280_10(self)
				(global0 normal: 0 view: 280 loop: 7 cel: 0)
				cycles = 2
			#end:case
			case 1:
				kernel.UnLoad(128, 900)
			#end:case
			case 2:
				if register:
					register = 27
					(self setScript: kernel.ScriptID(286, 1) self)
				else:
					register = 26
					(global1 givePoints: 2)
					(self setScript: kernel.ScriptID(286, 1) self 16384)
				#endif
			#end:case
			case 3:
				(global91 say: 4 66 register 1 kernel.ScriptID(286, 1))
			#end:case
			case 4:
				(global91
					say:
						4
						66
						register
						2
						if (register == 26):
							kernel.ScriptID(286, 1)
						else:
							self
						#endif
				)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				(self setScript: kernel.ScriptID(286, 0) self 1)
			#end:case
			case 7:
				(global91 say: 4 66 register 3 self)
			#end:case
			case 8:
				if (register == 27):
					state.post('++')
				#endif
				ticks = 1
			#end:case
			case 9:
				(global91 say: 4 66 register 4 self)
			#end:case
			case 10:
				(kernel.ScriptID(280, 2) setScript: kernel.ScriptID(280, 9))
				(global0 reset: 0)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super dispose:)
		kernel.DisposeScript(285)
	#end:method

#end:class or instance

@SCI.instance
class pearlForMapScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global0 put: 30 global11 get: 0)
				(global1 handsOff:)
				proc280_10(self)
				(global0 normal: 0 view: 280 loop: 7 cel: 0)
				cycles = 2
			#end:case
			case 1:
				kernel.UnLoad(128, 900)
			#end:case
			case 2:
				(self
					setScript:
						kernel.ScriptID(286, 1)
						self
						if register:
							register = 29
							-32768
						else:
							register = 28
							-16384
						#endif
				)
			#end:case
			case 3:
				(global91 say: 4 66 register 1 script)
			#end:case
			case 4:
				(global91
					say:
						4
						66
						register
						2
						if (register == 28):
							script
						else:
							state.post('++')
							self
						#endif
				)
			#end:case
			case 5:
				(global91 say: 4 66 register 3 self)
			#end:case
			case 6:
				(self setScript: kernel.ScriptID(286, 3) self)
			#end:case
			case 7:
				(kernel.ScriptID(280, 2) setScript: kernel.ScriptID(280, 9))
				(global0 reset: 0)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super dispose:)
		kernel.DisposeScript(285)
	#end:method

#end:class or instance

@SCI.instance
class mapForPearlOrRingScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global0 put: 0 global11)
				(global1 handsOff:)
				proc280_10(self)
				(global0 normal: 0 view: 280 loop: 7 cel: 0)
				cycles = 2
			#end:case
			case 1:
				kernel.UnLoad(128, 900)
			#end:case
			case 2:
				if (((global9 at: 30) owner:) == global11):
					register = 30
					(global0 get: 30)
				else:
					register = 31
					(global0 get: 39)
				#endif
				(global91 say: 4 12 register 1 self 280)
			#end:case
			case 3:
				(global91 say: 4 12 register 2 self 280)
			#end:case
			case 4:
				(self setScript: kernel.ScriptID(286, 3) self 1)
			#end:case
			case 5:
				(global91 say: 4 12 register 3 self 280)
			#end:case
			case 6:
				(self setScript: kernel.ScriptID(286, 0) self 1)
			#end:case
			case 7:
				(kernel.ScriptID(280, 2) setScript: kernel.ScriptID(280, 9))
				(global0 reset: 0)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super dispose:)
		kernel.DisposeScript(285)
	#end:method

#end:class or instance

