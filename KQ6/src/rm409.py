#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 409
import sci_sh
import kernel
import Main
import rLab
import n404
import KQ6Room
import n913
import RandCycle
import PolyPath
import Polygon
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm409 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.instance
class rm409(KQ6Room):
	#property vars (may be empty)
	modNum = 400
	noun = 2
	picture = 400
	style = 10
	horizon = 135
	south = 400
	walkOffEdge = 1
	autoLoad = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if rLab._send('hiddenDoorOpen:'):
			local0 = 54
			global2._send(
				'addObstacle:', Polygon._send('new:')._send(
						'type:', 2,
						'init:', 232, 144, 83, 144, 26, 185, 130, 185, 130, 189, 0, 189, 0, 0, 319, 4, 319, 171, 238, 171, 242, 154,
						'yourself:'
					), Polygon._send('new:')._send(
						'type:', 2,
						'init:', 319, 189, 192, 189, 192, 184, 319, 184,
						'yourself:'
					)
			)
		else:
			if rLab._send('seenSecretLatch:'):
				local0 = 53
			else:
				local0 = 55
			#endif
			global2._send(
				'addObstacle:', Polygon._send('new:')._send(
						'type:', 2,
						'init:', 0, 189, 0, 0, 319, 0, 319, 189, 190, 189, 190, 185, 266, 185, 237, 161, 235, 143, 86, 143, 39, 185, 130, 185, 130, 189,
						'yourself:'
					)
			)
		#endif
		super._send('init:', &rest)
		if (kernel.ScriptID(30, 0)._send('holeCoords:') == global11):
			proc404_1()
		#endif
		kernel.ScriptID(30, 0)._send('initCrypt:', 1)
		tapestry._send('init:')
		openDoor._send('init:')
		door._send('init:')
		myTorch._send('init:')
		self._send('setScript:', walkIn)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case global2._send('script:'):#end:case
			case global0._send('inRect:', 287, 167, 319, 189):
				kernel.ScriptID(30, 0)._send('prevEdgeHit:', 2)
				global2._send('setScript:', walkOut)
			#end:case
			case (global0._send('edgeHit:') == 3):
				kernel.ScriptID(30, 0)._send('prevEdgeHit:', 3)
				global2._send('setScript:', walkOut)
			#end:case
		)
		super._send('doit:', &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			match param1
				case 1:
					if rLab._send('hiddenDoorOpen:'):
						global91._send('say:', 2, 1, 54, 1, 0, 400)
						1
					else:
						global91._send('say:', 2, 1, 53, 1, 0, 400)
						1
					#endif
				#end:case
				else:
					super._send('doVerb:', param1, &rest)
				#end:else
			#end:match
		)
	#end:method

#end:class or instance

@SCI.instance
class tapestry(Prop):
	#property vars (may be empty)
	x = 246
	y = 189
	z = 100
	noun = 18
	modNum = 400
	view = 400
	loop = 5
	priority = 5
	signal = 26640
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('stopUpd:')
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 0:
				if rLab._send('seenSecretLatch:'):
					0
				else:
					global91._send('say:', 19, 0, 55, 1, 0, 400)
				#endif
			#end:case
			case 5:
				if rLab._send('hiddenDoorOpen:'):
					global2._send('setScript:', lookAtTapestry)
				else:
					global2._send('setScript:', liftTapestry)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class door(Prop):
	#property vars (may be empty)
	x = 278
	y = 189
	z = 73
	noun = 19
	modNum = 400
	approachX = 260
	approachY = 170
	view = 402
	loop = 3
	priority = 13
	signal = 16400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('approachVerbs:', 5)
		if rLab._send('hiddenDoorOpen:'):
			self._send('cel:', 5, 'stopUpd:')
		else:
			self._send('cel:', 0, 'stopUpd:')
		#endif
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 25:
				proc404_0(2)
			#end:case
			case 1:
				global91._send('say:', 19, 1, local0, 1, 0, 400)
			#end:case
			case 5:
				global91._send('say:', 19, 5, local0, 1, 0, 400)
			#end:case
			case 2:
				(cond
					case (not rLab._send('seenSecretLatch:')):
						global91._send('say:', 19, 2, 55, 1, 0, 400)
					#end:case
					case 
						(and
							rLab._send('seenSecretLatch:')
							(not rLab._send('hiddenDoorOpen:'))
						):
						global91._send('say:', 19, 2, 53, 1, 0, 400)
					#end:case
					case (rLab._send('hiddenDoorOpen:') and (not proc913_0(1))):
						global91._send('say:', 19, 2, 56, 1, 0, 400)
					#end:case
					case proc913_0(1):
						global91._send('say:', 19, 2, 57, 1, 0, 400)
					#end:case
				)
			#end:case
			else:
				(cond
					case (not rLab._send('seenSecretLatch:')):
						global91._send('say:', 19, 0, 55, 1, 0, 400)
					#end:case
					case 
						(and
							rLab._send('seenSecretLatch:')
							(not rLab._send('hiddenDoorOpen:'))
						):
						global91._send('say:', 19, 0, 53, 1, 0, 400)
					#end:case
					else:
						global91._send('say:', 19, 0, 54, 1, 0, 400)
					#end:else
				)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class openDoor(View):
	#property vars (may be empty)
	x = 278
	y = 189
	z = 73
	noun = 19
	modNum = 400
	approachX = 260
	approachY = 170
	view = 402
	loop = 2
	priority = 13
	signal = 16400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('approachVerbs:', 5)
		self._send('stopUpd:')
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		door._send('doVerb:', param1, &rest)
	#end:method

#end:class or instance

@SCI.instance
class myTorch(View):
	#property vars (may be empty)
	x = 77
	y = 141
	z = 71
	noun = 9
	modNum = 400
	view = 400
	loop = 8
	priority = 14
	signal = 17
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('stopUpd:')
		super._send('init:')
		myFlame._send('init:')
		myFlick._send('init:')
	#end:method

#end:class or instance

@SCI.instance
class myFlame(Prop):
	#property vars (may be empty)
	x = 84
	y = 141
	z = 95
	noun = 9
	modNum = 400
	view = 400
	loop = 2
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('setCycle:', Fwd, 'checkDetail:')
		super._send('init:')
	#end:method

#end:class or instance

@SCI.instance
class myFlick(Prop):
	#property vars (may be empty)
	x = 82
	y = 50
	modNum = 400
	onMeCheck = 0
	view = 400
	loop = 6
	signal = 16401
	cycleSpeed = 9
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('setCycle:', RandCycle, 'checkDetail:')
		super._send('init:')
	#end:method

#end:class or instance

@SCI.instance
class mino(Actor):
	#property vars (may be empty)
	x = 315
	y = 171
	yStep = 3
	view = 443
	signal = 16384
	xStep = 5
	
#end:class or instance

@SCI.instance
class walkIn(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				match kernel.ScriptID(30, 0)._send('prevEdgeHit:')
					case 4:
						global0._send(
							'posn:', 282, 164,
							'init:',
							'setMotion:', PolyPath, 247, 164, self
						)
					#end:case
					case 1:
						global0._send(
							'posn:', 158, 225,
							'init:',
							'setMotion:', PolyPath, 158, 187, self
						)
					#end:case
					else:
						global0._send('posn:', 160, 160, 'loop:', 2, 'init:')
						ticks = 6
					#end:else
				#end:match
			#end:case
			case 1:
				cycles = 6
			#end:case
			case 2:
				if ((global12 == 440) and (not proc913_0(1))):
					proc913_1(142)
					global91._send('say:', 1, 0, 50, 1, self, 400)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 3:
				global1._send('handsOn:')
				global69._send('enable:', 6)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walkOut(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				match kernel.ScriptID(30, 0)._send('prevEdgeHit:')
					case 3:
						global0._send('setMotion:', PolyPath, global0._send('x:'), 250, self)
					#end:case
					case 2:
						global0._send('setMotion:', PolyPath, 315, global0._send('y:'), self)
					#end:case
				#end:match
			#end:case
			case 1:
				match kernel.ScriptID(30, 0)._send('prevEdgeHit:')
					case 3:
						global2._send('newRoom:', 400)
					#end:case
					case 2:
						global2._send('newRoom:', 440)
					#end:case
				#end:match
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lookAtTapestry(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 235, 149, self)
			#end:case
			case 1:
				global0._send('setHeading:', 90)
				cycles = 6
			#end:case
			case 2:
				global91._send('say:', 18, 5, 54, 1, self, 400)
			#end:case
			case 3:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class liftTapestry(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 229, 146, self)
			#end:case
			case 1:
				global0._send('setHeading:', 90)
				cycles = 6
			#end:case
			case 2:
				if rLab._send('seenSecretLatch:'):
					local1 = 1
					local0 = 53
					global91._send('say:', 18, 5, 53, 1, self, 400)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 3:
				global0._send(
					'view:', 401,
					'setLoop:', 3,
					'cel:', 0,
					'normal:', 0,
					'illegalBits:', 0,
					'ignoreActors:', 1,
					'cycleSpeed:', 12,
					'posn:', (global0._send('x:') + 6), (global0._send('y:') + 3),
					'setCycle:', CT, 3, 1, self
				)
			#end:case
			case 4:
				global0._send('cel:', 4)
				tapestry._send('startUpd:', 'cel:', 1)
				cycles = 2
			#end:case
			case 5:
				global0._send('cel:', 5)
				tapestry._send('cel:', 2)
				cycles = 2
			#end:case
			case 6:
				if local1:
					global0._send(
						'setLoop:', 4,
						'cel:', 0,
						'posn:', (global0._send('x:') + 3), global0._send('y:'),
						'setCycle:', CT, 5, 1, self
					)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 7:
				if local1:
					global0._send('cel:', 6)
					cycles = 6
				else:
					self._send('cue:')
				#endif
			#end:case
			case 8:
				if local1:
					global0._send('cel:', 5)
					cycles = 6
				else:
					self._send('cue:')
				#endif
			#end:case
			case 9:
				if local1:
					global0._send('cel:', 4)
					cycles = 6
				else:
					self._send('cue:')
				#endif
			#end:case
			case 10:
				if local1:
					global0._send('cel:', 5)
					cycles = 6
				else:
					self._send('cue:')
				#endif
			#end:case
			case 11:
				if local1:
					global91._send('say:', 18, 5, 53, 2, self, 400)
				else:
					global91._send('say:', 18, 5, 55, 1, self, 400)
				#endif
			#end:case
			case 12:
				if local1:
					global0._send('cel:', 4)
					cycles = 6
				else:
					self._send('cue:')
				#endif
			#end:case
			case 13:
				if local1:
					global0._send('cel:', 5)
					cycles = 6
				else:
					self._send('cue:')
				#endif
			#end:case
			case 14:
				if local1:
					global0._send('cel:', 4)
					cycles = 6
				else:
					self._send('cue:')
				#endif
			#end:case
			case 15:
				if local1:
					global105._send('number:', 408, 'setLoop:', 1, 'play:')
					global0._send('cel:', 5)
					cycles = 6
				else:
					self._send('cue:')
				#endif
			#end:case
			case 16:
				if local1:
					global91._send('say:', 18, 5, 53, 3, self, 400)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 17:
				if local1:
					global0._send('cel:', 6)
					tapestry._send('setCycle:', Beg, self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 18:
				if local1:
					global105._send('number:', 909, 'setLoop:', 1, 'play:')
					door._send('setCycle:', End, self)
					rLab._send('hiddenDoorOpen:', 1)
					global2._send('obstacles:')._send('dispose:')
					local0 = 54
				else:
					self._send('cue:')
				#endif
			#end:case
			case 19:
				if local1:
					door._send('dispose:')
					global2._send(
						'addObstacle:', Polygon._send('new:')._send(
								'type:', 2,
								'init:', 232, 144, 83, 144, 26, 185, 130, 185, 130, 189, 0, 189, 0, 0, 319, 4, 319, 171, 238, 171, 242, 154,
								'yourself:'
							), Polygon._send('new:')._send(
								'type:', 2,
								'init:', 319, 189, 192, 189, 192, 184, 319, 184,
								'yourself:'
							)
					)
					global91._send('say:', 18, 5, 53, 4, self, 400)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 20:
				if local1:
					global1._send('givePoints:', 1)
					self._send('cue:')
				else:
					tapestry._send('cel:', 1)
					global0._send('setLoop:', 3, 'cel:', 5)
					cycles = 2
				#endif
			#end:case
			case 21:
				if local1:
					self._send('cue:')
				else:
					tapestry._send('cel:', 0)
					global0._send('cel:', 4)
					cycles = 2
				#endif
			#end:case
			case 22:
				if local1:
					self._send('cue:')
				else:
					global0._send('setCycle:', Beg, self)
				#endif
			#end:case
			case 23:
				global1._send('handsOn:')
				tapestry._send('stopUpd:')
				if local1:
					global0._send(
						'posn:', (global0._send('x:') - 9), (global0._send('y:') - 3),
						'reset:', 0
					)
				else:
					global0._send(
						'posn:', (global0._send('x:') - 6), (global0._send('y:') - 3),
						'reset:', 0
					)
				#endif
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

