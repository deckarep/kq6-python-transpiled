#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 650
import sci_sh
import kernel
import Main
import rgDead
import KQ6Room
import Inset
import Scaler
import RandCycle
import PolyPath
import Polygon
import Feature
import Sound
import Jump
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm650 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = [158, 52, 0, 299, 58, 1, 113, 82, 2, 65, 87, 3, 49, 87, 4, 0]
local16 = None
local17 = None
local18 = None
local19 = None


@SCI.instance
class rm650(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 650
	horizon = 88
	north = 660
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global2._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 105, 189, 105, 178, 253, 178, 267, 151, 267, 112, 253, 109, 199, 108, 123, 108, 77, 112, 52, 106, 52, 0, 319, 0, 319, 189,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 0, 168, 0, 0, 43, 0, 43, 104, 57, 112, 87, 115, 122, 110, 210, 110, 251, 113, 265, 117, 265, 137, 152, 168,
					'yourself:'
				)
		)
		super._send('init:', &rest)
		match global12
			case 660:
				global0._send('posn:', 79, 113)
				local18 = 1
			#end:case
			else:
				global102._send('number:', 650, 'loop:', -1, 'play:')
				global0._send('posn:', 47, 172)
			#end:else
		#end:match
		proc70_1(flames, @local0)
		glow1._send('init:', 'setCycle:', RandCycle)
		glow2._send('init:', 'setCycle:', RandCycle)
		riverStyx._send('init:')
		fallFeat._send('init:')
		knight._send('init:')
		global0._send(
			'init:',
			'baseSetter:', bSetter,
			'observeControl:', -32768,
			'setScale:', Scaler, 100, 65, 150, 100
		)
		path._send('init:')
		global1._send('handsOn:')
		ghost._send('init:', 'hide:', 'setScript:', ghostScript)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('doit:')
		temp0 = global0._send('onControl:', 1)
		(cond
			case script: 0#end:case
			case (global0._send('y:') >= 186):
				global1._send('handsOff:')
				self._send('setScript:', cantLeaveSouth)
			#end:case
			case (global0._send('x:') <= 5):
				global1._send('handsOff:')
				self._send('setScript:', cantLeaveWest)
			#end:case
			case (temp0 & 0x0800):
				if 
					(and
						(not global0._send('isStopped:'))
						(or
							(global0._send('mover:')._send('y:') < global0._send('y:'))
							proc999_5(global0._send('loop:'), 3, 6, 7)
						)
					)
					self._send('setScript:', egoNorthOverKnightScr)
				#endif
			#end:case
			case (temp0 & 0x0002):
				if 
					(and
						local18
						(not global0._send('isStopped:'))
						(or
							(global0._send('mover:')._send('y:') > global0._send('y:'))
							proc999_5(global0._send('loop:'), 2, 4, 5)
						)
					)
					self._send('setScript:', egoSouthOverKnightScr)
				#endif
			#end:case
			case (temp0 & 0x1000):
				self._send('newRoom:', north)
			#end:case
			case (not ((temp0 & 0x4000) or (temp0 & 0x2000) or (temp0 & 0x0002))):
				global1._send('handsOff:')
				self._send('setScript:', egoFallScr)
			#end:case
		)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('dispose:')
		kernel.DisposeScript(991)
	#end:method

#end:class or instance

@SCI.instance
class egoNorthOverKnightScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if (global0._send('mover:') and global0._send('mover:')._send('isKindOf:', PolyPath)):
					local16 = global0._send('mover:')._send('finalX:')
					local17 = global0._send('mover:')._send('finalY:')
				#endif
				global1._send('handsOff:')
				global0._send(
					'normal:', 0,
					'view:', 652,
					'loop:', 2,
					'cel:', 3,
					'posn:', (global0._send('x:') + 1), (global0._send('y:') + 5),
					'setPri:', 9
				)
				cycles = 1
			#end:case
			case 1:
				global0._send('setCycle:', CT, 7, 1, self)
			#end:case
			case 2:
				global0._send('setPri:', 8, 'x:', (global0._send('x:') + 2), 'setCycle:', End, self)
			#end:case
			case 3:
				global0._send('posn:', (global0._send('x:') - 2), (global0._send('y:') - 11), 'reset:', 3)
				cycles = 2
			#end:case
			case 4:
				if 
					(and
						local16
						(>
							kernel.GetDistance(local16, local17, global0._send('x:'), global0._send(
								'y:'
							))
							20
						)
					)
					global0._send('setMotion:', PolyPath, local16, local17)
					local16 = 0
				#endif
				global1._send('handsOn:')
				local18 = 1
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoSouthOverKnightScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if (global0._send('mover:') and global0._send('mover:')._send('isKindOf:', PolyPath)):
					local16 = global0._send('mover:')._send('finalX:')
					local17 = global0._send('mover:')._send('finalY:')
				#endif
				global1._send('handsOff:')
				cycles = 2
			#end:case
			case 1:
				global0._send(
					'setLoop:', 2,
					'setCycle:', 0,
					'setPri:', 9,
					'setMotion:', JumpTo, 261, 137, self
				)
			#end:case
			case 2:
				global0._send('reset:')
				local18 = 0
				if 
					(and
						local16
						(>
							kernel.GetDistance(local16, local17, global0._send('x:'), global0._send(
								'y:'
							))
							20
						)
					)
					global0._send('setMotion:', PolyPath, local16, local17)
					local16 = 0
				#endif
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoFallScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if (global0._send('y:') < 124):
					register = 1
					global0._send('setMotion:', PolyPath, 163, 108, self)
				else:
					register = 0
					global0._send('setMotion:', PolyPath, 119, 168, self)
				#endif
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				global91._send('say:', 3, 3, 3, 1, self)
			#end:case
			case 3:
				global102._send('stop:')
				global102._send('number:', 653, 'loop:', 1, 'play:')
				if register:
					global0._send(
						'normal:', 0,
						'view:', 653,
						'setLoop:', 0,
						'cel:', 0,
						'cycleSpeed:', 5,
						'setCycle:', End, self
					)
				else:
					global0._send(
						'normal:', 0,
						'view:', 653,
						'setLoop:', 1,
						'cel:', 0,
						'setPri:', 8,
						'cycleSpeed:', 5,
						'setCycle:', End, self
					)
				#endif
			#end:case
			case 4:
				global0._send('dispose:')
				splashSound._send('play:', self)
			#end:case
			case 5:
				global91._send('say:', 3, 3, 3, 2, self)
			#end:case
			case 6:
				proc0_1(31)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class splashSound(Sound):
	#property vars (may be empty)
	number = 923
	
#end:class or instance

@SCI.instance
class flames(Prop):
	#property vars (may be empty)
	noun = 12
	view = 650
	priority = 3
	signal = 16400
	
#end:class or instance

@SCI.instance
class glow1(Prop):
	#property vars (may be empty)
	x = 299
	y = 51
	view = 650
	loop = 6
	priority = 2
	signal = 16400
	
#end:class or instance

@SCI.instance
class glow2(Prop):
	#property vars (may be empty)
	x = 65
	y = 84
	view = 650
	loop = 7
	priority = 2
	signal = 16400
	
#end:class or instance

@SCI.instance
class knightInset(Inset):
	#property vars (may be empty)
	view = 652
	x = 228
	y = 112
	disposeNotOnMe = 1
	noun = 8
	
	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case ribbonFeat._send('onMe:', param1):
				ribbonFeat._send('handleEvent:', param1)
			#end:case
			case handFeat._send('onMe:', param1):
				handFeat._send('handleEvent:', param1)
			#end:case
			case knightFeat._send('onMe:', param1):
				knightFeat._send('handleEvent:', param1)
			#end:case
			case knightInsetFeat._send('onMe:', param1):
				knightInsetFeat._send('handleEvent:', param1)
			#end:case
			else:
				super._send('handleEvent:', param1)
			#end:else
		)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global69._send('disable:', 6)
		knightInsetFeat._send('init:')
		knightFeat._send('init:')
		ribbonFeat._send('init:')
		handFeat._send('init:')
		super._send('init:', &rest)
		if (global9._send('at:', 15)._send('owner:') == global11):
			gauntlet._send('init:')
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		ribbonFeat._send('dispose:')
		knightFeat._send('dispose:')
		knightInsetFeat._send('dispose:')
		handFeat._send('dispose:')
		super._send('dispose:')
		global69._send('enable:', 6)
	#end:method

#end:class or instance

@SCI.instance
class getGauntletScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				knightInset._send('dispose:')
				global0._send('reset:', 0)
				seconds = 2
			#end:case
			case 1:
				global0._send('setMotion:', PolyPath, 267, 130, self)
			#end:case
			case 2:
				global0._send(
					'normal:', 0,
					'view:', 652,
					'loop:', 1,
					'cycleSpeed:', 6,
					'cel:', 0,
					'posn:', 277, 131,
					'setCycle:', End, self
				)
				scrape._send('play:')
			#end:case
			case 3:
				global0._send('reset:', 0, 'posn:', 267, 130, 'get:', 15)
				cycles = 2
			#end:case
			case 4:
				global1._send('givePoints:', 1)
				global91._send('say:', 6, 5, 0, 0, self)
			#end:case
			case 5:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class scrape(Sound):
	#property vars (may be empty)
	number = 652
	
#end:class or instance

@SCI.instance
class gauntlet(Prop):
	#property vars (may be empty)
	x = 198
	y = 120
	noun = 6
	view = 652
	cel = 1
	priority = 15
	signal = 16
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global2._send('setScript:', getGauntletScr)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class knightGhost(Prop):
	#property vars (may be empty)
	x = 249
	y = 145
	view = 651
	priority = 9
	signal = 16
	
#end:class or instance

@SCI.instance
class ghost(Prop):
	#property vars (may be empty)
	x = 95
	y = 112
	noun = 10
	view = 650
	loop = 5
	priority = 8
	signal = 16
	cycleSpeed = 7
	
#end:class or instance

@SCI.instance
class ghostScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				cycles = kernel.Random(90, 300)
			#end:case
			case 1:
				ghost._send('show:', 'setCycle:', End, self)
			#end:case
			case 2:
				ghost._send('hide:')
				cycles = 1
			#end:case
			case 3:
				self._send('init:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class ghostTormentScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if (client == global2):
					global0._send('setMotion:', 0, 'setHeading:', 45)
				#endif
				global102._send('number:', 651, 'loop:', 1, 'play:')
				kernel.ScriptID(70, 0)._send('setIt:', 4)
				knightGhost._send('init:', 'cycleSpeed:', 10, 'setCycle:', End, self)
			#end:case
			case 1:
				global0._send('hide:')
				knightGhost._send('loop:', 1, 'cel:', 0, 'setPri:', -1, 'setCycle:', End, self)
			#end:case
			case 2:
				global0._send('show:')
				knightGhost._send(
					'loop:', 2,
					'cel:', 0,
					'posn:', 201, 127,
					'setPri:', 4,
					'setCycle:', End, self
				)
			#end:case
			case 3:
				global102._send('stop:')
				global102._send('number:', 650, 'loop:', -1, 'play:')
				knightGhost._send('dispose:')
				seconds = 2
			#end:case
			case 4:
				global91._send('say:', 1, 0, 4, 1, self)
			#end:case
			case 5:
				if (client == global2):
					global1._send('handsOn:')
				#endif
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class knightInsetScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global0._send(
					'setMotion:', PolyPath, knight._send('approachX:'), knight._send(
							'approachY:'
						), self
				)
			#end:case
			case 1:
				if (not kernel.ScriptID(70, 0)._send('isSet:', 4)):
					self._send('setScript:', ghostTormentScr, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				global0._send('setHeading:', 90, self)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				global1._send('handsOn:')
				global69._send('disable:', 0, 3, 4, 5)
				knightInset._send('init:', self, global2)
			#end:case
			case 5:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class knight(Feature):
	#property vars (may be empty)
	x = 300
	y = 128
	noun = 4
	sightAngle = 40
	onMeCheck = 2
	approachX = 251
	approachY = 147
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc999_5(param1, 5, 1):
			global1._send('handsOff:')
			global2._send('setScript:', knightInsetScr)
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class fallFeat(Feature):
	#property vars (may be empty)
	onMeCheck = 128
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 3):
			global1._send('handsOff:')
			global2._send('setScript:', egoFallScr)
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:')
		global93._send('addToFront:', self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global93._send('delete:', self)
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class riverStyx(Feature):
	#property vars (may be empty)
	noun = 9
	onMeCheck = 4
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 3):
			global1._send('handsOff:')
			global2._send('setScript:', egoFallScr)
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:')
		global93._send('addToFront:', self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global93._send('delete:', self)
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class bSetter(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		param1._send('brTop:', param1._send('y:'))
		param1._send('brBottom:', param1._send('y:'))
		param1._send('brLeft:', param1._send('x:'))
		param1._send('brRight:', param1._send('x:'))
	#end:method

#end:class or instance

@SCI.instance
class path(Feature):
	#property vars (may be empty)
	noun = 13
	onMeCheck = 16384
	
#end:class or instance

@SCI.instance
class cantLeaveSouth(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global91._send('say:', 3, 3, 2, 0, self)
			#end:case
			case 1:
				global0._send(
					'setMotion:', MoveTo, (global0._send('x:') + 3), (-
							global0._send('y:')
							10
						), self
				)
			#end:case
			case 2:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class cantLeaveWest(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global91._send('say:', 3, 3, 2, 0, self)
			#end:case
			case 1:
				global0._send(
					'setMotion:', MoveTo, (global0._send('x:') + 10), (-
							global0._send('y:')
							3
						), self
				)
			#end:case
			case 2:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class knightInsetFeat(Feature):
	#property vars (may be empty)
	noun = 8
	nsTop = 62
	nsLeft = 154
	nsBottom = 155
	nsRight = 307
	
#end:class or instance

@SCI.instance
class ribbonFeat(Feature):
	#property vars (may be empty)
	noun = 7
	nsTop = 99
	nsLeft = 232
	nsBottom = 107
	nsRight = 248
	
#end:class or instance

@SCI.instance
class handFeat(Feature):
	#property vars (may be empty)
	noun = 11
	nsTop = 114
	nsLeft = 187
	nsBottom = 130
	nsRight = 212
	
#end:class or instance

@SCI.instance
class knightFeat(Feature):
	#property vars (may be empty)
	noun = 5
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(= onMeCheck
			(= local19
				Polygon._send('new:')._send(
					'type:', 0,
					'init:', 298, 68, 298, 81, 290, 91, 303, 103, 304, 118, 282, 151, 267, 153, 280, 124, 265, 129, 256, 152, 234, 152, 237, 142, 218, 133, 157, 141, 156, 127, 230, 110, 253, 86, 269, 89, 275, 68,
					'yourself:'
				)
			)
		)
		super._send('init:', &rest)
	#end:method

#end:class or instance

