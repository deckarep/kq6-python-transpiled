#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 272
import sci_sh
import kernel
import Main
import Conversation
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	poemShelfScr = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = -1
local1 = None


@SCI.instance
class roomConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class turnPageScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('setCycle:', CT, 1, -1, self)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				global0._send('setCycle:', End, self)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class poemShelfScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				if (global0._send('loop:') != 3):
					global0._send('loop:', 3)
				#endif
				cycles = 2
			#end:case
			case 1:
				global0._send(
					'setSpeed:', 6,
					'view:', 279,
					'loop:', 2,
					'cel:', 0,
					'normal:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				global0._send('loop:', 3, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 3:
				if (global9._send('at:', 47)._send('owner:') != 270):
					register = 1
					roomConv._send(
						'add:', -1, 13, 5, 18, 1,
						'add:', -1, 13, 5, 18, 2,
						'add:', -1, 13, 5, 18, 3,
						'add:', turnPageScr,
						'add:', -1, 13, 5, 18, 4,
						'add:', -1, 13, 5, 18, 5,
						'init:', self
					)
				else:
					roomConv._send(
						'add:', -1, 13, 5, 17, 1,
						'add:', -1, 13, 5, 17, 2,
						'add:', -1, 13, 5, 17, 3,
						'add:', turnPageScr,
						'add:', -1, 13, 5, 17, 4,
						'add:', -1, 13, 5, 17, 5,
						'add:', turnPageScr,
						'add:', -1, 13, 5, 17, 6,
						'add:', turnPageScr,
						'add:', -1, 13, 5, 17, 7,
						'add:', turnPageScr,
						'add:', -1, 13, 5, 17, 8,
						'add:', -1, 13, 5, 17, 9,
						'add:', -1, 13, 5, 17, 10,
						'init:', self
					)
				#endif
			#end:case
			case 4:
				if (not register):
					global9._send('at:', 47)._send('owner:', -1)
					poem._send(
						'init:',
						'posn:', 303, 92,
						'view:', 279,
						'setLoop:', 6,
						'cel:', 0,
						'setCycle:', Fwd,
						'setMotion:', MoveTo, 281, 120, poem
					)
				#endif
				cycles = 2
			#end:case
			case 5:
				global0._send('loop:', 2, 'cel:', global0._send('lastCel:'))
				cycles = 2
			#end:case
			case 6:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 7:
				global0._send('reset:', 3)
				if (not register):
					global1._send('givePoints:', 1)
				#endif
				cycles = 1
			#end:case
			case 8:
				if ((not local1) and (not register)):
					state.post('--')
					ticks = 12
				else:
					cycles = 2
				#endif
			#end:case
			case 9:
				kernel.UnLoad(128, 279)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		register = 0
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class takePoemScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global1._send('givePoints:', 1)
				global0._send(
					'setSpeed:', 6,
					'view:', 2701,
					'loop:', 1,
					'cel:', 0,
					'normal:', 0,
					'setCycle:', CT, 3, 1, self
				)
			#end:case
			case 1:
				poem._send('dispose:')
				global0._send('get:', 47)
				cycles = 2
			#end:case
			case 2:
				global0._send('setCycle:', End, self)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				global0._send('reset:', 7)
				cycles = 2
			#end:case
			case 5:
				kernel.UnLoad(128, 2701)
				global91._send('say:', 6, 5, 0, 1, self)
			#end:case
			case 6:
				global91._send('say:', 6, 5, 0, 2, self)
			#end:case
			case 7:
				global91._send('say:', 6, 5, 0, 3, self)
			#end:case
			case 8:
				global0._send('setHeading:', 180, self)
			#end:case
			case 9:
				cycles = 2
			#end:case
			case 10:
				global91._send('say:', 6, 5, 0, 4, self)
			#end:case
			case 11:
				global1._send('handsOn:')
				self._send('dispose:')
				kernel.DisposeScript(272)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class poem(Actor):
	#property vars (may be empty)
	x = 281
	y = 120
	noun = 6
	approachX = 292
	approachY = 128
	view = 270
	loop = 2
	cel = 1
	priority = 1
	signal = 18449
	
	@classmethod
	def cue():
		if (not local0.post('++')):
			self._send('setCycle:', End, self)
		else:
			self._send('view:', 270, 'setLoop:', 2, 'cel:', 1)
			local1 = 1
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				global2._send('setScript:', takePoemScr)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('approachVerbs:', 5)
	#end:method

#end:class or instance

