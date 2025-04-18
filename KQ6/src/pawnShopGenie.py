#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 281
import sci_sh
import kernel
import Main
import n913
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	pawnShopGenie = 0,
	proc281_1 = 1,
)

@SCI.procedure
def proc281_1(param1 = None, *rest):
	if global5._send('contains:', eye):
		eye._send('dispose:')
	#endif
	pawnShopGenie._send('cycleSpeed:', 6)
	genieBrowseScr._send('caller:', param1, 'dispose:')
#end:procedure

@SCI.instance
class pawnShopGenie(Actor):
	#property vars (may be empty)
	x = 85
	y = 131
	noun = 5
	approachX = 117
	approachY = 133
	view = 2831
	signal = 16384
	cycleSpeed = 75
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 13:
				global2._send('setScript:', kernel.ScriptID(282, 3))
			#end:case
			case 67:
				global0._send('put:', 31, -1)
				global2._send('setScript:', kernel.ScriptID(282, 6))
			#end:case
			case 2:
				if proc999_5(global153, 4, 5):
					global91._send('say:', noun, param1, (68 if proc913_1(122) else 1))
				else:
					super._send('doVerb:', param1, &rest)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init(param1 = None, *rest):
		super._send('init:', &rest)
		self._send('approachVerbs:', 2, 0)
		if param1:
			self._send('setScript:', genieBrowseScr)
		else:
			global2._send('setScript:', kernel.ScriptID(282, 4))
		#endif
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		self._send('delete:')
		kernel.DisposeScript(281)
	#end:method

#end:class or instance

@SCI.instance
class eye(Prop):
	#property vars (may be empty)
	x = 92
	y = 92
	view = 902
	priority = 10
	signal = 16
	
#end:class or instance

@SCI.instance
class genieBrowseScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				pawnShopGenie._send('view:', 2831, 'loop:', 0, 'cel:', 0)
				self._send('cue:')
			#end:case
			case 1:
				pawnShopGenie._send('cycleSpeed:', kernel.Random(30, 75), 'setCycle:', CT, 3, 1, self)
			#end:case
			case 2:
				ticks = kernel.Random(60, 120)
			#end:case
			case 3:
				if ((global0._send('x:') > 67) and proc999_5(kernel.Random(0, 2), 0, 1)):
					eye._send('init:', 'cel:', 0, 'cycleSpeed:', 12, 'setCycle:', End, self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 4:
				ticks = 6
			#end:case
			case 5:
				eye._send('dispose:')
				ticks = kernel.Random(60, 120)
			#end:case
			case 6:
				pawnShopGenie._send('setCycle:', End, self)
			#end:case
			case 7:
				state = -1
				ticks = 25
			#end:case
		#end:match
	#end:method

#end:class or instance

