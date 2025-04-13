#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 340
import sci_sh
import kernel
import Main
import rSacred
import genie_341
import n342
import n343
import nightMare
import KQ6Room
import n913
import Conversation
import Scaler
import PolyPath
import Feature
import LoadMany
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm340 = 0,
	theDoor = 1,
	labRock = 2,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None


@SCI.instance
class cliffTalk(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class rm340(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 340
	horizon = 70
	walkOffEdge = 1
	
	@classmethod
	def notify():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		proc344_1()
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		kernel.Lock(143, 340, 0)
		proc343_0()
		global32._send(
			'add:', labDoor, niteShade, cave, oracle, myPath, mount,
			'eachElementDo:', #init
		)
		if proc913_0(1):
			local2 = 23
			minoOpening._send('init:')
		else:
			local2 = 20
		#endif
		global5._send('add:', theDoor, labRock, rockStep, berries, 'eachElementDo:', #init)
		global102._send('number:', 340, 'setLoop:', -1, 'play:')
		rockStep._send('addToPic:', 'dispose:')
		global0._send('actions:', egoDoVerb, 'init:')
		(cond
			case (global12 == 390):
				global2._send('setScript:', crawlOutOfCave)
			#end:case
			case (global12 == 405):
				global1._send('handsOff:')
				if (proc913_0(14) and proc913_0(4) and (not proc913_0(15))):
					proc958_0(128, 335, 337, 336)
					global103._send('number:', 345, 'play:')
					kernel.Load(130, 344)
					proc344_0()
				#endif
				global2._send('setScript:', fromLab)
			#end:case
			case (global12 == 440):
				global0._send(
					'posn:', 18, 138,
					'view:', 361,
					'setLoop:', 0,
					'setPri:', 9,
					'cel:', 0,
					'normal:', 0,
					'hide:'
				)
				if (not proc913_0(3)):
					kernel.Load(130, 342)
					berries._send('addToPic:', 'dispose:')
					theDoor._send('addToPic:', 'dispose:')
					kernel.UnLoad(128, 330)
					proc342_0()
				else:
					global1._send('handsOff:')
					if (proc913_0(14) and proc913_0(4) and (not proc913_0(15))):
						proc958_0(128, 335, 337, 336)
						global103._send('number:', 345, 'play:')
						kernel.Load(130, 344)
						proc344_0()
					#endif
					global2._send('setScript:', fromLab)
				#endif
			#end:case
			case (global12 == 370):
				global2._send('north:', 0)
				kernel.Load(130, 342)
				global0._send('posn:', 340, -10, 'reset:', 'ignoreHorizon:')
				proc342_1()
			#end:case
			case ((not proc913_0(1)) and proc913_0(2)):
				proc958_0(128, 343, 344)
				kernel.Load(130, 342)
				berries._send('addToPic:', 'dispose:')
				proc342_2()
			#end:case
			case (global12 == 350):
				global1._send('handsOn:')
				global0._send(
					'reset:',
					'posn:', 232, 77,
					'setScale:', Scaler, 100, 5, 105, 65,
					'setMotion:', MoveTo, 236, 122
				)
				global0._send('scaler:')._send('doit:')
			#end:case
			else:
				(cond
					case (proc999_5(global12, 320, 300) and (not proc913_0(4))):
						proc958_0(128, 334, 330)
						kernel.Load(130, 341)
						proc341_0()
					#end:case
					case (proc913_0(14) and proc913_0(4) and (not proc913_0(15))):
						proc958_0(128, 335, 337, 336)
						global103._send('number:', 345, 'play:')
						kernel.Load(130, 344)
						proc344_0()
					#end:case
				)
				global0._send(
					'view:', 301,
					'loop:', 6,
					'normal:', 0,
					'posn:', 219, 199,
					'cycleSpeed:', 10,
					'setPri:', 15,
					'setScale:', Scaler, 100, 5, 105, 65
				)
				global2._send('setScript:', egoEnters)
			#end:else
		)
		proc913_1(157)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (rSacred._send('geniePresent:') == 1):
				global91._send('say:', 3, 1, 21, 1)
			#end:case
			case (rSacred._send('marePresent:') == 1):
				global91._send('say:', 3, 1, 22, 1)
			#end:case
		)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		proc958_0(0, 341, 342, 344)
		if (not (global103._send('number:') == 155)):
			global103._send('fade:', 0, 5, 5)
		#endif
		rSacred._send('marePresent:', 0)
		global0._send('setScale:', 0)
		super._send('dispose:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			match param1
				case 1:
					if proc913_0(1):
						global91._send('say:', 3, 1, 23, 1, self)
					else:
						global91._send('say:', 3, 1, 20, 1, self)
					#endif
					1
				#end:case
				case 2:
					(cond
						case (rSacred._send('geniePresent:') == 1):
							global91._send('say:', 3, 2, 21, 1)
						#end:case
						case (rSacred._send('marePresent:') == 1):
							global91._send('say:', 3, 2, 22, 1)
						#end:case
						else:
							global91._send('say:', 3, 2, 24, 1)
						#end:else
					)
					1
				#end:case
				else:
					super._send('doVerb:', param1, &rest)
				#end:else
			#end:match
		)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case global2._send('script:'):#end:case
			case local3:#end:case
			case (global0._send('onControl:', 1) == 16):
				global102._send('fade:', 0, 10, 10)
				global2._send('newRoom:', 405)
			#end:case
			case ((global0._send('onControl:', 1) == 512) and proc913_0(1)):
				global102._send('fade:', 0, 10, 10)
				global2._send('setScript:', goToLair)
			#end:case
			case (global0._send('onControl:', 1) == 1024):
				global102._send('fade:', 0, 10, 10)
				global2._send('setScript:', stepDown)
			#end:case
			case (global0._send('onControl:', 1) == 2):
				global1._send('handsOff:')
				global2._send('setScript:', dieHard)
			#end:case
			case (global0._send('edgeHit:') == 1):
				global1._send('handsOff:')
				global102._send('fade:', 0, 10, 10)
				global2._send('setScript:', goNorth)
			#end:case
		)
		super._send('doit:')
	#end:method

	@classmethod
	def newRoom():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		local3 = 1
		super._send('newRoom:', &rest)
	#end:method

	@classmethod
	def scriptCheck():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 1
		if rSacred._send('geniePresent:'):
			global91._send('say:', 0, 0, 4, 1, 0, 899)
			temp0 = 0
		#endif
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class rockStep(View):
	#property vars (may be empty)
	x = 154
	y = 185
	noun = 6
	view = 341
	
#end:class or instance

@SCI.instance
class theDoor(Prop):
	#property vars (may be empty)
	x = 113
	y = 67
	noun = 4
	view = 340
	priority = 7
	signal = 28688
	cycleSpeed = 10
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc913_0(3):
			self._send('cel:', 4, 'stopUpd:')
		else:
			self._send('cel:', 0, 'stopUpd:')
		#endif
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		labDoor._send('doVerb:', param1, &rest)
	#end:method

#end:class or instance

@SCI.instance
class labRock(Actor):
	#property vars (may be empty)
	noun = 5
	view = 340
	loop = 1
	signal = 20480
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc913_0(3):
			self._send('posn:', 0, 149, 'stopUpd:')
		else:
			self._send('posn:', 9, 137, 'stopUpd:')
		#endif
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				global91._send('say:', 5, 1, local2, 1)
			#end:case
			case 5:
				global91._send('say:', 5, 5, local2, 1)
			#end:case
			case 2:
				super._send('doVerb:', param1, &rest)
			#end:case
			else:
				global91._send('say:', 5, 0, local2, 1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class berries(View):
	#property vars (may be empty)
	x = 283
	y = 112
	z = 15
	noun = 12
	view = 330
	priority = 7
	signal = 24592
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global1._send('handsOff:')
				global2._send('setScript:', gag_Die)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class labDoor(Feature):
	#property vars (may be empty)
	x = 98
	y = 166
	noun = 4
	onMeCheck = 16
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				global91._send('say:', 4, 1, local2, 1)
			#end:case
			case 5:
				(cond
					case proc913_0(1):
						global91._send('say:', 4, 5, local2, 1)
					#end:case
					case global2._send('script:'): 0#end:case
					else:
						global2._send('setScript:', tryDoor)
					#end:else
				)
			#end:case
			case 2:
				super._send('doVerb:', param1, &rest)
			#end:case
			else:
				global91._send('say:', 4, 0, local2, 1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class niteShade(Feature):
	#property vars (may be empty)
	x = 295
	y = 110
	noun = 9
	onMeCheck = 4
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				cliffTalk._send('add:', -1, 9, 1, 0, 1, 'add:', -1, 9, 1, 0, 2, 'init:')
			#end:case
			case 5:
				if (rSacred._send('geniePresent:') == 1):
					global91._send('say:', 9, 5, 21, 0)
				else:
					global91._send('say:', 9, 5, 27, 1)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class minoOpening(Feature):
	#property vars (may be empty)
	x = 18
	y = 131
	onMeCheck = 64
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 5):
			global2._send('setScript:', goToLair)
		else:
			labRock._send('doVerb:', param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class cave(Feature):
	#property vars (may be empty)
	x = 307
	y = 106
	noun = 7
	onMeCheck = 8
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 5):
			if (rSacred._send('geniePresent:') == 1):
				global91._send('say:', 7, 5, 21, 1)
			else:
				global2._send('setScript:', crawlIntoCave)
			#endif
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class mount(Feature):
	#property vars (may be empty)
	x = 256
	y = 41
	noun = 13
	onMeCheck = 32
	
#end:class or instance

@SCI.instance
class oracle(Feature):
	#property vars (may be empty)
	x = 258
	y = 15
	noun = 14
	onMeCheck = 128
	
#end:class or instance

@SCI.instance
class myPath(Feature):
	#property vars (may be empty)
	x = 232
	y = 78
	noun = 15
	onMeCheck = 4096
	
#end:class or instance

@SCI.instance
class egoEnters(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				if (global12 == 320):
					global104._send('number:', 341, 'setLoop:', -1, 'play:')
				#endif
				global0._send(
					'view:', 3011,
					'setLoop:', 6,
					'setPri:', 15,
					'cel:', 0,
					'normal:', 0,
					'posn:', 257, 237,
					'cycleSpeed:', 8,
					'setCycle:', End, self
				)
			#end:case
			case 1:
				global0._send('cel:', 0, 'posn:', 228, 223, 'setCycle:', End, self)
			#end:case
			case 2:
				global0._send('cel:', 0, 'posn:', 199, 209, 'setCycle:', End, self)
			#end:case
			case 3:
				global0._send('cel:', 0, 'posn:', 175, 195, 'setCycle:', End, self)
			#end:case
			case 4:
				global0._send(
					'view:', 3011,
					'setLoop:', 1,
					'cel:', 5,
					'posn:', 164, 194,
					'cycleSpeed:', 8,
					'setCycle:', End, self
				)
			#end:case
			case 5:
				global0._send('view:', 301, 'setLoop:', 0, 'cel:', 2, 'normal:', 0, 'posn:', 161, 185)
				cycles = 4
			#end:case
			case 6:
				global0._send('cel:', 3, 'posn:', 161, 185)
				cycles = 4
			#end:case
			case 7:
				global0._send('cel:', 4, 'posn:', 161, 185)
				cycles = 4
			#end:case
			case 8:
				global0._send(
					'posn:', 162, 169,
					'reset:', 6,
					'setScale:', Scaler, 100, 5, 105, 65,
					'setMotion:', MoveTo, 172, 160, self
				)
			#end:case
			case 9:
				cycles = 6
			#end:case
			case 10:
				(cond
					case ((global12 == 320) and (not proc913_0(4))):
						global91._send('say:', 1, 0, 1, 1)
						proc341_1()
					#end:case
					case (global12 == 300):
						global1._send('handsOn:')
						global91._send('say:', 1, 0, 33, 1)
					#end:case
					else:
						global1._send('handsOn:')
					#end:else
				)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class fromLab(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if (global12 == 405):
					global0._send(
						'posn:', 109, 107,
						'setScale:', Scaler, 100, 5, 105, 65,
						'setMotion:', PolyPath, 138, 122, self
					)
				else:
					global0._send(
						'show:',
						'ignoreActors:', 1,
						'setScale:', Scaler, 100, 5, 105, 65,
						'setPri:', 8,
						'cycleSpeed:', 12,
						'setCycle:', End, self
					)
				#endif
			#end:case
			case 1:
				if (global12 == 405):
					self._send('cue:')
				else:
					global0._send(
						'reset:', 0,
						'posn:', 22, 138,
						'setMotion:', MoveTo, 63, 148, self
					)
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
class crawlOutOfCave(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send(
					'view:', 331,
					'setLoop:', 3,
					'normal:', 0,
					'posn:', 331, 108,
					'cycleSpeed:', 8,
					'moveSpeed:', 8,
					'setCycle:', Fwd,
					'setMotion:', MoveTo, 294, 116, self
				)
			#end:case
			case 1:
				global0._send('setLoop:', 5, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 2:
				global1._send('handsOn:')
				global0._send(
					'posn:', (global0._send('x:') - 12), (global0._send('y:') + 3),
					'reset:', 5,
					'setScale:', Scaler, 100, 5, 105, 65
				)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class crawlIntoCave(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 283, 121, self)
			#end:case
			case 1:
				cycles = 6
			#end:case
			case 2:
				if (rSacred._send('geniePresent:') == 1):
					global0._send('setScript:', 0)
					proc341_3()
				#endif
				if proc913_0(96):
					global91._send('say:', 7, 5, 32, 1, self)
				else:
					global91._send('say:', 7, 5, 31, 1, self)
				#endif
			#end:case
			case 3:
				global0._send('setHeading:', 45)
				cycles = 6
			#end:case
			case 4:
				if (rSacred._send('geniePresent:') == 1):
					proc341_2()
				#endif
				global0._send(
					'setScale:', 0,
					'view:', 331,
					'normal:', 0,
					'setLoop:', 1,
					'cel:', 5,
					'cycleSpeed:', 10,
					'setPri:', 7,
					'posn:', 285, 133,
					'setCycle:', Beg, self
				)
			#end:case
			case 5:
				kernel.DisposeScript(341)
				global0._send(
					'setLoop:', 2,
					'cel:', 0,
					'cycleSpeed:', 8,
					'moveSpeed:', 8,
					'posn:', 290, 117,
					'setCycle:', Fwd,
					'setMotion:', MoveTo, 331, 106, self
				)
			#end:case
			case 6:
				global5._send('eachElementDo:', #hide)
				global2._send('drawPic:', 98, -32758)
				cycles = 6
			#end:case
			case 7:
				global1._send('handsOn:')
				global2._send('newRoom:', 390)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class goNorth(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if (rSacred._send('geniePresent:') == 1):
					self._send('setScript:', kernel.ScriptID(341, 5), self)
				else:
					cycles = 6
				#endif
			#end:case
			case 1:
				global2._send('newRoom:', 350)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class goToLair(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 35, 140, self)
			#end:case
			case 1:
				global0._send('setHeading:', 315)
				cycles = 10
			#end:case
			case 2:
				global0._send(
					'view:', 362,
					'setLoop:', 3,
					'cel:', 0,
					'setPri:', 9,
					'normal:', 0,
					'posn:', 15, 146,
					'cycleSpeed:', 12,
					'setCycle:', End, self
				)
			#end:case
			case 3:
				global2._send('newRoom:', 440)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class tryDoor(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 127, 118, self)
			#end:case
			case 1:
				global0._send('setMotion:', PolyPath, 127, 113, self)
			#end:case
			case 2:
				global0._send(
					'view:', 361,
					'loop:', 1,
					'normal:', 0,
					'posn:', 119, 115,
					'cycleSpeed:', 10,
					'setCycle:', End, self
				)
			#end:case
			case 3:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 4:
				global0._send('reset:', 7, 'posn:', 127, 113)
				ticks = 18
			#end:case
			case 5:
				global91._send('say:', 4, 5, 20, 1, self)
			#end:case
			case 6:
				global91._send('say:', 4, 5, 20, 2, self)
			#end:case
			case 7:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class stepDown(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', 0, 'posn:', 162, 169)
				if (rSacred._send('geniePresent:') == 1):
					self._send('setScript:', kernel.ScriptID(341, 5), self)
				else:
					cycles = 6
				#endif
			#end:case
			case 1:
				global0._send('view:', 301, 'setLoop:', 8, 'cel:', 6, 'normal:', 0, 'posn:', 152, 170)
				cycles = 4
			#end:case
			case 2:
				global0._send('cel:', 0, 'normal:', 0, 'posn:', 168, 177)
				cycles = 4
			#end:case
			case 3:
				global0._send('cel:', 5, 'normal:', 0, 'posn:', 151, 170)
				cycles = 4
			#end:case
			case 4:
				global0._send('cel:', 2, 'normal:', 0, 'posn:', 165, 178)
				cycles = 4
			#end:case
			case 5:
				global0._send(
					'view:', 301,
					'setPri:', 15,
					'cycleSpeed:', 8,
					'setLoop:', 8,
					'cel:', 0,
					'normal:', 0,
					'posn:', 178, 184,
					'setCycle:', End, self
				)
			#end:case
			case 6:
				global0._send('cel:', 0, 'normal:', 0, 'posn:', 198, 197, 'setCycle:', End, self)
			#end:case
			case 7:
				global0._send('cel:', 0, 'normal:', 0, 'posn:', 218, 209, 'setCycle:', End, self)
			#end:case
			case 8:
				global0._send('cel:', 0, 'normal:', 0, 'posn:', 239, 220, 'setCycle:', End, self)
			#end:case
			case 9:
				global0._send('y:', 280)
				cycles = 4
			#end:case
			case 10:
				global2._send('newRoom:', 300)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class gag_Die(Script):
	#property vars (may be empty)
	name = r"""gag&Die"""
	
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if rSacred._send('geniePresent:'):
					kernel.ScriptID(341, 4)._send('setScript:', 0)
				#endif
				global0._send('setScript:', 0)
				if (rSacred._send('geniePresent:') == 1):
					local0 = 21
				else:
					local0 = 27
				#endif
				global91._send('say:', 12, 5, local0, 1, self)
			#end:case
			case 1:
				global0._send('setMotion:', PolyPath, 271, 118, self)
			#end:case
			case 2:
				global0._send(
					'view:', 331,
					'setLoop:', 4,
					'cel:', 0,
					'normal:', 0,
					'cycleSpeed:', 10,
					'setCycle:', End, self
				)
			#end:case
			case 3:
				global91._send('say:', 12, 5, local0, 2, self)
			#end:case
			case 4:
				global91._send('say:', 12, 5, local0, 3, self)
			#end:case
			case 5:
				if (rSacred._send('geniePresent:') == 1):
					proc341_3()
				#endif
				global104._send('stop:')
				global105._send('number:', 343, 'setLoop:', 1, 'play:')
				global0._send(
					'view:', 332,
					'loop:', 1,
					'cel:', 0,
					'posn:', 247, 128,
					'setCycle:', End, self
				)
			#end:case
			case 6:
				if (rSacred._send('geniePresent:') == 1):
					proc341_2()
				#endif
				cycles = 6
			#end:case
			case 7:
				kernel.DisposeScript(341)
				cycles = 6
			#end:case
			case 8:
				global91._send('say:', 12, 5, local0, 4, self)
			#end:case
			case 9:
				proc0_1(20)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class dieHard(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				temp1 = 0
				global91._send('say:', 3, 3, 17, 1, self, 340)
			#end:case
			case 1:
				global105._send('number:', 305, 'setLoop:', 1, 'play:')
				global0._send(
					'setLoop:', 2,
					'normal:', 0,
					'cycleSpeed:', 1,
					'setPri:', 15,
					'setCycle:', Fwd
				)
				seconds = 3
			#end:case
			case 2:
				global105._send('number:', 306, 'setLoop:', 1, 'play:', self)
				global2._send('walkOffEdge:', 1)
				global0._send(
					'setLoop:', 2,
					'setStep:', -1, 15,
					'setMotion:', MoveTo, global0._send('x:'), 300, self
				)
			#end:case
			case 3: 0#end:case
			case 4:
				seconds = 4
			#end:case
			case 5:
				global105._send('number:', 307, 'setLoop:', 1, 'play:')
				kernel.ShakeScreen(3, 1)
				seconds = 3
			#end:case
			case 6:
				global91._send('say:', 3, 3, 17, 2, self, 340)
			#end:case
			case 7:
				proc0_1(8)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoDoVerb(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				return 0
			#end:case
			case 5:
				return 0
			#end:case
			case 2:
				return 0
			#end:case
			case 31:
				if (proc913_0(14) and proc913_0(4) and (not proc913_0(15))):
					global1._send('handsOff:')
					kernel.ScriptID(344, 2)._send('setScript:', kernel.ScriptID(344, 3))
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

