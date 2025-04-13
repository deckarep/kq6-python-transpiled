#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 850
import sci_sh
import kernel
import Main
import rgCastle
import NewFeature
import KQ6Print
import n913
import Conversation
import Scaler
import PolyPath
import Polygon
import Feature
import LoadMany
import StopWalk
import Motion
import User
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm850 = 0,
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
local10 = None


class NewProp(Prop):
	#property vars (may be empty)
	normal = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global72._send('addToFront:', self)
		global73._send('addToFront:', self)
		super._send('init:', &rest)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global72._send('delete:', self)
		global73._send('delete:', self)
		super._send('dispose:')
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				(not normal)
				(param1._send('type:') & 0x4000)
				self._send('onMe:', param1)
				(_approachVerbs & global66._send('doit:', param1._send('message:')))
			)
			CueObj._send('state:', 0, 'cycles:', 0, 'client:', self, 'theVerb:', param1._send('message:'))
			self._send('doSpecial:', CueObj._send('theVerb:'))
			param1._send('claimed:', 1)
			param1._send('claimed:')
			return
		else:
			super._send('handleEvent:', param1)
		#endif
	#end:method

	@classmethod
	def doSpecial():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('cue:')
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global0._send('setMotion:', PolyPath, approachX, approachY, CueObj)
	#end:method

#end:class or instance

@SCI.instance
class rm850(CastleRoom):
	#property vars (may be empty)
	noun = 3
	picture = 850
	style = 10
	south = 730
	vanishingX = 124
	vanishingY = 92
	minScaleSize = 37
	minScaleY = 111
	maxScaleY = 177
	moveOtherGuard = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		proc958_0(128, 881, 883, 850)
		self._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 0, 181, -10, 181, -10, -10, 319, -10, 319, 189, 304, 179, 288, 179, 279, 182, 263, 182, 254, 179, 246, 179, 225, 164, 202, 164, 191, 152, 206, 152, 193, 143, 229, 143, 203, 129, 172, 129, 156, 124, 151, 116, 169, 116, 169, 112, 101, 112, 89, 124, 76, 129, 70, 129, 50, 141, 57, 141, 38, 155, 56, 155, 45, 166, 21, 166,
					'yourself:'
				)
		)
		if 
			(and
				global0._send('has:', 20)
				(global9._send('at:', 8)._send('owner:') == 870)
				(not kernel.ScriptID(80, 0)._send('tstFlag:', 711, 512))
				(kernel.ScriptID(80, 0)._send('guardTimer:') > 30)
			)
			kernel.ScriptID(80, 0)._send('setFlag:', 711, 512, 'guardTimer:', 30)
		#endif
		portrait._send('init:', 'setPri:', 0)
		super._send('init:', &rest)
		kernel.ScriptID(1015, 6)._send('talkWidth:', 150, 'x:', 15, 'y:', 20)
		kernel.ScriptID(1015, 7)._send('talkWidth:', 135, 'x:', 160, 'y:', 20)
		if (global9._send('at:', 27)._send('owner:') == 850):
			bird._send('init:')
		#endif
		global0._send(
			'init:',
			'setScale:', Scaler, maxScaleSize, minScaleSize, maxScaleY, minScaleY
		)
		match global12
			case 870:
				if (global102._send('number:') != 700):
					global102._send('fadeTo:', 700, -1)
				#endif
				global0._send('posn:', 149, 112)
			#end:case
			case 781:
				global102._send('fadeTo:', 700, -1)
				global0._send('posn:', vizierDoor._send('approachX:'), vizierDoor._send('approachY:'))
			#end:case
			case 880:
				global0._send('loop:', 1)
				if (global0._send('x:') > 126):
					global0._send('posn:', 173, 130)
				else:
					global0._send('posn:', 187, 140)
				#endif
			#end:case
			else:
				local6 = 1
				if 
					(or
						(not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 512))
						kernel.ScriptID(80, 0)._send('tstFlag:', 710, 1)
						(not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 128))
					)
					global0._send('posn:', 230, 185)
				else:
					global0._send('posn:', 160, 185)
				#endif
				kernel.ScriptID(80, 0)._send('setFlag:', 709, 128)
			#end:else
		#end:match
		kernel.ScriptID(80, 0)._send('guard1Code:', guardsCode, 'guard2Code:', guardsCode)
		spotEgoScr = captureEgo
		if 
			(or
				(not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 512))
				(and
					kernel.ScriptID(80, 0)._send('tstFlag:', 710, 1)
					(not kernel.ScriptID(80, 0)._send('tstFlag:', 711, 256))
				)
				(not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 128))
			)
			kernel.ScriptID(80, 5)._send(
				'init:',
				'noun:', 6,
				'loop:', 3,
				'actions:', guardDoVerb,
				'okToCheck:', okToCheckCode
			)
			kernel.ScriptID(80, 5)._send('signal:', (kernel.ScriptID(80, 5)._send('signal:') & 0xefff))
			kernel.ScriptID(80, 6)._send(
				'init:',
				'noun:', 6,
				'loop:', 3,
				'actions:', guardDoVerb,
				'okToCheck:', okToCheckCode
			)
			kernel.ScriptID(80, 6)._send('signal:', (kernel.ScriptID(80, 6)._send('signal:') & 0xefff))
			local1 = 1
		#endif
		vizierDoor._send('cel:', ((global12 == 781) * 3), 'init:')
		global32._send(
			'add:', floor, roomFeatures, studyDoor, cassima_door, pillar, chairs, hideFeature,
			'eachElementDo:', #init
		)
		(cond
			case (local1 and kernel.ScriptID(80, 0)._send('tstFlag:', 711, 128)):
				kernel.ScriptID(80, 5)._send('loop:', 2, 'posn:', 118, 116, 'okToCheck:', 0)
				kernel.ScriptID(80, 6)._send('loop:', 2, 'posn:', 133, 117, 'okToCheck:', 0)
				self._send('setScript:', walkOutAtWrongTime)
			#end:case
			case (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 128)):
				kernel.ScriptID(80, 5)._send('posn:', 105, 149)
				kernel.ScriptID(80, 6)._send('posn:', 143, 150)
				self._send('setScript:', shouldNotHaveComeOut)
			#end:case
			case 
				(and
					kernel.ScriptID(80, 0)._send('tstFlag:', 710, 1)
					(not kernel.ScriptID(80, 0)._send('tstFlag:', 711, 256))
				):
				kernel.ScriptID(80, 5)._send('okToCheck:', 0, 'posn:', 126, 231)
				kernel.ScriptID(80, 6)._send('okToCheck:', 0, 'posn:', 163, 233)
				self._send('setScript:', walkGuardsOnScreen)
			#end:case
			case (local6 and local1):
				global1._send('handsOff:')
				global0._send('setSpeed:', 8)
				hideFeature._send('doVerb:', 5)
				kernel.ScriptID(80, 5)._send('sightAngle:', 180, 'posn:', 105, 149)
				kernel.ScriptID(80, 6)._send('sightAngle:', 180, 'posn:', 143, 150)
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 8)):
					kernel.ScriptID(80, 0)._send('setFlag:', 709, 8)
					startGuardScr._send('next:', watchGuardsTalk)
					watchGuardsTalk._send('next:', guardPatrol)
				else:
					startGuardScr._send('next:', guardPatrol)
				#endif
				kernel.ScriptID(80, 5)._send('setScript:', startGuardScr)
			#end:case
			else:
				(cond
					case kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2):
						kernel.ScriptID(80, 5)._send('posn:', 118, 116)
						kernel.ScriptID(80, 6)._send('posn:', 133, 117)
					#end:case
					case kernel.ScriptID(80, 0)._send('tstFlag:', 711, 256):
						spotEgoScr = walkGuardsOnScreen
						kernel.ScriptID(80, 0)._send('clrFlag:', 710, 1, 'guardTimer:', 2)
					#end:case
					case local1:
						kernel.ScriptID(80, 5)._send('posn:', 118, 126)
						kernel.ScriptID(80, 6)._send('posn:', 133, 126)
						startGuardScr._send('next:', guardPatrol)
						kernel.ScriptID(80, 5)._send('setScript:', startGuardScr)
					#end:case
				)
				global1._send('handsOn:')
				if (global12 == 781):
					global1._send('handsOff:')
				#endif
			#end:else
		)
		if global0._send('scaler:'):
			global0._send('scaler:')._send('doit:')
		#endif
		kernel.ScriptID(80, 0)._send('setupGuards:')
		if local1:
			global105._send('number:', 702, 'loop:', 1, 'play:')
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		local0 = global0._send('onControl:', 1)
		(cond
			case script: 0#end:case
			case 
				(and
					User._send('alterEgo:')._send('edgeHit:')
					kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2)
				):
				self._send('setScript:', weddingStarts)
			#end:case
			case proc999_4(158, 0, 320, 115, global0):
				global2._send('newRoom:', 870)
			#end:case
			case (local0 & 0x2000):
				global2._send('newRoom:', 781)
			#end:case
			case (local0 & 0x1200):
				global2._send('newRoom:', 880)
			#end:case
		)
		if ((not kernel.ScriptID(80, 0)._send('tstFlag:', 710, 2)) and (global0._send('y:') < 117)):
			kernel.ScriptID(80, 0)._send('setFlag:', 710, 2)
			global91._send('say:', 3, 3, 17, 0)
		#endif
		super._send('doit:', &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			match param1
				case 1:
					roomConv._send('add:', -1, noun, param1, 0, 1)
					1
					if local1:
						roomConv._send('add:', -1, noun, param1, 21, 1)
						1
					else:
						roomConv._send('add:', -1, noun, param1, 22, 1)
						1
					#endif
					roomConv._send('init:')
					1
				#end:case
				case 2:
					if local1:
						global91._send('say:', noun, param1, 21)
						1
					else:
						global91._send('say:', noun, param1, 22)
						1
					#endif
				#end:case
				else:
					super._send('doVerb:', param1, &rest)
					1
				#end:else
			#end:match
		)
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if kernel.ScriptID(80, 5)._send('script:'):
			kernel.ScriptID(80, 5)._send('setScript:', 0)
		#endif
		if (param1 != 730):
			kernel.ScriptID(80, 0)._send('clrFlag:', 711, 16384)
		#endif
		if kernel.ScriptID(80, 0)._send('tstFlag:', 711, 256):
			kernel.ScriptID(80, 0)._send('guardTimer:', 0)
		#endif
		super._send('newRoom:', param1, &rest)
	#end:method

	@classmethod
	def warnUser(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				self._send('setScript:', weddingStartsNow)
			#end:case
			case 2:
				global91._send('say:', 1, 0, 24, 0)
				spotEgoScr = walkGuardsOnScreen
				kernel.ScriptID(80, 0)._send('setFlag:', 711, 256, 'guardTimer:', 5)
			#end:case
			else:
				super._send('warnUser:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class hideEgo(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global73._send('addToFront:', self)
		global72._send('addToFront:', self)
		register = kernel.ScriptID(80, 0)._send('tstFlag:', 709, 8)
		super._send('init:', &rest)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (global0._send('mover:') and (state == 3)):
			global1._send('handsOff:')
			if (not local4):
				local4 = User._send('curEvent:')._send('x:')
				local5 = User._send('curEvent:')._send('y:')
				cycles = 3
			#endif
			global0._send('setMotion:', 0)
		#endif
		super._send('doit:')
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((not param1._send('modifiers:')) and User._send('input:')):
			param1._send('claimed:', 1)
			if 
				(and
					(global69._send('curIcon:') == global69._send('at:', 3))
					local1
					(or
						kernel.ScriptID(80, 5)._send('onMe:', param1)
						kernel.ScriptID(80, 6)._send('onMe:', param1)
					)
				)
				global1._send('handsOff:')
				local8 = 1
				CueObj._send('state:', 0, 'cycles:', 0, 'client:', kernel.ScriptID(80, 5), 'theVerb:', 2)
				CueObj._send('client:')._send('approachX:', 218, 'approachY:', 178)
				kernel.ScriptID(80, 5)._send('okToCheck:', 0)
				kernel.ScriptID(80, 6)._send('okToCheck:', 0)
				global91._send('say:', 6, 2, 0, 1, self)
				next = talkToGuards
			else:
				param1._send('claimed:', 0)
			#endif
		#endif
		param1._send('claimed:')
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 260, 180, self)
			#end:case
			case 1:
				global0._send('setHeading:', 225, self)
			#end:case
			case 2:
				global0._send(
					'normal:', 0,
					'view:', 881,
					'setLoop:', 2,
					'cel:', 0,
					'x:', 246,
					'y:', 188,
					'setScale:',
					'scaleX:', 148,
					'scaleY:', 148,
					'cycleSpeed:', 8,
					'setCycle:', End, self
				)
			#end:case
			case 3:
				if (not local9):
					if register:
						global1._send('handsOn:')
					#endif
				else:
					local9 = 0
					cycles = 1
				#endif
			#end:case
			case 4:
				global73._send('delete:', self)
				global72._send('delete:', self)
				kernel.ScriptID(80, 5)._send('sightAngle:', 40)
				kernel.ScriptID(80, 6)._send('sightAngle:', 40)
				global0._send('setCycle:', Beg, self)
			#end:case
			case 5:
				global0._send(
					'reset:', 5, 900,
					'posn:', hideFeature._send('approachX:'), hideFeature._send('approachY:')
				)
				(cond
					case 
						(and
							CueObj._send('client:')
							CueObj._send('client:')._send('approachX:')
							(&
								CueObj._send('client:')._send('_approachVerbs:')
								global66._send('doit:', CueObj._send('theVerb:'))
							)
						):
						if (CueObj._send('client:') == hideFeature):
							local10 = 1
							CueObj._send('client:')._send('doVerb:', CueObj._send('theVerb:'))
						else:
							global0._send(
								'setMotion:', PolyPath, CueObj._send('client:')._send(
										'approachX:'
									), (+
										global0._send('z:')
										CueObj._send('client:')._send('approachY:')
									), CueObj
							)
						#endif
					#end:case
					case local4:
						global0._send('setMotion:', PolyPath, local4, local5)
					#end:case
				)
				global1._send('handsOn:')
				local4 = local5 = register = 0
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class putDownBird(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setHeading:', 270, self)
			#end:case
			case 1:
				cycles = 3
			#end:case
			case 2:
				global91._send('say:', 4, 37, 19, 0, self)
			#end:case
			case 3:
				global105._send('number:', 930, 'loop:', -1, 'play:')
				global0._send(
					'normal:', 0,
					'view:', 883,
					'loop:', 0,
					'cel:', 0,
					'setScale:',
					'scaleX:', 85,
					'scaleY:', 85,
					'cycleSpeed:', 8,
					'setCycle:', Fwd
				)
				seconds = 5
			#end:case
			case 4:
				global105._send('loop:', 1, 'stop:')
				global0._send('loop:', 2, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 5:
				bird._send('init:')
				global102._send('fadeTo:', 931, -1)
				global0._send('put:', 27, 850)
				global0._send('reset:', 1)
				global1._send('givePoints:', 4)
				kernel.ScriptID(80, 0)._send('setFlag:', 711, 16384)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class timerScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				seconds = 7
			#end:case
			case 1:
				global91._send('say:', 1, 0, 2, 1, self, 880)
			#end:case
			case 2:
				if (local0 & floor._send('onMeCheck:')):
					global1._send('handsOff:')
					global2._send('spotEgo:', proc80_7())
					self._send('dispose:')
				else:
					kernel.ScriptID(80, 6)._send(
						'setMotion:', MoveTo, bird._send('x:'), (bird._send('y:') - 2)
					)
					kernel.ScriptID(80, 5)._send(
						'setMotion:', MoveTo, (bird._send('x:') - 30), bird._send('y:'), self
					)
				#endif
			#end:case
			case 3:
				kernel.ScriptID(80, 5)._send('setMotion:', MoveTo, 129, 144, self)
			#end:case
			case 4:
				kernel.ScriptID(80, 5)._send('setHeading:', 90, self)
			#end:case
			case 5:
				cycles = 4
			#end:case
			case 6:
				roomConv._send('add:', 880, 1, 0, 2, 2, 'add:', 880, 1, 0, 2, 3, 'init:', self)
			#end:case
			case 7:
				kernel.ScriptID(80, 5)._send('view:', 884, 'loop:', 1, 'cel:', 0, 'setCycle:', CT, 4, 1, self)
				global102._send('fadeTo:', 700, -1)
			#end:case
			case 8:
				bird._send('hide:')
				kernel.ScriptID(80, 5)._send('setCycle:', End, self)
			#end:case
			case 9:
				roomConv._send(
					'add:', 880, 1, 0, 2, 4,
					'add:', 880, 1, 0, 2, 5,
					'add:', 880, 1, 0, 2, 6,
					'add:', 880, 1, 0, 2, 7,
					'add:', 880, 1, 0, 2, 8,
					'add:', 880, 1, 0, 2, 9,
					'add:', 880, 1, 0, 2, 10,
					'add:', 880, 1, 0, 2, 11,
					'add:', 880, 1, 0, 2, 12,
					'init:', self
				)
			#end:case
			case 10:
				kernel.ScriptID(80, 5)._send('view:', 724, 'loop:', 4, 'cel:', 0, 'setCycle:', StopWalk, -1)
				self._send('setScript:', walkGuardsOffScreen, self)
			#end:case
			case 11:
				global91._send('say:', 1, 0, 13, 0, self)
			#end:case
			case 12:
				if (global2._send('script:') == hideEgo):
					CueObj._send('client:', 0)
					local4 = 0
					hideEgo._send('caller:', self)
					if (global2._send('script:')._send('state:') == 3):
						hideEgo._send('cue:')
					else:
						local9 = 1
					#endif
				else:
					cycles = 1
				#endif
			#end:case
			case 13:
				global2._send('spotEgo:', proc80_7())
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walkGuardsOffScreen(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				kernel.ScriptID(80, 5)._send('setMotion:', MoveTo, 126, 176, self)
				kernel.ScriptID(80, 6)._send('setMotion:', MoveTo, 163, 176)
			#end:case
			case 1:
				if register:
					global2._send('spotEgo:', proc80_7())
				#endif
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class captureEgo(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		register = 0
		super._send('dispose:', &rest)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				kernel.ScriptID(80, 5)._send('setScript:', 0, 'setMotion:', 0, 'okToCheck:', 0)
				kernel.ScriptID(80, 6)._send('setScript:', 0, 'setMotion:', 0, 'okToCheck:', 0)
				proc913_4(register, global0, self)
			#end:case
			case 1:
				global91._send('say:', 1, 0, 9, 1, self)
			#end:case
			case 2:
				(cond
					case (not global0._send('facingMe:', kernel.ScriptID(80, 5))):
						proc913_4(kernel.ScriptID(80, 5), global0, self)
					#end:case
					case (not global0._send('facingMe:', kernel.ScriptID(80, 6))):
						proc913_4(kernel.ScriptID(80, 6), global0, self)
					#end:case
					else:
						cycles = 1
					#end:else
				)
			#end:case
			case 3:
				proc913_4(global0, register, self)
			#end:case
			case 4:
				roomConv._send('add:', -1, 1, 0, 9, 2, 'add:', -1, 1, 0, 9, 3, 'init:', self)
			#end:case
			case 5:
				proc80_7()._send('setScript:', kernel.ScriptID(80, 4), self, 1)
			#end:case
			case 6:
				roomConv._send(
					'add:', -1, 1, 0, 9, 4,
					'add:', -1, 1, 0, 9, 5,
					'add:', -1, 1, 0, 9, 6,
					'init:', self
				)
			#end:case
			case 7:
				global2._send('newRoom:', 820)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walkGuardsOnScreen(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		register = 0
		super._send('dispose:', &rest)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				local1 = 1
				kernel.ScriptID(80, 0)._send('clrFlag:', 710, 1)
				kernel.ScriptID(80, 5)._send(
					'init:',
					'posn:', 126, 231,
					'setMotion:', MoveTo, 126, 188, self
				)
				kernel.ScriptID(80, 6)._send('init:', 'posn:', 163, 233, 'setMotion:', MoveTo, 163, 188)
				kernel.ScriptID(80, 0)._send('setupGuards:')
			#end:case
			case 1:
				global91._send('say:', 1, 0, 11, 0, self)
			#end:case
			case 2:
				if (global2._send('script:') == hideEgo):
					CueObj._send('client:', 0)
					local4 = 0
					hideEgo._send('caller:', self)
					if (hideEgo._send('state:') == 3):
						hideEgo._send('cue:')
					else:
						local9 = 1
					#endif
				else:
					self._send('cue:')
				#endif
			#end:case
			case 3:
				if (not vizierDoor._send('cel:')):
					global2._send('spotEgoScr:', captureEgo)
					global2._send('spotEgo:', proc80_7())
				else:
					kernel.ScriptID(80, 0)._send('setFlag:', 709, 1)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class shouldNotHaveComeOut(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		register = 0
		super._send('dispose:', &rest)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				kernel.ScriptID(80, 5)._send('okToCheck:', 0)
				kernel.ScriptID(80, 6)._send('okToCheck:', 0)
				cycles = 4
			#end:case
			case 1:
				global91._send('say:', 1, 0, 3, 0, self)
			#end:case
			case 2:
				global2._send('spotEgo:', proc80_7())
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class talkToGuards(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		register = 0
		super._send('dispose:', &rest)
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
				kernel.ScriptID(80, 5)._send('approachX:', 0, 'approachY:', 0)
				if (not local8):
					global91._send('say:', 6, 2, 0, 1, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				if (local0 & 0x0080):
					global0._send('setMotion:', PolyPath, 218, 178, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				if (not global0._send('facingMe:', kernel.ScriptID(80, 5))):
					proc913_4(global0, kernel.ScriptID(80, 5), self)
				else:
					cycles = 1
				#endif
			#end:case
			case 3:
				cycles = 1
			#end:case
			case 4:
				global91._send('say:', 6, 2, 0, 2, self, 'oneOnly:', 0)
			#end:case
			case 5:
				global2._send('spotEgo:', proc80_7())
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class startGuardScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				kernel.ScriptID(80, 5)._send('ignoreActors:', 1, 'setMotion:', MoveTo, 118, 116, self)
				kernel.ScriptID(80, 6)._send('setMotion:', MoveTo, 133, 117)
			#end:case
			case 1:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class watchGuardsTalk(Script):
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
				global91._send('say:', 1, 0, 1, 0, self)
			#end:case
			case 2:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class guardPatrol(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				seconds = kernel.Random(3, 6)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				if (not local7):
					kernel.ScriptID(80, 5)._send('setMotion:', MoveTo, 102, 145, self)
					kernel.ScriptID(80, 6)._send('setMotion:', MoveTo, 143, 145)
				else:
					self._send('dispose:')
				#endif
			#end:case
			case 3:
				state = -1
				kernel.ScriptID(80, 5)._send('setMotion:', MoveTo, 115, 114, self)
				kernel.ScriptID(80, 6)._send('setMotion:', MoveTo, 130, 114)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class weddingStarts(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global102._send('number:', 701, 'loop:', -1, 'play:')
				cycles = 2
			#end:case
			case 1:
				global91._send('say:', 1, 0, 8, 1, self)
			#end:case
			case 2:
				global91._send('say:', 1, 0, 8, 2, self)
			#end:case
			case 3:
				global2._send('newRoom:', 730)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class weddingStartsNow(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				kernel.ScriptID(80, 0)._send('setFlag:', 711, 16384)
				cycles = 1
			#end:case
			case 1:
				global91._send('say:', 1, 0, 8, 0, self)
			#end:case
			case 2:
				kernel.ScriptID(80, 5)._send('setScript:', walkGuardsOffScreen, 0, 1)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walkOutAtWrongTime(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				cycles = 3
			#end:case
			case 1:
				if global5._send('contains:', bird):
					global91._send('say:', 1, 0, 33, 0, self)
				else:
					global91._send('say:', 1, 0, 7, 0, self)
				#endif
			#end:case
			case 2:
				global2._send('spotEgo:', proc80_7())
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lookThruKeyhole(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(= temp0
					match CueObj._send('client:')
						case vizierDoor: 795#end:case
						case studyDoor: 798#end:case
					#end:match
				)
				kernel.ScriptID(82, 1)._send(
					'noun:', CueObj._send('client:')._send('noun:'),
					'actions:', keyHoleActions,
					'init:', temp0, 0, 0, 92, 54
				)
				cycles = 2
			#end:case
			case 1:
				global91._send('say:', CueObj._send('client:')._send('noun:'), 1, 29)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class bird(Prop):
	#property vars (may be empty)
	x = 146
	y = 144
	view = 883
	loop = 4
	scaleSignal = 1
	scaleX = 96
	scaleY = 96
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('setCycle:', Fwd, 'ignoreActors:', 'setScript:', timerScr)
	#end:method

#end:class or instance

@SCI.instance
class portrait(View):
	#property vars (may be empty)
	x = 200
	view = 850
	loop = 6
	signal = 24577
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(= y
			(112 if proc999_5(global9._send('at:', 26)._send('owner:'), 880, global0) else 100)
		)
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class vizierDoor(NewProp):
	#property vars (may be empty)
	x = 59
	y = 111
	noun = 9
	sightAngle = 40
	approachX = 79
	approachY = 127
	view = 850
	signal = 16385
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if cel:
			self._send('setScript:', closeMe)
		#endif
		super._send('init:', &rest)
		if local1:
			if (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2)):
				self._send('approachVerbs:', 5)
				normal = 0
			#endif
		else:
			self._send('approachVerbs:', 2, 5)
		#endif
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (global69._send('curIcon:') == global69._send('at:', 2)):
			if (global0._send('view:') == 881):
				sightAngle = 26505
			else:
				sightAngle = 40
			#endif
		#endif
		return super._send('onMe:', param1)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not local1):
			match param1
				case 5:
					if (not kernel.ScriptID(80, 0)._send('tstFlag:', 711, 1024)):
						kernel.ScriptID(80, 0)._send('setFlag:', 711, 1024)
						global91._send('say:', noun, param1, 31, 1)
					#endif
					global2._send('setScript:', openVizDoor)
				#end:case
				case 1:
					if (not local2):
						local2.post('++')
						(_approachVerbs |= global66._send('doit:', 1))
						global91._send('say:', 10, param1, 27)
					else:
						global2._send('setScript:', kernel.ScriptID(82), 0, lookThruKeyhole)
					#endif
				#end:case
				case 2:
					global91._send('say:', noun, param1, 22)
				#end:case
				else:
					if (global66._send('doit:', param1) == -32768):
						global91._send('say:', 9, 0)
					else:
						super._send('doVerb:', param1)
					#endif
				#end:else
			#end:match
		else:
			match param1
				case 1:
					if (not local2):
						local2.post('++')
						global91._send('say:', 10, param1, 27)
					else:
						global91._send('say:', 10, 1, 28)
					#endif
				#end:case
				case 5:
					if kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2):
						global91._send('say:', 9, param1, 25)
					else:
						global91._send('say:', noun, param1, 21)
					#endif
				#end:case
				case 2:
					global91._send('say:', noun, param1, 21)
				#end:case
				else:
					if (global66._send('doit:', param1) == -32768):
						global91._send('say:', 9, 0)
					else:
						global2._send('spotEgo:', proc80_7())
					#endif
				#end:else
			#end:match
		#endif
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global105._send('flags:', 1, 'stop:')
		if cel:
			proc80_2(4)
		else:
			self._send('setPri:', -1, 'stopUpd:')
		#endif
	#end:method

	@classmethod
	def doSpecial(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global91._send('say:', 10, 5, 21, 0, NewProp)
			#end:case
			else:
				super._send('doSpecial:')
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class openVizDoor(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				cycles = 2
			#end:case
			case 1:
				global105._send('number:', 901, 'loop:', 1, 'flags:', 0, 'play:')
				vizierDoor._send('setPri:', 10, 'setCycle:', End, self)
			#end:case
			case 2:
				vizierDoor._send('cue:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class closeMe(Script):
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
				vizierDoor._send('setPri:', 10, 'setCycle:', Beg, self)
			#end:case
			case 2:
				global105._send('number:', 902, 'loop:', 1, 'play:')
				if kernel.ScriptID(80, 0)._send('tstFlag:', 709, 128):
					global1._send('handsOn:')
				#endif
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class studyDoor(NewFeature):
	#property vars (may be empty)
	x = 91
	y = 114
	z = 11
	noun = 10
	nsTop = 93
	nsLeft = 88
	nsBottom = 114
	nsRight = 94
	sightAngle = 360
	approachX = 96
	approachY = 115
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		if local1:
			if (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2)):
				self._send('approachVerbs:', 5)
				normal = 0
			#endif
		else:
			self._send('approachVerbs:', 2, 5)
		#endif
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(and
				super._send('onMe:', param1)
				(or
					(and
						(global69._send('curIcon:') == global69._send('at:', 2))
						(or
							((global0._send('view:') == 881) and sightAngle = 26505)
							sightAngle = 40
						)
					)
					1
				)
			)
		)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				(cond
					case (not local3):
						local3.post('++')
						global91._send('say:', noun, param1, 27)
						if (not local1):
							(_approachVerbs |= global66._send('doit:', 1))
						#endif
					#end:case
					case local1:
						global91._send('say:', noun, param1, 28)
					#end:case
					else:
						global2._send('setScript:', kernel.ScriptID(82), 0, lookThruKeyhole)
					#end:else
				)
			#end:case
			case 2:
				if local1:
					global91._send('say:', 9, 2, 21, 0)
				else:
					proc913_1(59)
					global91._send('say:', noun, param1, 22, 0, self)
				#endif
			#end:case
			case 5:
				if kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2):
					global91._send('say:', 9, param1, 25)
				else:
					global91._send('say:', noun, param1, 22)
				#endif
			#end:case
			case 64:
				if local1:
					global91._send('say:', noun, param1, 21)
				else:
					global91._send('say:', noun, param1, 22)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1)
			#end:else
		#end:match
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		proc913_2(59)
	#end:method

	@classmethod
	def doSpecial(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global91._send('say:', 10, 5, 21, 0, NewFeature)
			#end:case
			else:
				super._send('doSpecial:')
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class floor(NewFeature):
	#property vars (may be empty)
	noun = 4
	onMeCheck = 66
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		normal = (not local1)
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(and
				super._send('onMe:', param1)
				(or
					(and
						(global69._send('curIcon:') == global69._send('useIconItem:'))
						(global69._send('curInvIcon:') == global9._send('at:', 27))
						_approachVerbs = -32768
						approachX = 161
						approachY = 143
					)
					(and
						(not _approachVerbs = 0)
						(not approachX = 0)
						(not approachY = 0)
					)
				)
			)
		)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 37:
				kernel.ScriptID(80, 0)._send('setFlag:', 709, 256)
				local7 = 1
				global2._send('setScript:', putDownBird)
			#end:case
			else:
				super._send('doVerb:', param1)
			#end:else
		#end:match
	#end:method

	@classmethod
	def doSpecial(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 37:
				global91._send('say:', 4, 37, 20, 0, self)
			#end:case
			else:
				super._send('doSpecial:')
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class cassima_door(Feature):
	#property vars (may be empty)
	x = 155
	y = 109
	z = 7
	heading = 180
	noun = 11
	nsTop = 94
	nsLeft = 152
	nsBottom = 110
	nsRight = 159
	approachX = 154
	approachY = 111
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(and
				super._send('onMe:', param1)
				(or
					((global0._send('view:') == 881) and sightAngle = 26505)
					sightAngle = 45
				)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class pillar(Feature):
	#property vars (may be empty)
	x = 189
	y = 134
	z = 32
	noun = 8
	nsTop = 72
	nsLeft = 183
	nsBottom = 133
	nsRight = 196
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(and
				super._send('onMe:', param1)
				(or
					((global0._send('view:') == 881) and sightAngle = 26505)
					sightAngle = 45
				)
				(or
					proc999_4(175, 71, 206, 135, param1)
					proc999_4(191, 135, 206, 144, param1)
				)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class chairs(Feature):
	#property vars (may be empty)
	noun = 19
	onMeCheck = 768
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		x = param1._send('x:')
		y = param1._send('y:')
		sightAngle = 26505
		return super._send('onMe:', param1)
	#end:method

#end:class or instance

@SCI.instance
class hideFeature(Feature):
	#property vars (may be empty)
	nsTop = 64
	nsLeft = 253
	nsBottom = 177
	nsRight = 319
	approachX = 260
	approachY = 180
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('approachVerbs:', 5)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				(cond
					case local10:
						local10 = 0
					#end:case
					case (global2._send('script:') != hideEgo):
						global2._send('setScript:', hideEgo)
					#end:case
					else:
						super._send('doVerb:', param1)
					#end:else
				)
			#end:case
			else:
				super._send('doVerb:', param1)
			#end:else
		#end:match
	#end:method

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
				((0x0004 & temp0) and noun = 16)
				((0x0008 & temp0) and noun = 15)
				((0x0020 & temp0) and noun = 13)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class guardsCode(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(or
				((global0._send('view:') != 881) and (local0 & 0x0042))
				(param1._send('onControl:', 1) & 0x0040)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class okToCheckCode(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(or
				(< 90 param1._send('heading:') 270)
				(global0._send('y:') <= param1._send('y:'))
				(global0._send('y:') <= 129)
			)
		)
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
		(cond
			case (param1 == 2):
				global2._send('setScript:', talkToGuards)
			#end:case
			case kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2):
				(cond
					case proc999_5(param1, 5, 1):
						global91._send('say:', 6, param1, 25)
					#end:case
					case (global66._send('doit:', param1) == -32768):
						global91._send('say:', 6, 0, 25)
					#end:case
					else:
						temp0 = 0
					#end:else
				)
			#end:case
			case (param1 == 37):
				CueObj._send('client:', floor, 'state:', 0, 'cycles:', 0, 'theVerb:', 37)
				KQ6Print._send('posn:', -1, 10, 'say:', 0, 6, 37, 0, 1, 'init:')
				global0._send(
					'setMotion:', PolyPath, floor._send('approachX:'), floor._send(
							'approachY:'
						), CueObj
				)
			#end:case
			else:
				temp0 = 0
			#end:else
		)
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class roomConv(Conversation):
	#property vars (may be empty)
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
				global91._send('say:', CueObj._send('client:')._send('noun:'), param1, 29, 2)
			#end:case
			else:
				temp0 = 0
			#end:else
		#end:match
		return temp0
	#end:method

#end:class or instance

