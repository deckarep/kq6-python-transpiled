#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 450
import sci_sh
import kernel
import Main
import n451
import KQ6Room
import n913
import Conversation
import Scaler
import PolyPath
import Polygon
import Feature
import LoadMany
import Sound
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm450 = 0,
	oyster = 1,
	giveItemScript = 2,
	rightInvItem = 3,
	wrongInvItem = 4,
	toTheSea = 5,
	gnomeGroup = 6,
	snooze4 = 7,
	proc450_8 = 8,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None
local4 = None
local5 = None
local6 = None


@SCI.procedure
def localproc_0(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	(tmpGnome
		view: (param1 view:)
		loop: (param1 loop:)
		cel: (param1 cel:)
		x: (param1 x:)
		y: (param1 y:)
		signal: (param1 signal:)
	)
	if (global5 contains: tmpGnome):
		(tmpGnome show:)
	else:
		(tmpGnome init:)
	#endif
#end:procedure

@SCI.procedure
def localproc_1(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	match local5
		case 1:
			(kernel.ScriptID(455, 0) doVerb: param1)
		#end:case
		case 2:
			(kernel.ScriptID(456, 0) doVerb: param1)
		#end:case
		case 3:
			(kernel.ScriptID(4561, 0) doVerb: param1)
		#end:case
		case 4:
			(kernel.ScriptID(457, 0) doVerb: param1)
		#end:case
		case 5:
			(kernel.ScriptID(458, 0) doVerb: param1)
		#end:case
	#end:match
#end:procedure

@SCI.procedure
def proc450_8(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	if param1:
		(snoreSong stop:)
		(snooze1 view: 2002)
		(snooze4 view: 2002)
		(shimmer1 dispose:)
		(shimmer2 dispose:)
	else:
		(snoreSong play:)
		(snooze1 view: 450 loop: 3 checkDetail:)
		if (kernel.ScriptID(40, 0) oysterDozing:):
			(snooze4 view: 450 loop: 5 init: setCycle: Fwd checkDetail:)
		#endif
		(shimmer1 init:)
		(shimmer2 init:)
	#endif
#end:procedure

@SCI.instance
class rm450(KQ6Room):
	#property vars (may be empty)
	picture = 450
	horizon = 70
	walkOffEdge = 1
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (global5 contains: mySentence):
			(mySentence
				y: ((mySentence y:) + 100)
				z: 0
				setScript: sentenceFloat
			)
		#endif
	#end:method

	@classmethod
	def notify(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case ((not argc) or (not param1)): 0#end:case
			case (not local5):
				(global2 setScript: 130)
			#end:case
			else:
				if (global2 script:):
					(kernel.ScriptID(130) next: resetGnomes)
				#endif
				(global2 setScript: 130)
			#end:else
		)
		(global0 actions: egoDoVerb)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global2
			addObstacle:
				((Polygon new:)
					type: 2
					init: 130 72 193 0 319 0 319 78 213 78
					yourself:
				)
				((Polygon new:)
					type: 2
					init:
						125
						72
						115
						80
						115
						92
						79
						97
						89
						111
						75
						128
						94
						141
						94
						150
						58
						150
						24
						189
						0
						189
						0
						0
						64
						0
					yourself:
				)
				((Polygon new:)
					type: 2
					init:
						235
						147
						233
						140
						246
						124
						319
						124
						319
						189
						286
						189
						286
						153
						299
						147
						279
						144
						256
						151
					yourself:
				)
				((Polygon new:)
					type: 2
					init: 125 137 94 137 90 134 93 131 124 131 129 134
					yourself:
				)
		)
		(global1 handsOff:)
		(super init: &rest)
		(oyster init:)
		if 
			(or
				(((global9 at: 30) owner:) != global11)
				(kernel.ScriptID(40, 0) oysterDozing:)
			)
			(oyster setCel: 2)
			(snooze4 init: setCycle: Fwd)
		else:
			(oyster setCel: 0)
			(oyBlink
				init:
				setPri: (oyster priority:)
				hide:
				setScript: oyBlinkScript
			)
		#endif
		kernel.Lock(143, 450, 0)
		(global105 number: 916 setLoop: -1 play:)
		(global32
			add:
				farFoliage
				rock
				oysterBeds
				otherRocks
				smallRocks
				sky
				beach
				myPath
				oysterCouch
				ocean
			eachElementDo: #init
		)
		(shimmer1 init:)
		(shimmer2 init:)
		(snoreSong play:)
		(snooze1 init: setCycle: Fwd)
		if (((global9 at: 50) owner:) == global11):
			(mySentence init: setCycle: Fwd setScript: sentenceFloat)
		#endif
		(global102 number: 915 setLoop: -1 play:)
		(global0 setScale: Scaler 100 30 126 70 actions: egoDoVerb)
		if proc999_5(global12, 470, 460):
			(global2 setScript: egoEnters)
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		proc913_2(59)
		proc958_0(0, 455, 456, 4561, 457, 458)
		if (((global9 at: 30) owner:) != global11):
			(kernel.ScriptID(40, 0) oysterDozing: 0)
		#endif
		(kernel.ScriptID(40, 0) setScript: 0)
		if (global5 contains: mySentence):
			(mySentence setMotion: 0)
		#endif
		(global105 fade: 0 10 10)
		(super dispose:)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (global2 script:):#end:case
			case 
				(and
					((global0 view:) != 900)
					(or
						((global0 onControl: 1) == 32)
						((global0 onControl: 1) == 64)
					)
				):
				if 
					(and
						(global5 contains: mySentence)
						((mySentence y:) > 158)
						(sentencePoly points:)
					)
					((global2 obstacles:) delete: sentencePoly)
					(sentencePoly dispose: points: 0)
					(mySentence setScript: sentenceFloat)
				#endif
				(global103 stop:)
				(global0 view: 900)
			#end:case
			case (((global0 view:) != 308) and ((global0 onControl: 1) == 4)):
				if (global5 contains: mySentence):
					(mySentence setMotion: 0 setScript: 0)
				#endif
				(cond
					case ((global0 view:) != 900): 0#end:case
					case ((global0 heading:) < 135):
						(global0 loop: 0)
					#end:case
					case ((global0 heading:) > 225):
						(global0 loop: 1)
					#end:case
					else:
						(global0 loop: 2)
					#end:else
				)
				(global0 view: 308)
				(global103 number: 922 setLoop: -1 play:)
			#end:case
			case (((global0 view:) != 3081) and ((global0 onControl: 1) == 2)):
				(global0 view: 3081)
			#end:case
			case 
				(and
					(not local2)
					((global0 view:) != 3082)
					((global0 onControl: 1) == 8192)
				):
				(global0 view: 3082)
			#end:case
			case ((global0 edgeHit:) == 1):
				(global2 newRoom: 470)
			#end:case
			case ((global0 edgeHit:) == 2):
				(global2 setScript: egoExits)
			#end:case
			case 
				(and
					proc999_5((global0 onControl: 1), 64, 128)
					(not proc913_0(42))
				):
				proc913_1(81)
				(global103 number: 451 setLoop: -1 play:)
				(self setScript: mainGnomeScript)
			#end:case
		)
		(super doit:)
	#end:method

	@classmethod
	def scriptCheck():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 1
		if local5:
			(global91 say: 0 0 194 1 0 899)
			temp0 = 0
		#endif
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class snoreSong(Sound):
	#property vars (may be empty)
	number = 962
	loop = -1
	
#end:class or instance

@SCI.instance
class oysterGuts(Prop):
	#property vars (may be empty)
	x = 60
	y = 132
	noun = 1
	view = 4531
	cel = 1
	priority = 11
	signal = 16400
	
#end:class or instance

@SCI.instance
class pearlGlint(Prop):
	#property vars (may be empty)
	x = 72
	y = 133
	view = 902
	loop = 1
	priority = 13
	signal = 16400
	
#end:class or instance

@SCI.instance
class snooze1(Prop):
	#property vars (may be empty)
	x = 66
	y = 113
	z = 20
	noun = 8
	view = 450
	loop = 3
	signal = 20480
	detailLevel = 3
	
	@classmethod
	def checkDetail(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (not detailLevel):#end:case
			case 
				(<
					if argc:
						param1
					else:
						(global1 detailLevel:)
					#endif
					detailLevel
				):
				(self cel: ((self lastCel:) - 1) stopUpd:)
			#end:case
			case cycler:
				(self startUpd:)
			#end:case
		)
	#end:method

#end:class or instance

@SCI.instance
class snooze4(Prop):
	#property vars (may be empty)
	x = 103
	y = 158
	z = 40
	noun = 8
	view = 450
	loop = 5
	signal = 20480
	detailLevel = 3
	
	@classmethod
	def checkDetail(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (not detailLevel):#end:case
			case 
				(<
					if argc:
						param1
					else:
						(global1 detailLevel:)
					#endif
					detailLevel
				):
				(self cel: ((self lastCel:) - 1) stopUpd:)
			#end:case
			case cycler:
				(self startUpd:)
			#end:case
		)
	#end:method

#end:class or instance

@SCI.instance
class oyster(Prop):
	#property vars (may be empty)
	x = 60
	y = 132
	noun = 1
	approachDist = 1000
	view = 4531
	loop = 2
	priority = 11
	signal = 16400
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				(cond
					case local5:
						(global91 say: 1 0 1 1)
					#end:case
					case (((global9 at: 30) owner:) != global11):
						(global91 say: 1 1 7 1)
					#end:case
					case (kernel.ScriptID(40, 0) oysterDozing:):
						(global91 say: 1 1 8 1)
					#end:case
					else:
						(global2 setScript: lookAtOyster)
					#end:else
				)
			#end:case
			case 5:
				(cond
					case 
						(or
							(((global9 at: 30) owner:) != global11)
							(kernel.ScriptID(40, 0) oysterDozing:)
						):
						(global91 say: 1 5 2 1)
					#end:case
					case proc913_0(107):
						(global91 say: 1 5 3 0)
					#end:case
					else:
						(global91 say: 1 5 4 0)
					#end:else
				)
			#end:case
			case 2:
				if (global5 contains: gnomeGroup):
					(global91 say: 1 0 1 1)
				else:
					(global0 setScript: oysterMessages 0 2)
				#endif
			#end:case
			case 42:
				if (global5 contains: gnomeGroup):
					(global91 say: 1 0 1 1)
				else:
					(global0 setScript: oysterMessages 0 42)
				#endif
			#end:case
			case 66:
				(global91 say: 1 66 0 1)
			#end:case
			case 30:
				if 
					(or
						(((global9 at: 30) owner:) != global11)
						(kernel.ScriptID(40, 0) oysterDozing:)
					)
					(global91 say: 1 30 2 1)
				else:
					(global91 say: 1 30 9 1)
				#endif
			#end:case
			case 31:
				(global1 handsOff:)
				(global2 setScript: oyFluteScript)
			#end:case
			else:
				(cond
					case (global5 contains: gnomeGroup):
						(global91 say: 1 0 1 1)
					#end:case
					case 
						(or
							(((global9 at: 30) owner:) != global11)
							(kernel.ScriptID(40, 0) oysterDozing:)
						):
						(global91 say: 1 5 2 1)
					#end:case
					case proc913_0(107):
						(global91 say: 1 0 3 1 self)
					#end:case
					else:
						(global91 say: 1 0 4 1 self)
					#end:else
				)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class oyBlink(Prop):
	#property vars (may be empty)
	x = 60
	y = 132
	view = 4531
	loop = 1
	signal = 16384
	
#end:class or instance

@SCI.instance
class oyBlinkScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				seconds = kernel.Random(3, 8)
			#end:case
			case 1:
				(client show:)
				cycles = 6
			#end:case
			case 2:
				(client hide:)
				(self init:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class oyFluteScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global0 setMotion: PolyPath 140 130 self)
			#end:case
			case 1:
				if 
					(or
						(((global9 at: 30) owner:) != global11)
						(kernel.ScriptID(40, 0) oysterDozing:)
					)
					(global91 say: 1 31 2 1 self)
				else:
					(global91 say: 1 31 9 0 self)
				#endif
			#end:case
			case 2:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class lookAtOyster(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91 say: 1 1 9 1 self)
			#end:case
			case 1:
				(global103 number: 961 setLoop: 1 play:)
				(oysterGuts init:)
				(oyster setPri: 12 setLoop: 1 cel: 0 setCycle: End self)
			#end:case
			case 2:
				(pearlGlint init: setCycle: End self)
			#end:case
			case 3:
				(pearlGlint dispose:)
				(oyster setCycle: Beg self)
			#end:case
			case 4:
				(oysterGuts dispose:)
				(oyster setLoop: 2 cel: 0 setPri: 11)
				cycles = 2
			#end:case
			case 5:
				(global91 say: 1 1 9 2 self)
			#end:case
			case 6:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class oysterMessages(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				if (((global0 x:) == 140) and ((global0 y:) == 130)):
					cycles = 1
				else:
					(global0 setMotion: PolyPath 140 130 self)
				#endif
			#end:case
			case 1:
				if ((global0 heading:) != 270):
					(global0 setHeading: 270 self)
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				if 
					(and
						(register == 2)
						(((global9 at: 30) owner:) == global11)
						(not proc913_0(107))
					)
					(global91 say: 1 2 10 1 self)
				else:
					cycles = 1
				#endif
			#end:case
			case 3:
				if 
					(and
						(register == 2)
						(((global9 at: 30) owner:) == global11)
					)
					(oyster setPri: 12)
				#endif
				cycles = 6
			#end:case
			case 4:
				match register
					case 2:
						(cond
							case 
								(or
									(((global9 at: 30) owner:) != global11)
									(kernel.ScriptID(40, 0) oysterDozing:)
								):
								(global91 say: 1 5 2 1 self)
							#end:case
							case proc913_0(107):
								(global91 say: 1 2 11 0 self)
							#end:case
							else:
								proc913_1(107)
								(global91 say: 1 2 10 2 self)
							#end:else
						)
					#end:case
					case 42:
						(cond
							case (((global9 at: 30) owner:) != global11):
								(global91 say: 1 42 7 1 self)
							#end:case
							case (not proc913_0(107)):
								(global91 say: 1 42 4 1 self)
							#end:case
							case (kernel.ScriptID(40, 0) oysterDozing:):
								(global91 say: 1 42 8 1 self)
							#end:case
							case proc913_0(108):
								(mySentence y: ((mySentence y:) - 100) z: -100)
								(oyBlink dispose:)
								proc450_8(1)
								proc451_0(1)
								(self dispose:)
							#end:case
							else:
								proc913_1(108)
								(global1 givePoints: 2)
								(mySentence y: ((mySentence y:) - 100) z: -100)
								(oyBlink dispose:)
								proc450_8(1)
								proc451_0(0)
								(self dispose:)
							#end:else
						)
					#end:case
				#end:match
			#end:case
			case 5:
				(global1 handsOn:)
				if (register == 2):
					(oyster setPri: 11)
				#endif
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class mySentence(Actor):
	#property vars (may be empty)
	x = 160
	y = 185
	noun = 11
	view = 4501
	priority = 5
	signal = 16
	cycleSpeed = 12
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case ((param1 == 1) or (param1 == 2)):
				(super doVerb: param1)
			#end:case
			case (param1 == 5):
				(cond
					case (global5 contains: gnomeGroup):
						(global91 say: 1 0 1 1)
					#end:case
					case (global5 contains: global0):
						(global1 handsOff:)
						(global0 setScript: getSentence)
					#end:case
					else:
						(global91 say: 11 1 0 1)
					#end:else
				)
			#end:case
			else:
				(global91 say: 11 0 0 1)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class shimmer1(Prop):
	#property vars (may be empty)
	x = 27
	y = 169
	noun = 7
	view = 447
	priority = 1
	signal = 16400
	cycleSpeed = 30
	detailLevel = 2
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self setCycle: Fwd)
		(super init:)
	#end:method

#end:class or instance

@SCI.instance
class shimmer2(Prop):
	#property vars (may be empty)
	x = 299
	y = 171
	noun = 7
	view = 447
	loop = 1
	priority = 1
	signal = 16400
	cycleSpeed = 30
	detailLevel = 2
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self setCycle: Fwd)
		(super init:)
	#end:method

#end:class or instance

@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class farFoliage(Feature):
	#property vars (may be empty)
	noun = 3
	onMeCheck = 512
	
#end:class or instance

@SCI.instance
class oysterBeds(Feature):
	#property vars (may be empty)
	noun = 8
	onMeCheck = 16
	
#end:class or instance

@SCI.instance
class oysterCouch(Feature):
	#property vars (may be empty)
	onMeCheck = 16384
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(oyster doVerb: param1 &rest)
	#end:method

#end:class or instance

@SCI.instance
class otherRocks(Feature):
	#property vars (may be empty)
	noun = 6
	onMeCheck = 256
	
#end:class or instance

@SCI.instance
class smallRocks(Feature):
	#property vars (may be empty)
	noun = 13
	onMeCheck = 1024
	
#end:class or instance

@SCI.instance
class sky(Feature):
	#property vars (may be empty)
	noun = 10
	onMeCheck = 2048
	
#end:class or instance

@SCI.instance
class myPath(Feature):
	#property vars (may be empty)
	noun = 9
	onMeCheck = 4096
	
#end:class or instance

@SCI.instance
class rock(Feature):
	#property vars (may be empty)
	noun = 5
	onMeCheck = 136
	
#end:class or instance

@SCI.instance
class beach(Feature):
	#property vars (may be empty)
	noun = 10
	onMeCheck = 96
	
#end:class or instance

@SCI.instance
class ocean(Feature):
	#property vars (may be empty)
	noun = 7
	onMeCheck = 8198
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		(global93 add: self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global93 delete: self)
		(super dispose:)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = (global80 curEvent:)
		match param1
			case 3:
				if 
					(and
						(or
							((global0 onControl: 1) == 32)
							((global0 onControl: 1) == 64)
						)
						((temp0 y:) > 171)
					)
					local1 = 165
					if ((temp0 x:) < (global0 x:)):
						local0 = ((global0 x:) - 30)
					else:
						local0 = ((global0 x:) + 30)
					#endif
				else:
					local0 = (temp0 x:)
					local1 = (temp0 y:)
				#endif
				(global0 setScript: inToWater 0 0)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

class Gnome(Actor):
	#property vars (may be empty)
	y = 127
	z = 1
	signal = 16384
	xStep = 6
	gnomesItem = 0
	msgCase = 0
	failCase = 0
	textCase = 0
	EOLx = 0
	FOLx = 0
	gnomeScript = 0
	startPoint = 0
	
#end:class or instance

@SCI.instance
class gnomeGroup(Actor):
	#property vars (may be empty)
	x = 130
	y = 71
	noun = 4
	yStep = 1
	view = 454
	signal = 16384
	cycleSpeed = 12
	illegalBits = 0
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if kernel.IsObject(scaler):
			(scaler dispose:)
		#endif
		scaler = 0
		(super dispose:)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if kernel.IsObject(scaler):
			(scaler dispose:)
		#endif
		scaler = 0
		(super dispose:)
	#end:method

#end:class or instance

@SCI.instance
class tmpGnome(Actor):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class mainGnomeScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global91 say: 10 3 19 1 self)
			#end:case
			case 1:
				(global0 setMotion: MoveTo 236 128 self)
			#end:case
			case 2:
				(global0 setHeading: 335)
				cycles = 8
			#end:case
			case 3:
				(snoreSong stop:)
				(snooze1 dispose:)
				if (global5 contains: snooze4):
					(snooze4 dispose:)
				#endif
				(gnomeGroup
					setScale: Scaler 100 30 126 70
					init:
					setCycle: Walk
					setMotion: MoveTo 96 126 self
				)
			#end:case
			case 4:
				(global0 setHeading: 270)
				cycles = 8
			#end:case
			case 5:
				(global91 say: 10 3 19 2 self)
			#end:case
			case 6:
				(gnomeGroup
					setScale: 0
					view: 4541
					setLoop: 0
					cel: 0
					posn: 146 128
					setCycle: End self
				)
				kernel.UnLoad(128, 454)
			#end:case
			case 7:
				local5 = 1
				(kernel.ScriptID(455, 0) init:)
				(gnomeGroup
					view: 459
					loop: -1
					setLoop: 0
					x: 155
					y: 126
					stopUpd:
					setScript: riddleAlex 0 kernel.ScriptID(455, 0)
				)
				kernel.UnLoad(128, 4541)
				cycles = 2
			#end:case
			case 8:#end:case
			case 9:
				localproc_0(kernel.ScriptID(455, 0))
				(kernel.ScriptID(455, 0) dispose:)
				cycles = 2
			#end:case
			case 10:
				kernel.DisposeScript(455)
				kernel.UnLoad(128, 455)
				cycles = 2
			#end:case
			case 11:
				local5 = 2
				(kernel.ScriptID(456, 0) init:)
				(gnomeGroup
					view: 4591
					loop: -1
					setScript: riddleAlex 0 kernel.ScriptID(456, 0)
				)
				(tmpGnome view: 2002 hide:)
				kernel.UnLoad(128, 459)
				cycles = 2
			#end:case
			case 12:#end:case
			case 13:
				(global0 setMotion: MoveTo ((global0 x:) - 6) (global0 y:) self)
			#end:case
			case 14:
				cycles = 2
			#end:case
			case 15:
				localproc_0(kernel.ScriptID(456, 0))
				(kernel.ScriptID(456, 0) dispose:)
				cycles = 2
			#end:case
			case 16:
				kernel.DisposeScript(456)
				kernel.UnLoad(128, 456)
				cycles = 2
			#end:case
			case 17:
				local5 = 3
				(kernel.ScriptID(4561, 0) init:)
				(gnomeGroup
					view: 4592
					loop: -1
					setScript: riddleAlex 0 kernel.ScriptID(4561, 0)
				)
				(tmpGnome view: 2002 hide:)
				kernel.UnLoad(128, 4591)
				cycles = 2
			#end:case
			case 18:#end:case
			case 19:
				(global0 setMotion: MoveTo ((global0 x:) - 1) (global0 y:) self)
			#end:case
			case 20:
				cycles = 2
			#end:case
			case 21:
				localproc_0(kernel.ScriptID(4561, 0))
				(kernel.ScriptID(4561, 0) dispose:)
				cycles = 2
			#end:case
			case 22:
				kernel.DisposeScript(4561)
				kernel.UnLoad(128, 4561)
				kernel.UnLoad(128, 8933)
				cycles = 2
			#end:case
			case 23:
				local5 = 4
				(kernel.ScriptID(457, 0) init:)
				(gnomeGroup
					view: 4593
					loop: -1
					setScript: riddleAlex 0 kernel.ScriptID(457, 0)
				)
				(tmpGnome view: 2002 hide:)
				kernel.UnLoad(128, 4592)
				cycles = 2
			#end:case
			case 24:#end:case
			case 25:
				cycles = 4
			#end:case
			case 26:
				localproc_0(kernel.ScriptID(457, 0))
				(kernel.ScriptID(457, 0) dispose:)
				cycles = 2
			#end:case
			case 27:
				kernel.DisposeScript(457)
				kernel.UnLoad(128, 457)
				cycles = 2
			#end:case
			case 28:
				local5 = 5
				(kernel.ScriptID(458, 0) init:)
				(gnomeGroup
					view: 4594
					loop: -1
					setScript: riddleAlex 0 kernel.ScriptID(458, 0)
				)
				(tmpGnome view: 2002 hide:)
				kernel.UnLoad(128, 4593)
				cycles = 2
			#end:case
			case 29:#end:case
			case 30:
				localproc_0(kernel.ScriptID(458, 0))
				(kernel.ScriptID(458, 0) dispose:)
				cycles = 2
			#end:case
			case 31:
				kernel.DisposeScript(458)
				kernel.UnLoad(128, 458)
				local5 = 0
				(gnomeGroup
					view: 4544
					setLoop: 1
					cel: 0
					posn: 110 128
					setCycle: End self
				)
				(tmpGnome dispose:)
				kernel.UnLoad(128, 4593)
			#end:case
			case 32:
				(gnomeGroup
					view: 4540
					setScale: Scaler 100 25 126 70
					setLoop: 2
					x: 106
					y: 126
					setCycle: Walk
					setMotion: MoveTo 131 70 self
				)
				kernel.UnLoad(128, 4544)
			#end:case
			case 33:
				(gnomeGroup dispose:)
				(global0
					view: 452
					setLoop: 1
					cel: 0
					cycleSpeed: 6
					setCycle: End self
				)
				(kernel.ScriptID(40, 0) alexInvisible: 0)
			#end:case
			case 34:
				if (kernel.ScriptID(40, 0) alexX:):
					temp0 = (kernel.ScriptID(40, 0) alexX:)
					temp1 = (kernel.ScriptID(40, 0) alexY:)
				else:
					temp0 = (global0 x:)
					temp1 = (global0 y:)
				#endif
				(global0
					posn: temp0 temp1
					setScale: Scaler 100 30 126 70
					reset: 1
				)
				ticks = 4
			#end:case
			case 35:
				(global1 handsOn:)
				(snoreSong play:)
				(snooze1 init: setCycle: Fwd checkDetail:)
				if (kernel.ScriptID(40, 0) oysterDozing:):
					(snooze4 init: setCycle: Fwd checkDetail:)
				#endif
				proc913_3()
				proc913_1(42)
				(global91 say: 2 83 14 3)
				(self dispose:)
				(global103 fade: 0 10 10)
				kernel.DisposeScript(1037)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class riddleAlex(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(gnomeGroup
					setLoop: ((gnomeGroup loop:) + 1)
					x: (register FOLx:)
					cel: 0
				)
				cycles = 4
			#end:case
			case 1:
				(gnomeGroup stopUpd:)
			#end:case
			case 2:
				(global103 number: 452 setLoop: 1 play:)
				(register setLoop: 3 cel: 0 setCycle: End self)
			#end:case
			case 3:
				(global1 handsOn:)
				(global69 disable: 0 1 3)
				if ((global0 heading:) != 270):
					(global0 setHeading: 270)
				#endif
				seconds = 12
			#end:case
			case 4:
				if ((global2 script:) != mainGnomeScript):
					0
				else:
					(global1 handsOff:)
					proc913_1(59)
					cycles = 6
				#endif
			#end:case
			case 5:
				((register gnomeScript:) start: (register startPoint:))
				(gnomeGroup setScript: (register gnomeScript:))
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class giveItemScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				temp2 = (global0 x:)
				temp3 = (global0 y:)
				(kernel.ScriptID(40, 0) alexX: (global0 x:))
				(kernel.ScriptID(40, 0) alexY: (global0 y:))
				match register
					case 37:
						(self setScript: giveGnomeBird self register)
					#end:case
					case 83:
						(self setScript: inkOutAlex self register)
					#end:case
					case 31:
						(self setScript: blowFlute self register)
					#end:case
					else:
						match register
							case 47:
								temp0 = 452
								temp1 = 0
								(temp2 += 2)
								temp4 = 4
							#end:case
							case 68:
								temp4 = 4
								temp0 = 452
								temp1 = 4
							#end:case
							else:
								temp0 = 452
								temp1 = 3
								temp4 = 4
							#end:else
						#end:match
						(global0
							view: temp0
							setLoop: temp1
							normal: 0
							cel: 0
							x: temp2
							y: temp3
							cycleSpeed: 0
							setCycle: CT temp4 1 self
						)
						kernel.UnLoad(128, 900)
					#end:else
				#end:match
			#end:case
			case 1:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class rightInvItem(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				match local5
					case 1:
						if (not proc913_1(145)):
							(global1 givePoints: 2)
						#endif
						kernel.UnLoad(128, 8931)
					#end:case
					case 2:
						if (not proc913_1(146)):
							(global1 givePoints: 2)
						#endif
						kernel.UnLoad(128, 8932)
					#end:case
					case 3:
						if (not proc913_1(147)):
							(global1 givePoints: 2)
						#endif
						kernel.UnLoad(128, 8933)
					#end:case
					case 4:
						if (not proc913_1(148)):
							(global1 givePoints: 2)
						#endif
						kernel.UnLoad(128, 8934)
					#end:case
					case 5:
						if (not proc913_1(149)):
							(global1 givePoints: 2)
						#endif
						kernel.UnLoad(128, 8935)
					#end:case
				#end:match
				(global103 number: 451 setLoop: -1 play:)
				(register
					setLoop: 0
					cel: 3
					z: 0
					setPri: 8
					setMotion: MoveTo (register x:) ((register y:) - 4) self
				)
			#end:case
			case 1:
				(register
					cel: 0
					setLoop: 5
					y: 125
					setCycle: Fwd
					setMotion: MoveTo (register EOLx:) 125 self
				)
			#end:case
			case 2:
				(register loop: 0 cel: 2 setCycle: 0)
				(gnomeGroup setCycle: End self)
			#end:case
			case 3:
				(register y: 126 cel: 0)
				ticks = 4
			#end:case
			case 4:
				(mainGnomeScript cue:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class wrongInvItem(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if (kernel.ScriptID(40, 0) alexInvisible:):
					(global0 view: 452 setLoop: 1 cel: 0 setCycle: End self)
					(kernel.ScriptID(40, 0) alexInvisible: 0)
				else:
					(self cue:)
				#endif
			#end:case
			case 1:
				if (kernel.ScriptID(40, 0) alexX:):
					temp0 = (kernel.ScriptID(40, 0) alexX:)
					temp1 = (kernel.ScriptID(40, 0) alexY:)
				else:
					temp0 = (global0 x:)
					temp1 = (global0 y:)
				#endif
				if ((global0 view:) != 900):
					(global0 reset: 1 posn: temp0 temp1)
				#endif
				cycles = 8
			#end:case
			case 2:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class toTheSea(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				proc913_2(59)
				(global2 drawPic: 450 -32758)
				if (global5 contains: mySentence):
					(mySentence setCycle: 0 setMotion: 0 setScript: 0)
				#endif
				(global0 hide:)
				(global103 number: 457 setLoop: 1 play: self)
				(gnomeGroup
					view: 4542
					setLoop: 0
					cel: 0
					posn: 200 138
					init:
					setCycle: Fwd
				)
			#end:case
			case 1:
				(global104 number: 458 setLoop: 1 play:)
				(gnomeGroup setLoop: 1)
				(global0
					view: 4542
					setLoop: 2
					setPri: 15
					posn: 195 110
					normal: 0
					show:
					cycleSpeed: 10
					setCycle: End self
				)
			#end:case
			case 2:
				(global2 style: 7)
				match local5
					case 1:
						kernel.DisposeScript(455)
					#end:case
					case 2:
						kernel.DisposeScript(456)
					#end:case
					case 3:
						kernel.DisposeScript(4561)
					#end:case
					case 4:
						kernel.DisposeScript(457)
					#end:case
					case 5:
						kernel.DisposeScript(458)
					#end:case
				#end:match
				global160 = 35
				cycles = 10
			#end:case
			case 3:
				(global2 newRoom: 135)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class giveGnomeBird(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global0
					view: 883
					normal: 0
					posn: ((global0 x:) - 1) ((global0 y:) + 1)
					loop: 0
					cycleSpeed: 50
				)
				kernel.UnLoad(128, 900)
				cycles = 6
			#end:case
			case 1:
				(global104 number: 930 setLoop: 1 play:)
				(global0 cel: 0 setCycle: End self)
			#end:case
			case 2:
				if (local4 < 4):
					local4.post('++')
					(state -= 2)
				#endif
				(self cue:)
			#end:case
			case 3:
				(global104 number: 931 setLoop: 1 play: self)
				kernel.UnLoad(132, 930)
				(global0 setLoop: 6 cel: 0 cycleSpeed: 0 setCycle: Fwd)
				if (local5 == 2):
					(kernel.ScriptID(456, 0) setLoop: 1 setCycle: Fwd)
				#endif
			#end:case
			case 4:
				(global0 view: 883 normal: 0 setCycle: 0 loop: 0)
				cycles = 6
			#end:case
			case 5:
				(global104 number: 0)
				kernel.UnLoad(132, 931)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class inkOutAlex(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global91 say: 2 83 14 1 self)
			#end:case
			case 1:
				(global0
					normal: 0
					view: 452
					setLoop: 5
					cel: 0
					normal: 0
					posn: ((global0 x:) + 2) ((global0 y:) + 1)
					cycleSpeed: 2
					setCycle: End self
				)
				kernel.UnLoad(128, 900)
			#end:case
			case 2:
				(global0 setLoop: 6 cel: 0 setCycle: End self)
			#end:case
			case 3:
				(global0 put: 51 450)
				(global69 curIcon: (global69 at: 0))
				(kernel.ScriptID(40, 0) alexInvisible: 1)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class blowFlute(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global0
					normal: 0
					view: 920
					setLoop: 1
					posn: (global0 x:) ((global0 y:) + 1)
					cel: 0
					cycleSpeed: 6
				)
				kernel.UnLoad(128, 900)
				cycles = 4
			#end:case
			case 1:
				(global104 number: 942 setLoop: 1 play: self)
				(global0 setCycle: Fwd)
			#end:case
			case 2:
				if (kernel.ScriptID(40, 0) alexX:):
					temp0 = (kernel.ScriptID(40, 0) alexX:)
					temp1 = (kernel.ScriptID(40, 0) alexY:)
				else:
					temp0 = (global0 x:)
					temp1 = (global0 y:)
				#endif
				(global0 reset: 1 posn: temp0 temp1)
				cycles = 4
			#end:case
			case 3:
				kernel.UnLoad(132, 942)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoEnters(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global0 init: setScale: Scaler 100 30 126 70)
				if (global0 scaler:):
					((global0 scaler:) doit:)
				#endif
				match global12
					case 460:
						(global0 posn: 345 90 setMotion: PolyPath 300 90 self)
					#end:case
					case 470:
						(global0 posn: 130 72 setMotion: PolyPath 134 101 self)
					#end:case
					else:
						(global0
							signal: (| (global0 signal:) 0x4000)
							posn: 228 121
							loop: 0
						)
						ticks = 6
					#end:else
				#end:match
			#end:case
			case 1:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoExits(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					setMotion: PolyPath ((global0 x:) + 15) (global0 y:) self
				)
			#end:case
			case 1:
				(global2 newRoom: 460)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class inToWater(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				if (((mySentence y:) > 158) and (not (sentencePoly points:))):
					(mySentence ignoreActors: 1)
					(global2
						addObstacle:
							(sentencePoly
								type: 2
								init:
									((mySentence x:) - 18)
									(mySentence y:)
									((mySentence x:) - 10)
									((mySentence y:) - 5)
									((mySentence x:) + 17)
									((mySentence y:) - 5)
									((mySentence x:) + 24)
									(mySentence y:)
									((mySentence x:) + 18)
									((mySentence y:) + 17)
									((mySentence x:) - 10)
									((mySentence y:) + 17)
								yourself:
							)
					)
					cycles = 2
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				(global0 setMotion: PolyPath local0 local1 self)
			#end:case
			case 2:
				cycles = 4
			#end:case
			case 3:
				(cond
					case (register == mySentence):
						(myConv add: -1 7 3 17 1 add: -1 7 3 17 2 init: self)
					#end:case
					case 
						(or
							((global0 onControl: 1) == 4)
							((global0 onControl: 1) == 2)
						):
						(global91 say: 7 3 16 1 self)
					#end:case
					case ((global0 onControl: 1) == 8192):
						(myConv add: -1 7 3 17 1 add: -1 7 3 17 2 init: self)
					#end:case
					else:
						cycles = 1
					#end:else
				)
			#end:case
			case 4:
				if 
					(or
						((global0 onControl: 1) == 8192)
						(register == mySentence)
					)
					cycles = 1
				else:
					(global1 handsOn:)
					(self dispose:)
				#endif
			#end:case
			case 5:
				local2 = 1
				(global103 number: 921 setLoop: 1 play:)
				(global0
					view: 309
					cel: 0
					normal: 0
					cycleSpeed: 6
					posn: (global0 x:) ((global0 y:) + 15)
					setCycle: End self
				)
			#end:case
			case 6:
				(global1 handsOn:)
				global160 = 34
				(global2 newRoom: 135)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class sentencePoly(Polygon):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class sentenceFloat(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				seconds = 20
			#end:case
			case 1:
				(mySentence setStep: 1 1 setLoop: 2)
				(cond
					case ((mySentence y:) > 175):
						(mySentence setMotion: MoveTo 135 175 self)
					#end:case
					case ((mySentence y:) > 158):
						(mySentence setMotion: MoveTo 120 154 self)
					#end:case
					else:
						(self dispose:)
					#end:else
				)
			#end:case
			case 2:
				if (((mySentence y:) < 158) and (not (sentencePoly points:))):
					(mySentence ignoreActors: 1)
					(global2
						addObstacle:
							(sentencePoly
								type: 2
								init:
									((mySentence x:) - 18)
									(mySentence y:)
									((mySentence x:) - 10)
									((mySentence y:) - 5)
									((mySentence x:) + 17)
									((mySentence y:) - 5)
									((mySentence x:) + 24)
									(mySentence y:)
									((mySentence x:) + 18)
									((mySentence y:) + 17)
									((mySentence x:) - 10)
									((mySentence y:) + 17)
								yourself:
							)
					)
				#endif
				(self init:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getSentence(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(mySentence setMotion: 0 setScript: 0)
				if (((mySentence y:) > 158) and (not (sentencePoly points:))):
					(mySentence ignoreActors: 1)
					(global2
						addObstacle:
							(sentencePoly
								type: 2
								init:
									((mySentence x:) - 18)
									(mySentence y:)
									((mySentence x:) - 10)
									((mySentence y:) - 5)
									((mySentence x:) + 17)
									((mySentence y:) - 5)
									((mySentence x:) + 24)
									(mySentence y:)
									((mySentence x:) + 18)
									((mySentence y:) + 17)
									((mySentence x:) - 10)
									((mySentence y:) + 17)
								yourself:
							)
					)
				#endif
				if 
					(and
						(or
							((global0 onControl: 1) == 32)
							((global0 onControl: 1) == 64)
						)
						((mySentence y:) > 158)
					)
					local3 = 1
					(global91 say: 11 5 20 1 self)
				else:
					(self cue:)
				#endif
			#end:case
			case 1:
				(global0
					setMotion:
						PolyPath
						(mySentence x:)
						((mySentence y:) - 11)
						self
				)
			#end:case
			case 2:
				(global0 setHeading: 180)
				cycles = 8
			#end:case
			case 3:
				(cond
					case (local3 and ((mySentence y:) > 158)):
						(global91 say: 11 5 20 2 self)
					#end:case
					case ((mySentence y:) > 158):
						(global91 say: 11 5 21 1 self)
					#end:case
					else:
						(self cue:)
					#end:else
				)
			#end:case
			case 4:
				(cond
					case (local3 and ((mySentence y:) > 158)):
						local3 = 0
						(global1 handsOn:)
						(self dispose:)
					#end:case
					case ((mySentence y:) > 160):
						local0 = (global0 x:)
						local1 = ((global0 y:) + 1)
						(self dispose:)
						(mySentence
							setStep: 20 15
							setLoop: 2
							setMotion:
								MoveTo
								((mySentence x:) - 28)
								(mySentence y:)
						)
						(global2 setScript: inToWater 0 mySentence)
					#end:case
					else:
						(self cue:)
					#end:else
				)
			#end:case
			case 5:
				(global2 setScript: pickUpSentence self)
				((global2 obstacles:) delete: sentencePoly)
				(sentencePoly dispose:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class pickUpSentence(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global0
					view: 311
					setLoop: 1
					normal: 0
					cel: 0
					setPri: (global0 priority:)
					posn: ((global0 x:) - 2) ((global0 y:) + 11)
					cycleSpeed: 6
					setCycle: CT 2 1 self
				)
			#end:case
			case 1:
				(mySentence dispose:)
				(global104 number: 924 setLoop: 1 play:)
				(global0 setCycle: End self)
			#end:case
			case 2:
				(global1 givePoints: 1)
				(global0
					reset: 2
					posn: ((global0 x:) + 2) ((global0 y:) - 11)
					get: 50
				)
				cycles = 8
			#end:case
			case 3:
				(global91 say: 11 5 0 0 self)
			#end:case
			case 4:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class resetGnomes(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				match local5
					case 1:
						(mainGnomeScript start: 8)
					#end:case
					case 2:
						(mainGnomeScript start: 12)
					#end:case
					case 3:
						(mainGnomeScript start: 18)
					#end:case
					case 4:
						(mainGnomeScript start: 24)
					#end:case
					case 5:
						(mainGnomeScript start: 29)
					#end:case
				#end:match
				(global2 setScript: mainGnomeScript)
				((gnomeGroup script:)
					state: (((gnomeGroup script:) state:) - 1)
					cue:
				)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoDoVerb(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 12:
				if 
					(or
						((global0 onControl: 1) == 32)
						((global0 onControl: 1) == 64)
					)
					if (global2 script:):
						(kernel.ScriptID(130) next: resetGnomes)
					#endif
					(global2 setScript: 130)
					return 1
				else:
					(global2 setScript: 130)
					return 1
				#endif
			#end:case
			case 31:
				if local5:
					localproc_1(param1)
					return 1
				else:
					return 0
				#endif
			#end:case
			case 37:
				if local5:
					localproc_1(param1)
					return 1
				else:
					return 0
				#endif
			#end:case
			case 83:
				if local5:
					localproc_1(param1)
					return 1
				else:
					return 0
				#endif
			#end:case
			else:
				return 0
			#end:else
		#end:match
	#end:method

#end:class or instance

