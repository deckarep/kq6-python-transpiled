#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 961
import sci_sh
import kernel
import Motion

# Public Export Declarations
SCI.public_exports(
	StopWalk = 0,
)

class StopWalk(Fwd):
	#property vars (may be empty)
	vWalking = 0
	vStopped = 0
	
	@classmethod
	def init(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			vWalking = client = param1._send('view:')
			if (argc >= 2):
				vStopped = param2
			#endif
		#endif
		super._send('init:', client)
		self._send('doit:')
	#end:method

	@classmethod
	def dispose():
		if (client._send('view:') == vStopped):
			client._send('view:', vWalking)
		#endif
		super._send('dispose:')
	#end:method

	@classmethod
	def doit():
		if client._send('isStopped:'):
			(cond
				case 
					(and
						(vStopped == -1)
						(client._send('loop:') != (kernel.NumLoops(client) - 1))
					):
					temp0 = client._send('loop:')
					super._send('doit:')
					client._send('loop:', (kernel.NumLoops(client) - 1), 'setCel:', temp0)
				#end:case
				case ((vStopped != -1) and (client._send('view:') == vWalking)):
					client._send('view:', vStopped)
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
					if (client._send('loop:') == (kernel.NumLoops(client) - 1)):
						client._send('loop:', client._send('cel:'), 'cel:', 0)
					#endif
				#end:case
			#end:match
			super._send('doit:')
		#endif
	#end:method

#end:class or instance

