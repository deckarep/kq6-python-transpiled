#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 277
import sci_sh
import kernel
import Main
import n913
import PolyPath
import Motion
import System

# Public Export Declarations
SCI.public_exports(
	talkClownNotFriendScr = 0,
	talkClownFriendScr = 1,
	showClownScr = 2,
	showItemScr = 3,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


@SCI.instance
class talkClownNotFriendScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if proc913_0(78):
					register = 16
				else:
					proc913_1(78)
					register = 8
				#endif
				global1._send('handsOff:')
				global91._send('say:', 10, 2, register, 1, self)
			#end:case
			case 1:
				kernel.ScriptID(274, 0)._send(
					'setScript:', 0,
					'view:', 2721,
					'loop:', 1,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				global91._send('say:', 10, 2, register, 2, self)
			#end:case
			case 3:
				kernel.ScriptID(274, 0)._send('setCycle:', Beg, self)
			#end:case
			case 4:
				global1._send('handsOn:')
				kernel.ScriptID(274, 0)._send('setScript:', kernel.ScriptID(274, 2))
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(277)
	#end:method

#end:class or instance

@SCI.instance
class talkClownFriendScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send(
					'setMotion:', PolyPath, kernel.ScriptID(274, 0)._send('approachX:'), kernel.ScriptID(274, 0)._send(
							'approachY:'
						), self
				)
			#end:case
			case 1:
				global0._send('setHeading:', 270, self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				register = (14 if (global153 == 3) else 15)
				global91._send('say:', 10, 2, register, 1, self)
			#end:case
			case 4:
				kernel.ScriptID(274, 0)._send(
					'setScript:', 0,
					'view:', 274,
					'loop:', 0,
					'cel:', 0,
					'setCycle:', CT, 3, 1, self
				)
			#end:case
			case 5:
				kernel.UnLoad(128, 2721)
				kernel.ScriptID(270, 3)._send('init:')
				cycles = 2
			#end:case
			case 6:
				kernel.ScriptID(274, 0)._send('setCycle:', CT, 5, 1, self)
			#end:case
			case 7:
				global91._send('say:', 10, 2, register, 2, self)
			#end:case
			case 8:
				global91._send('say:', 10, 2, register, 3, self)
			#end:case
			case 9:
				global91._send('say:', 10, 2, register, 4, self)
			#end:case
			case 10:
				cycles = 2
			#end:case
			case 11:
				global91._send(
					'say:', 19, 0, if (global153 == 3):
							28
						else:
							proc913_1(52)
							29
						#endif, 0, self
				)
			#end:case
			case 12:
				cycles = 2
			#end:case
			case 13:
				if (global153 == 3):
					global91._send('say:', 10, 2, register, 5, self)
				else:
					cycles = 2
				#endif
			#end:case
			case 14:
				kernel.ScriptID(274, 0)._send('view:', 274, 'loop:', 0, 'cel:', 5, 'setCycle:', End, self)
			#end:case
			case 15:
				client._send('setScript:', kernel.ScriptID(274, 1))
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(277)
	#end:method

#end:class or instance

@SCI.instance
class showClownScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				kernel.ScriptID(274, 0)._send('setScript:', 0)
				if register:
					local0 = register
				#endif
				register = (7 if proc913_0(10) else 8)
				self._send('setScript:', showItemScr, self)
			#end:case
			case 1:
				global91._send('say:', 10, 0, register, 1, self)
			#end:case
			case 2:
				kernel.ScriptID(274, 0)._send('view:', 2721, 'loop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 3:
				if local0:
					global91._send('say:', 10, local0, 0, 0, self)
				else:
					global91._send('say:', 10, 0, register, 2, self)
				#endif
			#end:case
			case 4:
				script._send('cue:')
				kernel.ScriptID(274, 0)._send('setCycle:', Beg)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				global1._send('handsOn:')
				kernel.ScriptID(274, 0)._send('setScript:', kernel.ScriptID(274, 2))
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		register = local0 = 0
		kernel.DisposeScript(277)
	#end:method

#end:class or instance

@SCI.instance
class showItemScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send(
					'setSpeed:', 6,
					'normal:', 0,
					'view:', 272,
					'loop:', 1,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 1:
				client._send('cue:')
			#end:case
			case 2:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 3:
				if register:
					client._send('cue:')
				else:
					cycles = 2
				#endif
			#end:case
			case 4:
				global0._send(
					'posn:', kernel.ScriptID(274, 0)._send('approachX:'), kernel.ScriptID(274, 0)._send(
							'approachY:'
						),
					'reset:', 7
				)
				cycles = 2
			#end:case
			case 5:
				kernel.UnLoad(128, 272)
				register = 0
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

