#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 11
import sci_sh
import kernel
import Main
import n913
import Inset
import Scaler
import PolyPath
import Feature
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	lampTradeScr = 2,
	talkToSellerScr = 3,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


@SCI.instance
class lampTradeScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				kernel.ScriptID(10, 0)._send('setIt:', 16)
				if (not kernel.ScriptID(10, 0)._send('isSet:', 4)):
					kernel.ScriptID(10, 0)._send('setIt:', 4)
					register = 22
				else:
					register = 23
				#endif
				global91._send('say:', 4, 43, register, 1, self, 240)
			#end:case
			case 1:
				kernel.ScriptID(241, 0)._send('setPri:', -1, 'loop:', 6, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				global0._send('hide:')
				kernel.ScriptID(241, 0)._send(
					'view:', 245,
					'loop:', 2,
					'cel:', 0,
					'posn:', 41, 128,
					'scaleX:', 102,
					'scaleY:', 102,
					'setScale:',
					'setSpeed:', 6,
					'setCycle:', End, self
				)
			#end:case
			case 4:
				global91._send('say:', 4, 43, register, 2, self, 240)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				kernel.ScriptID(241, 0)._send('hide:')
				global0._send(
					'show:',
					'normal:', 0,
					'view:', 247,
					'loop:', 0,
					'cel:', 0,
					'setSpeed:', 6,
					'setCycle:', End, self
				)
			#end:case
			case 7:
				global0._send('loop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 8:
				ticks = 60
			#end:case
			case 9:
				lampSellerInset._send('init:', self, global2)
			#end:case
			case 10:
				global1._send('handsOff:')
				cycles = 2
			#end:case
			case 11:
				if (not local0):
					global91._send('say:', 39, 0, 0, 1, self, 240)
				else:
					global91._send('say:', 34, 5, 0, 1, self, 240)
				#endif
			#end:case
			case 12:
				if local0:
					cycles = 1
				else:
					global0._send('reset:', 1, 'loop:', 9, 'cel:', 1)
					kernel.ScriptID(241, 0)._send(
						'show:',
						'setScale:', 0,
						'view:', 2431,
						'loop:', 6,
						'cel:', 6,
						'setPri:', 7,
						'posn:', 19, 128,
						'setCycle:', Beg, self
					)
					(state += 2)
				#endif
			#end:case
			case 13:
				global0._send('hide:')
				kernel.ScriptID(241, 0)._send(
					'show:',
					'view:', 245,
					'loop:', 1,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 14:
				cycles = 2
			#end:case
			case 15:
				if (not local0):
					global91._send('say:', 39, 0, 0, 2, self, 240)
				else:
					state.post('++')
					self._send('cue:')
				#endif
			#end:case
			case 16:
				kernel.ScriptID(241, 0)._send(
					'setScale:', 0,
					'posn:', 19, 128,
					'view:', 2431,
					'loop:', 6,
					'cel:', kernel.ScriptID(241, 0)._send('lastCel:'),
					'setCycle:', Beg, self
				)
				global0._send('reset:', 1)
				global1._send('handsOn:')
				client._send('setScript:', kernel.ScriptID(241, 1))
			#end:case
			case 17:
				kernel.ScriptID(241, 0)._send(
					'posn:', 19, 128,
					'view:', 243,
					'loop:', 0,
					'setCycle:', Walk,
					'setScale:', Scaler, 90, 72, 188, 95
				)
				global0._send('reset:', 1)
				client._send('setScript:', sealTheDealScr, self)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lamp(Prop):
	#property vars (may be empty)
	view = 245
	
#end:class or instance

@SCI.instance
class sealTheDealScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global91._send('say:', 34, 5, 0, 2, self, 240)
			#end:case
			case 1:
				global91._send('say:', 34, 5, 0, 3, self, 240)
			#end:case
			case 2:
				global2._send('notify:')
				cycles = 2
			#end:case
			case 3:
				kernel.ScriptID(241, 0)._send(
					'moveSpeed:', 3,
					'cycleSpeed:', 3,
					'setMotion:', PolyPath, 274, 187, self
				)
				proc913_1(12)
			#end:case
			case 4:
				kernel.ScriptID(241, 0)._send('loop:', 0)
				cycles = 2
			#end:case
			case 5:
				kernel.ScriptID(241, 0)._send(
					'moveSpeed:', 6,
					'cycleSpeed:', 6,
					'view:', 254,
					'loop:', 0,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 6:
				kernel.ScriptID(241, 0)._send('loop:', 1, 'cel:', 0, 'setCycle:', Fwd, self)
				seconds = 4
			#end:case
			case 7:
				global91._send('say:', 34, 5, 0, 4, self, 240)
			#end:case
			case 8:
				cycles = 3
			#end:case
			case 9:
				kernel.ScriptID(241, 0)._send('loop:', 0, 'cel:', kernel.ScriptID(241, 0)._send('lastCel:'))
				cycles = 2
			#end:case
			case 10:
				kernel.ScriptID(241, 0)._send('setCycle:', Beg, self)
			#end:case
			case 11:
				cycles = 2
			#end:case
			case 12:
				kernel.ScriptID(241, 0)._send(
					'moveSpeed:', 3,
					'cycleSpeed:', 3,
					'view:', 243,
					'setCycle:', Walk,
					'setMotion:', MoveTo, 274, 230, self
				)
			#end:case
			case 13:
				global1._send('handsOn:')
				client._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class talkToSellerScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				kernel.ScriptID(241, 0)._send('loop:', 0, 'cel:', 0, 'setCycle:', 0)
				if (register == -1):
					global0._send(
						'view:', 272,
						'loop:', 1,
						'cel:', 0,
						'setSpeed:', 6,
						'setCycle:', End, self
					)
				else:
					global91._send('say:', 4, 2, register, 0, self, 240)
					(state += 4)
				#endif
			#end:case
			case 1:
				global91._send('say:', 4, 0, 0, 0, self, 240)
			#end:case
			case 2:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				global0._send('reset:', 1)
				cycles = 2
			#end:case
			case 5:
				global1._send('handsOn:')
				client._send('setScript:', kernel.ScriptID(241, 1))
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lampSellerInset(Inset):
	#property vars (may be empty)
	picture = 245
	hideTheCast = 1
	disposeNotOnMe = 1
	noun = 9
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return proc999_4(83, 48, 232, 136, param1._send('x:'), param1._send('y:'))
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if script:
			script._send('doit:')
		#endif
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('drawInset:')
		super._send('init:', &rest)
		lamps._send('init:')
		global1._send('handsOn:')
		global69._send('disable:', 0, 3, 4, 5, 6, 'curIcon:', global69._send('at:', 1))
		global1._send('setCursor:', global69._send('curIcon:')._send('cursor:'))
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('doVerb:', param1, &rest)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global69._send('enable:', 6)
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class lamps(Feature):
	#property vars (may be empty)
	y = 1
	onMeCheck = 118
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(= noun
				match kernel.OnControl(4, param1._send('x:'), param1._send('y:'))
					case 2:
						lampTradeScr._send('register:', 0)
						global9._send('at:', 25)._send(
							'message:', 57,
							'noun:', 25,
							'cel:', 11,
							'setCursor:', 990, 1, 11
						)
						34
					#end:case
					case 4:
						lampTradeScr._send('register:', 3)
						global9._send('at:', 25)._send(
							'message:', 56,
							'noun:', 24,
							'loop:', 2,
							'cel:', 9,
							'setCursor:', 990, 2, 9
						)
						7
					#end:case
					case 8:
						lampTradeScr._send('register:', 4)
						global9._send('at:', 25)._send(
							'message:', 58,
							'noun:', 26,
							'cel:', 13,
							'setCursor:', 990, 1, 13
						)
						35
					#end:case
					case 16:
						lampTradeScr._send('register:', 3)
						global9._send('at:', 25)._send(
							'message:', 59,
							'noun:', 27,
							'cel:', 15,
							'setCursor:', 990, 1, 15
						)
						36
					#end:case
					case 32:
						lampTradeScr._send('register:', 4)
						global9._send('at:', 25)._send(
							'message:', 60,
							'noun:', 28,
							'cel:', 14,
							'setCursor:', 990, 1, 14
						)
						37
					#end:case
					case 64:
						global9._send('at:', 25)._send(
							'message:', 96,
							'noun:', 65,
							'cel:', 12,
							'setCursor:', 990, 1, 12
						)
						6
					#end:case
					else: 0#end:else
				#end:match
			)
		)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global1._send('givePoints:', 1)
				global0._send('put:', 19)
				global1._send('handsOff:')
				(cond
					case (noun == 7):
						global0._send('get:', 25)
					#end:case
					case (not global0._send('has:', 25)):
						global0._send('get:', 25)
					#end:case
				)
				local0 = 1
				lampSellerInset._send('dispose:')
			#end:case
			else:
				if (param1 != 1):
					noun = 34
				#endif
				global91._send('say:', noun, param1, 0, 0, 0, 240)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('sightAngle:', 26505)
	#end:method

#end:class or instance

