#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 992
import sci_sh
import kernel
import Main
import System

class Cycle(Obj):
	#property vars (may be empty)
	client = 0
	caller = 0
	cycleDir = 1
	cycleCnt = 0
	completed = 0
	
	@classmethod
	def init(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			client = param1
		#endif
		cycleCnt = global88
		completed = 0
	#end:method

	@classmethod
	def nextCel():
		(return
			if (kernel.Abs((global88 - cycleCnt)) < client._send('cycleSpeed:')):
				client._send('cel:')
			else:
				cycleCnt = global88
				(client._send('cel:') + cycleDir)
			#endif
		)
	#end:method

	@classmethod
	def cycleDone():#end:method

	@classmethod
	def motionCue():
		client._send('cycler:', 0)
		if (completed and kernel.IsObject(caller)):
			caller._send('cue:')
		#endif
		self._send('dispose:')
	#end:method

#end:class or instance

class Fwd(Cycle):
	#property vars (may be empty)
	@classmethod
	def doit():
		if (temp0 = self._send('nextCel:') > client._send('lastCel:')):
			self._send('cycleDone:')
		else:
			client._send('cel:', temp0)
		#endif
	#end:method

	@classmethod
	def cycleDone():
		client._send('cel:', 0)
	#end:method

#end:class or instance

class Walk(Fwd):
	#property vars (may be empty)
	@classmethod
	def doit():
		if (not client._send('isStopped:')):
			super._send('doit:')
		#endif
	#end:method

#end:class or instance

class CT(Cycle):
	#property vars (may be empty)
	endCel = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', param1)
		cycleDir = param3
		if (argc == 4):
			caller = param4
		#endif
		temp0 = client._send('lastCel:')
		endCel = (temp0 if (param2 > temp0) else param2)
	#end:method

	@classmethod
	def doit():
		temp1 = client._send('lastCel:')
		if (endCel > temp1):
			endCel = temp1
		#endif
		temp0 = self._send('nextCel:')
		client._send(
			'cel:', (cond
					case (temp0 > temp1): 0#end:case
					case (temp0 < 0): temp1#end:case
					else: temp0#end:else
				)
		)
		if ((global88 == cycleCnt) and (endCel == client._send('cel:'))):
			self._send('cycleDone:')
		#endif
	#end:method

	@classmethod
	def cycleDone():
		completed = 1
		if caller:
			global37 = 1
		else:
			self._send('motionCue:')
		#endif
	#end:method

#end:class or instance

class End(CT):
	#property vars (may be empty)
	@classmethod
	def init(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', param1, param1._send('lastCel:'), 1, (param2 if (argc == 2) else 0))
	#end:method

#end:class or instance

class Beg(CT):
	#property vars (may be empty)
	@classmethod
	def init(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', param1, 0, -1, (param2 if (argc == 2) else 0))
	#end:method

#end:class or instance

class SyncWalk(Fwd):
	#property vars (may be empty)
	xLast = 0
	yLast = 0
	
	@classmethod
	def doit():
		if 
			(and
				kernel.IsObject(temp0 = client._send('mover:'))
				((client._send('x:') != xLast) or (client._send('y:') != yLast))
			)
			xLast = client._send('x:')
			yLast = client._send('y:')
			super._send('doit:')
		#endif
	#end:method

	@classmethod
	def nextCel():
		cycleCnt = (global88 + client._send('cycleSpeed:'))
		super._send('nextCel:')
	#end:method

#end:class or instance

class Motion(Obj):
	#property vars (may be empty)
	client = 0
	caller = 0
	x = 0
	y = 0
	dx = 0
	dy = 0
	b-moveCnt = 0
	b-i1 = 0
	b-i2 = 0
	b-di = 0
	b-xAxis = 0
	b-incr = 0
	completed = 0
	xLast = 0
	yLast = 0
	
	@classmethod
	def init(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (argc >= 1):
			client = param1
			if (argc >= 2):
				x = param2
				if (argc >= 3):
					y = param3
					if (argc >= 4):
						caller = param4
					#endif
				#endif
			#endif
		#endif
		yLast = xLast = completed = 0
		b-moveCnt = (+ 1 client._send('moveSpeed:') global88)
		if temp3 = client._send('cycler:'):
			temp3._send('cycleCnt:', b-moveCnt)
		#endif
		if kernel.GetDistance(temp2 = client._send('x:'), temp3 = client._send('y:'), x, y):
			client._send('setHeading:', kernel.GetAngle(temp2, temp3, x, y))
		#endif
		kernel.InitBresen(self)
	#end:method

	@classmethod
	def onTarget():
		return ((client._send('x:') == x) and (client._send('y:') == y))
	#end:method

	@classmethod
	def setTarget(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			x = param1
			y = param2
		#endif
	#end:method

	@classmethod
	def doit():
		if (kernel.Abs((global88 - b-moveCnt)) >= client._send('moveSpeed:')):
			b-moveCnt = global88
			kernel.DoBresen(self)
		#endif
	#end:method

	@classmethod
	def moveDone():
		completed = 1
		if caller:
			global37 = 1
		else:
			self._send('motionCue:')
		#endif
	#end:method

	@classmethod
	def motionCue():
		client._send('mover:', 0)
		if (completed and kernel.IsObject(caller)):
			caller._send('cue:')
		#endif
		self._send('dispose:')
	#end:method

#end:class or instance

class MoveTo(Motion):
	#property vars (may be empty)
	@classmethod
	def onTarget():
		(return
			(and
				(kernel.Abs((client._send('x:') - x)) <= client._send('xStep:'))
				(kernel.Abs((client._send('y:') - y)) <= client._send('yStep:'))
			)
		)
	#end:method

#end:class or instance

