#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 720
import sci_sh
import kernel
import Main
import rgCastle
import n913
import Scaler
import PolyPath
import Polygon
import Feature
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm720 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.instance
class rm720(CastleRoom):
	#property vars (may be empty)
	noun = 7
	picture = 720
	style = 10
	east = 840
	west = 710
	vanishingY = -400
	minScaleSize = 75
	minScaleY = 143
	maxScaleY = 189
	
	@classmethod
	def init():
		self._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 0, -10, 319, -10, 319, 139, 296, 139, 290, 142, 214, 142, 209, 139, 89, 139, 86, 142, 39, 142, 27, 147, 0, 147,
					'yourself:'
				)
		)
		global32._send(
			'add:', statue, ceiling, theWindows, floorOrCeiling,
			'eachElementDo:', #init
		)
		kernel.ScriptID(80, 5)._send('noun:', 5)
		kernel.ScriptID(80, 6)._send('noun:', 5)
		kernel.ScriptID(81, 0)._send(
			'guard1Code:', path1Code,
			'guard2Code:', path1Code,
			'setupGuards:'
		)
		if kernel.ScriptID(81, 0)._send('tstFlag:', 709, 4):
			kernel.ScriptID(80, 0)._send('weddingRemind:', 0)
			kernel.ScriptID(80, 5)._send(
				'setMotion:', 0,
				'posn:', 131, 154, 0,
				'loop:', 3,
				'okToCheck:', 1,
				'init:',
				'setScale:', Scaler, maxScaleSize, minScaleSize, maxScaleY, minScaleY
			)
			kernel.ScriptID(80, 6)._send(
				'setMotion:', 0,
				'posn:', 140, 146, 0,
				'loop:', 2,
				'okToCheck:', 1,
				'init:',
				'setScale:', Scaler, maxScaleSize, minScaleSize, maxScaleY, minScaleY
			)
			moveOtherGuard = 1
		#endif
		guardDoor._send('init:', 'stopUpd:')
		super._send('init:', &rest)
		hiddenDoor._send('init:')
		arm._send('init:')
		spotEgoScr = captureEgo
		local1 = 1
		global0._send(
			'init:',
			'setScale:', Scaler, maxScaleSize, minScaleSize, maxScaleY, minScaleY
		)
		match global12
			case 800:
				local1 = 0
				arm._send('startUpd:', 'cel:', 1, 'stopUpd:')
				hiddenDoor._send('startUpd:', 'cel:', 7, 'stopUpd:')
				global0._send('posn:', 48, 144)
				self._send('setScript:', closeDoor)
				if kernel.ScriptID(80, 0)._send('tstFlag:', 710, 256):
					kernel.ScriptID(80, 0)._send('setFlag:', 711, 512)
					kernel.ScriptID(80, 0)._send('weddingRemind:', 121)
				#endif
			#end:case
			case 840:
				global0._send('posn:', 305, 168)
			#end:case
			else:
				global0._send('posn:', 13, 167)
			#end:else
		#end:match
		if 
			(and
				global5._send('contains:', kernel.ScriptID(80, 6))
				kernel.IsObject(kernel.ScriptID(80, 6)._send('regPathID:'))
				kernel.ScriptID(80, 6)._send('mover:')
				(kernel.ScriptID(80, 6)._send('regPathID:')._send('value:') < 6)
			)
			guardDoor._send('cel:', 4)
			kernel.ScriptID(80, 6)._send('posn:', 108, 142)
			kernel.ScriptID(80, 6)._send('regPathID:')._send('value:', 6, 'moveDone:')
		#endif
		global0._send('scaler:')._send('doit:')
		if 
			(and
				local1
				(not kernel.ScriptID(81, 0)._send('tstFlag:', 709, 4))
				(not kernel.ScriptID(81, 0)._send('tstFlag:', 709, 1))
				(not kernel.ScriptID(81, 0)._send('tstFlag:', 709, 2))
				(not kernel.Random(0, 5))
			)
			kernel.ScriptID(81, 0)._send('setFlag:', 709, 1, 'loiterTimer:', 1)
		#endif
		if (not script):
			global1._send('handsOn:')
		#endif
	#end:method

	@classmethod
	def warnUser(param1 = None, param2 = None, *rest):
		match param1
			case 5:
				if temp0 = self._send('roomToEdge:', param2[0]):
					match temp0
						case 2:
							global91._send('say:', 10, 0, 17)
						#end:case
					#end:match
				#endif
			#end:case
			case 6:
				if (not kernel.ScriptID(81, 0)._send('tstFlag:', 709, 4)):
					if (param2 == 7):
						global91._send('say:', 10, 0, 22)
					else:
						global91._send('say:', 10, 0, 24)
					#endif
				#endif
			#end:case
			case 1:
				(cond
					case (kernel.ScriptID(80, 0)._send('weddingMusicCount:') >= 3):
						if (kernel.ScriptID(80, 0)._send('weddingMusicCount:') >= 4):
							global1._send('handsOff:')
							kernel.ScriptID(81, 0)._send('setFlag:', 709, 2)
						else:
							temp1 = 33
							kernel.ScriptID(80, 0)._send('weddingRemind:', 15)
						#endif
					#end:case
					case (not kernel.ScriptID(80, 0)._send('weddingMusicCount:')):
						temp1 = 28
					#end:case
					else:
						temp1 = 29
					#end:else
				)
				kernel.ScriptID(81, 0)._send('warnUser:', param1, 10, 0, temp1)
			#end:case
			case 4:
				if (not kernel.ScriptID(81, 0)._send('tstFlag:', 709, 4)):
					kernel.ScriptID(81, 0)._send('clrFlag:', 709, 2)
					kernel.ScriptID(80, 6)._send('dispose:')
					global91._send('say:', 10, 0, 23)
				#endif
			#end:case
			else:
				super._send('warnUser:', param1, param2, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		if 
			(and
				(param1 == 840)
				(kernel.ScriptID(80, 0)._send('weddingMusicCount:') >= 3)
				(not kernel.ScriptID(81, 0)._send('tstFlag:', 709, 2))
			)
			kernel.ScriptID(81, 0)._send('setFlag:', 709, 2)
			kernel.ScriptID(80, 0)._send(
				'weddingRemind:', (kernel.ScriptID(80, 0)._send('weddingRemind:') + 9)
			)
		#endif
		super._send('newRoom:', param1)
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(964)
	#end:method

	@classmethod
	def scriptCheck(param1 = None, *rest):
		(cond
			case proc999_5(param1, 87, 908):
				if 
					(or
						kernel.ScriptID(81, 0)._send('tstFlag:', 709, 1)
						kernel.ScriptID(81, 0)._send('tstFlag:', 709, 2)
						kernel.ScriptID(81, 0)._send('tstFlag:', 709, 4)
					)
					global91._send('say:', 1, 14, 1, 0, 0, 899)
					return 0
				else:
					return super._send('scriptCheck:', param1, &rest)
				#endif
			#end:case
			case 
				(or
					kernel.ScriptID(81, 0)._send('tstFlag:', 709, 1)
					kernel.ScriptID(81, 0)._send('tstFlag:', 709, 2)
				):
				global91._send('say:', 0, 0, 6, 0, 0, 899)
				return 0
			#end:case
			else:
				return super._send('scriptCheck:', param1, &rest)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class enterGuardDoor(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				kernel.ScriptID(81, 0)._send('resetGuard:', kernel.ScriptID(80, 5), 1)
				kernel.ScriptID(81, 0)._send('resetGuard:', kernel.ScriptID(80, 6), 2)
				global91._send('say:', 4, 5, 4, 1, self)
			#end:case
			case 1:
				global0._send('setHeading:', 0, self)
			#end:case
			case 2:
				global105._send('number:', 901, 'loop:', 1, 'play:')
				guardDoor._send('setCycle:', End, self)
			#end:case
			case 3:
				global105._send('stop:')
				global91._send('say:', 4, 5, 4, 2, self)
			#end:case
			case 4:
				global0._send('setSpeed:', 5, 'setMotion:', MoveTo, 37, 158)
				ticks = 90
			#end:case
			case 5:
				kernel.ScriptID(80, 5)._send(
					'init:',
					'setScale:', Scaler, global2._send('maxScaleSize:'), global2._send(
							'minScaleSize:'
						), global2._send('maxScaleY:'), global2._send('minScaleY:'),
					'posn:', 130, 135, 0,
					'illegalBits:', 0,
					'setSpeed:', 5,
					'setMotion:', MoveTo, 109, 135, self
				)
			#end:case
			case 6:
				kernel.ScriptID(80, 5)._send('setMotion:', MoveTo, 107, 140, self)
			#end:case
			case 7:
				global91._send('say:', 4, 5, 4, 3, self)
			#end:case
			case 8:
				global1._send('handsOff:')
				proc913_4(global0, kernel.ScriptID(80, 5), self)
			#end:case
			case 9:
				cycles = 4
			#end:case
			case 10:
				kernel.ScriptID(80, 5)._send('setScript:', kernel.ScriptID(80, 4))
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class captureEgo(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				if 
					(and
						global5._send('contains:', kernel.ScriptID(80, 5))
						global5._send('contains:', kernel.ScriptID(80, 6))
						kernel.IsObject(kernel.ScriptID(80, 5)._send('regPathID:'))
						(==
							kernel.ScriptID(80, 5)._send('regPathID:')._send('currentRoom:')
							global11
						)
						kernel.IsObject(kernel.ScriptID(80, 6)._send('regPathID:'))
						(==
							kernel.ScriptID(80, 6)._send('regPathID:')._send('currentRoom:')
							global11
						)
					)
					global2._send('moveOtherGuard:', 1)
				#endif
				ticks = 2
			#end:case
			case 1:
				global91._send('say:', 10, 0, 16, 1, self)
			#end:case
			case 2:
				proc913_4(register, global0, self)
			#end:case
			case 3:
				global91._send('say:', 10, 0, 16, 2, self)
			#end:case
			case 4:
				register._send('setScript:', kernel.ScriptID(80, 4), self, 1)
			#end:case
			case 5:
				global91._send('say:', 10, 0, 16, 3, self)
			#end:case
			case 6:
				global91._send('say:', 10, 0, 16, 4, self)
			#end:case
			case 7:
				global5._send('eachElementDo:', #hide)
				global2._send('drawPic:', 98)
				cycles = 4
			#end:case
			case 8:
				global91._send('say:', 10, 0, 16, 5, self)
			#end:case
			case 9:
				global2._send('newRoom:', 820)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class statue(Feature):
	#property vars (may be empty)
	x = 23
	y = 144
	z = 30
	noun = 11
	sightAngle = 45
	onMeCheck = 2
	approachX = 9
	approachY = 147
	
	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('approachVerbs:', 5)
	#end:method

#end:class or instance

@SCI.instance
class arm(View):
	#property vars (may be empty)
	x = 18
	y = 101
	noun = 8
	approachX = 8
	approachY = 147
	view = 720
	loop = 2
	signal = 16385
	
	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('approachVerbs:', 5)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		if (global66._send('doit:', param1) == -32768):
			global91._send('say:', 11)
		else:
			match param1
				case 2:
					global91._send('say:', 11, param1)
				#end:case
				case 5:
					(cond
						case (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, -32768)):
							global91._send('say:', noun, param1, 9)
						#end:case
						case kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2):
							global91._send('say:', noun, param1, 7)
						#end:case
						else:
							global2._send('setScript:', openSecretDoor)
						#end:else
					)
				#end:case
				else:
					super._send('doVerb:', param1, &rest)
				#end:else
			#end:match
		#endif
	#end:method

#end:class or instance

@SCI.instance
class closeDoor(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cycles = 2
			#end:case
			case 1:
				global105._send('number:', 909, 'loop:', 1, 'play:')
				hiddenDoor._send('setCycle:', Beg, self)
			#end:case
			case 2:
				global105._send('stop:')
				arm._send('cel:', 0, 'forceUpd:')
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class openSecretDoor(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				kernel.ScriptID(80, 5)._send('okToCheck:', 0, 'setMotion:', 0)
				kernel.ScriptID(80, 6)._send('okToCheck:', 0, 'setMotion:', 0)
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 711, 2)):
					global1._send('givePoints:', 2)
					global91._send('say:', 8, 5, 5, 1, self)
				else:
					global91._send('say:', 8, 5, 6, 0, self)
				#endif
			#end:case
			case 1:
				global0._send(
					'normal:', 0,
					'view:', 722,
					'loop:', 0,
					'cel:', 0,
					'posn:', 5, 146,
					'cycleSpeed:', 8,
					'setScale:',
					'scaleX:', 107,
					'scaleY:', 107,
					'setCycle:', CT, 3, 1, self
				)
				arm._send('startUpd:')
			#end:case
			case 2:
				global105._send('number:', 720, 'loop:', 1, 'play:')
				arm._send('cel:', 1, 'stopUpd:')
				global0._send('setCycle:', Beg, self)
				hiddenDoor._send('startUpd:')
			#end:case
			case 3:
				global105._send('number:', 909, 'loop:', 1, 'play:')
				hiddenDoor._send('setCycle:', End, self)
			#end:case
			case 4:
				global105._send('stop:')
				hiddenDoor._send('stopUpd:')
				global0._send('reset:', 3, 900)
				cycles = 1
			#end:case
			case 5:
				if 
					(or
						(and
							global5._send('contains:', kernel.ScriptID(80, 5))
							(==
								kernel.ScriptID(80, 5)._send('regPathID:')._send('currentRoom:')
								global11
							)
							temp0 = kernel.ScriptID(80, 5)
						)
						(and
							global5._send('contains:', kernel.ScriptID(80, 6))
							(==
								kernel.ScriptID(80, 6)._send('regPathID:')._send('currentRoom:')
								global11
							)
							temp0 = kernel.ScriptID(80, 6)
						)
					)
					global2._send('spotEgo:', temp0)
				else:
					ticks = 1
				#endif
			#end:case
			case 6:
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 711, 2)):
					kernel.ScriptID(80, 0)._send('setFlag:', 711, 2)
					global91._send('say:', 8, 5, 5, 2, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 7:
				global0._send(
					'setSpeed:', 8,
					'setScale:', Scaler, global2._send('maxScaleSize:'), global2._send(
							'minScaleSize:'
						), global2._send('maxScaleY:'), global2._send('minScaleY:'),
					'setMotion:', PolyPath, 51, 141, self
				)
			#end:case
			case 8:
				global0._send('setHeading:', 0, self)
			#end:case
			case 9:
				global0._send(
					'normal:', 0,
					'view:', 722,
					'loop:', 1,
					'cel:', 0,
					'cycleSpeed:', 8,
					'posn:', 51, 143,
					'setScale:',
					'scaleX:', 106,
					'scaleY:', 106,
					'setCycle:', End, self
				)
			#end:case
			case 10:
				global0._send('dispose:')
				cycles = 4
			#end:case
			case 11:
				global2._send('newRoom:', 800)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class hiddenDoor(Prop):
	#property vars (may be empty)
	x = 40
	y = 117
	noun = 9
	view = 720
	loop = 1
	signal = 16385
	
	@classmethod
	def onMe(param1 = None, *rest):
		return (super._send('onMe:', param1) and kernel.ScriptID(80, 0)._send('tstFlag:', 711, 2))
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		if (global66._send('doit:', param1) == -32768):
			param1 = 0
		#endif
		global91._send('say:', noun, param1, 10)
	#end:method

#end:class or instance

@SCI.instance
class guardDoor(Prop):
	#property vars (may be empty)
	x = 99
	y = 117
	noun = 4
	sightAngle = 40
	approachX = 110
	approachY = 139
	view = 720
	cycleSpeed = 0
	
	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('approachVerbs:', 5, 1)
	#end:method

	@classmethod
	def doit():
		temp0 = kernel.ScriptID(80, 5)._send('onControl:', 1)
		temp1 = kernel.ScriptID(80, 6)._send('onControl:', 1)
		super._send('doit:')
		if (not cycler):
			(cond
				case 
					(and
						(not cel)
						(or
							(and
								kernel.ScriptID(81, 0)._send('tstFlag:', 709, 1)
								kernel.IsObject(kernel.ScriptID(80, 5)._send('regPathID:'))
								(==
									kernel.ScriptID(80, 5)._send('regPathID:')._send('currentRoom:')
									global11
								)
								(temp0 & 0x4000)
							)
							(and
								kernel.ScriptID(81, 0)._send('tstFlag:', 709, 2)
								kernel.IsObject(kernel.ScriptID(80, 6)._send('regPathID:'))
								(==
									kernel.ScriptID(80, 6)._send('regPathID:')._send('currentRoom:')
									global11
								)
								(temp1 & 0x4000)
							)
						)
					):
					self._send('cue:', 1, 'setCycle:', End)
				#end:case
				case 
					(and
						cel
						(or
							(and
								kernel.ScriptID(81, 0)._send('tstFlag:', 709, 1)
								kernel.IsObject(kernel.ScriptID(80, 5)._send('regPathID:'))
								(==
									kernel.ScriptID(80, 5)._send('regPathID:')._send('currentRoom:')
									global11
								)
								(not (temp0 & 0x4000))
							)
							(and
								kernel.ScriptID(81, 0)._send('tstFlag:', 709, 2)
								kernel.IsObject(kernel.ScriptID(80, 6)._send('regPathID:'))
								(==
									kernel.ScriptID(80, 6)._send('regPathID:')._send('currentRoom:')
									global11
								)
								(not (temp1 & 0x4000))
							)
						)
					):
					self._send('setCycle:', Beg, self)
				#end:case
				else: 0#end:else
			)
		#endif
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			global105._send('number:', 901, 'loop:', 1, 'play:')
		else:
			global105._send('number:', 902, 'loop:', 1, 'play:')
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				if local0:
					global2._send('setScript:', enterGuardDoor)
				else:
					global91._send('say:', noun, param1, (3 + local0))
				#endif
				local0 = 1
			#end:case
			else:
				super._send('doVerb:', param1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class ceiling(Feature):
	#property vars (may be empty)
	y = 2
	noun = 2
	onMeCheck = 16
	
#end:class or instance

@SCI.instance
class rightArm(Feature):
	#property vars (may be empty)
	y = 144
	noun = 8
	onMeCheck = 8
	approachX = 9
	approachY = 147
	
	@classmethod
	def onMe(param1 = None, *rest):
		x = param1._send('x:')
		return super._send('onMe:', param1)
	#end:method

	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('approachVerbs:', 5)
	#end:method

#end:class or instance

@SCI.instance
class theWindows(Feature):
	#property vars (may be empty)
	y = 75
	noun = 13
	onMeCheck = 4
	
	@classmethod
	def onMe(param1 = None, *rest):
		x = param1._send('x:')
		return super._send('onMe:', param1)
	#end:method

#end:class or instance

@SCI.instance
class floorOrCeiling(Feature):
	#property vars (may be empty)
	nsBottom = 200
	nsRight = 320
	
	@classmethod
	def init():
		super._send('init:', &rest)
		sightAngle = 26505
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		(return
			(or
				((param1._send('y:') <= 137) and noun = 12)
				((param1._send('y:') > 137) and noun = 3)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class path1Code(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		temp0 = 0
		if 
			(or
				(not kernel.IsObject(param1._send('regPathID:')))
				(param1._send('regPathID:')._send('currentRoom:') == global11)
			)
			temp0 = (>= 320 param1._send('x:') 0)
		#endif
		return temp0
	#end:method

#end:class or instance

