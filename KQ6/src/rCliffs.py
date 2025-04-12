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

	if ((kernel.ScriptID(21, 0) stepSound:) == 1):
		(kernel.ScriptID(21, 0) stepSound: 4)
	else:
		(kernel.ScriptID(21, 0) stepSound: ((kernel.ScriptID(21, 0) stepSound:) - 1))
	#endif
	(global104
		number:
			match (kernel.ScriptID(21, 0) stepSound:)
				case 1: 301#end:case
				case 2: 302#end:case
				case 3: 303#end:case
				case 4: 304#end:case
			#end:match
		setLoop: 1
		play:
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
		(super newRoom: param1 &rest)
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

		(super init:)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global69 enable: 6)
		(super dispose:)
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
			(rockList = (Set new:) add:)
		#endif
		(super init: &rest)
	#end:method

	@classmethod
	def constantRocks():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(rCliffs cheatCount: 0)
		temp0 = 0
		while (temp0 < 7): # inline for
			(local200[temp0] = (RockStep new:)
				x:
					if argc:
						(320 - local246[temp0])
					else:
						local246[temp0]
					#endif
				y: local262[temp0]
				cel: 3
				rockPointer: temp0
				corner: (1 if (temp0 == 6) else 0)
				init:
				stopUpd:
			)
			(rockList add: local200[temp0])
			if (temp0 < 6):
				(local200[temp0] addToPic:)
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
			(self rockCount: 0 maxRocks: 9)
		else:
			(self rockCount: 7 maxRocks: 16)
		#endif
		(self makeARock:)
	#end:method

	@classmethod
	def makeARock():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (rockCount == maxRocks):
			if (global11 == 300):
				(global91 say: 8 5 18 2 0 21)
			#endif
			((global2 script:) cue:)
		else:
			kernel.ShakeScreen(1, kernel.Random(0, 2))
			(global104 number: 300 setLoop: 1 play:)
			if (rockCount > 0):
				(local200[(rockCount - 1)] stopUpd:)
			#endif
			(local200[rockCount] = (RockStep new:)
				x:
					(cond
						case (global11 == 300): local278[rockCount]#end:case
						case flipRocks:
							(320 - local246[rockCount])
						#end:case
						else: local246[rockCount]#end:else
					)
				y:
					if (global11 == 300):
						local287[rockCount]
					else:
						local262[rockCount]
					#endif
				cel:
					if 
						(or
							(global12 == 130)
							(global12 == 340)
							(global12 == 370)
						)
						2
					else:
						0
					#endif
				rockPointer: rockCount
				corner:
					(cond
						case ((rockCount == 3) and (global11 == 300)): 1#end:case
						case 
							(and
								((rockCount == 6) or (rockCount == 11))
								(global11 == 320)
							):
							1
						#end:case
						else: 0#end:else
					)
				capStone:
					if 
						(or
							((rockCount == 14) and (global11 == 320))
							((rockCount == 7) and (global11 == 300))
						)
						1
					else:
						0
					#endif
				init:
				setCycle: End RockStep
			)
			(rockList add: local200[rockCount])
			(self rockCount: ((self rockCount:) + 1))
		#endif
	#end:method

	@classmethod
	def allRocksOut(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(rCliffs cheatCount: 0)
		if (global11 == 300):
			temp1 = 9
			temp2 = 0
		else:
			temp1 = 16
			temp2 = 0
		#endif
		temp0 = temp2
		while (temp0 < temp1): # inline for
			(local200[temp0] = (RockStep new:)
				x:
					(cond
						case (global11 == 300): local278[temp0]#end:case
						case param1:
							(320 - local246[temp0])
						#end:case
						else: local246[temp0]#end:else
					)
				y: (local287[temp0] if (global11 == 300) else local262[temp0])
				cel: 3
				rockPointer: temp0
				corner:
					(cond
						case (global11 == 300):
							(1 if (temp0 == 3) else 0)
						#end:case
						case ((temp0 == 6) or (temp0 == 11)): 1#end:case
						else: 0#end:else
					)
				capStone:
					(cond
						case (global11 == 300):
							(1 if (temp0 == 7) else 0)
						#end:case
						case (temp0 == 14): 1#end:case
						else: 0#end:else
					)
				init:
				stopUpd:
			)
			(rockList add: local200[temp0])
			if (temp0 < 6):
				(local200[temp0] addToPic:)
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
			(rockList release:)
		#endif
		temp0 = 0
		while (temp0 < 16): # inline for
			if (global5 contains: local200[temp0]):
				(local200[temp0] dispose: delete:)
				local200[temp0] = 0
			#endif
			# for:reinit
			temp0.post('++')
		#end:loop
		temp0 = 0
		while (temp0 < 16): # inline for
			if (global10 contains: local200[temp0]):
				(local200[temp0] dispose: delete:)
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

		(global74 delete: global2)
		if rockList:
			(rockList release: dispose:)
			rockList = 0
		#endif
		(super newRoom: &rest)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				(User controls:)
				((param1 type:) & 0x0040)
				((param1 message:) != 0)
				((global69 curIcon:) == (global69 at: 0))
				kernel.IsObject(rockList)
			)
			if (not temp0 = (rockList firstTrue: #onMe (User curEvent:))):
				temp0 = (rockList firstTrue: #onMe global0)
			#endif
			temp1 = (rockList indexOf: temp0)
			match (param1 message:)
				case 1:
					if ((rockList size:) != (temp1 - 1)):
						temp0 = (rockList at: (temp1 + 1))
					#endif
				#end:case
				case 5:
					if (temp1 != 0):
						temp0 = (rockList at: (temp1 - 1))
					#endif
				#end:case
				else: 0#end:else
			#end:match
			if kernel.IsObject(temp0):
				kernel.SetCursor(((temp0 x:) + 8), (temp0 y:))
			#endif
			(param1 claimed: 1)
			return
		else:
			(super handleEvent: param1)
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
				(global91 say: 6 1 0 1 0 21)
			#end:case
			case 5:
				(global91 say: 6 5 0 1 0 21)
			#end:case
			case 2:
				(global91 say: 6 2 0 1 0 21)
			#end:case
			else:
				(global91 say: 6 0 0 1 0 21)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		(global72 addToFront: self)
		(global73 addToFront: self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global72 delete: self)
		(global73 delete: self)
		(super dispose:)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global2 makeARock:)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if local325:
			(cond
				case (global0 script:):#end:case
				case (local326 > 0):
					local326.post('--')
				#end:case
				else:
					(global0 setScript: egoWobbles)
				#end:else
			)
		#endif
		(super doit:)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				(User canInput:)
				((param1 type:) != 16384)
				(not (param1 modifiers:))
				((global69 curIcon:) == (global69 at: 0))
			)
			if 
				(and
					(((param1 message:) == 13) or ((param1 type:) == 1))
					(self onMe: param1)
				)
				(param1 claimed: 1)
				local325 = 0
				(cond
					case ((global0 script:) == egoWobbles):
						proc913_1(59)
						(global91 say: 6 3 17 1 0 21)
					#end:case
					case 
						(and
							(or
								((global0 view:) == 900)
								((global0 view:) == 308)
								((global0 view:) == 3081)
							)
							((self rockPointer:) == 0)
						):
						(global0 setScript: takeFirstStep 0 local200[0])
					#end:case
					case 
						(and
							(((self y:) - (global0 y:)) < 15)
							(((self y:) - (global0 y:)) > 2)
						):
						(global0
							setScript: stepDown 0 local200[(self rockPointer:)]
						)
					#end:case
					case 
						(or
							(kernel.Abs(((global0 y:) - (self y:))) > 20)
							(kernel.Abs(((global0 x:) - (self x:))) > 64)
						):
						(global91 say: 6 3 16 1 0 21)
					#end:case
					case 
						(or
							(and
								(((self x:) - (global0 x:)) < 40)
								(((self x:) - (global0 x:)) > 35)
								((self y:) < (global0 y:))
							)
							(and
								(((global0 x:) - (self x:)) < 57)
								(((global0 x:) - (self x:)) > 54)
								((self y:) < (global0 y:))
							)
						):
						(global0
							setScript: takeStep 0 local200[(self rockPointer:)]
						)
					#end:case
					case 
						(and
							((self x:) > (global0 x:))
							((global0 y:) < 99)
							(global11 == 300)
							((self y:) < (global0 y:))
						):
						(global0
							setScript: takeStep 0 local200[(self rockPointer:)]
						)
					#end:case
					case 
						(and
							((self x:) > (global0 x:))
							((self y:) < (global0 y:))
						):
						(global0
							setScript: takeStep 0 local200[(self rockPointer:)]
						)
					#end:case
					case 
						(and
							((self x:) < (global0 x:))
							((self y:) < (global0 y:))
						):
						(global0
							setScript: takeStep 0 local200[(self rockPointer:)]
						)
					#end:case
				)
			else:
				(super handleEvent: param1)
			#endif
		else:
			(super handleEvent: param1)
		#endif
		(param1 claimed:)
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
					(global104 number: 308 setLoop: 1 play:)
					(local218[temp0] = (letter new:)
						view: buttView
						setLoop: proc999_6(buttLoop, temp0)
						cel: proc999_6(buttCel, temp0)
						x: (proc999_6(buttX, temp0) + temp1)
						y: proc999_6(buttY, temp0)
						hyroVal: proc999_6(buttVal, temp0)
						deathButt: proc999_6(buttKill, temp0)
						setPri: 14
						init:
						stopUpd:
					)
					local327 = 1
					if (local218[temp0] deathButt:):
						local328 = 1
						(rCliffs cue:)
						(global2 setScript: seeYa 0 self)
					else:
						(self cue: (local218[temp0] hyroVal:))
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

		(global2 setScript: puzzleSolvedPause 0 self)
	#end:method

	@classmethod
	def cue(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self buttonCount: ((self buttonCount:) + 1))
		(cond
			case ((param1 == correctButton) or (param1 == -1)):
				(self correctButton: ((self correctButton:) + 1))
				if (correctButton == (maxButtons + 1)):
					correctButton = (buttonCount = 0 + 1)
					(global2 setScript: notifyTheRoom 0 self)
				#endif
			#end:case
			case (buttonCount == buttNumber):
				(global2 setScript: clearTheButtons 0 self)
			#end:case
			case (param1 != correctButton):
				(self correctButton: ((self correctButton:) + 10))
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
				(local218[temp0] dispose:)
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

		(global69 disable: 3 0 4 5 6)
		temp0 = 0
		while (temp0 < 28): # inline for
			local218[temp0] = 0
			# for:reinit
			temp0.post('++')
		#end:loop
		(rCliffs puzzleIsUp: 1)
		(self setPri: 12 signal: 4112 ignoreActors: stopUpd:)
		(super init: &rest)
		(global72 addToFront: self)
		(global73 addToFront: self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(rCliffs puzzleIsUp: 0)
		(self dumpButtons:)
		correctButton = (local324 = buttonCount = 0 + 1)
		(global72 delete: self)
		(global73 delete: self)
		if (not local328):
			(global1 handsOn:)
		#endif
		(global69 enable: 6)
		(super dispose:)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				(User canInput:)
				((param1 type:) != 16384)
				(or
					(((param1 message:) == 13) and ((param1 type:) & 0x0004))
					((param1 type:) == 1)
				)
				(not (param1 modifiers:))
			)
			(cond
				case solvedPuzz:
					(param1 claimed: 1)
					(self solvedPuzz: 0)
					(self dispose:)
				#end:case
				case 
					(and
						(self onMe: param1)
						((global69 curIcon:) == (global69 at: 2))
					):
					(param1 claimed: 1)
					(global91 say: lookMsg 1 0 1 0 21)
				#end:case
				case 
					(and
						(or
							((param1 type:) & 0x0001)
							(and
								((param1 type:) & 0x0004)
								((param1 message:) == 13)
							)
						)
						(self doButton: (param1 x:) (param1 y:))
					):
					(param1 claimed: 1)
				#end:case
				case ((param1 type:) & 0x0001):
					(param1 claimed: 1)
					(global2 setScript: clearTheButtons 0 self)
				#end:case
				case (((param1 type:) & 0x0001) and (param1 modifiers:)):
					(param1 claimed: 0)
				#end:case
				case ((param1 type:) & 0x0004):
					(cond
						case ((param1 message:) == 13):
							(param1 claimed: 1)
							(global91 say: 8 5 7 1 0 21)
							(self dispose:)
						#end:case
						case 27:
							(param1 claimed: 1)
							(global91 say: 8 5 7 1 0 21)
							(self dispose:)
						#end:case
						else:
							(param1 claimed: 0)
						#end:else
					)
				#end:case
				else:
					(param1 claimed: 0)
				#end:else
			)
		else:
			(param1 claimed: 0)
		#endif
		(param1 claimed:)
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
				(global1 handsOff:)
				(rCliffs cheatCount: ((rCliffs cheatCount:) - 1))
				(cond
					case (local200[((register rockPointer:) + 1)] corner:):
						if ((global0 loop:) < 6):
							(rCliffs stepDirection: 1)
						else:
							(rCliffs stepDirection: 2)
						#endif
						ticks = 4
					#end:case
					case ((rCliffs stepDirection:) == 4):
						(global0
							view: 3011
							setLoop: 1
							cel: 0
							x: ((global0 x:) + 18)
							y: ((global0 y:) + 11)
						)
						(rCliffs stepDirection: 1)
						cycles = 6
					#end:case
					case ((rCliffs stepDirection:) == 3):
						(global0
							view: 3011
							setLoop: 1
							cel: 0
							x: ((global0 x:) - 18)
							y: ((global0 y:) + 11)
						)
						(rCliffs stepDirection: 2)
						cycles = 6
					#end:case
					else:
						(self cue:)
					#end:else
				)
			#end:case
			case 1:
				if ((rCliffs stepSound:) == 1):
					(rCliffs stepSound: 4)
				else:
					(rCliffs stepSound: ((rCliffs stepSound:) - 1))
				#endif
				(global104
					number:
						match (rCliffs stepSound:)
							case 1: 301#end:case
							case 2: 302#end:case
							case 3: 303#end:case
							case 4: 304#end:case
						#end:match
					setLoop: 1
					play:
				)
				if ((rCliffs stepDirection:) == 2):
					(global0
						view: 301
						setLoop: 7
						cel: 0
						cycleSpeed: 16
						posn: ((register x:) + 24) ((register y:) - 13)
					)
				else:
					(global0
						view: 301
						setLoop: 8
						cel: 0
						posn: ((register x:) - 6) ((register y:) - 13)
						cycleSpeed: 16
					)
				#endif
				cycles = 6
			#end:case
			case 2:
				(global0 cel: 1)
				if ((rCliffs stepDirection:) == 2):
					(global0 posn: ((register x:) + 19) ((register y:) - 11))
				else:
					(global0 posn: ((register x:) - 3) ((register y:) - 11))
				#endif
				cycles = 5
			#end:case
			case 3:
				(global0 cel: 2)
				if ((rCliffs stepDirection:) == 2):
					(global0 posn: ((register x:) + 23) ((register y:) - 8))
				else:
					(global0 posn: ((register x:) - 5) ((register y:) - 11))
				#endif
				cycles = 5
			#end:case
			case 4:
				(global0 cel: 3)
				if ((rCliffs stepDirection:) == 2):
					(global0 posn: ((register x:) + 18) ((register y:) - 14))
				else:
					(global0 posn: ((register x:) - 5) ((register y:) - 14))
				#endif
				cycles = 5
			#end:case
			case 5:
				(global0 cel: 4)
				if ((rCliffs stepDirection:) == 2):
					(global0 posn: ((register x:) + 19) ((register y:) - 14))
				else:
					(global0 posn: ((register x:) - 6) ((register y:) - 14))
				#endif
				cycles = 5
			#end:case
			case 6:
				(global0 cel: 5)
				if ((rCliffs stepDirection:) == 2):
					(global0 posn: ((register x:) + 19) ((register y:) - 14))
				else:
					(global0 posn: ((register x:) - 6) ((register y:) - 14))
				#endif
				cycles = 5
			#end:case
			case 7:
				(global0 cel: 6)
				if ((rCliffs stepDirection:) == 2):
					(global0 posn: ((register x:) + 19) ((register y:) - 14))
				else:
					(global0 posn: ((register x:) - 4) ((register y:) - 14))
				#endif
				cycles = 5
			#end:case
			case 8:
				(cond
					case 
						(and
							((register corner:) == 1)
							((rCliffs stepDirection:) == 2)
						):
						(global0
							setLoop: 5
							cel: 0
							cycleSpeed: 7
							posn: ((register x:) + 9) ((global0 y:) + 18)
							setCycle: End self
						)
						(rCliffs stepDirection: 3)
					#end:case
					case ((register corner:) == 1):
						(global0
							setLoop: 4
							cel: 0
							cycleSpeed: 7
							posn: ((register x:) + 8) ((global0 y:) + 18)
							setCycle: End self
						)
						(rCliffs stepDirection: 4)
					#end:case
					else:
						(self cue:)
					#end:else
				)
			#end:case
			case 9:
				(cond
					case ((register corner:) and ((global0 loop:) == 5)):
						(global0
							posn: ((register x:) + 27) ((register y:) - 2)
							setLoop: kernel.Random(1, 2)
							cel: 0
						)
					#end:case
					case ((register corner:) and ((global0 loop:) == 4)):
						(global0
							posn: ((register x:) - 9) ((register y:) - 1)
							setLoop: 6
							cel: 0
						)
					#end:case
					case ((rCliffs stepDirection:) == 1):
						(global0
							view: 301
							setLoop: kernel.Random(1, 2)
							cel: 0
							posn: ((register x:) + 26) ((register y:) - 1)
						)
					#end:case
					else:
						(global0
							view: 301
							setLoop: 6
							cel: 0
							posn: ((register x:) - 8) ((register y:) - 1)
						)
					#end:else
				)
				cycles = 6
			#end:case
			case 10:
				(global1 handsOn:)
				if ((register corner:) != 1):
					local325 = 1
					local326 = kernel.Random(1000, 2000)
				#endif
				if ((register rockPointer:) == 0):
					if ((kernel.ScriptID(21, 0) cliffFace:) == 0):
						(global2 cue: -1)
					else:
						(global2 cue: 0)
					#endif
				#endif
				(self dispose:)
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
				(global1 handsOff:)
				(global0 actions: egoStepVerb setMotion: MoveTo 110 112 self)
			#end:case
			case 1:
				(rCliffs stepSound: 1)
				(global104 number: 301 setLoop: 1 play:)
				(global0 view: 301 normal: 0 setLoop: 0 cel: 0)
				ticks = 6
			#end:case
			case 2:
				(global0 cel: 1)
				ticks = 6
			#end:case
			case 3:
				(global0
					cel: 2
					posn: ((register x:) + 7) ((register y:) + 9)
					cycleSpeed: 10
					setCycle: End self
				)
			#end:case
			case 4:
				(global1 handsOn:)
				(global0
					posn: ((register x:) + 26) ((register y:) - 2)
					setLoop: 2
					cel: 0
				)
				local325 = 1
				(rCliffs stepDirection: 3)
				local326 = kernel.Random(1000, 2000)
				(global74 add: global2)
				(self dispose:)
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
				(global1 handsOff:)
				(rCliffs cheatCount: ((rCliffs cheatCount:) + 1))
				(cond
					case ((rCliffs stepDirection:) == 2):
						(global0
							view: 3011
							setLoop: 1
							cel: 0
							posn: ((register x:) - 19) ((register y:) + 21)
						)
						(rCliffs stepDirection: 3)
						cycles = 2
					#end:case
					case ((rCliffs stepDirection:) == 1):
						(global0
							view: 3011
							setLoop: 1
							cel: 0
							posn: ((register x:) + 37) ((register y:) + 19)
						)
						(rCliffs stepDirection: 4)
						cycles = 2
					#end:case
					else:
						(self cue:)
					#end:else
				)
			#end:case
			case 1:
				if ((rCliffs stepSound:) == 4):
					(rCliffs stepSound: 1)
				else:
					(rCliffs stepSound: ((rCliffs stepSound:) + 1))
				#endif
				(global104
					number:
						match (rCliffs stepSound:)
							case 1: 301#end:case
							case 2: 302#end:case
							case 3: 303#end:case
							case 4: 304#end:case
						#end:match
					setLoop: 1
					play:
				)
				if ((rCliffs stepDirection:) == 3):
					(global0
						view: 301
						cycleSpeed: 10
						setLoop: kernel.Random(1, 2)
						cel: 0
						posn: ((register x:) - 2) ((register y:) + 10)
						setCycle: End self
					)
				else:
					(global0
						view: 301
						setLoop: 6
						cycleSpeed: 10
						posn: ((register x:) + 20) ((register y:) + 11)
						setCycle: End self
					)
				#endif
			#end:case
			case 2:
				if ((rCliffs stepDirection:) == 3):
					(global0
						posn: ((register x:) + 27) ((register y:) - 2)
						cel: 0
					)
				else:
					(global0
						posn: ((register x:) - 9) ((register y:) - 1)
						cel: 0
					)
				#endif
				ticks = 6
			#end:case
			case 3:
				(cond
					case 
						(and
							((register corner:) == 1)
							((rCliffs stepDirection:) == 3)
						):
						(global0
							setLoop: 4
							cycleSpeed: 12
							posn: ((register x:) + 7) ((global0 y:) + 7)
							setCycle: End self
						)
					#end:case
					case ((register corner:) == 1):
						(global0
							setLoop: 5
							cycleSpeed: 12
							posn: ((register x:) + 10) ((global0 y:) + 5)
							setCycle: End self
						)
					#end:case
					else:
						(self cue:)
					#end:else
				)
			#end:case
			case 4:
				(cond
					case 
						((register corner:) and ((rCliffs stepDirection:) == 3)):
						(global0
							posn: ((register x:) - 9) ((register y:) - 1)
							setLoop: 6
							cel: 0
						)
						(rCliffs stepDirection: 4)
					#end:case
					case (register corner:):
						(global0
							posn: ((register x:) + 27) ((register y:) - 2)
							setLoop: kernel.Random(1, 2)
							cel: 0
						)
						(rCliffs stepDirection: 3)
					#end:case
				)
				ticks = 6
			#end:case
			case 5:
				(global1 handsOn:)
				if ((register corner:) != 1):
					local325 = 1
					local326 = kernel.Random(1000, 2000)
				#endif
				if ((register capStone:) == 1):
					if ((rCliffs stepDirection:) == 4):
						(rCliffs stepDirection: 3)
					else:
						(rCliffs stepDirection: 4)
					#endif
					(global0 setScript: nextScreenUp 0 register)
				#endif
				(self dispose:)
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
				(global1 handsOff:)
				if ((rCliffs stepSound:) == 4):
					(rCliffs stepSound: 1)
				else:
					(rCliffs stepSound: ((rCliffs stepSound:) + 1))
				#endif
				(global104
					number:
						match (rCliffs stepSound:)
							case 1: 301#end:case
							case 2: 302#end:case
							case 3: 303#end:case
							case 4: 304#end:case
						#end:match
					setLoop: 1
					play:
				)
				if ((rCliffs stepDirection:) == 4):
					(global0
						cycleSpeed: 10
						setLoop: kernel.Random(1, 2)
						setCycle: End self
					)
				else:
					(global0 setLoop: 6 cycleSpeed: 10 setCycle: End self)
				#endif
			#end:case
			case 1:
				if ((rCliffs stepDirection:) == 4):
					(global0
						posn: ((register x:) + 56) ((register y:) - 14)
						cel: 0
					)
				else:
					(global0
						posn: ((register x:) - 38) ((register y:) - 13)
						cel: 0
					)
				#endif
				ticks = 6
			#end:case
			case 2:
				(global1 handsOn:)
				(global0 hide:)
				if (global11 == 320):
					(global2 cue: 1)
					(self dispose:)
				else:
					(global2 newRoom: (global2 north:))
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
				(global1 givePoints: 1)
				(register dispose:)
				cycles = 1
			#end:case
			case 1:
				match (rCliffs cliffFace:)
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
					(global91 say: 4 5 6 1 self 21)
				else:
					(global91 say: 8 5 18 1 self 21)
				#endif
			#end:case
			case 2:
				(global2 notify:)
				(self dispose:)
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
				(global104 number: 305 setLoop: 1 play:)
				if ((global0 loop:) == 6):
					(global0
						view: 3011
						posn: ((global0 x:) + 18) ((global0 y:) + 10)
						cycleSpeed: 12
						setLoop: 1
					)
				else:
					(global0
						view: 301
						posn: ((global0 x:) - 18) ((global0 y:) + 7)
						cycleSpeed: kernel.Random(4, 16)
						setLoop: 3
					)
				#endif
				(global0 cel: 0 setCycle: End self)
			#end:case
			case 1:
				if ((global0 view:) == 301):
					(global0 setCycle: Beg self)
				else:
					(self cue:)
				#endif
			#end:case
			case 2:
				if ((global0 view:) == 301):
					(global0
						posn: ((global0 x:) + 18) ((global0 y:) - 7)
						setLoop: kernel.Random(1, 2)
					)
				else:
					(global0
						posn: ((global0 x:) - 18) ((global0 y:) - 10)
						setLoop: 6
					)
				#endif
				(global0 view: 301 cycleSpeed: 18 cel: 0)
				local326 = kernel.Random(1000, 2000)
				proc913_2(59)
				(self dispose:)
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
				(global1 handsOff:)
				(global69 disable: 6)
				(register dispose:)
				ticks = 4
			#end:case
			case 1:
				(global91 say: 3 5 3 1 self 21)
			#end:case
			case 2:
				(local200[6] setCycle: Beg self)
				(global104 number: 300 setLoop: 1 play:)
			#end:case
			case 3:
				(global91 say: 3 5 3 2 self 21)
			#end:case
			case 4:
				(global0
					posn: ((global0 x:) - 10) (global0 y:)
					ignoreActors:
					illegalBits: 0
					view: 4011
					normal: 0
					cycleSpeed: 6
					setLoop: 0
					setCycle: CT 10 1 self
				)
			#end:case
			case 5:
				(global104 number: 306 setLoop: 1 play: self)
				(global0 setCycle: End)
			#end:case
			case 6:
				(global0 y: 280)
				seconds = 2
			#end:case
			case 7:
				(global104 number: 307 setLoop: 1 play:)
				kernel.ShakeScreen(2, 2)
				ticks = 4
			#end:case
			case 8:
				(global91 say: 3 5 3 3 self 21)
			#end:case
			case 9:
				(global105 fade: 0 5 5)
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
				(register dispose:)
				cycles = 4
			#end:case
			case 2:
				if local327:
					(global91 say: 8 5 7 1 self 21)
				else:
					(self cue:)
				#endif
			#end:case
			case 3:
				local327 = 0
				(self dispose:)
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
				(global91 say: 8 5 8 1 self 21)
			#end:case
			case 2:
				if (global11 == 320):
					if ((global0 cel:) == 1):
						(global0 view: 301 setLoop: 6 cel: 0)
					else:
						(global0 view: 301 setLoop: 1)
					#endif
				#endif
				kernel.UnLoad(128, 3012)
				(self dispose:)
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
				(global91 say: 0 0 64 1 0 899)
				return 1
			#end:else
		#end:match
	#end:method

#end:class or instance

