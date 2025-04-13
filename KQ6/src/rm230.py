#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 230
import sci_sh
import kernel
import Main
import KQ6Print
import KQ6Room
import CartoonScript
import n913
import Inset
import Scaler
import PolyPath
import Polygon
import Feature
import DPath
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm230 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.instance
class rm230(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 230
	horizon = 0
	north = 220
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global2._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 0, 0, 319, 0, 319, 81, 250, 81, 250, 63, 232, 62, 232, 73, 202, 79, 165, 97, 112, 126, 105, 133, 62, 148, 47, 148, 0, 156,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 171, 115, 250, 115, 236, 126, 182, 126,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 161, 182, 168, 187, 192, 180, 319, 165, 319, 189, 0, 189, 0, 170, 64, 182,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 1,
					'init:', 325, 90, 325, 158, 317, 158, 317, 90,
					'yourself:'
				)
		)
		super._send('init:', &rest)
		global0._send('init:', 'setScale:', Scaler, 100, 58, 140, 58)
		self._send('setScript:', enterRoomScr)
		castleWall._send('init:')
		vine._send('init:')
		bush._send('init:')
		if (global1._send('_detailLevel:') >= 2):
			bush._send('setScript:', kernel.ScriptID(13, 0))
		#endif
		if proc913_0(23):
			magicDoor._send('init:')
			if proc913_0(24):
				magicDoor._send('view:', 233, 'loop:', 8, 'cel:', 0)
			#endif
		#endif
		if (global9._send('at:', 18)._send('owner:') == global11):
			holeOnWall._send('init:')
		#endif
		genericFeatures._send('init:')
		kernel.ScriptID(10, 4)._send('onMeCheck:', 136, 'init:')
		global103._send('number:', 917, 'loop:', -1, 'play:')
	#end:method

	@classmethod
	def notify():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global2._send('setScript:', enchantDoorScr)
	#end:method

	@classmethod
	def edgeToRoom(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 2):
			global0._send('x:', (global0._send('x:') - 1))
			global91._send('say:', 3, 3, 15, 1)
			return 0
		else:
			super._send('edgeToRoom:', param1, &rest)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = global0._send('onControl:', 1)
		(cond
			case script: 0#end:case
			case (temp0 & 0x4000):
				global2._send('setScript:', exitRoomScr)
			#end:case
			case ((temp0 & 0x0080) and (not local0) and global0._send('isStopped:')):
				local0 = 1
				global91._send('say:', noun, 3, 12)
			#end:case
			case (local0 and (temp0 & 0x0080) and (not global0._send('isStopped:'))):
				local0 = 0
			#end:case
		)
		super._send('doit:', &rest)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global103._send('fade:')
		super._send('dispose:')
		kernel.DisposeScript(964)
		kernel.DisposeScript(13)
		kernel.DisposeScript(231)
	#end:method

#end:class or instance

@SCI.instance
class holeInset(Inset):
	#property vars (may be empty)
	view = 487
	x = 133
	y = 101
	disposeNotOnMe = 1
	noun = 12
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global103._send('fade:')
		super._send('init:', &rest)
		wallView._send('init:')
		global1._send('handsOn:')
		global69._send('disable:', 0, 1, 3, 4, 5, 6)
		insetView._send('signal:', (| insetView._send('signal:') 0x1000))
		if (not guardWalkByScr._send('register:')):
			self._send('setScript:', guardWalkByScr)
		#endif
		global102._send('number:', 704, 'loop:', -1, 'play:')
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global102._send('fade:')
		global69._send('enable:', 6)
		global1._send('handsOff:')
		super._send('dispose:')
		global103._send('number:', 917, 'loop:', -1, 'play:')
	#end:method

#end:class or instance

@SCI.instance
class enterRoomScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global0._send(
					'setScale:',
					'scaleX:', 83,
					'scaleY:', 83,
					'setPri:', 3,
					'setSpeed:', 6,
					'posn:', 223, 88,
					'setMotion:', MoveTo, 238, 88, self
				)
			#end:case
			case 1:
				global0._send('setMotion:', MoveTo, 250, 84, self)
			#end:case
			case 2:
				global0._send('setLoop:', 2, 'setMotion:', MoveTo, 244, 71, self)
			#end:case
			case 3:
				global0._send(
					'setScale:', Scaler, 100, 58, 140, 58,
					'setPri:', -1,
					'setLoop:', -1,
					'setMotion:', MoveTo, 228, 77, self
				)
			#end:case
			case 4:
				global0._send('reset:', 2)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class exitRoomScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setSpeed:', 6, 'setMotion:', MoveTo, 244, 71, self)
			#end:case
			case 1:
				global0._send(
					'setScale:',
					'scaleX:', 83,
					'scaleY:', 83,
					'setPri:', 3,
					'setLoop:', 3,
					'setScale:',
					'setMotion:', MoveTo, 250, 84, self
				)
			#end:case
			case 2:
				global0._send('setLoop:', -1, 'setMotion:', DPath, 238, 88, 223, 88, self)
			#end:case
			case 3:
				global2._send('newRoom:', global2._send('north:'))
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class climbVineScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send(
					'normal:', 0,
					'setSpeed:', 6,
					'view:', 231,
					'posn:', 204, 82,
					'loop:', 0,
					'cel:', 0
				)
				cycles = 2
			#end:case
			case 1:
				global0._send('setCycle:', End, self)
			#end:case
			case 2:
				global0._send('reset:', 1, 'posn:', 200, 81)
				ticks = 10
			#end:case
			case 3:
				global91._send('say:', 13, 5, 0, 0, self)
			#end:case
			case 4:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class paintWallScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global9._send('at:', 3)._send('cue:')
				global91._send('say:', 4, 44, 8, 1, self)
			#end:case
			case 1:
				global0._send(
					'normal:', 0,
					'posn:', 136, 113,
					'view:', 233,
					'loop:', 0,
					'cycleSpeed:', 10,
					'setScale:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				register = 3
				global105._send('number:', 230, 'loop:', 1, 'play:')
				global0._send('loop:', 1, 'cel:', 0, 'setCycle:', CT, 2, 1, self)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				global105._send('number:', 230, 'loop:', 1, 'play:')
				global0._send('setCycle:', CT, 4, 1, self)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				global105._send('number:', 230, 'loop:', 1, 'play:')
				global0._send('setCycle:', End, self)
			#end:case
			case 7:
				if (not register.post('--')):
					global0._send('cel:', 2)
					(state -= 3)
				#endif
				cycles = 2
			#end:case
			case 8:
				register = 3
				global105._send('number:', 230, 'loop:', 1, 'play:')
				global0._send('loop:', 2, 'cel:', 0, 'setCycle:', CT, 4, 1, self)
			#end:case
			case 9:
				global105._send('number:', 230, 'loop:', 1, 'play:')
				global0._send('setCycle:', CT, 8, 1, self)
			#end:case
			case 10:
				global105._send('number:', 230, 'loop:', 1, 'play:')
				global0._send('setCycle:', End, self)
			#end:case
			case 11:
				if (not register.post('--')):
					global0._send('cel:', 4)
					(state -= 3)
				#endif
				cycles = 2
			#end:case
			case 12:
				global0._send('loop:', 3, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 13:
				register = 3
				global105._send('number:', 230, 'loop:', 1, 'play:')
				global0._send('loop:', 4, 'cel:', 0, 'setCycle:', CT, 2, 1, self)
			#end:case
			case 14:
				cycles = 2
			#end:case
			case 15:
				global105._send('number:', 230, 'loop:', 1, 'play:')
				global0._send('setCycle:', CT, 4, 1, self)
			#end:case
			case 16:
				cycles = 2
			#end:case
			case 17:
				global105._send('number:', 230, 'loop:', 1, 'play:')
				global0._send('setCycle:', End, self)
			#end:case
			case 18:
				if (not register.post('--')):
					global0._send('cel:', 2)
					(state -= 3)
				#endif
				cycles = 2
			#end:case
			case 19:
				global0._send('loop:', 5, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 20:
				magicDoor._send('init:')
				global0._send('reset:', 7, 'posn:', 148, 107, 'setScale:', Scaler, 100, 58, 140, 58)
				cycles = 2
			#end:case
			case 21:
				global1._send('givePoints:', 1)
				ticks = 20
			#end:case
			case 22:
				global91._send('say:', 4, 44, 8, 2, self)
			#end:case
			case 23:
				proc913_1(23)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class enchantDoorScr(CartoonScript):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				if ((global0._send('x:') != 147) or (global0._send('y:') != 115)):
					global0._send('setMotion:', PolyPath, 147, 115, self)
				else:
					cycles = 2
				#endif
			#end:case
			case 1:
				global91._send('say:', 1, 0, 13, 1, self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				KQ6Print._send(
					'posn:', -1, 10,
					'font:', global22,
					'say:', 0, 1, 0, 13, 2,
					'modeless:', 1,
					'ticks:', 20,
					'init:'
				)
				cycles = 2
			#end:case
			case 4:
				global0._send(
					'normal:', 0,
					'setSpeed:', 6,
					'view:', 234,
					'loop:', 0,
					'cel:', 0,
					'setScale:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 5:
				register = 60
				self._send('cue:')
			#end:case
			case 6:
				ticks = register
			#end:case
			case 7:
				global0._send('cel:', 0, 'loop:', 1, 'setCycle:', End, self)
				(register -= 15)
				if (local1.post('++') != 4):
					(state -= 2)
				#endif
			#end:case
			case 8:
				ticks = 45
			#end:case
			case 9:
				global0._send('cycleSpeed:', 9, 'loop:', 2, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 10:
				ticks = 35
			#end:case
			case 11:
				magicDoor._send('loop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 12:
				magicDoor._send('loop:', 2, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 13:
				magicDoor._send('loop:', 3, 'setCycle:', End, self)
				global0._send('reset:', 7, 'setScale:', Scaler, 100, 58, 140, 58)
			#end:case
			case 14:
				global105._send('number:', 231, 'loop:', 1, 'play:')
				magicDoor._send('loop:', 4, 'setCycle:', End, self)
			#end:case
			case 15:
				magicDoor._send('view:', 233, 'loop:', 8, 'cel:', 0)
				cycles = 1
			#end:case
			case 16:
				if global25:
					global25._send('dispose:')
					cycles = 1
				else:
					self._send('cue:')
				#endif
			#end:case
			case 17:
				cycles = 20
			#end:case
			case 18:
				global91._send('say:', 1, 0, 13, 3, self)
			#end:case
			case 19:
				proc913_1(24)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class openDoorScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 148, 111, self)
			#end:case
			case 1:
				global0._send('setHeading:', 270, self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				global91._send('say:', 6, 5, 11, 1, self)
			#end:case
			case 4:
				global0._send(
					'setSpeed:', 6,
					'setPri:', 14,
					'normal:', 0,
					'view:', 233,
					'loop:', 9,
					'cel:', 0,
					'posn:', 136, 113,
					'setScale:', 0
				)
				cycles = 2
			#end:case
			case 5:
				global105._send('number:', 901, 'loop:', 1, 'play:', self)
				global0._send('setCycle:', CT, 2, 1, self)
				magicDoor._send('hide:')
			#end:case
			case 6:
				magicDoor._send('setPri:', -1, 'show:', 'cel:', 1)
				global0._send('cel:', 3)
				cycles = 2
			#end:case
			case 7:#end:case
			case 8:
				global91._send('say:', 6, 5, 11, 2, self)
			#end:case
			case 9:
				global1._send('givePoints:', 2)
				global0._send('setCycle:', End, self)
			#end:case
			case 10:
				global2._send('newRoom:', 710)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lookHoleScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global91._send('say:', 5, 1, 0, 0, self)
			#end:case
			case 1:
				global0._send(
					'normal:', 0,
					'setSpeed:', 6,
					'view:', 232,
					'loop:', 4,
					'cel:', 0,
					'posn:', 89, 140,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				holeInset._send('init:', self, global2)
			#end:case
			case 3:
				cycles = 3
			#end:case
			case 4:
				global0._send('loop:', 4, 'setCycle:', Beg, self)
			#end:case
			case 5:
				global0._send('posn:', 97, 140, 'reset:', 7)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class placeHoleScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global0._send('put:', 18, global11)
				global1._send('handsOff:')
				global0._send(
					'normal:', 0,
					'posn:', 84, 140,
					'setSpeed:', 6,
					'view:', 232,
					'loop:', 1,
					'cel:', 0,
					'setCycle:', CT, 5, 1, self
				)
			#end:case
			case 1:
				holeOnWall._send('init:')
				global0._send('setCycle:', End, self)
			#end:case
			case 2:
				global0._send('posn:', 94, 139, 'reset:', 7)
				cycles = 2
			#end:case
			case 3:
				global91._send('say:', 4, 25, 0, 0, self)
			#end:case
			case 4:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class removeHoleScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('get:', 18)
				global0._send(
					'normal:', 0,
					'posn:', 84, 140,
					'setSpeed:', 6,
					'view:', 232,
					'loop:', 1,
					'cel:', 6,
					'setCycle:', CT, 5, -1, self
				)
			#end:case
			case 1:
				holeOnWall._send('dispose:')
				global0._send('setCycle:', Beg, self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				global0._send('posn:', 94, 139, 'reset:', 7)
				cycles = 2
			#end:case
			case 4:
				global91._send('say:', 5, 5, 0, 0, self)
			#end:case
			case 5:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class guardWalkByScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				register = 1
				seconds = kernel.Random(5, 15)
			#end:case
			case 1:
				guardDog._send('init:', 'setMotion:', MoveTo, 190, 137, self)
			#end:case
			case 2:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('dispose:')
		if global5._send('contains:', guardDog):
			guardDog._send('dispose:')
		#endif
	#end:method

#end:class or instance

@SCI.instance
class bush(Prop):
	#property vars (may be empty)
	x = 18
	y = 134
	noun = 9
	view = 230
	priority = 15
	signal = 20496
	
#end:class or instance

@SCI.instance
class magicDoor(Prop):
	#property vars (may be empty)
	x = 136
	y = 113
	noun = 6
	sightAngle = 15
	approachX = 147
	approachY = 115
	view = 235
	priority = 1
	signal = 16401
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				temp0 = super._send('onMe:', param1)
				(or
					((param1._send('message:') == 5) and proc913_0(24))
					((param1._send('message:') == 28) and (not proc913_0(24)))
				)
			)
			_approachVerbs = global66._send('doit:', param1._send('message:'))
		#endif
		return temp0
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (param1 == 5):
				if proc913_0(24):
					global2._send('setScript:', openDoorScr)
				else:
					global91._send('say:', noun, 5, 10)
				#endif
			#end:case
			case proc999_5(param1, 1, 2):
				global91._send('say:', noun, param1, (11 if proc913_0(24) else 10))
			#end:case
			case (param1 == 28):
				if proc913_0(24):
					global91._send('say:', noun, param1, 11)
				else:
					KQ6Print._send('say:', 0, 6, 28, 10, 1, 'init:')
					global2._send('setScript:', kernel.ScriptID(190))
				#endif
			#end:case
			case (param1 == 29):
				global91._send('say:', 4, param1, 5)
			#end:case
			case (param1 == 44):
				global91._send('say:', noun, param1)
			#end:case
			else:
				global91._send('say:', noun, 0, (11 if proc913_0(24) else 10))
			#end:else
		)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('approachVerbs:', 28)
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class guardDog(Actor):
	#property vars (may be empty)
	x = 78
	y = 137
	noun = 15
	view = 726
	priority = 13
	signal = 16400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('setScale:', 'setCycle:', Walk)
	#end:method

#end:class or instance

@SCI.instance
class holeOnWall(View):
	#property vars (may be empty)
	x = 75
	y = 141
	z = 47
	noun = 5
	approachX = 92
	approachY = 140
	view = 482
	loop = 1
	signal = 17
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if temp0 = super._send('onMe:', param1, &rest):
			match param1._send('message:')
				case 5:
					(approachX == 97)
				#end:case
				case 1:
					(approachY == 94)
				#end:case
			#end:match
		#endif
		return temp0
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				global2._send('setScript:', lookHoleScr)
			#end:case
			case 5:
				global2._send('setScript:', removeHoleScr)
			#end:case
			else:
				super._send('doVerb:', param1)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('approachVerbs:', 5, 1)
	#end:method

#end:class or instance

@SCI.instance
class wallView(View):
	#property vars (may be empty)
	x = 141
	y = 96
	noun = 12
	view = 230
	loop = 1
	priority = 12
	signal = 17
	
#end:class or instance

@SCI.instance
class castleWall(Feature):
	#property vars (may be empty)
	noun = 4
	sightAngle = 45
	onMeCheck = 2
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if temp0 = super._send('onMe:', param1, &rest):
			if 
				(or
					(param1._send('message:') == 25)
					(and
						proc999_5(param1._send('message:'), 44, 29)
						proc913_0(22)
						global0._send('has:', 3)
						global0._send('has:', 46)
					)
				)
				self._send('_approachVerbs:', (| 0x8000 self._send('_approachVerbs:')))
				if (param1._send('message:') == 25):
					approachX = 94
					approachY = 140
					x = 70
					y = 118
					return temp0
				#endif
			else:
				self._send('_approachVerbs:', (0x7fff & self._send('_approachVerbs:')))
			#endif
		#endif
		if (approachX != 147):
			approachX = 147
			approachY = 115
			x = 136
			y = 105
		#endif
		return temp0
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 44:
				(cond
					case proc913_0(23):
						global91._send('say:', noun, param1, 5)
					#end:case
					case (not proc913_0(22)):
						if (proc913_0(58) or proc913_0(68)):
							global91._send('say:', noun, param1, 6)
						else:
							global91._send('say:', noun, param1, 9)
						#endif
					#end:case
					case (not global0._send('has:', 3)):
						global91._send('say:', noun, 44, 7)
					#end:case
					else:
						global2._send('setScript:', paintWallScr)
					#end:else
				)
			#end:case
			case 29:
				(cond
					case proc913_0(23):
						global91._send('say:', noun, param1, 5)
					#end:case
					case proc913_0(22):
						self._send('doVerb:', 44, &rest)
					#end:case
					else:
						global91._send('say:', noun, param1, 6)
					#end:else
				)
			#end:case
			case 25:
				global2._send('setScript:', placeHoleScr)
			#end:case
			case 1:
				global91._send(
					'say:', noun, param1, (cond
							case (not proc913_0(23)): 0#end:case
							case proc913_0(24): 11#end:case
							else: 10#end:else
						)
				)
			#end:case
			case 28:
				if (not proc913_0(23)):
					global91._send('say:', noun, param1, 4)
				else:
					magicDoor._send('doVerb:', param1)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genericFeatures(Feature):
	#property vars (may be empty)
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(= noun
				match kernel.OnControl(4, param1._send('x:'), param1._send('y:'))
					case 4: 9#end:case
					case 16: 8#end:case
					case 32: 11#end:case
					else: 0#end:else
				#end:match
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class vine(Feature):
	#property vars (may be empty)
	noun = 13
	onMeCheck = 256
	approachX = 200
	approachY = 81
	_approachVerbs = 8
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global2._send('setScript:', climbVineScr)
			#end:case
			else:
				super._send('doVerb:', param1)
			#end:else
		#end:match
	#end:method

#end:class or instance

