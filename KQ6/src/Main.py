#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 0
import sci_sh
import kernel
import Kq6IconBar
import Kq6Sound
import EgoGroop
import KQ6Print
import Interface
import KQ6Room
import Kq6Talker
import Kq6Window
import n913
import Body
import Print
import Dialog
import Messager
import Conversation
import Talker
import PseudoMouse
import Scaler
import RandCycle
import PolyPath
import Polygon
import Feature
import Timer
import Sound
import Game
import User
import System

# Public Export Declarations
SCI.public_exports(
	Kq6 = 0,
	proc0_1 = 1,
	proc0_2 = 2,
	emberTimer = 4,
	beastTimer = 5,
	CharonTimer = 6,
	lettuceTimer = 7,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
	; 0
global0 = None
global1 = None
global2 = None
global3 = None
global4 = None
	; 5
global5 = None
global6 = None
global7 = None
global8 = None
global9 = None
	; 10
global10 = None
global11 = None
global12 = None
global13 = None
global14 = None
	; 15
global15 = None
global16 = None
global17 = None
global18 = None
global19 = None
	; 20
global20 = 999
global21 = 997
global22 = 1
global23 = 4
global24 = None
	; 25
global25 = None
global26 = 1
global27 = None
global28 = None
global29 = None
	; 30
global30 = None
global31 = None
global32 = None
global33 = None
global34 = None
	; 35
global35 = None
global36 = -1
global37 = None
global38 = None
global39 = None
	; 40
global40 = None
global41 = None
global42 = None
global43 = None
global44 = None
	; 45
global45 = None
global46 = None
global47 = None
global48 = None
global49 = None
	; 50
global50 = None
global51 = None
global52 = None
global53 = None
global54 = None
	; 55
global55 = None
global56 = None
global57 = None
global58 = None
global59 = None
	; 60
global60 = None
global61 = None
global62 = None
global63 = None
global64 = None
	; 65
global65 = None
global66 = None
global67 = 1
global68 = None
global69 = None
	; 70
global70 = None
global71 = None
global72 = None
global73 = None
global74 = None
	; 75
global75 = None
global76 = None
global77 = None
global78 = None
global79 = 60
	; 80
global80 = None
global81 = None
global82 = None
global83 = None
global84 = None
	; 85
global85 = None
global86 = None
global87 = None
global88 = None
global89 = None
	; 90
global90 = 1
global91 = None
global92 = None
global93 = None
global94 = 2
	; 95
global95 = None
global96 = None
global97 = None
global98 = None
global99 = None
	; 100
global100 = None
global101 = 1234
global102 = None
global103 = None
global104 = None
	; 105
global105 = None
global106 = None
global107 = None
global108 = None
global109 = None
	; 110
global110 = None
global111 = None
global112 = None
global113 = None
global114 = None
	; 115
global115 = None
global116 = None
global117 = None
global118 = None
global119 = None
	; 120
global120 = None
global121 = None
global122 = None
global123 = None
global124 = None
	; 125
global125 = None
global126 = None
global127 = None
global128 = None
global129 = None
	; 130
global130 = None
global131 = None
global132 = None
global133 = None
global134 = None
	; 135
global135 = None
global136 = None
global137 = None
global138 = None
global139 = None
	; 140
global140 = None
global141 = None
global142 = None
global143 = None
global144 = None
	; 145
global145 = None
global146 = None
global147 = None
global148 = None
global149 = None
	; 150
global150 = None
global151 = None
global152 = None
global153 = None
global154 = None
	; 155
global155 = None
global156 = None
global157 = None
global158 = None
global159 = None
	; 160
global160 = None
global161 = None
global162 = None
global163 = None
global164 = None
	; 165
global165 = None
global166 = None
global167 = None
global168 = None
global169 = None
	; 170
global170 = None


@SCI.procedure
def proc0_1(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	global160 = param1
	proc913_1(44)
	(global2 newRoom: 640)
#end:procedure

@SCI.procedure
def proc0_2(param1 = None, param2 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	if (param1 < 0):
		param1 = 0
	#endif
	if (param1 > 255):
		param1 = 255
	#endif
	if (param2 < 0):
		param2 = 0
	#endif
	if (param2 > 15):
		param2 = 15
	#endif
	return (param1 if (global107 >= 32) else param2)
#end:procedure

class Kq6Points(Kq6Sound):
	#property vars (may be empty)
	@classmethod
	def check():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super check: &rest)
		if (prevSignal == -1):
			(self dispose:)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class ego(Body):
	#property vars (may be empty)
	noun = 1
	modNum = 0
	sightAngle = 45
	view = 900
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		(scaleSignal |= 0x0004)
		(state |= 0x0002)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((param1 type:) & 0x0040):
			return 0
		else:
			(super handleEvent: param1 &rest)
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 19:
				(global2 setScript: 908)
			#end:case
			case 14:
				if ((global11 != 280) and proc913_0(153)):
					(global91 say: 1 14 18 0 0 0)
				else:
					(global2 setScript: 87)
				#endif
			#end:case
			case 31:
				(global2 setScript: 85)
			#end:case
			case 42:
				(global2 setScript: 88)
			#end:case
			case 27:
				(global2 setScript: 90)
			#end:case
			case 83:
				if proc913_0(151):
					(global91 say: 1 83 17 0 0 0)
				else:
					(global2 setScript: 92)
				#endif
			#end:case
			case 37:
				(global2 setScript: 93)
			#end:case
			case 28:
				(global2 setScript: 190)
			#end:case
			case 32:
				if (global2 script:):
					(global91 say: 7 0 16 0 0 0)
				else:
					(global2 setScript: 97)
				#endif
			#end:case
			case 65:
				if (global2 script:):
					(global91 say: 7 0 16 0 0 0)
				else:
					(global2 setScript: 96)
				#endif
			#end:case
			case 61:
				if (global2 script:):
					(global91 say: 7 0 16 0 0 0)
				else:
					(global2 setScript: 101)
				#endif
			#end:case
			case 67:
				(global0 put: 31 0)
				(global91 say: noun param1 0 1 0 0)
			#end:case
			case 24:
				(global0 put: 40 0)
				(global91 say: noun param1 0 1 0 0)
			#end:case
			case 62:
				(global0 put: 22 470)
				(global91 say: noun param1 0 1 0 0)
			#end:case
			case 63:
				(global0 put: 23 280)
				(global91 say: noun param1 0 1 0 0)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

class NewSound(Sound):
	#property vars (may be empty)
	flags = 1
	newPiece = 0
	newLoop = 0
	fadeTicks = 15
	fadeStep = 10
	volSwitch = 50
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		prevSignal = -1
	#end:method

	@classmethod
	def fadeTo(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		newLoop = 0
		if (argc and (argc >= 1)):
			newPiece = param1[0]
			if (argc >= 2):
				newLoop = param1[1]
			#endif
		#endif
		if (prevSignal == -1):
			(self cue:)
		else:
			(self client: self fade: volSwitch fadeTicks fadeStep 1)
		#endif
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (prevSignal == -1):
			(self
				number: newPiece
				loop: newLoop
				play: volSwitch
				fade: 127 fadeTicks fadeStep 0
			)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class globalSound(NewSound):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class globalSound2(Kq6Sound):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class globalSound3(Kq6Sound):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class globalSound4(Kq6Sound):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class kq6KeyDownHandler(EventHandler):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class kq6MouseDownHandler(EventHandler):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class kq6DirectionHandler(EventHandler):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class kq6WalkHandler(EventHandler):
	#property vars (may be empty)
#end:class or instance

class Kq6(Game):
	#property vars (may be empty)
	isHandsOn = 1
	oldCurIcon = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.ScriptID(982)
		DText
		DButton
		Polygon
		PolyPath
		KQ6Room
		Kq6Talker
		Talker
		RandCycle
		Conversation
		Scaler
		(super init: &rest)
		(global7
			add:
				(emberTimer client: emberTimer yourself:)
				(beastTimer client: beastTimer yourself:)
				(CharonTimer client: CharonTimer yourself:)
				(lettuceTimer client: lettuceTimer yourself:)
		)
		if (kernel.FileIO(10, r"""KQ6CD""") and kernel.DoAudio(9)):
			global90 = 2
			kernel.DoAudio(7, 22050)
		else:
			global90 = 1
		#endif
		global107 = kernel.Graph(2)
		global38 = Kq6Window
		global19 = theGameCursor
		global21 = theWaitCursor
		global20 = arrowCursor
		global22 = 4
		(self setCursor: (global21 posn: 300 180 yourself:))
		global89 = Kq6Narrator
		global91 = Kq6Messager
		(kernel.ScriptID(902) init:)
		kernel.DisposeScript(902)
		global151 = EgoGroop
		global34 = 1
		kernel.StrCpy(@global42, r"""""")
		global65 = kq6DoVerbCode
		global64 = kq6FtrInit
		global66 = kq6ApproachCode
		(global72 = kq6KeyDownHandler add:)
		(global73 = kq6MouseDownHandler add:)
		(global74 = kq6DirectionHandler add:)
		(global93 = kq6WalkHandler add:)
		global77 = kq6PseudoMouse
		global0 = ego
		(User alterEgo: global0 canControl: 0 canInput: 0)
		(global102 = globalSound owner: self init:)
		(global103 = globalSound2 owner: self init:)
		(global104 = globalSound3 owner: self init:)
		(global105 = globalSound4 owner: self init:)
		global16 = 231
		global27 = r"""x.yyy.zzz"""
		kernel.Format(@temp0, 0, 0, 911)
		if kernel.FileIO(10, @temp0):
			global100 = 1
		else:
			global100 = 0
		#endif
		if ((kernel.Platform(4) == 2) and (global107 == 256)):
			global169 = 1
		#endif
		(global0 setSpeed: 6 currentSpeed: 6)
		global108 = kernel.DoSound(3)
		(global69 = Kq6IconBar
			add:
				(icon0 cursor: cIcon0 yourself:)
				(icon1 cursor: cIcon1 yourself:)
				(icon2 cursor: cIcon2 yourself:)
				(icon3 cursor: cIcon3 yourself:)
				icon4
				icon5
				icon6
			eachElementDo: #init
			eachElementDo: #highlightColor 0
			eachElementDo: #lowlightColor 53
			curIcon: icon0
			useIconItem: icon4
			walkIconItem: icon0
			disable: icon4
			disable:
		)
		(icon5 message: (3840 if kernel.HaveMouse() else 9))
		(kernel.ScriptID(907) init:)
		global136 = (200 if kernel.GameIsRestarting() else 100)
		global79 = 2
		kernel.Load(128, 998)
		kernel.Lock(128, 998, 1)
		(self newRoom: 99)
	#end:method

	@classmethod
	def setCursor(param1 = None, param2 = None, param3 = None, param4 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = global19
		global19 = param1
		if (argc > 2):
			temp1 = (0 if (param3 < 0) else param3)
			temp2 = (0 if (param4 < 0) else param4)
			kernel.SetCursor(temp1, temp2)
		#endif
		if kernel.IsObject(param1):
			if argc:
				(global19 = param1 init:)
			#endif
			(param1 init:)
		else:
			kernel.SetCursor(param1, 0, 0)
		#endif
		return temp0
	#end:method

	@classmethod
	def save():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((not proc913_0(49)) and (kernel.MemoryInfo(0) >= 1500)):
			(super save: &rest)
			(self
				setCursor:
					if ((global80 canControl:) or (global80 canInput:)):
						((global69 curIcon:) cursor:)
					else:
						global21
					#endif
			)
		else:
			(global91 say: 7 0 15 0 0 0)
		#endif
	#end:method

	@classmethod
	def restore():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((not proc913_0(49)) or (kernel.MemoryInfo(0) >= 1500)):
			(super restore: &rest)
			(self
				setCursor:
					(cond
						case ((global80 canControl:) or (global80 canInput:)):
							((global69 curIcon:) cursor:)
						#end:case
						case proc913_0(44): global20#end:case
						else: global21#end:else
					)
			)
		else:
			(global91 say: 7 0 15 0 0 0)
		#endif
	#end:method

	@classmethod
	def pragmaFail(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (User canInput:):
			temp0 = kernel.Random(1, 3)
			if ((global66 doit: param1) == -32768):
				param1 = 0
			#endif
			(global91 say: 0 param1 0 temp0 0 0)
		#endif
	#end:method

	@classmethod
	def refresh(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 and argc):
			if (global84 and (not ((global9 state:) & 0x0020))):
				kernel.Animate((global5 elements:), 0)
			#endif
		else:
			global170 = 1
		#endif
	#end:method

	@classmethod
	def quitGame():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if global25:
			(global25 dispose:)
		#endif
		if 
			(or
				((global11 == 640) and proc913_0(44))
				((global11 == 740) and (global90 == 2) and (global12 == 180))
			)
			kernel.DoAudio(10, 3)
			global4 = 1
		else:
			temp0 = (global1 setCursor: global20)
			if 
				(not
					(= global4
						(KQ6Print
							posn: 59 70
							font: 4
							addButton: 1 4 0 12 0 0 36 0
							addButton: 0 4 0 11 0 85 36 0
							font: 1
							say: 1 4 0 0 0 0 0 0
							init:
						)
					)
				)
				(global1 setCursor: temp0)
			#endif
		#endif
	#end:method

	@classmethod
	def restart(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if global25:
			(global25 dispose:)
		#endif
		if (not argc):
			temp1 = (global1 setCursor: global20)
			if 
				(= temp0
					(KQ6Print
						posn: 59 70
						font: 4
						addButton: 1 5 0 13 0 0 36 0
						addButton: 0 5 0 14 0 115 36 0
						font: 1
						say: 1 5 0 0 0 0 0 0
						init:
					)
				)
				(super restart: &rest)
			else:
				(global1 setCursor: temp1)
			#endif
		else:
			(super restart: &rest)
		#endif
	#end:method

	@classmethod
	def startRoom(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(= temp0
			if global169:
				kernel.Platform(6)
			#endif
		)
		if global77:
			(global77 stop:)
		#endif
		(kernel.ScriptID(919) doit: param1)
		if temp0:
			kernel.Portrait(2, 0)
		#endif
		if 
			(and
				global100
				(not proc913_0(38))
				(u> kernel.MemoryInfo(1) (10 + kernel.MemoryInfo(0)))
				((kernel.MemoryInfo(1) - 2) != kernel.MemoryInfo(0))
				match
					(Print
						font: global22
						addText: r"""*** Memory fragmented."""
						addButton: 0 r"""Who cares""" 0 20
						addButton: 1 r"""Debug""" 0 34
						init:
					)
					case 0:
						proc913_1(38)
					#end:case
					case 1:
						kernel.SetDebug()
					#end:case
				#end:match
			)
		#endif
		if global14:
			kernel.SetDebug()
		#endif
		(cond
			case proc999_5(param1, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290):
				kernel.ScriptID(10)
				(kernel.ScriptID(param1) setRegions: 10)
			#end:case
			case proc999_5(param1, 300, 310, 320, 330, 340, 350, 370, 380, 390):
				kernel.ScriptID(20)
				if proc999_5(param1, 300, 320):
					kernel.ScriptID(21)
					(kernel.ScriptID(param1) setRegions: 21)
				#endif
				(kernel.ScriptID(param1) setRegions: 20)
			#end:case
			case 
				proc999_5(param1, 400, 405, 410, 415, 420, 425, 430, 435, 440, 406, 407, 408, 409, 411):
				kernel.ScriptID(30)
				(kernel.ScriptID(param1) setRegions: 30)
			#end:case
			case proc999_5(param1, 450, 460, 461, 470, 475, 480, 490):
				kernel.ScriptID(40)
				(kernel.ScriptID(param1) setRegions: 40)
			#end:case
			case proc999_5(param1, 500, 510, 520, 530, 540):
				kernel.ScriptID(50)
				(kernel.ScriptID(param1) setRegions: 50)
			#end:case
			case proc999_5(param1, 550, 560, 570, 580):
				kernel.ScriptID(60)
				(kernel.ScriptID(param1) setRegions: 60)
			#end:case
			case proc999_5(param1, 600, 605, 615, 620, 630, 640, 650, 660, 670, 680, 690):
				kernel.ScriptID(70)
				(kernel.ScriptID(param1) setRegions: 70)
			#end:case
			case 
				proc999_5(param1, 700, 710, 720, 730, 740, 750, 760, 770, 780, 781, 790, 800, 810, 820, 840, 850, 860, 870, 880, 180, 743):
				kernel.ScriptID(80)
				if proc999_5(param1, 840, 710, 720, 770, 820, 780):
					kernel.ScriptID(81)
					(kernel.ScriptID(param1) setRegions: 81)
				#endif
				(kernel.ScriptID(param1) setRegions: 80)
			#end:case
			else: 0#end:else
		)
		(super startRoom: param1)
		(CueObj client: 0 state: 0)
		if ((global5 contains: global0) and (not (global0 looper:))):
			(global0 setLoop: EgoGroop)
		#endif
		if temp0:
			(kernel.ScriptID(109, 0) doit: param1)
		#endif
	#end:method

	@classmethod
	def handsOff():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		isHandsOn = 0
		if (not argc):
			(global0 setMotion: 0)
		#endif
		if (not oldCurIcon):
			oldCurIcon = (global69 curIcon:)
		#endif
		(global0 oldXStep: (global0 xStep:))
		(global0 oldYStep: (global0 yStep:))
		if 
			(and
				((global0 scaleSignal:) & 0x0003)
				(not (global0 oldScaleSignal:))
			)
			(global0 oldScaleSignal: ((global0 scaleSignal:) & 0xfffb))
			(cond
				case ((global0 oldScaleSignal:) & 0x0002):
					(global0 oldMaxScale: (global0 maxScale:))
				#end:case
				case kernel.IsObject((global0 scaler:)):
					(global0
						oldMaxScale: ((global0 scaler:) frontSize:)
						oldBackSize: ((global0 scaler:) backSize:)
						oldFrontY: ((global0 scaler:) frontY:)
						oldBackY: ((global0 scaler:) backY:)
					)
				#end:case
			)
		#endif
		(global69 disable: (global69 at: 0) icon1 icon2 icon3 icon4 icon5)
		(User canControl: 0 canInput: 0)
		(global1 setCursor: global21)
		if global77:
			(global77 stop:)
		#endif
	#end:method

	@classmethod
	def handsOn():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		isHandsOn = 1
		(User canControl: 1 canInput: 1)
		if kernel.IsObject(oldCurIcon):
			(global69 curIcon: oldCurIcon)
		#endif
		oldCurIcon = 0
		(global69 enable: (global69 at: 0) icon1 icon2 icon3 icon4 icon5)
		if (not (global69 curInvIcon:)):
			(global69 disable: icon4)
		#endif
		(global1 setCursor: ((global69 curIcon:) cursor:))
	#end:method

	@classmethod
	def givePoints(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global15 += param1)
		((Kq6Points new:) flags: 1 number: 900 play:)
	#end:method

	@classmethod
	def play():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global1 = self
		global29 = kernel.GetSaveDir()
		(self init:)
		while (not global4):

			(self doit:)
		#end:loop
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 claimed:):
			return 1
		#endif
		if global100:
			match (param1 type:)
				case 4:
					match (param1 message:)
						case 9:
							if (not ((icon5 signal:) & 0x0004)):
								(kernel.ScriptID(907, 1) init: global0)
								(param1 claimed: 1)
							#endif
						#end:case
						case 3840:
							if (not ((icon5 signal:) & 0x0004)):
								(kernel.ScriptID(907, 1) init: global0)
								(param1 claimed: 1)
							#endif
						#end:case
						case 17:
							(global1 quitGame:)
							(param1 claimed: 1)
						#end:case
						case 15360:
							(cond
								case (global1 masterVolume:):
									(self masterVolume: 0)
								#end:case
								case (global108 > 1):
									(self masterVolume: 15)
								#end:case
								else:
									(self masterVolume: 1)
								#end:else
							)
							(param1 claimed: 1)
						#end:case
						case 16128:
							(self save:)
							(param1 claimed: 1)
						#end:case
						case 16640:
							(self restore:)
							(param1 claimed: 1)
						#end:case
						case 17152:
							(self restart:)
							(param1 claimed: 1)
						#end:case
						else:
							(param1 claimed: 1)
							if 
								(and
									global100
									(not
										proc999_5(global11, 440, 450, 480, 270, 280, 470, 490, 670, 750, 740)
									)
								)
								(param1 claimed: 0)
								(kernel.ScriptID(911) handleEvent: param1)
								(kernel.ScriptID(911) dispose:)
								kernel.DisposeScript(911)
							#endif
						#end:else
					#end:match
				#end:case
			#end:match
		#endif
		(cond
			case (param1 claimed:): 1#end:case
			case (script and (script handleEvent: param1)): 1#end:case
			case ((param1 type:) & 0x4000):
				(self pragmaFail: (param1 message:))
			#end:case
		)
		(param1 claimed:)
	#end:method

	@classmethod
	def killSound(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (argc and param1):
			(global8 eachElementDo: #pause 1)
			global163 = global8
			(global8 = globalSounds add:)
		else:
			(globalSounds dispose:)
			global8 = global163
			global163 = 0
			(global8 eachElementDo: #pause 0)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class globalSounds(Sounds):
	#property vars (may be empty)
#end:class or instance

class Kq6Messager(Messager):
	#property vars (may be empty)
	@classmethod
	def findTalker(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(= temp0
				match param1
					case 21:
						kernel.ScriptID(1000, 21)
					#end:case
					case 2:
						kernel.ScriptID(1001, 2)
					#end:case
					case 87: global89#end:case
					case 62:
						kernel.ScriptID(1063, 62)
					#end:case
					case 20:
						kernel.ScriptID(1002, 20)
					#end:case
					case 56:
						kernel.ScriptID(1057, 56)
					#end:case
					case 17:
						kernel.ScriptID(1003, 17)
					#end:case
					case 33:
						kernel.ScriptID(1034, 33)
					#end:case
					case 43:
						kernel.ScriptID(1044, 43)
					#end:case
					case 77:
						kernel.ScriptID(1050, 77)
					#end:case
					case 82:
						kernel.ScriptID(1015, 6)
					#end:case
					case 88:
						kernel.ScriptID(1039, 71)
					#end:case
					case 71:
						kernel.ScriptID(1039, 71)
					#end:case
					case 48:
						kernel.ScriptID(1049, 48)
					#end:case
					case 46:
						kernel.ScriptID(1047, 46)
					#end:case
					case 11:
						kernel.ScriptID(1004, 11)
					#end:case
					case 28:
						kernel.ScriptID(1005, 28)
					#end:case
					case 93: global89#end:case
					case 4:
						kernel.ScriptID(1006, 4)
					#end:case
					case 57:
						kernel.ScriptID(1010, 57)
					#end:case
					case 73:
						kernel.ScriptID(1040, 73)
					#end:case
					case 9:
						kernel.ScriptID(1007, 9)
					#end:case
					case 79:
						kernel.ScriptID(1025, 79)
					#end:case
					case 45:
						kernel.ScriptID(1046, 45)
					#end:case
					case 69:
						kernel.ScriptID(1016, 69)
					#end:case
					case 83:
						kernel.ScriptID(1060, 83)
					#end:case
					case 59:
						kernel.ScriptID(1033, 59)
					#end:case
					case 60:
						kernel.ScriptID(1033, 60)
					#end:case
					case 23:
						kernel.ScriptID(1008, 23)
					#end:case
					case 58:
						kernel.ScriptID(1061, 58)
					#end:case
					case 14:
						kernel.ScriptID(1009, 14)
					#end:case
					case 15:
						kernel.ScriptID(1009, 15)
					#end:case
					case 27:
						kernel.ScriptID(1011, 27)
					#end:case
					case 32:
						kernel.ScriptID(1012, 32)
					#end:case
					case 55:
						kernel.ScriptID(1056, 55)
					#end:case
					case 29:
						kernel.ScriptID(1013, 29)
					#end:case
					case 34:
						kernel.ScriptID(1035, 34)
					#end:case
					case 30:
						kernel.ScriptID(1014, 30)
					#end:case
					case 36:
						kernel.ScriptID(1037, 36)
					#end:case
					case 94:
						kernel.ScriptID(1065, 94)
					#end:case
					case 8:
						kernel.ScriptID(1015, 8)
					#end:case
					case 6:
						kernel.ScriptID(1015, 6)
					#end:case
					case 7:
						kernel.ScriptID(1015, 7)
					#end:case
					case 1:
						kernel.ScriptID(1018, 1)
					#end:case
					case 22:
						kernel.ScriptID(1019, 22)
					#end:case
					case 26:
						kernel.ScriptID(1033, 26)
					#end:case
					case 38:
						kernel.ScriptID(1041, 38)
					#end:case
					case 5:
						kernel.ScriptID(1020, 5)
					#end:case
					case 16:
						kernel.ScriptID(1021, 16)
					#end:case
					case 78:
						kernel.ScriptID(1024, 78)
					#end:case
					case 3:
						kernel.ScriptID(1022, 3)
					#end:case
					case 40:
						kernel.ScriptID(1064, 40)
					#end:case
					case 99: global89#end:case
					case 80:
						kernel.ScriptID(1062, 80)
					#end:case
					case 19:
						kernel.ScriptID(1023, 19)
					#end:case
					case 44:
						kernel.ScriptID(1045, 44)
					#end:case
					case 35:
						kernel.ScriptID(1036, 35)
					#end:case
					case 97: -1#end:case
					case 42:
						kernel.ScriptID(1017, 42)
					#end:case
					case 13:
						kernel.ScriptID(1026, 13)
					#end:case
					case 10:
						kernel.ScriptID(1027, 10)
					#end:case
					case 75:
						kernel.ScriptID(1055, 75)
					#end:case
					case 95:
						kernel.ScriptID(1067, 95)
					#end:case
					case 53:
						kernel.ScriptID(490, 53)
					#end:case
					case 50:
						kernel.ScriptID(1051, 50)
					#end:case
					case 92: global89#end:case
					case 81:
						kernel.ScriptID(1015, 7)
					#end:case
					case 74:
						kernel.ScriptID(1031, 74)
					#end:case
					case 86:
						kernel.ScriptID(1028, 86)
					#end:case
					case 68:
						kernel.ScriptID(1037, 68)
					#end:case
					case 65:
						kernel.ScriptID(1037, 65)
					#end:case
					case 72:
						kernel.ScriptID(1042, 72)
					#end:case
					case 61:
						kernel.ScriptID(1037, 61)
					#end:case
					case 47:
						kernel.ScriptID(1048, 47)
					#end:case
					case 25:
						kernel.ScriptID(1059, 25)
					#end:case
					case 37:
						kernel.ScriptID(1038, 37)
					#end:case
					case 66:
						kernel.ScriptID(1037, 66)
					#end:case
					case 70:
						kernel.ScriptID(1051, 50)
					#end:case
					case 67:
						kernel.ScriptID(1037, 67)
					#end:case
					case 51:
						kernel.ScriptID(1052, 51)
					#end:case
					case 41: global89#end:case
					case 12:
						kernel.ScriptID(1066, 12)
					#end:case
					case 24:
						kernel.ScriptID(1029, 24)
					#end:case
					case 91: global89#end:case
					case 49:
						kernel.ScriptID(1058, 49)
					#end:case
					case 90: global89#end:case
					case 39:
						kernel.ScriptID(1043, 39)
					#end:case
					case 76:
						kernel.ScriptID(1055, 76)
					#end:case
					case 18:
						kernel.ScriptID(1030, 18)
					#end:case
					case 31:
						kernel.ScriptID(1030, 31)
					#end:case
					case 52:
						kernel.ScriptID(490, 52)
					#end:case
				#end:match
			)
			return
		else:
			(super findTalker: param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class kq6DoVerbCode(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case 
				(and
					((kq6ApproachCode doit: param1) == -32768)
					kernel.Message(0, (param2 modNum:), (param2 noun:), 0, 0, 1)
				):
				(global91 say: (param2 noun:) 0 0 0 0 (param2 modNum:))
			#end:case
			case (not (global2 doVerb: param1)):
				(global1 pragmaFail: param1)
			#end:case
		)
	#end:method

#end:class or instance

@SCI.instance
class kq6FtrInit(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((param1 sightAngle:) == 26505):
			(param1 sightAngle: 90)
		#endif
		if ((param1 actions:) == 26505):
			(param1 actions: 0)
		#endif
		if 
			(and
				((param1 onMeCheck:) != 26505)
				(not kernel.IsObject((param1 onMeCheck:)))
			)
			(param1 state: (| (param1 state:) 0x0004))
		#endif
	#end:method

#end:class or instance

@SCI.instance
class kq6ApproachCode(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			match param1
				case 1: 1#end:case
				case 2: 2#end:case
				case 3: 4#end:case
				case 5: 8#end:case
				else: -32768#end:else
			#end:match
		)
	#end:method

#end:class or instance

@SCI.instance
class kq6PseudoMouse(PseudoMouse):
	#property vars (may be empty)
	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((param1 type:) & 0x0040):
			temp0 = (global69 curIcon:)
			(global69 curIcon: 0)
			(super handleEvent: param1)
			(global69 curIcon: temp0)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class icon0(Kq6IconItem):
	#property vars (may be empty)
	loop = 0
	cel = 0
	type = 20480
	message = 3
	signal = 65
	maskCel = 2
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		maskView = view = 980
		(super init: &rest)
	#end:method

#end:class or instance

@SCI.instance
class icon1(Kq6IconItem):
	#property vars (may be empty)
	loop = 1
	cel = 0
	message = 5
	signal = 65
	maskLoop = 1
	maskCel = 2
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		maskView = view = 980
		(super init: &rest)
	#end:method

#end:class or instance

@SCI.instance
class icon2(Kq6IconItem):
	#property vars (may be empty)
	loop = 2
	cel = 0
	message = 1
	signal = 65
	maskLoop = 2
	maskCel = 2
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		maskView = view = 980
		(super init: &rest)
	#end:method

#end:class or instance

@SCI.instance
class icon3(Kq6IconItem):
	#property vars (may be empty)
	loop = 3
	cel = 0
	message = 2
	signal = 65
	maskLoop = 3
	maskCel = 2
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		maskView = view = 980
		(super init: &rest)
	#end:method

#end:class or instance

@SCI.instance
class icon4(Kq6IconItem):
	#property vars (may be empty)
	loop = 4
	cel = 0
	message = 0
	signal = 64
	maskLoop = 4
	maskCel = 2
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		maskView = view = 980
		(super init: &rest)
	#end:method

#end:class or instance

@SCI.instance
class icon5(Kq6IconItem):
	#property vars (may be empty)
	loop = 5
	cel = 0
	type = 0
	message = 0
	signal = 67
	maskLoop = 5
	maskCel = 2
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		maskView = view = 980
		(super init: &rest)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(kernel.ScriptID(907, 1) init: global0)
	#end:method

#end:class or instance

@SCI.instance
class icon6(Kq6IconItem):
	#property vars (may be empty)
	loop = 6
	cel = 0
	message = 0
	signal = 67
	maskLoop = 6
	maskCel = 2
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		maskView = view = 980
		(super init: &rest)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((Cursor hidden:) and (kernel.MemoryInfo(0) >= 1500)):
			(kernel.ScriptID(903) init: show: dispose:)
		else:
			(global91 say: 7 0 15 0 0 0)
		#endif
	#end:method

	@classmethod
	def select():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			if (super select: &rest):
				(global1 setCursor: global21)
				(global69 hide:)
				1
			else:
				0
			#endif
		)
	#end:method

#end:class or instance

@SCI.instance
class theGameCursor(Cursor):
	#property vars (may be empty)
	view = 998
	loop = 1
	cel = 7
	
#end:class or instance

@SCI.instance
class theWaitCursor(Cursor):
	#property vars (may be empty)
	view = 998
	loop = 1
	cel = 8
	
#end:class or instance

@SCI.instance
class cIcon0(Cursor):
	#property vars (may be empty)
	view = 998
	loop = 1
	
#end:class or instance

@SCI.instance
class cIcon1(Cursor):
	#property vars (may be empty)
	view = 998
	loop = 1
	cel = 2
	
#end:class or instance

@SCI.instance
class cIcon2(Cursor):
	#property vars (may be empty)
	view = 998
	loop = 1
	cel = 1
	
#end:class or instance

@SCI.instance
class cIcon3(Cursor):
	#property vars (may be empty)
	view = 998
	loop = 1
	cel = 3
	
#end:class or instance

@SCI.instance
class arrowCursor(Cursor):
	#property vars (may be empty)
	view = 998
	loop = 1
	cel = 7
	
#end:class or instance

@SCI.instance
class emberTimer(Timer):
	#property vars (may be empty)
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (client != self):
			(super doit: &rest)
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super dispose:)
		client = self
	#end:method

	@classmethod
	def delete():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not client):
			client = self
		#endif
		(super delete:)
	#end:method

#end:class or instance

@SCI.instance
class beastTimer(Timer):
	#property vars (may be empty)
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (client != self):
			(super doit: &rest)
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super dispose:)
		client = self
	#end:method

#end:class or instance

@SCI.instance
class CharonTimer(Timer):
	#property vars (may be empty)
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (client != self):
			(super doit: &rest)
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super dispose:)
		client = self
	#end:method

#end:class or instance

@SCI.instance
class lettuceTimer(Timer):
	#property vars (may be empty)
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (client != self):
			(super doit: &rest)
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super dispose:)
		client = self
	#end:method

	@classmethod
	def delete():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not client):
			client = self
		#endif
		(super delete:)
	#end:method

#end:class or instance

