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
def localproc_0(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	if param1:
		(global2
			addObstacle: (roomPoly type: 3 points: @local70 size: 16 yourself:)
		)
	else:
		(global2
			addObstacle: (roomPoly type: 3 points: @local102 size: 15 yourself:)
		)
	#endif
#end:procedure

@SCI.procedure
def proc270_7(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	if (shopOwner script:):
		(shopOwnerScr caller: param1)
		if ((shopOwnerScr state:) == 0):
			(shopOwnerScr dispose:)
		#endif
	else:
		(param1 cue:)
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
		argc = sum(v is not None for v in locals().values())

		(global2
			addObstacle:
				((Polygon new:)
					type: 2
					init: 231 124 247 129 197 136 180 132 180 123
					yourself:
				)
		)
		(super init: &rest)
		(global0 init: posn: 92 144 reset: 0 setScale: Scaler 108 83 170 113)
		(global32
			add:
				genericFeatures
				poemShelf
				clownChair
				readingTable
				bookStand
				shelfFeatures
				frontCounter
			eachElementDo: #init
		)
		(fire setCycle: Fwd init:)
		(shopDoor init: setCycle: Beg shopDoor)
		if (((global9 at: 45) owner:) == global11):
			(spellBook init:)
		#endif
		if (not proc999_5(((global9 at: 1) owner:), global0, -1)):
			(kernel.ScriptID(273, 0) init:)
		#endif
		(shopOwner init:)
		if (not proc913_0(27)):
			proc913_2(54)
			proc913_1(53)
		#endif
		(cond
			case (not proc913_0(16)):
				proc913_1(27)
				(kernel.ScriptID(271, 0) init:)
				local132 = 1
				(clownBook init:)
			#end:case
			case 
				(and
					proc913_0(16)
					(global153 == 1)
					(not proc913_0(26))
					proc913_0(54)
				):
				proc913_1(26)
				(kernel.ScriptID(274, 0) init:)
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
				(kernel.ScriptID(274, 0) init:)
				if (proc913_0(10) and proc999_5(global153, 3, 4)):
					(global2 setScript: kernel.ScriptID(277, 1))
				#endif
			#end:case
			else:
				(clownBook init:)
			#end:else
		)
		if (not (global2 script:)):
			if (not (kernel.ScriptID(10, 0) isSet: 64)):
				(kernel.ScriptID(10, 0) setIt: 64)
				(global2 setScript: ownerFromCounterScr)
			else:
				(global2 setScript: ownerNotAtCounterScr)
			#endif
		#endif
		if (not (global5 contains: clownBook)):
			(global102 number: 780 loop: -1 play:)
		#endif
		proc913_1(27)
		if (not (global2 script:)):
			(global1 handsOn:)
		#endif
		(localproc_0 local132)
	#end:method

	@classmethod
	def scriptCheck(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 1
		if (kernel.ScriptID(10, 0) isSet: 2):
			(kernel.ScriptID(10, 0) clrIt: 2)
		#endif
		match param1
			case 87:
				(global91 say: 0 0 14 0 0 899)
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
		argc = sum(v is not None for v in locals().values())

		if ((global102 number:) == 240):
			(kernel.ScriptID(10, 0) setIt: 512)
			(global102 fade: 127 15 15 0)
		else:
			(global102 fade:)
		#endif
		(super dispose:)
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
		argc = sum(v is not None for v in locals().values())

		(super init:)
		(self setCycle: Walk)
	#end:method

#end:class or instance

@SCI.instance
class spiderScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

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
				(spider
					posn:
						proc999_6(local134, local133.post('++'))
						proc999_6(local134, local133.post('++'))
				)
				cycles = 2
			#end:case
			case 1:
				match temp0 = proc999_6(local134, local133.post('++'))
					case -4088:
						(spider setScale: 0)
					#end:case
					case -4095:
						(spider setLoop: proc999_6(local134, local133.post('++')))
						state.post('--')
						cycles = 1
					#end:case
					case -4094:
						(spider
							posn:
								proc999_6(local134, local133.post('++'))
								proc999_6(local134, local133.post('++'))
						)
						state.post('--')
						cycles = 1
					#end:case
					case -4092:
						state.post('++')
						ticks = 1
					#end:case
					else:
						(spider
							cycleSpeed: kernel.Random(3, 8)
							moveSpeed: kernel.Random(3, 8)
							setMotion:
								MoveTo
								temp0
								proc999_6(local134, local133.post('++'))
								self
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
				(spider hide:)
				seconds = kernel.Random(5, 20)
			#end:case
			case 4:
				(spider show:)
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
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				cycles = 2
			#end:case
			case 1:
				(global0 setHeading: 315 self)
				(proc270_7 self)
			#end:case
			case 2: 0#end:case
			case 3:
				if (not ((shopOwner y:) < 145)):
					(shopOwner view: 277 loop: 2 cel: 0 setCycle: End)
				#endif
				(global105 number: 901 loop: 1 play:)
				(shopDoor setCycle: End self)
			#end:case
			case 4:
				(shopDoor setPri: 15)
				(global0 setMotion: MoveTo 70 142 self)
			#end:case
			case 5:
				(global2 newRoom: 240)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class clownChairScr(CartoonScript):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					setSpeed: 6
					normal: 0
					posn: 205 133
					view: 2711
					loop: 0
					cel: 0
					scaleX: 128
					scaleY: 128
					setScale: 0
					setCycle: End self
				)
			#end:case
			case 1:
				(global91 say: 14 5 20 1 self)
			#end:case
			case 2:
				(KQ6Print
					font: global22
					modeless: 1
					ticks: 20
					posn: -1 10
					say: 0 14 5 20 2
					init: self
				)
				cycles = 1
			#end:case
			case 3:
				(global0 loop: 3 cel: 0 setCycle: CT 1 1 self)
			#end:case
			case 4:
				(clownBook dispose:)
				cycles = 2
			#end:case
			case 5:
				(global0 setCycle: End self)
			#end:case
			case 6:
				(global0 setSpeed: 6 loop: 1 cel: 0 setCycle: End self)
			#end:case
			case 7:
				seconds = 4
			#end:case
			case 8:
				(global0 cel: 0 setCycle: End self)
			#end:case
			case 9:
				seconds = 2
			#end:case
			case 10:
				if global25:
					(KQ6Print caller: self)
				else:
					(self cue:)
				#endif
			#end:case
			case 11:
				(global0 loop: 3 cel: 2 setCycle: CT 1 -1 self)
			#end:case
			case 12:
				(clownBook init:)
				cycles = 2
			#end:case
			case 13:
				(global0 setCycle: Beg self)
			#end:case
			case 14:
				(global0 loop: 2 cel: 0 setCycle: End self)
			#end:case
			case 15:
				(global0 reset: 4 posn: 207 133 setScale: Scaler 108 83 170 113)
				cycles = 2
			#end:case
			case 16:
				(global91 say: 14 5 20 3 self)
			#end:case
			case 17:
				kernel.UnLoad(128, 2711)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class randomConvScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(proc270_7 self)
			#end:case
			case 1:
				(global91 say: 18 2 23 1 self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				(global91 say: 18 2 24 kernel.Random(1, 5) self)
			#end:case
			case 4:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class boringBookDoScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(proc270_7 self)
			#end:case
			case 1:
				(global91 say: 18 42 0 1 self)
			#end:case
			case 2:
				(global91 say: 18 register 0 0 self)
			#end:case
			case 3:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class ownerNotAtCounterScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				cycles = 2
			#end:case
			case 1:
				if (shopDoor cycler:):
					((shopDoor cycler:) caller: self)
				else:
					(state += 2)
					(self cue:)
				#endif
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				(shopDoor stopUpd:)
				(global105 number: 902 loop: 1 play: self)
			#end:case
			case 4:
				(global91 say: 19 0 36 0 self)
			#end:case
			case 5:
				(shopOwner setScript: shopOwnerScr)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class ownerFromCounterScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(kernel.ScriptID(270, 2)
					view: 276
					loop: 0
					cel: 0
					setPri: 1
					posn: 290 134
				)
				cycles = 2
			#end:case
			case 1:
				if (shopDoor cycler:):
					((shopDoor cycler:) caller: self)
				else:
					(self cue:)
				#endif
			#end:case
			case 2:
				(global105 number: 902 loop: 1 play:)
				(kernel.ScriptID(270, 2) setCycle: End self)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				(global91 say: 18 2 25 1 self)
			#end:case
			case 5:
				ticks = 150
			#end:case
			case 6:
				(kernel.ScriptID(270, 2)
					posn: 290 138
					loop: 1
					cel: 0
					setPri: 8
					setCycle: End self
				)
			#end:case
			case 7:
				(kernel.ScriptID(270, 2)
					posn: 288 140
					loop: 2
					cel: 0
					setCycle: CT 2 1 self
				)
			#end:case
			case 8:
				(kernel.ScriptID(270, 2) setPri: 12 setCycle: End self)
			#end:case
			case 9:
				cycles = 2
			#end:case
			case 10:
				(kernel.ScriptID(270, 2)
					loop: 3
					cel: 0
					posn: 303 151
					setCycle: End self
				)
			#end:case
			case 11:
				cycles = 2
			#end:case
			case 12:
				(kernel.ScriptID(270, 2)
					view: 277
					loop: 2
					cel: 0
					setScript: shopOwnerScr
				)
				cycles = 2
			#end:case
			case 13:
				(global91 say: 18 2 25 2 self)
				cycles = 1
			#end:case
			case 14:
				kernel.UnLoad(128, 276)
				(kernel.ScriptID(270, 2) stopUpd:)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class shopOwnerScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				seconds = 10
			#end:case
			case 1:
				(shopOwner
					view: 277
					loop: 0
					cel: 0
					posn: 297 159
					setCycle: End self
				)
			#end:case
			case 2:
				ticks = 20
			#end:case
			case 3:
				(shopOwner loop: 1 cel: 0 setCycle: End self)
			#end:case
			case 4:
				ticks = 20
			#end:case
			case 5:
				(shopOwner cel: 0 setCycle: End self)
			#end:case
			case 6:
				ticks = 20
			#end:case
			case 7:
				(shopOwner setCycle: Beg self)
			#end:case
			case 8:
				(shopOwner loop: 1 cel: (shopOwner lastCel:) setCycle: Beg self)
			#end:case
			case 9:
				(shopOwner view: 277 loop: 2 cel: 0 posn: 303 151)
				cycles = 2
			#end:case
			case 10:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genericTalkScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(proc270_7 self)
			#end:case
			case 1:
				(global91 say: 18 2 register 0 self)
			#end:case
			case 2:
				(global1 handsOn:)
				(self dispose:)
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
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (kernel.ScriptID(10, 0) isSet: 2):
			(kernel.ScriptID(10, 0) clrIt: 2)
		#endif
		match param1
			case 2:
				(cond
					case (not proc913_0(64)):
						proc913_1(64)
						proc913_1(73)
						(global2 setScript: genericTalkScr 0 26)
					#end:case
					case ((not proc913_0(16)) and proc913_0(73)):
						(global1 givePoints: 1)
						proc913_1(16)
						proc913_2(54)
						proc913_1(53)
						(global2 setScript: kernel.ScriptID(276, 3))
					#end:case
					case (not proc913_0(16)):
						proc913_1(16)
						(global1 givePoints: 1)
						(global2 setScript: genericTalkScr 0 22)
					#end:case
					else:
						(global2 setScript: randomConvScr)
					#end:else
				)
			#end:case
			case 27:
				(global2 setScript: kernel.ScriptID(276, 1))
			#end:case
			else:
				if proc999_5(param1, 28, 32):
					(global2 setScript: boringBookDoScr 0 param1)
				else:
					if (param1 == 67):
						param1 = 63
					#endif
					(super doVerb: param1 &rest)
				#endif
			#end:else
		#end:match
	#end:method

	@classmethod
	def init(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 2 27)
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
		argc = sum(v is not None for v in locals().values())

		(self stopUpd:)
		(global105 number: 902 loop: 1 play:)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 5)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global2 setScript: exitShopScr)
			#end:case
			else:
				(super doVerb: param1 &rest)
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
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if temp0 = (super onMe: param1 &rest):
			if ((param1 message:) == 1):
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
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				if (((global9 at: 1) owner:) == global11):
					(global91 say: 2 1 4)
				else:
					(KQ6Print
						font: global22
						posn: -1 10
						say: 0 noun param1 4 1
						init:
					)
					(KQ6Print
						font: global22
						posn: -1 10
						say: 0 noun param1 3 1
						init:
					)
				#endif
			#end:case
			case 5:
				if (((global9 at: 1) owner:) != global11):
					(global91 say: noun param1 3)
				else:
					(global2 setScript: kernel.ScriptID(273, 1))
				#endif
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 1 5)
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
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global2 setScript: kernel.ScriptID(272, 0))
			#end:case
			else:
				if ((param1 == 2) or (not proc999_5(param1, 5, 1))):
					if (param1 != 2):
						param1 = 0
					#endif
					(global91 say: 4 param1)
				else:
					(super doVerb: param1 &rest)
				#endif
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 5 1)
	#end:method

#end:class or instance

@SCI.instance
class shelfFeatures(Feature):
	#property vars (may be empty)
	sightAngle = 40
	
	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if _approachVerbs:
			_approachVerbs = 0
		#endif
		(return
			(= noun
				match kernel.OnControl(4, (param1 x:), (param1 y:))
					case 512:
						x = 162
						y = 113
						approachX = 159
						approachY = 119
						(self approachVerbs: 5 1)
						4
					#end:case
					case 1024:
						x = 186
						y = 110
						approachX = 192
						approachY = 121
						(self approachVerbs: 5 1)
						20
					#end:case
					case 2048:
						x = 265
						y = 116
						approachX = 266
						approachY = 121
						(self approachVerbs: 5 1)
						16
					#end:case
					case 256:
						x = 134
						y = 118
						approachX = 142
						approachY = 121
						(self approachVerbs: 5 1)
						11
					#end:case
					else: 0#end:else
				#end:match
			)
		)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if ((param1 == 2) or (not proc999_5(param1, 5, 1))):
			noun = 4
			if (param1 != 2):
				param1 = 0
			#endif
		#endif
		(super doVerb: param1 &rest)
	#end:method

#end:class or instance

@SCI.instance
class genericFeatures(Feature):
	#property vars (may be empty)
	sightAngle = 40
	
	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			(= noun
				match kernel.OnControl(4, (param1 x:), (param1 y:))
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
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 == 1):
			(global91
				say: 5 1 (6 if (((global9 at: 45) owner:) == global11) else 5)
			)
		else:
			(super doVerb: param1 &rest)
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
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if temp0 = (super onMe: param1 &rest):
			temp1 = kernel.OnControl(4, (param1 x:), (param1 y:))
			(cond
				case (((param1 message:) == 5) and (temp1 == 16384)):
					temp0 = 0
				#end:case
				case 
					(and
						((param1 message:) == 5)
						(not (global5 contains: kernel.ScriptID(274, 0)))
						(temp1 == 8)
					):
					(self approachVerbs: 5)
				#end:case
				else:
					_approachVerbs = 0
				#end:else
			)
		#endif
		return temp0
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				if 
					(and
						(global5 contains: kernel.ScriptID(274, 0))
						(not (global5 contains: clownBook))
					)
					(global91 say: noun param1 19)
				else:
					(global2 setScript: clownChairScr)
				#endif
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 5)
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
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if temp0 = (super onMe: param1 &rest):
			if 
				(and
					(not (global5 contains: kernel.ScriptID(274, 0)))
					(((param1 message:) == 5) or ((param1 message:) == 1))
				)
				(self approachVerbs: 5 1)
				if ((param1 message:) == 5):
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
		argc = sum(v is not None for v in locals().values())

		(readingTable doVerb: &rest)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 1)
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
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if temp0 = (super onMe: param1 &rest):
			if 
				(and
					(not (global5 contains: kernel.ScriptID(274, 0)))
					(((param1 message:) == 5) or ((param1 message:) == 1))
				)
				(self approachVerbs: 5 1)
				if ((param1 message:) == 5):
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
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				if (global5 contains: kernel.ScriptID(274, 0)):
					(global91 say: noun param1 37)
				else:
					(global91 say: noun param1 38)
				#endif
			#end:case
			else:
				(clownChair doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 1)
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
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				if proc913_0(7):
					(global91 say: noun param1 2)
				else:
					proc913_1(7)
					(global1 givePoints: 2)
					(global91 say: noun param1 1)
				#endif
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self
			approachX: (shopOwner approachX:)
			approachY: (shopOwner approachY:)
			approachVerbs: 5
		)
	#end:method

#end:class or instance

@SCI.instance
class roomPoly(Polygon):
	#property vars (may be empty)
#end:class or instance

