#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 458
import sci_sh
import kernel
import Main
import rm450
import n913
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	sightGnome = 0,
)

@SCI.instance
class sightGnome(Gnome):
	#property vars (may be empty)
	x = 179
	noun = 12
	view = 458
	EOLx = 96
	FOLx = 145
	startPoint = 5
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('gnomeScript:', sightScript, 'setScript:', sightInit, 'stopUpd:')
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 1):
			global91._send('say:', noun, param1, 22, 1, 0, 450)
		else:
			kernel.ScriptID(450, 6)._send('setScript:', sightScript, 0, param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class sightInit(Script):
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
				global91._send('say:', 12, 0, 14, 1, self, 450)
			#end:case
			case 2:
				kernel.DisposeScript(1037)
				kernel.UnLoad(128, 8930)
				kernel.ScriptID(450, 6)._send('script:')._send('cue:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class sightScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				match register
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
						global91._send('say:', 12, 0, 14, 2, self, 450)
					#end:else
				#end:match
			#end:case
			case 1:
				self._send('setScript:', kernel.ScriptID(450, 2), self, register)
			#end:case
			case 2:
				sightGnome._send('setLoop:', 1, 'cel:', 0, 'setCycle:', CT, 2, 1, self)
			#end:case
			case 3:
				global104._send('number:', 456, 'setLoop:', 1, 'play:')
				sightGnome._send('setCycle:', CT, 5, 1, self)
			#end:case
			case 4:
				global104._send('play:')
				sightGnome._send('setCycle:', End, self)
			#end:case
			case 5:
				global104._send('play:')
				if (register == 83):
					sightGnome._send('setLoop:', 4, 'cel:', 0, 'setCycle:', End, self)
				else:
					self._send('setScript:', failScript, 0, register)
				#endif
			#end:case
			case 6:
				sightGnome._send('setLoop:', 0, 'cel:', 0)
				cycles = 2
			#end:case
			case 7:
				global91._send('say:', 2, 83, 14, 2, self, 450)
			#end:case
			case 8:
				kernel.ScriptID(450, 6)._send('setScript:', kernel.ScriptID(450, 3), 0, sightGnome)
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
					case (register == 31):
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
				sightGnome._send('setLoop:', 2, 'cel:', 0, 'setCycle:', CT, 2, 1, self)
			#end:case
			case 3:
				global104._send('number:', 456, 'setLoop:', 1, 'play:')
				sightGnome._send('setCycle:', CT, 4, 1, self)
			#end:case
			case 4:
				global104._send('play:')
				sightGnome._send('setCycle:', CT, 9, 1, self)
			#end:case
			case 5:
				global104._send('number:', 459, 'setLoop:', 1, 'play:')
				sightGnome._send('setCycle:', End, self)
			#end:case
			case 6:
				proc913_1(59)
				if (not register):
					global91._send('say:', 16, 0, 32, 1, self, 450)
				else:
					global91._send('say:', 12, 0, 14, 3, self, 450)
				#endif
			#end:case
			case 7:
				proc913_2(59)
				sightGnome._send('setLoop:', 0, 'cel:', 0)
				self._send('setScript:', kernel.ScriptID(450, 4), self, register)
			#end:case
			case 8:
				global91._send('say:', 16, 0, 28, 1, self, 450)
			#end:case
			case 9:
				sightGnome._send('addToPic:', 'delete:', 'dispose:')
				cycles = 10
			#end:case
			case 10:
				kernel.ScriptID(450, 6)._send('setScript:', kernel.ScriptID(450, 5))
			#end:case
		#end:match
	#end:method

#end:class or instance

