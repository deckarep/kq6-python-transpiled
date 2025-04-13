#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 286
import sci_sh
import kernel
import Main
import rm280
import Scaler
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	ownerGiveScr = 0,
	alexGiveScr = 1,
	alexShowScr = 2,
	alexTakeMapScr = 3,
	genericShowScr = 4,
	fullMsgShowScr = 5,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


@SCI.instance
class ownerGiveScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if register:
					kernel.ScriptID(280, 2)._send('view:', 286, 'loop:', 1, 'cel:', 0)
					cycles = 2
				else:
					(state += 4)
					self._send('cue:')
				#endif
			#end:case
			case 1:
				kernel.ScriptID(280, 2)._send('setCycle:', CT, 2, 1, self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				kernel.ScriptID(280, 2)._send('setCycle:', Beg, self)
			#end:case
			case 4:
				cycles = 2
			#end:case
			case 5:
				kernel.ScriptID(280, 2)._send('view:', 284, 'loop:', 2, 'cel:', 0)
				cycles = 2
			#end:case
			case 6:
				kernel.ScriptID(280, 2)._send('setCycle:', CT, 1, 1, self)
			#end:case
			case 7:
				cycles = 2
			#end:case
			case 8:
				global0._send(
					'normal:', 0,
					'setSpeed:', 6,
					'posn:', 188, 135,
					'view:', 2811,
					'loop:', 1,
					'setScale:', 0,
					'cel:', 0
				)
				cycles = 2
			#end:case
			case 9:
				global0._send('setCycle:', CT, 2, 1, self)
			#end:case
			case 10:
				cycles = 2
			#end:case
			case 11:
				kernel.ScriptID(280, 2)._send('setCycle:', Beg, self)
				global0._send('setCycle:', End, self)
			#end:case
			case 12: 0#end:case
			case 13:
				kernel.ScriptID(280, 2)._send('view:', 2841, 'loop:', 0, 'cel:', 0)
				global0._send(
					'posn:', kernel.ScriptID(280, 2)._send('approachX:'), kernel.ScriptID(280, 2)._send(
							'approachY:'
						),
					'view:', 280,
					'loop:', 7,
					'cel:', 0,
					'setScale:', Scaler, 105, 90, 139, 121
				)
				cycles = 2
			#end:case
			case 14:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('dispose:')
		kernel.DisposeScript(286)
	#end:method

#end:class or instance

@SCI.instance
class arm(Prop):
	#property vars (may be empty)
	x = 199
	y = 102
	view = 281
	priority = 15
	signal = 16
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class alexShowScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global0._send(
					'normal:', 0,
					'setSpeed:', 6,
					'posn:', 188, 135,
					'view:', 2811,
					'setScale:', 0,
					'loop:', 1,
					'cel:', 0
				)
				if register:
					arm._send(
						'loop:', match register
								case 3: 5#end:case
								case 2: 6#end:case
								case 0: 7#end:case
								case 1: 8#end:case
							#end:match,
						'cel:', 0,
						'init:'
					)
				#endif
				cycles = 2
			#end:case
			case 1:
				global0._send('setCycle:', CT, 2, 1, self)
				if register:
					arm._send('setCycle:', CT, 2, 1)
				#endif
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				if register:
					local0 = 1
					register = 0
				#endif
				client._send('cue:')
			#end:case
			case 4:
				if local0:
					arm._send('dispose:')
				#endif
				if register:
					arm._send(
						'loop:', match register
								case 3: 5#end:case
								case 2: 6#end:case
								case 0: 7#end:case
								case 1: 8#end:case
							#end:match,
						'cel:', 2,
						'init:'
					)
				#endif
				cycles = 2
			#end:case
			case 5:
				global0._send('setCycle:', End, self)
				if register:
					arm._send('setCycle:', End, arm)
				#endif
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				global0._send(
					'posn:', kernel.ScriptID(280, 2)._send('approachX:'), kernel.ScriptID(280, 2)._send(
							'approachY:'
						),
					'view:', 280,
					'loop:', 7,
					'cel:', 0,
					'setScale:', Scaler, 105, 90, 139, 121
				)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not proc999_5(client, fullMsgShowScr, genericShowScr)):
			temp0 = 1
		else:
			temp0 = 0
		#endif
		super._send('dispose:')
		if temp0:
			kernel.DisposeScript(286)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class alexGiveScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global0._send(
					'normal:', 0,
					'setSpeed:', 6,
					'posn:', 188, 135,
					'view:', 2811,
					'loop:', 1,
					'cel:', 0,
					'setScale:', 0
				)
				cycles = 2
			#end:case
			case 1:
				global0._send('setCycle:', CT, 2, 1, self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				client._send('cue:')
			#end:case
			case 4:
				kernel.ScriptID(280, 2)._send('view:', 284, 'loop:', 2, 'cel:', 0)
				cycles = 2
			#end:case
			case 5:
				kernel.ScriptID(280, 2)._send('setCycle:', CT, 1, 1, self)
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				global0._send('setCycle:', End, self)
				if (register & 0x4000):
					kernel.ScriptID(280, 2)._send('setCycle:', End, self)
				else:
					(state += 3)
					self._send('cue:')
				#endif
			#end:case
			case 8: 0#end:case
			case 9:
				cycles = 2
			#end:case
			case 10:
				client._send('cue:')
			#end:case
			case 11:
				kernel.ScriptID(280, 2)._send('setCycle:', Beg, self)
			#end:case
			case 12:
				if (not (register & 0x4000)):
					0
				else:
					self._send('cue:')
				#endif
			#end:case
			case 13:
				cycles = 2
			#end:case
			case 14:
				if (register & 0x8000):
					kernel.ScriptID(280, 2)._send(
						'view:', 286,
						'loop:', 1,
						'cel:', 1,
						'setCycle:', CT, 2, 1, self
					)
				else:
					(state += 2)
					self._send('cue:')
				#endif
			#end:case
			case 15:
				cycles = 2
			#end:case
			case 16:
				kernel.ScriptID(280, 2)._send('setCycle:', Beg, self)
			#end:case
			case 17:
				cycles = 2
			#end:case
			case 18:
				global0._send(
					'posn:', kernel.ScriptID(280, 2)._send('approachX:'), kernel.ScriptID(280, 2)._send(
							'approachY:'
						),
					'view:', 280,
					'loop:', 7,
					'cel:', 0,
					'setScale:', Scaler, 105, 90, 139, 121
				)
				kernel.ScriptID(280, 2)._send('view:', 280, 'loop:', 8, 'cel:', 0)
				cycles = 2
			#end:case
			case 19:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('dispose:')
		kernel.DisposeScript(286)
	#end:method

#end:class or instance

@SCI.instance
class alexTakeMapScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global0._send(
					'normal:', 0,
					'setSpeed:', 6,
					'view:', 2861,
					'posn:', 199, 143,
					'loop:', 0,
					'setScale:', 0
				)
				if (not register):
					global0._send('cel:', 0)
				else:
					global0._send('cel:', 4)
				#endif
				cycles = 2
			#end:case
			case 1:
				global0._send('setCycle:', CT, 2, (-1 if register else 1), self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				if register:
					kernel.ScriptID(280, 1)._send('init:')
				else:
					kernel.ScriptID(280, 1)._send('dispose:')
				#endif
				cycles = 2
			#end:case
			case 4:
				if register:
					global0._send('setCycle:', Beg, self, 'put:', 0)
				else:
					global0._send('setCycle:', End, self, 'get:', 0)
				#endif
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				global0._send(
					'posn:', kernel.ScriptID(280, 2)._send('approachX:'), kernel.ScriptID(280, 2)._send(
							'approachY:'
						),
					'view:', 280,
					'loop:', 7,
					'cel:', 0,
					'setScale:', Scaler, 105, 90, 139, 121
				)
				ticks = 12
			#end:case
			case 7:
				cycles = 2
			#end:case
			case 8:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('dispose:')
		kernel.DisposeScript(286)
	#end:method

#end:class or instance

@SCI.instance
class fullMsgShowScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				proc280_10(self)
				global0._send('normal:', 0, 'view:', 280, 'loop:', 7, 'cel:', 0)
				cycles = 2
			#end:case
			case 1:
				kernel.UnLoad(128, 900)
			#end:case
			case 2:
				self._send('setScript:', alexShowScr, self)
			#end:case
			case 3:
				global91._send('say:', 4, register, 0, 1, alexShowScr)
			#end:case
			case 4:
				global91._send('say:', 4, register, 0, 2, self)
			#end:case
			case 5:
				global0._send('reset:', 0)
				kernel.ScriptID(280, 2)._send('setScript:', kernel.ScriptID(280, 9))
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('dispose:')
		kernel.DisposeScript(286)
	#end:method

#end:class or instance

@SCI.instance
class genericShowScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				proc280_10(self)
				global0._send('normal:', 0, 'view:', 280, 'loop:', 7, 'cel:', 0)
				cycles = 2
			#end:case
			case 1:
				kernel.UnLoad(128, 900)
			#end:case
			case 2:
				self._send('setScript:', alexShowScr, self)
			#end:case
			case 3:
				if (not register):
					register = 0
				#endif
				global91._send('say:', 4, 0, 0, 1, alexShowScr)
			#end:case
			case 4:
				global91._send('say:', 4, register, 0, (2 if (register == 0) else 1), self)
			#end:case
			case 5:
				kernel.ScriptID(280, 2)._send('setScript:', kernel.ScriptID(280, 9))
				global0._send('reset:', 0)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('dispose:')
		kernel.DisposeScript(286)
	#end:method

#end:class or instance

