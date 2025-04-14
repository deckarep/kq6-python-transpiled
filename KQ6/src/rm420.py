#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 420
import sci_sh
import kernel
import Main
import rLab
import KQ6Room
import Conversation
import Scaler
import PolyPath
import Polygon
import Feature
import LoadMany
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm420 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class rm420(KQ6Room):
	#property vars (may be empty)
	noun = 2
	picture = 420
	style = 10
	walkOffEdge = 1
	
	@classmethod
	def init():
		global2._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 3,
					'init:', 194, 120, 122, 120, 116, 122, 54, 122, 50, 125, 110, 125, 96, 130, 96, 150, 221, 150, 220, 132, 204, 125, 245, 125, 243, 122, 198, 122,
					'yourself:'
				)
		)
		super._send('init:', &rest)
		proc958_0(128, 421)
		global0._send('init:', 'setScale:', Scaler, 100, 60, 128, 100, 'actions:', egoDoCrushCode)
		kernel.ScriptID(30, 0)._send('cue:')
		global32._send('add:', floor, walls, exits, 'eachElementDo:', #init)
		if local0 = (global9._send('at:', 2)._send('owner:') == global11):
			local1 = 5
			theBrick._send('addToPic:')
			gears._send('addToPic:')
			ceiling._send('addToPic:')
		else:
			local1 = 4
			eastDoor._send('init:')
			westDoor._send('init:')
			gears._send('init:', 'stopUpd:')
			ceiling._send('init:', 'stopUpd:')
		#endif
		if (not rLab._send('prevEdgeHit:')):
			rLab._send('prevEdgeHit:', 2)
		#endif
		self._send('setScript:', walkIn)
	#end:method

	@classmethod
	def doit():
		(cond
			case self._send('script:'):#end:case
			case (global0._send('onControl:', 1) == 16384):
				kernel.ScriptID(30, 0)._send('prevEdgeHit:', 2)
				self._send('setScript:', walkOut)
			#end:case
			case (global0._send('onControl:', 1) == 8192):
				kernel.ScriptID(30, 0)._send('prevEdgeHit:', 4)
				self._send('setScript:', walkOut)
			#end:case
		)
		super._send('doit:', &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		(return
			match param1
				case 1:
					global91._send('say:', 2, 1, local1, 1)
					1
				#end:case
				case 2:
					if local0:
						global91._send('say:', 2, 2, local1, 1)
						1
					else:
						myConv._send('add:', -1, 2, 2, local1, 1, 'add:', -1, 2, 2, local1, 2, 'init:')
						1
					#endif
				#end:case
				case 5:
					global91._send('say:', 2, 5, local1, 1)
					1
				#end:case
				else:
					global91._send('say:', 2, 0, local1, 1)
					1
				#end:else
			#end:match
		)
	#end:method

	@classmethod
	def scriptCheck():
		temp0 = 1
		if (not local0):
			global91._send('say:', 0, 0, 164, 1, 0, 899)
			temp0 = 0
		#endif
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class floor(Feature):
	#property vars (may be empty)
	noun = 8
	onMeCheck = 2048
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				global91._send('say:', 8, 5, local1, 1)
			#end:case
			case 1:
				global91._send('say:', 8, 1, 0, 1)
			#end:case
			case 2:
				global91._send('say:', 8, 2, local1, 0)
			#end:case
			else:
				global91._send('say:', 2, 0, local1, 1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walls(Feature):
	#property vars (may be empty)
	noun = 7
	onMeCheck = 1024
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				global91._send('say:', 7, 1, local1, 1)
			#end:case
			case 5:
				global91._send('say:', 7, 5, local1, 1)
			#end:case
			case 2:
				if local0:
					global91._send('say:', 2, 2, local1, 0)
				else:
					global91._send('say:', 7, 2, local1, 0)
				#endif
			#end:case
			else:
				global91._send('say:', 2, 0, local1, 1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class exits(Feature):
	#property vars (may be empty)
	onMeCheck = 4096
	
	@classmethod
	def doVerb(param1 = None, *rest):
		westDoor._send('doVerb:', param1, &rest)
	#end:method

#end:class or instance

@SCI.instance
class gears(Prop):
	#property vars (may be empty)
	x = 160
	y = 118
	noun = 6
	view = 424
	loop = 1
	signal = 16400
	cycleSpeed = 18
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				global91._send('say:', 6, 1, local1, 1)
			#end:case
			case 5:
				global91._send('say:', 6, 5, local1, 1)
			#end:case
			case 2:
				global91._send('say:', 6, 2, local1, 1)
			#end:case
			case 39:
				global2._send('setScript:', useBrick)
			#end:case
			case 51:
				if local0:
					global91._send('say:', 6, 0, local1, 1)
				else:
					global2._send('setScript:', throwSkull)
				#endif
			#end:case
			case 17:
				if local0:
					global91._send('say:', 6, 0, local1, 1)
				else:
					global91._send('say:', 6, 17, local1, 1)
				#endif
			#end:case
			case 28:
				if local0:
					global91._send('say:', 6, 0, local1, 1)
				else:
					global91._send('say:', 6, 28, local1, 1)
				#endif
			#end:case
			case 36:
				if local0:
					global91._send('say:', 6, 0, local1, 1)
				else:
					global91._send('say:', 6, 36, local1, 1)
				#endif
			#end:case
			case 42:
				if local0:
					global91._send('say:', 6, 0, local1, 1)
				else:
					global91._send('say:', 6, 42, local1, 1)
				#endif
			#end:case
			case 20:
				if local0:
					global91._send('say:', 6, 0, local1, 1)
				else:
					global91._send('say:', 6, 20, local1, 1)
				#endif
			#end:case
			case 34:
				if local0:
					global91._send('say:', 6, 0, local1, 1)
				else:
					global91._send('say:', 6, 34, local1, 1)
				#endif
			#end:case
			case 94:
				if local0:
					global91._send('say:', 6, 0, local1, 1)
				else:
					global91._send('say:', 6, 94, local1, 1)
				#endif
			#end:case
			else:
				global91._send('say:', 6, 0, local1, 1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class ceiling(Prop):
	#property vars (may be empty)
	x = 162
	y = 71
	noun = 4
	view = 424
	priority = 7
	signal = 20496
	cycleSpeed = 12
	
	@classmethod
	def addToPic():
		self._send(
			'y:', kernel.ScriptID(30, 0)._send('crushCeilingY:'),
			'cel:', kernel.ScriptID(30, 0)._send('crushCeilingCel:')
		)
		super._send('addToPic:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				global91._send('say:', 4, 1, local1, 1)
			#end:case
			case 5:
				global91._send('say:', 4, 5, local1, 1)
			#end:case
			case 2:
				global91._send('say:', 4, 2, local1, 1)
			#end:case
			case 51:
				if local0:
					global91._send('say:', 4, 0, local1, 1)
				else:
					global91._send('say:', 4, 51, local1, 1)
				#endif
			#end:case
			case 17:
				if local0:
					global91._send('say:', 4, 0, local1, 1)
				else:
					global91._send('say:', 4, 17, local1, 1)
				#endif
			#end:case
			case 28:
				if local0:
					global91._send('say:', 4, 0, local1, 1)
				else:
					global91._send('say:', 4, 28, local1, 1)
				#endif
			#end:case
			case 94:
				if local0:
					global91._send('say:', 4, 0, local1, 1)
				else:
					global91._send('say:', 4, 94, local1, 1)
				#endif
			#end:case
			case 12:
				global91._send('say:', 4, 12, 0, 1)
			#end:case
			else:
				global91._send('say:', 4, 0, local1, 1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class westDoor(Prop):
	#property vars (may be empty)
	x = 101
	y = 71
	noun = 5
	view = 424
	loop = 2
	signal = 20480
	cycleSpeed = 4
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				global91._send('say:', 5, 1, local1, 1)
			#end:case
			case 5:
				global91._send('say:', 5, 5, local1, 1)
			#end:case
			case 2:
				super._send('doVerb:', param1, &rest)
			#end:case
			else:
				global91._send('say:', 5, 0, local1, 1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class eastDoor(Prop):
	#property vars (may be empty)
	x = 211
	y = 70
	noun = 5
	view = 424
	loop = 3
	signal = 20480
	cycleSpeed = 3
	
	@classmethod
	def doVerb(param1 = None, *rest):
		westDoor._send('doVerb:', param1, &rest)
	#end:method

#end:class or instance

@SCI.instance
class theBrick(Prop):
	#property vars (may be empty)
	noun = 10
	view = 424
	loop = 5
	signal = 16384
	cycleSpeed = 1
	
	@classmethod
	def init():
		if (global9._send('at:', 2)._send('owner:') == global11):
			self._send('x:', 169, 'y:', 119, 'z:', 32)
		else:
			self._send('x:', 169, 'y:', 118)
		#endif
		super._send('init:')
	#end:method

#end:class or instance

@SCI.instance
class theSkull(Prop):
	#property vars (may be empty)
	x = 166
	y = 118
	view = 424
	loop = 4
	cycleSpeed = 1
	
#end:class or instance

@SCI.instance
class cog(Prop):
	#property vars (may be empty)
	x = 182
	y = 133
	view = 423
	signal = 16384
	cycleSpeed = 5
	
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
					case 2:
						global0._send('edgeHit:', 2, 'setMotion:', MoveTo, 232, 123, self)
					#end:case
					case 4:
						global0._send('edgeHit:', 4, 'setMotion:', MoveTo, 82, 123, self)
					#end:case
				#end:match
			#end:case
			case 1:
				global2._send('newRoom:', 400)
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
				global1._send('handsOff:')
				match rLab._send('prevEdgeHit:')
					case 4:
						global0._send('posn:', 232, 123, 'setMotion:', PolyPath, 194, 123, self)
					#end:case
					case 2:
						global0._send('posn:', 82, 123, 'setMotion:', PolyPath, 122, 123, self)
					#end:case
				#end:match
			#end:case
			case 1:
				if local0:
					global1._send('handsOn:')
					self._send('dispose:')
				else:
					global0._send('setPri:', 14, 'setMotion:', PolyPath, 152, 134, self)
				#endif
			#end:case
			case 2:
				global0._send('setHeading:', 90)
				eastDoor._send('setCycle:', End)
				westDoor._send('setCycle:', End, self)
				global105._send('number:', 426, 'setLoop:', 1, 'play:')
			#end:case
			case 3:
				global1._send('handsOn:')
				global69._send('enable:', 6, 'disable:', 0)
				global102._send('number:', 420, 'setLoop:', -1, 'play:', self)
				global103._send('number:', 421, 'setLoop:', -1, 'play:', self)
				ticks = 4
			#end:case
			case 4:
				eastDoor._send('stopUpd:')
				westDoor._send('stopUpd:')
				global91._send('say:', 1, 0, 1, 1, self)
			#end:case
			case 5:
				ceiling._send('startUpd:', 'y:', (ceiling._send('y:') + 1))
				gears._send('setCycle:', Fwd)
				cycles = 4
			#end:case
			case 6:
				global91._send('say:', 1, 0, 1, 2, self)
			#end:case
			case 7:
				self._send('setScript:', dropCeiling, self, 1)
			#end:case
			case 8:
				ceiling._send('stopUpd:')
				seconds = 1
			#end:case
			case 9:
				global2._send('setScript:', sqwishEm)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class dropCeiling(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				ceiling._send('startUpd:', 'y:', (ceiling._send('y:') + 1))
				seconds = 2
			#end:case
			case 1:
				if (register == 1):
					temp0 = 85
				else:
					temp0 = 91
				#endif
				if (ceiling._send('y:') < temp0):
					self._send('changeState:', 0)
				else:
					self._send('dispose:')
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class throwSkull(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global91._send('say:', 6, 51, 4, 1, self)
			#end:case
			case 1:
				global0._send('view:', 421, 'normal:', 0, 'setLoop:', 1, 'cel:', 4, 'posn:', 162, 146)
				ticks = 4
			#end:case
			case 2:
				global0._send('cel:', 5)
				theSkull._send('init:')
				ticks = 4
			#end:case
			case 3:
				global0._send('cel:', 6)
				ticks = 4
			#end:case
			case 4:
				global0._send('cel:', 7)
				theSkull._send('posn:', 161, 124)
				theSkull._send('posn:', (theSkull._send('x:') - 8), (theSkull._send('y:') + 6))
				ticks = 4
			#end:case
			case 5:
				global0._send('cel:', 8)
				theSkull._send(
					'setPri:', 11,
					'posn:', (theSkull._send('x:') - 10), (theSkull._send('y:') - 3)
				)
				ticks = 4
			#end:case
			case 6:
				global0._send('cel:', 9)
				theSkull._send(
					'setPri:', -1,
					'posn:', (theSkull._send('x:') + 26), (theSkull._send('y:') - 3)
				)
				ticks = 4
			#end:case
			case 7:
				global0._send('cel:', 10)
				theSkull._send('posn:', (theSkull._send('x:') - 5), (theSkull._send('y:') - 18))
				ticks = 2
			#end:case
			case 8:
				theSkull._send('cel:', 1, 'posn:', (theSkull._send('x:') + 1), (theSkull._send('y:') - 6))
				ticks = 2
			#end:case
			case 9:
				theSkull._send('cel:', 2, 'posn:', (theSkull._send('x:') + 1), (theSkull._send('y:') - 5))
				ticks = 2
			#end:case
			case 10:
				theSkull._send('cel:', 3, 'posn:', (theSkull._send('x:') + 1), (theSkull._send('y:') - 7))
				ticks = 2
			#end:case
			case 11:
				theSkull._send('cel:', 0, 'posn:', (theSkull._send('x:') + 1), (theSkull._send('y:') - 5))
				ticks = 2
			#end:case
			case 12:
				theSkull._send('cel:', 1, 'posn:', (theSkull._send('x:') + 1), (theSkull._send('y:') + 2))
				ticks = 2
			#end:case
			case 13:
				theSkull._send('cel:', 2, 'posn:', (theSkull._send('x:') + 1), (theSkull._send('y:') + 2))
				ticks = 2
			#end:case
			case 14:
				theSkull._send('cel:', 3, 'posn:', (theSkull._send('x:') + 1), (theSkull._send('y:') + 1))
				ticks = 2
			#end:case
			case 15:
				global102._send('stop:')
				global103._send('stop:')
				global105._send('number:', 422, 'setLoop:', 1, 'play:', self)
				global104._send('number:', 424, 'setLoop:', 1, 'play:')
				theSkull._send('cel:', 0, 'posn:', (theSkull._send('x:') + 1), (theSkull._send('y:') + 4))
			#end:case
			case 16:
				theSkull._send('posn:', (theSkull._send('x:') - 1), (theSkull._send('y:') - 1))
				global91._send('say:', 6, 51, 4, 2, self)
			#end:case
			case 17:
				gears._send('setCycle:', 0, 'stopUpd:')
				global0._send('reset:', 0, 'posn:', 155, 134)
				global91._send('say:', 6, 51, 4, 3, self)
			#end:case
			case 18:
				global91._send('say:', 6, 51, 4, 4, self)
			#end:case
			case 19:
				seconds = 2
			#end:case
			case 20:
				theSkull._send('setLoop:', 6, 'setCycle:', End, self)
				global105._send('number:', 423, 'setLoop:', 1, 'play:', self)
			#end:case
			case 21:
				global102._send('number:', 420, 'setLoop:', -1, 'play:', self)
				global103._send('number:', 421, 'setLoop:', -1, 'play:', self)
			#end:case
			case 22:
				gears._send('setCycle:', Fwd)
				global91._send('say:', 6, 51, 4, 5, self)
			#end:case
			case 23:
				theSkull._send('dispose:')
				global69._send('disable:', 0)
				global0._send('put:', 11, global11)
				ceiling._send('y:', 84)
				seconds = 2
			#end:case
			case 24:
				global2._send('setScript:', sqwishEm, 0, 1)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class sqwishEm(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global91._send('say:', 1, 0, 3, 1, self)
			#end:case
			case 1:
				ceiling._send('setPri:', 12, 'setCycle:', CT, 3, 1, self)
				global0._send(
					'view:', 421,
					'normal:', 0,
					'setLoop:', 2,
					'cel:', 0,
					'cycleSpeed:', 6,
					'setPri:', 14,
					'posn:', (global0._send('x:') - 2), (global0._send('y:') + 4),
					'setCycle:', End, self
				)
			#end:case
			case 2:
				ceiling._send('cel:', (ceiling._send('cel:') + 1))
				global0._send('setPri:', 13, 'setLoop:', 3, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 3:
				ceiling._send('cel:', (ceiling._send('cel:') + 1))
				global0._send('setLoop:', 4, 'cel:', 0, 'setCycle:', CT, 4, 1, self)
			#end:case
			case 4:
				global91._send('say:', 1, 0, 3, 2, self)
			#end:case
			case 5:
				ceiling._send('setPri:', 14, 'cel:', (ceiling._send('cel:') + 1))
				global0._send('setCycle:', CT, 7, 1, self)
			#end:case
			case 6:
				ceiling._send('cel:', (ceiling._send('cel:') + 1))
				global0._send('setCycle:', CT, 8, 1, self)
			#end:case
			case 7:
				global91._send('say:', 1, 0, 3, 3, self)
			#end:case
			case 8:
				ceiling._send('setCycle:', End, self)
			#end:case
			case 9:
				global102._send('stop:')
				global103._send('stop:')
				global105._send('number:', 425, 'setLoop:', 1, 'play:')
				cycles = 6
			#end:case
			case 10:
				ceiling._send('stopUpd:')
				if register:
					global91._send('say:', 6, 51, 4, 6, self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 11:
				global1._send('handsOn:')
				proc0_1(9)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class useBrick(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global91._send('say:', 6, 39, 0, 1, self)
			#end:case
			case 1:
				global0._send('view:', 421, 'normal:', 0, 'setLoop:', 0, 'cel:', 4, 'posn:', 162, 146)
				ticks = 2
			#end:case
			case 2:
				global0._send('cel:', 5)
				theBrick._send('init:')
				ticks = 2
			#end:case
			case 3:
				global0._send('cel:', 6)
				theBrick._send('posn:', (theBrick._send('x:') - 2), (theBrick._send('y:') - 4))
				ticks = 2
			#end:case
			case 4:
				global0._send('cel:', 7)
				theBrick._send('posn:', (theBrick._send('x:') - 10), (theBrick._send('y:') + 8))
				ticks = 2
			#end:case
			case 5:
				global0._send('cel:', 8)
				theBrick._send(
					'setPri:', 11,
					'posn:', (theBrick._send('x:') - 7), (theBrick._send('y:') - 3)
				)
				ticks = 2
			#end:case
			case 6:
				global0._send('cel:', 9)
				theBrick._send(
					'setPri:', -1,
					'posn:', (theBrick._send('x:') + 24), (theBrick._send('y:') - 1)
				)
				ticks = 2
			#end:case
			case 7:
				global0._send('cel:', 10)
				theBrick._send('posn:', (theBrick._send('x:') - 4), (theBrick._send('y:') - 19))
				ticks = 2
			#end:case
			case 8:
				theBrick._send('cel:', 1, 'posn:', (theBrick._send('x:') + 1), (theBrick._send('y:') - 6))
				ticks = 2
			#end:case
			case 9:
				theBrick._send('cel:', 2, 'posn:', theBrick._send('x:'), (theBrick._send('y:') - 5))
				ticks = 2
			#end:case
			case 10:
				theBrick._send('cel:', 3, 'posn:', theBrick._send('x:'), (theBrick._send('y:') - 6))
				ticks = 2
			#end:case
			case 11:
				theBrick._send('cel:', 0, 'posn:', theBrick._send('x:'), (theBrick._send('y:') - 4))
				ticks = 2
			#end:case
			case 12:
				theBrick._send('cel:', 1, 'posn:', theBrick._send('x:'), (theBrick._send('y:') + 3))
				ticks = 2
			#end:case
			case 13:
				theBrick._send('cel:', 2, 'posn:', theBrick._send('x:'), (theBrick._send('y:') + 3))
				ticks = 2
			#end:case
			case 14:
				theBrick._send('cel:', 3, 'posn:', theBrick._send('x:'), (theBrick._send('y:') + 2))
				ticks = 2
			#end:case
			case 15:
				global102._send('stop:')
				global103._send('stop:')
				global105._send('number:', 422, 'setLoop:', 1, 'play:', self)
				global104._send('number:', 424, 'setLoop:', 1, 'play:')
				theBrick._send('cel:', 0, 'posn:', theBrick._send('x:'), (theBrick._send('y:') + 2))
			#end:case
			case 16:
				theBrick._send('x:', 169, 'y:', 119, 'z:', 32, 'stopUpd:')
				global91._send('say:', 6, 39, 0, 2, self)
			#end:case
			case 17:
				gears._send('setCycle:', 0, 'stopUpd:')
				cog._send('init:', 'setCycle:', End, self)
				global0._send('reset:', 0, 'posn:', 155, 134)
			#end:case
			case 18:
				global91._send('say:', 6, 39, 0, 3, self)
			#end:case
			case 19:
				global1._send('givePoints:', 2)
				cog._send('dispose:')
				global105._send('number:', 426, 'setLoop:', 1, 'play:')
				eastDoor._send('setCycle:', Beg)
				westDoor._send('setCycle:', Beg, self)
			#end:case
			case 20:
				global91._send('say:', 6, 39, 0, 4, self)
			#end:case
			case 21:
				kernel.ScriptID(30, 0)._send('crushCeilingCel:', ceiling._send('cel:'))
				kernel.ScriptID(30, 0)._send('crushCeilingY:', ceiling._send('y:'))
				local0 = 1
				local1 = 5
				ceiling._send('stopUpd:')
				global102._send('number:', 400, 'play:')
				global1._send('handsOn:')
				global0._send('put:', 2, global11)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoDoCrushCode(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 17:
				global91._send('say:', 3, 17, local1, 1)
				return 1
			#end:case
			case 12:
				global91._send('say:', 3, 12, 0, 1)
				return 1
			#end:case
			else:
				return 0
			#end:else
		#end:match
	#end:method

#end:class or instance

