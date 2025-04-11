#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 976
import sci_sh
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
		argc = sum(v is not None for v in locals().values())

		return 1
	#end:method

	@classmethod
	def findPosn():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		return 1
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (super handleEvent: param1):#end:case
			case (active and ((param1 type:) == 2)):
				active = 0
				(param1 claimed: 1)
				(LocalToGlobal param1)
				(self posn: ((param1 x:) + dx) ((param1 y:) + dy) z)
				(GlobalToLocal param1)
				if caller:
					(caller cue: self)
				#endif
			#end:case
			case (proc255_2 self param1):
				(param1 claimed: 1)
				(self track: param1)
			#end:case
		)
	#end:method

	@classmethod
	def track(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(LocalToGlobal param1)
		dx = (x - (param1 x:))
		dy = (y - (param1 y:))
		if doCast:
			active = 1
		else:
			(temp0 = (Collect new:) add: self)
			while
				(and
					(2 != (param1 type:))
					(outOfTouch or (proc255_2 self (param1 type: 1 yourself:)))
				):

				(self posn: ((param1 x:) + dx) ((param1 y:) + dy) z)
				(Animate (temp0 elements:) 1)
				(GetEvent 32767 param1)
			#end:loop
			(temp0 release: dispose:)
			if caller:
				(caller cue: self)
			#endif
			(GlobalToLocal param1)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (not doCast):
				active = 0
			#end:case
			case active:
				temp0 = (global80 curEvent:)
				(self posn: ((temp0 x:) + dx) ((temp0 y:) + dy) z)
			#end:case
		)
		(super doit:)
	#end:method

	@classmethod
	def posn(param1 = None, param2 = None, param3 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if argc:
			x = param1
			if (argc >= 2):
				y = param2
				if (argc >= 3):
					z = param3
				#endif
			#endif
		#endif
		temp0 = (proc999_0 diagonal)
		if (not (== -1 top bottom left right)):
			match (Abs diagonal)
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
			x = (proc999_3 left (proc999_2 right x))
			y = (proc999_3 top (proc999_2 bottom y))
		#endif
		(super posn: x y z)
	#end:method

#end:class or instance

