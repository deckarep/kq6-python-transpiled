#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 994
import sci_sh
import Main
import Print
import Polygon
import Sound
import Save
import Motion
import Inventory
import User
import System

@SCI.procedure
def localproc_0(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	temp81 = (Memory 1 150)
	temp0 = 1
	(DeviceInfo 0 global29 @temp1)
	(DeviceInfo 1 @temp41)
	if 
		(and
			(DeviceInfo 3 @temp41)
			(or
				(DeviceInfo 2 @temp1 @temp41)
				(not (DeviceInfo 6 (global1 name:)))
			)
		)
		(Message 0 994 6 0 0 1 @temp82)
		(Message 0 994 7 0 0 1 @temp122)
		(Message 0 994 8 0 0 1 @temp132)
		(Format temp81 @temp82 (@temp122 if param1 else @temp132) @temp1)
		(Load 135 global22)
		(DeviceInfo 4)
		(Message 0 994 2 0 0 1 @temp82)
		(Message 0 994 4 0 0 1 @temp122)
		(Message 0 994 5 0 0 1 @temp132)
		if 
			(==
				(= temp0
					if param1:
						(Print
							font: 0
							addText: temp81
							addButton: 1 @temp82 0 40
							addButton: 0 @temp122 30 40
							addButton: 2 @temp132
							init:
						)
					else:
						(Print
							font: 0
							addText: temp81
							addButton: 1 @temp82 0 40
							init:
						)
					#endif
				)
				2
			)
			temp0 = (proc990_0 global29)
		#endif
	#endif
	(Memory 3 temp81)
	return temp0
#end:procedure

@SCI.instance
class cast(EventHandler):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class features(EventHandler):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class theDoits(EventHandler):
	#property vars (may be empty)
#end:class or instance

class Sounds(EventHandler):
	#property vars (may be empty)
	@classmethod
	def pause(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self eachElementDo: #perform mayPause (param1 if argc else 1))
	#end:method

#end:class or instance

@SCI.instance
class mayPause(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not ((param1 flags:) & 0x0001)):
			(param1 pause: param2)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class regions(EventHandler):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class addToPics(EventHandler):
	#property vars (may be empty)
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self eachElementDo: #perform aTOC)
		(AddToPic elements)
	#end:method

#end:class or instance

@SCI.instance
class timers(Set):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class mouseDownHandler(EventHandler):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class keyDownHandler(EventHandler):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class directionHandler(EventHandler):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class walkHandler(EventHandler):
	#property vars (may be empty)
#end:class or instance

class Cue(Obj):
	#property vars (may be empty)
	cuee = 0
	cuer = 0
	register = 0
	
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global18 delete: self)
		if (global18 isEmpty:):
			(global18 dispose:)
			global18 = 0
		#endif
		(cuee cue: register cuer)
		(self dispose:)
	#end:method

#end:class or instance

@SCI.instance
class aTOC(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not ((param1 signal:) & 0x4000)):
			temp0 = ((global0 xStep:) + ((CelWide (global0 view:) 2 0) / 2))
			temp1 = ((global0 yStep:) * 2)
			(global2
				addObstacle:
					((Polygon new:)
						init:
							((param1 brLeft:) - temp0)
							((CoordPri 1 (CoordPri (param1 y:))) - temp1)
							((param1 brRight:) + temp0)
							((CoordPri 1 (CoordPri (param1 y:))) - temp1)
							((param1 brRight:) + temp0)
							((param1 y:) + temp1)
							((param1 brLeft:) - temp0)
							((param1 y:) + temp1)
						yourself:
					)
			)
		#endif
	#end:method

#end:class or instance

class Game(Obj):
	#property vars (may be empty)
	script = 0
	printLang = 1
	_detailLevel = 3
	panelObj = 0
	panelSelector = 0
	handsOffCode = 0
	handsOnCode = 0
	
	@classmethod
	def play():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		global1 = self
		global29 = (GetSaveDir)
		(self setCursor: global21 1 init:)
		(self setCursor: global20 1)
		while (not global4):

			(self doit:)
		#end:loop
	#end:method

	@classmethod
	def quitGame(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((not argc) or param1):
			global4 = 1
		#endif
	#end:method

	@classmethod
	def masterVolume(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if argc:
			(DoSound 0 param1)
		else:
			(DoSound 0)
		#endif
	#end:method

	@classmethod
	def detailLevel(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if argc:
			_detailLevel = param1
			(global5 eachElementDo: #checkDetail)
		#endif
		return _detailLevel
	#end:method

	@classmethod
	def replay():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if global24:
			(global24 dispose:)
		#endif
		if global25:
			(global25 dispose:)
		#endif
		(global5 eachElementDo: #perform RU)
		(global1 setCursor: global21 1)
		(= temp0
			if (not (proc999_5 (global2 style:) -1 11 12 13 14)):
				(global2 style:)
			else:
				100
			#endif
		)
		(DrawPic (global2 curPic:) temp0 1)
		if (global36 != -1):
			(DrawPic global36 100 0)
		#endif
		(global10 doit:)
		(cond
			case ((not (global80 canControl:)) and (not (global80 canInput:))):
				(global1 setCursor: global21)
			#end:case
			case (global69 and (global69 curIcon:)):
				(global1 setCursor: ((global69 curIcon:) cursor:))
			#end:case
			else:
				(global1 setCursor: global20)
			#end:else
		)
		(SL doit:)
		(DoSound 2)
		(global8 pause: 0)
		global86 = (global88 - (GetTime))
		while (not global4):

			(self doit:)
		#end:loop
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		Motion
		Sound
		(global5 = cast add:)
		(global32 = features add:)
		(global8 = Sounds add:)
		(global6 = regions add:)
		(global10 = addToPics add:)
		(global7 = timers add:)
		(global78 = theDoits add:)
		(global73 = mouseDownHandler add:)
		(global72 = keyDownHandler add:)
		(global74 = directionHandler add:)
		(global93 = walkHandler add:)
		global84 = 0
		global29 = (GetSaveDir)
		(Inv init:)
		if (not global80):
			global80 = User
		#endif
		(global80 init:)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if panelObj:
			temp1 = panelObj
			temp2 = panelSelector
			panelObj = panelSelector = 0
			(proc999_7 temp1 temp2)
		#endif
		global88 = (global86 + (GetTime))
		if global84:
			while global84:

				(global84 eachElementDo: #doit)
				if ((temp0 = (Event new:) type:) and global84):
					(global84 firstTrue: #handleEvent temp0)
				#endif
				(temp0 dispose:)
				global88 = (global86 + (GetTime))
				(global8 eachElementDo: #check)
			#end:loop
		#endif
		if global92:
			(global92 eachElementDo: #doit)
			if (not global25):
				if ((temp0 = (Event new:) type:) and global92):
					(global92 firstTrue: #handleEvent temp0)
				#endif
				(temp0 dispose:)
				global88 = (global86 + (GetTime))
				return
			#endif
		#endif
		(global8 eachElementDo: #check)
		(global7 eachElementDo: #doit)
		if (global25 and (global25 check:)):
			(global25 dispose:)
		#endif
		(Animate (global5 elements:) 1)
		if global37:
			global37 = 0
			(global5 eachElementDo: #motionCue)
		#endif
		if global18:
			(global18 eachElementDo: #doit)
		#endif
		if script:
			(script doit:)
		#endif
		(global6 eachElementDo: #doit)
		if global84:
			return
		#endif
		if (global13 == global11):
			(global80 doit:)
		#endif
		(global78 doit:)
		if (global13 != global11):
			(self newRoom: global13)
		#endif
		(global7 eachElementDo: #delete)
		(GameIsRestarting 0)
	#end:method

	@classmethod
	def newRoom(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global10 eachElementDo: #dispose eachElementDo: #delete release:)
		(global32 eachElementDo: #perform fDC release:)
		(global5 eachElementDo: #dispose eachElementDo: #delete)
		(global7 eachElementDo: #delete)
		(global6 eachElementDo: #perform DNKR release:)
		(global78 release:)
		(Animate 0)
		global12 = global11
		global11 = param1
		global13 = param1
		(FlushResources param1)
		(self startRoom: global11)
		while (temp5 = (Event new: 3) type:):

			(temp5 dispose:)
		#end:loop
		(temp5 dispose:)
	#end:method

	@classmethod
	def startRoom(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if global14:
			(SetDebug)
		#endif
		(global6 addToFront: global2 = (ScriptID param1))
		(global2 init:)
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (param1 claimed:): 1#end:case
			case (script and (script handleEvent: param1)): 1#end:case
			case ((param1 type:) & 0x4000):
				(self pragmaFail:)
			#end:case
		)
		(param1 claimed:)
	#end:method

	@classmethod
	def changeScore(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global15 += param1)
		(SL doit:)
	#end:method

	@classmethod
	def restart():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if global25:
			(global25 dispose:)
		#endif
		(RestartGame)
	#end:method

	@classmethod
	def save():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not (ValidPath global29)):
			(Message 0 994 9 0 0 1 @temp22)
			(Format @temp127 @temp22 global29)
			(Print font: 0 addText: @temp127 init:)
			(proc990_0 global29)
		#endif
		(Load 135 global23)
		(ScriptID 990)
		temp21 = (self setCursor: global20)
		(global8 pause: 1)
		if (localproc_0 1):
			if global25:
				(global25 dispose:)
			#endif
			if (temp20 = (Save doit: @temp0) != -1):
				temp21 = (self setCursor: global21 1)
				if (not (SaveGame name temp20 @temp0 global27)):
					(Message 0 994 1 0 0 1 @temp22)
					(Message 0 994 2 0 0 1 @temp122)
					(Print
						font: 0
						addText: @temp22
						addButton: 1 @temp122 0 40
						init:
					)
				#endif
				(self setCursor: temp21 (HaveMouse))
			#endif
			(localproc_0 0)
		#endif
		(global8 pause: 0)
	#end:method

	@classmethod
	def restore():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not (ValidPath global29)):
			(Message 0 994 9 0 0 1 @temp22)
			(Format @temp127 @temp22 global29)
			(Print font: 0 addText: @temp127 init:)
			(proc990_0 global29)
		#endif
		(Load 135 global23)
		(ScriptID 990)
		temp21 = (self setCursor: global20)
		(global8 pause: 1)
		if (localproc_0 1):
			if global25:
				(global25 dispose:)
			#endif
			if (temp20 = (Restore doit: &rest) != -1):
				(self setCursor: global21 1)
				if (CheckSaveGame name temp20 global27):
					(RestoreGame name temp20 global27)
				else:
					(Message 0 994 3 0 0 1 @temp22)
					(Message 0 994 2 0 0 1 @temp122)
					(Print
						font: 0
						addText: @temp22
						addButton: 1 @temp122 0 40
						init:
					)
					(self setCursor: temp21 (HaveMouse))
				#endif
			#endif
			(localproc_0 0)
		#endif
		(global8 pause: 0)
	#end:method

	@classmethod
	def setCursor(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, param6 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = global19
		if (IsObject param1):
			global19 = param1
			(param1 init:)
		else:
			(SetCursor param1 0 0)
		#endif
		if (argc > 1):
			(SetCursor param2)
			if (argc > 2):
				(SetCursor param3 param4)
				if (argc > 4):
					(SetCursor param1 0 0 param5 param6)
				#endif
			#endif
		#endif
		return temp0
	#end:method

	@classmethod
	def showMem():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(Format
			@temp0
			r"""Free Heap: %u Bytes\nLargest ptr: %u Bytes\nFreeHunk: %u KBytes\nLargest hunk: %u Bytes"""
			(MemoryInfo 1)
			(MemoryInfo 0)
			((MemoryInfo 3) >> 0x0006)
			(MemoryInfo 2)
		)
		(Print addText: @temp0 init:)
	#end:method

	@classmethod
	def pragmaFail():#end:method

	@classmethod
	def notify():#end:method

	@classmethod
	def setScript(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if script:
			(script dispose:)
		#endif
		if param1:
			(param1 init: self &rest)
		#endif
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if script:
			(script cue:)
		#endif
	#end:method

	@classmethod
	def handsOff():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if handsOffCode:
			(handsOffCode doit: &rest)
		else:
			(User canControl: 0 canInput: 0)
			if (IsObject global0):
				(global0 setMotion: 0)
			#endif
		#endif
	#end:method

	@classmethod
	def handsOn():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if handsOnCode:
			(handsOnCode doit: &rest)
		else:
			(User canControl: 1 canInput: 1)
		#endif
	#end:method

#end:class or instance

class Rgn(Obj):
	#property vars (may be empty)
	script = 0
	number = 0
	modNum = -1
	noun = 0
	timer = 0
	keep = 0
	initialized = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not initialized):
			initialized = 1
			if (not (global6 contains: self)):
				(global6 addToEnd: self)
			#endif
			(super init:)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if script:
			(script doit:)
		#endif
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (param1 claimed:): 1#end:case
			case ((param1 type:) & 0x0040): 0#end:case
			case 
				(not
					(and
						script
						((script handleEvent: param1) or 1)
						(param1 claimed:)
					)
				):
				(param1 claimed: (self doVerb: (param1 message:)))
			#end:case
		)
		(param1 claimed:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (modNum == -1):
			modNum = global11
		#endif
		(return
			if (Message 0 modNum noun param1 0 1):
				(global91 say: noun param1 0 0 0 modNum)
				1
			else:
				0
			#endif
		)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global6 delete: self)
		if (IsObject script):
			(script dispose:)
		#endif
		if (IsObject timer):
			(timer dispose: delete:)
		#endif
		(global8 eachElementDo: #clean self)
		(DisposeScript number)
	#end:method

	@classmethod
	def setScript(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (IsObject script):
			(script dispose:)
		#endif
		if param1:
			(param1 init: self &rest)
		#endif
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if script:
			(script cue:)
		#endif
	#end:method

	@classmethod
	def newRoom():#end:method

	@classmethod
	def notify():#end:method

#end:class or instance

class Rm(Rgn):
	#property vars (may be empty)
	picture = 0
	style = -1
	horizon = 0
	controls = 0
	north = 0
	east = 0
	south = 0
	west = 0
	curPic = 0
	picAngle = 0
	vanishingX = 160
	vanishingY = 0
	obstacles = 0
	inset = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		number = global11
		global31 = picAngle
		if picture:
			(self drawPic: picture)
		#endif
		(self reflectPosn: (global80 alterEgo:) ((global80 alterEgo:) edgeHit:))
		((global80 alterEgo:) edgeHit: 0)
	#end:method

	@classmethod
	def reflectPosn(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param2
			case 1:
				(param1 y: 188)
			#end:case
			case 4:
				(param1 x: (319 - (param1 xStep:)))
			#end:case
			case 3:
				(param1 y: (horizon + (param1 yStep:)))
			#end:case
			case 2:
				(param1 x: 1)
			#end:case
		#end:match
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if script:
			(script doit:)
		#endif
		if temp0 = (self edgeToRoom: ((global80 alterEgo:) edgeHit:)):
			(self newRoom: temp0)
		#endif
	#end:method

	@classmethod
	def edgeToRoom(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			match param1
				case 1: north#end:case
				case 2: east#end:case
				case 3: south#end:case
				case 4: west#end:case
			#end:match
		)
	#end:method

	@classmethod
	def roomToEdge(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			match param1
				case north: 1#end:case
				case south: 3#end:case
				case east: 2#end:case
				case west: 4#end:case
			#end:match
		)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if obstacles:
			(obstacles dispose:)
		#endif
		(super dispose:)
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		((inset and (inset handleEvent: param1)) or (super handleEvent: param1))
		(param1 claimed:)
	#end:method

	@classmethod
	def setInset(param1 = None, param2 = None, param3 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if inset:
			(inset dispose:)
		#endif
		if (argc and param1):
			(param1
				init:
					(param2 if (argc >= 2) else 0)
					self
					(param3 if (argc >= 3) else 0)
			)
		#endif
	#end:method

	@classmethod
	def setRegions(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 0
		while (temp0 < argc): # inline for
			temp1 = param1[temp0]
			temp2 = (ScriptID temp1)
			(temp2 number: temp1)
			(global6 add: temp2)
			if (not (temp2 initialized:)):
				(temp2 init:)
			#endif
			# for:reinit
			temp0++
		#end:loop
	#end:method

	@classmethod
	def addObstacle(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not (IsObject obstacles)):
			obstacles = (List new:)
		#endif
		(obstacles add: param1 &rest)
	#end:method

	@classmethod
	def newRoom(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global6 delete: self eachElementDo: #newRoom param1 addToFront: self)
		global13 = param1
		(super newRoom: param1)
	#end:method

	@classmethod
	def drawPic(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if global10:
			(global10 eachElementDo: #dispose release:)
		#endif
		curPic = param1
		global36 = -1
		(DrawPic
			param1
			(cond
				case (argc == 2): param2#end:case
				case (style != -1): style#end:case
				else: 100#end:else
			)
			1
		)
	#end:method

	@classmethod
	def overlay(param1 = None, param2 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		global36 = param1
		(DrawPic
			param1
			(cond
				case (argc == 2): param2#end:case
				case (style != -1): style#end:case
				else: 100#end:else
			)
			0
		)
	#end:method

#end:class or instance

class SL(Obj):
	#property vars (may be empty)
	state = 0
	code = 0
	
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if code:
			temp0 = (Memory 1 150)
			(code doit: temp0)
			(DrawStatus (temp0 if state else 0))
			(Memory 3 temp0)
		#endif
	#end:method

	@classmethod
	def enable():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		state = 1
		(self doit:)
	#end:method

	@classmethod
	def disable():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		state = 0
		(self doit:)
	#end:method

#end:class or instance

@SCI.instance
class RU(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 underBits:):
			temp0 = (temp0 = (| temp0 = (param1 signal:) 0x0001) & 0xfffb)
			(param1 underBits: 0 signal: temp0)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class DNKR(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not (param1 keep:)):
			(param1 dispose:)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class fDC(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 respondsTo: #delete):
			(param1 signal: ((param1 signal:) & 0xffdf) dispose: delete:)
		else:
			(param1 dispose:)
		#endif
	#end:method

#end:class or instance

