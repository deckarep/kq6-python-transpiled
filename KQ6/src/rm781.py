#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 781
import sci_sh
import kernel
import Main
import rgCastle
import KQ6Print
import n913
import Inset
import Conversation
import Scaler
import Polygon
import Feature
import LoadMany
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm781 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.instance
class rm781(CastleRoom):
	#property vars (may be empty)
	noun = 3
	picture = 780
	style = 10
	vanishingX = 183
	vanishingY = 98
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		proc958_0(128, 787, 785, 786, 724, 726)
		(global0 init: setPri: 13 setScale: Scaler 118 70 190 140)
		(self
			addObstacle:
				((Polygon new:)
					type: 2
					init:
						-10
						-10
						329
						-10
						329
						179
						319
						179
						271
						154
						250
						154
						233
						143
						207
						143
						201
						147
						176
						147
						173
						142
						167
						142
						162
						147
						76
						147
						48
						162
						33
						162
						0
						177
						-10
						177
					yourself:
				)
		)
		(global32 add: trunk box rug chandelier eachElementDo: #init)
		(door cel: ((global12 == 850) * 4) init: stopUpd: approachVerbs: 5)
		(super init: &rest)
		(trunkLid init:)
		(boxLid init:)
		(candles init:)
		(doorFrame1ATP addToPic:)
		(doorFrame2ATP addToPic:)
		(fireplaceATP addToPic:)
		(fireplace setCycle: Fwd init:)
		(wardrobeDoor init:)
		(bedATP addToPic:)
		match global12
			case 810:
				(wardrobeDoor hide:)
				(self setScript: wardrobeEntrance)
			#end:case
			else:
				(self setScript: hallDoorEntrance)
			#end:else
		#end:match
		if (global0 scaler:):
			((global0 scaler:) doit:)
		#endif
		if (not script):
			(global1 handsOn:)
		#endif
		(global102 fadeTo: 150 -1)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (global0 onControl: 1)
		(cond
			case script: 0#end:case
			case (temp0 & 0x4000):
				(global2 newRoom: 850)
			#end:case
		)
		(super doit: &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(return
			match param1
				case 1:
					if (global0 has: 20):
						(global91 say: noun param1 5)
						1
					else:
						(global91 say: noun param1 4)
						1
					#endif
				#end:case
				else:
					(super doVerb: param1 &rest)
				#end:else
			#end:match
		)
	#end:method

	@classmethod
	def warnUser(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 2:
				if inset:
					(script next: they_reBack)
					(inset dispose:)
				else:
					(self setScript: they_reBack)
				#endif
			#end:case
			else:
				(super warnUser: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global0 setPri: -1)
		(super dispose:)
	#end:method

#end:class or instance

@SCI.instance
class hallDoorEntrance(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(door cel: 4 forceUpd:)
				(global0
					setPri: -1
					posn: 306 157
					setMotion: MoveTo (door approachX:) (door approachY:) self
				)
			#end:case
			case 1:
				(global0 setPri: 13)
				(door setCycle: Beg self)
			#end:case
			case 2:
				(global105 number: 902 loop: 1 play:)
				(door stopUpd:)
				if (kernel.ScriptID(80, 0) tstFlag: 709 1):
					(kernel.ScriptID(80, 0) clrFlag: 709 1)
					cycles = 10
				else:
					(global1 handsOn:)
					(self dispose:)
				#endif
			#end:case
			case 3:
				(global2 warnUser: 2)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class openTrunk(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				if 
					(and
						(not (kernel.ScriptID(80, 0) tstFlag: 711 4096))
						proc999_5(register, 64, 35)
					)
					(global1 givePoints: 1)
				#endif
				(global0
					normal: 0
					view: 787
					loop: 0
					cel: 0
					cycleSpeed: 8
					setScale: 0
					scaleX: 128
					scaleY: 128
					posn: 151 154
					setCycle: CT 3 1 self
				)
			#end:case
			case 1:
				if (kernel.ScriptID(80, 0) tstFlag: 711 4096):
					if proc999_5(register, 64, 35):
						state = 4
						(global91 say: 4 35 14 0 self)
					else:
						(global91 say: 4 5 14 0 self)
					#endif
				else:
					if (not proc999_5(register, 64, 35)):
						state = 4
					else:
						(global105 number: 781 loop: 1 play:)
					#endif
					(global91 say: 4 register 13 0 self)
				#endif
			#end:case
			case 2:
				(kernel.ScriptID(80, 0) setFlag: 711 4096)
				(trunkLid hide:)
				(global105 number: 904 loop: 1 play:)
				(global0 cel: 4 setCycle: End self)
			#end:case
			case 3:
				(global105 stop:)
				(global1 handsOn:)
				(global69 disable: 0 3 4 5)
				(global69 disable: 0)
				(chestInset init: self global2)
			#end:case
			case 4:
				(global105 number: 905 loop: 1 play:)
				(global0 setCycle: CT 3 -1 self)
			#end:case
			case 5:
				(trunkLid show:)
				(global105 stop:)
				(global0 setCycle: Beg self)
			#end:case
			case 6:
				(global1 handsOn:)
				(global0 reset: 1 setPri: 13 posn: 171 148)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class openEbonyBox(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91 say: 14 5 0 0 self)
			#end:case
			case 1:
				(global0
					normal: 0
					view: 787
					loop: 2
					cel: 0
					setScale: 0
					scaleX: 128
					scaleY: 128
					cycleSpeed: 8
					setCycle: CT 4 1 self
				)
			#end:case
			case 2:
				(global69 disable: 0)
				(ebonyBoxInset init: self global2)
				(global1 handsOn:)
				(global69 disable: 0 3 4 5)
			#end:case
			case 3:
				(global1 handsOff:)
				(global0 setCycle: End self)
			#end:case
			case 4:
				(global0
					reset: 6
					setPri: 13
					posn: (box approachX:) (box approachY:)
				)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class wardrobeEntrance(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global103 number: 783 loop: 1 play:)
				(global0
					normal: 0
					view: 785
					loop: 2
					cel: 9
					posn: 58 162
					cycleSpeed: 8
					setScale: 0
					scaleX: 128
					scaleY: 128
					setCycle: Beg self
				)
				(global105 number: 901 loop: 1 play:)
			#end:case
			case 1:
				(global0 loop: 1 cel: 5 setCycle: CT 2 -1 self)
			#end:case
			case 2:
				(global0 setCycle: Beg)
				(global105 number: 902 loop: 1 play:)
				ticks = 60
			#end:case
			case 3:
				(global0
					posn: (wardrobeDoor approachX:) (wardrobeDoor approachY:)
					reset: 0
					setPri: 13
				)
				(wardrobeDoor show: stopUpd:)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class they_reBack(Script):
	#property vars (may be empty)
	name = r"""they'reBack"""
	
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91 say: 1 0 3 1 self)
			#end:case
			case 1:
				proc913_4(global0, door, self)
			#end:case
			case 2:
				(global105 number: 901 loop: 1 play:)
				(door setCycle: CT 2 1 self)
			#end:case
			case 3:
				(global105 stop:)
				(global91 say: 1 0 3 2 self)
			#end:case
			case 4:
				(global105 number: 901 loop: 1 play:)
				(door setCycle: End self)
			#end:case
			case 5:
				(global105 stop:)
				(kernel.ScriptID(80, 5) init: posn: 307 158 loop: 1)
				(kernel.ScriptID(80, 0) setupGuards:)
				(kernel.ScriptID(80, 5) setMotion: MoveTo 283 158 self)
			#end:case
			case 6:
				(global102 number: 710 loop: -1 play:)
				(global91 say: 1 0 3 3 self oneOnly: 0)
			#end:case
			case 7:
				(global102 fade:)
				(kernel.ScriptID(80, 0) setFlag: 709 8192)
				(global2 newRoom: 820)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class openWardrobe(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not local1):
			match state = param1
				case 0:
					(global1 handsOff:)
					(wardrobeDoor hide:)
					(global0
						normal: 0
						view: 785
						setScale: 0
						scaleX: 128
						scaleY: 128
						loop: 1
						cel: 0
						posn: 58 162
						cycleSpeed: 8
						setCycle: CT 2 1 self
					)
				#end:case
				case 1:
					(global103 number: 901 loop: 1 play:)
					(global0 setCycle: End self)
				#end:case
				case 2:
					if (global12 != 810):
						(global91 say: 12 5 8 0 self)
					else:
						(state += 2)
						cycles = 1
					#endif
				#end:case
				case 3:
					(global0 setCycle: CT 1 -1 self)
				#end:case
				case 4:
					local1 = 1
					(global0 cel: 0)
					(global105 number: 902 loop: 1 play: self)
				#end:case
				case 5:
					(global103 number: 783 loop: 1 play:)
					(global0 loop: 2 cel: 0 setCycle: CT 8 1 self)
				#end:case
				case 6:
					(global0 cel: 9)
					(global105 number: 902 loop: 1 play:)
					cycles = 2
				#end:case
				case 7:
					(global91 say: 12 5 9 0 self)
				#end:case
				case 8:
					(global2 newRoom: 810)
				#end:case
			#end:match
		else:
			local1 = 0
			(global1 handsOn:)
			(wardrobeDoor show: stopUpd:)
			(global0
				posn: (wardrobeDoor approachX:) (wardrobeDoor approachY:)
				reset: 1
				setPri: 13
			)
			(self dispose:)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class door(Prop):
	#property vars (may be empty)
	x = 298
	y = 161
	noun = 10
	sightAngle = 40
	approachX = 265
	approachY = 157
	view = 786
	loop = 1
	priority = 1
	signal = 16400
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global1 handsOff:)
				(global0 setPri: -1)
				(global105 number: 901 loop: 1 play:)
				(self setCycle: End self)
			#end:case
			case 1:
				if local0:
					(global91 say: noun param1 12)
					(global2 setScript: kernel.ScriptID(82) 0 hallScr)
				else:
					local0.post('++')
					(_approachVerbs |= (global66 doit: 1))
					(global91 say: noun param1 11)
				#endif
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global105 stop:)
		proc80_2(2)
	#end:method

#end:class or instance

@SCI.instance
class hallScr(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if register = (not (kernel.ScriptID(80, 0) tstFlag: 709 128)):
			(tempGuard1
				view: (kernel.ScriptID(80, 6) view:)
				posn: 192 126
				setSpeed: (3 if (global87 < 2) else 5)
				init:
			)
			(tempGuard2
				posn: 200 128
				setSpeed: (3 if (global87 < 2) else 5)
				init:
			)
		#endif
		(super init: &rest)
		(client caller: self)
		(kernel.ScriptID(82, 1) noun: 26 actions: keyHoleDoVerb init: 786 0 0 91 59)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if register:
			(tempGuard1 dispose:)
			(tempGuard2 dispose:)
		#endif
		(super dispose:)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if client:
			(super cue: &rest)
		else:
			(global0 setPri: 13)
		#endif
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				if register:
					if ((tempGuard1 x:) < 160):
						(tempGuard1 setMotion: MoveTo 192 126 self)
						(tempGuard2 setMotion: MoveTo 200 128)
					else:
						(kernel.ScriptID(80, 0) setFlag: 711 128)
						(tempGuard1 setMotion: MoveTo 128 126 self)
						(tempGuard2 setMotion: MoveTo 120 128)
					#endif
				else:
					cycles = 4
				#endif
			#end:case
			case 1:
				if register:
					if ((tempGuard1 x:) < 160):
						seconds = 4
					else:
						seconds = 10
					#endif
				#endif
			#end:case
			case 2:
				(kernel.ScriptID(80, 0) clrFlag: 711 128)
				(self changeState: 0)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class keyHoleDoVerb(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = 1
		match param1
			case 1:
				if (kernel.ScriptID(80, 0) tstFlag: 709 128):
					(global91 say: 26 1 8)
				else:
					(global91 say: 26 1 9)
				#endif
			#end:case
			else:
				temp0 = 0
			#end:else
		#end:match
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class tempGuard1(Actor):
	#property vars (may be empty)
	noun = 26
	sightAngle = 180
	loop = 4
	priority = 14
	signal = 16400
	scaleSignal = 1
	scaleX = 121
	scaleY = 121
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self setCycle: Walk setStep: 4 2 actions: keyHoleDoVerb)
	#end:method

#end:class or instance

@SCI.instance
class tempGuard2(Actor):
	#property vars (may be empty)
	noun = 26
	sightAngle = 180
	view = 724
	loop = 4
	cel = 1
	priority = 14
	signal = 16400
	scaleSignal = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self setCycle: Walk setStep: 4 2 actions: keyHoleDoVerb)
	#end:method

#end:class or instance

@SCI.instance
class doorJam(View):
	#property vars (may be empty)
	x = 298
	y = 161
	onMeCheck = 0
	view = 786
	loop = 8
	cel = 3
	
#end:class or instance

@SCI.instance
class wardrobeDoor(Prop):
	#property vars (may be empty)
	x = 40
	y = 116
	noun = 12
	approachX = 55
	approachY = 161
	view = 785
	loop = 3
	priority = 12
	signal = 16401
	
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

		if (param1 == 5):
			(global2 setScript: openWardrobe)
		else:
			(super doVerb: param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class trunkLid(Prop):
	#property vars (may be empty)
	x = 137
	y = 134
	noun = 4
	sightAngle = 40
	approachX = 166
	approachY = 149
	view = 787
	loop = 3
	priority = 12
	signal = 20496
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 5 35 64)
	#end:method

	@classmethod
	def doVerb():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(trunk doVerb: &rest)
	#end:method

#end:class or instance

@SCI.instance
class boxLid(Prop):
	#property vars (may be empty)
	x = 189
	y = 127
	sightAngle = 40
	onMeCheck = 0
	view = 787
	loop = 4
	signal = 20480
	
#end:class or instance

@SCI.instance
class candles(Prop):
	#property vars (may be empty)
	x = 165
	y = 84
	noun = 25
	view = 785
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self setCycle: Fwd)
		(super init: &rest)
	#end:method

#end:class or instance

@SCI.instance
class doorFrame1ATP(View):
	#property vars (may be empty)
	x = 298
	y = 160
	onMeCheck = 0
	view = 786
	loop = 8
	cel = 2
	signal = 20496
	
#end:class or instance

@SCI.instance
class doorFrame2ATP(View):
	#property vars (may be empty)
	x = 298
	y = 160
	onMeCheck = 0
	view = 786
	loop = 8
	cel = 3
	signal = 16384
	
#end:class or instance

@SCI.instance
class bedATP(View):
	#property vars (may be empty)
	x = 21
	y = 100
	sightAngle = 180
	view = 786
	loop = 8
	priority = 12
	signal = 20496
	
	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (param1 x:)
		temp1 = (param1 y:)
		approachY = approachX = _approachVerbs = 0
		(return
			(and
				(super onMe: temp0 temp1)
				(temp0 -= nsLeft)
				(temp1 -= nsTop)
				(or
					(and
						(temp0 > 41)
						(or
							(and
								((global69 curIcon:) == (global69 at: 1))
								(_approachVerbs |= (global66 doit: 5))
								approachX = 105
								approachY = 150
							)
							1
						)
						noun = 21
					)
					(self approachX: 55 approachY: 161 approachVerbs: 5)
					noun = 12
				)
			)
		)
	#end:method

	@classmethod
	def doVerb():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (noun == 12):
			(wardrobeDoor doVerb: &rest)
		else:
			(super doVerb: &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class fireplaceATP(View):
	#property vars (may be empty)
	x = 224
	y = 126
	view = 786
	loop = 8
	cel = 1
	signal = 20496
	
	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (param1 x:)
		temp1 = (param1 y:)
		(return
			(and
				(super onMe: temp0 temp1)
				(temp0 -= nsLeft)
				(temp1 -= nsTop)
				(or
					(and (<= 0 temp0 26) (<= 30 temp1 51) noun = 20)
					(and (<= 63 temp0 98) (<= 44 temp1 60) noun = 24)
					noun = 23
				)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class fireplace(Prop):
	#property vars (may be empty)
	x = 225
	y = 117
	heading = 180
	noun = 23
	sightAngle = 40
	view = 786
	loop = 9
	priority = 1
	signal = 16400
	cycleSpeed = 8
	detailLevel = 2
	
#end:class or instance

@SCI.instance
class trunk(Feature):
	#property vars (may be empty)
	x = 153
	y = 145
	z = 8
	noun = 4
	nsTop = 132
	nsLeft = 138
	nsBottom = 146
	nsRight = 156
	sightAngle = 40
	approachX = 166
	approachY = 149
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 5 35 64)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case proc999_5(param1, 5, 35, 64):
				(global2 setScript: openTrunk 0 param1)
			#end:case
			case ((global66 doit: param1) == -32768):
				match param1
					case 61:
						(super doVerb: param1)
					#end:case
					else:
						if (kernel.ScriptID(80, 0) tstFlag: 711 4096):
							(global91 say: noun 0 14)
						else:
							(global91 say: noun 0 13)
						#endif
					#end:else
				#end:match
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class box(Feature):
	#property vars (may be empty)
	x = 191
	y = 144
	z = 19
	heading = 180
	noun = 14
	nsTop = 122
	nsLeft = 183
	nsBottom = 128
	nsRight = 199
	sightAngle = 40
	approachX = 179
	approachY = 150
	
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
				(global2 setScript: openEbonyBox)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class rug(Feature):
	#property vars (may be empty)
	noun = 22
	onMeCheck = 2
	
#end:class or instance

@SCI.instance
class chandelier(Feature):
	#property vars (may be empty)
	noun = 25
	onMeCheck = 4
	
#end:class or instance

@SCI.instance
class chestInset(Inset):
	#property vars (may be empty)
	view = 7861
	priority = 13
	disposeNotOnMe = 1
	noun = 8
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global69 disable: 6)
		(global0 setPri: 0 stopUpd:)
		x = (160 - (kernel.CelWide(view, loop, cel) / 2))
		y = (90 - (kernel.CelHigh(view, loop, cel) / 2))
		(super init: &rest)
		(papers_ChestInset init: self)
		(books_ChestInset init: self)
		(vase_ChestInset init: self)
		(lid_ChestInset init: self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global69 enable: 6)
		if (caller == openTrunk):
			(global1 handsOff:)
		#endif
		(super dispose:)
		(global0 setPri: 13 startUpd:)
	#end:method

#end:class or instance

@SCI.instance
class ebonyBoxInset(Inset):
	#property vars (may be empty)
	view = 7862
	disposeNotOnMe = 1
	noun = 15
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global69 disable: 6)
		(global0 stopUpd:)
		x = (160 - (kernel.CelWide(view, loop, cel) / 2))
		y = (90 - (kernel.CelHigh(view, loop, cel) / 2))
		(super init: &rest)
		(global105 number: 904 play:)
		(paper_BoxInset init: self)
		(pens_BoxInset init: self)
		(dice_BoxInset init: self)
		(lid_BoxInset cel: 1 init: self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global69 enable: 6)
		(super dispose: &rest)
	#end:method

	@classmethod
	def handleEvent(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(cond
			case (inset and (inset handleEvent: param1)): 0#end:case
			case ((param1 type:) & 0x4000):
				(cond
					case (self onMe: param1):
						(param1 claimed: 1)
						(self doVerb: (param1 message:))
					#end:case
					case disposeNotOnMe:
						(param1 claimed: 1)
						(lid_BoxInset doVerb: 5)
					#end:case
					else:
						return 0
					#end:else
				)
			#end:case
		)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 2:
				(global91 say: 14 param1)
			#end:case
			else:
				if ((global66 doit: param1) == -32768):
					(global91 say: 14)
				else:
					(super doVerb: param1)
				#endif
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class letterInset(Inset):
	#property vars (may be empty)
	view = 7863
	priority = 15
	disposeNotOnMe = 1
	noun = 15
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global69 disable: 6)
		x = (160 - (kernel.CelWide(view, loop, cel) / 2))
		y = (100 - (kernel.CelHigh(view, loop, cel) / 2))
		(super init: &rest)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global69 enable: 6)
		(super dispose:)
	#end:method

#end:class or instance

class InsetView(View):
	#property vars (may be empty)
	sightAngle = 180
	priority = 15
	signal = 20497
	offsetX = 0
	offsetY = 0
	
	@classmethod
	def init(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		x = ((param1 x:) + offsetX)
		y = ((param1 y:) + offsetY)
		(super init: &rest)
		(self stopUpd:)
	#end:method

#end:class or instance

@SCI.instance
class papers_ChestInset(InsetView):
	#property vars (may be empty)
	noun = 5
	view = 7861
	cel = 1
	offsetX = 64
	offsetY = 50
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				if (global0 has: 20):
					temp0 = 7
				else:
					temp0 = 6
				#endif
				(global91 say: noun param1 temp0)
			#end:case
			case 5:
				if (not (global0 has: 20)):
					(global0 get: 20)
					(global1 givePoints: 1)
					(openTrunk next: viewLetter)
					(chestInset dispose:)
				else:
					(global91 say: noun param1 7)
				#endif
			#end:case
			case 61:
				(global91 say: 4 61)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class viewLetter(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91 say: 5 5 6 1 self)
			#end:case
			case 1:
				(letterInset init: 0 global2)
				cycles = 2
			#end:case
			case 2:
				(roomConv
					add: -1 5 5 6 2
					add: -1 5 5 6 3
					add: -1 5 5 6 4
					add: -1 5 5 6 5
					init: self
				)
			#end:case
			case 3:
				(letterInset caller: self dispose:)
			#end:case
			case 4:
				cycles = 2
			#end:case
			case 5:
				(global91 say: 5 5 6 6 self oneOnly: 0)
			#end:case
			case 6:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class books_ChestInset(InsetView):
	#property vars (may be empty)
	noun = 6
	view = 7861
	cel = 2
	offsetX = 81
	offsetY = 42
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 2:
				(papers_ChestInset doVerb: param1)
			#end:case
			case 61:
				(global91 say: 4 61)
			#end:case
			else:
				if ((global66 doit: param1) == -32768):
					(global91 say: 5)
				else:
					(super doVerb: param1 &rest)
				#endif
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class vase_ChestInset(InsetView):
	#property vars (may be empty)
	noun = 7
	view = 7861
	cel = 3
	offsetX = 95
	offsetY = 39
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 2:
				(papers_ChestInset doVerb: param1)
			#end:case
			case 61:
				(global91 say: 4 61)
			#end:case
			else:
				if ((global66 doit: param1) == -32768):
					(global91 say: 5)
				else:
					(super doVerb: param1 &rest)
				#endif
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lid_ChestInset(InsetView):
	#property vars (may be empty)
	view = 7861
	cel = 4
	offsetX = 75
	offsetY = 6
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 == 5):
			(chestInset dispose:)
		else:
			(chestInset doVerb: param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class paper_BoxInset(InsetView):
	#property vars (may be empty)
	noun = 19
	view = 7862
	cel = 1
	offsetX = 68
	offsetY = 39
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 == 1):
			if (not (kernel.ScriptID(80, 0) tstFlag: 709 64)):
				(global1 givePoints: 1)
			#endif
			(kernel.ScriptID(80, 0) setFlag: 709 64)
			(KQ6Print posn: -1 10 say: 1 noun param1 0 1 init:)
		else:
			(super doVerb: param1 &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class pens_BoxInset(InsetView):
	#property vars (may be empty)
	noun = 16
	view = 7862
	cel = 2
	offsetX = 69
	offsetY = 32
	
#end:class or instance

@SCI.instance
class dice_BoxInset(InsetView):
	#property vars (may be empty)
	noun = 17
	view = 7862
	cel = 3
	offsetX = 98
	offsetY = 35
	
	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (param1 x:)
		temp1 = (param1 y:)
		(return
			(and
				(super onMe: temp0 temp1)
				(temp0 -= nsLeft)
				(temp1 -= nsTop)
				(((temp0 > 17) and noun = 18) or noun = 17)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class lid_BoxInset(InsetView):
	#property vars (may be empty)
	view = 7862
	loop = 1
	cel = 1
	offsetX = 91
	offsetY = 24
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(self startUpd:)
				cel = 0
				(global105 number: 905 play:)
				kernel.Animate((global5 elements:), 0)
				kernel.Animate((global5 elements:), 0)
				(ebonyBoxInset dispose:)
			#end:case
			else:
				(ebonyBoxInset doVerb: param1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class roomConv(Conversation):
	#property vars (may be empty)
#end:class or instance

