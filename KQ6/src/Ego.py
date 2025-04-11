#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 988
import sci_sh
import Main
import PolyPath
import Motion
import Actor

class Ego(Actor):
	#property vars (may be empty)
	signal = 8192
	edgeHit = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init:)
		if (not cycler):
			(self setCycle: Walk)
		#endif
	#end:method

	@classmethod
	def facingMe():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		return 1
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super doit:)
		(= edgeHit
			(cond
				case (x <= 0): 4#end:case
				case (x >= 319): 2#end:case
				case (y >= 189): 3#end:case
				case (y <= (global2 horizon:)): 1#end:case
				else: 0#end:else
			)
		)
	#end:method

	@classmethod
	def get(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 0
		while (temp0 < argc): # inline for
			((global9 at: param1[temp0]) moveTo: self)
			# for:reinit
			temp0++
		#end:loop
	#end:method

	@classmethod
	def put(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (self has: param1):
			(temp0 = (global9 at: param1)
				moveTo: (-1 if (argc == 1) else param2)
			)
			if (global69 and ((global69 curInvIcon:) == temp0)):
				(global69
					curInvIcon: 0
					disable: ((global69 useIconItem:) cursor: 999 yourself:)
				)
			#endif
		#endif
	#end:method

	@classmethod
	def has(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if temp0 = (global9 at: param1):
			(temp0 ownedBy: self)
		#endif
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp1 = (param1 type:)
		temp2 = (param1 message:)
		(cond
			case (script and (script handleEvent: param1)): 1#end:case
			case (temp1 & 0x0040):
				if ((temp0 = temp2 == 0) and (temp1 & 0x0004)):
					(param1 claimed:)
					return
				#endif
				if 
					(and
						(temp1 & 0x0004)
						(temp0 == (global80 prevDir:))
						(IsObject mover)
					)
					temp0 = 0
				#endif
				(global80 prevDir: temp0)
				(self setDirection: temp0)
				(param1 claimed: 1)
			#end:case
			case (temp1 & 0x4000):
				if (temp1 & 0x1000):
					match global67
						case 0:
							(self
								setMotion: MoveTo (param1 x:) ((param1 y:) + z)
							)
						#end:case
						case 1:
							(self
								setMotion:
									PolyPath
									(param1 x:)
									((param1 y:) + z)
							)
						#end:case
						case 2:
							(self
								setMotion:
									PolyPath
									(param1 x:)
									((param1 y:) + z)
									0
									0
							)
						#end:case
					#end:match
					(global80 prevDir: 0)
					(param1 claimed: 1)
				else:
					(super handleEvent: param1)
				#endif
			#end:case
			else:
				(super handleEvent: param1)
			#end:else
		)
		(param1 claimed:)
	#end:method

#end:class or instance

