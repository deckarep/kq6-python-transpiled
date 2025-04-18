#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 271
import sci_sh
import kernel
import Main
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	bookShopGenie = 0,
	genieKickingItScr = 1,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.instance
class genieEye(Prop):
	#property vars (may be empty)
	x = 183
	y = 82
	view = 902
	loop = 1
	
#end:class or instance

@SCI.instance
class genieKickingItScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				client._send('loop:', 0, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 1:
				seconds = kernel.Random(5, 10)
			#end:case
			case 2:
				client._send('loop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 3:
				ticks = 60
			#end:case
			case 4:
				if ((not (kernel.Random(0, 2) - 1)) or (not local1)):
					local1 = 1
					genieEye._send('init:', 'cel:', 0, 'setCycle:', End, self)
				else:
					(state += 2)
					cycles = 2
				#endif
			#end:case
			case 5:
				ticks = 6
			#end:case
			case 6:
				genieEye._send('dispose:')
				cycles = 2
			#end:case
			case 7:
				ticks = kernel.Random(60, 120)
			#end:case
			case 8:
				client._send('setCycle:', Beg, self)
			#end:case
			case 9:
				state = -1
				seconds = kernel.Random(10, 15)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		if global5._send('contains:', genieEye):
			genieEye._send('dispose:')
		#endif
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class bookShopGenie(Actor):
	#property vars (may be empty)
	x = 179
	y = 117
	noun = 9
	approachX = 212
	approachY = 123
	view = 275
	priority = 1
	signal = 16400
	scaleSignal = 1
	scaleX = 113
	scaleY = 113
	
	@classmethod
	def doVerb(param1 = None, *rest):
		if (param1 == 63):
			global2._send('setScript:', kernel.ScriptID(278))
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('setScript:', genieKickingItScr, 'approachVerbs:', 2, 0)
	#end:method

#end:class or instance

