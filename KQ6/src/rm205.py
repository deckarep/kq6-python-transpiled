#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 205
import sci_sh
import kernel
import Main
import KQ6Print
import KQ6Room
import Kq6Talker
import Body
import Print
import Messager
import Scaler
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm205 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.instance
class rm205(KQ6Room):
	#property vars (may be empty)
	picture = 200
	
	@classmethod
	def init():
		super._send('init:', &rest)
		global102._send('number:', 915, 'loop:', -1, 'play:')
		global103._send('number:', 916, 'loop:', -1, 'play:')
		global91 = demoMessager
		global0 = ego
		royalRing._send('init:')
		global0._send('init:', 'posn:', 168, 120)
		ourCursor._send('init:', 'illegalBits:', 0, 'ignoreActors:', 1, 'ignoreHorizon:', 1)
		Cursor._send('showCursor:', 0)
		global90 = 1
		global1._send('handsOff:')
		self._send('setScript:', helpScript)
		global73._send('addToFront:', self)
		global72._send('addToFront:', self)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		if 
			(and
				(not param1._send('modifiers:'))
				(param1._send('type:') & 0x0005)
				(not param1._send('claimed:'))
			)
			restartCode._send('doit:')
			return 1
		#endif
	#end:method

#end:class or instance

@SCI.instance
class restartCode(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		Cursor._send('showCursor:', 1)
		global1._send('setCursor:', global20)
		if (argc and param1):
			temp0 = 1
		else:
			(= temp0
				Print._send(
					'posn:', 70, 70,
					'font:', 4,
					'addText:', 0, 0, 5, 1, 0, 0,
					'addButton:', 1, 0, 0, 5, 3, 0, 20,
					'addButton:', 0, 0, 0, 5, 2, 0, 38,
					'init:'
				)
			)
		#endif
		if temp0:
			global102._send('fade:')
			global103._send('fade:')
			kernel.DrawPic(98)
			global73._send('delete:', global2)
			global72._send('delete:', global2)
			global1._send('restart:', 1)
		else:
			Cursor._send('showCursor:', 0)
		#endif
		super._send('doit:')
	#end:method

#end:class or instance

@SCI.instance
class ego(Body):
	#property vars (may be empty)
	modNum = 0
	sightAngle = 45
	view = 900
	
	@classmethod
	def reset(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (argc > 0):
			global0._send('loop:', param1)
		#endif
		global0._send(
			'view:', (param2 if (argc > 1) else 900),
			'signal:', 4096,
			'z:', 0,
			'setLoop:', -1,
			'setLoop:', global151,
			'setPri:', -1,
			'setMotion:', 0,
			'illegalBits:', 0,
			'ignoreActors:', 0,
			'ignoreHorizon:', 1,
			'setStep:', 5, 3,
			'setCycle:', Walk,
			'normal:', 1,
			'setSpeed:', currentSpeed
		)
		if (oldScaleSignal and (view == 900)):
			(cond
				case (oldScaleSignal & 0x0002):
					scaleSignal = oldScaleSignal
					maxScale = oldMaxScale
				#end:case
				case (oldMaxScale or oldBackSize or oldFrontY or oldBackY):
					global0._send(
						'setScale:', Scaler, oldMaxScale, oldBackSize, oldFrontY, oldBackY
					)
				#end:case
				else:
					global0._send('setScale:')
				#end:else
			)
			(= oldScaleSignal
				oldMaxScale = oldBackSize = oldFrontY = oldBackY = 0
			)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class demoMessager(Messager):
	#property vars (may be empty)
	@classmethod
	def findTalker(param1 = None, *rest):
		(= temp0
			match param1
				case 2: Alex_Demo#end:case
				else: global89#end:else
			#end:match
		)
	#end:method

#end:class or instance

@SCI.instance
class helpScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('reset:', 2)
				cycles = 2
			#end:case
			case 1:
				global91._send('say:', 0, 0, 6, 0, self)
			#end:case
			case 2:
				global91._send('say:', 0, 0, 0, 1, self)
			#end:case
			case 3:
				global69._send('disable:')
				ourCursor._send('setCel:', 7, 'setMotion:', MoveTo, 23, 23, self)
			#end:case
			case 4:
				theWalkIcon._send('init:', 'stopUpd:')
				theHandIcon._send('init:', 'stopUpd:')
				theLookIcon._send('init:', 'stopUpd:')
				theTalkIcon._send('init:', 'stopUpd:')
				theCurInvIcon._send('init:', 'stopUpd:')
				theCurInvIconMask._send('init:', 'stopUpd:')
				theInvIcon._send('init:', 'stopUpd:')
				theControlIcon._send('init:', 'stopUpd:')
				cycles = 2
			#end:case
			case 5:
				if kernel.FileIO(10, r"""g"""):
					ourCursor._send('hide:')
					Cursor._send('showCursor:', 1)
					temp1 = 0
					temp0 = 0
					global1._send('setCursor:', global20)
					while True: #repeat
						(breakif
							(!=
								(= temp0
									Print._send(
										'font:', global23,
										'addText:', r"""Which script?""",
										'addEdit:', @temp1, 5, 80,
										'addButton:', 1, r"""1._______Continue_______""", 0, 20,
										'addButton:', 2, r"""2._____OtherIcons_______""", 0, 34,
										'addButton:', 3, r"""3.____InventoryScript___""", 0, 48,
										'addButton:', 4, r"""4.__ControlPanelScript__""", 0, 62,
										'init:'
									)
								)
								0
							)
						)
					#end:loop
					if temp1:
						temp0 = kernel.ReadNumber(@temp1)
					#endif
					match temp0
						case 1:
							helpScript._send('cue:')
						#end:case
						case 2:
							client._send('setScript:', otherIconsScript)
						#end:case
						case 3:
							client._send('setScript:', inventoryScript)
						#end:case
						case 4:
							client._send('setScript:', controlPanelScript)
						#end:case
					#end:match
					ourCursor._send('show:')
					Cursor._send('showCursor:', 0)
				else:
					helpScript._send('cue:')
				#endif
			#end:case
			case 6:
				global91._send('say:', 0, 0, 0, 2, self)
			#end:case
			case 7:
				global91._send('say:', 0, 0, 0, 3, self)
			#end:case
			case 8:
				theWalkIcon._send('setCel:', 1)
				seconds = 2
			#end:case
			case 9:
				theWalkIcon._send('setCel:', 0)
				ourCursor._send('setMotion:', MoveTo, 67, 23, self)
			#end:case
			case 10:
				global91._send('say:', 0, 0, 0, 4, self)
			#end:case
			case 11:
				theHandIcon._send('setCel:', 1)
				seconds = 2
			#end:case
			case 12:
				theHandIcon._send('setCel:', 0)
				ourCursor._send('setMotion:', MoveTo, 108, 23, self)
			#end:case
			case 13:
				global91._send('say:', 0, 0, 0, 5, self)
			#end:case
			case 14:
				theLookIcon._send('setCel:', 1)
				seconds = 2
			#end:case
			case 15:
				theLookIcon._send('setCel:', 0)
				ourCursor._send('setMotion:', MoveTo, 154, 23, self)
			#end:case
			case 16:
				global91._send('say:', 0, 0, 0, 6, self)
			#end:case
			case 17:
				theTalkIcon._send('setCel:', 1)
				seconds = 2
			#end:case
			case 18:
				theTalkIcon._send('setCel:', 0)
				ourCursor._send('setMotion:', MoveTo, 202, 23, self)
			#end:case
			case 19:
				global91._send('say:', 0, 0, 0, 7, self)
			#end:case
			case 20:
				ourCursor._send('setMotion:', MoveTo, 253, 23, self)
			#end:case
			case 21:
				global91._send('say:', 0, 0, 0, 8, self)
			#end:case
			case 22:
				theInvIcon._send('setCel:', 1)
				seconds = 2
			#end:case
			case 23:
				theInvIcon._send('setCel:', 0)
				ourCursor._send('setMotion:', MoveTo, 297, 23, self)
			#end:case
			case 24:
				global91._send('say:', 0, 0, 0, 9, self)
			#end:case
			case 25:
				theControlIcon._send('setCel:', 1)
				seconds = 2
			#end:case
			case 26:
				theControlIcon._send('setCel:', 0)
				cycles = 1
			#end:case
			case 27:
				global91._send('say:', 0, 0, 0, 10, self)
			#end:case
			case 28:
				ourCursor._send('setMotion:', MoveTo, 23, 23, self)
			#end:case
			case 29:
				seconds = 2
			#end:case
			case 30:
				theWalkIcon._send('setCel:', 1)
				seconds = 2
			#end:case
			case 31:
				theWalkIcon._send('setCel:', 0)
				ourCursor._send('setCel:', 0)
				cycles = 15
			#end:case
			case 32:
				theWalkIcon._send('hide:')
				theHandIcon._send('hide:')
				theLookIcon._send('hide:')
				theTalkIcon._send('hide:')
				theCurInvIcon._send('hide:')
				theCurInvIconMask._send('hide:')
				theInvIcon._send('hide:')
				theControlIcon._send('hide:')
				ourCursor._send('setMotion:', MoveTo, 118, 90, self)
			#end:case
			case 33:
				global91._send('say:', 0, 0, 0, 11, self)
			#end:case
			case 34:
				seconds = 2
			#end:case
			case 35:
				ourCursor._send('setCel:', 1)
				seconds = 1
			#end:case
			case 36:
				ourCursor._send('setCel:', 2)
				seconds = 1
			#end:case
			case 37:
				ourCursor._send('setCel:', 3)
				seconds = 1
			#end:case
			case 38:
				ourCursor._send('setCel:', 0)
				seconds = 1
			#end:case
			case 39:
				ourCursor._send('setCel:', 1)
				seconds = 1
			#end:case
			case 40:
				global91._send('say:', 0, 0, 0, 12, self)
			#end:case
			case 41:
				seconds = 2
			#end:case
			case 42:
				ourCursor._send('setCel:', 0)
				seconds = 1
			#end:case
			case 43:
				ourCursor._send('setCel:', 1)
				seconds = 1
			#end:case
			case 44:
				ourCursor._send('setCel:', 0)
				seconds = 1
			#end:case
			case 45:
				ourCursor._send('setCel:', 1)
				seconds = 1
			#end:case
			case 46:
				global91._send('say:', 0, 0, 0, 13, self)
			#end:case
			case 47:
				global91._send('say:', 0, 0, 0, 14, self)
			#end:case
			case 48:
				ourCursor._send('setMotion:', MoveTo, 23, 23, self)
			#end:case
			case 49:
				theWalkIcon._send('show:', 'stopUpd:')
				theHandIcon._send('show:', 'stopUpd:')
				theLookIcon._send('show:', 'stopUpd:')
				theTalkIcon._send('show:', 'stopUpd:')
				theCurInvIcon._send('show:', 'stopUpd:')
				theCurInvIconMask._send('show:', 'stopUpd:')
				theInvIcon._send('show:', 'stopUpd:')
				theControlIcon._send('show:', 'stopUpd:')
				ourCursor._send('setCel:', 7)
				cycles = 2
			#end:case
			case 50:
				global91._send('say:', 0, 0, 0, 15, self)
			#end:case
			case 51:
				seconds = 2
			#end:case
			case 52:
				theWalkIcon._send('setCel:', 1)
				seconds = 2
			#end:case
			case 53:
				theWalkIcon._send('setCel:', 0)
				ourCursor._send('setCel:', 0)
				cycles = 15
			#end:case
			case 54:
				theWalkIcon._send('hide:')
				theHandIcon._send('hide:')
				theLookIcon._send('hide:')
				theTalkIcon._send('hide:')
				theCurInvIcon._send('hide:')
				theCurInvIconMask._send('hide:')
				theInvIcon._send('hide:')
				theControlIcon._send('hide:')
				ourCursor._send('setMotion:', MoveTo, 217, 158, self)
			#end:case
			case 55:
				global0._send('setMotion:', MoveTo, 217, 158, self)
			#end:case
			case 56:
				seconds = 2
			#end:case
			case 57:
				ourCursor._send('setMotion:', MoveTo, 168, 120, self)
			#end:case
			case 58:
				seconds = 2
			#end:case
			case 59:
				global0._send('setMotion:', MoveTo, 168, 120, self)
			#end:case
			case 60:
				global0._send('reset:', 2)
				cycles = 2
			#end:case
			case 61:
				ourCursor._send('setMotion:', MoveTo, 108, 23, self)
			#end:case
			case 62:
				theWalkIcon._send('show:', 'stopUpd:')
				theHandIcon._send('show:', 'stopUpd:')
				theLookIcon._send('show:', 'stopUpd:')
				theTalkIcon._send('show:', 'stopUpd:')
				theCurInvIcon._send('show:', 'stopUpd:')
				theCurInvIconMask._send('show:', 'stopUpd:')
				theInvIcon._send('show:', 'stopUpd:')
				theControlIcon._send('show:', 'stopUpd:')
				ourCursor._send('setCel:', 7)
				cycles = 2
			#end:case
			case 63:
				global91._send('say:', 0, 0, 0, 16, self)
			#end:case
			case 64:
				global91._send('say:', 0, 0, 0, 17, self)
			#end:case
			case 65:
				theLookIcon._send('setCel:', 1)
				seconds = 2
			#end:case
			case 66:
				theLookIcon._send('setCel:', 0)
				ourCursor._send('setCel:', 1)
				cycles = 15
			#end:case
			case 67:
				theWalkIcon._send('hide:')
				theHandIcon._send('hide:')
				theLookIcon._send('hide:')
				theTalkIcon._send('hide:')
				theCurInvIcon._send('hide:')
				theCurInvIconMask._send('hide:')
				theInvIcon._send('hide:')
				theControlIcon._send('hide:')
				ourCursor._send('setMotion:', MoveTo, 104, 134, self)
			#end:case
			case 68:
				cycles = 2
			#end:case
			case 69:
				global91._send('say:', 0, 0, 0, 18, self)
			#end:case
			case 70:
				global91._send('say:', 0, 0, 0, 19, self)
			#end:case
			case 71:
				ourCursor._send('setMotion:', MoveTo, 67, 23, self)
			#end:case
			case 72:
				theWalkIcon._send('show:', 'stopUpd:')
				theHandIcon._send('show:', 'stopUpd:')
				theLookIcon._send('show:', 'stopUpd:')
				theTalkIcon._send('show:', 'stopUpd:')
				theCurInvIcon._send('show:', 'stopUpd:')
				theCurInvIconMask._send('show:', 'stopUpd:')
				theInvIcon._send('show:', 'stopUpd:')
				theControlIcon._send('show:', 'stopUpd:')
				ourCursor._send('setCel:', 7)
				cycles = 2
			#end:case
			case 73:
				global91._send('say:', 0, 0, 0, 20, self)
			#end:case
			case 74:
				global91._send('say:', 0, 0, 0, 21, self)
			#end:case
			case 75:
				theHandIcon._send('setCel:', 1)
				seconds = 2
			#end:case
			case 76:
				theHandIcon._send('setCel:', 0)
				ourCursor._send('setCel:', 2)
				cycles = 15
			#end:case
			case 77:
				theWalkIcon._send('hide:')
				theHandIcon._send('hide:')
				theLookIcon._send('hide:')
				theTalkIcon._send('hide:')
				theCurInvIcon._send('hide:')
				theCurInvIconMask._send('hide:')
				theInvIcon._send('hide:')
				theControlIcon._send('hide:')
				ourCursor._send('setMotion:', MoveTo, 104, 131, self)
			#end:case
			case 78:
				global0._send(
					'moveSpeed:', 4,
					'cycleSpeed:', 4,
					'setMotion:', MoveTo, 134, 136, self
				)
			#end:case
			case 79:
				self._send('setScript:', takeRingScr, self)
			#end:case
			case 80:
				global0._send(
					'moveSpeed:', 4,
					'cycleSpeed:', 4,
					'setMotion:', MoveTo, 168, 120, self
				)
			#end:case
			case 81:
				global0._send('reset:', 2)
				cycles = 2
			#end:case
			case 82:
				global91._send('say:', 0, 0, 0, 22, self)
			#end:case
			case 83:
				global91._send('say:', 0, 0, 0, 23, self)
			#end:case
			case 84:
				client._send('setScript:', otherIconsScript)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class otherIconsScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				ourCursor._send('setMotion:', MoveTo, 154, 23, self)
			#end:case
			case 1:
				theWalkIcon._send('show:', 'stopUpd:')
				theHandIcon._send('show:', 'stopUpd:')
				theLookIcon._send('show:', 'stopUpd:')
				theTalkIcon._send('show:', 'stopUpd:')
				theCurInvIcon._send('show:', 'stopUpd:')
				theCurInvIconMask._send('show:', 'stopUpd:')
				theInvIcon._send('show:', 'stopUpd:')
				theControlIcon._send('show:', 'stopUpd:')
				ourCursor._send('setCel:', 7)
				cycles = 2
			#end:case
			case 2:
				global91._send('say:', 0, 0, 3, 1, self)
			#end:case
			case 3:
				theTalkIcon._send('setCel:', 1)
				seconds = 2
			#end:case
			case 4:
				theTalkIcon._send('setCel:', 0, 'stopUpd:')
				ourCursor._send('setCel:', 3)
				cycles = 2
			#end:case
			case 5:
				theWalkIcon._send('hide:')
				theHandIcon._send('hide:')
				theLookIcon._send('hide:')
				theTalkIcon._send('hide:')
				theCurInvIcon._send('hide:')
				theCurInvIconMask._send('hide:')
				theInvIcon._send('hide:')
				theControlIcon._send('hide:')
				cycles = 2
			#end:case
			case 6:
				global91._send('say:', 0, 0, 3, 2, self)
			#end:case
			case 7:
				ourCursor._send('setMotion:', MoveTo, 79, 162, self)
			#end:case
			case 8:
				global91._send('say:', 0, 0, 3, 3, self)
			#end:case
			case 9:
				global91._send('say:', 0, 0, 3, 4, self)
			#end:case
			case 10:
				ourCursor._send('setMotion:', MoveTo, 202, 23, self)
			#end:case
			case 11:
				theWalkIcon._send('show:', 'stopUpd:')
				theHandIcon._send('show:', 'stopUpd:')
				theLookIcon._send('show:', 'stopUpd:')
				theTalkIcon._send('show:', 'stopUpd:')
				theCurInvIcon._send('show:', 'stopUpd:')
				theCurInvIconMask._send('show:', 'stopUpd:')
				theInvIcon._send('show:', 'stopUpd:')
				theControlIcon._send('show:', 'stopUpd:')
				ourCursor._send('setCel:', 7)
				cycles = 2
			#end:case
			case 12:
				global91._send('say:', 0, 0, 3, 5, self)
			#end:case
			case 13:
				client._send('setScript:', inventoryScript)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class inventoryScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				ourCursor._send('setMotion:', MoveTo, 253, 23, self)
			#end:case
			case 1:
				global91._send('say:', 0, 0, 2, 1, self)
			#end:case
			case 2:
				theInvIcon._send('setCel:', 1)
				seconds = 2
			#end:case
			case 3:
				theInvIcon._send('setCel:', 0)
				cycles = 15
			#end:case
			case 4:
				theWalkIcon._send('hide:')
				theHandIcon._send('hide:')
				theLookIcon._send('hide:')
				theTalkIcon._send('hide:')
				theCurInvIcon._send('hide:')
				theCurInvIconMask._send('hide:')
				theInvIcon._send('hide:')
				theControlIcon._send('hide:')
				cycles = 2
			#end:case
			case 5:
				theInvWindow._send('init:', 'setPri:', 15, 'stopUpd:', 'addToPic:')
				invEye._send('init:', 'stopUpd:')
				invHand._send('init:', 'stopUpd:')
				invArrow._send('init:', 'stopUpd:')
				invTalk._send('init:', 'stopUpd:')
				invMore._send('init:', 'stopUpd:')
				invOk._send('init:', 'stopUpd:')
				local1 = 1
				local0 = 1
				cycles = 2
			#end:case
			case 6:
				global91._send('say:', 0, 0, 2, 2, self)
			#end:case
			case 7:
				ourCursor._send('setMotion:', MoveTo, 86, 119, self)
			#end:case
			case 8:
				invEye._send('setCel:', 1)
				seconds = 2
			#end:case
			case 9:
				invEye._send('setCel:', 0, 'stopUpd:')
				ourCursor._send('cel:', 1, 'setMotion:', MoveTo, 89, 76, self)
			#end:case
			case 10:
				seconds = 2
			#end:case
			case 11:
				global91._send('say:', 0, 0, 2, 3, self)
			#end:case
			case 12:
				ourCursor._send('setMotion:', MoveTo, 117, 119, self)
			#end:case
			case 13:
				global91._send('say:', 0, 0, 2, 4, self)
			#end:case
			case 14:
				global91._send('say:', 0, 0, 2, 5, self)
			#end:case
			case 15:
				invHand._send('setCel:', 1)
				seconds = 2
			#end:case
			case 16:
				invHand._send('setCel:', 0, 'stopUpd:')
				ourCursor._send('cel:', 2, 'setMotion:', MoveTo, 89, 76, self)
			#end:case
			case 17:
				global91._send('say:', 0, 0, 2, 6, self)
			#end:case
			case 18:
				ourCursor._send('setMotion:', MoveTo, 174, 119, self)
			#end:case
			case 19:
				seconds = 2
			#end:case
			case 20:
				global91._send('say:', 0, 0, 2, 7, self)
			#end:case
			case 21:
				invTalk._send('setCel:', 1)
				seconds = 2
			#end:case
			case 22:
				invTalk._send('setCel:', 0, 'stopUpd:')
				ourCursor._send('cel:', 3, 'setMotion:', MoveTo, 89, 76, self)
			#end:case
			case 23:
				global91._send('say:', 0, 0, 2, 8, self)
			#end:case
			case 24:
				ourCursor._send('setCel:', 7, 'setMotion:', MoveTo, 203, 119, self)
			#end:case
			case 25:
				seconds = 2
			#end:case
			case 26:
				global91._send('say:', 0, 0, 2, 9, self)
			#end:case
			case 27:
				global91._send('say:', 0, 0, 2, 10, self)
			#end:case
			case 28:
				invMore._send('setCel:', 1)
				seconds = 2
			#end:case
			case 29:
				invMore._send('setCel:', 0, 'stopUpd:')
				cycles = 2
			#end:case
			case 30:
				global91._send('say:', 0, 0, 2, 11, self)
			#end:case
			case 31:
				ourCursor._send('setMotion:', MoveTo, 146, 119, self)
			#end:case
			case 32:
				seconds = 2
			#end:case
			case 33:
				global91._send('say:', 0, 0, 2, 12, self)
			#end:case
			case 34:
				invArrow._send('setCel:', 1)
				seconds = 2
			#end:case
			case 35:
				invArrow._send('setCel:', 0, 'stopUpd:')
				ourCursor._send('cel:', 7, 'setMotion:', MoveTo, 89, 76, self)
			#end:case
			case 36:
				ourCursor._send('view:', 990, 'setLoop:', 2, 'cel:', 14)
				seconds = 2
			#end:case
			case 37:
				global91._send('say:', 0, 0, 2, 13, self)
			#end:case
			case 38:
				global91._send('say:', 0, 0, 2, 14, self)
			#end:case
			case 39:
				ourCursor._send('setMotion:', MoveTo, 232, 119, self)
			#end:case
			case 40:
				global91._send('say:', 0, 0, 2, 15, self)
			#end:case
			case 41:
				invOk._send('setCel:', 1)
				seconds = 2
			#end:case
			case 42:
				theInvWindow._send('dispose:')
				invEye._send('dispose:')
				invHand._send('dispose:')
				invArrow._send('dispose:')
				invTalk._send('dispose:')
				invMore._send('dispose:')
				invOk._send('dispose:')
				local1 = 0
				local0 = 0
				cycles = 2
			#end:case
			case 43:
				kernel.DrawPic(global2._send('picture:'), 9)
				ourCursor._send('setMotion:', MoveTo, 202, 23, self)
			#end:case
			case 44:
				theCurInvIconMask._send(
					'view:', 990,
					'setLoop:', 2,
					'ignoreActors:', 1,
					'illegalBits:', 0,
					'ignoreHorizon:', 1,
					'cel:', 14,
					'posn:', 199, 9,
					'show:',
					'stopUpd:'
				)
				theWalkIcon._send('show:', 'stopUpd:')
				theHandIcon._send('show:', 'stopUpd:')
				theLookIcon._send('show:', 'stopUpd:')
				theTalkIcon._send('show:', 'stopUpd:')
				theCurInvIcon._send('show:', 'stopUpd:')
				theInvIcon._send('show:', 'stopUpd:')
				theControlIcon._send('show:', 'stopUpd:')
				ourCursor._send('view:', 998, 'setLoop:', 1, 'setCel:', 7)
				cycles = 2
			#end:case
			case 45:
				global91._send('say:', 0, 0, 2, 16, self)
			#end:case
			case 46:
				global91._send('say:', 0, 0, 2, 17, self)
			#end:case
			case 47:
				global91._send('say:', 0, 0, 2, 18, self)
			#end:case
			case 48:
				theWalkIcon._send('hide:')
				theHandIcon._send('hide:')
				theLookIcon._send('hide:')
				theTalkIcon._send('hide:')
				theCurInvIcon._send('hide:')
				theCurInvIconMask._send('hide:')
				theInvIcon._send('hide:')
				theControlIcon._send('hide:')
				ourCursor._send(
					'view:', 990,
					'setLoop:', 2,
					'cel:', 14,
					'setMotion:', MoveTo, 79, 162, self
				)
			#end:case
			case 49:
				seconds = 2
			#end:case
			case 50:
				global91._send('say:', 0, 0, 2, 19, self)
			#end:case
			case 51:
				global91._send('say:', 0, 0, 2, 20, self)
			#end:case
			case 52:
				ourCursor._send('setMotion:', MoveTo, 168, 90, self)
			#end:case
			case 53:
				global91._send('say:', 0, 0, 2, 21, self)
			#end:case
			case 54:
				global91._send('say:', 0, 0, 2, 22, self)
			#end:case
			case 55:
				global91._send('say:', 0, 0, 2, 23, self)
			#end:case
			case 56:
				ourCursor._send('setMotion:', MoveTo, 23, 23, self)
			#end:case
			case 57:
				theWalkIcon._send('setCel:', 2, 'show:', 'stopUpd:')
				theHandIcon._send('setCel:', 2, 'show:', 'stopUpd:')
				theLookIcon._send('show:', 'stopUpd:')
				theTalkIcon._send('show:', 'stopUpd:')
				theCurInvIcon._send('show:', 'stopUpd:')
				theCurInvIconMask._send(
					'view:', 980,
					'setLoop:', 4,
					'setCel:', 1,
					'posn:', 176, 7,
					'show:',
					'stopUpd:'
				)
				theInvIcon._send('show:', 'stopUpd:')
				theControlIcon._send('show:', 'stopUpd:')
				ourCursor._send('view:', 998, 'setLoop:', 1, 'setCel:', 7)
				cycles = 2
			#end:case
			case 58:
				global91._send('say:', 0, 0, 2, 24, self)
			#end:case
			case 59:
				client._send('setScript:', controlPanelScript)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class controlPanelScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				ourCursor._send('setMotion:', MoveTo, 297, 23, self)
			#end:case
			case 1:
				theWalkIcon._send('show:', 'stopUpd:')
				theHandIcon._send('show:', 'stopUpd:')
				theLookIcon._send('show:', 'stopUpd:')
				theTalkIcon._send('show:', 'stopUpd:')
				theCurInvIcon._send('show:', 'stopUpd:')
				theCurInvIconMask._send('show:', 'stopUpd:')
				theInvIcon._send('show:', 'stopUpd:')
				theControlIcon._send('show:', 'stopUpd:')
				ourCursor._send('setCel:', 7)
				cycles = 2
			#end:case
			case 2:
				global91._send('say:', 0, 0, 1, 1, self)
			#end:case
			case 3:
				theControlIcon._send('setCel:', 1)
				seconds = 2
			#end:case
			case 4:
				theControlIcon._send('setCel:', 0)
				seconds = 2
			#end:case
			case 5:
				theWalkIcon._send('hide:')
				theHandIcon._send('hide:')
				theLookIcon._send('hide:')
				theTalkIcon._send('hide:')
				theCurInvIcon._send('hide:')
				theCurInvIconMask._send('hide:')
				theInvIcon._send('hide:')
				theControlIcon._send('hide:')
				cycles = 2
			#end:case
			case 6:
				local1 = 1
				theControlPanel._send('init:', 'stopUpd:')
				saveBut._send('init:', 'stopUpd:')
				restoreBut._send('init:', 'stopUpd:')
				restartBut._send('init:', 'stopUpd:')
				quitBut._send('init:', 'stopUpd:')
				aboutBut._send('init:', 'stopUpd:')
				modeBut._send('init:', 'stopUpd:')
				playBut._send('init:', 'stopUpd:')
				cycles = 2
			#end:case
			case 7:
				global91._send('say:', 0, 0, 1, 2, self)
			#end:case
			case 8:
				ourCursor._send('setMotion:', MoveTo, 100, 48, self)
			#end:case
			case 9:
				global91._send('say:', 0, 0, 1, 3, self)
			#end:case
			case 10:
				saveBut._send('setCel:', 1)
				seconds = 2
			#end:case
			case 11:
				saveBut._send('setCel:', 0, 'stopUpd:')
				ourCursor._send('setMotion:', MoveTo, 100, 68, self)
			#end:case
			case 12:
				global91._send('say:', 0, 0, 1, 4, self)
			#end:case
			case 13:
				restoreBut._send('setCel:', 1)
				seconds = 2
			#end:case
			case 14:
				restoreBut._send('setCel:', 0, 'stopUpd:')
				ourCursor._send('setMotion:', MoveTo, 100, 88, self)
			#end:case
			case 15:
				global91._send('say:', 0, 0, 1, 5, self)
			#end:case
			case 16:
				restartBut._send('setCel:', 1)
				seconds = 2
			#end:case
			case 17:
				restartBut._send('setCel:', 0, 'stopUpd:')
				ourCursor._send('setMotion:', MoveTo, 100, 108, self)
			#end:case
			case 18:
				global91._send('say:', 0, 0, 1, 6, self)
			#end:case
			case 19:
				quitBut._send('setCel:', 1)
				seconds = 2
			#end:case
			case 20:
				local0 = 1
				quitBut._send('setCel:', 0, 'stopUpd:')
				ourCursor._send('setMotion:', MoveTo, 100, 128, self)
			#end:case
			case 21:
				global91._send('say:', 0, 0, 1, 7, self)
			#end:case
			case 22:
				aboutBut._send('setCel:', 1)
				seconds = 2
			#end:case
			case 23:
				aboutBut._send('setCel:', 0, 'stopUpd:')
				ourCursor._send('setMotion:', MoveTo, 100, 148, self)
			#end:case
			case 24:
				global91._send('say:', 0, 0, 1, 8, self)
			#end:case
			case 25:
				playBut._send('setCel:', 1)
				seconds = 2
			#end:case
			case 26:
				playBut._send('setCel:', 0, 'stopUpd:')
				ourCursor._send('setMotion:', MoveTo, 187, 150, self)
			#end:case
			case 27:
				if (global90 & 0x0002):
					seconds = 2
				else:
					KQ6Print._send(
						'posn:', 10, 10,
						'width:', 290,
						'addText:', r"""The MODE button lets you switch from speech to text during play.""",
						'init:', self
					)
				#endif
			#end:case
			case 28:
				modeBut._send('setCel:', 1)
				seconds = 2
			#end:case
			case 29:
				modeBut._send('setLoop:', 9, 'setCel:', 0)
				seconds = 2
			#end:case
			case 30:
				modeBut._send('setCel:', 1)
				seconds = 1
			#end:case
			case 31:
				modeBut._send('setLoop:', 8, 'setCel:', 0, 'stopUpd:')
				ourCursor._send('setMotion:', MoveTo, 147, 116, self)
			#end:case
			case 32:
				global91._send('say:', 0, 0, 1, 9, self)
			#end:case
			case 33:
				ourCursor._send('setMotion:', MoveTo, 187, 116, self)
			#end:case
			case 34:
				global91._send('say:', 0, 0, 1, 10, self)
			#end:case
			case 35:
				ourCursor._send('setMotion:', MoveTo, 227, 116, self)
			#end:case
			case 36:
				global91._send('say:', 0, 0, 1, 11, self)
			#end:case
			case 37:
				theControlPanel._send('dispose:')
				saveBut._send('dispose:')
				restoreBut._send('dispose:')
				restartBut._send('dispose:')
				quitBut._send('dispose:')
				aboutBut._send('dispose:')
				modeBut._send('dispose:')
				playBut._send('dispose:')
				cycles = 2
			#end:case
			case 38:
				local1 = 0
				client._send('setScript:', doneScript)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class doneScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global91._send('say:', 0, 0, 4, 1, self)
			#end:case
			case 1:
				global91._send('say:', 0, 0, 4, 2, self)
			#end:case
			case 2:
				global91._send('say:', 0, 0, 4, 3, self)
			#end:case
			case 3:
				global91._send('say:', 0, 0, 4, 4, self)
			#end:case
			case 4:
				ourCursor._send('hide:')
				seconds = 2
			#end:case
			case 5:
				restartCode._send('doit:', 1)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class objectGlitter(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				seconds = kernel.Random(5, 10)
			#end:case
			case 1:
				state = -1
				client._send('cel:', 0, 'setCycle:', End, self)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class takeRingScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				if (global0._send('loop:') != 1):
					global0._send('setHeading:', 315, self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				global0._send(
					'normal:', 0,
					'setSpeed:', 6,
					'view:', 201,
					'loop:', 4,
					'cel:', 0,
					'setScale:', 0,
					'setCycle:', End, self
				)
				royalRing._send('dispose:')
			#end:case
			case 3:
				global0._send(
					'posn:', royalRing._send('approachX:'), royalRing._send('approachY:'),
					'reset:', 7,
					'setScale:', Scaler, 100, 50, 112, 57,
					'get:', 39
				)
				cycles = 2
			#end:case
			case 4:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class ourCursor(Actor):
	#property vars (may be empty)
	x = 120
	y = 120
	view = 998
	cycleSpeed = 0
	moveSpeed = 0
	
	@classmethod
	def init():
		self._send('setLoop:', 1, 'setPri:', 15)
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class theWalkIcon(Actor):
	#property vars (may be empty)
	x = 4
	y = 7
	view = 980
	priority = 14
	signal = 4112
	
#end:class or instance

@SCI.instance
class theHandIcon(Actor):
	#property vars (may be empty)
	x = 47
	y = 7
	view = 980
	loop = 1
	priority = 14
	signal = 4112
	
#end:class or instance

@SCI.instance
class theLookIcon(Actor):
	#property vars (may be empty)
	x = 90
	y = 7
	view = 980
	loop = 2
	priority = 14
	signal = 4112
	
#end:class or instance

@SCI.instance
class theTalkIcon(Actor):
	#property vars (may be empty)
	x = 133
	y = 7
	view = 980
	loop = 3
	priority = 14
	signal = 4112
	
#end:class or instance

@SCI.instance
class theCurInvIcon(Actor):
	#property vars (may be empty)
	x = 176
	y = 7
	view = 980
	loop = 4
	priority = 14
	signal = 4112
	
#end:class or instance

@SCI.instance
class theCurInvIconMask(Actor):
	#property vars (may be empty)
	x = 176
	y = 7
	view = 980
	loop = 4
	cel = 1
	priority = 14
	signal = 4112
	
#end:class or instance

@SCI.instance
class theInvIcon(Actor):
	#property vars (may be empty)
	x = 238
	y = 7
	view = 980
	loop = 5
	priority = 14
	signal = 4112
	
#end:class or instance

@SCI.instance
class theControlIcon(Actor):
	#property vars (may be empty)
	x = 281
	y = 7
	view = 980
	loop = 6
	priority = 14
	signal = 4112
	
#end:class or instance

@SCI.instance
class royalRing(Prop):
	#property vars (may be empty)
	x = 104
	y = 134
	sightAngle = 45
	approachX = 134
	approachY = 136
	view = 202
	loop = 2
	
	@classmethod
	def init():
		self._send('cel:', 0, 'setCycle:', End, 'setScript:', kernel.Clone(objectGlitter))
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class theControlPanel(Actor):
	#property vars (may be empty)
	x = 58
	y = 20
	view = 1205
	priority = 15
	signal = 16
	
	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('addToPic:')
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:', &rest)
		kernel.DrawPic(global2._send('picture:'))
	#end:method

#end:class or instance

@SCI.instance
class saveBut(Actor):
	#property vars (may be empty)
	x = 76
	y = 36
	view = 947
	loop = 2
	priority = 15
	signal = 16
	
#end:class or instance

@SCI.instance
class restoreBut(Actor):
	#property vars (may be empty)
	x = 76
	y = 56
	view = 947
	loop = 3
	priority = 15
	signal = 16
	
#end:class or instance

@SCI.instance
class restartBut(Actor):
	#property vars (may be empty)
	x = 76
	y = 76
	view = 947
	loop = 4
	priority = 15
	signal = 16
	
#end:class or instance

@SCI.instance
class quitBut(Actor):
	#property vars (may be empty)
	x = 76
	y = 96
	view = 947
	loop = 5
	priority = 15
	signal = 16
	
#end:class or instance

@SCI.instance
class aboutBut(Actor):
	#property vars (may be empty)
	x = 76
	y = 116
	view = 947
	loop = 6
	priority = 15
	signal = 16
	
#end:class or instance

@SCI.instance
class modeBut(Actor):
	#property vars (may be empty)
	x = 161
	y = 136
	view = 947
	loop = 8
	priority = 15
	signal = 16
	
#end:class or instance

@SCI.instance
class playBut(Actor):
	#property vars (may be empty)
	x = 76
	y = 136
	view = 947
	loop = 7
	priority = 15
	signal = 16
	
#end:class or instance

@SCI.instance
class theInvWindow(Actor):
	#property vars (may be empty)
	x = 63
	y = 63
	view = 1205
	loop = 2
	priority = 15
	
#end:class or instance

@SCI.instance
class invEye(Actor):
	#property vars (may be empty)
	x = 86
	y = 121
	view = 901
	loop = 2
	priority = 15
	signal = 16
	
#end:class or instance

@SCI.instance
class invHand(Actor):
	#property vars (may be empty)
	x = 116
	y = 121
	view = 901
	priority = 15
	signal = 16
	
#end:class or instance

@SCI.instance
class invArrow(Actor):
	#property vars (may be empty)
	x = 145
	y = 121
	view = 901
	loop = 4
	priority = 15
	signal = 16
	
#end:class or instance

@SCI.instance
class invTalk(Actor):
	#property vars (may be empty)
	x = 174
	y = 121
	view = 901
	loop = 5
	priority = 15
	signal = 16
	
#end:class or instance

@SCI.instance
class invMore(Actor):
	#property vars (may be empty)
	x = 203
	y = 121
	view = 901
	loop = 6
	priority = 15
	signal = 16
	
#end:class or instance

@SCI.instance
class invOk(Actor):
	#property vars (may be empty)
	x = 232
	y = 121
	view = 901
	loop = 3
	priority = 15
	signal = 16
	
#end:class or instance

@SCI.instance
class Alex_Demo(Kq6Talker):
	#property vars (may be empty)
	name = r"""Alex Demo"""
	view = 1205
	loop = 1
	disposeWhenDone = 1
	
	@classmethod
	def init():
		if local1:
			if local0:
				self._send(
					'cel:', 1,
					'x:', 167,
					'y:', 75,
					'talkWidth:', 290,
					'textX:', -158,
					'textY:', -65,
					'keepWindow:', 0
				)
			else:
				self._send(
					'cel:', 1,
					'x:', 167,
					'y:', 75,
					'talkWidth:', 290,
					'textX:', -158,
					'textY:', 45,
					'keepWindow:', 0
				)
			#endif
			super._send('init:', 0, 0, 0, &rest)
		else:
			self._send(
				'cel:', 1,
				'x:', 167,
				'y:', 75,
				'talkWidth:', 290,
				'textX:', -158,
				'textY:', 32,
				'keepWindow:', 0
			)
			super._send('init:', 0, 0, tMouthA, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class tMouthA(Prop):
	#property vars (may be empty)
	view = 1205
	loop = 1
	
#end:class or instance

