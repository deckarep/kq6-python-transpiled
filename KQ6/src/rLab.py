#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 30
import sci_sh
import kernel
import Main
import n404
import KQ6Room
import n913
import RandCycle
import PolyPath
import Feature
import Motion
import Game
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rLab = 0,
	walkIn = 1,
	walkOut = 2,
	theTorch = 3,
	corpseNiche = 4,
	leftDoor = 5,
	rightDoor = 6,
	topDoor = 7,
	bottomBlock = 8,
	leftWing = 9,
	rightWing = 10,
	checkBody = 11,
	rat = 12,
	bat = 13,
)

class rLab(Rgn):
	#property vars (may be empty)
	modNum = 400
	curLabyrinthRoom = 0
	labCoords = 0
	prevEdgeHit = 0
	timesInHoleWallRoom = 0
	timesGenieHasAppeared = 0
	geniePresent = 0
	hiddenDoorOpen = 0
	seenSecretLatch = 0
	crushCeilingCel = 0
	crushCeilingY = 0
	corpseWall = 0
	darkRoomLit = 0
	msgNum = 1
	holeCoords = 0
	holeWall = 0
	holeIsUp = 0
	seenByMino = 0
	scarfOnMino = 0
	
	@classmethod
	def initCrypt(param1 = None, *rest):
		self._send('corpseWall:', param1)
		corpseNiche._send('addToPic:')
	#end:method

	@classmethod
	def notify():
		global32._send('add:', floor, eastWall, northWall, westWall, 'eachElementDo:', #init)
	#end:method

	@classmethod
	def cue():
		match global11
			case 407:
				eastWall._send('dispose:')
			#end:case
			case 410:
				eastWall._send('dispose:')
				westWall._send('dispose:')
				northWall._send('dispose:')
				if (not proc913_0(1)):
					floor._send('dispose:')
				#endif
			#end:case
			else:
				floor._send('dispose:')
				eastWall._send('dispose:')
				westWall._send('dispose:')
				northWall._send('dispose:')
			#end:else
		#end:match
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		if kernel.ScriptID(30, 0)._send('holeIsUp:'):
			proc404_2()
		#endif
		(= keep
			proc999_5(param1, 400, 405, 410, 415, 420, 425, 430, 435, 440, 406, 407, 408, 409, 411)
		)
		initialized = 0
		match global12
			case 407:
				eastWall._send('init:')
			#end:case
			case 410:
				floor._send('init:')
			#end:case
			case 420:
				global32._send(
					'add:', floor, eastWall, northWall, westWall,
					'eachElementDo:', #init
				)
			#end:case
			case 440:
				global32._send(
					'add:', floor, eastWall, northWall, westWall,
					'eachElementDo:', #init
				)
			#end:case
		#end:match
		super._send('newRoom:', param1, &rest)
	#end:method

	@classmethod
	def init():
		super._send('init:', &rest)
		(cond
			case proc913_0(1):
				timesGenieHasAppeared = 3
				hiddenDoorOpen = seenSecretLatch = 1
				rLab._send('darkRoomLit:', 1)
			#end:case
			case (not script):
				self._send('setScript:', minotaurTimer)
			#end:case
		)
		if (global102._send('number:') != 400):
			global102._send('number:', 400, 'setLoop:', -1, 'play:')
		#endif
		global32._send('add:', floor, eastWall, northWall, westWall, 'eachElementDo:', #init)
	#end:method

#end:class or instance

class LabRoom(KQ6Room):
	#property vars (may be empty)
	modNum = 400
	noun = 2
	picture = 400
	horizon = 135
	walkOffEdge = 1
	autoLoad = 0
	
	@classmethod
	def makeCritters():
		if kernel.Random(0, 1):
			if kernel.Random(0, 1):
				if global10._send('contains:', corpseNiche):
					match rLab._send('prevEdgeHit:')
						case 1:
							if 
								proc999_5(rLab._send('labCoords:'), 19, 22, 35, 38, 51, 67, 85, 87, 97, 99, 101, 103, 113, 115, 117, 146, 149, 161, 163, 165, 168, 177, 179, 184, 193, 197, 200, 209, 213, 216, 226, 228, 230, 243)
								match rLab._send('corpseWall:')
									case 4:
										global0._send('setScript:', rats, 0, 3)
									#end:case
									case 2:
										global0._send('setScript:', rats, 0, 5)
									#end:case
								#end:match
							#endif
						#end:case
						case 3:
							if 
								proc999_5(rLab._send('labCoords:'), 3, 6, 19, 22, 35, 51, 69, 71, 81, 83, 85, 87, 97, 99, 101, 117, 130, 133, 145, 147, 149, 152, 161, 163, 168, 177, 184, 193, 197, 200, 210, 212, 214, 227)
								match rLab._send('corpseWall:')
									case 4:
										global0._send('setScript:', rats, 0, 4)
									#end:case
									case 2:
										global0._send('setScript:', rats, 0, 6)
									#end:case
								#end:match
							#endif
						#end:case
						case 4:
							if 
								(and
									proc999_5(rLab._send('labCoords:'), 2, 3, 7, 20, 21, 22, 39, 66, 67, 68, 69, 82, 83, 86, 87, 113, 114, 115, 116, 117, 146, 147, 148, 149, 150, 151, 152, 177, 178, 179, 180, 184, 210, 213, 214, 215, 216, 227, 228)
									(rLab._send('corpseWall:') == 1)
								)
								global0._send('setScript:', rats, 0, 1)
							#endif
						#end:case
						case 2:
							if 
								(and
									proc999_5(rLab._send('labCoords:'), 1, 2, 6, 19, 20, 21, 38, 65, 66, 67, 68, 81, 82, 85, 86, 112, 113, 114, 115, 116, 145, 146, 147, 148, 149, 150, 151, 176, 177, 178, 179, 183, 209, 212, 213, 214, 215, 226, 227)
									(rLab._send('corpseWall:') == 1)
								)
								global0._send('setScript:', rats, 0, 2)
							#endif
						#end:case
					#end:match
				#endif
			else:
				match rLab._send('prevEdgeHit:')
					case 1:
						(cond
							case 
								proc999_5(rLab._send('labCoords:'), 19, 22, 35, 38, 51, 67, 85, 87, 97, 99, 101, 103, 113, 115, 117, 146, 149, 161, 163, 165, 168, 177, 179, 184, 193, 197, 200, 209, 213, 216, 226, 228, 230, 243):
								global0._send('setScript:', bats, 0, 1)
							#end:case
							case 
								(and
									proc999_5(rLab._send('labCoords:'), 2, 3, 7, 20, 21, 22, 39, 66, 67, 68, 69, 82, 83, 86, 87, 113, 114, 115, 116, 117, 146, 147, 148, 149, 150, 151, 152, 177, 178, 179, 180, 184, 210, 213, 214, 215, 216, 227, 228)
									proc999_5(rLab._send('labCoords:'), 1, 2, 6, 19, 20, 21, 38, 65, 66, 67, 68, 81, 82, 85, 86, 112, 113, 114, 115, 116, 145, 146, 147, 148, 149, 150, 151, 176, 177, 178, 179, 183, 209, 212, 213, 214, 215, 226, 227)
								):
								if 2:
									global0._send('setScript:', bats, 0, 4)
								else:
									global0._send('setScript:', bats, 0, 2)
								#endif
							#end:case
						)
					#end:case
					case 3:
						(cond
							case 
								proc999_5(rLab._send('labCoords:'), 3, 6, 19, 22, 35, 51, 69, 71, 81, 83, 85, 87, 97, 99, 101, 117, 130, 133, 145, 147, 149, 152, 161, 163, 168, 177, 184, 193, 197, 200, 210, 212, 214, 227):
								global0._send('setScript:', bats, 0, 3)
							#end:case
							case 
								(and
									proc999_5(rLab._send('labCoords:'), 2, 3, 7, 20, 21, 22, 39, 66, 67, 68, 69, 82, 83, 86, 87, 113, 114, 115, 116, 117, 146, 147, 148, 149, 150, 151, 152, 177, 178, 179, 180, 184, 210, 213, 214, 215, 216, 227, 228)
									proc999_5(rLab._send('labCoords:'), 1, 2, 6, 19, 20, 21, 38, 65, 66, 67, 68, 81, 82, 85, 86, 112, 113, 114, 115, 116, 145, 146, 147, 148, 149, 150, 151, 176, 177, 178, 179, 183, 209, 212, 213, 214, 215, 226, 227)
								):
								if 2:
									global0._send('setScript:', bats, 0, 4)
								else:
									global0._send('setScript:', bats, 0, 2)
								#endif
							#end:case
						)
					#end:case
					case 4:
						(cond
							case 
								proc999_5(rLab._send('labCoords:'), 2, 3, 7, 20, 21, 22, 39, 66, 67, 68, 69, 82, 83, 86, 87, 113, 114, 115, 116, 117, 146, 147, 148, 149, 150, 151, 152, 177, 178, 179, 180, 184, 210, 213, 214, 215, 216, 227, 228):
								global0._send('setScript:', bats, 0, 4)
							#end:case
							case 
								(and
									proc999_5(rLab._send('labCoords:'), 19, 22, 35, 38, 51, 67, 85, 87, 97, 99, 101, 103, 113, 115, 117, 146, 149, 161, 163, 165, 168, 177, 179, 184, 193, 197, 200, 209, 213, 216, 226, 228, 230, 243)
									proc999_5(rLab._send('labCoords:'), 3, 6, 19, 22, 35, 51, 69, 71, 81, 83, 85, 87, 97, 99, 101, 117, 130, 133, 145, 147, 149, 152, 161, 163, 168, 177, 184, 193, 197, 200, 210, 212, 214, 227)
								):
								if 0:
									global0._send('setScript:', bats, 0, 1)
								else:
									global0._send('setScript:', bats, 0, 3)
								#endif
							#end:case
						)
					#end:case
					case 2:
						(cond
							case 
								proc999_5(rLab._send('labCoords:'), 1, 2, 6, 19, 20, 21, 38, 65, 66, 67, 68, 81, 82, 85, 86, 112, 113, 114, 115, 116, 145, 146, 147, 148, 149, 150, 151, 176, 177, 178, 179, 183, 209, 212, 213, 214, 215, 226, 227):
								global0._send('setScript:', bats, 0, 2)
							#end:case
							case 
								(and
									proc999_5(rLab._send('labCoords:'), 19, 22, 35, 38, 51, 67, 85, 87, 97, 99, 101, 103, 113, 115, 117, 146, 149, 161, 163, 165, 168, 177, 179, 184, 193, 197, 200, 209, 213, 216, 226, 228, 230, 243)
									proc999_5(rLab._send('labCoords:'), 3, 6, 19, 22, 35, 51, 69, 71, 81, 83, 85, 87, 97, 99, 101, 117, 130, 133, 145, 147, 149, 152, 161, 163, 168, 177, 184, 193, 197, 200, 210, 212, 214, 227)
								):
								if 0:
									global0._send('setScript:', bats, 0, 1)
								else:
									global0._send('setScript:', bats, 0, 3)
								#endif
							#end:case
						)
					#end:case
				#end:match
			#endif
		#endif
	#end:method

	@classmethod
	def init():
		if proc913_0(48):
			self._send('style:', 10)
		else:
			self._send('style:', -32761)
		#endif
		super._send('init:')
		if (rLab._send('holeCoords:') == global11):
			proc404_1()
		#endif
		if ((global12 == 435) and (not rLab._send('darkRoomLit:'))):
			0
		else:
			theTorch._send('init:')
		#endif
		if (global11 != 400):
			self._send('makeCritters:')
		#endif
	#end:method

	@classmethod
	def doit():
		(cond
			case global2._send('script:'):#end:case
			case (global0._send('onControl:', 1) == 8192):
				rLab._send('prevEdgeHit:', 4)
				global0._send('setScript:', 0)
				global2._send('setScript:', kernel.ScriptID(30, 2))
			#end:case
			case 
				(or
					(global0._send('onControl:', 1) == 16384)
					(global0._send('onControl:', 1) == 4096)
				):
				rLab._send('prevEdgeHit:', 2)
				global0._send('setScript:', 0)
				global2._send('setScript:', kernel.ScriptID(30, 2))
			#end:case
			case (global0._send('edgeHit:') == 3):
				rLab._send('prevEdgeHit:', 3)
				global0._send('setScript:', 0)
				global2._send('setScript:', kernel.ScriptID(30, 2))
			#end:case
			case (global0._send('edgeHit:') == 1):
				rLab._send('prevEdgeHit:', 1)
				global0._send('setScript:', 0)
				global2._send('setScript:', kernel.ScriptID(30, 2))
			#end:case
		)
		super._send('doit:')
	#end:method

#end:class or instance

@SCI.instance
class theTorch(Prop):
	#property vars (may be empty)
	noun = 9
	modNum = 400
	sightAngle = 45
	view = 400
	priority = 1
	signal = 20497
	detailLevel = 3
	
	@classmethod
	def show():
		if (mod rLab._send('labCoords:') 2):
			self._send('view:', 400, 'x:', 228, 'y:', 141, 'z:', 81, 'setLoop:', 8, 'cel:', 1, 'stopUpd:')
			theFlame._send(
				'x:', (x + 4),
				'y:', y,
				'z:', 106,
				'setLoop:', 3,
				'show:',
				'setCycle:', Fwd,
				'checkDetail:'
			)
			if (global11 != 406):
				torchCycler._send(
					'x:', 233,
					'y:', 48,
					'loop:', 7,
					'show:',
					'setCycle:', RandCycle,
					'checkDetail:'
				)
			#endif
		else:
			self._send('view:', 400, 'x:', 77, 'y:', 141, 'z:', 71, 'setLoop:', 8, 'cel:', 0, 'stopUpd:')
			theFlame._send(
				'x:', 84,
				'y:', 141,
				'z:', (61 if (global11 == 406) else 95),
				'setLoop:', 2,
				'show:',
				'setCycle:', Fwd,
				'checkDetail:'
			)
			if (global11 != 406):
				torchCycler._send(
					'x:', 82,
					'y:', 50,
					'loop:', 6,
					'show:',
					'setCycle:', RandCycle,
					'checkDetail:'
				)
			#endif
		#endif
		super._send('show:')
	#end:method

	@classmethod
	def init():
		if (mod rLab._send('labCoords:') 2):
			self._send('view:', 400, 'x:', 228, 'y:', 141, 'z:', 81, 'setLoop:', 8, 'cel:', 1, 'stopUpd:')
			theFlame._send(
				'x:', 232,
				'y:', 141,
				'z:', 106,
				'setLoop:', 3,
				'init:',
				'setCycle:', Fwd,
				'checkDetail:'
			)
			if (global11 != 410):
				torchCycler._send(
					'x:', 233,
					'y:', 48,
					'setLoop:', 7,
					'init:',
					'setCycle:', RandCycle,
					'checkDetail:'
				)
			#endif
		else:
			self._send(
				'view:', 400,
				'x:', 77,
				'y:', 141,
				'z:', match global11
						case 406: 37#end:case
						case 410: 82#end:case
						else: 71#end:else
					#end:match,
				'setLoop:', 8,
				'cel:', 0,
				'stopUpd:'
			)
			theFlame._send(
				'x:', 84,
				'y:', 141,
				'z:', match global11
						case 406: 61#end:case
						case 410: 106#end:case
						else: 95#end:else
					#end:match,
				'setLoop:', 2,
				'init:',
				'setCycle:', Fwd,
				'checkDetail:'
			)
			torchCycler._send(
				'view:', (400 if (global11 != 410) else 410),
				'x:', match global11
						case 406: 77#end:case
						case 410: 85#end:case
						else: 82#end:else
					#end:match,
				'y:', match global11
						case 406: 98#end:case
						case 410: 30#end:case
						else: 50#end:else
					#end:match,
				'setLoop:', (9 if (global11 == 406) else 6),
				'init:',
				'setCycle:', RandCycle,
				'checkDetail:'
			)
		#endif
		super._send('init:')
	#end:method

#end:class or instance

@SCI.instance
class rat(Actor):
	#property vars (may be empty)
	noun = 20
	view = 410
	signal = 24576
	
#end:class or instance

@SCI.instance
class bat(Actor):
	#property vars (may be empty)
	noun = 21
	yStep = 10
	view = 415
	priority = 15
	signal = 24592
	xStep = 15
	
#end:class or instance

@SCI.instance
class theFlame(Prop):
	#property vars (may be empty)
	noun = 9
	modNum = 400
	sightAngle = 45
	view = 400
	priority = 1
	signal = 20496
	detailLevel = 3
	
#end:class or instance

@SCI.instance
class torchCycler(Prop):
	#property vars (may be empty)
	modNum = 400
	onMeCheck = 0
	view = 400
	signal = 16401
	cycleSpeed = 9
	detailLevel = 3
	
#end:class or instance

@SCI.instance
class corpseNiche(View):
	#property vars (may be empty)
	z = 30
	noun = 8
	modNum = 400
	sightAngle = 45
	view = 400
	loop = 1
	signal = 20496
	
	@classmethod
	def doVerb(param1 = None, *rest):
		if (param1 == 5):
			global2._send('setScript:', checkBody, 0, self)
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

	@classmethod
	def init():
		match rLab._send('corpseWall:')
			case 1:
				self._send('cel:', 2, 'x:', 135, 'y:', 139, 'stopUpd:')
			#end:case
			case 4:
				self._send('cel:', 0, 'x:', 62, 'y:', 147, 'setPri:', 10, 'stopUpd:')
			#end:case
			case 2:
				self._send('cel:', 1, 'x:', 258, 'y:', 150, 'setPri:', 10, 'stopUpd:')
			#end:case
		#end:match
		super._send('init:')
	#end:method

#end:class or instance

@SCI.instance
class leftDoor(View):
	#property vars (may be empty)
	x = 63
	y = 155
	noun = 4
	modNum = 400
	sightAngle = 45
	view = 405
	cel = 1
	priority = 11
	signal = 28688
	
#end:class or instance

@SCI.instance
class leftWing(View):
	#property vars (may be empty)
	x = 43
	y = 168
	noun = 4
	modNum = 400
	sightAngle = 45
	view = 405
	priority = 13
	signal = 28688
	
#end:class or instance

@SCI.instance
class rightDoor(View):
	#property vars (may be empty)
	x = 246
	y = 155
	noun = 4
	modNum = 400
	sightAngle = 45
	view = 407
	priority = 11
	signal = 28688
	
#end:class or instance

@SCI.instance
class rightWing(View):
	#property vars (may be empty)
	x = 263
	y = 169
	noun = 4
	modNum = 400
	sightAngle = 45
	view = 407
	cel = 1
	priority = 13
	signal = 28688
	
#end:class or instance

@SCI.instance
class topDoor(View):
	#property vars (may be empty)
	x = 157
	y = 144
	noun = 4
	modNum = 400
	sightAngle = 45
	view = 406
	priority = 8
	signal = 28688
	
#end:class or instance

@SCI.instance
class bottomBlock(View):
	#property vars (may be empty)
	x = 149
	y = 189
	noun = 6
	modNum = 400
	sightAngle = 45
	view = 408
	priority = 15
	signal = 20496
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 25:
				global91._send('say:', 6, 25, 9, 0, 0, 400)
			#end:case
			case 1:
				global91._send('say:', 6, 1, 9, 0, 0, 400)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class floor(Feature):
	#property vars (may be empty)
	noun = 5
	modNum = 400
	sightAngle = 45
	onMeCheck = 2048
	
#end:class or instance

@SCI.instance
class eastWall(Feature):
	#property vars (may be empty)
	x = 255
	y = 140
	noun = 6
	modNum = 400
	sightAngle = 45
	onMeCheck = 17408
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				global91._send('say:', 6, 1, 8, 0, 0, 400)
			#end:case
			case 25:
				if 
					(not
						proc999_5(rLab._send('labCoords:'), 1, 2, 6, 19, 20, 21, 38, 65, 66, 67, 68, 81, 82, 85, 86, 112, 113, 114, 115, 116, 145, 146, 147, 148, 149, 150, 151, 176, 177, 178, 179, 183, 209, 212, 213, 214, 215, 226, 227)
					)
					proc404_0(2)
				else:
					global91._send('say:', 6, 25, 5, 0, 0, 400)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class northWall(Feature):
	#property vars (may be empty)
	x = 160
	y = 120
	noun = 6
	modNum = 400
	sightAngle = 45
	onMeCheck = 4608
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				global91._send('say:', 6, 1, 6, 0, 0, 400)
			#end:case
			case 25:
				if 
					(not
						proc999_5(rLab._send('labCoords:'), 19, 22, 35, 38, 51, 67, 85, 87, 97, 99, 101, 103, 113, 115, 117, 146, 149, 161, 163, 165, 168, 177, 179, 184, 193, 197, 200, 209, 213, 216, 226, 228, 230, 243)
					)
					proc404_0(1)
				else:
					global91._send('say:', 6, 25, 5, 0, 0, 400)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class westWall(Feature):
	#property vars (may be empty)
	x = 60
	y = 140
	noun = 6
	modNum = 400
	sightAngle = 45
	onMeCheck = 8448
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				global91._send('say:', 6, 1, 7, 0, 0, 400)
			#end:case
			case 25:
				if 
					(not
						proc999_5(rLab._send('labCoords:'), 2, 3, 7, 20, 21, 22, 39, 66, 67, 68, 69, 82, 83, 86, 87, 113, 114, 115, 116, 117, 146, 147, 148, 149, 150, 151, 152, 177, 178, 179, 180, 184, 210, 213, 214, 215, 216, 227, 228)
					)
					proc404_0(4)
				else:
					global91._send('say:', 6, 25, 5, 0, 0, 400)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class minotaurTimer(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				seconds = 25
			#end:case
			case 1:
				if ((global11 == 400) and (not global2._send('script:'))):
					global105._send('number:', 401, 'setLoop:', 5, 'play:')
					seconds = 3
				else:
					self._send('cue:')
				#endif
			#end:case
			case 2:
				if 
					(and
						(global11 == 400)
						(not global2._send('script:'))
						(not global0._send('script:'))
					)
					if (rLab._send('msgNum:') == 3):
						rLab._send('msgNum:', 1)
					else:
						rLab._send('msgNum:', (rLab._send('msgNum:') + 1))
					#endif
					global91._send('say:', 1, 0, 1, rLab._send('msgNum:'), self, 400)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 3:
				self._send('changeState:', 0)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class checkBody(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				(cond
					case (register._send('x:') < 90):
						global0._send('setMotion:', PolyPath, 68, 160, self)
					#end:case
					case (register._send('x:') < 230):
						global0._send('setMotion:', PolyPath, 147, 149, self)
					#end:case
					else:
						global0._send('setMotion:', PolyPath, 251, 156, self)
					#end:else
				)
			#end:case
			case 1:
				(cond
					case (register._send('x:') < 90):
						global0._send('posn:', 58, 164, 'setLoop:', 2)
					#end:case
					case (register._send('x:') < 230):
						global0._send('posn:', 148, 150, 'setLoop:', 4)
					#end:case
					else:
						global0._send('posn:', 250, 163, 'setLoop:', 3)
					#end:else
				)
				global0._send(
					'view:', 431,
					'normal:', 0,
					'cel:', 0,
					'cycleSpeed:', 10,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				(cond
					case (register._send('x:') < 90):
						global0._send('posn:', 56, 164, 'setLoop:', 0)
					#end:case
					case (register._send('x:') < 230):
						global0._send('posn:', 149, 151, 'setLoop:', 5)
					#end:case
					else:
						global0._send('posn:', 252, 164, 'setLoop:', 1)
					#end:else
				)
				global0._send('cycleSpeed:', 18, 'setCycle:', End, self)
			#end:case
			case 3:
				(cond
					case (register._send('x:') < 90):
						global0._send('posn:', 68, 160, 'reset:', 1)
					#end:case
					case (register._send('x:') < 230):
						global0._send('posn:', 147, 149, 'reset:', 3)
					#end:case
					else:
						global0._send('posn:', 246, 161, 'reset:', 0)
					#end:else
				)
				cycles = 6
			#end:case
			case 4:
				global91._send('say:', 8, 5, 0, 1, self, 400)
			#end:case
			case 5:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walkIn(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if (global11 == 400):
					if proc913_0(48):
						global2._send('drawPic:', 400, 10)
					else:
						global2._send('drawPic:', 400, -32761)
					#endif
				#endif
				match rLab._send('prevEdgeHit:')
					case 4:
						global0._send(
							'posn:', 282, 158,
							'init:',
							'ignoreHorizon:',
							'setMotion:', PolyPath, 237, 158, self
						)
					#end:case
					case 2:
						global0._send(
							'posn:', 36, 158,
							'init:',
							'ignoreHorizon:',
							'setMotion:', PolyPath, 84, 158, self
						)
					#end:case
					case 1:
						global0._send(
							'posn:', 165, 250,
							'init:',
							'ignoreHorizon:',
							'setMotion:', PolyPath, 165, 184, self
						)
					#end:case
					case 3:
						global0._send(
							'posn:', 165, 136,
							'init:',
							'ignoreHorizon:',
							'setMotion:', PolyPath, 165, 145, self
						)
					#end:case
					else:
						global0._send('posn:', 160, 160, 'loop:', 2, 'init:', 'ignoreHorizon:')
						ticks = 6
					#end:else
				#end:match
			#end:case
			case 1:
				if (not rLab._send('geniePresent:')):
					global1._send('handsOn:')
				#endif
				self._send('dispose:')
				global69._send('enable:', 6)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walkOut(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global69._send('disable:', 6)
				match rLab._send('prevEdgeHit:')
					case 1:
						cycles = 8
					#end:case
					case 3:
						global0._send('setMotion:', MoveTo, global0._send('x:'), 250, self)
					#end:case
					case 2:
						global0._send('setMotion:', MoveTo, 310, global0._send('y:'), self)
					#end:case
					case 4:
						global0._send('setMotion:', MoveTo, 10, global0._send('y:'), self)
					#end:case
				#end:match
			#end:case
			case 1:
				match rLab._send('prevEdgeHit:')
					case 1:
						global2._send('newRoom:', global2._send('north:'))
					#end:case
					case 3:
						global2._send('newRoom:', global2._send('south:'))
					#end:case
					case 2:
						global2._send('newRoom:', global2._send('east:'))
					#end:case
					case 4:
						global2._send('newRoom:', global2._send('west:'))
					#end:case
				#end:match
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class bats(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				match register
					case 1:
						temp0 = 3
						temp1 = 206
						temp2 = 185
						temp3 = 195
						temp4 = 164
					#end:case
					case 3:
						temp0 = 2
						temp1 = 159
						temp2 = 85
						temp3 = 248
						temp4 = 195
					#end:case
					case 4:
						temp0 = 1
						temp1 = 246
						temp2 = 74
						temp3 = 184
						temp4 = 76
					#end:case
					case 2:
						temp0 = 0
						temp1 = 63
						temp2 = 87
						temp3 = 132
						temp4 = 82
					#end:case
				#end:match
				bat._send(
					'posn:', temp1, temp2,
					'setLoop:', temp0,
					'init:',
					'setStep:', 15, 12,
					'setCycle:', Walk,
					'setMotion:', MoveTo, temp3, temp4, self
				)
			#end:case
			case 1:
				match register
					case 1:
						temp0 = 6
						temp1 = 190
						temp2 = 157
					#end:case
					case 4:
						temp0 = 5
						temp1 = 170
						temp2 = 70
					#end:case
					case 2:
						temp0 = 4
						temp1 = 144
						temp2 = 78
					#end:case
				#end:match
				if (register == 3):
					(state += 2)
					self._send('cue:')
				else:
					bat._send('setLoop:', temp0, 'posn:', temp1, temp2, 'setCycle:', End, self)
				#endif
			#end:case
			case 2:
				if (register == 1):
					bat._send('setLoop:', 5, 'cel:', 7, 'posn:', 179, 149)
					cycles = 4
				else:
					self._send('cue:')
				#endif
			#end:case
			case 3:
				match register
					case 1:
						temp0 = 3
						temp1 = 169
						temp2 = 142
						temp3 = 159
						temp4 = 88
					#end:case
					case 4:
						temp0 = 1
						temp1 = 155
						temp2 = 68
						temp3 = 62
						temp4 = 74
					#end:case
					case 2:
						temp0 = 0
						temp1 = 160
						temp2 = 77
						temp3 = 248
						temp4 = 78
					#end:case
				#end:match
				bat._send(
					'posn:', temp1, temp2,
					'setLoop:', temp0,
					'setCycle:', Walk,
					'setMotion:', MoveTo, temp3, temp4, self
				)
			#end:case
			case 4:
				bat._send('dispose:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class rats(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				match register
					case 1:
						temp0 = 2
						temp1 = 11
						temp2 = 127
						temp3 = 124
						temp4 = 121
						temp5 = 146
					#end:case
					case 2:
						temp0 = 2
						temp1 = 11
						temp2 = 192
						temp3 = 123
						temp4 = 195
						temp5 = 149
					#end:case
					case 3:
						temp0 = 4
						temp2 = 72
						temp3 = 125
						temp4 = 85
						temp5 = 149
					#end:case
					case 4:
						temp0 = 4
						temp2 = 58
						temp3 = 132
						temp4 = 64
						temp5 = 169
					#end:case
					case 5:
						temp0 = 5
						temp2 = 258
						temp3 = 131
						temp4 = 241
						temp5 = 155
					#end:case
					case 6:
						temp0 = 5
						temp2 = 258
						temp3 = 131
						temp4 = 241
						temp5 = 155
					#end:case
				#end:match
				rat._send(
					'posn:', temp2, temp3,
					'setLoop:', temp0,
					'cel:', 0,
					'init:',
					'setStep:', 15, 11,
					'setCycle:', 0,
					'setMotion:', MoveTo, temp4, temp5, self
				)
			#end:case
			case 1:
				match register
					case 1:
						temp0 = 2
						temp2 = 121
						temp3 = 146
						temp4 = 109
						temp5 = 158
					#end:case
					case 2:
						temp0 = 2
						temp2 = 195
						temp3 = 149
						temp4 = 206
						temp5 = 161
					#end:case
					case 3:
						temp0 = 0
						temp2 = 88
						temp3 = 149
						temp4 = 132
						temp5 = 149
					#end:case
					case 4:
						temp0 = 2
						temp2 = 64
						temp3 = 174
						temp4 = 65
						temp5 = 200
					#end:case
					case 5:
						temp0 = 1
						temp2 = 240
						temp3 = 155
						temp4 = 194
						temp5 = 152
					#end:case
					case 6:
						temp0 = 2
						temp2 = 233
						temp3 = 159
						temp4 = 232
						temp5 = 200
					#end:case
				#end:match
				rat._send(
					'setLoop:', temp0,
					'posn:', temp2, temp3,
					'setStep:', 8, 5,
					'setCycle:', Walk,
					'setMotion:', MoveTo, temp4, temp5, self
				)
			#end:case
			case 2:
				match register
					case 1:
						temp0 = 1
						temp2 = 106
						temp3 = 157
						temp4 = 36
						temp5 = 157
					#end:case
					case 2:
						temp0 = 0
						temp2 = 212
						temp3 = 160
						temp4 = 275
						temp5 = 160
					#end:case
					case 3:
						temp0 = 3
						temp2 = 138
						temp3 = 146
						temp4 = 135
						temp5 = 138
					#end:case
					case 4:
						rat._send('dispose:')
						self._send('dispose:')
					#end:case
					case 5:
						temp0 = 3
						temp2 = 186
						temp3 = 152
						temp4 = 179
						temp5 = 135
					#end:case
					case 6:
						rat._send('dispose:')
						self._send('dispose:')
					#end:case
				#end:match
				rat._send(
					'setLoop:', temp0,
					'posn:', temp2, temp3,
					'setCycle:', Walk,
					'setMotion:', MoveTo, temp4, temp5, self
				)
			#end:case
			case 3:
				rat._send('dispose:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

