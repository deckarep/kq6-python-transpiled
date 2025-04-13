#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 4561
import sci_sh
import kernel
import Main
import rm450
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	tasteGnome = 0,
)

@SCI.instance
class tasteGnome(Gnome):
	#property vars (may be empty)
	x = 190
	noun = 17
	view = 4561
	EOLx = 95
	FOLx = 149
	startPoint = 3
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('gnomeScript:', tasteScript, 'setScript:', tasteInit, 'stopUpd:')
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 1):
			global91._send('say:', noun, param1, 22, 1, 0, 450)
		else:
			kernel.ScriptID(450, 6)._send('setScript:', tasteScript, 0, param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class tasteInit(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				seconds = 1
			#end:case
			case 1:
				global91._send('say:', 17, 0, 39, 1, self, 450)
			#end:case
			case 2:
				kernel.ScriptID(450, 6)._send('script:')._send('cue:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class tasteScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				match register
					case 63:
						global91._send('say:', 17, 63, 39, 1, self, 450)
					#end:case
					case 83:
						self._send('cue:')
					#end:case
					case 31:
						self._send('cue:')
					#end:case
					case 37:
						global91._send('say:', 2, 37, 42, 1, self, 450)
					#end:case
					else:
						global91._send('say:', 17, 0, 39, 2, self, 450)
					#end:else
				#end:match
			#end:case
			case 1:
				self._send('setScript:', kernel.ScriptID(450, 2), self, register)
			#end:case
			case 2:
				global104._send('number:', 454, 'setLoop:', 1, 'play:')
				tasteGnome._send('setLoop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 3:
				if (register == 63):
					tasteGnome._send('setLoop:', 4, 'cel:', 0, 'setCycle:', End, self)
				else:
					self._send('setScript:', failScript, 0, register)
				#endif
			#end:case
			case 4:
				tasteGnome._send('setLoop:', 0, 'cel:', 0)
				global0._send('setCycle:', End, self)
			#end:case
			case 5:
				if kernel.ScriptID(40, 0)._send('alexX:'):
					global0._send(
						'posn:', kernel.ScriptID(40, 0)._send('alexX:'), kernel.ScriptID(40, 0)._send('alexY:')
					)
				#endif
				if (global0._send('view:') != 900):
					global0._send('reset:', 1)
				#endif
				cycles = 6
			#end:case
			case 6:
				global91._send('say:', 17, 63, 39, 2, self, 450)
			#end:case
			case 7:
				global0._send('put:', 23, 450)
				global69._send('curIcon:', global69._send('at:', 0))
				kernel.ScriptID(450, 6)._send('setScript:', kernel.ScriptID(450, 3), 0, tasteGnome)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class failScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(cond
					case (kernel.ScriptID(40, 0)._send('alexInvisible:') or (register == 31)):
						self._send('state:', (state + 1), 'cue:')
					#end:case
					case register:
						global0._send('setCycle:', End, self)
					#end:case
					else:
						cycles = 1
					#end:else
				)
			#end:case
			case 1:
				if kernel.ScriptID(40, 0)._send('alexX:'):
					global0._send(
						'posn:', kernel.ScriptID(40, 0)._send('alexX:'), kernel.ScriptID(40, 0)._send('alexY:')
					)
				#endif
				if (global0._send('view:') != 900):
					global0._send('reset:', 1)
				#endif
				cycles = 2
			#end:case
			case 2:
				if (not register):
					tasteGnome._send('setCycle:', Beg, self)
					global104._send('number:', 454, 'setLoop:', 1, 'play:')
				else:
					cycles = 1
				#endif
			#end:case
			case 3:
				tasteGnome._send('setLoop:', 2, 'setCycle:', End, self)
			#end:case
			case 4:
				tasteGnome._send('setCycle:', Beg, self)
			#end:case
			case 5:
				if (not register):
					global91._send('say:', 16, 0, 35, 1, self, 450)
				else:
					global91._send('say:', 17, 0, 39, 3, self, 450)
				#endif
			#end:case
			case 6:
				self._send('setScript:', kernel.ScriptID(450, 4), self, register)
			#end:case
			case 7:
				global91._send('say:', 16, 0, 31, 1, self, 450)
			#end:case
			case 8:
				tasteGnome._send('addToPic:', 'delete:', 'dispose:')
				cycles = 10
			#end:case
			case 9:
				kernel.ScriptID(450, 6)._send('setScript:', kernel.ScriptID(450, 5))
			#end:case
		#end:match
	#end:method

#end:class or instance

