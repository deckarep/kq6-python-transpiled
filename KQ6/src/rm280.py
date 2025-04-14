#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 280
import sci_sh
import kernel
import Main
import KQ6Room
import n913
import Scaler
import Polygon
import Feature
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm280 = 0,
	map = 1,
	shopOwner = 2,
	shopDoor = 3,
	smBird = 4,
	smTinderBox = 5,
	smFlute = 6,
	smPBrush = 7,
	proc280_8 = 8,
	shopOwnerScr = 9,
	proc280_10 = 10,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = -1
local2 = -1
local3 = None
local4 = [22, 129, 22, 157, 217, 157, 250, 157, 241, 148, 214, 148, 184, 127, 210, 127, 210, 121, 188, 121, 160, 121, 139, 133, 88, 133, 61, 133, 57, 120, 40, 120]
local36 = [22, 129, 22, 157, 217, 157, 250, 157, 241, 148, 214, 148, 184, 127, 210, 127, 210, 121, 188, 121, 160, 121, 141, 131, 86, 131, 78, 122, 40, 120]
local66 = None
local67 = [51, 152, 135, 150, 255, 133, 311, 165, 202, 157, 235, 154, -1]
local80 = None


@SCI.procedure
def proc280_10(param1 = None, *rest):
	(cond
		case shopOwner._send('cycler:'):
			removeOwnerScr._send('client:', removeOwnerScr, 'register:', param1)
			shopOwner._send('cycler:')._send('caller:', removeOwnerScr)
		#end:case
		case (shopOwnerScr._send('state:') == 5):
			removeOwnerScr._send('client:', removeOwnerScr, 'register:', param1)
			shopOwnerScr._send('register:', removeOwnerScr, 'seconds:', 0, 'ticks:', 1)
		#end:case
		else:
			shopOwner._send('setScript:', 0)
			param1._send('cue:')
		#end:else
	)
#end:procedure

@SCI.procedure
def proc280_8(param1 = None, *rest):
	if param1:
		global2._send(
			'addObstacle:', roomPoly._send('type:', 3, 'points:', @local4, 'size:', 16, 'yourself:')
		)
	else:
		global2._send(
			'addObstacle:', roomPoly._send('type:', 3, 'points:', @local36, 'size:', 15, 'yourself:')
		)
	#endif
#end:procedure

@SCI.instance
class rm280(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 280
	autoLoad = 0
	
	@classmethod
	def init():
		super._send('init:', &rest)
		if (global12 == 240):
			shopDoor._send('cel:', 5, 'init:', 'setScript:', doorScr)
		else:
			shopDoor._send('init:')
		#endif
		if ((global12 == 145) and proc913_0(41)):
			global0._send('posn:', 190, 138)
		else:
			global0._send('posn:', 51, 121)
		#endif
		global0._send('init:', 'reset:', 'loop:', 9, 'cel:', 0, 'setScale:', Scaler, 105, 90, 139, 121)
		shopOwner._send('init:')
		mints._send('init:')
		if (global9._send('at:', 48)._send('owner:') == global11):
			smTinderBox._send('init:')
		#endif
		if (global9._send('at:', 3)._send('owner:') == global11):
			smPBrush._send('init:')
		#endif
		if (global9._send('at:', 27)._send('owner:') == global11):
			smBird._send('init:')
		#endif
		if (global9._send('at:', 14)._send('owner:') == global11):
			smFlute._send('init:')
		#endif
		if (proc913_0(29) and proc913_0(30) and (not global0._send('has:', 0))):
			map._send('init:')
		#endif
		(cond
			case ((global12 == 145) and proc913_0(41)):
				global102._send('number:', 240, 'loop:', -1, 'play:', 70)
				global1._send('handsOn:')
			#end:case
			case (global12 == 145):
				global2._send('setScript:', kernel.ScriptID(282, 0))
			#end:case
			case 
				(or
					(proc913_0(17) and (not global0._send('has:', 0)))
					(and
						(not proc913_0(82))
						(not proc913_0(28))
						proc999_5(global153, 4, 5)
					)
					(and
						(not proc913_0(82))
						(global153 == 5)
						proc913_0(15)
						(not proc913_1(158))
					)
				):
				if ((not proc913_0(158)) and (global153 == 5) and proc913_0(15)):
					proc913_1(158)
				#endif
				proc913_1(28)
				kernel.ScriptID(281, 0)._send('init:', 1)
				local66 = 1
			#end:case
			case ((not proc913_0(28)) and (global153 == 3)):
				proc913_1(28)
				kernel.ScriptID(281, 0)._send('init:', 0)
				local66 = 1
			#end:case
		)
		global32._send(
			'add:', genericFeatures, eastShelf, northShelf,
			'eachElementDo:', #init
		)
		if (not global2._send('script:')):
			local80 = 1
			shopOwner._send(
				'setScript:', shopOwnerScr, 0, (0 if (global12 == 145) else 1)
			)
		#endif
		proc280_8(local66)
	#end:method

	@classmethod
	def scriptCheck(param1 = None, *rest):
		temp0 = 1
		if (param1 == 87):
			if global5._send('contains:', kernel.ScriptID(281, 0)):
				global2._send('setScript:', kernel.ScriptID(282, 1))
			else:
				global2._send('setScript:', kernel.ScriptID(282, 5))
			#endif
			temp0 = 0
		#endif
		return temp0
	#end:method

	@classmethod
	def dispose():
		if (global13 == 240):
			global102._send('fade:', 127, 15, 15, 0)
			kernel.ScriptID(10, 0)._send('setIt:', 512)
		else:
			global102._send('fade:')
		#endif
		kernel.ScriptID(281, 0)._send('dispose:')
		kernel.DisposeScript(969)
		kernel.DisposeScript(923)
		kernel.DisposeScript(283)
		kernel.DisposeScript(282)
		proc913_2(49)
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class exitScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				cycles = 2
			#end:case
			case 1:
				global0._send('setHeading:', 270, self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				global0._send(
					'setSpeed:', 6,
					'normal:', 0,
					'setPri:', 1,
					'view:', 2812,
					'loop:', 0,
					'cel:', 0,
					'posn:', 47, 125,
					'setScale:', 0,
					'scaleX:', 117,
					'scaleY:', 117,
					'scaleSignal:', 1,
					'setCycle:', CT, 2, 1, self
				)
			#end:case
			case 4:
				global105._send('number:', 901, 'loop:', 1, 'play:')
				shopDoor._send('setCycle:', End, self)
				global0._send('setCycle:', End, self)
			#end:case
			case 5: 0#end:case
			case 6:
				cycles = 1
			#end:case
			case 7:
				global2._send('newRoom:', 240)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class doorScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				ticks = 45
			#end:case
			case 1:
				client._send('cycleSpeed:', 8, 'setCycle:', Beg, self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				client._send('stopUpd:')
				global105._send('number:', 902, 'loop:', 1, 'play:', self)
			#end:case
			case 4:
				cycles = 2
			#end:case
			case 5:
				kernel.UnLoad(132, 902)
			#end:case
			case 6:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class removeOwnerScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global78._send('add:', self)
				cycles = 2
			#end:case
			case 1:
				client = 0
				global78._send('delete:', self)
				proc280_10(register)
				state = -1
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class shopOwnerScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if register:
					client._send('view:', 2841, 'loop:', 1, 'cel:', 0)
				#endif
				seconds = 2
			#end:case
			case 1:
				if register:
					client._send('setCycle:', End, self)
				else:
					ticks = 1
				#endif
			#end:case
			case 2:
				client._send('view:', 280, 'loop:', 8, 'posn:', 236, 127, 'cel:', 0)
				if (local80 and register):
					local80 = 0
					global1._send('handsOn:')
					global91._send('say:', 1, 0, (67 if (global153 > 1) else 66))
				#endif
				client._send('stopUpd:')
				seconds = kernel.Random(10, 20)
			#end:case
			case 3:
				state = (kernel.Random(4, 5) - 1)
				cycles = 1
			#end:case
			case 4:
				client._send('view:', 285, 'loop:', 0, 'cel:', 0, 'setCycle:', End, self)
				state = 1
			#end:case
			case 5:
				client._send('view:', 2852, 'loop:', 0, 'cel:', 0, 'setCycle:', End)
				seconds = 10
			#end:case
			case 6:
				client._send(
					'view:', 2853,
					'loop:', 0,
					'cel:', 0,
					'setCycle:', End, (register if register else removeOwnerScr)
				)
				state = 1
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		register = 0
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class genericTalkScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				proc280_10(self)
				global0._send('normal:', 0, 'view:', 280, 'loop:', 7, 'cel:', 0)
				cycles = 2
			#end:case
			case 1:
				kernel.UnLoad(128, 900)
			#end:case
			case 2:
				global91._send('say:', 4, 2, register, 0, self)
			#end:case
			case 3:
				global0._send('reset:', 0)
				kernel.ScriptID(280, 2)._send('setScript:', kernel.ScriptID(280, 9))
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class shopOwner(Actor):
	#property vars (may be empty)
	x = 236
	y = 127
	noun = 4
	approachX = 192
	approachY = 133
	view = 2841
	signal = 20481
	
	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('approachVerbs:', 2, 70)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		(cond
			case (param1 == 2):
				(cond
					case (global153 > 1):
						global2._send('setScript:', kernel.ScriptID(284, 5))
					#end:case
					case (not proc913_1(64)):
						global2._send('setScript:', genericTalkScr, 0, 61)
					#end:case
					case ((not proc913_0(29)) and (not proc913_1(30))):
						global2._send('setScript:', genericTalkScr, 0, 11)
					#end:case
					case (not proc913_0(29)):
						global2._send('setScript:', genericTalkScr, 0, 12)
					#end:case
					case (not proc913_1(30)):
						global2._send('setScript:', kernel.ScriptID(284, 0))
					#end:case
					else:
						global2._send('setScript:', genericTalkScr, 0, 14)
					#end:else
				)
			#end:case
			case (param1 == 70):
				(cond
					case ((global153 == 1) and (not global5._send('contains:', map))):
						global2._send('setScript:', kernel.ScriptID(284, 1), self)
					#end:case
					case (global153 == 1):
						global2._send('setScript:', kernel.ScriptID(284, 2))
					#end:case
					case ((global153 != 1) and global0._send('has:', 0)):
						global2._send('setScript:', kernel.ScriptID(284, 3))
					#end:case
					else:
						global2._send('setScript:', kernel.ScriptID(284, 4))
					#end:else
				)
			#end:case
			case (param1 == 40):
				if global5._send('contains:', map):
					global2._send('setScript:', kernel.ScriptID(283, 3))
				else:
					global2._send('setScript:', kernel.ScriptID(283, 1))
				#endif
			#end:case
			case proc999_5(param1, 37, 20, 29, 31):
				global2._send('setScript:', kernel.ScriptID(283, 2), 0, param1)
			#end:case
			case (param1 == 66):
				if global0._send('has:', 0):
					global2._send('setScript:', kernel.ScriptID(285, 0), 0, proc913_0(36))
				else:
					global2._send('setScript:', kernel.ScriptID(285, 1), 0, proc913_0(36))
				#endif
				proc913_1(36)
			#end:case
			case (param1 == 12):
				global2._send('setScript:', kernel.ScriptID(285, 2))
			#end:case
			case proc999_5(param1, 13, 42, 27, 28, 39, 45, 7, 83):
				if proc999_5(param1, 27, 28):
					param1 = 42
				#endif
				global2._send('setScript:', kernel.ScriptID(286, 5), 0, param1)
			#end:case
			case 
				(or
					proc999_5(param1, 8, 30, 47, 48, 52, 68, 38, 16)
					proc999_5(param1, 85, 17, 35, 51, 32)
					(and
						proc999_5(param1, 92, 43, 57, 58, 59, 60, 96, 56)
						param1 = 92
					)
				):
				if (param1 == 17):
					param1 = 48
				#endif
				global2._send('setScript:', kernel.ScriptID(286, 4), 0, param1)
			#end:case
			case 
				(or
					proc999_5(param1, 5, 1, 49, 15, 18, 50, 54)
					proc999_5(param1, 63, 65, 33, 69, 25, 94, 34, 24)
				):
				if (param1 == 50):
					param1 = 49
				#endif
				if (param1 == 18):
					param1 = 15
				#endif
				super._send('doVerb:', param1)
			#end:case
			else:
				global2._send('setScript:', kernel.ScriptID(286, 4))
			#end:else
		)
	#end:method

#end:class or instance

class SmallItem(View):
	#property vars (may be empty)
	noun = 9
	approachX = 190
	approachY = 138
	view = 280
	loop = 6
	signal = 16401
	
	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('approachVerbs:', 5, 1)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		if proc999_5(param1, 5, 1):
			global2._send('setScript:', kernel.ScriptID(283, 4))
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class smPBrush(SmallItem):
	#property vars (may be empty)
	x = 229
	y = 117
	cel = 5
	priority = 12
	
#end:class or instance

@SCI.instance
class smFlute(SmallItem):
	#property vars (may be empty)
	x = 220
	y = 111
	cel = 2
	priority = 10
	
#end:class or instance

@SCI.instance
class smTinderBox(SmallItem):
	#property vars (may be empty)
	x = 216
	y = 115
	cel = 4
	priority = 12
	
#end:class or instance

@SCI.instance
class smBird(SmallItem):
	#property vars (may be empty)
	x = 213
	y = 109
	cel = 3
	priority = 10
	
#end:class or instance

@SCI.instance
class map(View):
	#property vars (may be empty)
	x = 236
	y = 127
	noun = 6
	view = 280
	loop = 6
	priority = 9
	signal = 4113
	
#end:class or instance

@SCI.instance
class shopDoor(Prop):
	#property vars (may be empty)
	x = 39
	y = 126
	noun = 14
	approachX = 56
	approachY = 125
	view = 280
	loop = 2
	signal = 20481
	
	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('approachVerbs:', 5)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		if (param1 == 5):
			self._send('setScript:', exitScr)
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class takeMintScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				if (not proc913_1(90)):
					global1._send('givePoints:', 1)
				#endif
				global0._send(
					'setSpeed:', 7,
					'normal:', 0,
					'view:', 2813,
					'loop:', 0,
					'posn:', 176, 133,
					'get:', 23,
					'setCycle:', End, self
				)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				global0._send('reset:', 0, 'posn:', mints._send('approachX:'), mints._send('approachY:'))
				cycles = 2
			#end:case
			case 3:
				kernel.UnLoad(128, 2813)
				global91._send('say:', 7, 5, 34, 1, self)
			#end:case
			case 4:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class mints(View):
	#property vars (may be empty)
	x = 201
	y = 110
	noun = 7
	approachX = 180
	approachY = 131
	view = 280
	loop = 3
	priority = 9
	signal = 16401
	
	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('approachVerbs:', 5, 1)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				if (global153 < 3):
					if (not global0._send('has:', 23)):
						global2._send('setScript:', takeMintScr)
					else:
						global91._send('say:', noun, param1, 35)
					#endif
				else:
					global91._send('say:', 7, 5, 32)
				#endif
			#end:case
			case 1:
				if (global153 < 3):
					global91._send('say:', noun, param1, 33)
				else:
					global91._send('say:', noun, param1, 32)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class firstWallLookScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global91._send(
					'say:', register, 1, (58 if (register == 17) else 49), 0, self
				)
			#end:case
			case 1:
				global91._send('say:', register, 1, 50, 0, self)
			#end:case
			case 2:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class northShelf(Feature):
	#property vars (may be empty)
	x = 205
	y = 85
	sightAngle = 45
	onMeCheck = 128
	
	@classmethod
	def init():
		super._send('init:', &rest)
		(state |= 0x0004)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		noun = 17
		match param1
			case 1:
				if ((local1 + 1) == 0):
					global2._send('setScript:', firstWallLookScr, 0, noun)
					(local1 += 2)
				else:
					global91._send(
						'say:', noun, param1, match local1.post('++')
								case 0: 0#end:case
								case 1: 50#end:case
								case 2: 51#end:case
								case 3: 52#end:case
								case 4: 53#end:case
								case 5: 54#end:case
								case 6: 55#end:case
								case 7: 56#end:case
								case 8: 57#end:case
								case 9: 59#end:case
								case 10:
									local1 = 0
									60
								#end:case
							#end:match
					)
				#endif
			#end:case
			else:
				(cond
					case 
						(or
							(and
								(global66._send('doit:', param1) == -32768)
								(param1 = 0 or 1)
							)
							(param1 == 5)
						):
						noun = 27
					#end:case
					case (param1 == 2):
						noun = 16
					#end:case
				)
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class eastShelf(Feature):
	#property vars (may be empty)
	x = 280
	y = 90
	sightAngle = 45
	onMeCheck = 256
	
	@classmethod
	def init():
		super._send('init:', &rest)
		(state |= 0x0004)
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		return (super._send('onMe:', param1, &rest) and (param1._send('x:') > 119))
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		noun = 16
		match param1
			case 1:
				if ((local2 + 1) == 0):
					global2._send('setScript:', firstWallLookScr, 0, noun)
					(local2 += 2)
				else:
					global91._send(
						'say:', noun, param1, match local2.post('++')
								case 0: 50#end:case
								case 1: 51#end:case
								case 2: 52#end:case
								case 3: 53#end:case
								case 4: 54#end:case
								case 5: 55#end:case
								case 6: 56#end:case
								case 7:
									local2 = 0
									57
								#end:case
							#end:match
					)
				#endif
			#end:case
			else:
				if 
					(or
						(and
							(global66._send('doit:', param1) == -32768)
							(param1 = 0 or 1)
						)
						(param1 == 5)
					)
					noun = 27
				#endif
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class roomPoly(Polygon):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class genericFeatures(Feature):
	#property vars (may be empty)
	sightAngle = 45
	
	@classmethod
	def init():
		super._send('init:', &rest)
		(state |= 0x0004)
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		temp0 = kernel.OnControl(4, param1._send('x:'), param1._send('y:'))
		self._send('x:', param1._send('x:'), 'y:', param1._send('y:'))
		local3 = 0
		(= noun
			match temp0
				case 2:
					(8 if (param1._send('y:') > 85) else 15)
				#end:case
				case 4:
					if (param1._send('y:') > 136):
						local3 = 2
						23
					else:
						local3 = 3
						18
					#endif
				#end:case
				case 8:
					if (param1._send('y:') > 146):
						local3 = 3
						28
					else:
						22
					#endif
				#end:case
				case 16: 36#end:case
				case 32:
					local3 = 3
					20
				#end:case
				case 256:
					(32 if (param1._send('x:') < 120) else 0)
				#end:case
				case 64:
					if (param1._send('y:') > 131):
						29
					else:
						local3 = 2
						21
					#endif
				#end:case
				case 128:
					(27 if (param1._send('y:') > 131) else 0)
				#end:case
				case 512:
					if (param1._send('x:') > 176):
						local3 = 2
						31
					else:
						local3 = 2
						24
					#endif
				#end:case
				case 1024:
					if (param1._send('x:') > 98):
						local3 = 3
						30
					else:
						19
					#endif
				#end:case
				case 8192: 19#end:case
				else: 0#end:else
			#end:match
		)
		return noun
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		if 
			(or
				(and
					(global66._send('doit:', param1) == -32768)
					(local3 & 0x0002)
					(param1 = 0 or 1)
				)
				((param1 == 5) and (local3 & 0x0001))
			)
			global91._send('say:', 27, param1)
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

#end:class or instance

