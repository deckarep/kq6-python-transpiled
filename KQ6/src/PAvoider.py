#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 927
import sci_sh
import kernel
import PolyPath
import Polygon
import System

@SCI.procedure
def localproc_0(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	temp3 = -100
	temp0 = 0
	while (temp3 != 30583): # inline for
		temp3 = proc999_6(param1, (2 * temp0))
		# for:reinit
		temp0.post('++')
	#end:loop
	temp0.post('--')
#end:procedure

@SCI.procedure
def localproc_1(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	temp3 = (param1 size:)
	temp0 = 0
	while (temp0 < temp3): # inline for
		temp1 = (param1 at: temp0)
		if (temp2 = (temp1 type:) >= 16):
			(temp1 type: (temp2 - 16))
		#endif
		# for:reinit
		temp0.post('++')
	#end:loop
#end:procedure

class PAvoider(Code):
	#property vars (may be empty)
	client = 0
	oldBlocker = 0
	oldBlockerMover = 0
	oldMoverX = -99
	oldMoverY = -99
	
	@classmethod
	def init(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (argc >= 1):
			client = param1
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if kernel.IsObject(oldBlockerMover):
			(oldBlockerMover dispose:)
		#endif
		(super dispose:)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp9 = (client mover:)
		if (oldBlocker and ((client distanceTo: oldBlocker) >= 20)):
			(oldBlocker ignoreActors: 0)
			if oldBlockerMover:
				(oldBlocker mover: oldBlockerMover)
			#endif
			oldMoverY = oldMoverX = -99
			oldBlocker = oldBlockerMover = 0
			if 
				(and
					temp9
					kernel.IsObject((temp9 obstacles:))
					((temp9 obstacles:) isEmpty:)
				)
				((temp9 obstacles:) dispose:)
				(temp9 obstacles: 0)
			#endif
		#endif
		if 
			(and
				temp9 = (client mover:)
				kernel.IsObject(temp4 = (temp9 doit:))
				(not (temp9 completed:))
				(temp9 isKindOf: PolyPath)
			)
			if (temp4 respondsTo: #mover):
				oldBlockerMover = (temp4 mover:)
				if oldBlockerMover:
					(temp4 mover: 0)
				#endif
			else:
				oldBlockerMover = 0
			#endif
			oldMoverX = (temp9 finalX:)
			oldMoverY = (temp9 finalY:)
			oldBlocker = temp4
			(oldBlocker ignoreActors: 1)
			(= temp5
				(-
					(temp4 brLeft:)
					(= temp2
						(+
							(2 * (client xStep:))
							(/
								proc999_3(kernel.CelWide((client view:), 2, 0), kernel.CelWide((client
									view:
								), 0, 0))
								2
							)
						)
					)
				)
			)
			temp6 = kernel.CoordPri(1, kernel.CoordPri((temp4 y:)))
			temp3 = (2 * (temp4 yStep:))
			temp7 = ((temp4 brRight:) + temp2)
			if ((temp8 = (+ (temp4 y:) temp3 2) - temp6) <= 3):
				(temp6 -= 2)
				(temp8 += 2)
			#endif
			temp0 = ((temp9 finalX:) - (client x:))
			temp1 = ((temp9 finalY:) - (client y:))
			temp23 = (client heading:)
			(cond
				case (<= 85 temp23 95):
					temp14 = 0
				#end:case
				case (<= 265 temp23 275):
					temp14 = 1
				#end:case
				case (temp1 >= 0):
					temp14 = 2
				#end:case
				else:
					temp14 = 3
				#end:else
			)
			match temp14
				case 3:
					(= temp17
						((Polygon new:)
							init:
								temp5
								(client y:)
								temp5
								temp6
								temp7
								temp6
								temp7
								(client y:)
								30583
								0
							type: 2
							name: r"""isBlockedPoly"""
							yourself:
						)
					)
				#end:case
				case 2:
					(= temp17
						((Polygon new:)
							init:
								temp7
								(client y:)
								temp7
								temp8
								temp5
								temp8
								temp5
								(client y:)
								30583
								0
							type: 2
							name: r"""isBlockedPoly"""
							yourself:
						)
					)
				#end:case
				case 0:
					(= temp17
						((Polygon new:)
							init:
								(client x:)
								temp6
								temp7
								temp6
								temp7
								temp8
								(client x:)
								temp8
								30583
								0
							type: 2
							name: r"""isBlockedPoly"""
							yourself:
						)
					)
				#end:case
				case 1:
					(= temp17
						((Polygon new:)
							init:
								(client x:)
								temp8
								temp5
								temp8
								temp5
								temp6
								(client x:)
								temp6
								30583
								0
							type: 2
							name: r"""isBlockedPoly"""
							yourself:
						)
					)
				#end:case
			#end:match
			if (not (temp9 obstacles:)):
				(temp9 obstacles: (List new:))
			#endif
			if 
				(= temp16
					kernel.MergePoly((temp17 points:), ((temp9 obstacles:)
						elements:
					), ((temp9 obstacles:) size:))
				)
				(temp15 = (Polygon new:)
					points: temp16
					size: localproc_0(temp16)
					type: 2
					dynamic: 1
				)
			#endif
			((temp9 obstacles:) add: temp15)
			(temp9 value: 2 init: client (temp9 finalX:) (temp9 finalY:))
			((temp9 obstacles:) delete: temp15)
			((temp9 obstacles:) delete: temp17)
			if kernel.IsObject((temp9 obstacles:)):
				localproc_1((temp9 obstacles:))
			#endif
			(temp17 dispose:)
			(temp15 dispose:)
		#endif
	#end:method

#end:class or instance

