#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 976
import sci_sh
import kernel
import Main
import Interface
import Actor
import System

class Cat(Actor):
	#property vars (may be empty)
	top = -1
	left = -1
	bottom = -1
	right = -1
	diagonal = 0
	doCast = 0
	outOfTouch = 1
	caller = 0
	active = 0
	dx = 0
	dy = 0
	
	@classmethod
	def canBeHere():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return 1
	#end:method

	@classmethod
	def findPosn():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return 1
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case super._send('handleEvent:', param1):#end:case
			case (active and (param1._send('type:') == 2)):
				active = 0
				param1._send('claimed:', 1)
				kernel.LocalToGlobal(param1)
				self._send('posn:', (param1._send('x:') + dx), (param1._send('y:') + dy), z)
				kernel.GlobalToLocal(param1)
				if caller:
					caller._send('cue:', self)
				#endif
			#end:case
			case proc255_2(self, param1):
				param1._send('claimed:', 1)
				self._send('track:', param1)
			#end:case
		)
	#end:method

	@classmethod
	def track(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.LocalToGlobal(param1)
		dx = (x - param1._send('x:'))
		dy = (y - param1._send('y:'))
		if doCast:
			active = 1
		else:
			temp0 = Collect._send('new:')._send('add:', self)
			while
				(and
					(2 != param1._send('type:'))
					(outOfTouch or proc255_2(self, param1._send('type:', 1, 'yourself:')))
				):

				self._send('posn:', (param1._send('x:') + dx), (param1._send('y:') + dy), z)
				kernel.Animate(temp0._send('elements:'), 1)
				kernel.GetEvent(32767, param1)
			#end:loop
			temp0._send('release:', 'dispose:')
			if caller:
				caller._send('cue:', self)
			#endif
			kernel.GlobalToLocal(param1)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (not doCast):
				active = 0
			#end:case
			case active:
				temp0 = global80._send('curEvent:')
				self._send('posn:', (temp0._send('x:') + dx), (temp0._send('y:') + dy), z)
			#end:case
		)
		super._send('doit:')
	#end:method

	@classmethod
	def posn(param1 = None, param2 = None, param3 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			x = param1
			if (argc >= 2):
				y = param2
				if (argc >= 3):
					z = param3
				#endif
			#endif
		#endif
		temp0 = proc999_0(diagonal)
		if (not (== -1 top bottom left right)):
			match kernel.Abs(diagonal)
				case 1:
					(= y
						(+
							(top if (temp0 > 0) else bottom)
							(/
								(* (right - x) (bottom - top) temp0)
								(right - left)
							)
						)
					)
				#end:case
				case 2:
					(= x
						(+
							(left if (temp0 > 0) else right)
							(/
								(* (bottom - y) (right - left) temp0)
								(bottom - top)
							)
						)
					)
				#end:case
			#end:match
			x = proc999_3(left, proc999_2(right, x))
			y = proc999_3(top, proc999_2(bottom, y))
		#endif
		super._send('posn:', x, y, z)
	#end:method

#end:class or instance

