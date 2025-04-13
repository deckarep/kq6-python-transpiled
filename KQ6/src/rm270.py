#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 270
import sci_sh
import kernel
import Main
import KQ6Print
import KQ6Room
import CartoonScript
import n913
import Scaler
import Polygon
import Feature
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm270 = 0,
	bookStand = 1,
	shopOwner = 2,
	clownBook = 3,
	shopDoor = 4,
	clownChair = 5,
	spellBook = 6,
	proc270_7 = 7,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = [268, 160, -4095, 4, 151, 168, -4095, 6, 141, 164, -4095, 4, -4094, 133, 160, 43, 152, -4095, 6, -4094, 37, 148, 34, 116, -4095, 4, -4094, 29, 110, -7, 114, -4092]
local32 = [182, 28, -4095, 8, 160, 14, -4088, -4094, 171, 18, 101, -4, -4092]
local45 = [16, 36, -4095, 7, 14, 72, -4095, 5, 48, 69, -4095, 4, -5, 69, -4092]
local60 = [64, -4, -4095, 9, 96, 17, 128, -4, -4092, 0]
local70 = [129, 123, 119, 133, 102, 133, 85, 138, 59, 148, 84, 165, 112, 178, 315, 178, 303, 166, 254, 166, 286, 132, 314, 132, 314, 121, 207, 119, 168, 119, 152, 114]
local102 = [129, 123, 119, 133, 102, 133, 85, 138, 59, 148, 84, 165, 112, 178, 315, 178, 303, 166, 254, 166, 286, 132, 314, 132, 314, 121, 207, 119, 152, 114]
local132 = None
local133 = -1
local134 = None


@SCI.procedure
def localproc_0(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	if param1:
		global2._send(
			'addObstacle:', roomPoly._send('type:', 3, 'points:', @local70, 'size:', 16, 'yourself:')
		)
	else:
		global2._send(
			'addObstacle:', roomPoly._send('type:', 3, 'points:', @local102, 'size:', 15, 'yourself:')
		)
	#endif
#end:procedure

@SCI.procedure
def proc270_7(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	if shopOwner._send('script:'):
		shopOwnerScr._send('caller:', param1)
		if (shopOwnerScr._send('state:') == 0):
			shopOwnerScr._send('dispose:')
		#endif
	else:
		param1._send('cue:')
	#endif
#end:procedure

@SCI.instance
class rm270(KQ6Room):
	#property vars (may be empty)
	noun = 15
	picture = 270
	autoLoad = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global2._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 231, 124, 247, 129, 197, 136, 180, 132, 180, 123,
					'yourself:'
				)
		)
		super._send('init:', &rest)
		global0._send('init:', 'posn:', 92, 144, 'reset:', 0, 'setScale:', Scaler, 108, 83, 170, 113)
		global32._send(
			'add:', genericFeatures, poemShelf, clownChair, readingTable, bookStand, shelfFeatures, frontCounter,
			'eachElementDo:', #init
		)
		fire._send('setCycle:', Fwd, 'init:')
		shopDoor._send('init:', 'setCycle:', Beg, shopDoor)
		if (global9._send('at:', 45)._send('owner:') == global11):
			spellBook._send('init:')
		#endif
		if (not proc999_5(global9._send('at:', 1)._send('owner:'), global0, -1)):
			kernel.ScriptID(273, 0)._send('init:')
		#endif
		shopOwner._send('init:')
		if (not proc913_0(27)):
			proc913_2(54)
			proc913_1(53)
		#endif
		(cond
			case (not proc913_0(16)):
				proc913_1(27)
				kernel.ScriptID(271, 0)._send('init:')
				local132 = 1
				clownBook._send('init:')
			#end:case
			case 
				(and
					proc913_0(16)
					(global153 == 1)
					(not proc913_0(26))
					proc913_0(54)
				):
				proc913_1(26)
				kernel.ScriptID(274, 0)._send('init:')
				proc913_2(54)
				proc913_1(53)
			#end:case
			case 
				(or
					(and
						(global153 == 1)
						proc913_0(26)
						proc913_0(53)
						(not proc913_0(54))
					)
					(and
						(global153 == 2)
						(not proc913_0(54))
						(not proc913_0(10))
					)
					((not proc913_0(54)) and proc999_5(global153, 3, 4))
				):
				kernel.ScriptID(274, 0)._send('init:')
				if (proc913_0(10) and proc999_5(global153, 3, 4)):
					global2._send('setScript:', kernel.ScriptID(277, 1))
				#endif
			#end:case
			else:
				clownBook._send('init:')
			#end:else
		)
		if (not global2._send('script:')):
			if (not kernel.ScriptID(10, 0)._send('isSet:', 64)):
				kernel.ScriptID(10, 0)._send('setIt:', 64)
				global2._send('setScript:', ownerFromCounterScr)
			else:
				global2._send('setScript:', ownerNotAtCounterScr)
			#endif
		#endif
		if (not global5._send('contains:', clownBook)):
			global102._send('number:', 780, 'loop:', -1, 'play:')
		#endif
		proc913_1(27)
		if (not global2._send('script:')):
			global1._send('handsOn:')
		#endif
		localproc_0(local132)
	#end:method

	@classmethod
	def scriptCheck(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 1
		if kernel.ScriptID(10, 0)._send('isSet:', 2):
			kernel.ScriptID(10, 0)._send('clrIt:', 2)
		#endif
		match param1
			case 87:
				global91._send('say:', 0, 0, 14, 0, 0, 899)
				temp0 = 0
			#end:case
			case 190:
				temp0 = 1
			#end:case
		#end:match
		return temp0
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (global102._send('number:') == 240):
			kernel.ScriptID(10, 0)._send('setIt:', 512)
			global102._send('fade:', 127, 15, 15, 0)
		else:
			global102._send('fade:')
		#endif
		super._send('dispose:')
		kernel.DisposeScript(923)
		kernel.DisposeScript(11)
		kernel.DisposeScript(271)
		kernel.DisposeScript(272)
		kernel.DisposeScript(273)
		kernel.DisposeScript(274)
		kernel.DisposeScript(276)
	#end:method

#end:class or instance

@SCI.instance
class spider(Actor):
	#property vars (may be empty)
	noun = 22
	view = 270
	loop = 4
	priority = 15
	signal = 2064
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:')
		self._send('setCycle:', Walk)
	#end:method

#end:class or instance

@SCI.instance
class spiderScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				local133 = -1
				(= local134
					match kernel.Random(0, 3)
						case 0: @local0#end:case
						case 1: @local32#end:case
						case 2: @local45#end:case
						case 3: @local60#end:case
					#end:match
				)
				spider._send(
					'posn:', proc999_6(local134, local133.post('++')), proc999_6(local134, (++
							local133
						))
				)
				cycles = 2
			#end:case
			case 1:
				match temp0 = proc999_6(local134, local133.post('++'))
					case -4088:
						spider._send('setScale:', 0)
					#end:case
					case -4095:
						spider._send('setLoop:', proc999_6(local134, local133.post('++')))
						state.post('--')
						cycles = 1
					#end:case
					case -4094:
						spider._send(
							'posn:', proc999_6(local134, local133.post('++')), proc999_6(local134, (++
									local133
								))
						)
						state.post('--')
						cycles = 1
					#end:case
					case -4092:
						state.post('++')
						ticks = 1
					#end:case
					else:
						spider._send(
							'cycleSpeed:', kernel.Random(3, 8),
							'moveSpeed:', kernel.Random(3, 8),
							'setMotion:', MoveTo, temp0, proc999_6(local134, (++
									local133
								)), self
						)
					#end:else
				#end:match
			#end:case
			case 2:
				state = 0
				if (not kernel.Random(0, 1)):
					seconds = kernel.Random(3, 5)
				else:
					cycles = 1
				#endif
			#end:case
			case 3:
				spider._send('hide:')
				seconds = kernel.Random(5, 20)
			#end:case
			case 4:
				spider._send('show:')
				state = -1
				cycles = 2
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class exitShopScr(Script):
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
				global0._send('setHeading:', 315, self)
				proc270_7(self)
			#end:case
			case 2: 0#end:case
			case 3:
				if (not (shopOwner._send('y:') < 145)):
					shopOwner._send('view:', 277, 'loop:', 2, 'cel:', 0, 'setCycle:', End)
				#endif
				global105._send('number:', 901, 'loop:', 1, 'play:')
				shopDoor._send('setCycle:', End, self)
			#end:case
			case 4:
				shopDoor._send('setPri:', 15)
				global0._send('setMotion:', MoveTo, 70, 142, self)
			#end:case
			case 5:
				global2._send('newRoom:', 240)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class clownChairScr(CartoonScript):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send(
					'setSpeed:', 6,
					'normal:', 0,
					'posn:', 205, 133,
					'view:', 2711,
					'loop:', 0,
					'cel:', 0,
					'scaleX:', 128,
					'scaleY:', 128,
					'setScale:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 1:
				global91._send('say:', 14, 5, 20, 1, self)
			#end:case
			case 2:
				KQ6Print._send(
					'font:', global22,
					'modeless:', 1,
					'ticks:', 20,
					'posn:', -1, 10,
					'say:', 0, 14, 5, 20, 2,
					'init:', self
				)
				cycles = 1
			#end:case
			case 3:
				global0._send('loop:', 3, 'cel:', 0, 'setCycle:', CT, 1, 1, self)
			#end:case
			case 4:
				clownBook._send('dispose:')
				cycles = 2
			#end:case
			case 5:
				global0._send('setCycle:', End, self)
			#end:case
			case 6:
				global0._send('setSpeed:', 6, 'loop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 7:
				seconds = 4
			#end:case
			case 8:
				global0._send('cel:', 0, 'setCycle:', End, self)
			#end:case
			case 9:
				seconds = 2
			#end:case
			case 10:
				if global25:
					KQ6Print._send('caller:', self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 11:
				global0._send('loop:', 3, 'cel:', 2, 'setCycle:', CT, 1, -1, self)
			#end:case
			case 12:
				clownBook._send('init:')
				cycles = 2
			#end:case
			case 13:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 14:
				global0._send('loop:', 2, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 15:
				global0._send('reset:', 4, 'posn:', 207, 133, 'setScale:', Scaler, 108, 83, 170, 113)
				cycles = 2
			#end:case
			case 16:
				global91._send('say:', 14, 5, 20, 3, self)
			#end:case
			case 17:
				kernel.UnLoad(128, 2711)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class randomConvScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				proc270_7(self)
			#end:case
			case 1:
				global91._send('say:', 18, 2, 23, 1, self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				global91._send('say:', 18, 2, 24, kernel.Random(1, 5), self)
			#end:case
			case 4:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class boringBookDoScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				proc270_7(self)
			#end:case
			case 1:
				global91._send('say:', 18, 42, 0, 1, self)
			#end:case
			case 2:
				global91._send('say:', 18, register, 0, 0, self)
			#end:case
			case 3:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class ownerNotAtCounterScr(Script):
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
				if shopDoor._send('cycler:'):
					shopDoor._send('cycler:')._send('caller:', self)
				else:
					(state += 2)
					self._send('cue:')
				#endif
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				shopDoor._send('stopUpd:')
				global105._send('number:', 902, 'loop:', 1, 'play:', self)
			#end:case
			case 4:
				global91._send('say:', 19, 0, 36, 0, self)
			#end:case
			case 5:
				shopOwner._send('setScript:', shopOwnerScr)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class ownerFromCounterScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				kernel.ScriptID(270, 2)._send(
					'view:', 276,
					'loop:', 0,
					'cel:', 0,
					'setPri:', 1,
					'posn:', 290, 134
				)
				cycles = 2
			#end:case
			case 1:
				if shopDoor._send('cycler:'):
					shopDoor._send('cycler:')._send('caller:', self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 2:
				global105._send('number:', 902, 'loop:', 1, 'play:')
				kernel.ScriptID(270, 2)._send('setCycle:', End, self)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				global91._send('say:', 18, 2, 25, 1, self)
			#end:case
			case 5:
				ticks = 150
			#end:case
			case 6:
				kernel.ScriptID(270, 2)._send(
					'posn:', 290, 138,
					'loop:', 1,
					'cel:', 0,
					'setPri:', 8,
					'setCycle:', End, self
				)
			#end:case
			case 7:
				kernel.ScriptID(270, 2)._send(
					'posn:', 288, 140,
					'loop:', 2,
					'cel:', 0,
					'setCycle:', CT, 2, 1, self
				)
			#end:case
			case 8:
				kernel.ScriptID(270, 2)._send('setPri:', 12, 'setCycle:', End, self)
			#end:case
			case 9:
				cycles = 2
			#end:case
			case 10:
				kernel.ScriptID(270, 2)._send(
					'loop:', 3,
					'cel:', 0,
					'posn:', 303, 151,
					'setCycle:', End, self
				)
			#end:case
			case 11:
				cycles = 2
			#end:case
			case 12:
				kernel.ScriptID(270, 2)._send(
					'view:', 277,
					'loop:', 2,
					'cel:', 0,
					'setScript:', shopOwnerScr
				)
				cycles = 2
			#end:case
			case 13:
				global91._send('say:', 18, 2, 25, 2, self)
				cycles = 1
			#end:case
			case 14:
				kernel.UnLoad(128, 276)
				kernel.ScriptID(270, 2)._send('stopUpd:')
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class shopOwnerScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				seconds = 10
			#end:case
			case 1:
				shopOwner._send(
					'view:', 277,
					'loop:', 0,
					'cel:', 0,
					'posn:', 297, 159,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				ticks = 20
			#end:case
			case 3:
				shopOwner._send('loop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 4:
				ticks = 20
			#end:case
			case 5:
				shopOwner._send('cel:', 0, 'setCycle:', End, self)
			#end:case
			case 6:
				ticks = 20
			#end:case
			case 7:
				shopOwner._send('setCycle:', Beg, self)
			#end:case
			case 8:
				shopOwner._send('loop:', 1, 'cel:', shopOwner._send('lastCel:'), 'setCycle:', Beg, self)
			#end:case
			case 9:
				shopOwner._send('view:', 277, 'loop:', 2, 'cel:', 0, 'posn:', 303, 151)
				cycles = 2
			#end:case
			case 10:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genericTalkScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				proc270_7(self)
			#end:case
			case 1:
				global91._send('say:', 18, 2, register, 0, self)
			#end:case
			case 2:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class shopOwner(Actor):
	#property vars (may be empty)
	x = 303
	y = 151
	noun = 18
	sightAngle = 40
	approachX = 266
	approachY = 151
	view = 277
	loop = 2
	priority = 12
	signal = 20497
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if kernel.ScriptID(10, 0)._send('isSet:', 2):
			kernel.ScriptID(10, 0)._send('clrIt:', 2)
		#endif
		match param1
			case 2:
				(cond
					case (not proc913_0(64)):
						proc913_1(64)
						proc913_1(73)
						global2._send('setScript:', genericTalkScr, 0, 26)
					#end:case
					case ((not proc913_0(16)) and proc913_0(73)):
						global1._send('givePoints:', 1)
						proc913_1(16)
						proc913_2(54)
						proc913_1(53)
						global2._send('setScript:', kernel.ScriptID(276, 3))
					#end:case
					case (not proc913_0(16)):
						proc913_1(16)
						global1._send('givePoints:', 1)
						global2._send('setScript:', genericTalkScr, 0, 22)
					#end:case
					else:
						global2._send('setScript:', randomConvScr)
					#end:else
				)
			#end:case
			case 27:
				global2._send('setScript:', kernel.ScriptID(276, 1))
			#end:case
			else:
				if proc999_5(param1, 28, 32):
					global2._send('setScript:', boringBookDoScr, 0, param1)
				else:
					if (param1 == 67):
						param1 = 63
					#endif
					super._send('doVerb:', param1, &rest)
				#endif
			#end:else
		#end:match
	#end:method

	@classmethod
	def init(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('approachVerbs:', 2, 27)
	#end:method

#end:class or instance

@SCI.instance
class shopDoor(Prop):
	#property vars (may be empty)
	x = 69
	y = 90
	noun = 17
	approachX = 80
	approachY = 142
	view = 270
	cel = 4
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('stopUpd:')
		global105._send('number:', 902, 'loop:', 1, 'play:')
	#end:method

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
				global2._send('setScript:', exitShopScr)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class fire(Prop):
	#property vars (may be empty)
	x = 225
	y = 105
	noun = 8
	view = 270
	loop = 1
	signal = 16384
	detailLevel = 1
	
#end:class or instance

@SCI.instance
class bookStand(Feature):
	#property vars (may be empty)
	x = 113
	y = 131
	noun = 2
	nsTop = 116
	nsLeft = 99
	nsBottom = 132
	nsRight = 123
	sightAngle = 40
	approachX = 112
	approachY = 137
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if temp0 = super._send('onMe:', param1, &rest):
			if (param1._send('message:') == 1):
				approachX = 134
				approachY = 129
			else:
				approachX = 112
				approachY = 137
			#endif
		#endif
		return temp0
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				if (global9._send('at:', 1)._send('owner:') == global11):
					global91._send('say:', 2, 1, 4)
				else:
					KQ6Print._send(
						'font:', global22,
						'posn:', -1, 10,
						'say:', 0, noun, param1, 4, 1,
						'init:'
					)
					KQ6Print._send(
						'font:', global22,
						'posn:', -1, 10,
						'say:', 0, noun, param1, 3, 1,
						'init:'
					)
				#endif
			#end:case
			case 5:
				if (global9._send('at:', 1)._send('owner:') != global11):
					global91._send('say:', noun, param1, 3)
				else:
					global2._send('setScript:', kernel.ScriptID(273, 1))
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('approachVerbs:', 1, 5)
	#end:method

#end:class or instance

@SCI.instance
class poemShelf(Feature):
	#property vars (may be empty)
	x = 302
	y = 90
	noun = 13
	onMeCheck = 4096
	approachX = 302
	approachY = 124
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global2._send('setScript:', kernel.ScriptID(272, 0))
			#end:case
			else:
				if ((param1 == 2) or (not proc999_5(param1, 5, 1))):
					if (param1 != 2):
						param1 = 0
					#endif
					global91._send('say:', 4, param1)
				else:
					super._send('doVerb:', param1, &rest)
				#endif
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
class shelfFeatures(Feature):
	#property vars (may be empty)
	sightAngle = 40
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if _approachVerbs:
			_approachVerbs = 0
		#endif
		(return
			(= noun
				match kernel.OnControl(4, param1._send('x:'), param1._send('y:'))
					case 512:
						x = 162
						y = 113
						approachX = 159
						approachY = 119
						self._send('approachVerbs:', 5, 1)
						4
					#end:case
					case 1024:
						x = 186
						y = 110
						approachX = 192
						approachY = 121
						self._send('approachVerbs:', 5, 1)
						20
					#end:case
					case 2048:
						x = 265
						y = 116
						approachX = 266
						approachY = 121
						self._send('approachVerbs:', 5, 1)
						16
					#end:case
					case 256:
						x = 134
						y = 118
						approachX = 142
						approachY = 121
						self._send('approachVerbs:', 5, 1)
						11
					#end:case
					else: 0#end:else
				#end:match
			)
		)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((param1 == 2) or (not proc999_5(param1, 5, 1))):
			noun = 4
			if (param1 != 2):
				param1 = 0
			#endif
		#endif
		super._send('doVerb:', param1, &rest)
	#end:method

#end:class or instance

@SCI.instance
class genericFeatures(Feature):
	#property vars (may be empty)
	sightAngle = 40
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(= noun
				match kernel.OnControl(4, param1._send('x:'), param1._send('y:'))
					case 32:
						x = 225
						y = 118
						3
					#end:case
					case 64:
						x = 125
						y = 115
						21
					#end:case
					case 4:
						x = 223
						y = 117
						7
					#end:case
					case 128:
						x = 72
						y = 141
						12
					#end:case
					else: 0#end:else
				#end:match
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class frontCounter(Feature):
	#property vars (may be empty)
	x = 281
	y = 139
	z = -10
	noun = 5
	onMeCheck = 2
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 1):
			global91._send(
				'say:', 5, 1, (6 if (global9._send('at:', 45)._send('owner:') == global11) else 5)
			)
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class clownChair(Feature):
	#property vars (may be empty)
	x = 215
	y = 131
	noun = 14
	sightAngle = 40
	onMeCheck = 16392
	approachX = 217
	approachY = 134
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if temp0 = super._send('onMe:', param1, &rest):
			temp1 = kernel.OnControl(4, param1._send('x:'), param1._send('y:'))
			(cond
				case ((param1._send('message:') == 5) and (temp1 == 16384)):
					temp0 = 0
				#end:case
				case 
					(and
						(param1._send('message:') == 5)
						(not global5._send('contains:', kernel.ScriptID(274, 0)))
						(temp1 == 8)
					):
					self._send('approachVerbs:', 5)
				#end:case
				else:
					_approachVerbs = 0
				#end:else
			)
		#endif
		return temp0
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				if 
					(and
						global5._send('contains:', kernel.ScriptID(274, 0))
						(not global5._send('contains:', clownBook))
					)
					global91._send('say:', noun, param1, 19)
				else:
					global2._send('setScript:', clownChairScr)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('approachVerbs:', 5)
	#end:method

#end:class or instance

@SCI.instance
class clownBook(View):
	#property vars (may be empty)
	x = 227
	y = 129
	z = 10
	approachX = 227
	approachY = 132
	view = 270
	loop = 2
	cel = 2
	priority = 9
	signal = 16401
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if temp0 = super._send('onMe:', param1, &rest):
			if 
				(and
					(not global5._send('contains:', kernel.ScriptID(274, 0)))
					((param1._send('message:') == 5) or (param1._send('message:') == 1))
				)
				self._send('approachVerbs:', 5, 1)
				if (param1._send('message:') == 5):
					approachX = 217
					approachY = 134
				else:
					approachX = 227
					approachY = 132
				#endif
			else:
				_approachVerbs = 0
			#endif
		#endif
		return temp0
	#end:method

	@classmethod
	def doVerb():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		readingTable._send('doVerb:', &rest)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('approachVerbs:', 1)
	#end:method

#end:class or instance

@SCI.instance
class readingTable(Feature):
	#property vars (may be empty)
	x = 227
	y = 129
	noun = 23
	onMeCheck = 8192
	approachX = 227
	approachY = 132
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if temp0 = super._send('onMe:', param1, &rest):
			if 
				(and
					(not global5._send('contains:', kernel.ScriptID(274, 0)))
					((param1._send('message:') == 5) or (param1._send('message:') == 1))
				)
				self._send('approachVerbs:', 5, 1)
				if (param1._send('message:') == 5):
					approachX = 217
					approachY = 134
				else:
					approachX = 227
					approachY = 132
				#endif
			else:
				_approachVerbs = 0
			#endif
		#endif
		return temp0
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				if global5._send('contains:', kernel.ScriptID(274, 0)):
					global91._send('say:', noun, param1, 37)
				else:
					global91._send('say:', noun, param1, 38)
				#endif
			#end:case
			else:
				clownChair._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('approachVerbs:', 1)
	#end:method

#end:class or instance

@SCI.instance
class spellBook(View):
	#property vars (may be empty)
	x = 294
	y = 150
	z = 15
	noun = 1
	view = 270
	loop = 3
	priority = 13
	signal = 16400
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				if proc913_0(7):
					global91._send('say:', noun, param1, 2)
				else:
					proc913_1(7)
					global1._send('givePoints:', 2)
					global91._send('say:', noun, param1, 1)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send(
			'approachX:', shopOwner._send('approachX:'),
			'approachY:', shopOwner._send('approachY:'),
			'approachVerbs:', 5
		)
	#end:method

#end:class or instance

@SCI.instance
class roomPoly(Polygon):
	#property vars (may be empty)
#end:class or instance

