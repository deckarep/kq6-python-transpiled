#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 407
import sci_sh
import kernel
import Main
import rLab
import n401
import n913
import PolyPath
import Feature
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm407 = 0,
)

@SCI.instance
class rm407(LabRoom):
	#property vars (may be empty)
	west = 400
	
	@classmethod
	def cue():
		global1._send('handsOff:')
		global2._send('setScript:', emptyHandedDeath)
	#end:method

	@classmethod
	def init():
		proc401_2()
		super._send('init:', &rest)
		hiwEastWall._send('init:')
		if ((not proc913_0(1)) and (not rLab._send('seenSecretLatch:'))):
			global2._send('setScript:', holeInWallEntry)
		else:
			kernel.ScriptID(30, 0)._send('cue:')
			global2._send('setScript:', kernel.ScriptID(30, 1))
		#endif
		kernel.ScriptID(30, 0)._send('initCrypt:', 1)
		kernel.ScriptID(30, 5)._send('addToPic:')
		kernel.ScriptID(30, 9)._send('addToPic:')
		kernel.ScriptID(30, 8)._send('addToPic:')
	#end:method

	@classmethod
	def notify():
		kernel.ScriptID(30, 5)._send('addToPic:')
		kernel.ScriptID(30, 9)._send('addToPic:')
		kernel.ScriptID(30, 8)._send('addToPic:')
		kernel.ScriptID(30, 3)._send('show:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				global91._send('say:', 2, 1, 44, 1, 0, 400)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class holeInset(View):
	#property vars (may be empty)
	x = 159
	y = 190
	z = 85
	view = 487
	priority = 15
	signal = 24592
	
#end:class or instance

@SCI.instance
class holeRoom(View):
	#property vars (may be empty)
	x = 159
	y = 139
	view = 414
	priority = 12
	signal = 24592
	
#end:class or instance

@SCI.instance
class tapestry(View):
	#property vars (may be empty)
	x = 158
	y = 135
	view = 414
	loop = 1
	priority = 13
	signal = 24592
	
#end:class or instance

@SCI.instance
class sDoor(Prop):
	#property vars (may be empty)
	x = 204
	y = 96
	view = 414
	loop = 4
	priority = 13
	signal = 24592
	cycleSpeed = 3
	
#end:class or instance

@SCI.instance
class minoInset(Prop):
	#property vars (may be empty)
	x = 158
	y = 135
	view = 414
	loop = 2
	priority = 14
	signal = 24592
	cycleSpeed = 3
	
#end:class or instance

@SCI.instance
class tapeMove(Prop):
	#property vars (may be empty)
	x = 158
	y = 135
	view = 414
	loop = 3
	priority = 13
	signal = 24592
	cycleSpeed = 3
	
#end:class or instance

@SCI.instance
class mino(Actor):
	#property vars (may be empty)
	x = 5
	y = 158
	yStep = 3
	view = 443
	signal = 16384
	xStep = 5
	
#end:class or instance

@SCI.instance
class theHole(Actor):
	#property vars (may be empty)
	x = 261
	y = 164
	z = 50
	noun = 17
	modNum = 400
	view = 232
	loop = 6
	signal = 26640
	moveSpeed = 3
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				holeTimer._send('dispose:')
				global2._send('setScript:', lookInHole)
			#end:case
			case 2:
				global91._send('say:', 17, 2, 0, 1, 0, 400)
			#end:case
			case 5:
				global2._send('setScript:', getTheHole)
			#end:case
			else:
				global91._send('say:', 17, 0, 0, 1, 0, 400)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class hiwEastWall(Feature):
	#property vars (may be empty)
	x = 255
	y = 155
	noun = 16
	modNum = 400
	approachX = 242
	approachY = 162
	
	@classmethod
	def init():
		self._send('approachVerbs:', 5, 'setOnMeCheck:', 1, 1024, 16384)
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 25:
				global2._send('setScript:', putHoleOnWall, 0, 1)
			#end:case
			case 1:
				if rLab._send('seenSecretLatch:'):
					global91._send('say:', 16, 1, 46, 1, 0, 400)
				else:
					global91._send('say:', 16, 1, 45, 0, 0, 400)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class holeInWallEntry(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('posn:', 36, 158, 'init:', 'setMotion:', PolyPath, 73, 158, self)
			#end:case
			case 1:
				kernel.ScriptID(30, 0)._send('cue:')
				global69._send('enable:', 6)
				global105._send('number:', 401, 'setLoop:', 1, 'play:', self)
			#end:case
			case 2:
				(cond
					case (rLab._send('timesInHoleWallRoom:') == 0):
						global91._send('say:', 1, 0, 39, 0, self, 400)
					#end:case
					case global0._send('has:', 18):
						global91._send('say:', 1, 0, 41, 1, self, 400)
					#end:case
					case (not rLab._send('seenSecretLatch:')):
						global91._send('say:', 1, 0, 39, 1, self, 400)
					#end:case
					else:
						self._send('cue:')
					#end:else
				)
			#end:case
			case 3:
				if 
					(and
						(not kernel.ScriptID(30, 0)._send('holeIsUp:'))
						(not global0._send('has:', 18))
						(not rLab._send('seenSecretLatch:'))
					)
					global2._send('setScript:', emptyHandedDeath)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 4:
				if (rLab._send('timesInHoleWallRoom:') == 0):
					rLab._send('timesInHoleWallRoom:', 1)
				#endif
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class emptyHandedDeath(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('reset:', 'setMotion:', PolyPath, 160, 160, self)
			#end:case
			case 1:
				global105._send('number:', 401, 'setLoop:', 1, 'play:', self)
			#end:case
			case 2:
				global91._send('say:', 1, 0, 40, 1, self, 400)
			#end:case
			case 3:
				seconds = 3
			#end:case
			case 4:
				if (global0._send('heading:') != 180):
					global0._send('setHeading:', 180)
				#endif
				cycles = 12
			#end:case
			case 5:
				global105._send('number:', 401, 'setLoop:', 1, 'play:', self)
			#end:case
			case 6:
				global91._send('say:', 1, 0, 40, 2, self, 400)
			#end:case
			case 7:
				seconds = 3
			#end:case
			case 8:
				global0._send('setHeading:', 270)
				cycles = 12
			#end:case
			case 9:
				global105._send('number:', 401, 'setLoop:', 1, 'play:', self)
			#end:case
			case 10:
				global91._send('say:', 1, 0, 40, 3, self, 400)
			#end:case
			case 11:
				global91._send('say:', 1, 0, 40, 4, self, 400)
			#end:case
			case 12:
				global105._send('number:', 401, 'setLoop:', 1, 'play:')
				global102._send('number:', 407, 'setLoop:', 1, 'play:')
				mino._send('init:', 'setCycle:', Walk, 'setMotion:', PolyPath, 84, 158, self)
			#end:case
			case 13:
				global91._send('say:', 1, 0, 40, 5, self, 400)
			#end:case
			case 14:
				global0._send(
					'view:', 413,
					'setStep:', 2, 1,
					'setLoop:', 0,
					'normal:', 0,
					'setCycle:', Fwd,
					'cycleSpeed:', 1,
					'setMotion:', MoveTo, 160, 144, self
				)
				mino._send('setMotion:', PolyPath, 160, 160, self)
				global105._send('number:', 401, 'setLoop:', 1, 'play:')
			#end:case
			case 15:
				global0._send('setCycle:', 0)
			#end:case
			case 16:
				global105._send('stop:')
				mino._send('setHeading:', 0)
				cycles = 6
			#end:case
			case 17:
				global91._send('say:', 1, 0, 40, 6, self, 400)
			#end:case
			case 18:
				global105._send('number:', 401, 'setLoop:', 1, 'play:')
				mino._send('setMotion:', PolyPath, 159, 149, self)
			#end:case
			case 19:
				global105._send('stop:')
				global0._send(
					'setLoop:', 2,
					'cel:', 0,
					'posn:', 159, 149,
					'cycleSpeed:', 3,
					'setCycle:', CT, 2, 1, self
				)
				mino._send('dispose:')
			#end:case
			case 20:
				global0._send('setCycle:', End, self)
				global102._send('stop:')
				global105._send('number:', 402, 'setLoop:', 1, 'play:')
			#end:case
			case 21:
				global105._send('number:', 960, 'setLoop:', 1, 'play:')
				cycles = 6
			#end:case
			case 22:
				if global5._send('contains:', theHole):
					proc0_1(28)
				else:
					proc0_1(27)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class putHoleOnWall(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('put:', 18, global11)
				global1._send('handsOff:')
				global2._send('style:', 100)
				global0._send('setMotion:', PolyPath, 242, 162, self)
			#end:case
			case 1:
				global0._send(
					'view:', 232,
					'setLoop:', 0,
					'normal:', 0,
					'posn:', 254, 162,
					'setCycle:', CT, 5, 1, self
				)
			#end:case
			case 2:
				global0._send('cel:', 6)
				if (not proc913_0(114)):
					proc913_1(114)
					global1._send('givePoints:', 1)
				#endif
				theHole._send('init:')
				global91._send('say:', 16, 25, 0, 0, self, 400)
			#end:case
			case 3:
				global0._send(
					'posn:', 242, 162,
					'reset:', 0,
					'setLoop:', global0._send('cel:'),
					'setMotion:', MoveTo, 225, 162, self
				)
			#end:case
			case 4:
				global0._send('setLoop:', -1)
				if (register == 1):
					global0._send('setScript:', holeTimer)
					global1._send('handsOn:')
					self._send('dispose:')
				else:
					client._send('setScript:', emptyHandedDeath)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getTheHole(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setScript:', 0, 'setMotion:', PolyPath, 242, 162, self)
			#end:case
			case 1:
				global0._send('setHeading:', 45)
				cycles = 6
			#end:case
			case 2:
				global0._send('view:', 232, 'normal:', 0, 'setLoop:', 0, 'posn:', 254, 162, 'cel:', 6)
				cycles = 3
			#end:case
			case 3:
				theHole._send('dispose:')
				global0._send('cycleSpeed:', 6, 'setCycle:', Beg, self)
			#end:case
			case 4:
				global0._send('posn:', 242, 162, 'reset:', 6)
				cycles = 8
			#end:case
			case 5:
				global0._send('setLoop:', global0._send('cel:'), 'setMotion:', MoveTo, 225, 162, self)
			#end:case
			case 6:
				global1._send('handsOn:')
				global0._send('setLoop:', -1, 'get:', 18)
				kernel.ScriptID(30, 0)._send('holeCoords:', 0)
				kernel.ScriptID(30, 0)._send('holeWall:', 0)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lookInHole(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 234, 162, self)
			#end:case
			case 1:
				global0._send(
					'view:', 232,
					'setLoop:', 3,
					'cel:', 0,
					'normal:', 0,
					'posn:', 246, 163,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				global91._send('say:', 17, 1, 47, 1, self, 400)
			#end:case
			case 3:
				global91._send('say:', 17, 1, 47, 2, self, 400)
			#end:case
			case 4:
				global1._send('givePoints:', 1)
				self._send('setScript:', holie, self)
			#end:case
			case 5:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 6:
				global0._send('posn:', 234, 162, 'reset:', 0)
				cycles = 4
			#end:case
			case 7:
				global91._send('say:', 17, 1, 47, 3, self, 400)
			#end:case
			case 8:
				global91._send('say:', 17, 1, 47, 4, self, 400)
			#end:case
			case 9:
				global105._send('number:', 483, 'setLoop:', 1, 'play:')
				theHole._send(
					'view:', 232,
					'setLoop:', 6,
					'setPri:', 13,
					'setCycle:', Fwd,
					'setMotion:', MoveTo, 315, 93, self
				)
			#end:case
			case 10:
				global91._send('say:', 17, 1, 47, 5, self, 400)
			#end:case
			case 11:
				global91._send('say:', 17, 1, 47, 6, self, 400)
			#end:case
			case 12:
				rLab._send('seenSecretLatch:', 1)
				theHole._send('dispose:')
				global1._send('handsOn:')
				global2._send('style:', 10)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class holie(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				kernel.ScriptID(30, 3)._send('addToPic:')
				seconds = 2
			#end:case
			case 1:
				holeInset._send('addToPic:')
				holeRoom._send('addToPic:')
				tapestry._send('addToPic:')
				sDoor._send('init:', 'stopUpd:')
				minoInset._send('init:')
				tapeMove._send('init:')
				seconds = 2
			#end:case
			case 2:
				minoInset._send('setCycle:', CT, 3, 1, self)
				tapeMove._send('setCycle:', CT, 3, 1)
			#end:case
			case 3:
				global105._send('number:', 408, 'setLoop:', 1, 'play:', self)
			#end:case
			case 4:
				global105._send('number:', 909, 'setLoop:', 1, 'play:')
				sDoor._send('setCycle:', End, self)
			#end:case
			case 5:
				minoInset._send('setCycle:', End, self)
				tapeMove._send('setCycle:', End)
			#end:case
			case 6:
				holeInset._send('dispose:')
				holeRoom._send('dispose:')
				tapestry._send('dispose:')
				sDoor._send('dispose:')
				minoInset._send('dispose:')
				tapeMove._send('dispose:')
				global2._send('drawPic:', 400, (15 if global169 else 100))
				kernel.ScriptID(30, 5)._send('addToPic:')
				kernel.ScriptID(30, 9)._send('addToPic:')
				kernel.ScriptID(30, 8)._send('addToPic:')
				kernel.ScriptID(30, 3)._send('init:', 'show:')
				kernel.ScriptID(30, 4)._send('addToPic:')
				cycles = 6
			#end:case
			case 7:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class holeTimer(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				seconds = 20
			#end:case
			case 1:
				global1._send('handsOff:')
				global91._send('say:', 1, 0, 43, 1, self, 400)
			#end:case
			case 2:
				global105._send('number:', 483, 'setLoop:', 1, 'play:')
				theHole._send('setPri:', 13, 'setCycle:', Fwd, 'setMotion:', MoveTo, 315, 93, self)
			#end:case
			case 3:
				global91._send('say:', 1, 0, 43, 2, self, 400)
			#end:case
			case 4:
				global0._send('setMotion:', PolyPath, 160, 160, self)
			#end:case
			case 5:
				theHole._send('setCycle:', 0, 'dispose:')
				emptyHandedDeath._send('start:', 2)
				global2._send('setScript:', emptyHandedDeath)
			#end:case
		#end:match
	#end:method

#end:class or instance

