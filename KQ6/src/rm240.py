#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 240
import sci_sh
import kernel
import Main
import rgCrown
import walkEgoInScr
import KQ6Print
import KQ6Room
import n913
import Print
import Inset
import PAvoider
import Scaler
import PolyPath
import Polygon
import Feature
import LoadMany
import DPath
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm240 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = [0, -10, 319, -10, 326, 175, 243, 150, 231, 149, 204, 140, 181, 134, 162, 137, 158, 132, 152, 130, 142, 132, 135, 123, 119, 117, 105, 102, 71, 102, 58, 97, 58, 0, 46, 0, 46, 94, 13, 103, 29, 113, 13, 119, 24, 132, 14, 144, 42, 160, 64, 174, 101, 178, 117, 189, 0, 189]
local59 = [0, -10, 319, -10, 326, 175, 243, 150, 231, 149, 204, 140, 181, 134, 162, 137, 158, 132, 152, 130, 142, 132, 135, 123, 119, 117, 105, 102, 71, 102, 58, 97, 58, 0, 46, 0, 46, 94, 11, 104, 19, 117, 54, 117, 34, 137, 18, 137, 39, 159, 64, 174, 101, 178, 117, 189, 0, 189]


@SCI.procedure
def localproc_0(param1 = None, *rest):
	if param1:
		global2._send('addObstacle:', roomPoly._send('points:', @local59, 'yourself:'))
	else:
		global2._send('addObstacle:', roomPoly._send('points:', @local1, 'yourself:'))
	#endif
#end:procedure

@SCI.instance
class rm240(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 240
	horizon = 10
	south = 210
	
	@classmethod
	def init():
		proc958_0(128, 240, 241)
		kernel.Load(143, picture)
		super._send('init:', &rest)
		global0._send(
			'init:',
			'reset:', 3,
			'setAvoider:', PAvoider,
			'setScale:', Scaler, 90, 72, 188, 95
		)
		if (global153 > 2):
			proclamation._send('init:')
		else:
			procCover._send('init:', 'stopUpd:')
		#endif
		pot._send('init:')
		doorBell1._send('init:')
		doorBell2._send('init:')
		genericFeatures._send('init:')
		randomVillagers._send('init:', 'setScript:', villagersScr)
		if kernel.ScriptID(10, 0)._send('isSet:', 2):
			kernel.ScriptID(10, 0)._send('clrIt:', 2)
			clown._send('init:')
		#endif
		(cond
			case proc999_5(global12, 280, 270):
				if (global12 == 280):
					pshopDoor._send('cel:', 5)
				else:
					bshopDoor._send('cel:', 5)
				#endif
				self._send('setScript:', enterFromShopScr)
			#end:case
			case (global12 == 250):
				self._send('setScript:', enterFromVillage2Scr)
			#end:case
			else:
				proc12_1(191, 185, -45)
			#end:else
		)
		pshopDoor._send('init:')
		bshopDoor._send('init:')
		bush1._send('init:')
		bush2._send('init:')
		if (global1._send('_detailLevel:') >= 2):
			bush1._send('setScript:', kernel.Clone(kernel.ScriptID(13, 0)))
			bush2._send('setScript:', kernel.ScriptID(13, 0))
		#endif
		if (not kernel.ScriptID(10, 0)._send('isSet:', 512)):
			global102._send('number:', 240, 'loop:', -1, 'play:')
		else:
			kernel.ScriptID(10, 0)._send('clrIt:', 512)
		#endif
		if 
			(and
				(not proc999_5(global12, 270, 280))
				global0._send('has:', 0)
				(not proc913_0(110))
			)
			proc913_1(110)
			proc10_2(dumpTrashScr)
		#endif
		if (proc999_5(global153, 1, 5) and (not proc913_0(12))):
			kernel.ScriptID(241, 0)._send('init:')
			localproc_0(1)
		else:
			localproc_0(0)
		#endif
	#end:method

	@classmethod
	def doit():
		temp0 = global0._send('onControl:', 1)
		(cond
			case script: 0#end:case
			case (temp0 & 0x4000):
				global102._send('fade:', 0, 10, 10, 0)
				self._send('setScript:', exitToVillage2Scr)
			#end:case
		)
		super._send('doit:', &rest)
	#end:method

	@classmethod
	def edgeToRoom(param1 = None, *rest):
		if (param1 == 3):
			global102._send('fade:', 0, 10, 10, 0)
			proc12_0(param1, -45)
			return 0
		else:
			super._send('edgeToRoom:', param1, &rest)
		#endif
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		if ((param1 == 210) and global5._send('contains:', clown)):
			kernel.ScriptID(10, 0)._send('setIt:', 2)
		#endif
		if (proc913_0(53) and (not (param1 == 270))):
			proc913_1(54)
			proc913_2(53)
		#endif
		super._send('newRoom:', param1, &rest)
	#end:method

	@classmethod
	def notify():
		global2._send('obstacles:')._send('delete:', roomPoly)
		localproc_0(0)
	#end:method

	@classmethod
	def dispose():
		if proc999_5(global13, 270, 280):
			global102._send('fade:', 70, 10, 15, 0)
		#endif
		kernel.DisposeScript(11)
		kernel.DisposeScript(923)
		kernel.DisposeScript(927)
		kernel.DisposeScript(964)
		kernel.DisposeScript(930)
		kernel.DisposeScript(13)
		kernel.DisposeScript(241)
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class procInset(Inset):
	#property vars (may be empty)
	view = 242
	x = 80
	y = 73
	disposeNotOnMe = 1
	noun = 10
	
	@classmethod
	def init():
		super._send('init:', &rest)
		global1._send('handsOn:')
		global69._send('disable:', 0, 1, 3, 4, 5, 6)
	#end:method

	@classmethod
	def doVerb():
		Print._send('font:', global22, 'posn:', 160, 30, 'width:', 138, 'addText:', 10, 1, 0, 1, 'init:')
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		if (not temp0 = super._send('onMe:', param1, &rest)):
			global1._send('handsOn:')
			global69._send('enable:', 6)
		#endif
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class exitToVillage2Scr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send(
					'setScale:', Scaler, 75, 25, 95, 68,
					'setMotion:', DPath, 43, 92, 33, 90, self
				)
			#end:case
			case 1:
				global2._send('newRoom:', 250)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class enterFromVillage2Scr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send(
					'posn:', 34, 90,
					'setScale:', Scaler, 75, 25, 95, 68,
					'setMotion:', DPath, 43, 92, 54, 96, self
				)
			#end:case
			case 1:
				global0._send(
					'setScale:', Scaler, 90, 72, 188, 95,
					'setMotion:', MoveTo, 55, 101, self
				)
			#end:case
			case 2:
				if (not script):
					cycles = 1
				#endif
			#end:case
			case 3:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class exitToShopScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global69._send('disable:')
				global0._send(
					'setMotion:', 0,
					'setSpeed:', 6,
					'view:', 241,
					'loop:', 1,
					'cel:', 0,
					'normal:', 0
				)
				if (register == 1):
					global0._send('posn:', 232, 144, 'scaleX:', 117, 'scaleY:', 117)
					local0 = pshopDoor
				else:
					global0._send('posn:', 160, 130, 'scaleX:', 107, 'scaleY:', 107)
					local0 = bshopDoor
				#endif
				global0._send('setScale:', 'setCycle:', End, self)
			#end:case
			case 1:
				if (register == 1):
					global0._send('posn:', 239, 128)
				else:
					global0._send('setPri:', 9, 'posn:', 171, 115)
				#endif
				global0._send('loop:', 0, 'cel:', 0, 'setCycle:', End, self)
				global105._send('number:', 901, 'loop:', 1, 'play:')
				local0._send('cel:', 0, 'setCycle:', CT, 4, 1, self)
			#end:case
			case 2: 0#end:case
			case 3:
				global0._send('reset:')
				global69._send('enable:')
				if (self._send('register:') == 1):
					global2._send('newRoom:', 280)
				else:
					global2._send('newRoom:', 270)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class enterFromShopScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('setMotion:', 0, 'view:', 241, 'loop:', 2, 'cel:', 0, 'normal:', 0)
				if (global12 == 280):
					global0._send('posn:', 224, 145, 'scaleX:', 117, 'scaleY:', 117)
					local0 = pshopDoor
				else:
					global0._send('setPri:', 9, 'posn:', 158, 129, 'scaleX:', 107, 'scaleY:', 107)
					local0 = bshopDoor
				#endif
				global0._send('setScale:')
				cycles = 2
			#end:case
			case 1:
				local0._send('setCycle:', Beg, self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				local0._send('stopUpd:')
				global105._send('number:', 902, 'loop:', 1, 'play:')
				global0._send('setCycle:', End, self)
			#end:case
			case 4:
				if (not global5._send('contains:', clown)):
					global1._send('handsOn:')
				#endif
				global0._send('reset:', 5, 'setScale:', Scaler, 90, 72, 188, 95)
				if (global12 == 280):
					global0._send('posn:', 214, 147)
				else:
					global0._send('setPri:', -1, 'posn:', 150, 132)
				#endif
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class dumpTrashScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				proc913_1(110)
				seconds = 2
			#end:case
			case 1:
				global105._send('number:', 901, 'loop:', 1, 'play:')
				pshopDoor._send(
					'view:', 248,
					'cycleSpeed:', 9,
					'loop:', 1,
					'cel:', 0,
					'setCycle:', CT, 6, 1, self
				)
			#end:case
			case 2:
				global104._send('number:', 241, 'loop:', 1, 'play:')
				pshopDoor._send('setCycle:', End, self)
			#end:case
			case 3:
				global105._send('number:', 902, 'loop:', 1, 'play:')
				cycles = 2
			#end:case
			case 4:
				pshopDoor._send('view:', 240, 'loop:', 0, 'cel:', 0, 'stopUpd:')
				cycles = 2
			#end:case
			case 5:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class searchUrnScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send(
					'setSpeed:', 6,
					'normal:', 0,
					'posn:', 194, 135,
					'view:', 248,
					'loop:', 0,
					'cel:', 0,
					'setScale:', 0
				)
				cycles = 2
			#end:case
			case 1:
				global0._send('setCycle:', CT, 2, 1, self)
			#end:case
			case 2:
				global104._send('number:', 241, 'loop:', -1, 'play:')
				global0._send('setCycle:', kernel.ScriptID(231, 0), 3)
				ticks = 120
			#end:case
			case 3:
				global104._send('stop:')
				global91._send(
					'say:', 26, 5, (cond
							case (proc913_0(110) and (not proc913_0(111))):
								register = 1
								global0._send('get:', 51)
								proc913_1(111)
								38
							#end:case
							case proc913_0(110): 39#end:case
							else: 37#end:else
						), 0, self
				)
			#end:case
			case 4:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				global0._send(
					'reset:', 0,
					'posn:', pot._send('approachX:'), pot._send('approachY:'),
					'setScale:', Scaler, 90, 72, 188, 95
				)
				cycles = 2
			#end:case
			case 7:
				if register:
					global1._send('givePoints:', 1)
				#endif
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		kernel.DisposeScript(231)
		super._send('dispose:')
		register = 0
	#end:method

#end:class or instance

@SCI.instance
class villagersScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				client._send('hide:')
				(= state
					match kernel.Random(0, 2)
						case 0: 0#end:case
						case 1: 8#end:case
						case 2: 17#end:case
					#end:match
				)
				seconds = kernel.Random(45, 60)
			#end:case
			case 1:
				client._send(
					'show:',
					'loop:', 1,
					'cel:', 0,
					'posn:', 159, 123, 78,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				client._send('loop:', 0, 'cel:', 0)
				ticks = 60
			#end:case
			case 3:
				client._send('loop:', 3, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 4:
				ticks = 60
			#end:case
			case 5:
				client._send('loop:', 3, 'setCycle:', Beg, self)
			#end:case
			case 6:
				ticks = 60
			#end:case
			case 7:
				client._send('loop:', 3, 'setCycle:', End, self)
			#end:case
			case 8:
				client._send('loop:', 2, 'cel:', 0, 'setCycle:', End, self)
				state = -1
			#end:case
			case 9:
				client._send(
					'show:',
					'loop:', 5,
					'cel:', 0,
					'posn:', 198, 123, 90,
					'setCycle:', End, self
				)
			#end:case
			case 10:
				client._send('loop:', 4, 'cel:', 0)
				ticks = kernel.Random(45, 120)
			#end:case
			case 11:
				client._send('loop:', 6, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 12:
				ticks = kernel.Random(45, 120)
			#end:case
			case 13:
				client._send('loop:', 6, 'cel:', 0, 'setCycle:', Beg, self)
			#end:case
			case 14:
				ticks = kernel.Random(45, 120)
			#end:case
			case 15:
				client._send('loop:', 6, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 16:
				ticks = kernel.Random(45, 120)
			#end:case
			case 17:
				client._send('loop:', 7, 'cel:', 0, 'setCycle:', End, self)
				state = -1
			#end:case
			case 18:
				client._send(
					'show:',
					'posn:', 247, 122, 84,
					'loop:', 9,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 19:
				client._send('loop:', 8, 'cel:', 0)
				ticks = kernel.Random(45, 120)
			#end:case
			case 20:
				client._send('loop:', 12, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 21:
				ticks = kernel.Random(45, 120)
			#end:case
			case 22:
				client._send('setCycle:', Beg, self)
			#end:case
			case 23:
				ticks = kernel.Random(45, 120)
			#end:case
			case 24:
				client._send('loop:', 10, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 25:
				client._send('loop:', 11, 'cel:', 0, 'setCycle:', Fwd)
				ticks = 80
			#end:case
			case 26:
				client._send('loop:', 13, 'cel:', 0, 'setCycle:', End, self)
				state = -1
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class clownScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				client._send('setMotion:', PolyPath, 156, 250, self)
			#end:case
			case 1:
				global1._send('handsOn:')
				global69._send('curIcon:', global69._send('at:', 0))
				global1._send('setCursor:', global69._send('curIcon:')._send('cursor:'))
				seconds = 20
			#end:case
			case 2:
				client._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lookAtProcScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				register = 0
				if (not proc913_1(71)):
					if (proc913_0(72) or proc913_0(52)):
						register = 30
					else:
						register = 31
					#endif
					global91._send('say:', 8, 1, 30, 1, self)
				else:
					global91._send('say:', 8, 1, 33, 1, self)
					register = 33
				#endif
			#end:case
			case 1:
				global0._send(
					'setMotion:', PolyPath, proclamation._send('approachX:'), proclamation._send(
							'approachY:'
						), self
				)
			#end:case
			case 2:
				global0._send('setHeading:', 0, self)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				procInset._send('init:', 0, global2)
				cycles = 2
			#end:case
			case 5:
				if (global90 & 0x0002):
					global91._send('say:', 10, 1, 0, 1, self)
				else:
					KQ6Print._send(
						'font:', global22,
						'posn:', 160, 30,
						'width:', 138,
						'addText:', 10, 1, 0, 1,
						'init:', self
					)
				#endif
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				(cond
					case ((global90 & 0x0002) and (register != 33)):
						global91._send(
							'say:', 8, 1, register, if (register == 30):
									2
								else:
									1
								#endif, self
						)
					#end:case
					case (register != 33):
						KQ6Print._send(
							'font:', global22,
							'posn:', 160, 52,
							'width:', 138,
							'addText:', 8, 1, register, (2 if (register == 30) else 1),
							'init:', self
						)
					#end:case
					else:
						cycles = 1
					#end:else
				)
			#end:case
			case 8:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class bshopDoor(Prop):
	#property vars (may be empty)
	x = 186
	y = 134
	z = 49
	noun = 46
	approachX = 155
	approachY = 131
	view = 240
	loop = 1
	priority = 5
	signal = 16401
	
	@classmethod
	def doVerb(param1 = None, *rest):
		if (param1 == 5):
			global2._send('setScript:', exitToShopScr, 0, 0)
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('approachVerbs:', 5)
	#end:method

#end:class or instance

@SCI.instance
class pshopDoor(Prop):
	#property vars (may be empty)
	x = 255
	y = 99
	noun = 45
	approachX = 218
	approachY = 147
	view = 240
	signal = 1
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				global2._send('setScript:', exitToShopScr, 0, 1)
			#end:case
			case 1:
				super._send('doVerb:', param1, &rest)
			#end:case
			else:
				bshopDoor._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('approachVerbs:', 5)
	#end:method

#end:class or instance

@SCI.instance
class randomVillagers(Prop):
	#property vars (may be empty)
	noun = 33
	view = 246
	
	@classmethod
	def doVerb(param1 = None, *rest):
		if (global66._send('doit:', param1) == -32768):
			param1 = 5
		#endif
		if (param1 == 2):
			global91._send('say:', noun, param1, kernel.Random(27, 28))
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class clown(Actor):
	#property vars (may be empty)
	x = 139
	y = 140
	view = 717
	signal = 16384
	
	@classmethod
	def init():
		super._send('init:', &rest)
		self._send(
			'setScale:', Scaler, 90, 72, 188, 95,
			'setCycle:', Walk,
			'setSpeed:', 4,
			'setScript:', clownScr
		)
	#end:method

#end:class or instance

@SCI.instance
class procCover(Prop):
	#property vars (may be empty)
	x = 90
	y = 86
	noun = 50
	view = 2401
	priority = 6
	signal = 16
	
#end:class or instance

@SCI.instance
class bush1(Prop):
	#property vars (may be empty)
	x = 11
	y = 167
	view = 240
	loop = 2
	priority = 15
	signal = 16400
	cycleSpeed = 2
	
#end:class or instance

@SCI.instance
class bush2(Prop):
	#property vars (may be empty)
	x = 54
	y = 186
	view = 240
	loop = 3
	cel = 3
	priority = 15
	signal = 16400
	cycleSpeed = 4
	
#end:class or instance

@SCI.instance
class proclamation(Feature):
	#property vars (may be empty)
	x = 90
	y = 101
	noun = 8
	nsTop = 75
	nsLeft = 83
	nsBottom = 91
	nsRight = 96
	sightAngle = 40
	approachX = 88
	approachY = 109
	
	@classmethod
	def doVerb(param1 = None, *rest):
		if proc999_5(param1, 1, 5):
			global2._send('setScript:', lookAtProcScr)
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class pot(Feature):
	#property vars (may be empty)
	x = 213
	y = 135
	noun = 26
	onMeCheck = 256
	approachX = 195
	approachY = 134
	
	@classmethod
	def onMe(param1 = None, *rest):
		if 
			(and
				(kernel.OnControl(4, param1._send('x:'), param1._send('y:')) == onMeCheck)
				(param1._send('x:') < 235)
			)
			return 1
		else:
			return 0
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				global2._send('setScript:', searchUrnScr)
			#end:case
			else:
				super._send('doVerb:', param1)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('approachVerbs:', 5)
	#end:method

#end:class or instance

@SCI.instance
class genericFeatures(Feature):
	#property vars (may be empty)
	sightAngle = 40
	
	@classmethod
	def onMe(param1 = None, *rest):
		x = param1._send('x:')
		y = param1._send('y:')
		(return
			(= noun
				match kernel.OnControl(4, param1._send('x:'), param1._send('y:'))
					case 2:
						if (param1._send('y:') < 100):
							y = 154
							5
						else:
							0
						#endif
					#end:case
					case 4096:
						y = 131
						47
					#end:case
					case 8192:
						y = 131
						48
					#end:case
					case 8:
						y = 97
						50
					#end:case
					case 32:
						y = 122
						43
					#end:case
					case 16:
						y = 122
						13
					#end:case
					case 64:
						y = 134
						41
					#end:case
					case 128:
						y = 120
						42
					#end:case
					case 512:
						if (param1._send('x:') > 96):
							y = 154
							23
						else:
							49
						#endif
					#end:case
					case 256:
						(cond
							case (param1._send('x:') > 265):
								y = 155
								11
							#end:case
							case (param1._send('x:') < 235): 0#end:case
							else:
								y = 146
								24
							#end:else
						)
					#end:case
					case 1024:
						(cond
							case (param1._send('y:') > 131):
								y = 160
								25
							#end:case
							case (param1._send('y:') < 80):
								y = 148
								40
							#end:case
							else:
								y = 151
								44
							#end:else
						)
					#end:case
					case 2048:
						y = 153
						14
					#end:case
					else: 0#end:else
				#end:match
			)
		)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		(cond
			case ((param1 == 5) and proc999_5(noun, 11, 26, 24)):
				global91._send('say:', 24, param1)
			#end:case
			case 
				(or
					(and
						(or
							proc999_5(param1, 5, 2)
							(global66._send('doit:', param1) == -32768)
						)
						(noun == 14)
						noun = 13
					)
					((param1 == 2) and (noun == 40) and noun = 41)
					(and
						(global66._send('doit:', param1) == -32768)
						(or
							((noun == 44) and noun = 42)
							((noun == 49) and param1 = 5)
						)
					)
				):
				super._send('doVerb:', param1, &rest)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class doorBell1(Feature):
	#property vars (may be empty)
	x = 185
	y = 132
	z = 56
	noun = 12
	nsTop = 70
	nsLeft = 179
	nsBottom = 82
	nsRight = 191
	sightAngle = 40
	
#end:class or instance

@SCI.instance
class doorBell2(Feature):
	#property vars (may be empty)
	x = 225
	y = 139
	z = 53
	noun = 12
	nsTop = 81
	nsLeft = 221
	nsBottom = 91
	nsRight = 229
	sightAngle = 40
	
#end:class or instance

@SCI.instance
class roomPoly(Polygon):
	#property vars (may be empty)
	size = 29
	type = 2
	
#end:class or instance

