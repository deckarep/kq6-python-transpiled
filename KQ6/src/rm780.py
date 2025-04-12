#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 780
import sci_sh
import kernel
import Main
import rgCastle
import n913
import Conversation
import Scaler
import PolyPath
import Polygon
import Feature
import LoadMany
import StopWalk
import DPath
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm780 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None


@SCI.instance
class rm780(CastleRoom):
	#property vars (may be empty)
	noun = 3
	picture = 780
	style = 10
	vanishingX = 183
	vanishingY = 98
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		proc958_0(128, 7881, 789, 788)
		(global0 init: posn: 20 157 setScale: Scaler 100 70 190 140)
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
						180
						319
						180
						301
						169
						282
						169
						259
						152
						218
						152
						218
						147
						200
						147
						200
						144
						134
						144
						134
						149
						69
						149
						57
						155
						45
						155
						35
						159
						35
						163
						0
						178
						-10
						178
					yourself:
				)
		)
		(global32 add: chandelierF rugF eachElementDo: #init)
		(super init: &rest)
		if (((global9 at: 25) owner:) != 750):
			(theClown init:)
		#endif
		(candles init:)
		(door init: stopUpd:)
		(doorJam1 addToPic:)
		(doorJam2 addToPic:)
		(fireplace addToPic:)
		(otherFireplace addToPic:)
		(bed addToPic:)
		(chair init:)
		(fire setCycle: Fwd init:)
		((global0 scaler:) doit:)
		(self setScript: enterRoom)
		if proc913_0(10):
			(global102 fadeTo: 780 -1)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = (global0 onControl: 1)
		(cond
			case script: 0#end:case
			case (temp0 & 0x4000):
				(global2 newRoom: 840)
			#end:case
		)
		(super doit: &rest)
	#end:method

	@classmethod
	def warnUser(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				local3 = 1
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if local3:
			(kernel.ScriptID(80, 0) weddingRemind: 1)
		#endif
		if (not (kernel.ScriptID(80, 0) tstFlag: 710 512)):
			(kernel.ScriptID(80, 0) setFlag: 710 512)
		#endif
		(super dispose:)
		kernel.DisposeScript(964)
	#end:method

#end:class or instance

@SCI.instance
class enterRoom(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if proc913_0(10):
					(global0 setMotion: MoveTo 44 157 self)
				else:
					(global0 setMotion: MoveTo 64 157 self)
				#endif
			#end:case
			case 1:
				(door setCycle: Beg self)
			#end:case
			case 2:
				(global105 number: 902 setLoop: 1 play:)
				(door stopUpd:)
				register = 0
				if (global5 contains: kernel.ScriptID(80, 5)):
					(kernel.ScriptID(81, 0) resetGuard: kernel.ScriptID(80, 5) 1)
					(kernel.ScriptID(80, 5) dispose:)
					register = 1
				#endif
				if (global5 contains: kernel.ScriptID(80, 6)):
					(kernel.ScriptID(81, 0) resetGuard: kernel.ScriptID(80, 6) 2)
					(kernel.ScriptID(80, 6) dispose:)
					register = 1
				#endif
				if (not (register and proc913_0(10))):
					state.post('++')
				#endif
				cycles = 2
			#end:case
			case 3:
				(global91 say: 1 0 19 0 self)
			#end:case
			case 4:
				(cond
					case (not proc913_0(10)):
						(global2 setScript: callGuards)
					#end:case
					case (not (kernel.ScriptID(80, 0) tstFlag: 710 512)):
						local2 = 1
						(self setScript: turnClownAround self)
					#end:case
					else:
						(global1 handsOn:)
						(self dispose:)
					#end:else
				)
			#end:case
			case 5:
				(global0
					setMotion:
						PolyPath
						(theClown approachX:)
						(theClown approachY:)
						self
				)
			#end:case
			case 6:
				cycles = 10
			#end:case
			case 7:
				if (kernel.ScriptID(80, 0) tstFlag: 710 256):
					if (kernel.ScriptID(80, 0) tstFlag: 711 32):
						(roomConv add: -1 1 0 16)
					else:
						(roomConv add: -1 1 0 9 1)
					#endif
					proc913_1(155)
					(roomConv
						add: -1 1 0 9 2
						add: -1 1 0 9 3
						add: -1 1 0 9 4
						add: -1 1 0 9 5
						add: -1 1 0 9 6
						add: -1 1 0 9 7
					)
					if proc913_0(52):
						(roomConv add: -1 1 0 4)
					else:
						(roomConv add: -1 1 0 10)
					#endif
				else:
					if (kernel.ScriptID(80, 0) tstFlag: 711 32):
						(roomConv add: -1 1 0 16)
					else:
						(roomConv add: -1 1 0 8 1)
					#endif
					(roomConv
						add: -1 1 0 8 2
						add: -1 1 0 8 3
						add: -1 1 0 8 4
						add: -1 1 0 8 5
						add: -1 1 0 8 6
						add: -1 1 0 8 7
						add: -1 1 0 8 8
						add: -1 1 0 8 9
						add: -1 1 0 8 10
						add: -1 1 0 8 11
					)
					if proc913_0(52):
						(roomConv add: -1 1 0 2)
					else:
						(roomConv add: -1 1 0 10)
					#endif
				#endif
				(roomConv init: self)
			#end:case
			case 8:
				(chair priority: 1)
				(theClown priority: 0 loop: 2 cel: 2 setCycle: Beg self)
			#end:case
			case 9:
				local2 = 0
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class turnClownAround(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(theClown loop: 2 cel: 0 setCycle: CT 2 1 self)
			#end:case
			case 1:
				(chair priority: 0)
				(theClown priority: 1 setCycle: End self)
			#end:case
			case 2:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class callGuards(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(self setScript: callGuardsConvScr self)
			#end:case
			case 1:
				if proc913_0(154):
					(roomConv add: -1 1 0 18 1 add: -1 1 0 18 2 init: self)
				else:
					(roomConv add: -1 1 0 1 1 add: -1 1 0 1 2 init: self)
				#endif
			#end:case
			case 2:
				(self setScript: callGuardsConvScr self)
			#end:case
			case 3:
				if proc913_0(154):
					(roomConv add: -1 1 0 18 3 init: self)
				else:
					(roomConv add: -1 1 0 1 3 init: self)
				#endif
			#end:case
			case 4:
				(self setScript: callGuardsConvScr self)
			#end:case
			case 5:
				if proc913_0(154):
					(roomConv
						add: -1 1 0 18 4
						add: -1 1 0 18 5
						add: -1 1 0 18 6
						init: self
					)
				else:
					(roomConv
						add: -1 1 0 1 4
						add: -1 1 0 1 5
						add: -1 1 0 1 6
						init: self
					)
				#endif
			#end:case
			case 6:
				proc913_1(154)
				(global2 spotEgo: kernel.ScriptID(80, 5))
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class callGuardsConvScr(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		start = (state + 1)
		(super dispose: &rest)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(chair hide:)
				(theClown
					view: 7881
					loop: 0
					cel: 0
					posn: 242 154 0
					setCycle: End self
				)
			#end:case
			case 1:
				(chair
					view: 7881
					loop: 3
					cel: 0
					posn: 266 149
					setPri: 14
					show:
					stopUpd:
				)
				(theClown loop: 1 cel: 0 posn: 227 152 0 setCycle: CT 4 1 self)
			#end:case
			case 2:
				(self dispose:)
			#end:case
			case 3:
				(theClown setCycle: End self)
			#end:case
			case 4:
				(theClown loop: 2 cel: 6 posn: 221 151 setCycle: CT 3 -1 self)
			#end:case
			case 5:
				(self dispose:)
			#end:case
			case 6:
				(theClown loop: 2 cel: 3 setCycle: Beg self)
			#end:case
			case 7:
				cycles = 10
			#end:case
			case 8:
				(global105 number: 901 loop: 1 play:)
				(door setCycle: End self)
			#end:case
			case 9:
				(global105 stop:)
				(kernel.ScriptID(80, 5)
					setScale:
					scaleX: 110
					scaleY: 110
					posn: 13 158
					init:
					setMotion: MoveTo 39 158 self
				)
			#end:case
			case 10:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class jolloScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(theClown loop: 2 cel: 0 setCycle: CT 2 1 self)
			#end:case
			case 1:
				(theClown doVerb: register)
			#end:case
			case 2:
				(chair priority: 1)
				(theClown
					loop: 2
					cel: 2
					priority: 0
					posn: 232 144
					setCycle: Beg self
				)
			#end:case
			case 3:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class showLamp(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					loop:
						match register
							case 43: 2#end:case
							case 57: 1#end:case
							case 58: 2#end:case
							case 59: 0#end:case
							case 60: 2#end:case
							case 96: 1#end:case
							case 56: 0#end:case
						#end:match
				)
				(global0
					normal: 0
					view: 789
					setScale:
					scaleX: 104
					scaleY: 104
					cel: 0
					cycleSpeed: 8
				)
				cycles = (theClown cycleSpeed:)
			#end:case
			case 1:
				if (not (kernel.ScriptID(80, 0) tstFlag: 709 16)):
					(chair priority: 0)
					(theClown loop: 5 cel: 0 posn: 225 142 priority: 1)
				#endif
				cycles = (theClown cycleSpeed:)
			#end:case
			case 2:
				if (kernel.ScriptID(80, 0) tstFlag: 709 16):
					if proc999_5(register, 43, 57):
						(roomConv add: -1 4 register 12)
					else:
						cycles = 1
					#endif
				else:
					(kernel.ScriptID(80, 0) setFlag: 709 16)
					match register
						case 43:
							(roomConv add: -1 4 register 11 0)
						#end:case
						case 57:
							(self setScript: gaveNewLamp self register)
						#end:case
						else:
							(global1 givePoints: 3)
							(self setScript: gaveReplicaLamp self register)
						#end:else
					#end:match
				#endif
				if (roomConv size:):
					(roomConv init: self)
				#endif
			#end:case
			case 3:
				(global1 handsOn:)
				(global0
					reset: 0
					posn: (theClown approachX:) (theClown approachY:)
				)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class gaveNewLamp(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global91 say: 4 register 11 1 self)
			#end:case
			case 1:
				(self setScript: badLampConvScr self)
			#end:case
			case 2:
				(global91 say: 4 register 11 2 self oneOnly: 0)
			#end:case
			case 3:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class gaveReplicaLamp(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global91 say: 4 register 11 1 self)
			#end:case
			case 1:
				(self setScript: goodLampConvScr self)
			#end:case
			case 2:
				(global91 say: 4 register 11 2 self oneOnly: 0)
			#end:case
			case 3:
				(self setScript: goodLampConvScr self)
			#end:case
			case 4:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class goodLampConvScr(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		start = (state + 1)
		(super dispose: &rest)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global0 setCycle: CT 1 1 self)
			#end:case
			case 1:
				(chair priority: 0)
				(theClown
					view: 788
					loop: 5
					cel: 0
					priority: 1
					setCycle: End self
				)
			#end:case
			case 2:
				(global0 cel: 3)
				(theClown setCycle: CT 2 -1 self)
			#end:case
			case 3:
				(global0 setCycle: End)
				(theClown loop: 9 setCycle: End self)
			#end:case
			case 4:
				(global0
					reset: 0
					posn: (theClown approachX:) (theClown approachY:)
				)
				seconds = 3
			#end:case
			case 5:
				(theClown loop: 6 setCycle: CT 5 1 self)
			#end:case
			case 6:
				(theClown loop: 5 cel: 0)
				(self dispose:)
			#end:case
			case 7:
				(theClown
					view: 717
					setCycle: StopWalk -1
					posn: 218 151 0
					setPri: -1
					setScale:
						Scaler
						(global2 maxScaleSize:)
						(global2 minScaleSize:)
						(global2 maxScaleY:)
						(global2 minScaleY:)
					cycleSpeed: 6
					moveSpeed: 6
					setStep: 5 3
					setMotion: DPath 205 157 42 158 self
				)
			#end:case
			case 8:
				(global105 number: 901 loop: 1 play:)
				(door setCycle: End self)
			#end:case
			case 9:
				(global105 stop:)
				(theClown setMotion: MoveTo 12 158 self)
			#end:case
			case 10:
				(theClown hide:)
				(door setCycle: Beg self)
			#end:case
			case 11:
				(global105 number: 902 loop: 1 play:)
				(theClown setScript: followTimer)
				(global1 handsOn:)
				(global0 put: 25 750)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class followTimer(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(kernel.ScriptID(80, 0) setFlag: 711 -32768)
				seconds = 11
			#end:case
			case 1:
				(kernel.ScriptID(80, 0) clrFlag: 711 -32768)
				(theClown dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class badLampConvScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global0 setCycle: CT 1 1 self)
			#end:case
			case 1:
				(global0 setCycle: Beg)
				(theClown view: 788 loop: 4 cel: 0 setCycle: End self)
			#end:case
			case 2:
				(global0
					reset: 0
					posn: (theClown approachX:) (theClown approachY:)
				)
				(theClown cel: 0)
				cycles = (theClown cycleSpeed:)
			#end:case
			case 3:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lookThruKeyhole(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(kernel.ScriptID(82, 1)
					noun: 5
					actions: keyHoleActions
					init: 797 0 0 92 54
				)
				cycles = 2
			#end:case
			case 1:
				(global91 say: 5 1 14)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class doorJam1(View):
	#property vars (may be empty)
	x = 35
	y = 134
	noun = 5
	sightAngle = 40
	approachX = 44
	approachY = 157
	view = 788
	loop = 1
	cel = 1
	signal = 20496
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		(self approachVerbs: 5)
	#end:method

	@classmethod
	def doVerb():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(door noun: 5)
		(door doVerb: &rest)
	#end:method

#end:class or instance

@SCI.instance
class doorJam2(View):
	#property vars (may be empty)
	x = 35
	y = 134
	noun = 5
	approachX = 44
	approachY = 157
	view = 788
	loop = 1
	cel = 3
	priority = 12
	signal = 20496
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		(self approachVerbs: 5)
	#end:method

	@classmethod
	def doVerb():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(door noun: 5)
		(door doVerb: &rest)
	#end:method

#end:class or instance

@SCI.instance
class door(Prop):
	#property vars (may be empty)
	x = 28
	y = 154
	z = 20
	noun = 5
	approachX = 50
	approachY = 157
	view = 788
	cel = 5
	signal = 20480
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		(self approachVerbs: 5)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				(global1 handsOff:)
				(global105 number: 901 loop: 1 play:)
				(door setCycle: End self)
			#end:case
			case 1:
				if (not local1):
					local1.post('++')
					(_approachVerbs |= (global66 doit: 1))
					(global91 say: noun param1 13 0)
				else:
					(global2 setScript: kernel.ScriptID(82) 0 lookThruKeyhole)
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
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global105 stop:)
		proc80_2(4)
	#end:method

#end:class or instance

@SCI.instance
class bed(View):
	#property vars (may be empty)
	x = 122
	y = 135
	view = 788
	loop = 1
	signal = 20496
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = (param1 x:)
		temp1 = (param1 y:)
		(return
			(and
				(super onMe: temp0 temp1)
				(temp0 -= nsLeft)
				(temp1 -= nsTop)
				(((temp0 > 82) and noun = 12) or noun = 7)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class fireplace(View):
	#property vars (may be empty)
	x = 252
	y = 134
	view = 788
	loop = 1
	cel = 2
	signal = 20496
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = (param1 x:)
		temp1 = (param1 y:)
		(return
			(and
				(super onMe: temp0 temp1)
				(temp0 -= nsLeft)
				(temp1 -= nsTop)
				(or
					(and
						(temp0 < 61)
						(or
							((<= 14 temp0 35) and (<= 2 temp1 27) and noun = 13)
							((<= 39 temp0 50) and (<= 17 temp1 32) and noun = 14)
							noun = 10
						)
					)
					noun = 9
				)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class theClown(Actor):
	#property vars (may be empty)
	x = 232
	y = 144
	z = -10
	noun = 4
	approachX = 201
	approachY = 151
	view = 788
	loop = 2
	signal = 20496
	cycleSpeed = 13
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		(self approachVerbs: 43 56 57 2)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case proc999_5(param1, 1, 5):
				(super doVerb: param1 &rest)
			#end:case
			case ((not script) and (not local2)):
				(global1 handsOff:)
				(self setScript: jolloScr 0 param1)
			#end:case
			case proc999_5(param1, 43, 56, 57, 58, 59, 60, 96):
				param1 = proc999_3(43, proc999_2(57, param1))
				(script setScript: showLamp jolloScr param1)
			#end:case
			case 
				(and
					(kernel.ScriptID(80, 0) tstFlag: 710 256)
					(not proc913_0(155))
					(param1 == 2)
				):
				proc913_1(155)
				(global91 say: noun param1 15 0 jolloScr)
			#end:case
			else:
				if script:
					(jolloScr cycles: 10)
				#endif
				(super doVerb: param1 &rest)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class chair(View):
	#property vars (may be empty)
	x = 226
	y = 150
	noun = 11
	view = 788
	loop = 7
	priority = 1
	signal = 20496
	
#end:class or instance

@SCI.instance
class otherFireplace(View):
	#property vars (may be empty)
	x = 294
	y = 124
	view = 788
	loop = 1
	cel = 4
	priority = 12
	signal = 16400
	
#end:class or instance

@SCI.instance
class candles(Prop):
	#property vars (may be empty)
	x = 165
	y = 84
	noun = 15
	view = 788
	loop = 8
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self setCycle: Fwd)
		(super init: &rest)
	#end:method

#end:class or instance

@SCI.instance
class chandelierF(Feature):
	#property vars (may be empty)
	noun = 15
	onMeCheck = 4
	
#end:class or instance

@SCI.instance
class rugF(Feature):
	#property vars (may be empty)
	noun = 8
	onMeCheck = 2
	
#end:class or instance

@SCI.instance
class fire(Prop):
	#property vars (may be empty)
	x = 274
	y = 140
	noun = 9
	sightAngle = 40
	view = 788
	loop = 10
	cycleSpeed = 8
	
#end:class or instance

@SCI.instance
class roomConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class keyHoleActions(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 1
		match param1
			case 1:
				(global91 say: 5 param1 14 2)
			#end:case
			else:
				temp0 = 0
			#end:else
		#end:match
		return temp0
	#end:method

#end:class or instance

