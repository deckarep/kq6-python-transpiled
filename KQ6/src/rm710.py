#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 710
import sci_sh
import kernel
import Main
import rgCastle
import n913
import PanelInset
import Scaler
import PolyPath
import Polygon
import Feature
import StopWalk
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm710 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = [1, 12, 9, 28, 5, 2, 21]
local7 = None
local8 = None
local9 = None
local10 = None
local11 = None
local12 = None


@SCI.procedure
def localproc_0(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	local8 = global0._send('y:')
	if (argc >= 1):
		local7 = param1[0]
		if (argc >= 2):
			local8 = param1[1]
		#endif
	#endif
#end:procedure

class DungeonDoor(Prop):
	#property vars (may be empty)
	noun = 4
	sightAngle = 45
	view = 710
	cycleSpeed = 8
	dungeon# = 0
	
	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('approachVerbs:', 5, 35, 2)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				(cond
					case 
						(or
							kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2)
							kernel.ScriptID(81, 0)._send('tstFlag:', 709, 4)
						):
						global91._send('say:', noun, param1, 8, 1)
					#end:case
					case (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2)):
						kernel.ScriptID(80, 0)._send('dungeonEntered:', dungeon#)
						global2._send('setScript:', enterDungeon, 0, self)
					#end:case
				)
			#end:case
			else:
				super._send('doVerb:', param1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class rm710(CastleRoom):
	#property vars (may be empty)
	noun = 8
	picture = 710
	style = 10
	north = 720
	east = 840
	minScaleSize = 37
	minScaleY = 112
	maxScaleY = 173
	
	@classmethod
	def init():
		self._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 0, 0, 319, 0, 319, 176, 243, 176, 192, 141, 198, 141, 177, 128, 171, 128, 152, 115, 177, 115, 177, 111, 102, 111, 75, 129, 70, 129, 48, 143, 54, 143, 0, 179,
					'yourself:'
				)
		)
		global32._send('add:', armour, roomStuff, 'eachElementDo:', #init)
		kernel.ScriptID(80, 6)._send('noun:', 13, 'actions:', guardDoVerb)
		kernel.ScriptID(81, 0)._send('guard2Code:', path2Code, 'setupGuards:')
		spotEgoScr = captureEgo
		super._send('init:', &rest)
		dungeonDoor1._send('init:', 'stopUpd:')
		dungeonDoor2._send('init:', 'stopUpd:')
		dungeonDoor3._send('init:', 'stopUpd:')
		treasureDoor._send('init:', 'stopUpd:')
		temp1 = 0
		global0._send(
			'init:',
			'reset:',
			'setScale:', Scaler, maxScaleSize, minScaleSize, maxScaleY, minScaleY
		)
		match global12
			case 770:
				global0._send('posn:', 65, 134)
				if kernel.ScriptID(81, 0)._send('tstFlag:', 709, 4):
					kernel.ScriptID(81, 0)._send('setFlag:', 709, 2)
					kernel.ScriptID(81, 0)._send('startGuard:')
				#endif
			#end:case
			case 720:
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 711, 512)):
					temp1 = 1
				#endif
				global0._send('posn:', 148, 114)
			#end:case
			case 820:
				kernel.ScriptID(80, 0)._send('clrFlag:', 709, 8192)
				match kernel.ScriptID(80, 0)._send('dungeonEntered:')
					case 1:
						global0._send(
							'posn:', dungeonDoor1._send('approachX:'), dungeonDoor1._send(
									'approachY:'
								)
						)
					#end:case
					case 2:
						global0._send(
							'posn:', dungeonDoor2._send('approachX:'), dungeonDoor2._send(
									'approachY:'
								)
						)
					#end:case
					case 3:
						global0._send(
							'posn:', dungeonDoor3._send('approachX:'), dungeonDoor3._send(
									'approachY:'
								)
						)
						(cond
							case kernel.ScriptID(80, 0)._send('tstFlag:', 709, 1):
								kernel.ScriptID(80, 0)._send('clrFlag:', 709, 1)
								jollo._send(
									'view:', 717,
									'loop:', 4,
									'cel:', 2,
									'posn:', 170, 154,
									'setScale:', Scaler, global2._send('maxScaleSize:'), global2._send(
											'minScaleSize:'
										), global2._send('maxScaleY:'), global2._send(
											'minScaleY:'
										),
									'init:',
									'ignoreActors:', 1,
									'setCycle:', StopWalk, -1
								)
								self._send('setScript:', jolloHelpedEgo)
							#end:case
							case kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2):
								global102._send('fadeTo:', 701, -1)
								kernel.ScriptID(81, 0)._send('setFlag:', 709, 2)
								self._send('setScript:', tempScript)
							#end:case
						)
					#end:case
				#end:match
			#end:case
			case 840:
				temp1 = 1
				global0._send('posn:', 305, 184)
			#end:case
			else:
				global0._send('posn:', 88, 132)
				proc913_1(15)
				self._send('setScript:', kernel.ScriptID(711, 0))
			#end:else
		#end:match
		if 
			(and
				temp1
				(not kernel.ScriptID(81, 0)._send('tstFlag:', 709, 1))
				(not kernel.ScriptID(81, 0)._send('tstFlag:', 709, 2))
				(not kernel.Random(0, 5))
			)
			kernel.ScriptID(81, 0)._send('setFlag:', 709, 2, 'loiterTimer:', 1)
		#endif
		global0._send('scaler:')._send('doit:')
		if (not script):
			global1._send('handsOn:')
		#endif
	#end:method

	@classmethod
	def notify(param1 = None, *rest):
		kernel.ScriptID(80, 0)._send('stopTimers:', 0)
		if param1:
			global2._send('script:')._send('changeState:', 2)
		else:
			global2._send('script:')._send('changeState:', 7)
		#endif
	#end:method

	@classmethod
	def doit():
		local9 = global0._send('onControl:', 1)
		(cond
			case script: 0#end:case
			case (local9 & 0x4000):
				global2._send('newRoom:', 720)
			#end:case
			case (local9 & 0x2000):
				global2._send('newRoom:', 820)
			#end:case
			case (local9 & 0x0400):
				global2._send('newRoom:', 770)
			#end:case
		)
		super._send('doit:', &rest)
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		global0._send('setMotion:', 0)
		kernel.ScriptID(80, 6)._send('actions:', 0)
		super._send('newRoom:', param1, &rest)
	#end:method

	@classmethod
	def warnUser(param1 = None, param2 = None, *rest):
		match param1
			case 5:
				if temp0 = self._send('roomToEdge:', param2):
					match temp0
						case 1:
							global91._send('say:', 9, 0, 19)
						#end:case
						case 2:
							global91._send('say:', 9, 0, 18)
						#end:case
					#end:match
				#endif
			#end:case
			case 6:
				if (param2 == 8):
					global91._send('say:', 9, 0, 35)
				else:
					global91._send('say:', 9, 0, 34)
				#endif
			#end:case
			case 4:
				if kernel.ScriptID(81, 0)._send('tstFlag:', 709, 1):
					kernel.ScriptID(81, 0)._send('clrFlag:', 709, 1)
					kernel.ScriptID(80, 5)._send('dispose:')
					global91._send('say:', 9, 0, 37)
				else:
					kernel.ScriptID(81, 0)._send('clrFlag:', 709, 2)
					kernel.ScriptID(80, 6)._send('dispose:')
					global91._send('say:', 9, 0, 36)
				#endif
			#end:case
			case 1:
				temp1 = 0
				(cond
					case (kernel.ScriptID(80, 0)._send('weddingMusicCount:') >= 3):
						if (not global5._send('contains:', alphaInset)):
							kernel.ScriptID(81, 0)._send('setFlag:', 709, 2)
						else:
							kernel.ScriptID(81, 0)._send('setFlag:', 709, 16)
						#endif
					#end:case
					case (not kernel.ScriptID(80, 0)._send('weddingMusicCount:')):
						if (global12 == 770):
							kernel.ScriptID(80, 0)._send(
								'weddingMusicCount:', 2,
								'weddingRemind:', 2
							)
						#endif
						temp1 = 24
					#end:case
					else:
						temp1 = 25
					#end:else
				)
				kernel.ScriptID(81, 0)._send('warnUser:', param1, 9, 0, temp1)
			#end:case
			else:
				super._send('warnUser:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def dispose():
		kernel.ScriptID(81, 0)._send('clrFlag:', 709, 16)
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
class tempScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cycles = 2
			#end:case
			case 1:
				kernel.ScriptID(81, 0)._send('startGuard:')
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class enterDungeon(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global91._send('say:', 4, 5, 7, 0, self)
			#end:case
			case 1:
				global105._send('number:', 821, 'loop:', 1, 'play:')
				global0._send('setPri:', global0._send('priority:'))
				register._send('setCycle:', End)
				global0._send(
					'view:', 711,
					'normal:', 0,
					'loop:', 1,
					'cel:', 0,
					'cycleSpeed:', 8,
					'posn:', (global0._send('x:') + 2), (global0._send('y:') + 7),
					'setCycle:', End, self
				)
			#end:case
			case 2:
				global0._send('dispose:')
				cycles = 4
			#end:case
			case 3:
				global2._send('newRoom:', 820)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class doTreasureDoor(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global91._send('say:', 11, 2, 31, 0, self)
			#end:case
			case 1:
				local10 = kernel.ScriptID(81, 0)._send('loiterTimer:')
				kernel.ScriptID(81, 0)._send('loiterTimer:', 0)
				kernel.ScriptID(80, 0)._send('stopTimers:', 1)
				global1._send('handsOn:')
				global69._send('disable:', 0, 2, 3, 4, 5)
				alphaInset._send(
					'view:', 713,
					'offsetX:', 30,
					'offsetY:', 20,
					'maxCol:', 5,
					'maxRow:', 5,
					'numButtons:', 30,
					'posn:', 87, 39,
					'init:', @local0, 7
				)
			#end:case
			case 2:
				global1._send('handsOff:')
				cycles = 2
			#end:case
			case 3:
				global91._send('say:', 2, 5, 4, 1, self)
			#end:case
			case 4:
				global105._send('number:', 901, 'loop:', 1, 'play:')
				treasureDoor._send('cycleSpeed:', 10, 'setCycle:', End, self)
			#end:case
			case 5:
				global105._send('stop:')
				global91._send('say:', 2, 5, 4, 2, self)
			#end:case
			case 6:
				proc80_2(4)
				self._send('dispose:')
			#end:case
			case 7:
				global1._send('handsOff:')
				cycles = 2
			#end:case
			case 8:
				global91._send('say:', 2, 5, 6, 0, self)
			#end:case
			case 9:
				global1._send('handsOn:')
				if kernel.ScriptID(81, 0)._send('tstFlag:', 709, 16):
					kernel.ScriptID(81, 0)._send('setFlag:', 709, 2, 'clrFlag:', 709, 16)
					kernel.ScriptID(81, 0)._send('startGuard:')
				#endif
				kernel.ScriptID(81, 0)._send('loiterTimer:', local10)
				local10 = 0
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class jolloHelpedEgo(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cycles = 3
			#end:case
			case 1:
				global91._send('say:', 9, 0, 9, 0, self)
			#end:case
			case 2:
				jollo._send('setSpeed:', 6, 'setMotion:', MoveTo, 184, 180, self)
			#end:case
			case 3:
				jollo._send('setMotion:', MoveTo, 343, 180, self)
			#end:case
			case 4:
				if kernel.ScriptID(81, 0)._send('tstFlag:', 709, 4):
					kernel.ScriptID(81, 0)._send('setFlag:', 709, 2)
					kernel.ScriptID(81, 0)._send('startGuard:')
				#endif
				if kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2):
					global102._send('fadeTo:', 701, -1)
					kernel.ScriptID(81, 0)._send('setFlag:', 709, 2)
					kernel.ScriptID(81, 0)._send('startGuard:')
					jollo._send('dispose:')
				else:
					global102._send('fadeTo:', 704, -1)
					jollo._send('hide:', 'setScript:', followTimer)
				#endif
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class followTimer(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				kernel.ScriptID(80, 0)._send('setFlag:', 711, -32768)
				seconds = 6
			#end:case
			case 1:
				kernel.ScriptID(80, 0)._send('clrFlag:', 711, -32768)
				jollo._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class talkToGuards(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		register = 0
		super._send('dispose:', &rest)
	#end:method

	@classmethod
	def doit():
		super._send('doit:')
		if ((state == 1) and register._send('perform:', path2Code)):
			global0._send('setMotion:', 0)
			self._send('cue:')
		#endif
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				kernel.ScriptID(80, 5)._send('okToCheck:', 0)
				kernel.ScriptID(80, 6)._send('okToCheck:', 0, 'checkCode:', 0)
				register = CueObj._send('client:')
				global91._send('say:', 13, 2, 0, 1, self)
			#end:case
			case 1:
				global0._send('setMotion:', PolyPath, register._send('x:'), register._send('y:'))
			#end:case
			case 2:
				if (not global0._send('facingMe:', register)):
					proc913_4(global0, register, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 3:
				cycles = 1
			#end:case
			case 4:
				global91._send('say:', 13, 2, 0, 2, self, 'oneOnly:', 0)
			#end:case
			case 5:
				client._send('setScript:', captureEgo, 0, register)
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
				if (not register):
					global91._send('say:', 9, 0, 17, 1, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				proc913_4(kernel.ScriptID(80, 6), global0, self)
			#end:case
			case 2:
				global91._send('say:', 9, 0, 17, 2, self)
			#end:case
			case 3:
				kernel.ScriptID(80, 6)._send('setScript:', kernel.ScriptID(80, 4), self, 1)
			#end:case
			case 4:
				global91._send('say:', 9, 0, 17, 3, self)
			#end:case
			case 5:
				global91._send('say:', 9, 0, 17, 4, self)
			#end:case
			case 6:
				global5._send('eachElementDo:', #hide)
				global2._send('drawPic:', 98)
				cycles = 4
			#end:case
			case 7:
				global91._send('say:', 9, 0, 17, 5, self)
			#end:case
			case 8:
				global2._send('newRoom:', 820)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class dungeonDoor1(DungeonDoor):
	#property vars (may be empty)
	x = 165
	y = 110
	approachX = 150
	approachY = 121
	loop = 3
	priority = 8
	signal = 20496
	dungeon# = 1
	
#end:class or instance

@SCI.instance
class dungeonDoor2(DungeonDoor):
	#property vars (may be empty)
	x = 193
	y = 117
	approachX = 175
	approachY = 133
	loop = 2
	signal = 20480
	dungeon# = 2
	
#end:class or instance

@SCI.instance
class dungeonDoor3(DungeonDoor):
	#property vars (may be empty)
	x = 227
	y = 134
	approachX = 199
	approachY = 160
	signal = 20480
	dungeon# = 3
	
#end:class or instance

@SCI.instance
class treasureDoor(Prop):
	#property vars (may be empty)
	x = 52
	y = 109
	noun = 11
	sightAngle = 45
	approachX = 66
	approachY = 134
	view = 710
	loop = 1
	signal = 20480
	
	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('approachVerbs:', 5, 2)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 2:
				if 
					(or
						kernel.ScriptID(81, 0)._send('tstFlag:', 709, 2)
						kernel.ScriptID(81, 0)._send('tstFlag:', 709, 4)
					)
					global91._send('say:', noun, 2, 30, 1)
				else:
					global2._send('setScript:', doTreasureDoor)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class alphaInset(PanelInset):
	#property vars (may be empty)
	noun = 2
	
	@classmethod
	def init():
		global69._send('disable:', 6)
		super._send('init:', &rest)
	#end:method

	@classmethod
	def dispose():
		global69._send('enable:', 6)
		if (charCount < strLen):
			global2._send('setScript:', clearedInset, 0, charCount)
		#endif
		super._send('dispose:')
		local11 = local12 = 0
	#end:method

	@classmethod
	def drawButton():
		temp0 = 0
		if (not proc999_5(value, 26, 27, 29, 30)):
			if (not (local11[(value / 16)] & (0x8000 >> (mod value 16)))):
				(local11[(value / 16)] |= (0x8000 >> (mod value 16)))
				temp0 = super._send('drawButton:', &rest)
				global104._send('number:', 910, 'setLoop:', 1, 'play:')
			else:
				temp0 = 0
			#endif
		#endif
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class clearedInset(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				cycles = 2
			#end:case
			case 1:
				if register:
					global91._send('say:', 2, 5, 6, 0, self)
				else:
					global91._send('say:', 2, 5, 5, 0, self)
				#endif
			#end:case
			case 2:
				global1._send('handsOn:')
				kernel.ScriptID(80, 0)._send('stopTimers:', 0)
				kernel.ScriptID(81, 0)._send('loiterTimer:', local10)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class armour(Feature):
	#property vars (may be empty)
	x = 151
	y = 111
	z = 10
	noun = 10
	nsTop = 91
	nsLeft = 148
	nsBottom = 111
	nsRight = 155
	sightAngle = 45
	approachX = 149
	approachY = 112
	
#end:class or instance

@SCI.instance
class roomStuff(Feature):
	#property vars (may be empty)
	@classmethod
	def init():
		super._send('init:', &rest)
		sightAngle = 26505
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		temp0 = kernel.OnControl(4, param1._send('x:'), param1._send('y:'))
		(return
			(or
				((0x1000 & temp0) and noun = 14)
				((0x0002 & temp0) and noun = 3)
				((0x6404 & temp0) and noun = 12)
				((0x0188 & temp0) and noun = 5)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class jollo(Actor):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class path2Code(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		temp0 = 0
		if 
			(and
				(param1._send('regPathID:')._send('currentRoom:') == global11)
				(not param1._send('inRect:', 140, 0, 320, 116))
				(>= 320 param1._send('x:') 0)
			)
			temp1 = param1._send('onControl:', 1)
			temp0 = ((local9 == temp1) or ((| local9 temp1) & 0x0100))
		#endif
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class guardDoVerb(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		temp0 = 1
		if (param1 == 2):
			global2._send('setScript:', talkToGuards)
		else:
			temp0 = 0
		#endif
		return temp0
	#end:method

#end:class or instance

