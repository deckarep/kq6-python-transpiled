#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 241
import sci_sh
import kernel
import Main
import n913
import Polygon
import Feature
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	lampSeller = 0,
	lampSellerScr = 1,
)

@SCI.instance
class lampSeller(Actor):
	#property vars (may be empty)
	x = 19
	y = 128
	noun = 4
	approachX = 58
	approachY = 128
	_approachVerbs = -32766
	view = 2431
	priority = 7
	signal = 20496
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 43:
				self._send('setScript:', kernel.ScriptID(11, 2))
			#end:case
			case 2:
				(cond
					case kernel.ScriptID(10, 0)._send('isSet:', 16):
						self._send('setScript:', kernel.ScriptID(11, 3), 0, 24)
					#end:case
					case (not kernel.ScriptID(10, 0)._send('isSet:', 8)):
						kernel.ScriptID(10, 0)._send('setIt:', 8)
						self._send('setScript:', kernel.ScriptID(11, 3), 0, 22)
					#end:case
					case kernel.ScriptID(10, 0)._send('isSet:', 8):
						self._send('setScript:', kernel.ScriptID(11, 3), 0, 23)
					#end:case
				)
			#end:case
			else:
				if proc999_5(param1, 1, 5):
					global91._send('say:', noun, param1, 0, 0, 0, 240)
				else:
					self._send('setScript:', kernel.ScriptID(11, 3), 0, -1)
				#endif
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		polePoly._send('init:')
		self._send('setScript:', lampSellerScr)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('dispose:')
		polePoly._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class lampSellerScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				kernel.ScriptID(241, 0)._send('loop:', 0, 'cel:', 0, 'setCycle:', 0, 'setSpeed:', 6)
				if register:
					register = 0
				else:
					register = 1
					(= state
						match kernel.Random(0, 2)
							case 0: 4#end:case
							case 1: 5#end:case
							case 2: 6#end:case
						#end:match
					)
					state.post('--')
				#endif
				seconds = kernel.Random(5, 8)
			#end:case
			case 1:
				if (not global2._send('script:')):
					kernel.ScriptID(241, 0)._send('loop:', 2, 'cel:', 0, 'setCycle:', End)
					if (global90 & 0x0002):
						if (global0._send('y:') <= 130):
							cycles = 1
						else:
							global91._send('say:', 1, 0, 19, 1, self, 240)
						#endif
					else:
						cycles = 6
					#endif
				else:
					cycles = state = 2
				#endif
			#end:case
			case 2:
				proc913_1(59)
				if (not (global90 & 0x0002)):
					global91._send('say:', 1, 0, 19, 1, self, 240)
				else:
					ticks = 6
				#endif
			#end:case
			case 3:
				proc913_2(59)
				state = -1
				self._send('cue:')
			#end:case
			case 4:
				kernel.ScriptID(241, 0)._send(
					'loop:', 0,
					'cel:', 0,
					'cycleSpeed:', 10,
					'setCycle:', End, self
				)
				state = -1
			#end:case
			case 5:
				kernel.ScriptID(241, 0)._send('loop:', 3, 'cel:', 0)
				seconds = kernel.Random(2, 4)
				state = -1
			#end:case
			case 6:
				kernel.ScriptID(241, 0)._send('loop:', 4, 'cel:', 0)
				ticks = 45
			#end:case
			case 7:
				kernel.ScriptID(241, 0)._send('loop:', 5, 'cel:', 0, 'setCycle:', End, self)
				state = -1
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		proc913_2(59)
		register = 0
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class polePoly(Feature):
	#property vars (may be empty)
	x = 19
	y = 129
	noun = 15
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(= onMeCheck
			Polygon._send('new:')._send(
				'type:', 3,
				'init:', 21, 134, 36, 123, 39, 117, 44, 124, 30, 137,
				'yourself:'
			)
		)
		super._send('init:', &rest)
	#end:method

#end:class or instance

