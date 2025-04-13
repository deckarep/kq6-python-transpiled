#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 21
import sci_sh
import kernel
import Main
import KQ6Room
import n913
import Feature
import Motion
import Game
import User
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rCliffs = 0,
	proc21_1 = 1,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0
local200
local218
local246 = [74, 103, 132, 161, 190, 219, 248, 219, 190, 161, 132, 103, 132, 161, 190, 219]
local262 = [184, 172, 160, 148, 136, 124, 112, 100, 88, 76, 64, 52, 40, 28, 16, 4]
local278 = [103, 132, 161, 190, 161, 132, 103, 74, 45]
local287 = [100, 88, 76, 64, 52, 40, 28, 16, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
local324 = None
local325 = None
local326 = None
local327 = None
local328 = None


@SCI.procedure
def proc21_1():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	if (kernel.ScriptID(21, 0)._send('stepSound:') == 1):
		kernel.ScriptID(21, 0)._send('stepSound:', 4)
	else:
		kernel.ScriptID(21, 0)._send('stepSound:', (kernel.ScriptID(21, 0)._send('stepSound:') - 1))
	#endif
	global104._send(
		'number:', match kernel.ScriptID(21, 0)._send('stepSound:')
				case 1: 301#end:case
				case 2: 302#end:case
				case 3: 303#end:case
				case 4: 304#end:case
			#end:match,
		'setLoop:', 1,
		'play:'
	)
#end:procedure

class rCliffs(Rgn):
	#property vars (may be empty)
	cliffFace = 0
	puzzleIsUp = 0
	stepDirection = 0
	stepSound = 1
	cheatCount = 0
	
	@classmethod
	def newRoom(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		keep = proc999_5(param1, 300, 320)
		initialized = 0
		super._send('newRoom:', param1, &rest)
	#end:method

	@classmethod
	def notify():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		local325 = 1
		local326 = kernel.Random(500, 1000)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		local325 = 0
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:')
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global69._send('enable:', 6)
		super._send('dispose:')
	#end:method

#end:class or instance

class CliffRoom(KQ6Room):
	#property vars (may be empty)
	maxRocks = 0
	rockCount = 0
	flipRocks = 0
	rockList = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not rockList):
			rockList = Set._send('new:')._send('add:')
		#endif
		super._send('init:', &rest)
	#end:method

	@classmethod
	def constantRocks():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		rCliffs._send('cheatCount:', 0)
		temp0 = 0
		while (temp0 < 7): # inline for
			local200[temp0] = RockStep._send('new:')._send(
				'x:', if argc:
						(320 - local246[temp0])
					else:
						local246[temp0]
					#endif,
				'y:', local262[temp0],
				'cel:', 3,
				'rockPointer:', temp0,
				'corner:', (1 if (temp0 == 6) else 0),
				'init:',
				'stopUpd:'
			)
			rockList._send('add:', local200[temp0])
			if (temp0 < 6):
				local200[temp0]._send('addToPic:')
			#endif
			# for:reinit
			temp0.post('++')
		#end:loop
	#end:method

	@classmethod
	def callForRocks():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (global11 == 300):
			self._send('rockCount:', 0, 'maxRocks:', 9)
		else:
			self._send('rockCount:', 7, 'maxRocks:', 16)
		#endif
		self._send('makeARock:')
	#end:method

	@classmethod
	def makeARock():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (rockCount == maxRocks):
			if (global11 == 300):
				global91._send('say:', 8, 5, 18, 2, 0, 21)
			#endif
			global2._send('script:')._send('cue:')
		else:
			kernel.ShakeScreen(1, kernel.Random(0, 2))
			global104._send('number:', 300, 'setLoop:', 1, 'play:')
			if (rockCount > 0):
				local200[(rockCount - 1)]._send('stopUpd:')
			#endif
			local200[rockCount] = RockStep._send('new:')._send(
				'x:', (cond
						case (global11 == 300): local278[rockCount]#end:case
						case flipRocks:
							(320 - local246[rockCount])
						#end:case
						else: local246[rockCount]#end:else
					),
				'y:', if (global11 == 300):
						local287[rockCount]
					else:
						local262[rockCount]
					#endif,
				'cel:', if 
						(or
							(global12 == 130)
							(global12 == 340)
							(global12 == 370)
						)
						2
					else:
						0
					#endif,
				'rockPointer:', rockCount,
				'corner:', (cond
						case ((rockCount == 3) and (global11 == 300)): 1#end:case
						case 
							(and
								((rockCount == 6) or (rockCount == 11))
								(global11 == 320)
							):
							1
						#end:case
						else: 0#end:else
					),
				'capStone:', if 
						(or
							((rockCount == 14) and (global11 == 320))
							((rockCount == 7) and (global11 == 300))
						)
						1
					else:
						0
					#endif,
				'init:',
				'setCycle:', End, RockStep
			)
			rockList._send('add:', local200[rockCount])
			self._send('rockCount:', (self._send('rockCount:') + 1))
		#endif
	#end:method

	@classmethod
	def allRocksOut(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		rCliffs._send('cheatCount:', 0)
		if (global11 == 300):
			temp1 = 9
			temp2 = 0
		else:
			temp1 = 16
			temp2 = 0
		#endif
		temp0 = temp2
		while (temp0 < temp1): # inline for
			local200[temp0] = RockStep._send('new:')._send(
				'x:', (cond
						case (global11 == 300): local278[temp0]#end:case
						case param1:
							(320 - local246[temp0])
						#end:case
						else: local246[temp0]#end:else
					),
				'y:', (local287[temp0] if (global11 == 300) else local262[temp0]),
				'cel:', 3,
				'rockPointer:', temp0,
				'corner:', (cond
						case (global11 == 300):
							(1 if (temp0 == 3) else 0)
						#end:case
						case ((temp0 == 6) or (temp0 == 11)): 1#end:case
						else: 0#end:else
					),
				'capStone:', (cond
						case (global11 == 300):
							(1 if (temp0 == 7) else 0)
						#end:case
						case (temp0 == 14): 1#end:case
						else: 0#end:else
					),
				'init:',
				'stopUpd:'
			)
			rockList._send('add:', local200[temp0])
			if (temp0 < 6):
				local200[temp0]._send('addToPic:')
			#endif
			# for:reinit
			temp0.post('++')
		#end:loop
		kernel.UnLoad(128, 300)
	#end:method

	@classmethod
	def dumpRocks():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if rockList:
			rockList._send('release:')
		#endif
		temp0 = 0
		while (temp0 < 16): # inline for
			if global5._send('contains:', local200[temp0]):
				local200[temp0]._send('dispose:', 'delete:')
				local200[temp0] = 0
			#endif
			# for:reinit
			temp0.post('++')
		#end:loop
		temp0 = 0
		while (temp0 < 16): # inline for
			if global10._send('contains:', local200[temp0]):
				local200[temp0]._send('dispose:', 'delete:')
				local200[temp0] = 0
			#endif
			# for:reinit
			temp0.post('++')
		#end:loop
	#end:method

	@classmethod
	def newRoom():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global74._send('delete:', global2)
		if rockList:
			rockList._send('release:', 'dispose:')
			rockList = 0
		#endif
		super._send('newRoom:', &rest)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				User._send('controls:')
				(param1._send('type:') & 0x0040)
				(param1._send('message:') != 0)
				(global69._send('curIcon:') == global69._send('at:', 0))
				kernel.IsObject(rockList)
			)
			if (not temp0 = rockList._send('firstTrue:', #onMe, User._send('curEvent:'))):
				temp0 = rockList._send('firstTrue:', #onMe, global0)
			#endif
			temp1 = rockList._send('indexOf:', temp0)
			match param1._send('message:')
				case 1:
					if (rockList._send('size:') != (temp1 - 1)):
						temp0 = rockList._send('at:', (temp1 + 1))
					#endif
				#end:case
				case 5:
					if (temp1 != 0):
						temp0 = rockList._send('at:', (temp1 - 1))
					#endif
				#end:case
				else: 0#end:else
			#end:match
			if kernel.IsObject(temp0):
				kernel.SetCursor((temp0._send('x:') + 8), temp0._send('y:'))
			#endif
			param1._send('claimed:', 1)
			return
		else:
			super._send('handleEvent:', param1)
		#endif
	#end:method

#end:class or instance

class RockStep(Prop):
	#property vars (may be empty)
	view = 300
	loop = 5
	signal = 16401
	cycleSpeed = 24
	corner = 0
	rockPointer = 0
	capStone = 0
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				global91._send('say:', 6, 1, 0, 1, 0, 21)
			#end:case
			case 5:
				global91._send('say:', 6, 5, 0, 1, 0, 21)
			#end:case
			case 2:
				global91._send('say:', 6, 2, 0, 1, 0, 21)
			#end:case
			else:
				global91._send('say:', 6, 0, 0, 1, 0, 21)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		global72._send('addToFront:', self)
		global73._send('addToFront:', self)
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
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global2._send('makeARock:')
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if local325:
			(cond
				case global0._send('script:'):#end:case
				case (local326 > 0):
					local326.post('--')
				#end:case
				else:
					global0._send('setScript:', egoWobbles)
				#end:else
			)
		#endif
		super._send('doit:')
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				User._send('canInput:')
				(param1._send('type:') != 16384)
				(not param1._send('modifiers:'))
				(global69._send('curIcon:') == global69._send('at:', 0))
			)
			if 
				(and
					((param1._send('message:') == 13) or (param1._send('type:') == 1))
					self._send('onMe:', param1)
				)
				param1._send('claimed:', 1)
				local325 = 0
				(cond
					case (global0._send('script:') == egoWobbles):
						proc913_1(59)
						global91._send('say:', 6, 3, 17, 1, 0, 21)
					#end:case
					case 
						(and
							(or
								(global0._send('view:') == 900)
								(global0._send('view:') == 308)
								(global0._send('view:') == 3081)
							)
							(self._send('rockPointer:') == 0)
						):
						global0._send('setScript:', takeFirstStep, 0, local200[0])
					#end:case
					case 
						(and
							((self._send('y:') - global0._send('y:')) < 15)
							((self._send('y:') - global0._send('y:')) > 2)
						):
						global0._send(
							'setScript:', stepDown, 0, local200[self._send('rockPointer:')]
						)
					#end:case
					case 
						(or
							(kernel.Abs((global0._send('y:') - self._send('y:'))) > 20)
							(kernel.Abs((global0._send('x:') - self._send('x:'))) > 64)
						):
						global91._send('say:', 6, 3, 16, 1, 0, 21)
					#end:case
					case 
						(or
							(and
								((self._send('x:') - global0._send('x:')) < 40)
								((self._send('x:') - global0._send('x:')) > 35)
								(self._send('y:') < global0._send('y:'))
							)
							(and
								((global0._send('x:') - self._send('x:')) < 57)
								((global0._send('x:') - self._send('x:')) > 54)
								(self._send('y:') < global0._send('y:'))
							)
						):
						global0._send(
							'setScript:', takeStep, 0, local200[self._send('rockPointer:')]
						)
					#end:case
					case 
						(and
							(self._send('x:') > global0._send('x:'))
							(global0._send('y:') < 99)
							(global11 == 300)
							(self._send('y:') < global0._send('y:'))
						):
						global0._send(
							'setScript:', takeStep, 0, local200[self._send('rockPointer:')]
						)
					#end:case
					case 
						(and
							(self._send('x:') > global0._send('x:'))
							(self._send('y:') < global0._send('y:'))
						):
						global0._send(
							'setScript:', takeStep, 0, local200[self._send('rockPointer:')]
						)
					#end:case
					case 
						(and
							(self._send('x:') < global0._send('x:'))
							(self._send('y:') < global0._send('y:'))
						):
						global0._send(
							'setScript:', takeStep, 0, local200[self._send('rockPointer:')]
						)
					#end:case
				)
			else:
				super._send('handleEvent:', param1)
			#endif
		else:
			super._send('handleEvent:', param1)
		#endif
		param1._send('claimed:')
	#end:method

#end:class or instance

class HyroGliph(View):
	#property vars (may be empty)
	hyroVal = 0
	deathButt = 0
	
#end:class or instance

@SCI.instance
class letter(HyroGliph):
	#property vars (may be empty)
#end:class or instance

class PuzzleInset(View):
	#property vars (may be empty)
	maxButtons = 0
	buttNumber = 0
	buttView = 0
	buttTop = 0
	buttLeft = 0
	buttRight = 0
	buttBottom = 0
	buttLoop = 0
	buttCel = 0
	buttX = 0
	buttY = 0
	buttVal = 0
	buttKill = 0
	buttonCount = 0
	correctButton = 1
	savePMouse = 0
	solvedPuzz = 0
	lookMsg = 0
	puzzNumber = 0
	
	@classmethod
	def doButton(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 0
		while (temp0 < buttNumber): # inline for
			if 
				(and
					(<=
						proc999_6(buttLeft, temp0)
						param1
						proc999_6(buttRight, temp0)
					)
					(<=
						proc999_6(buttTop, temp0)
						param2
						proc999_6(buttBottom, temp0)
					)
				)
				if (local218[temp0] == 0):
					if ((global11 == 300) and (local324 == 3)):
						global110 = temp0
					#endif
					if ((puzzNumber == 2) or (puzzNumber == 4)):
						temp1 = 2
					else:
						temp1 = 0
					#endif
					local324.post('++')
					global104._send('number:', 308, 'setLoop:', 1, 'play:')
					local218[temp0] = letter._send('new:')._send(
						'view:', buttView,
						'setLoop:', proc999_6(buttLoop, temp0),
						'cel:', proc999_6(buttCel, temp0),
						'x:', (proc999_6(buttX, temp0) + temp1),
						'y:', proc999_6(buttY, temp0),
						'hyroVal:', proc999_6(buttVal, temp0),
						'deathButt:', proc999_6(buttKill, temp0),
						'setPri:', 14,
						'init:',
						'stopUpd:'
					)
					local327 = 1
					if local218[temp0]._send('deathButt:'):
						local328 = 1
						rCliffs._send('cue:')
						global2._send('setScript:', seeYa, 0, self)
					else:
						self._send('cue:', local218[temp0]._send('hyroVal:'))
					#endif
					return 1
				else:
					return 1
				#endif
				(break)
			#endif
			# for:reinit
			temp0.post('++')
		#end:loop
	#end:method

	@classmethod
	def puzzSolved():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global2._send('setScript:', puzzleSolvedPause, 0, self)
	#end:method

	@classmethod
	def cue(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('buttonCount:', (self._send('buttonCount:') + 1))
		(cond
			case ((param1 == correctButton) or (param1 == -1)):
				self._send('correctButton:', (self._send('correctButton:') + 1))
				if (correctButton == (maxButtons + 1)):
					correctButton = (buttonCount = 0 + 1)
					global2._send('setScript:', notifyTheRoom, 0, self)
				#endif
			#end:case
			case (buttonCount == buttNumber):
				global2._send('setScript:', clearTheButtons, 0, self)
			#end:case
			case (param1 != correctButton):
				self._send('correctButton:', (self._send('correctButton:') + 10))
			#end:case
		)
	#end:method

	@classmethod
	def dumpButtons():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 0
		while (temp0 < 28): # inline for
			if (local218[temp0] != 0):
				local218[temp0]._send('dispose:')
				local218[temp0] = 0
			#endif
			# for:reinit
			temp0.post('++')
		#end:loop
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global69._send('disable:', 3, 0, 4, 5, 6)
		temp0 = 0
		while (temp0 < 28): # inline for
			local218[temp0] = 0
			# for:reinit
			temp0.post('++')
		#end:loop
		rCliffs._send('puzzleIsUp:', 1)
		self._send('setPri:', 12, 'signal:', 4112, 'ignoreActors:', 'stopUpd:')
		super._send('init:', &rest)
		global72._send('addToFront:', self)
		global73._send('addToFront:', self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		rCliffs._send('puzzleIsUp:', 0)
		self._send('dumpButtons:')
		correctButton = (local324 = buttonCount = 0 + 1)
		global72._send('delete:', self)
		global73._send('delete:', self)
		if (not local328):
			global1._send('handsOn:')
		#endif
		global69._send('enable:', 6)
		super._send('dispose:')
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				User._send('canInput:')
				(param1._send('type:') != 16384)
				(or
					((param1._send('message:') == 13) and (param1._send('type:') & 0x0004))
					(param1._send('type:') == 1)
				)
				(not param1._send('modifiers:'))
			)
			(cond
				case solvedPuzz:
					param1._send('claimed:', 1)
					self._send('solvedPuzz:', 0)
					self._send('dispose:')
				#end:case
				case 
					(and
						self._send('onMe:', param1)
						(global69._send('curIcon:') == global69._send('at:', 2))
					):
					param1._send('claimed:', 1)
					global91._send('say:', lookMsg, 1, 0, 1, 0, 21)
				#end:case
				case 
					(and
						(or
							(param1._send('type:') & 0x0001)
							(and
								(param1._send('type:') & 0x0004)
								(param1._send('message:') == 13)
							)
						)
						self._send('doButton:', param1._send('x:'), param1._send('y:'))
					):
					param1._send('claimed:', 1)
				#end:case
				case (param1._send('type:') & 0x0001):
					param1._send('claimed:', 1)
					global2._send('setScript:', clearTheButtons, 0, self)
				#end:case
				case ((param1._send('type:') & 0x0001) and param1._send('modifiers:')):
					param1._send('claimed:', 0)
				#end:case
				case (param1._send('type:') & 0x0004):
					(cond
						case (param1._send('message:') == 13):
							param1._send('claimed:', 1)
							global91._send('say:', 8, 5, 7, 1, 0, 21)
							self._send('dispose:')
						#end:case
						case 27:
							param1._send('claimed:', 1)
							global91._send('say:', 8, 5, 7, 1, 0, 21)
							self._send('dispose:')
						#end:case
						else:
							param1._send('claimed:', 0)
						#end:else
					)
				#end:case
				else:
					param1._send('claimed:', 0)
				#end:else
			)
		else:
			param1._send('claimed:', 0)
		#endif
		param1._send('claimed:')
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
				rCliffs._send('cheatCount:', (rCliffs._send('cheatCount:') - 1))
				(cond
					case local200[(register._send('rockPointer:') + 1)]._send('corner:'):
						if (global0._send('loop:') < 6):
							rCliffs._send('stepDirection:', 1)
						else:
							rCliffs._send('stepDirection:', 2)
						#endif
						ticks = 4
					#end:case
					case (rCliffs._send('stepDirection:') == 4):
						global0._send(
							'view:', 3011,
							'setLoop:', 1,
							'cel:', 0,
							'x:', (global0._send('x:') + 18),
							'y:', (global0._send('y:') + 11)
						)
						rCliffs._send('stepDirection:', 1)
						cycles = 6
					#end:case
					case (rCliffs._send('stepDirection:') == 3):
						global0._send(
							'view:', 3011,
							'setLoop:', 1,
							'cel:', 0,
							'x:', (global0._send('x:') - 18),
							'y:', (global0._send('y:') + 11)
						)
						rCliffs._send('stepDirection:', 2)
						cycles = 6
					#end:case
					else:
						self._send('cue:')
					#end:else
				)
			#end:case
			case 1:
				if (rCliffs._send('stepSound:') == 1):
					rCliffs._send('stepSound:', 4)
				else:
					rCliffs._send('stepSound:', (rCliffs._send('stepSound:') - 1))
				#endif
				global104._send(
					'number:', match rCliffs._send('stepSound:')
							case 1: 301#end:case
							case 2: 302#end:case
							case 3: 303#end:case
							case 4: 304#end:case
						#end:match,
					'setLoop:', 1,
					'play:'
				)
				if (rCliffs._send('stepDirection:') == 2):
					global0._send(
						'view:', 301,
						'setLoop:', 7,
						'cel:', 0,
						'cycleSpeed:', 16,
						'posn:', (register._send('x:') + 24), (register._send('y:') - 13)
					)
				else:
					global0._send(
						'view:', 301,
						'setLoop:', 8,
						'cel:', 0,
						'posn:', (register._send('x:') - 6), (register._send('y:') - 13),
						'cycleSpeed:', 16
					)
				#endif
				cycles = 6
			#end:case
			case 2:
				global0._send('cel:', 1)
				if (rCliffs._send('stepDirection:') == 2):
					global0._send('posn:', (register._send('x:') + 19), (register._send('y:') - 11))
				else:
					global0._send('posn:', (register._send('x:') - 3), (register._send('y:') - 11))
				#endif
				cycles = 5
			#end:case
			case 3:
				global0._send('cel:', 2)
				if (rCliffs._send('stepDirection:') == 2):
					global0._send('posn:', (register._send('x:') + 23), (register._send('y:') - 8))
				else:
					global0._send('posn:', (register._send('x:') - 5), (register._send('y:') - 11))
				#endif
				cycles = 5
			#end:case
			case 4:
				global0._send('cel:', 3)
				if (rCliffs._send('stepDirection:') == 2):
					global0._send('posn:', (register._send('x:') + 18), (register._send('y:') - 14))
				else:
					global0._send('posn:', (register._send('x:') - 5), (register._send('y:') - 14))
				#endif
				cycles = 5
			#end:case
			case 5:
				global0._send('cel:', 4)
				if (rCliffs._send('stepDirection:') == 2):
					global0._send('posn:', (register._send('x:') + 19), (register._send('y:') - 14))
				else:
					global0._send('posn:', (register._send('x:') - 6), (register._send('y:') - 14))
				#endif
				cycles = 5
			#end:case
			case 6:
				global0._send('cel:', 5)
				if (rCliffs._send('stepDirection:') == 2):
					global0._send('posn:', (register._send('x:') + 19), (register._send('y:') - 14))
				else:
					global0._send('posn:', (register._send('x:') - 6), (register._send('y:') - 14))
				#endif
				cycles = 5
			#end:case
			case 7:
				global0._send('cel:', 6)
				if (rCliffs._send('stepDirection:') == 2):
					global0._send('posn:', (register._send('x:') + 19), (register._send('y:') - 14))
				else:
					global0._send('posn:', (register._send('x:') - 4), (register._send('y:') - 14))
				#endif
				cycles = 5
			#end:case
			case 8:
				(cond
					case 
						(and
							(register._send('corner:') == 1)
							(rCliffs._send('stepDirection:') == 2)
						):
						global0._send(
							'setLoop:', 5,
							'cel:', 0,
							'cycleSpeed:', 7,
							'posn:', (register._send('x:') + 9), (global0._send('y:') + 18),
							'setCycle:', End, self
						)
						rCliffs._send('stepDirection:', 3)
					#end:case
					case (register._send('corner:') == 1):
						global0._send(
							'setLoop:', 4,
							'cel:', 0,
							'cycleSpeed:', 7,
							'posn:', (register._send('x:') + 8), (global0._send('y:') + 18),
							'setCycle:', End, self
						)
						rCliffs._send('stepDirection:', 4)
					#end:case
					else:
						self._send('cue:')
					#end:else
				)
			#end:case
			case 9:
				(cond
					case (register._send('corner:') and (global0._send('loop:') == 5)):
						global0._send(
							'posn:', (register._send('x:') + 27), (register._send('y:') - 2),
							'setLoop:', kernel.Random(1, 2),
							'cel:', 0
						)
					#end:case
					case (register._send('corner:') and (global0._send('loop:') == 4)):
						global0._send(
							'posn:', (register._send('x:') - 9), (register._send('y:') - 1),
							'setLoop:', 6,
							'cel:', 0
						)
					#end:case
					case (rCliffs._send('stepDirection:') == 1):
						global0._send(
							'view:', 301,
							'setLoop:', kernel.Random(1, 2),
							'cel:', 0,
							'posn:', (register._send('x:') + 26), (register._send('y:') - 1)
						)
					#end:case
					else:
						global0._send(
							'view:', 301,
							'setLoop:', 6,
							'cel:', 0,
							'posn:', (register._send('x:') - 8), (register._send('y:') - 1)
						)
					#end:else
				)
				cycles = 6
			#end:case
			case 10:
				global1._send('handsOn:')
				if (register._send('corner:') != 1):
					local325 = 1
					local326 = kernel.Random(1000, 2000)
				#endif
				if (register._send('rockPointer:') == 0):
					if (kernel.ScriptID(21, 0)._send('cliffFace:') == 0):
						global2._send('cue:', -1)
					else:
						global2._send('cue:', 0)
					#endif
				#endif
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class takeFirstStep(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('actions:', egoStepVerb, 'setMotion:', MoveTo, 110, 112, self)
			#end:case
			case 1:
				rCliffs._send('stepSound:', 1)
				global104._send('number:', 301, 'setLoop:', 1, 'play:')
				global0._send('view:', 301, 'normal:', 0, 'setLoop:', 0, 'cel:', 0)
				ticks = 6
			#end:case
			case 2:
				global0._send('cel:', 1)
				ticks = 6
			#end:case
			case 3:
				global0._send(
					'cel:', 2,
					'posn:', (register._send('x:') + 7), (register._send('y:') + 9),
					'cycleSpeed:', 10,
					'setCycle:', End, self
				)
			#end:case
			case 4:
				global1._send('handsOn:')
				global0._send(
					'posn:', (register._send('x:') + 26), (register._send('y:') - 2),
					'setLoop:', 2,
					'cel:', 0
				)
				local325 = 1
				rCliffs._send('stepDirection:', 3)
				local326 = kernel.Random(1000, 2000)
				global74._send('add:', global2)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class takeStep(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				rCliffs._send('cheatCount:', (rCliffs._send('cheatCount:') + 1))
				(cond
					case (rCliffs._send('stepDirection:') == 2):
						global0._send(
							'view:', 3011,
							'setLoop:', 1,
							'cel:', 0,
							'posn:', (register._send('x:') - 19), (register._send('y:') + 21)
						)
						rCliffs._send('stepDirection:', 3)
						cycles = 2
					#end:case
					case (rCliffs._send('stepDirection:') == 1):
						global0._send(
							'view:', 3011,
							'setLoop:', 1,
							'cel:', 0,
							'posn:', (register._send('x:') + 37), (register._send('y:') + 19)
						)
						rCliffs._send('stepDirection:', 4)
						cycles = 2
					#end:case
					else:
						self._send('cue:')
					#end:else
				)
			#end:case
			case 1:
				if (rCliffs._send('stepSound:') == 4):
					rCliffs._send('stepSound:', 1)
				else:
					rCliffs._send('stepSound:', (rCliffs._send('stepSound:') + 1))
				#endif
				global104._send(
					'number:', match rCliffs._send('stepSound:')
							case 1: 301#end:case
							case 2: 302#end:case
							case 3: 303#end:case
							case 4: 304#end:case
						#end:match,
					'setLoop:', 1,
					'play:'
				)
				if (rCliffs._send('stepDirection:') == 3):
					global0._send(
						'view:', 301,
						'cycleSpeed:', 10,
						'setLoop:', kernel.Random(1, 2),
						'cel:', 0,
						'posn:', (register._send('x:') - 2), (register._send('y:') + 10),
						'setCycle:', End, self
					)
				else:
					global0._send(
						'view:', 301,
						'setLoop:', 6,
						'cycleSpeed:', 10,
						'posn:', (register._send('x:') + 20), (register._send('y:') + 11),
						'setCycle:', End, self
					)
				#endif
			#end:case
			case 2:
				if (rCliffs._send('stepDirection:') == 3):
					global0._send(
						'posn:', (register._send('x:') + 27), (register._send('y:') - 2),
						'cel:', 0
					)
				else:
					global0._send(
						'posn:', (register._send('x:') - 9), (register._send('y:') - 1),
						'cel:', 0
					)
				#endif
				ticks = 6
			#end:case
			case 3:
				(cond
					case 
						(and
							(register._send('corner:') == 1)
							(rCliffs._send('stepDirection:') == 3)
						):
						global0._send(
							'setLoop:', 4,
							'cycleSpeed:', 12,
							'posn:', (register._send('x:') + 7), (global0._send('y:') + 7),
							'setCycle:', End, self
						)
					#end:case
					case (register._send('corner:') == 1):
						global0._send(
							'setLoop:', 5,
							'cycleSpeed:', 12,
							'posn:', (register._send('x:') + 10), (global0._send('y:') + 5),
							'setCycle:', End, self
						)
					#end:case
					else:
						self._send('cue:')
					#end:else
				)
			#end:case
			case 4:
				(cond
					case 
						(register._send('corner:') and (rCliffs._send('stepDirection:') == 3)):
						global0._send(
							'posn:', (register._send('x:') - 9), (register._send('y:') - 1),
							'setLoop:', 6,
							'cel:', 0
						)
						rCliffs._send('stepDirection:', 4)
					#end:case
					case register._send('corner:'):
						global0._send(
							'posn:', (register._send('x:') + 27), (register._send('y:') - 2),
							'setLoop:', kernel.Random(1, 2),
							'cel:', 0
						)
						rCliffs._send('stepDirection:', 3)
					#end:case
				)
				ticks = 6
			#end:case
			case 5:
				global1._send('handsOn:')
				if (register._send('corner:') != 1):
					local325 = 1
					local326 = kernel.Random(1000, 2000)
				#endif
				if (register._send('capStone:') == 1):
					if (rCliffs._send('stepDirection:') == 4):
						rCliffs._send('stepDirection:', 3)
					else:
						rCliffs._send('stepDirection:', 4)
					#endif
					global0._send('setScript:', nextScreenUp, 0, register)
				#endif
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class nextScreenUp(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				if (rCliffs._send('stepSound:') == 4):
					rCliffs._send('stepSound:', 1)
				else:
					rCliffs._send('stepSound:', (rCliffs._send('stepSound:') + 1))
				#endif
				global104._send(
					'number:', match rCliffs._send('stepSound:')
							case 1: 301#end:case
							case 2: 302#end:case
							case 3: 303#end:case
							case 4: 304#end:case
						#end:match,
					'setLoop:', 1,
					'play:'
				)
				if (rCliffs._send('stepDirection:') == 4):
					global0._send(
						'cycleSpeed:', 10,
						'setLoop:', kernel.Random(1, 2),
						'setCycle:', End, self
					)
				else:
					global0._send('setLoop:', 6, 'cycleSpeed:', 10, 'setCycle:', End, self)
				#endif
			#end:case
			case 1:
				if (rCliffs._send('stepDirection:') == 4):
					global0._send(
						'posn:', (register._send('x:') + 56), (register._send('y:') - 14),
						'cel:', 0
					)
				else:
					global0._send(
						'posn:', (register._send('x:') - 38), (register._send('y:') - 13),
						'cel:', 0
					)
				#endif
				ticks = 6
			#end:case
			case 2:
				global1._send('handsOn:')
				global0._send('hide:')
				if (global11 == 320):
					global2._send('cue:', 1)
					self._send('dispose:')
				else:
					global2._send('newRoom:', global2._send('north:'))
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class notifyTheRoom(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('givePoints:', 1)
				register._send('dispose:')
				cycles = 1
			#end:case
			case 1:
				match rCliffs._send('cliffFace:')
					case 0:
						match global11
							case 300:
								proc913_1(5)
							#end:case
							case 320:
								proc913_1(123)
							#end:case
						#end:match
					#end:case
					case 1:
						proc913_1(124)
					#end:case
					case 2:
						proc913_1(125)
					#end:case
					case 3:
						proc913_1(126)
						proc913_1(6)
					#end:case
				#end:match
				if (global11 == 320):
					global91._send('say:', 4, 5, 6, 1, self, 21)
				else:
					global91._send('say:', 8, 5, 18, 1, self, 21)
				#endif
			#end:case
			case 2:
				global2._send('notify:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoWobbles(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global104._send('number:', 305, 'setLoop:', 1, 'play:')
				if (global0._send('loop:') == 6):
					global0._send(
						'view:', 3011,
						'posn:', (global0._send('x:') + 18), (global0._send('y:') + 10),
						'cycleSpeed:', 12,
						'setLoop:', 1
					)
				else:
					global0._send(
						'view:', 301,
						'posn:', (global0._send('x:') - 18), (global0._send('y:') + 7),
						'cycleSpeed:', kernel.Random(4, 16),
						'setLoop:', 3
					)
				#endif
				global0._send('cel:', 0, 'setCycle:', End, self)
			#end:case
			case 1:
				if (global0._send('view:') == 301):
					global0._send('setCycle:', Beg, self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 2:
				if (global0._send('view:') == 301):
					global0._send(
						'posn:', (global0._send('x:') + 18), (global0._send('y:') - 7),
						'setLoop:', kernel.Random(1, 2)
					)
				else:
					global0._send(
						'posn:', (global0._send('x:') - 18), (global0._send('y:') - 10),
						'setLoop:', 6
					)
				#endif
				global0._send('view:', 301, 'cycleSpeed:', 18, 'cel:', 0)
				local326 = kernel.Random(1000, 2000)
				proc913_2(59)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class seeYa(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global69._send('disable:', 6)
				register._send('dispose:')
				ticks = 4
			#end:case
			case 1:
				global91._send('say:', 3, 5, 3, 1, self, 21)
			#end:case
			case 2:
				local200[6]._send('setCycle:', Beg, self)
				global104._send('number:', 300, 'setLoop:', 1, 'play:')
			#end:case
			case 3:
				global91._send('say:', 3, 5, 3, 2, self, 21)
			#end:case
			case 4:
				global0._send(
					'posn:', (global0._send('x:') - 10), global0._send('y:'),
					'ignoreActors:',
					'illegalBits:', 0,
					'view:', 4011,
					'normal:', 0,
					'cycleSpeed:', 6,
					'setLoop:', 0,
					'setCycle:', CT, 10, 1, self
				)
			#end:case
			case 5:
				global104._send('number:', 306, 'setLoop:', 1, 'play:', self)
				global0._send('setCycle:', End)
			#end:case
			case 6:
				global0._send('y:', 280)
				seconds = 2
			#end:case
			case 7:
				global104._send('number:', 307, 'setLoop:', 1, 'play:')
				kernel.ShakeScreen(2, 2)
				ticks = 4
			#end:case
			case 8:
				global91._send('say:', 3, 5, 3, 3, self, 21)
			#end:case
			case 9:
				global105._send('fade:', 0, 5, 5)
				proc0_1(6)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class clearTheButtons(Script):
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
				register._send('dispose:')
				cycles = 4
			#end:case
			case 2:
				if local327:
					global91._send('say:', 8, 5, 7, 1, self, 21)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 3:
				local327 = 0
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class puzzleSolvedPause(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				cycles = 1
			#end:case
			case 1:
				global91._send('say:', 8, 5, 8, 1, self, 21)
			#end:case
			case 2:
				if (global11 == 320):
					if (global0._send('cel:') == 1):
						global0._send('view:', 301, 'setLoop:', 6, 'cel:', 0)
					else:
						global0._send('view:', 301, 'setLoop:', 1)
					#endif
				#endif
				kernel.UnLoad(128, 3012)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoStepVerb(Actions):
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
			else:
				global91._send('say:', 0, 0, 64, 1, 0, 899)
				return 1
			#end:else
		#end:match
	#end:method

#end:class or instance

