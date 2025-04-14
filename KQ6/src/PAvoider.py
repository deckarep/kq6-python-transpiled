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
def localproc_0(param1 = None, *rest):
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
def localproc_1(param1 = None, *rest):
	temp3 = param1._send('size:')
	temp0 = 0
	while (temp0 < temp3): # inline for
		temp1 = param1._send('at:', temp0)
		if (temp2 = temp1._send('type:') >= 16):
			temp1._send('type:', (temp2 - 16))
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
	def init(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (argc >= 1):
			client = param1
		#endif
	#end:method

	@classmethod
	def dispose():
		if kernel.IsObject(oldBlockerMover):
			oldBlockerMover._send('dispose:')
		#endif
		super._send('dispose:')
	#end:method

	@classmethod
	def doit():
		temp9 = client._send('mover:')
		if (oldBlocker and (client._send('distanceTo:', oldBlocker) >= 20)):
			oldBlocker._send('ignoreActors:', 0)
			if oldBlockerMover:
				oldBlocker._send('mover:', oldBlockerMover)
			#endif
			oldMoverY = oldMoverX = -99
			oldBlocker = oldBlockerMover = 0
			if 
				(and
					temp9
					kernel.IsObject(temp9._send('obstacles:'))
					temp9._send('obstacles:')._send('isEmpty:')
				)
				temp9._send('obstacles:')._send('dispose:')
				temp9._send('obstacles:', 0)
			#endif
		#endif
		if 
			(and
				temp9 = client._send('mover:')
				kernel.IsObject(temp4 = temp9._send('doit:'))
				(not temp9._send('completed:'))
				temp9._send('isKindOf:', PolyPath)
			)
			if temp4._send('respondsTo:', #mover):
				oldBlockerMover = temp4._send('mover:')
				if oldBlockerMover:
					temp4._send('mover:', 0)
				#endif
			else:
				oldBlockerMover = 0
			#endif
			oldMoverX = temp9._send('finalX:')
			oldMoverY = temp9._send('finalY:')
			oldBlocker = temp4
			oldBlocker._send('ignoreActors:', 1)
			(= temp5
				(-
					temp4._send('brLeft:')
					(= temp2
						(+
							(2 * client._send('xStep:'))
							(/
								proc999_3(kernel.CelWide(client._send('view:'), 2, 0), kernel.CelWide(client._send(
									'view:'
								), 0, 0))
								2
							)
						)
					)
				)
			)
			temp6 = kernel.CoordPri(1, kernel.CoordPri(temp4._send('y:')))
			temp3 = (2 * temp4._send('yStep:'))
			temp7 = (temp4._send('brRight:') + temp2)
			if ((temp8 = (+ temp4._send('y:') temp3 2) - temp6) <= 3):
				(temp6 -= 2)
				(temp8 += 2)
			#endif
			temp0 = (temp9._send('finalX:') - client._send('x:'))
			temp1 = (temp9._send('finalY:') - client._send('y:'))
			temp23 = client._send('heading:')
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
						Polygon._send('new:')._send(
							'init:', temp5, client._send('y:'), temp5, temp6, temp7, temp6, temp7, client._send(
									'y:'
								), 30583, 0,
							'type:', 2,
							'name:', r"""isBlockedPoly""",
							'yourself:'
						)
					)
				#end:case
				case 2:
					(= temp17
						Polygon._send('new:')._send(
							'init:', temp7, client._send('y:'), temp7, temp8, temp5, temp8, temp5, client._send(
									'y:'
								), 30583, 0,
							'type:', 2,
							'name:', r"""isBlockedPoly""",
							'yourself:'
						)
					)
				#end:case
				case 0:
					(= temp17
						Polygon._send('new:')._send(
							'init:', client._send('x:'), temp6, temp7, temp6, temp7, temp8, client._send(
									'x:'
								), temp8, 30583, 0,
							'type:', 2,
							'name:', r"""isBlockedPoly""",
							'yourself:'
						)
					)
				#end:case
				case 1:
					(= temp17
						Polygon._send('new:')._send(
							'init:', client._send('x:'), temp8, temp5, temp8, temp5, temp6, client._send(
									'x:'
								), temp6, 30583, 0,
							'type:', 2,
							'name:', r"""isBlockedPoly""",
							'yourself:'
						)
					)
				#end:case
			#end:match
			if (not temp9._send('obstacles:')):
				temp9._send('obstacles:', List._send('new:'))
			#endif
			if 
				(= temp16
					kernel.MergePoly(temp17._send('points:'), temp9._send('obstacles:')._send(
						'elements:'
					), temp9._send('obstacles:')._send('size:'))
				)
				temp15 = Polygon._send('new:')._send(
					'points:', temp16,
					'size:', localproc_0(temp16),
					'type:', 2,
					'dynamic:', 1
				)
			#endif
			temp9._send('obstacles:')._send('add:', temp15)
			temp9._send('value:', 2, 'init:', client, temp9._send('finalX:'), temp9._send('finalY:'))
			temp9._send('obstacles:')._send('delete:', temp15)
			temp9._send('obstacles:')._send('delete:', temp17)
			if kernel.IsObject(temp9._send('obstacles:')):
				localproc_1(temp9._send('obstacles:'))
			#endif
			temp17._send('dispose:')
			temp15._send('dispose:')
		#endif
	#end:method

#end:class or instance

