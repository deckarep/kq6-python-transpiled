#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 790
import sci_sh
import kernel
import Main
import rgCastle
import n913
import FlipPoly
import Scaler
import PolyPath
import Polygon
import Feature
import Timer
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm790 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = 1
local2 = None


@SCI.procedure
def localproc_0():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	temp1 = local0
	if argc:
		local0 = (1 + (not (local0 == 2)))
		if (global2 obstacles:):
			((global2 obstacles:) dispose:)
			(global2 obstacles: 0)
			match local0
				case 1:
					(global2
						addObstacle:
							((Polygon new:)
								type: 3
								init:
									81
									129
									56
									138
									114
									169
									114
									177
									107
									177
									64
									153
									26
									125
									4
									99
									4
									63
									33
									34
									69
									18
									57
									18
									24
									32
									0
									49
									-10
									83
									0
									164
									51
									189
									230
									189
									285
									185
									319
									169
									319
									155
									298
									146
									230
									128
									186
									124
									129
									124
								yourself:
							)
					)
				#end:case
				else:
					(global2
						addObstacle:
							((Polygon new:)
								type: 3
								init:
									191
									124
									134
									124
									90
									128
									58
									134
									36
									154
									44
									154
									72
									134
									85
									134
									48
									158
									0
									158
									1
									169
									35
									185
									90
									189
									269
									189
									320
									164
									330
									83
									320
									49
									296
									32
									263
									18
									251
									18
									287
									34
									316
									63
									316
									99
									294
									125
									256
									153
									213
									177
									206
									177
									206
									169
									226
									129
								yourself:
							)
					)
				#end:else
			#end:match
		#endif
	#endif
	if (temp1 != local0):
		local2 = (not local2)
	#endif
	(global0 oldScaleSignal: 0)
	if local2:
		(global0 setPri: 5 setScale: Scaler 100 56 131 41)
	else:
		(global0
			setScale:
				Scaler
				(global2 maxScaleSize:)
				(global2 minScaleSize:)
				(global2 maxScaleY:)
				(global2 minScaleY:)
			setPri: -1
		)
	#endif
	((global0 scaler:) doit:)
#end:procedure

@SCI.procedure
def localproc_1(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	if (local0 == 2):
		return (320 - param1)
	else:
		return param1
	#endif
#end:procedure

@SCI.instance
class rm790(CastleRoom):
	#property vars (may be empty)
	noun = 3
	picture = 790
	style = 10
	walkOffEdge = 1
	autoLoad = 0
	minScaleSize = 60
	minScaleY = 122
	maxScaleY = 173
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (global12 == 750):
			(style |= 0x4000)
		else:
			(style &= 0xbfff)
		#endif
		(self
			addObstacle:
				((Polygon new:)
					type: 3
					init:
						81
						129
						56
						138
						114
						169
						114
						177
						107
						177
						64
						153
						26
						125
						4
						99
						4
						63
						33
						34
						69
						18
						57
						18
						24
						32
						0
						49
						-10
						83
						0
						164
						51
						189
						230
						189
						285
						185
						319
						169
						319
						155
						298
						146
						230
						128
						186
						124
						129
						124
					yourself:
				)
		)
		(super init: &rest)
		(global0 init:)
		(global32
			add: stairsFeature doorFeature torchFeature
			eachElementDo: #init
		)
		match global12
			case 750:
				proc926_0()
				(global0 posn: 256 19)
				local2 = 1
				local0 = 2
				(self setScript: enterFromTop)
				(stairs addToPic:)
				(railing addToPic:)
				(doorCover addToPic:)
			#end:case
			else:
				(rglow init: posn: 228 81 setLoop: 0)
				(lglow init: posn: 96 73 setLoop: 2)
				(rflame init: posn: 229 73 setLoop: 4 setCycle: Fwd)
				(lflame init: posn: 97 71 setLoop: 4 setCycle: Fwd)
				(global0 loop: 2 posn: 159 125)
				(vizier init:)
				local0 = 1
				if ((not global87) or (not kernel.HaveMouse())):
					(kernel.ScriptID(80, 0) loiterTimer: 242)
				else:
					(kernel.ScriptID(80, 0) loiterTimer: 122)
				#endif
			#end:else
		#end:match
		localproc_0()
		((global0 scaler:) doit:)
		if (not script):
			(global1 handsOn:)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (global0 onControl: 1)
		(cond
			case script: 0#end:case
			case ((temp0 & 0x0002) or ((local0 == 2) and (temp0 & 0x0044))):
				(self setScript: changeTowerRooms)
			#end:case
			case ((temp0 & 0x2000) and local2):
				(global0
					setScale:
						Scaler
						maxScaleSize
						minScaleSize
						maxScaleY
						minScaleY
					setPri: -1
				)
				local2 = 0
			#end:case
			case ((temp0 & 0x4020) and (not local2)):
				(global0 setPri: 13 setScale: Scaler 100 56 131 41)
				((global0 scaler:) doit:)
				local2 = 1
			#end:case
			case local2:
				(cond
					case ((global0 y:) < 83):
						if ((global0 priority:) == 13):
							(global0 priority: 5)
						#endif
					#end:case
					case ((global0 priority:) == 5):
						(global0 priority: 13)
					#end:case
				)
			#end:case
		)
		(super doit: &rest)
	#end:method

	@classmethod
	def doLoiter():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global2 setScript: castSpell 0 2)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose:)
		kernel.DisposeScript(752)
	#end:method

	@classmethod
	def newRoom(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(lTimer dispose: delete:)
		(rTimer dispose: delete:)
		(super newRoom: param1)
	#end:method

#end:class or instance

@SCI.instance
class changeTowerRooms(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(global1 handsOff:)
		(super init: &rest)
		register = local2
	#end:method

	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(kernel.ScriptID(80, 0) loiterTimer: 0)
				cycles = 2
			#end:case
			case 1:
				(= temp0
					if register:
						localproc_1(64)
					else:
						49
					#endif
				)
				temp1 = (19 if register else 149)
				(global0 setMotion: MoveTo temp0 temp1 self)
			#end:case
			case 2:
				temp2 = 1
				if register:
					if (local0 == 2):
						(global2 newRoom: 750)
						temp2 = 0
					else:
						(global0 posn: 49 149)
					#endif
				else:
					(global0 posn: 64 19)
				#endif
				if temp2:
					localproc_0(register)
					if (local0 == 1):
						(global2 style: ((global2 style:) & 0xbfff))
					else:
						(global2 style: (| (global2 style:) 0x4000))
					#endif
					(global2 drawPic: 790)
					if (local0 == local1):
						(vizier init:)
					#endif
					if (local0 == 2):
						(stairs addToPic:)
						(railing addToPic:)
						(doorCover addToPic:)
						(rglow init: posn: 223 73 setLoop: 3)
						(rTimer client: rglow)
						(lglow init: posn: 90 81 setLoop: 1)
						(lTimer client: lglow)
						(rflame init: posn: 222 71 setLoop: 4 setCycle: Fwd)
						(lflame init: posn: 90 73 setLoop: 4 setCycle: Fwd)
					else:
						if (global10 contains: stairs):
							(stairs dispose:)
							(railing dispose:)
							(doorCover dispose:)
						#endif
						(rglow init: posn: 228 81 setLoop: 0 cue:)
						(rTimer client: rglow)
						(lglow init: posn: 96 73 setLoop: 2)
						(lTimer client: lglow)
						(rflame init: posn: 229 73 setLoop: 4 setCycle: Fwd)
						(lflame init: posn: 97 71 setLoop: 4 setCycle: Fwd)
					#endif
					cycles = 2
				#endif
			#end:case
			case 3:
				(= temp0
					if register:
						68
					else:
						localproc_1(42)
					#endif
				)
				temp1 = (132 if register else 45)
				(global0 setMotion: PolyPath temp0 temp1 self)
			#end:case
			case 4:
				if (not local2):
					(global0 reset:)
					(global1 handsOn:)
					if ((not global87) or (not kernel.HaveMouse())):
						(kernel.ScriptID(80, 0) loiterTimer: 61)
					else:
						(kernel.ScriptID(80, 0) loiterTimer: 31)
					#endif
					(self dispose:)
				else:
					(global2 setScript: castSpell 0 3)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class enterFromTop(Script):
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
				(global0 setMotion: MoveTo 278 29 self)
			#end:case
			case 2:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class castSpell(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(genie loop: 8 cel: (6 + ((global0 x:) < 160)) setPri: 15)
				(cond
					case ((global0 x:) >= 160):
						if (local0 == 2):
							(genie posn: localproc_1(257) 162)
						else:
							(genie posn: 17 137)
						#endif
					#end:case
					case (local0 == 2):
						(genie posn: localproc_1(17) 137)
					#end:case
					else:
						(genie posn: localproc_1(257) 162)
					#end:else
				)
				cycles = 2
			#end:case
			case 1:
				(self setScript: kernel.ScriptID(752, 1) self genie)
			#end:case
			case 2:
				proc913_4(global0, genie, self)
			#end:case
			case 3:
				cycles = 5
			#end:case
			case 4:
				match register
					case 1:
						(global91 say: 4 5 0 0 self)
					#end:case
					case 2:
						(global91 say: 1 0 2 0 self)
					#end:case
					case 3:
						(global91 say: 1 0 4 0 self)
					#end:case
				#end:match
			#end:case
			case 5:
				global106 = global0
				global156 = getEgo
				(self setScript: kernel.ScriptID(752, 0) 0 genie)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getEgo(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0
					view: 749
					normal: 0
					cel: 0
					loop: (mod (global0 cel:) 4)
					cycleSpeed: 8
					setCycle: CT 2 1 self
				)
			#end:case
			case 1:
				if ((not local2) or (local2 and ((global0 y:) < 43))):
					(global0
						loop:
							match (global0 loop:)
								case 0: 3#end:case
								case 1: 2#end:case
								case 2: 1#end:case
								case 3: 0#end:case
							#end:match
					)
				#endif
				(global0 setCycle: End self)
			#end:case
			case 2:
				if ((global0 loop:) > 2):
					(global0
						loop: (4 + ((global0 loop:) == 3))
						cycleSpeed: 10
						setCycle: End self
					)
				else:
					cycles = 1
				#endif
			#end:case
			case 3:
				if register:
					(self dispose:)
				else:
					proc0_1(18)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genie(Actor):
	#property vars (may be empty)
	x = 257
	y = 162
	view = 702
	loop = 7
	priority = 13
	signal = 16
	
#end:class or instance

@SCI.instance
class vizier(Actor):
	#property vars (may be empty)
	view = 145
	signal = 8192
	scaleSignal = 1
	scaleX = 80
	scaleY = 80
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		x = localproc_1(20)
		y = 39
		(super init: &rest)
		(self
			setCycle: Walk
			setStep: 8 4
			setMotion: MoveTo localproc_1(80) 14 self
		)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		local1.post('++')
		(self dispose:)
	#end:method

#end:class or instance

@SCI.instance
class doorFeature(Feature):
	#property vars (may be empty)
	noun = 4
	onMeCheck = 8
	
	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		return ((super onMe: param1) and (local0 == 1))
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global2 setScript: castSpell 0 1)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class stairsFeature(Feature):
	#property vars (may be empty)
	noun = 5
	onMeCheck = 52
	
#end:class or instance

@SCI.instance
class torchFeature(Feature):
	#property vars (may be empty)
	noun = 7
	onMeCheck = 128
	
#end:class or instance

@SCI.instance
class stairs(View):
	#property vars (may be empty)
	x = 84
	y = 161
	noun = 6
	view = 790
	cel = 1
	signal = 20496
	
#end:class or instance

@SCI.instance
class railing(View):
	#property vars (may be empty)
	x = 84
	y = 161
	noun = 6
	view = 790
	priority = 10
	signal = 20496
	
#end:class or instance

@SCI.instance
class doorCover(View):
	#property vars (may be empty)
	x = 133
	y = 65
	onMeCheck = 0
	view = 790
	loop = 1
	signal = 16400
	
#end:class or instance

@SCI.instance
class mainPoly(Polygon):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class rglow(Prop):
	#property vars (may be empty)
	view = 791
	priority = 4
	signal = 18448
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(rTimer setCycle: self kernel.Random(10, 30))
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self cel: kernel.Random(0, 2))
		(rflame cycleSpeed: kernel.Random(4, 8))
		(rTimer setCycle: self kernel.Random(2, 20))
	#end:method

#end:class or instance

@SCI.instance
class lglow(Prop):
	#property vars (may be empty)
	view = 791
	priority = 4
	signal = 18448
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(lTimer setCycle: self kernel.Random(10, 30))
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self cel: kernel.Random(0, 2))
		(lflame cycleSpeed: kernel.Random(4, 8))
		(lTimer setCycle: self kernel.Random(2, 20))
	#end:method

#end:class or instance

@SCI.instance
class rflame(Prop):
	#property vars (may be empty)
	view = 791
	priority = 5
	signal = 18448
	
#end:class or instance

@SCI.instance
class lflame(Prop):
	#property vars (may be empty)
	view = 791
	priority = 5
	signal = 18448
	
#end:class or instance

@SCI.instance
class lTimer(Timer):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class rTimer(Timer):
	#property vars (may be empty)
#end:class or instance

