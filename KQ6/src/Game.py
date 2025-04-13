#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 994
import sci_sh
import kernel
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
def localproc_0(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	temp81 = kernel.Memory(1, 150)
	temp0 = 1
	kernel.DeviceInfo(0, global29, @temp1)
	kernel.DeviceInfo(1, @temp41)
	if 
		(and
			kernel.DeviceInfo(3, @temp41)
			(or
				kernel.DeviceInfo(2, @temp1, @temp41)
				(not kernel.DeviceInfo(6, global1._send('name:')))
			)
		)
		kernel.Message(0, 994, 6, 0, 0, 1, @temp82)
		kernel.Message(0, 994, 7, 0, 0, 1, @temp122)
		kernel.Message(0, 994, 8, 0, 0, 1, @temp132)
		kernel.Format(temp81, @temp82, (@temp122 if param1 else @temp132), @temp1)
		kernel.Load(135, global22)
		kernel.DeviceInfo(4)
		kernel.Message(0, 994, 2, 0, 0, 1, @temp82)
		kernel.Message(0, 994, 4, 0, 0, 1, @temp122)
		kernel.Message(0, 994, 5, 0, 0, 1, @temp132)
		if 
			(==
				(= temp0
					if param1:
						Print._send(
							'font:', 0,
							'addText:', temp81,
							'addButton:', 1, @temp82, 0, 40,
							'addButton:', 0, @temp122, 30, 40,
							'addButton:', 2, @temp132,
							'init:'
						)
					else:
						Print._send(
							'font:', 0,
							'addText:', temp81,
							'addButton:', 1, @temp82, 0, 40,
							'init:'
						)
					#endif
				)
				2
			)
			temp0 = proc990_0(global29)
		#endif
	#endif
	kernel.Memory(3, temp81)
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
	def pause(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('eachElementDo:', #perform, mayPause, (param1 if argc else 1))
	#end:method

#end:class or instance

@SCI.instance
class mayPause(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not (param1._send('flags:') & 0x0001)):
			param1._send('pause:', param2)
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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('eachElementDo:', #perform, aTOC)
		kernel.AddToPic(elements)
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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global18._send('delete:', self)
		if global18._send('isEmpty:'):
			global18._send('dispose:')
			global18 = 0
		#endif
		cuee._send('cue:', register, cuer)
		self._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class aTOC(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not (param1._send('signal:') & 0x4000)):
			temp0 = (global0._send('xStep:') + (kernel.CelWide(global0._send('view:'), 2, 0) / 2))
			temp1 = (global0._send('yStep:') * 2)
			global2._send(
				'addObstacle:', Polygon._send('new:')._send(
						'init:', (param1._send('brLeft:') - temp0), (-
								kernel.CoordPri(1, kernel.CoordPri(param1._send('y:')))
								temp1
							), (param1._send('brRight:') + temp0), (-
								kernel.CoordPri(1, kernel.CoordPri(param1._send('y:')))
								temp1
							), (param1._send('brRight:') + temp0), (+
								param1._send('y:')
								temp1
							), (param1._send('brLeft:') - temp0), (+
								param1._send('y:')
								temp1
							),
						'yourself:'
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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global1 = self
		global29 = kernel.GetSaveDir()
		self._send('setCursor:', global21, 1, 'init:')
		self._send('setCursor:', global20, 1)
		while (not global4):

			self._send('doit:')
		#end:loop
	#end:method

	@classmethod
	def quitGame(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((not argc) or param1):
			global4 = 1
		#endif
	#end:method

	@classmethod
	def masterVolume(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			kernel.DoSound(0, param1)
		else:
			kernel.DoSound(0)
		#endif
	#end:method

	@classmethod
	def detailLevel(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			_detailLevel = param1
			global5._send('eachElementDo:', #checkDetail)
		#endif
		return _detailLevel
	#end:method

	@classmethod
	def replay():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if global24:
			global24._send('dispose:')
		#endif
		if global25:
			global25._send('dispose:')
		#endif
		global5._send('eachElementDo:', #perform, RU)
		global1._send('setCursor:', global21, 1)
		(= temp0
			if (not proc999_5(global2._send('style:'), -1, 11, 12, 13, 14)):
				global2._send('style:')
			else:
				100
			#endif
		)
		kernel.DrawPic(global2._send('curPic:'), temp0, 1)
		if (global36 != -1):
			kernel.DrawPic(global36, 100, 0)
		#endif
		global10._send('doit:')
		(cond
			case ((not global80._send('canControl:')) and (not global80._send('canInput:'))):
				global1._send('setCursor:', global21)
			#end:case
			case (global69 and global69._send('curIcon:')):
				global1._send('setCursor:', global69._send('curIcon:')._send('cursor:'))
			#end:case
			else:
				global1._send('setCursor:', global20)
			#end:else
		)
		SL._send('doit:')
		kernel.DoSound(2)
		global8._send('pause:', 0)
		global86 = (global88 - kernel.GetTime())
		while (not global4):

			self._send('doit:')
		#end:loop
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		Motion
		Sound
		global5 = cast._send('add:')
		global32 = features._send('add:')
		global8 = Sounds._send('add:')
		global6 = regions._send('add:')
		global10 = addToPics._send('add:')
		global7 = timers._send('add:')
		global78 = theDoits._send('add:')
		global73 = mouseDownHandler._send('add:')
		global72 = keyDownHandler._send('add:')
		global74 = directionHandler._send('add:')
		global93 = walkHandler._send('add:')
		global84 = 0
		global29 = kernel.GetSaveDir()
		Inv._send('init:')
		if (not global80):
			global80 = User
		#endif
		global80._send('init:')
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if panelObj:
			temp1 = panelObj
			temp2 = panelSelector
			panelObj = panelSelector = 0
			proc999_7(temp1, temp2)
		#endif
		global88 = (global86 + kernel.GetTime())
		if global84:
			while global84:

				global84._send('eachElementDo:', #doit)
				if (temp0 = Event._send('new:')._send('type:') and global84):
					global84._send('firstTrue:', #handleEvent, temp0)
				#endif
				temp0._send('dispose:')
				global88 = (global86 + kernel.GetTime())
				global8._send('eachElementDo:', #check)
			#end:loop
		#endif
		if global92:
			global92._send('eachElementDo:', #doit)
			if (not global25):
				if (temp0 = Event._send('new:')._send('type:') and global92):
					global92._send('firstTrue:', #handleEvent, temp0)
				#endif
				temp0._send('dispose:')
				global88 = (global86 + kernel.GetTime())
				return
			#endif
		#endif
		global8._send('eachElementDo:', #check)
		global7._send('eachElementDo:', #doit)
		if (global25 and global25._send('check:')):
			global25._send('dispose:')
		#endif
		kernel.Animate(global5._send('elements:'), 1)
		if global37:
			global37 = 0
			global5._send('eachElementDo:', #motionCue)
		#endif
		if global18:
			global18._send('eachElementDo:', #doit)
		#endif
		if script:
			script._send('doit:')
		#endif
		global6._send('eachElementDo:', #doit)
		if global84:
			return
		#endif
		if (global13 == global11):
			global80._send('doit:')
		#endif
		global78._send('doit:')
		if (global13 != global11):
			self._send('newRoom:', global13)
		#endif
		global7._send('eachElementDo:', #delete)
		kernel.GameIsRestarting(0)
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global10._send('eachElementDo:', #dispose, 'eachElementDo:', #delete, 'release:')
		global32._send('eachElementDo:', #perform, fDC, 'release:')
		global5._send('eachElementDo:', #dispose, 'eachElementDo:', #delete)
		global7._send('eachElementDo:', #delete)
		global6._send('eachElementDo:', #perform, DNKR, 'release:')
		global78._send('release:')
		kernel.Animate(0)
		global12 = global11
		global11 = param1
		global13 = param1
		kernel.FlushResources(param1)
		self._send('startRoom:', global11)
		while temp5 = Event._send('new:', 3)._send('type:'):

			temp5._send('dispose:')
		#end:loop
		temp5._send('dispose:')
	#end:method

	@classmethod
	def startRoom(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if global14:
			kernel.SetDebug()
		#endif
		global6._send('addToFront:', global2 = kernel.ScriptID(param1))
		global2._send('init:')
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case param1._send('claimed:'): 1#end:case
			case (script and script._send('handleEvent:', param1)): 1#end:case
			case (param1._send('type:') & 0x4000):
				self._send('pragmaFail:')
			#end:case
		)
		param1._send('claimed:')
	#end:method

	@classmethod
	def changeScore(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global15 += param1)
		SL._send('doit:')
	#end:method

	@classmethod
	def restart():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if global25:
			global25._send('dispose:')
		#endif
		kernel.RestartGame()
	#end:method

	@classmethod
	def save():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not kernel.ValidPath(global29)):
			kernel.Message(0, 994, 9, 0, 0, 1, @temp22)
			kernel.Format(@temp127, @temp22, global29)
			Print._send('font:', 0, 'addText:', @temp127, 'init:')
			proc990_0(global29)
		#endif
		kernel.Load(135, global23)
		kernel.ScriptID(990)
		temp21 = self._send('setCursor:', global20)
		global8._send('pause:', 1)
		if localproc_0(1):
			if global25:
				global25._send('dispose:')
			#endif
			if (temp20 = Save._send('doit:', @temp0) != -1):
				temp21 = self._send('setCursor:', global21, 1)
				if (not kernel.SaveGame(name, temp20, @temp0, global27)):
					kernel.Message(0, 994, 1, 0, 0, 1, @temp22)
					kernel.Message(0, 994, 2, 0, 0, 1, @temp122)
					Print._send(
						'font:', 0,
						'addText:', @temp22,
						'addButton:', 1, @temp122, 0, 40,
						'init:'
					)
				#endif
				self._send('setCursor:', temp21, kernel.HaveMouse())
			#endif
			localproc_0(0)
		#endif
		global8._send('pause:', 0)
	#end:method

	@classmethod
	def restore():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not kernel.ValidPath(global29)):
			kernel.Message(0, 994, 9, 0, 0, 1, @temp22)
			kernel.Format(@temp127, @temp22, global29)
			Print._send('font:', 0, 'addText:', @temp127, 'init:')
			proc990_0(global29)
		#endif
		kernel.Load(135, global23)
		kernel.ScriptID(990)
		temp21 = self._send('setCursor:', global20)
		global8._send('pause:', 1)
		if localproc_0(1):
			if global25:
				global25._send('dispose:')
			#endif
			if (temp20 = Restore._send('doit:', &rest) != -1):
				self._send('setCursor:', global21, 1)
				if kernel.CheckSaveGame(name, temp20, global27):
					kernel.RestoreGame(name, temp20, global27)
				else:
					kernel.Message(0, 994, 3, 0, 0, 1, @temp22)
					kernel.Message(0, 994, 2, 0, 0, 1, @temp122)
					Print._send(
						'font:', 0,
						'addText:', @temp22,
						'addButton:', 1, @temp122, 0, 40,
						'init:'
					)
					self._send('setCursor:', temp21, kernel.HaveMouse())
				#endif
			#endif
			localproc_0(0)
		#endif
		global8._send('pause:', 0)
	#end:method

	@classmethod
	def setCursor(param1 = None, param2 = None, param3 = None, param4 = None, param5 = None, param6 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = global19
		if kernel.IsObject(param1):
			global19 = param1
			param1._send('init:')
		else:
			kernel.SetCursor(param1, 0, 0)
		#endif
		if (argc > 1):
			kernel.SetCursor(param2)
			if (argc > 2):
				kernel.SetCursor(param3, param4)
				if (argc > 4):
					kernel.SetCursor(param1, 0, 0, param5, param6)
				#endif
			#endif
		#endif
		return temp0
	#end:method

	@classmethod
	def showMem():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.Format(@temp0, r"""Free Heap: %u Bytes\nLargest ptr: %u Bytes\nFreeHunk: %u KBytes\nLargest hunk: %u Bytes""", kernel.MemoryInfo(1), kernel.MemoryInfo(0), (>>
			kernel.MemoryInfo(3)
			0x0006
		), kernel.MemoryInfo(2))
		Print._send('addText:', @temp0, 'init:')
	#end:method

	@classmethod
	def pragmaFail():#end:method

	@classmethod
	def notify():#end:method

	@classmethod
	def setScript(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if script:
			script._send('dispose:')
		#endif
		if param1:
			param1._send('init:', self, &rest)
		#endif
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if script:
			script._send('cue:')
		#endif
	#end:method

	@classmethod
	def handsOff():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if handsOffCode:
			handsOffCode._send('doit:', &rest)
		else:
			User._send('canControl:', 0, 'canInput:', 0)
			if kernel.IsObject(global0):
				global0._send('setMotion:', 0)
			#endif
		#endif
	#end:method

	@classmethod
	def handsOn():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if handsOnCode:
			handsOnCode._send('doit:', &rest)
		else:
			User._send('canControl:', 1, 'canInput:', 1)
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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not initialized):
			initialized = 1
			if (not global6._send('contains:', self)):
				global6._send('addToEnd:', self)
			#endif
			super._send('init:')
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if script:
			script._send('doit:')
		#endif
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case param1._send('claimed:'): 1#end:case
			case (param1._send('type:') & 0x0040): 0#end:case
			case 
				(not
					(and
						script
						(script._send('handleEvent:', param1) or 1)
						param1._send('claimed:')
					)
				):
				param1._send('claimed:', self._send('doVerb:', param1._send('message:')))
			#end:case
		)
		param1._send('claimed:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (modNum == -1):
			modNum = global11
		#endif
		(return
			if kernel.Message(0, modNum, noun, param1, 0, 1):
				global91._send('say:', noun, param1, 0, 0, 0, modNum)
				1
			else:
				0
			#endif
		)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global6._send('delete:', self)
		if kernel.IsObject(script):
			script._send('dispose:')
		#endif
		if kernel.IsObject(timer):
			timer._send('dispose:', 'delete:')
		#endif
		global8._send('eachElementDo:', #clean, self)
		kernel.DisposeScript(number)
	#end:method

	@classmethod
	def setScript(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if kernel.IsObject(script):
			script._send('dispose:')
		#endif
		if param1:
			param1._send('init:', self, &rest)
		#endif
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if script:
			script._send('cue:')
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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		number = global11
		global31 = picAngle
		if picture:
			self._send('drawPic:', picture)
		#endif
		self._send('reflectPosn:', global80._send('alterEgo:'), global80._send('alterEgo:')._send('edgeHit:'))
		global80._send('alterEgo:')._send('edgeHit:', 0)
	#end:method

	@classmethod
	def reflectPosn(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param2
			case 1:
				param1._send('y:', 188)
			#end:case
			case 4:
				param1._send('x:', (319 - param1._send('xStep:')))
			#end:case
			case 3:
				param1._send('y:', (horizon + param1._send('yStep:')))
			#end:case
			case 2:
				param1._send('x:', 1)
			#end:case
		#end:match
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if script:
			script._send('doit:')
		#endif
		if temp0 = self._send('edgeToRoom:', global80._send('alterEgo:')._send('edgeHit:')):
			self._send('newRoom:', temp0)
		#endif
	#end:method

	@classmethod
	def edgeToRoom(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

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
	def roomToEdge(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if obstacles:
			obstacles._send('dispose:')
		#endif
		super._send('dispose:')
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		((inset and inset._send('handleEvent:', param1)) or super._send('handleEvent:', param1))
		param1._send('claimed:')
	#end:method

	@classmethod
	def setInset(param1 = None, param2 = None, param3 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if inset:
			inset._send('dispose:')
		#endif
		if (argc and param1):
			param1._send(
				'init:', (param2 if (argc >= 2) else 0), self, if (argc >= 3):
						param3
					else:
						0
					#endif
			)
		#endif
	#end:method

	@classmethod
	def setRegions(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 0
		while (temp0 < argc): # inline for
			temp1 = param1[temp0]
			temp2 = kernel.ScriptID(temp1)
			temp2._send('number:', temp1)
			global6._send('add:', temp2)
			if (not temp2._send('initialized:')):
				temp2._send('init:')
			#endif
			# for:reinit
			temp0.post('++')
		#end:loop
	#end:method

	@classmethod
	def addObstacle(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not kernel.IsObject(obstacles)):
			obstacles = List._send('new:')
		#endif
		obstacles._send('add:', param1, &rest)
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global6._send('delete:', self, 'eachElementDo:', #newRoom, param1, 'addToFront:', self)
		global13 = param1
		super._send('newRoom:', param1)
	#end:method

	@classmethod
	def drawPic(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if global10:
			global10._send('eachElementDo:', #dispose, 'release:')
		#endif
		curPic = param1
		global36 = -1
		kernel.DrawPic(param1, (cond
			case (argc == 2): param2#end:case
			case (style != -1): style#end:case
			else: 100#end:else
		), 1)
	#end:method

	@classmethod
	def overlay(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global36 = param1
		kernel.DrawPic(param1, (cond
			case (argc == 2): param2#end:case
			case (style != -1): style#end:case
			else: 100#end:else
		), 0)
	#end:method

#end:class or instance

class SL(Obj):
	#property vars (may be empty)
	state = 0
	code = 0
	
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if code:
			temp0 = kernel.Memory(1, 150)
			code._send('doit:', temp0)
			kernel.DrawStatus((temp0 if state else 0))
			kernel.Memory(3, temp0)
		#endif
	#end:method

	@classmethod
	def enable():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		state = 1
		self._send('doit:')
	#end:method

	@classmethod
	def disable():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		state = 0
		self._send('doit:')
	#end:method

#end:class or instance

@SCI.instance
class RU(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if param1._send('underBits:'):
			temp0 = (temp0 = (| temp0 = param1._send('signal:') 0x0001) & 0xfffb)
			param1._send('underBits:', 0, 'signal:', temp0)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class DNKR(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not param1._send('keep:')):
			param1._send('dispose:')
		#endif
	#end:method

#end:class or instance

@SCI.instance
class fDC(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if param1._send('respondsTo:', #delete):
			param1._send('signal:', (param1._send('signal:') & 0xffdf), 'dispose:', 'delete:')
		else:
			param1._send('dispose:')
		#endif
	#end:method

#end:class or instance

