#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 840
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
	rm840 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None
local4 = None
local5 = None
local6 = None
local7 = None
local8 = None
local9 = None


@SCI.instance
class rm840(CastleRoom):
	#property vars (may be empty)
	noun = 9
	picture = 840
	style = 10
	horizon = 10
	north = 720
	west = 710
	vanishingX = 202
	vanishingY = 95
	minScaleSize = 35
	minScaleY = 111
	maxScaleY = 173
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		scalerCode = guardScalerCode
		self._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', -260, -10, 319, -10, 319, 179, 266, 142, 272, 142, 252, 129, 246, 129, 220, 111, 147, 111, 147, 115, 171, 115, 137, 135, 85, 103, 65, 55, 31, 55, 31, 58, 58, 58, 80, 105, 134, 139, 77, 178, -260, 178,
					'yourself:'
				)
		)
		global32._send('add:', stairCase, roomFeatures, floors, 'eachElementDo:', #init)
		super._send('init:', &rest)
		spotEgoScr = captureEgo
		kernel.ScriptID(80, 5)._send('noun:', 1, 'okToCheck:', CheckCode, 'actions:', guardDoVerb)
		kernel.ScriptID(80, 6)._send('noun:', 1, 'okToCheck:', CheckCode, 'actions:', guardDoVerb)
		kernel.ScriptID(81, 0)._send(
			'guard1Code:', path1Code,
			'guard2Code:', path1Code,
			'setupGuards:'
		)
		clownDoor._send('init:', 'stopUpd:')
		grandHallDoor._send('init:', 'stopUpd:')
		global0._send(
			'init:',
			'actions:', egoDoVerb,
			'setScale:', Scaler, maxScaleSize, minScaleSize, maxScaleY, minScaleY
		)
		match global12
			case 720:
				global0._send('posn:', 175, 116)
			#end:case
			case 710:
				global0._send('posn:', 16, 184)
			#end:case
			case 780:
				global0._send('posn:', 232, 122)
			#end:case
			else:
				local1 = local2 = 1
				global0._send('posn:', 48, 58, 'setScale:', 'scaleX:', 107, 'scaleY:', 107)
			#end:else
		#end:match
		if kernel.IsObject(global0._send('scaler:')):
			global0._send('scaler:')._send('doit:')
		#endif
		if 
			(and
				kernel.ScriptID(81, 0)._send('tstFlag:', 709, 4)
				(not kernel.ScriptID(81, 0)._send('tstFlag:', 709, 8))
			)
			self._send('setScript:', weddingCorralCrunch)
		#endif
		if kernel.ScriptID(80, 0)._send('tstFlag:', 711, -32768):
			if script:
				followedClown._send('next:', script)
			#endif
			self._send('setScript:', followedClown)
		#endif
		if (not script):
			global1._send('handsOn:')
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		local0 = global0._send('onControl:', 1)
		(cond
			case script: 0#end:case
			case (local0 & 0x4000):
				global2._send('newRoom:', 720)
			#end:case
			case ((not local7) and (local0 & 0x3000)):
				self._send('setScript:', climbStairs)
			#end:case
			case (local0 & 0x0800):
				global2._send('newRoom:', 780)
			#end:case
			case (proc999_4(61, 45, 137, 130, global0) and global0._send('isStopped:')):
				self._send('setScript:', climbStairs, 0, 1)
			#end:case
		)
		if 
			(and
				proc999_4(61, 45, 136, 137, global0)
				global0._send('isBlocked:')
				(script != captureEgo)
			)
			if temp0 = global5._send('firstTrue:', #perform, RoomCheck):
				self._send('spotEgo:', temp0)
			else:
				global0._send('ignoreActors:', 1)
			#endif
		#endif
		if local1:
			if global0._send('inRect:', 0, 0, 85, 78):
				local3 = 0
				if (not local2):
					local2 = 1
					global0._send(
						'oldScaleSignal:', 0,
						'setScale:',
						'scaleX:', 107,
						'scaleY:', 107
					)
				#endif
			else:
				local2 = 0
				if (not local3):
					local3 = 1
					global0._send(
						'oldScaleSignal:', 0,
						'setScale:', Scaler, maxScaleSize, minScaleSize, maxScaleY, minScaleY
					)
				#endif
			#endif
		#endif
		(cond
			case (local1 and (local0 & 0x0008)):
				local1 = 0
			#end:case
			case ((not local1) and (local0 & 0x1000)):
				local1 = 1
			#end:case
		)
		super._send('doit:', &rest)
	#end:method

	@classmethod
	def doLoiter():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not argc):
			global91._send('say:', 10, 0, 26)
			kernel.ScriptID(81, 0)._send('loiterTimer:', 15)
		#endif
	#end:method

	@classmethod
	def warnUser(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				local9 = 0
				(cond
					case (kernel.ScriptID(80, 0)._send('weddingMusicCount:') >= 3):
						local9 = 30
						kernel.ScriptID(81, 0)._send('setFlag:', 709, 1, 2)
					#end:case
					case (not kernel.ScriptID(80, 0)._send('weddingMusicCount:')):
						clownDoor._send('_approachVerbs:', 0)
						local9 = 28
					#end:case
					else:
						local9 = 29
					#end:else
				)
				kernel.ScriptID(81, 0)._send('warnUser:', param1, 10, 0, local9)
			#end:case
			case 6:
				global91._send('say:', 10, 0, 22)
			#end:case
			case 5:
				if 
					(and
						(not (global2._send('script:') == weddingCorralCrunch))
						temp0 = self._send('roomToEdge:', param2)
					)
					match temp0
						case 4:
							global91._send('say:', 10, 0, 19)
						#end:case
						case 1:
							global91._send('say:', 10, 0, 18)
						#end:case
					#end:match
				#endif
			#end:case
			case 4:
				if (not kernel.ScriptID(81, 0)._send('tstFlag:', 709, 4)):
					if kernel.ScriptID(81, 0)._send('tstFlag:', 709, 2):
						global91._send('say:', 10, 0, 23)
					else:
						global91._send('say:', 10, 0, 21)
					#endif
				#endif
			#end:case
			else:
				super._send('warnUser:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.ScriptID(80, 5)._send('actions:', 0)
		kernel.ScriptID(80, 6)._send('actions:', 0)
		kernel.ScriptID(80, 0)._send('clrFlag:', 711, -32768)
		super._send('newRoom:', param1, &rest)
	#end:method

	@classmethod
	def scriptCheck(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case proc999_5(param1, 87, 908):
				if 
					(or
						kernel.ScriptID(81, 0)._send('tstFlag:', 709, 1)
						kernel.ScriptID(81, 0)._send('tstFlag:', 709, 2)
						kernel.ScriptID(81, 0)._send('tstFlag:', 709, 4)
					)
					global91._send('say:', 3, 14, 1, 0, 0, 899)
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
class RoomCheck(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(and
				param1._send('isKindOf:', GuardDog)
				(param1._send('regPathID:')._send('currentRoom:') == global11)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class talkToGuards(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('dispose:', &rest)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('doit:')
		if ((state == 1) and register._send('perform:', register._send('checkCode:'))):
			global0._send('setMotion:', 0)
			self._send('cue:')
		#endif
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				kernel.ScriptID(80, 5)._send('okToCheck:', 0)
				kernel.ScriptID(80, 6)._send('okToCheck:', 0)
				register = CueObj._send('client:')
				global91._send('say:', 1, 2, 0, 1, self)
			#end:case
			case 1:
				local6 = 1
				local7 = 1
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
				global91._send('say:', 1, 2, 0, 2, self, 'oneOnly:', 0)
			#end:case
			case 5:
				global2._send('spotEgo:', register)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class captureEgo(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				if 
					(and
						global5._send('contains:', kernel.ScriptID(80, 5))
						global5._send('contains:', kernel.ScriptID(80, 6))
						(==
							kernel.ScriptID(80, 5)._send('regPathID:')._send('currentRoom:')
							global11
						)
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
				if (not local6):
					global91._send('say:', 10, 0, 16, 1, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				proc913_4(register, global0, self)
			#end:case
			case 3:
				cycles = 14
			#end:case
			case 4:
				global0._send('stopUpd:')
				grandHallDoor._send('setCycle:', 0, 'stopUpd:')
				cycles = 4
			#end:case
			case 5:
				global91._send('say:', 10, 0, 16, 2, self)
			#end:case
			case 6:
				register._send('setScript:', kernel.ScriptID(80, 4), self, 1)
			#end:case
			case 7:
				register._send('stopUpd:')
				cycles = 4
			#end:case
			case 8:
				global91._send('say:', 10, 0, 16, 3, self)
			#end:case
			case 9:
				global91._send('say:', 10, 0, 16, 4, self)
			#end:case
			case 10:
				global5._send('eachElementDo:', #hide)
				global2._send('drawPic:', 98)
				cycles = 4
			#end:case
			case 11:
				global91._send('say:', 10, 0, 16, 5, self)
			#end:case
			case 12:
				global2._send('newRoom:', 820)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class weddingCorralCrunch(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				cycles = 2
			#end:case
			case 1:
				if (kernel.ScriptID(80, 6)._send('regPathID:')._send('value:') < 8):
					kernel.ScriptID(80, 6)._send('regPathID:')._send('value:', 8, 'moveDone:')
				#endif
				kernel.ScriptID(81, 0)._send('setFlag:', 709, 1, 8)
				global91._send('say:', 10, 0, 15, 0, self)
			#end:case
			case 2:
				kernel.ScriptID(81, 0)._send('startGuard:')
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class climbStairs(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				if register:
					(= register
						(grandHallDoor if (global0._send('x:') <= 88) else stairCase)
					)
				else:
					(= register
						(grandHallDoor if (local0 & 0x2000) else stairCase)
					)
				#endif
				global0._send(
					'setMotion:', PolyPath, register._send('approachX:'), register._send(
							'approachY:'
						), self
				)
			#end:case
			case 1:
				global1._send('handsOn:')
				register = 0
				global0._send('oldScaleSignal:', 0, 'reset:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class followedClown(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				kernel.ScriptID(80, 0)._send('clrFlag:', 711, -32768)
				jollo._send('view:', 717, 'loop:', 8)
				if (global12 == 710):
					jollo._send('posn:', 142, 150, 'loop:', 3)
				else:
					jollo._send('posn:', 177, 130, 'loop:', 1)
				#endif
				jollo._send(
					'ignoreActors:', 1,
					'setCycle:', Walk,
					'setScale:', Scaler, global2._send('maxScaleSize:'), global2._send(
							'minScaleSize:'
						), global2._send('maxScaleY:'), global2._send('minScaleY:'),
					'init:'
				)
				cycles = 2
			#end:case
			case 1:
				if (global9._send('at:', 25)._send('owner:') == 750):
					self._send('setScript:', jolloClimbStairs, self)
				else:
					self._send('setScript:', jolloGotoBed, self)
				#endif
			#end:case
			case 2:
				if (not next):
					global1._send('handsOn:')
				#endif
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class jolloClimbStairs(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				jollo._send('setMotion:', MoveTo, 132, 134, self)
			#end:case
			case 1:
				jollo._send('setMotion:', PolyPath, 90, 134, self)
			#end:case
			case 2:
				jollo._send(
					'setScale:',
					'scaleX:', 107,
					'scaleY:', 107,
					'setMotion:', PolyPath, 48, 55, self
				)
			#end:case
			case 3:
				global105._send('number:', 901, 'loop:', 1, 'play:')
				grandHallDoor._send('priority:', 10, 'setCycle:', End, self)
			#end:case
			case 4:
				global105._send('stop:')
				jollo._send('setMotion:', MoveTo, (jollo._send('x:') - 15), jollo._send('y:'), self)
			#end:case
			case 5:
				jollo._send('hide:')
				grandHallDoor._send('priority:', 0, 'setCycle:', Beg, self)
			#end:case
			case 6:
				global105._send('number:', 902, 'loop:', 1, 'play:')
				grandHallDoor._send('stopUpd:')
				if (global9._send('at:', 25)._send('owner:') == 750):
					jollo._send('setScript:', followTimer)
				else:
					jollo._send('dispose:')
				#endif
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
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				kernel.ScriptID(80, 0)._send('setFlag:', 711, -32768)
				seconds = 10
			#end:case
			case 1:
				kernel.ScriptID(80, 0)._send('clrFlag:', 711, -32768)
				jollo._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class jolloGotoBed(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				jollo._send('setMotion:', MoveTo, 236, 124, self)
			#end:case
			case 1:
				global105._send('number:', 901, 'loop:', 1, 'play:')
				clownDoor._send('setCycle:', End, self)
			#end:case
			case 2:
				global105._send('stop:')
				jollo._send('setMotion:', MoveTo, 238, 121, self)
			#end:case
			case 3:
				jollo._send('setMotion:', MoveTo, (jollo._send('x:') + 10), jollo._send('y:'), self)
			#end:case
			case 4:
				jollo._send('dispose:')
				clownDoor._send('setCycle:', Beg, self)
			#end:case
			case 5:
				global105._send('number:', 902, 'loop:', 1, 'play:')
				clownDoor._send('stopUpd:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class clownDoor(Prop):
	#property vars (may be empty)
	x = 237
	y = 104
	noun = 5
	sightAngle = 45
	approachX = 234
	approachY = 122
	view = 840
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('ignoreActors:', 1, 'yStep:', -1)
		if (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2)):
			self._send('approachVerbs:', 5)
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				if kernel.ScriptID(80, 0)._send('tstFlag:', 709, 4):
					global91._send('say:', noun, param1, 9, 0)
				else:
					global91._send('say:', noun, param1, 8, 0)
				#endif
			#end:case
			case 5:
				(cond
					case 
						(or
							kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2)
							kernel.ScriptID(81, 0)._send('tstFlag:', 709, 4)
						):
						global91._send('say:', noun, param1, 7, 0)
					#end:case
					case 
						(or
							kernel.ScriptID(81, 0)._send('tstFlag:', 709, 1)
							kernel.ScriptID(81, 0)._send('tstFlag:', 709, 2)
						):
						if kernel.ScriptID(80, 0)._send('tstFlag:', 709, 4):
							global91._send('say:', noun, param1, 6, 0, self)
						else:
							global91._send('say:', noun, param1, 5, 0, self)
						#endif
					#end:case
					case (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 4)):
						global91._send('say:', noun, param1, 3, 0, self)
					#end:case
					else:
						self._send('cue:', 0)
					#end:else
				)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def cue(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1 = yStep.post('++')
			case 0:
				global1._send('handsOff:')
				self._send('ignoreActors:', 'setCycle:', End, self)
				global104._send('number:', 901, 'setLoop:', 1, 'play:')
			#end:case
			case 1:
				kernel.ScriptID(80, 0)._send('setFlag:', 709, 4)
				proc80_2(2)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class grandHallDoor(Prop):
	#property vars (may be empty)
	x = 26
	y = 55
	z = 36
	noun = 7
	sightAngle = 45
	approachX = 48
	approachY = 55
	view = 840
	loop = 1
	cycleSpeed = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		(signal |= 0x0010)
		self._send('approachVerbs:', 5)
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		local7 = 0
		if 
			(and
				temp0 = super._send('onMe:', param1)
				(&
					_approachVerbs
					global66._send('doit:', global69._send('curIcon:')._send('message:'))
				)
			)
			local7 = 1
		#endif
		return temp0
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = kernel.ScriptID(80, 5)._send('onControl:', 1)
		temp1 = kernel.ScriptID(80, 6)._send('onControl:', 1)
		super._send('doit:')
		if (not cycler):
			(cond
				case 
					(and
						cel
						(or
							(and
								kernel.ScriptID(81, 0)._send('tstFlag:', 709, 1)
								(not (temp0 & 0x0400))
							)
							(and
								kernel.ScriptID(81, 0)._send('tstFlag:', 709, 2)
								kernel.IsObject(kernel.ScriptID(80, 6)._send('regPathID:'))
								(==
									kernel.ScriptID(80, 6)._send('regPathID:')._send('currentRoom:')
									global11
								)
								(not (temp1 & 0x0400))
							)
						)
					):
					self._send('setCycle:', Beg, self)
				#end:case
				case 
					(and
						(not cel)
						(or
							(and
								kernel.ScriptID(81, 0)._send('tstFlag:', 709, 1)
								kernel.ScriptID(80, 5)._send('mover:')
								(temp0 & 0x0400)
							)
							(and
								kernel.ScriptID(81, 0)._send('tstFlag:', 709, 2)
								kernel.IsObject(kernel.ScriptID(80, 6)._send('regPathID:'))
								(==
									kernel.ScriptID(80, 6)._send('regPathID:')._send('currentRoom:')
									global11
								)
								(temp1 & 0x0400)
							)
						)
					):
					self._send('cue:', 1, 'setCycle:', End)
				#end:case
				else: 0#end:else
			)
		#endif
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('ignoreActors:', (not (signal & 0x4000)))
		if (not local5):
			if argc:
				priority = 10
				global105._send('number:', 901, 'loop:', 1, 'play:')
			else:
				priority = 0
				self._send('stopUpd:')
				global105._send('number:', 902, 'loop:', 1, 'play:')
			#endif
		else:
			global2._send('newRoom:', 730)
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		local7 = 0
		match param1
			case 5:
				global1._send('handsOff:')
				global2._send('newRoom:', 730)
			#end:case
			case 1:
				if (not local4):
					local4.post('++')
					(_approachVerbs |= global66._send('doit:', 1))
					global91._send('say:', noun, param1, 11)
				else:
					global0._send(
						'oldScaleSignal:', 0,
						'oldMaxScale:', 0,
						'oldBackSize:', 0,
						'oldFrontY:', 0,
						'oldBackY:', 0
					)
					global1._send('handsOff:')
					global91._send('say:', noun, param1, 10, 1)
					global2._send('setScript:', kernel.ScriptID(82), 0, lookIntoGrandHall)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class keyHoleActions(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 1
		match param1
			case 1:
				if kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2):
					global91._send('say:', 8, param1, 32)
				else:
					temp0 = 0
				#endif
			#end:case
			else:
				temp0 = 0
			#end:else
		#end:match
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class lookIntoGrandHall(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if register:
			register = 0
			tempGuard1._send('dispose:')
			tempGuard2._send('dispose:')
		#endif
		accessaryView._send('dispose:')
		if kernel.ScriptID(80, 0)._send('tstFlag:', 711, -32768):
			jollo._send('dispose:')
		#endif
		kernel.ScriptID(80, 0)._send('clrFlag:', 711, -32768)
		super._send('dispose:')
		kernel.ScriptID(80, 0)._send('stopTimers:', 0)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				kernel.ScriptID(80, 0)._send('stopTimers:', 1)
				kernel.ScriptID(82, 1)._send(
					'noun:', 8,
					'actions:', keyHoleActions,
					'init:', 793, 0, 0, 74, 46
				)
				jollo._send('setScript:', 0)
				accessaryView._send('init:')
				if (not register = kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2)):
					tempGuard1._send('init:', 'stopUpd:')
					tempGuard2._send('init:', 'stopUpd:')
				#endif
				cycles = 2
			#end:case
			case 1:
				local9 = (32 if register else 10)
				global91._send('say:', 7, 1, local9, 2, self)
			#end:case
			case 2:
				if kernel.ScriptID(80, 0)._send('tstFlag:', 711, -32768):
					jollo._send(
						'view:', 717,
						'loop:', 0,
						'cel:', 5,
						'x:', 143,
						'y:', 96,
						'setScale:',
						'scaleX:', 49,
						'scaleY:', 49,
						'priority:', 12,
						'setCycle:', Walk,
						'signal:', 16400,
						'init:',
						'setMotion:', MoveTo, 173, 79
					)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class accessaryView(View):
	#property vars (may be empty)
	view = 793
	cel = 1
	priority = 11
	signal = 16400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		x = kernel.ScriptID(82, 1)._send('x:')
		y = kernel.ScriptID(82, 1)._send('y:')
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class tempGuard1(View):
	#property vars (may be empty)
	x = 148
	y = 128
	noun = 8
	sightAngle = 180
	view = 793
	loop = 1
	priority = 14
	signal = 16400
	scaleSignal = 1
	
#end:class or instance

@SCI.instance
class tempGuard2(View):
	#property vars (may be empty)
	x = 167
	y = 126
	noun = 8
	sightAngle = 180
	view = 793
	loop = 1
	cel = 1
	priority = 14
	signal = 16400
	scaleSignal = 1
	
#end:class or instance

@SCI.instance
class stairCase(Feature):
	#property vars (may be empty)
	x = 129
	y = 136
	z = 24
	noun = 11
	nsTop = 90
	nsLeft = 123
	nsBottom = 135
	nsRight = 136
	sightAngle = 45
	approachX = 141
	approachY = 137
	
#end:class or instance

@SCI.instance
class roomFeatures(Feature):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		sightAngle = 26505
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = kernel.OnControl(4, param1._send('x:'), param1._send('y:'))
		(return
			(or
				((0x0010 & temp0) and noun = 13)
				((0x0002 & temp0) and noun = 4)
				((0x7804 & temp0) and noun = 12)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class floors(Feature):
	#property vars (may be empty)
	noun = 6
	onMeCheck = 392
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		global93._send('add:', self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global93._send('delete:', self)
		super._send('dispose:')
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		local7 = 0
		if 
			(and
				(param1._send('type:') & 0x1000)
				(not param1._send('modifiers:'))
				self._send('onMe:', param1)
			)
			local7 = 1
		else:
			super._send('handleEvent:', param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class jollo(Actor):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class guardScalerCode(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case param1._send('inRect:', 0, 0, 88, 86):
				if param1._send('scaler:'):
					param1._send('setScale:', 'scaleX:', 107, 'scaleY:', 107)
				#endif
			#end:case
			case (not param1._send('scaler:')):
				param1._send(
					'setScale:', Scaler, global2._send('maxScaleSize:'), global2._send(
							'minScaleSize:'
						), global2._send('maxScaleY:'), global2._send('minScaleY:')
				)
				param1._send('scaler:')._send('doit:')
			#end:case
		)
	#end:method

#end:class or instance

@SCI.instance
class CheckCode(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(and
				param1._send('regPathID:')
				(param1._send('regPathID:')._send('currentRoom:') == global11)
				(not param1._send('inRect:', 136, 64, 174, 118))
				(not param1._send('inRect:', -20, 0, 35, 67))
				(param1._send('x:') > 0)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class path1Code(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp1 = 0
		temp0 = param1._send('onControl:', 1)
		if param1._send('regPathID:'):
			if ((not local1) and (global2._send('script:') != climbStairs)):
				(= temp1
					if 
						(and
							(param1._send('regPathID:')._send('currentRoom:') == global11)
							(temp0 & 0x0188)
						)
						if (param1._send('loop:') == 3):
							(global0._send('y:') <= param1._send('y:'))
						else:
							((local0 == temp0) or ((| local0 temp0) & 0x0100))
						#endif
					else:
						0
					#endif
				)
			else:
				(= temp1
					if (param1._send('regPathID:')._send('currentRoom:') == global11):
						param1._send('inRect:', 0, 0, 119, 131)
					#endif
				)
			#endif
		#endif
		return temp1
	#end:method

#end:class or instance

@SCI.instance
class egoDoVerb(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 1
		if proc999_5(param1, 14, 19):
			if 
				(or
					kernel.ScriptID(81, 0)._send('tstFlag:', 709, 1)
					kernel.ScriptID(81, 0)._send('tstFlag:', 709, 2)
					kernel.ScriptID(81, 0)._send('tstFlag:', 709, 4)
				)
				global91._send('say:', 3, 14, 1)
			else:
				temp0 = 0
			#endif
		else:
			temp0 = 0
		#endif
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class guardDoVerb(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 1
		if (param1 == 2):
			global2._send('setScript:', talkToGuards)
		else:
			temp0 = 0
		#endif
		return temp0
	#end:method

#end:class or instance

