#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 450
import sci_sh
import kernel
import Main
import n451
import KQ6Room
import n913
import Conversation
import Scaler
import PolyPath
import Polygon
import Feature
import LoadMany
import Sound
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm450 = 0,
	oyster = 1,
	giveItemScript = 2,
	rightInvItem = 3,
	wrongInvItem = 4,
	toTheSea = 5,
	gnomeGroup = 6,
	snooze4 = 7,
	proc450_8 = 8,
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


@SCI.procedure
def localproc_0(param1 = None, *rest):
	tmpGnome._send(
		'view:', param1._send('view:'),
		'loop:', param1._send('loop:'),
		'cel:', param1._send('cel:'),
		'x:', param1._send('x:'),
		'y:', param1._send('y:'),
		'signal:', param1._send('signal:')
	)
	if global5._send('contains:', tmpGnome):
		tmpGnome._send('show:')
	else:
		tmpGnome._send('init:')
	#endif
#end:procedure

@SCI.procedure
def localproc_1(param1 = None, *rest):
	match local5
		case 1:
			kernel.ScriptID(455, 0)._send('doVerb:', param1)
		#end:case
		case 2:
			kernel.ScriptID(456, 0)._send('doVerb:', param1)
		#end:case
		case 3:
			kernel.ScriptID(4561, 0)._send('doVerb:', param1)
		#end:case
		case 4:
			kernel.ScriptID(457, 0)._send('doVerb:', param1)
		#end:case
		case 5:
			kernel.ScriptID(458, 0)._send('doVerb:', param1)
		#end:case
	#end:match
#end:procedure

@SCI.procedure
def proc450_8(param1 = None, *rest):
	if param1:
		snoreSong._send('stop:')
		snooze1._send('view:', 2002)
		snooze4._send('view:', 2002)
		shimmer1._send('dispose:')
		shimmer2._send('dispose:')
	else:
		snoreSong._send('play:')
		snooze1._send('view:', 450, 'loop:', 3, 'checkDetail:')
		if kernel.ScriptID(40, 0)._send('oysterDozing:'):
			snooze4._send('view:', 450, 'loop:', 5, 'init:', 'setCycle:', Fwd, 'checkDetail:')
		#endif
		shimmer1._send('init:')
		shimmer2._send('init:')
	#endif
#end:procedure

@SCI.instance
class rm450(KQ6Room):
	#property vars (may be empty)
	picture = 450
	horizon = 70
	walkOffEdge = 1
	
	@classmethod
	def cue():
		if global5._send('contains:', mySentence):
			mySentence._send(
				'y:', (mySentence._send('y:') + 100),
				'z:', 0,
				'setScript:', sentenceFloat
			)
		#endif
	#end:method

	@classmethod
	def notify(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case ((not argc) or (not param1)): 0#end:case
			case (not local5):
				global2._send('setScript:', 130)
			#end:case
			else:
				if global2._send('script:'):
					kernel.ScriptID(130)._send('next:', resetGnomes)
				#endif
				global2._send('setScript:', 130)
			#end:else
		)
		global0._send('actions:', egoDoVerb)
	#end:method

	@classmethod
	def init():
		global2._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 130, 72, 193, 0, 319, 0, 319, 78, 213, 78,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 125, 72, 115, 80, 115, 92, 79, 97, 89, 111, 75, 128, 94, 141, 94, 150, 58, 150, 24, 189, 0, 189, 0, 0, 64, 0,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 235, 147, 233, 140, 246, 124, 319, 124, 319, 189, 286, 189, 286, 153, 299, 147, 279, 144, 256, 151,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 125, 137, 94, 137, 90, 134, 93, 131, 124, 131, 129, 134,
					'yourself:'
				)
		)
		global1._send('handsOff:')
		super._send('init:', &rest)
		oyster._send('init:')
		if 
			(or
				(global9._send('at:', 30)._send('owner:') != global11)
				kernel.ScriptID(40, 0)._send('oysterDozing:')
			)
			oyster._send('setCel:', 2)
			snooze4._send('init:', 'setCycle:', Fwd)
		else:
			oyster._send('setCel:', 0)
			oyBlink._send(
				'init:',
				'setPri:', oyster._send('priority:'),
				'hide:',
				'setScript:', oyBlinkScript
			)
		#endif
		kernel.Lock(143, 450, 0)
		global105._send('number:', 916, 'setLoop:', -1, 'play:')
		global32._send(
			'add:', farFoliage, rock, oysterBeds, otherRocks, smallRocks, sky, beach, myPath, oysterCouch, ocean,
			'eachElementDo:', #init
		)
		shimmer1._send('init:')
		shimmer2._send('init:')
		snoreSong._send('play:')
		snooze1._send('init:', 'setCycle:', Fwd)
		if (global9._send('at:', 50)._send('owner:') == global11):
			mySentence._send('init:', 'setCycle:', Fwd, 'setScript:', sentenceFloat)
		#endif
		global102._send('number:', 915, 'setLoop:', -1, 'play:')
		global0._send('setScale:', Scaler, 100, 30, 126, 70, 'actions:', egoDoVerb)
		if proc999_5(global12, 470, 460):
			global2._send('setScript:', egoEnters)
		#endif
	#end:method

	@classmethod
	def dispose():
		proc913_2(59)
		proc958_0(0, 455, 456, 4561, 457, 458)
		if (global9._send('at:', 30)._send('owner:') != global11):
			kernel.ScriptID(40, 0)._send('oysterDozing:', 0)
		#endif
		kernel.ScriptID(40, 0)._send('setScript:', 0)
		if global5._send('contains:', mySentence):
			mySentence._send('setMotion:', 0)
		#endif
		global105._send('fade:', 0, 10, 10)
		super._send('dispose:')
	#end:method

	@classmethod
	def doit():
		(cond
			case global2._send('script:'):#end:case
			case 
				(and
					(global0._send('view:') != 900)
					(or
						(global0._send('onControl:', 1) == 32)
						(global0._send('onControl:', 1) == 64)
					)
				):
				if 
					(and
						global5._send('contains:', mySentence)
						(mySentence._send('y:') > 158)
						sentencePoly._send('points:')
					)
					global2._send('obstacles:')._send('delete:', sentencePoly)
					sentencePoly._send('dispose:', 'points:', 0)
					mySentence._send('setScript:', sentenceFloat)
				#endif
				global103._send('stop:')
				global0._send('view:', 900)
			#end:case
			case ((global0._send('view:') != 308) and (global0._send('onControl:', 1) == 4)):
				if global5._send('contains:', mySentence):
					mySentence._send('setMotion:', 0, 'setScript:', 0)
				#endif
				(cond
					case (global0._send('view:') != 900): 0#end:case
					case (global0._send('heading:') < 135):
						global0._send('loop:', 0)
					#end:case
					case (global0._send('heading:') > 225):
						global0._send('loop:', 1)
					#end:case
					else:
						global0._send('loop:', 2)
					#end:else
				)
				global0._send('view:', 308)
				global103._send('number:', 922, 'setLoop:', -1, 'play:')
			#end:case
			case ((global0._send('view:') != 3081) and (global0._send('onControl:', 1) == 2)):
				global0._send('view:', 3081)
			#end:case
			case 
				(and
					(not local2)
					(global0._send('view:') != 3082)
					(global0._send('onControl:', 1) == 8192)
				):
				global0._send('view:', 3082)
			#end:case
			case (global0._send('edgeHit:') == 1):
				global2._send('newRoom:', 470)
			#end:case
			case (global0._send('edgeHit:') == 2):
				global2._send('setScript:', egoExits)
			#end:case
			case 
				(and
					proc999_5(global0._send('onControl:', 1), 64, 128)
					(not proc913_0(42))
				):
				proc913_1(81)
				global103._send('number:', 451, 'setLoop:', -1, 'play:')
				self._send('setScript:', mainGnomeScript)
			#end:case
		)
		super._send('doit:')
	#end:method

	@classmethod
	def scriptCheck():
		temp0 = 1
		if local5:
			global91._send('say:', 0, 0, 194, 1, 0, 899)
			temp0 = 0
		#endif
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class snoreSong(Sound):
	#property vars (may be empty)
	number = 962
	loop = -1
	
#end:class or instance

@SCI.instance
class oysterGuts(Prop):
	#property vars (may be empty)
	x = 60
	y = 132
	noun = 1
	view = 4531
	cel = 1
	priority = 11
	signal = 16400
	
#end:class or instance

@SCI.instance
class pearlGlint(Prop):
	#property vars (may be empty)
	x = 72
	y = 133
	view = 902
	loop = 1
	priority = 13
	signal = 16400
	
#end:class or instance

@SCI.instance
class snooze1(Prop):
	#property vars (may be empty)
	x = 66
	y = 113
	z = 20
	noun = 8
	view = 450
	loop = 3
	signal = 20480
	detailLevel = 3
	
	@classmethod
	def checkDetail(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (not detailLevel):#end:case
			case 
				(<
					if argc:
						param1
					else:
						global1._send('detailLevel:')
					#endif
					detailLevel
				):
				self._send('cel:', (self._send('lastCel:') - 1), 'stopUpd:')
			#end:case
			case cycler:
				self._send('startUpd:')
			#end:case
		)
	#end:method

#end:class or instance

@SCI.instance
class snooze4(Prop):
	#property vars (may be empty)
	x = 103
	y = 158
	z = 40
	noun = 8
	view = 450
	loop = 5
	signal = 20480
	detailLevel = 3
	
	@classmethod
	def checkDetail(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (not detailLevel):#end:case
			case 
				(<
					if argc:
						param1
					else:
						global1._send('detailLevel:')
					#endif
					detailLevel
				):
				self._send('cel:', (self._send('lastCel:') - 1), 'stopUpd:')
			#end:case
			case cycler:
				self._send('startUpd:')
			#end:case
		)
	#end:method

#end:class or instance

@SCI.instance
class oyster(Prop):
	#property vars (may be empty)
	x = 60
	y = 132
	noun = 1
	approachDist = 1000
	view = 4531
	loop = 2
	priority = 11
	signal = 16400
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				(cond
					case local5:
						global91._send('say:', 1, 0, 1, 1)
					#end:case
					case (global9._send('at:', 30)._send('owner:') != global11):
						global91._send('say:', 1, 1, 7, 1)
					#end:case
					case kernel.ScriptID(40, 0)._send('oysterDozing:'):
						global91._send('say:', 1, 1, 8, 1)
					#end:case
					else:
						global2._send('setScript:', lookAtOyster)
					#end:else
				)
			#end:case
			case 5:
				(cond
					case 
						(or
							(global9._send('at:', 30)._send('owner:') != global11)
							kernel.ScriptID(40, 0)._send('oysterDozing:')
						):
						global91._send('say:', 1, 5, 2, 1)
					#end:case
					case proc913_0(107):
						global91._send('say:', 1, 5, 3, 0)
					#end:case
					else:
						global91._send('say:', 1, 5, 4, 0)
					#end:else
				)
			#end:case
			case 2:
				if global5._send('contains:', gnomeGroup):
					global91._send('say:', 1, 0, 1, 1)
				else:
					global0._send('setScript:', oysterMessages, 0, 2)
				#endif
			#end:case
			case 42:
				if global5._send('contains:', gnomeGroup):
					global91._send('say:', 1, 0, 1, 1)
				else:
					global0._send('setScript:', oysterMessages, 0, 42)
				#endif
			#end:case
			case 66:
				global91._send('say:', 1, 66, 0, 1)
			#end:case
			case 30:
				if 
					(or
						(global9._send('at:', 30)._send('owner:') != global11)
						kernel.ScriptID(40, 0)._send('oysterDozing:')
					)
					global91._send('say:', 1, 30, 2, 1)
				else:
					global91._send('say:', 1, 30, 9, 1)
				#endif
			#end:case
			case 31:
				global1._send('handsOff:')
				global2._send('setScript:', oyFluteScript)
			#end:case
			else:
				(cond
					case global5._send('contains:', gnomeGroup):
						global91._send('say:', 1, 0, 1, 1)
					#end:case
					case 
						(or
							(global9._send('at:', 30)._send('owner:') != global11)
							kernel.ScriptID(40, 0)._send('oysterDozing:')
						):
						global91._send('say:', 1, 5, 2, 1)
					#end:case
					case proc913_0(107):
						global91._send('say:', 1, 0, 3, 1, self)
					#end:case
					else:
						global91._send('say:', 1, 0, 4, 1, self)
					#end:else
				)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class oyBlink(Prop):
	#property vars (may be empty)
	x = 60
	y = 132
	view = 4531
	loop = 1
	signal = 16384
	
#end:class or instance

@SCI.instance
class oyBlinkScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				seconds = kernel.Random(3, 8)
			#end:case
			case 1:
				client._send('show:')
				cycles = 6
			#end:case
			case 2:
				client._send('hide:')
				self._send('init:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class oyFluteScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('setMotion:', PolyPath, 140, 130, self)
			#end:case
			case 1:
				if 
					(or
						(global9._send('at:', 30)._send('owner:') != global11)
						kernel.ScriptID(40, 0)._send('oysterDozing:')
					)
					global91._send('say:', 1, 31, 2, 1, self)
				else:
					global91._send('say:', 1, 31, 9, 0, self)
				#endif
			#end:case
			case 2:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lookAtOyster(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global91._send('say:', 1, 1, 9, 1, self)
			#end:case
			case 1:
				global103._send('number:', 961, 'setLoop:', 1, 'play:')
				oysterGuts._send('init:')
				oyster._send('setPri:', 12, 'setLoop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 2:
				pearlGlint._send('init:', 'setCycle:', End, self)
			#end:case
			case 3:
				pearlGlint._send('dispose:')
				oyster._send('setCycle:', Beg, self)
			#end:case
			case 4:
				oysterGuts._send('dispose:')
				oyster._send('setLoop:', 2, 'cel:', 0, 'setPri:', 11)
				cycles = 2
			#end:case
			case 5:
				global91._send('say:', 1, 1, 9, 2, self)
			#end:case
			case 6:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class oysterMessages(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				if ((global0._send('x:') == 140) and (global0._send('y:') == 130)):
					cycles = 1
				else:
					global0._send('setMotion:', PolyPath, 140, 130, self)
				#endif
			#end:case
			case 1:
				if (global0._send('heading:') != 270):
					global0._send('setHeading:', 270, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				if 
					(and
						(register == 2)
						(global9._send('at:', 30)._send('owner:') == global11)
						(not proc913_0(107))
					)
					global91._send('say:', 1, 2, 10, 1, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 3:
				if 
					(and
						(register == 2)
						(global9._send('at:', 30)._send('owner:') == global11)
					)
					oyster._send('setPri:', 12)
				#endif
				cycles = 6
			#end:case
			case 4:
				match register
					case 2:
						(cond
							case 
								(or
									(global9._send('at:', 30)._send('owner:') != global11)
									kernel.ScriptID(40, 0)._send('oysterDozing:')
								):
								global91._send('say:', 1, 5, 2, 1, self)
							#end:case
							case proc913_0(107):
								global91._send('say:', 1, 2, 11, 0, self)
							#end:case
							else:
								proc913_1(107)
								global91._send('say:', 1, 2, 10, 2, self)
							#end:else
						)
					#end:case
					case 42:
						(cond
							case (global9._send('at:', 30)._send('owner:') != global11):
								global91._send('say:', 1, 42, 7, 1, self)
							#end:case
							case (not proc913_0(107)):
								global91._send('say:', 1, 42, 4, 1, self)
							#end:case
							case kernel.ScriptID(40, 0)._send('oysterDozing:'):
								global91._send('say:', 1, 42, 8, 1, self)
							#end:case
							case proc913_0(108):
								mySentence._send('y:', (mySentence._send('y:') - 100), 'z:', -100)
								oyBlink._send('dispose:')
								proc450_8(1)
								proc451_0(1)
								self._send('dispose:')
							#end:case
							else:
								proc913_1(108)
								global1._send('givePoints:', 2)
								mySentence._send('y:', (mySentence._send('y:') - 100), 'z:', -100)
								oyBlink._send('dispose:')
								proc450_8(1)
								proc451_0(0)
								self._send('dispose:')
							#end:else
						)
					#end:case
				#end:match
			#end:case
			case 5:
				global1._send('handsOn:')
				if (register == 2):
					oyster._send('setPri:', 11)
				#endif
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class mySentence(Actor):
	#property vars (may be empty)
	x = 160
	y = 185
	noun = 11
	view = 4501
	priority = 5
	signal = 16
	cycleSpeed = 12
	
	@classmethod
	def doVerb(param1 = None, *rest):
		(cond
			case ((param1 == 1) or (param1 == 2)):
				super._send('doVerb:', param1)
			#end:case
			case (param1 == 5):
				(cond
					case global5._send('contains:', gnomeGroup):
						global91._send('say:', 1, 0, 1, 1)
					#end:case
					case global5._send('contains:', global0):
						global1._send('handsOff:')
						global0._send('setScript:', getSentence)
					#end:case
					else:
						global91._send('say:', 11, 1, 0, 1)
					#end:else
				)
			#end:case
			else:
				global91._send('say:', 11, 0, 0, 1)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class shimmer1(Prop):
	#property vars (may be empty)
	x = 27
	y = 169
	noun = 7
	view = 447
	priority = 1
	signal = 16400
	cycleSpeed = 30
	detailLevel = 2
	
	@classmethod
	def init():
		self._send('setCycle:', Fwd)
		super._send('init:')
	#end:method

#end:class or instance

@SCI.instance
class shimmer2(Prop):
	#property vars (may be empty)
	x = 299
	y = 171
	noun = 7
	view = 447
	loop = 1
	priority = 1
	signal = 16400
	cycleSpeed = 30
	detailLevel = 2
	
	@classmethod
	def init():
		self._send('setCycle:', Fwd)
		super._send('init:')
	#end:method

#end:class or instance

@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class farFoliage(Feature):
	#property vars (may be empty)
	noun = 3
	onMeCheck = 512
	
#end:class or instance

@SCI.instance
class oysterBeds(Feature):
	#property vars (may be empty)
	noun = 8
	onMeCheck = 16
	
#end:class or instance

@SCI.instance
class oysterCouch(Feature):
	#property vars (may be empty)
	onMeCheck = 16384
	
	@classmethod
	def doVerb(param1 = None, *rest):
		oyster._send('doVerb:', param1, &rest)
	#end:method

#end:class or instance

@SCI.instance
class otherRocks(Feature):
	#property vars (may be empty)
	noun = 6
	onMeCheck = 256
	
#end:class or instance

@SCI.instance
class smallRocks(Feature):
	#property vars (may be empty)
	noun = 13
	onMeCheck = 1024
	
#end:class or instance

@SCI.instance
class sky(Feature):
	#property vars (may be empty)
	noun = 10
	onMeCheck = 2048
	
#end:class or instance

@SCI.instance
class myPath(Feature):
	#property vars (may be empty)
	noun = 9
	onMeCheck = 4096
	
#end:class or instance

@SCI.instance
class rock(Feature):
	#property vars (may be empty)
	noun = 5
	onMeCheck = 136
	
#end:class or instance

@SCI.instance
class beach(Feature):
	#property vars (may be empty)
	noun = 10
	onMeCheck = 96
	
#end:class or instance

@SCI.instance
class ocean(Feature):
	#property vars (may be empty)
	noun = 7
	onMeCheck = 8198
	
	@classmethod
	def init():
		super._send('init:', &rest)
		global93._send('add:', self)
	#end:method

	@classmethod
	def dispose():
		global93._send('delete:', self)
		super._send('dispose:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		temp0 = global80._send('curEvent:')
		match param1
			case 3:
				if 
					(and
						(or
							(global0._send('onControl:', 1) == 32)
							(global0._send('onControl:', 1) == 64)
						)
						(temp0._send('y:') > 171)
					)
					local1 = 165
					if (temp0._send('x:') < global0._send('x:')):
						local0 = (global0._send('x:') - 30)
					else:
						local0 = (global0._send('x:') + 30)
					#endif
				else:
					local0 = temp0._send('x:')
					local1 = temp0._send('y:')
				#endif
				global0._send('setScript:', inToWater, 0, 0)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

class Gnome(Actor):
	#property vars (may be empty)
	y = 127
	z = 1
	signal = 16384
	xStep = 6
	gnomesItem = 0
	msgCase = 0
	failCase = 0
	textCase = 0
	EOLx = 0
	FOLx = 0
	gnomeScript = 0
	startPoint = 0
	
#end:class or instance

@SCI.instance
class gnomeGroup(Actor):
	#property vars (may be empty)
	x = 130
	y = 71
	noun = 4
	yStep = 1
	view = 454
	signal = 16384
	cycleSpeed = 12
	illegalBits = 0
	
	@classmethod
	def cue():
		if kernel.IsObject(scaler):
			scaler._send('dispose:')
		#endif
		scaler = 0
		super._send('dispose:')
	#end:method

	@classmethod
	def dispose():
		if kernel.IsObject(scaler):
			scaler._send('dispose:')
		#endif
		scaler = 0
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class tmpGnome(Actor):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class mainGnomeScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global91._send('say:', 10, 3, 19, 1, self)
			#end:case
			case 1:
				global0._send('setMotion:', MoveTo, 236, 128, self)
			#end:case
			case 2:
				global0._send('setHeading:', 335)
				cycles = 8
			#end:case
			case 3:
				snoreSong._send('stop:')
				snooze1._send('dispose:')
				if global5._send('contains:', snooze4):
					snooze4._send('dispose:')
				#endif
				gnomeGroup._send(
					'setScale:', Scaler, 100, 30, 126, 70,
					'init:',
					'setCycle:', Walk,
					'setMotion:', MoveTo, 96, 126, self
				)
			#end:case
			case 4:
				global0._send('setHeading:', 270)
				cycles = 8
			#end:case
			case 5:
				global91._send('say:', 10, 3, 19, 2, self)
			#end:case
			case 6:
				gnomeGroup._send(
					'setScale:', 0,
					'view:', 4541,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', 146, 128,
					'setCycle:', End, self
				)
				kernel.UnLoad(128, 454)
			#end:case
			case 7:
				local5 = 1
				kernel.ScriptID(455, 0)._send('init:')
				gnomeGroup._send(
					'view:', 459,
					'loop:', -1,
					'setLoop:', 0,
					'x:', 155,
					'y:', 126,
					'stopUpd:',
					'setScript:', riddleAlex, 0, kernel.ScriptID(455, 0)
				)
				kernel.UnLoad(128, 4541)
				cycles = 2
			#end:case
			case 8:#end:case
			case 9:
				localproc_0(kernel.ScriptID(455, 0))
				kernel.ScriptID(455, 0)._send('dispose:')
				cycles = 2
			#end:case
			case 10:
				kernel.DisposeScript(455)
				kernel.UnLoad(128, 455)
				cycles = 2
			#end:case
			case 11:
				local5 = 2
				kernel.ScriptID(456, 0)._send('init:')
				gnomeGroup._send(
					'view:', 4591,
					'loop:', -1,
					'setScript:', riddleAlex, 0, kernel.ScriptID(456, 0)
				)
				tmpGnome._send('view:', 2002, 'hide:')
				kernel.UnLoad(128, 459)
				cycles = 2
			#end:case
			case 12:#end:case
			case 13:
				global0._send('setMotion:', MoveTo, (global0._send('x:') - 6), global0._send('y:'), self)
			#end:case
			case 14:
				cycles = 2
			#end:case
			case 15:
				localproc_0(kernel.ScriptID(456, 0))
				kernel.ScriptID(456, 0)._send('dispose:')
				cycles = 2
			#end:case
			case 16:
				kernel.DisposeScript(456)
				kernel.UnLoad(128, 456)
				cycles = 2
			#end:case
			case 17:
				local5 = 3
				kernel.ScriptID(4561, 0)._send('init:')
				gnomeGroup._send(
					'view:', 4592,
					'loop:', -1,
					'setScript:', riddleAlex, 0, kernel.ScriptID(4561, 0)
				)
				tmpGnome._send('view:', 2002, 'hide:')
				kernel.UnLoad(128, 4591)
				cycles = 2
			#end:case
			case 18:#end:case
			case 19:
				global0._send('setMotion:', MoveTo, (global0._send('x:') - 1), global0._send('y:'), self)
			#end:case
			case 20:
				cycles = 2
			#end:case
			case 21:
				localproc_0(kernel.ScriptID(4561, 0))
				kernel.ScriptID(4561, 0)._send('dispose:')
				cycles = 2
			#end:case
			case 22:
				kernel.DisposeScript(4561)
				kernel.UnLoad(128, 4561)
				kernel.UnLoad(128, 8933)
				cycles = 2
			#end:case
			case 23:
				local5 = 4
				kernel.ScriptID(457, 0)._send('init:')
				gnomeGroup._send(
					'view:', 4593,
					'loop:', -1,
					'setScript:', riddleAlex, 0, kernel.ScriptID(457, 0)
				)
				tmpGnome._send('view:', 2002, 'hide:')
				kernel.UnLoad(128, 4592)
				cycles = 2
			#end:case
			case 24:#end:case
			case 25:
				cycles = 4
			#end:case
			case 26:
				localproc_0(kernel.ScriptID(457, 0))
				kernel.ScriptID(457, 0)._send('dispose:')
				cycles = 2
			#end:case
			case 27:
				kernel.DisposeScript(457)
				kernel.UnLoad(128, 457)
				cycles = 2
			#end:case
			case 28:
				local5 = 5
				kernel.ScriptID(458, 0)._send('init:')
				gnomeGroup._send(
					'view:', 4594,
					'loop:', -1,
					'setScript:', riddleAlex, 0, kernel.ScriptID(458, 0)
				)
				tmpGnome._send('view:', 2002, 'hide:')
				kernel.UnLoad(128, 4593)
				cycles = 2
			#end:case
			case 29:#end:case
			case 30:
				localproc_0(kernel.ScriptID(458, 0))
				kernel.ScriptID(458, 0)._send('dispose:')
				cycles = 2
			#end:case
			case 31:
				kernel.DisposeScript(458)
				kernel.UnLoad(128, 458)
				local5 = 0
				gnomeGroup._send(
					'view:', 4544,
					'setLoop:', 1,
					'cel:', 0,
					'posn:', 110, 128,
					'setCycle:', End, self
				)
				tmpGnome._send('dispose:')
				kernel.UnLoad(128, 4593)
			#end:case
			case 32:
				gnomeGroup._send(
					'view:', 4540,
					'setScale:', Scaler, 100, 25, 126, 70,
					'setLoop:', 2,
					'x:', 106,
					'y:', 126,
					'setCycle:', Walk,
					'setMotion:', MoveTo, 131, 70, self
				)
				kernel.UnLoad(128, 4544)
			#end:case
			case 33:
				gnomeGroup._send('dispose:')
				global0._send(
					'view:', 452,
					'setLoop:', 1,
					'cel:', 0,
					'cycleSpeed:', 6,
					'setCycle:', End, self
				)
				kernel.ScriptID(40, 0)._send('alexInvisible:', 0)
			#end:case
			case 34:
				if kernel.ScriptID(40, 0)._send('alexX:'):
					temp0 = kernel.ScriptID(40, 0)._send('alexX:')
					temp1 = kernel.ScriptID(40, 0)._send('alexY:')
				else:
					temp0 = global0._send('x:')
					temp1 = global0._send('y:')
				#endif
				global0._send(
					'posn:', temp0, temp1,
					'setScale:', Scaler, 100, 30, 126, 70,
					'reset:', 1
				)
				ticks = 4
			#end:case
			case 35:
				global1._send('handsOn:')
				snoreSong._send('play:')
				snooze1._send('init:', 'setCycle:', Fwd, 'checkDetail:')
				if kernel.ScriptID(40, 0)._send('oysterDozing:'):
					snooze4._send('init:', 'setCycle:', Fwd, 'checkDetail:')
				#endif
				proc913_3()
				proc913_1(42)
				global91._send('say:', 2, 83, 14, 3)
				self._send('dispose:')
				global103._send('fade:', 0, 10, 10)
				kernel.DisposeScript(1037)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class riddleAlex(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				gnomeGroup._send(
					'setLoop:', (gnomeGroup._send('loop:') + 1),
					'x:', register._send('FOLx:'),
					'cel:', 0
				)
				cycles = 4
			#end:case
			case 1:
				gnomeGroup._send('stopUpd:')
			#end:case
			case 2:
				global103._send('number:', 452, 'setLoop:', 1, 'play:')
				register._send('setLoop:', 3, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 3:
				global1._send('handsOn:')
				global69._send('disable:', 0, 1, 3)
				if (global0._send('heading:') != 270):
					global0._send('setHeading:', 270)
				#endif
				seconds = 12
			#end:case
			case 4:
				if (global2._send('script:') != mainGnomeScript):
					0
				else:
					global1._send('handsOff:')
					proc913_1(59)
					cycles = 6
				#endif
			#end:case
			case 5:
				register._send('gnomeScript:')._send('start:', register._send('startPoint:'))
				gnomeGroup._send('setScript:', register._send('gnomeScript:'))
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class giveItemScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				temp2 = global0._send('x:')
				temp3 = global0._send('y:')
				kernel.ScriptID(40, 0)._send('alexX:', global0._send('x:'))
				kernel.ScriptID(40, 0)._send('alexY:', global0._send('y:'))
				match register
					case 37:
						self._send('setScript:', giveGnomeBird, self, register)
					#end:case
					case 83:
						self._send('setScript:', inkOutAlex, self, register)
					#end:case
					case 31:
						self._send('setScript:', blowFlute, self, register)
					#end:case
					else:
						match register
							case 47:
								temp0 = 452
								temp1 = 0
								(temp2 += 2)
								temp4 = 4
							#end:case
							case 68:
								temp4 = 4
								temp0 = 452
								temp1 = 4
							#end:case
							else:
								temp0 = 452
								temp1 = 3
								temp4 = 4
							#end:else
						#end:match
						global0._send(
							'view:', temp0,
							'setLoop:', temp1,
							'normal:', 0,
							'cel:', 0,
							'x:', temp2,
							'y:', temp3,
							'cycleSpeed:', 0,
							'setCycle:', CT, temp4, 1, self
						)
						kernel.UnLoad(128, 900)
					#end:else
				#end:match
			#end:case
			case 1:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class rightInvItem(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				match local5
					case 1:
						if (not proc913_1(145)):
							global1._send('givePoints:', 2)
						#endif
						kernel.UnLoad(128, 8931)
					#end:case
					case 2:
						if (not proc913_1(146)):
							global1._send('givePoints:', 2)
						#endif
						kernel.UnLoad(128, 8932)
					#end:case
					case 3:
						if (not proc913_1(147)):
							global1._send('givePoints:', 2)
						#endif
						kernel.UnLoad(128, 8933)
					#end:case
					case 4:
						if (not proc913_1(148)):
							global1._send('givePoints:', 2)
						#endif
						kernel.UnLoad(128, 8934)
					#end:case
					case 5:
						if (not proc913_1(149)):
							global1._send('givePoints:', 2)
						#endif
						kernel.UnLoad(128, 8935)
					#end:case
				#end:match
				global103._send('number:', 451, 'setLoop:', -1, 'play:')
				register._send(
					'setLoop:', 0,
					'cel:', 3,
					'z:', 0,
					'setPri:', 8,
					'setMotion:', MoveTo, register._send('x:'), (register._send('y:') - 4), self
				)
			#end:case
			case 1:
				register._send(
					'cel:', 0,
					'setLoop:', 5,
					'y:', 125,
					'setCycle:', Fwd,
					'setMotion:', MoveTo, register._send('EOLx:'), 125, self
				)
			#end:case
			case 2:
				register._send('loop:', 0, 'cel:', 2, 'setCycle:', 0)
				gnomeGroup._send('setCycle:', End, self)
			#end:case
			case 3:
				register._send('y:', 126, 'cel:', 0)
				ticks = 4
			#end:case
			case 4:
				mainGnomeScript._send('cue:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class wrongInvItem(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if kernel.ScriptID(40, 0)._send('alexInvisible:'):
					global0._send('view:', 452, 'setLoop:', 1, 'cel:', 0, 'setCycle:', End, self)
					kernel.ScriptID(40, 0)._send('alexInvisible:', 0)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 1:
				if kernel.ScriptID(40, 0)._send('alexX:'):
					temp0 = kernel.ScriptID(40, 0)._send('alexX:')
					temp1 = kernel.ScriptID(40, 0)._send('alexY:')
				else:
					temp0 = global0._send('x:')
					temp1 = global0._send('y:')
				#endif
				if (global0._send('view:') != 900):
					global0._send('reset:', 1, 'posn:', temp0, temp1)
				#endif
				cycles = 8
			#end:case
			case 2:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class toTheSea(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				proc913_2(59)
				global2._send('drawPic:', 450, -32758)
				if global5._send('contains:', mySentence):
					mySentence._send('setCycle:', 0, 'setMotion:', 0, 'setScript:', 0)
				#endif
				global0._send('hide:')
				global103._send('number:', 457, 'setLoop:', 1, 'play:', self)
				gnomeGroup._send(
					'view:', 4542,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', 200, 138,
					'init:',
					'setCycle:', Fwd
				)
			#end:case
			case 1:
				global104._send('number:', 458, 'setLoop:', 1, 'play:')
				gnomeGroup._send('setLoop:', 1)
				global0._send(
					'view:', 4542,
					'setLoop:', 2,
					'setPri:', 15,
					'posn:', 195, 110,
					'normal:', 0,
					'show:',
					'cycleSpeed:', 10,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				global2._send('style:', 7)
				match local5
					case 1:
						kernel.DisposeScript(455)
					#end:case
					case 2:
						kernel.DisposeScript(456)
					#end:case
					case 3:
						kernel.DisposeScript(4561)
					#end:case
					case 4:
						kernel.DisposeScript(457)
					#end:case
					case 5:
						kernel.DisposeScript(458)
					#end:case
				#end:match
				global160 = 35
				cycles = 10
			#end:case
			case 3:
				global2._send('newRoom:', 135)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class giveGnomeBird(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send(
					'view:', 883,
					'normal:', 0,
					'posn:', (global0._send('x:') - 1), (global0._send('y:') + 1),
					'loop:', 0,
					'cycleSpeed:', 50
				)
				kernel.UnLoad(128, 900)
				cycles = 6
			#end:case
			case 1:
				global104._send('number:', 930, 'setLoop:', 1, 'play:')
				global0._send('cel:', 0, 'setCycle:', End, self)
			#end:case
			case 2:
				if (local4 < 4):
					local4.post('++')
					(state -= 2)
				#endif
				self._send('cue:')
			#end:case
			case 3:
				global104._send('number:', 931, 'setLoop:', 1, 'play:', self)
				kernel.UnLoad(132, 930)
				global0._send('setLoop:', 6, 'cel:', 0, 'cycleSpeed:', 0, 'setCycle:', Fwd)
				if (local5 == 2):
					kernel.ScriptID(456, 0)._send('setLoop:', 1, 'setCycle:', Fwd)
				#endif
			#end:case
			case 4:
				global0._send('view:', 883, 'normal:', 0, 'setCycle:', 0, 'loop:', 0)
				cycles = 6
			#end:case
			case 5:
				global104._send('number:', 0)
				kernel.UnLoad(132, 931)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class inkOutAlex(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global91._send('say:', 2, 83, 14, 1, self)
			#end:case
			case 1:
				global0._send(
					'normal:', 0,
					'view:', 452,
					'setLoop:', 5,
					'cel:', 0,
					'normal:', 0,
					'posn:', (global0._send('x:') + 2), (global0._send('y:') + 1),
					'cycleSpeed:', 2,
					'setCycle:', End, self
				)
				kernel.UnLoad(128, 900)
			#end:case
			case 2:
				global0._send('setLoop:', 6, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 3:
				global0._send('put:', 51, 450)
				global69._send('curIcon:', global69._send('at:', 0))
				kernel.ScriptID(40, 0)._send('alexInvisible:', 1)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class blowFlute(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send(
					'normal:', 0,
					'view:', 920,
					'setLoop:', 1,
					'posn:', global0._send('x:'), (global0._send('y:') + 1),
					'cel:', 0,
					'cycleSpeed:', 6
				)
				kernel.UnLoad(128, 900)
				cycles = 4
			#end:case
			case 1:
				global104._send('number:', 942, 'setLoop:', 1, 'play:', self)
				global0._send('setCycle:', Fwd)
			#end:case
			case 2:
				if kernel.ScriptID(40, 0)._send('alexX:'):
					temp0 = kernel.ScriptID(40, 0)._send('alexX:')
					temp1 = kernel.ScriptID(40, 0)._send('alexY:')
				else:
					temp0 = global0._send('x:')
					temp1 = global0._send('y:')
				#endif
				global0._send('reset:', 1, 'posn:', temp0, temp1)
				cycles = 4
			#end:case
			case 3:
				kernel.UnLoad(132, 942)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoEnters(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('init:', 'setScale:', Scaler, 100, 30, 126, 70)
				if global0._send('scaler:'):
					global0._send('scaler:')._send('doit:')
				#endif
				match global12
					case 460:
						global0._send('posn:', 345, 90, 'setMotion:', PolyPath, 300, 90, self)
					#end:case
					case 470:
						global0._send('posn:', 130, 72, 'setMotion:', PolyPath, 134, 101, self)
					#end:case
					else:
						global0._send(
							'signal:', (| global0._send('signal:') 0x4000),
							'posn:', 228, 121,
							'loop:', 0
						)
						ticks = 6
					#end:else
				#end:match
			#end:case
			case 1:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoExits(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send(
					'setMotion:', PolyPath, (global0._send('x:') + 15), global0._send('y:'), self
				)
			#end:case
			case 1:
				global2._send('newRoom:', 460)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class inToWater(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				if ((mySentence._send('y:') > 158) and (not sentencePoly._send('points:'))):
					mySentence._send('ignoreActors:', 1)
					global2._send(
						'addObstacle:', sentencePoly._send(
								'type:', 2,
								'init:', (mySentence._send('x:') - 18), mySentence._send(
										'y:'
									), (mySentence._send('x:') - 10), (-
										mySentence._send('y:')
										5
									), (mySentence._send('x:') + 17), (-
										mySentence._send('y:')
										5
									), (mySentence._send('x:') + 24), mySentence._send(
										'y:'
									), (mySentence._send('x:') + 18), (+
										mySentence._send('y:')
										17
									), (mySentence._send('x:') - 10), (+
										mySentence._send('y:')
										17
									),
								'yourself:'
							)
					)
					cycles = 2
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				global0._send('setMotion:', PolyPath, local0, local1, self)
			#end:case
			case 2:
				cycles = 4
			#end:case
			case 3:
				(cond
					case (register == mySentence):
						myConv._send('add:', -1, 7, 3, 17, 1, 'add:', -1, 7, 3, 17, 2, 'init:', self)
					#end:case
					case 
						(or
							(global0._send('onControl:', 1) == 4)
							(global0._send('onControl:', 1) == 2)
						):
						global91._send('say:', 7, 3, 16, 1, self)
					#end:case
					case (global0._send('onControl:', 1) == 8192):
						myConv._send('add:', -1, 7, 3, 17, 1, 'add:', -1, 7, 3, 17, 2, 'init:', self)
					#end:case
					else:
						cycles = 1
					#end:else
				)
			#end:case
			case 4:
				if 
					(or
						(global0._send('onControl:', 1) == 8192)
						(register == mySentence)
					)
					cycles = 1
				else:
					global1._send('handsOn:')
					self._send('dispose:')
				#endif
			#end:case
			case 5:
				local2 = 1
				global103._send('number:', 921, 'setLoop:', 1, 'play:')
				global0._send(
					'view:', 309,
					'cel:', 0,
					'normal:', 0,
					'cycleSpeed:', 6,
					'posn:', global0._send('x:'), (global0._send('y:') + 15),
					'setCycle:', End, self
				)
			#end:case
			case 6:
				global1._send('handsOn:')
				global160 = 34
				global2._send('newRoom:', 135)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class sentencePoly(Polygon):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class sentenceFloat(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				seconds = 20
			#end:case
			case 1:
				mySentence._send('setStep:', 1, 1, 'setLoop:', 2)
				(cond
					case (mySentence._send('y:') > 175):
						mySentence._send('setMotion:', MoveTo, 135, 175, self)
					#end:case
					case (mySentence._send('y:') > 158):
						mySentence._send('setMotion:', MoveTo, 120, 154, self)
					#end:case
					else:
						self._send('dispose:')
					#end:else
				)
			#end:case
			case 2:
				if ((mySentence._send('y:') < 158) and (not sentencePoly._send('points:'))):
					mySentence._send('ignoreActors:', 1)
					global2._send(
						'addObstacle:', sentencePoly._send(
								'type:', 2,
								'init:', (mySentence._send('x:') - 18), mySentence._send(
										'y:'
									), (mySentence._send('x:') - 10), (-
										mySentence._send('y:')
										5
									), (mySentence._send('x:') + 17), (-
										mySentence._send('y:')
										5
									), (mySentence._send('x:') + 24), mySentence._send(
										'y:'
									), (mySentence._send('x:') + 18), (+
										mySentence._send('y:')
										17
									), (mySentence._send('x:') - 10), (+
										mySentence._send('y:')
										17
									),
								'yourself:'
							)
					)
				#endif
				self._send('init:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getSentence(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				mySentence._send('setMotion:', 0, 'setScript:', 0)
				if ((mySentence._send('y:') > 158) and (not sentencePoly._send('points:'))):
					mySentence._send('ignoreActors:', 1)
					global2._send(
						'addObstacle:', sentencePoly._send(
								'type:', 2,
								'init:', (mySentence._send('x:') - 18), mySentence._send(
										'y:'
									), (mySentence._send('x:') - 10), (-
										mySentence._send('y:')
										5
									), (mySentence._send('x:') + 17), (-
										mySentence._send('y:')
										5
									), (mySentence._send('x:') + 24), mySentence._send(
										'y:'
									), (mySentence._send('x:') + 18), (+
										mySentence._send('y:')
										17
									), (mySentence._send('x:') - 10), (+
										mySentence._send('y:')
										17
									),
								'yourself:'
							)
					)
				#endif
				if 
					(and
						(or
							(global0._send('onControl:', 1) == 32)
							(global0._send('onControl:', 1) == 64)
						)
						(mySentence._send('y:') > 158)
					)
					local3 = 1
					global91._send('say:', 11, 5, 20, 1, self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 1:
				global0._send(
					'setMotion:', PolyPath, mySentence._send('x:'), (-
							mySentence._send('y:')
							11
						), self
				)
			#end:case
			case 2:
				global0._send('setHeading:', 180)
				cycles = 8
			#end:case
			case 3:
				(cond
					case (local3 and (mySentence._send('y:') > 158)):
						global91._send('say:', 11, 5, 20, 2, self)
					#end:case
					case (mySentence._send('y:') > 158):
						global91._send('say:', 11, 5, 21, 1, self)
					#end:case
					else:
						self._send('cue:')
					#end:else
				)
			#end:case
			case 4:
				(cond
					case (local3 and (mySentence._send('y:') > 158)):
						local3 = 0
						global1._send('handsOn:')
						self._send('dispose:')
					#end:case
					case (mySentence._send('y:') > 160):
						local0 = global0._send('x:')
						local1 = (global0._send('y:') + 1)
						self._send('dispose:')
						mySentence._send(
							'setStep:', 20, 15,
							'setLoop:', 2,
							'setMotion:', MoveTo, (mySentence._send('x:') - 28), mySentence._send(
									'y:'
								)
						)
						global2._send('setScript:', inToWater, 0, mySentence)
					#end:case
					else:
						self._send('cue:')
					#end:else
				)
			#end:case
			case 5:
				global2._send('setScript:', pickUpSentence, self)
				global2._send('obstacles:')._send('delete:', sentencePoly)
				sentencePoly._send('dispose:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class pickUpSentence(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send(
					'view:', 311,
					'setLoop:', 1,
					'normal:', 0,
					'cel:', 0,
					'setPri:', global0._send('priority:'),
					'posn:', (global0._send('x:') - 2), (global0._send('y:') + 11),
					'cycleSpeed:', 6,
					'setCycle:', CT, 2, 1, self
				)
			#end:case
			case 1:
				mySentence._send('dispose:')
				global104._send('number:', 924, 'setLoop:', 1, 'play:')
				global0._send('setCycle:', End, self)
			#end:case
			case 2:
				global1._send('givePoints:', 1)
				global0._send(
					'reset:', 2,
					'posn:', (global0._send('x:') + 2), (global0._send('y:') - 11),
					'get:', 50
				)
				cycles = 8
			#end:case
			case 3:
				global91._send('say:', 11, 5, 0, 0, self)
			#end:case
			case 4:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class resetGnomes(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				match local5
					case 1:
						mainGnomeScript._send('start:', 8)
					#end:case
					case 2:
						mainGnomeScript._send('start:', 12)
					#end:case
					case 3:
						mainGnomeScript._send('start:', 18)
					#end:case
					case 4:
						mainGnomeScript._send('start:', 24)
					#end:case
					case 5:
						mainGnomeScript._send('start:', 29)
					#end:case
				#end:match
				global2._send('setScript:', mainGnomeScript)
				gnomeGroup._send('script:')._send(
					'state:', (gnomeGroup._send('script:')._send('state:') - 1),
					'cue:'
				)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoDoVerb(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 12:
				if 
					(or
						(global0._send('onControl:', 1) == 32)
						(global0._send('onControl:', 1) == 64)
					)
					if global2._send('script:'):
						kernel.ScriptID(130)._send('next:', resetGnomes)
					#endif
					global2._send('setScript:', 130)
					return 1
				else:
					global2._send('setScript:', 130)
					return 1
				#endif
			#end:case
			case 31:
				if local5:
					localproc_1(param1)
					return 1
				else:
					return 0
				#endif
			#end:case
			case 37:
				if local5:
					localproc_1(param1)
					return 1
				else:
					return 0
				#endif
			#end:case
			case 83:
				if local5:
					localproc_1(param1)
					return 1
				else:
					return 0
				#endif
			#end:case
			else:
				return 0
			#end:else
		#end:match
	#end:method

#end:class or instance

