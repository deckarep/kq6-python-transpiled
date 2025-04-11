#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 961
import sci_sh
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
	def init(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if argc:
			vWalking = (client = param1 view:)
			if (argc >= 2):
				vStopped = param2
			#endif
		#endif
		(super init: client)
		(self doit:)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((client view:) == vStopped):
			(client view: vWalking)
		#endif
		(super dispose:)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (client isStopped:):
			(cond
				case 
					(and
						(vStopped == -1)
						((client loop:) != ((NumLoops client) - 1))
					):
					temp0 = (client loop:)
					(super doit:)
					(client loop: ((NumLoops client) - 1) setCel: temp0)
				#end:case
				case ((vStopped != -1) and ((client view:) == vWalking)):
					(client view: vStopped)
					(super doit:)
				#end:case
				case (vStopped != -1):
					(super doit:)
				#end:case
			)
		else:
			match vStopped
				case (client view:):
					(client view: vWalking)
				#end:case
				case -1:
					(client setLoop: -1 setCel: -1)
					if ((client loop:) == ((NumLoops client) - 1)):
						(client loop: (client cel:) cel: 0)
					#endif
				#end:case
			#end:match
			(super doit:)
		#endif
	#end:method

#end:class or instance

