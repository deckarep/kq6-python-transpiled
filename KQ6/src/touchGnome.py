#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 457
import sci_sh
import kernel
import Main
import rm450
import n913
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	touchGnome = 0,
)

@SCI.instance
class touchGnome(Gnome):
	#property vars (may be empty)
	x = 187
	noun = 18
	view = 457
	EOLx = 96
	FOLx = 140
	startPoint = 5
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('gnomeScript:', touchScript, 'setScript:', touchInit, 'stopUpd:')
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 1):
			global91._send('say:', noun, param1, 22, 1, 0, 450)
		else:
			kernel.ScriptID(450, 6)._send('setScript:', touchScript, 0, param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class touchInit(Script):
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
				global91._send('say:', 18, 0, 41, 1, self, 450)
			#end:case
			case 2:
				kernel.ScriptID(450, 6)._send('script:')._send('cue:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class touchScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				match register
					case 68:
						global91._send('say:', 18, 68, 41, 1, self, 450)
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
						global91._send('say:', 18, 0, 41, 2, self, 450)
					#end:else
				#end:match
			#end:case
			case 1:
				self._send('setScript:', kernel.ScriptID(450, 2), self, register)
			#end:case
			case 2:
				global104._send('number:', 455, 'setLoop:', 1)
				touchGnome._send('setLoop:', 1, 'cel:', 0, 'setCycle:', CT, 6, 1, self)
			#end:case
			case 3:
				global104._send('play:')
				touchGnome._send('setCycle:', End, self)
			#end:case
			case 4:
				global104._send('play:')
				cycles = 1
			#end:case
			case 5:
				if (register == 68):
					touchGnome._send('setLoop:', 4, 'cel:', 0, 'setCycle:', End, self)
				else:
					self._send('setScript:', failScript, 0, register)
				#endif
			#end:case
			case 6:
				global0._send('setCycle:', End, self)
				touchGnome._send('setLoop:', 3)
				touchGnome._send('cel:', (kernel.NumCels(touchGnome) - 1), 'setCycle:', Beg, self)
			#end:case
			case 7: 0#end:case
			case 8:
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
			case 9:
				global91._send('say:', 18, 68, 41, 2, self, 450)
			#end:case
			case 10:
				kernel.ScriptID(450, 6)._send('setScript:', kernel.ScriptID(450, 3), 0, touchGnome)
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
					global104._send('number:', 455, 'setLoop:', 1)
					touchGnome._send('setLoop:', 1, 'cel:', 0, 'setCycle:', CT, 6, 1, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 3:
				if (not register):
					global104._send('play:')
					touchGnome._send('setCycle:', End, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 4:
				if (not register):
					global104._send('play:')
					cycles = 1
				else:
					cycles = 1
				#endif
			#end:case
			case 5:
				touchGnome._send('setLoop:', 2, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 6:
				proc913_1(59)
				if (not register):
					global91._send('say:', 16, 0, 36, 1, self, 450)
				else:
					global91._send('say:', 18, 0, 41, 3, self, 450)
				#endif
			#end:case
			case 7:
				touchGnome._send('cel:', 4)
				touchGnome._send('setCycle:', Beg, self)
			#end:case
			case 8:
				touchGnome._send('setLoop:', 3)
				touchGnome._send('cel:', touchGnome._send('lastCel:'), 'setCycle:', Beg, self)
				proc913_2(59)
			#end:case
			case 9:
				self._send('setScript:', kernel.ScriptID(450, 4), self, register)
			#end:case
			case 10:
				global91._send('say:', 16, 0, 37, 1, self, 450)
			#end:case
			case 11:
				touchGnome._send('addToPic:', 'delete:', 'dispose:')
				cycles = 10
			#end:case
			case 12:
				kernel.ScriptID(450, 6)._send('setScript:', kernel.ScriptID(450, 5))
			#end:case
		#end:match
	#end:method

#end:class or instance

