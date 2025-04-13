#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 224
import sci_sh
import kernel
import Main
import Scaler
import PolyPath
import StopWalk
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	clownScr = 0,
)

@SCI.instance
class clownScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				clown._send('init:', 'setMotion:', PolyPath, 124, 119, self)
			#end:case
			case 1:
				clown._send('setHeading:', 0, self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				global91._send('say:', 1, 0, 2, 1, self)
			#end:case
			case 4:
				global91._send('say:', 1, 0, 2, 2, self)
			#end:case
			case 5:
				self._send('setScript:', kernel.ScriptID(220, 1), self, 1)
			#end:case
			case 6:
				clown._send('setMotion:', MoveTo, 117, 109, self)
			#end:case
			case 7:
				clown._send('setMotion:', MoveTo, 104, 95, self)
			#end:case
			case 8:
				clown._send(
					'setPri:', 2,
					'setScale:', Scaler, 64, 94, 103, 95,
					'setMotion:', MoveTo, 75, 100, self
				)
			#end:case
			case 9:
				kernel.ScriptID(10, 0)._send('clrIt:', 2)
				clown._send('dispose:')
				script._send('cue:')
			#end:case
			case 10:
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
		kernel.DisposeScript(224)
	#end:method

#end:class or instance

@SCI.instance
class ModStopWalk(StopWalk):
	#property vars (may be empty)
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if client._send('isStopped:'):
			(cond
				case ((vStopped == -1) and (client._send('loop:') != 4)):
					temp0 = client._send('loop:')
					if (temp1 = client._send('mover:') and (not temp1._send('completed:'))):
						client._send('setMotion:', 0)
					#endif
					super._send('doit:')
					client._send('loop:', 4, 'setCel:', temp0)
				#end:case
				case ((vStopped != -1) and (client._send('view:') == vWalking)):
					client._send('view:', vStopped)
					if (temp1 = client._send('mover:') and (not temp1._send('completed:'))):
						client._send('setMotion:', 0)
					#endif
					super._send('doit:')
				#end:case
				case (vStopped != -1):
					super._send('doit:')
				#end:case
			)
		else:
			match vStopped
				case client._send('view:'):
					client._send('view:', vWalking)
				#end:case
				case -1:
					client._send('setLoop:', -1, 'setCel:', -1)
					if (client._send('loop:') == 4):
						client._send('loop:', client._send('cel:'), 'cel:', 0)
					#endif
				#end:case
			#end:match
			super._send('doit:')
		#endif
	#end:method

#end:class or instance

@SCI.instance
class clown(Actor):
	#property vars (may be empty)
	x = 166
	y = 172
	view = 717
	signal = 16384
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('setScale:', 'setCycle:', ModStopWalk, -1)
	#end:method

#end:class or instance

