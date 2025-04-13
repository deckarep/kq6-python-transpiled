#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 950
import sci_sh
import kernel
import Main
import PolyPath
import System

class CueObj(Script):
	#property vars (may be empty)
	theVerb = 0
	
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 1:
				global0._send(
					'setHeading:', kernel.GetAngle(global0._send('x:'), global0._send(
							'y:'
						), client._send('x:'), client._send('y:')), self
				)
				global78._send('add:', self)
			#end:case
			case 2:
				cycles = 3
			#end:case
			case 3:
				global78._send('delete:', self)
				if 
					(not
						(and
							kernel.IsObject(client)
							kernel.IsObject(client._send('actions:'))
							client._send('actions:')._send('doVerb:', theVerb)
						)
					)
					client._send('doVerb:', theVerb)
				#endif
				state = 0
			#end:case
		#end:match
	#end:method

#end:class or instance

class Feature(Obj):
	#property vars (may be empty)
	x = 0
	y = 0
	z = 0
	heading = 0
	noun = 0
	modNum = -1
	nsTop = 0
	nsLeft = 0
	nsBottom = 0
	nsRight = 0
	sightAngle = 26505
	actions = 0
	onMeCheck = 26505
	state = 0
	approachX = 0
	approachY = 0
	approachDist = 0
	_approachVerbs = 0
	
	@classmethod
	def init(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('initialize:', (param1 if argc else 0))
		if self._send('respondsTo:', #underBits):
			global5._send('add:', self)
		else:
			global32._send('add:', self)
		#endif
	#end:method

	@classmethod
	def initialize(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (argc and param1):
				self._send('perform:', param1)
			#end:case
			case global64:
				self._send('perform:', global64)
			#end:case
		)
	#end:method

	@classmethod
	def approachVerbs(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		_approachVerbs = 0
		if (argc and global66 and param1[0]):
			temp0 = 0
			while (temp0 < argc): # inline for
				temp1 = global66._send('doit:', param1[temp0])
				self._send('_approachVerbs:', (| self._send('_approachVerbs:') temp1))
				# for:reinit
				temp0.post('++')
			#end:loop
		#endif
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case param1._send('claimed:'):
				return 1
			#end:case
			case 
				(and
					(param1._send('type:') & 0x4000)
					self._send('onMe:', param1)
					self._send('isNotHidden:')
				):
				CueObj._send(
					'state:', 0,
					'cycles:', 0,
					'client:', self,
					'theVerb:', param1._send('message:')
				)
				param1._send('claimed:', 1)
				if 
					(and
						global80._send('canControl:')
						(global0._send('state:') & 0x0002)
						(>
							kernel.GetDistance(global0._send('x:'), global0._send('y:'), approachX, approachY)
							approachDist
						)
						global66
						(_approachVerbs & global66._send('doit:', param1._send('message:')))
					)
					global0._send(
						'setMotion:', PolyPath, approachX, (+
								global0._send('z:')
								approachY
							), CueObj
					)
				else:
					global0._send('setMotion:', 0)
					if self._send('facingMe:'):
						CueObj._send('changeState:', 3)
					#endif
				#endif
			#end:case
		)
		param1._send('claimed:')
	#end:method

	@classmethod
	def notFacing():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global0._send('setMotion:', 0)
		CueObj._send('client:', self, 'state:', 0, 'cycles:', 0, 'cue:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = (global65 if global65 else dftDoVerb)
		if (modNum == -1):
			modNum = global11
		#endif
		if (global90 and kernel.Message(0, modNum, noun, param1, 0, 1)):
			global91._send('say:', noun, param1, 0, 0, 0, modNum)
		else:
			temp0._send('doit:', param1, self)
		#endif
	#end:method

	@classmethod
	def facingMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case argc:
				temp0 = param1
			#end:case
			case global5._send('contains:', global0):
				temp0 = global0
			#end:case
			else:
				return 1
			#end:else
		)
		if 
			(>
				(= temp1
					kernel.Abs((-
						kernel.GetAngle(temp0._send('x:'), temp0._send('y:'), x, y)
						temp0._send('heading:')
					))
				)
				180
			)
			temp1 = (360 - temp1)
		#endif
		if (temp1 <= sightAngle):
			return 1
		else:
			if (sightAngle != 26505):
				self._send('notFacing:')
			#endif
			return 0
		#endif
	#end:method

	@classmethod
	def isNotHidden():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return 1
	#end:method

	@classmethod
	def onMe(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if kernel.IsObject(param1):
			temp0 = param1._send('x:')
			temp1 = param1._send('y:')
		else:
			temp0 = param1
			temp1 = param2
		#endif
		(return
			(cond
				case (state & 0x0004):
					if 
						(or
							(not (nsLeft or nsRight or nsTop or nsBottom))
							(and
								(<= nsLeft temp0 nsRight)
								(<= nsTop temp1 nsBottom)
							)
						)
						(onMeCheck & kernel.OnControl(4, temp0, temp1))
					else:
						0
					#endif
				#end:case
				case kernel.IsObject(onMeCheck):
					kernel.AvoidPath(temp0, temp1, onMeCheck)
				#end:case
				case 
					(or
						(not (nsLeft or nsRight or nsTop or nsBottom))
						(and
							(<= nsLeft temp0 nsRight)
							(<= nsTop temp1 nsBottom)
						)
					):
					1
				#end:case
				else: 0#end:else
			)
		)
	#end:method

	@classmethod
	def setName(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(state |= 0x0001)
		name = kernel.Memory(1, (kernel.StrLen(param1) + 1))
		kernel.StrCpy(name, param1)
	#end:method

	@classmethod
	def setOnMeCheck(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 26505:
				onMeCheck = param1
				(state &= 0xfffb)
			#end:case
			case 2:
				onMeCheck = param2[0]
				(state &= 0xfffb)
			#end:case
			case 1:
				temp0 = onMeCheck = 0
				while (temp0 < (argc - 1)): # inline for
					(onMeCheck |= param2[temp0])
					# for:reinit
					temp0.post('++')
				#end:loop
				(state |= 0x0004)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if actions:
			actions._send('dispose:')
			actions = 0
		#endif
		if (kernel.IsObject(onMeCheck) and (not (state & 0x0004))):
			onMeCheck._send('dispose:')
			onMeCheck = 0
		#endif
		global32._send('delete:', self)
		if (state & 0x0001):
			kernel.Memory(3, name)
			name = 0
		#endif
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class dftDoVerb(Code):
	#property vars (may be empty)
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return 1
	#end:method

#end:class or instance

class Actions(Code):
	#property vars (may be empty)
	@classmethod
	def doVerb():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return 0
	#end:method

#end:class or instance

