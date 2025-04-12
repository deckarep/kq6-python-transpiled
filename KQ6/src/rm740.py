#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 740
import sci_sh
import kernel
import Main
import rgCastle
import n913
import Print
import Conversation
import Scaler
import Polygon
import Feature
import StopWalk
import Timer
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm740 = 0,
	priest = 1,
	vizier = 2,
	genie = 3,
	jollo = 4,
	saladin = 5,
	roomConv = 7,
	door = 8,
	guard3 = 9,
	proc740_10 = 10,
	caliphimallaria = 11,
	grahamvalanice = 12,
	rosella = 13,
	prince = 14,
	beauty = 15,
	redQueen = 16,
	whiteQueen = 17,
	druid1 = 18,
	druid2 = 19,
	druid3 = 20,
	leftGuard = 21,
	rightGuard = 22,
	theGreatEscape = 23,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = 1
local1 = None
local2 = None
local3 = None
local4 = None
local5 = None


@SCI.procedure
def proc740_10():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	if ((global2 curPic:) != 740):
		(global69 disable:)
		(global2 drawPic: 740 10)
	#endif
	(priest
		view: 748
		init:
		setLoop: 0
		posn: 178 139
		setCycle: 0
		cel: 0
		setScale: 0
		signal: 26624
	)
	(saladin
		view: 7411
		init:
		setLoop: 0
		cel: 0
		posn: 183 129
		signal: 26624
		addToPic:
	)
	if proc913_0(15):
		(caliphimallaria init: stopUpd:)
		global164 = 105
		global165 = 155
	else:
		global164 = 116
		global165 = 143
	#endif
	if (((global9 at: 25) owner:) == global11):
		(genie
			view: 7020
			init:
			setLoop: 0
			cel: 0
			posn: 274 160
			scaleSignal: 1
			scaleX: 115
			scaleY: 115
			signal: 26624
			stopUpd:
		)
		(grahamvalanice init: stopUpd:)
		(rosella init: stopUpd:)
		if (kernel.ScriptID(80, 0) tstFlag: 710 16):
			(druid1 init: stopUpd:)
			(druid2 init: stopUpd:)
			(druid3 init: stopUpd:)
			(celeste init: addToPic:)
			(aeriel init: addToPic:)
			(azure init: addToPic:)
			(beauty init: setPri: 15 stopUpd:)
			(prince init: setPri: 14 stopUpd:)
			(redQBody init: addToPic:)
			(whiteQBody init: addToPic:)
			(redQueen init: stopUpd:)
			(whiteQueen init: stopUpd:)
		#endif
	#endif
	(leftGuard init: stopUpd:)
	(rightGuard init: stopUpd:)
	(jollo
		init:
		view: 7463
		loop: 1
		cel: 0
		posn: 116 143
		scaleSignal: 1
		scaleX: 115
		scaleY: 115
		posn: global164 global165
		signal: 26624
		stopUpd:
	)
	(door init: addToPic:)
	(global69 enable:)
#end:procedure

@SCI.instance
class rm740(CastleRoom):
	#property vars (may be empty)
	noun = 3
	picture = 740
	style = 10
	vanishingX = 204
	vanishingY = 99
	autoLoad = 0
	minScaleSize = 82
	maxScaleSize = 108
	minScaleY = 142
	maxScaleY = 189
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self
			addObstacle:
				((Polygon new:)
					type: 2
					init:
						0
						-10
						319
						-10
						319
						189
						228
						121
						221
						121
						221
						134
						120
						134
						0
						179
					yourself:
				)
		)
		(global32 add: roomFeatures eachElementDo: #init)
		if ((global12 == 99) and global100 and kernel.FileIO(10, r"""g""")):
			match
				(Print
					addText: r"""select:"""
					addButton: 1 r"""V wedding""" 0 12
					addButton: 2 r"""A wedding""" 0 26
					init:
				)
				case 1:
					if 
						(Print
							addText: r"""Are Cassima's parents alive?"""
							addButton: 1 r"""No""" 0 12
							addButton: 0 r"""Yes""" 0 26
							init:
						)
						(kernel.ScriptID(80, 0) setFlag: 709 128)
					#endif
					(global102 number: 701 setLoop: -1 play:)
					(kernel.ScriptID(80, 0) setFlag: 709 2)
					(global0 get: 24 get: 31)
					((global9 at: 25) owner: 750)
					((global9 at: 8) owner: 870)
					global12 = 730
				#end:case
				case 2:
					global12 = 180
				#end:case
			#end:match
		#endif
		if (global12 == 180):
			if (global100 and kernel.FileIO(10, r"""g""") and (not (global102 handle:))):
				(global102 number: 743 setLoop: -1 play:)
			#endif
			if 
				(and
					global100
					kernel.FileIO(10, r"""g""")
					(Print
						addText: r"""Are Cassima's parents alive?"""
						addButton: 0 r"""No""" 0 12
						addButton: 1 r"""Yes""" 0 26
						init:
					)
				)
				proc913_1(15)
			#endif
			if 
				(and
					global100
					kernel.FileIO(10, r"""g""")
					(Print
						addText: r"""genie status?"""
						addButton: 0 r"""Killed with peppermint""" 0 12
						addButton: 1 r"""Saved""" 0 26
						init:
					)
				)
				((global9 at: 25) owner: global11)
			#endif
			if 
				(and
					global100
					kernel.FileIO(10, r"""g""")
					(Print
						addText: r"""Found missing treasure?"""
						addButton: 0 r"""No""" 0 12
						addButton: 1 r"""Yes""" 0 26
						init:
					)
				)
				(kernel.ScriptID(80, 0) setFlag: 710 16)
			#endif
			if 
				(and
					global100
					kernel.FileIO(10, r"""g""")
					(Print
						addText: r"""Befriended Court Clown?"""
						addButton: 0 r"""No""" 0 12
						addButton: 1 r"""Yes""" 0 26
						init:
					)
				)
				proc913_1(10)
			#endif
			if (global100 and kernel.FileIO(10, r"""g""")):
				while True: #repeat
					match
						(= temp1
							(Print
								addText: r"""Which ring?"""
								addButton: 1 r"""Cassima has a ring""" 0 12
								addButton: 2 r"""Alex has a ring """ 0 26
								addButton: 3 r"""Left ring at pawn shop""" 0 40
								init:
							)
						)
						case 1:
							((global9 at: 39) owner: 140)
						#end:case
						case 2:
							(global0 get: 39)
						#end:case
						case 3:#end:case
					#end:match
					if temp1:
						(break)
					#endif
				#end:loop
			#endif
			(super init: &rest)
			proc740_10()
			(self setScript: kernel.ScriptID(743, 0))
		else:
			(super init: &rest)
			(global0
				init:
				reset: 3
				setScale: Scaler maxScaleSize minScaleSize maxScaleY minScaleY
			)
			(door init:)
			match global12
				case 790:
					(global0 posn: 222 126)
				#end:case
				else:
					if (kernel.ScriptID(80, 0) tstFlag: 709 2):
						(global0 posn: 131 180)
						(saladin
							posn: 147 187
							init:
							setStep: 5 3
							setCycle: StopWalk -1
							setScale: Scaler 110 93 189 141
						)
						if (not proc913_0(10)):
							(jollo init: stopUpd:)
						#endif
						(kernel.ScriptID(80, 5) actions: guardsActions)
						(kernel.ScriptID(80, 6) actions: guardsActions)
						(guard3 actions: guardsActions)
						(self setScript: kernel.ScriptID(742, 0))
					else:
						(global0 posn: 128 185)
						(self setScript: kernel.ScriptID(741, 0))
					#endif
				#end:else
			#end:match
			((global0 scaler:) doit:)
		#endif
		if (not script):
			(global1 handsOn:)
		#endif
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				((global69 curIcon:) == (global69 at: 3))
				((param1 type:) != 16384)
				(not (param1 modifiers:))
				(not (vizier onMe: param1))
				(not (jollo onMe: param1))
				(or
					(((param1 type:) & 0x0004) and ((param1 message:) == 13))
					((param1 type:) & 0x0001)
				)
			)
			(global1 handsOff:)
			(kernel.ScriptID(740, 7) add: -1 3 2 21 0)
			(global2 setScript: kernel.ScriptID(742, 1))
			(param1 claimed: 1)
			(param1 claimed:)
			return
		else:
			(super handleEvent: param1)
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
				if (global5 contains: genie):
					(genie setScript: 0)
				#endif
				(global2 newRoom: 790)
			#end:case
		)
		if (global0 scaler:):
			(cond
				case ((global0 y:) < 142):
					if local0:
						local0 = 0
						(global0 setScale: Scaler 83 43 142 120)
					#endif
				#end:case
				case (not local0):
					local0 = 1
					(global0
						setScale:
							Scaler
							maxScaleSize
							minScaleSize
							maxScaleY
							minScaleY
					)
				#end:case
			)
		#endif
		(super doit: &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = (22 if (kernel.ScriptID(80, 0) tstFlag: 710 2048) else 21)
		(return
			match param1
				case 1:
					(global91 say: noun param1 temp0)
					1
				#end:case
				case 2:
					(kernel.ScriptID(80, 0) setFlag: 710 2048)
					(global91 say: noun param1 temp0)
					1
				#end:case
				else:
					(super doVerb: param1)
					1
				#end:else
			#end:match
		)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super dispose:)
		kernel.DisposeScript(741)
		kernel.DisposeScript(742)
		kernel.DisposeScript(743)
		kernel.DisposeScript(964)
		kernel.DisposeScript(939)
		kernel.DisposeScript(752)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (global90 == 2):
			(global2 setScript: kernel.ScriptID(52))
		else:
			(global2 newRoom: 94)
		#endif
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(bTimer dispose: delete:)
		(pTimer dispose: delete:)
		(lgTimer dispose: delete:)
		(rgTimer dispose: delete:)
		(super newRoom: param1)
	#end:method

#end:class or instance

@SCI.instance
class roomFeatures(Feature):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		y = 1
		sightAngle = 26505
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((global2 curPic:) == 740):
			(return
				(or
					(and
						(&
							temp0 = kernel.OnControl(4, (param1 x:), (param1 y:))
							0x0002
						)
						noun = 17
					)
					((temp0 & 0x0004) and noun = 18)
					((temp0 & 0x0008) and noun = 9)
					((temp0 & 0x0010) and noun = 15)
				)
			)
		else:
			return 0
		#endif
	#end:method

#end:class or instance

@SCI.instance
class priest(Prop):
	#property vars (may be empty)
	x = 179
	y = 128
	view = 741
	cel = 1
	signal = 20480
	cycleSpeed = 8
	detailLevel = 2
	
#end:class or instance

@SCI.instance
class vizier(Prop):
	#property vars (may be empty)
	x = 176
	y = 142
	view = 741
	loop = 2
	cel = 2
	signal = 20480
	cycleSpeed = 8
	detailLevel = 2
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(and
				(super onMe: param1)
				(or
					(and
						(view == 741)
						(loop == 2)
						(((param1 x:) - nsLeft) < 15)
						noun = 6
					)
					noun = 4
				)
			)
		)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc999_5(param1, 5, 2):
			(roomConv add: -1 noun param1 0 1)
			(global2 setScript: kernel.ScriptID(742, 1))
		else:
			(super doVerb: param1 &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class genie(Prop):
	#property vars (may be empty)
	x = 176
	y = 142
	view = 741
	loop = 3
	cel = 5
	signal = 16384
	cycleSpeed = 8
	detailLevel = 2
	
#end:class or instance

@SCI.instance
class saladin(Actor):
	#property vars (may be empty)
	x = 176
	y = 142
	noun = 7
	view = 736
	loop = 3
	cel = 5
	signal = 16384
	cycleSpeed = 8
	detailLevel = 2
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((global66 doit: param1) == -32768):
			param1 = 0
		#endif
		temp0 = (22 if (kernel.ScriptID(80, 0) tstFlag: 710 2048) else 21)
		(global91 say: noun param1 temp0)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self setHeading: 0)
	#end:method

#end:class or instance

@SCI.instance
class jollo(Prop):
	#property vars (may be empty)
	x = 61
	y = 167
	view = 746
	cel = 1
	signal = 20480
	cycleSpeed = 8
	detailLevel = 2
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self view: 7464 loop: 0 cel: 0 stopUpd:)
		(super cue:)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				(global91 say: 19 1 0 1)
			#end:case
			case 2:
				if (kernel.ScriptID(80, 0) tstFlag: 710 2048):
					(global91 say: 19 2 22 1)
				else:
					(global91 say: 19 2 21 1)
				#endif
			#end:case
			case 5:
				if (kernel.ScriptID(80, 0) tstFlag: 710 2048):
					(global91 say: 19 5 22 1)
				else:
					(global91 say: 19 5 21 1)
				#endif
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class door(Prop):
	#property vars (may be empty)
	x = 220
	y = 108
	noun = 8
	approachX = 220
	approachY = 108
	view = 740
	priority = 8
	signal = 16401
	detailLevel = 2
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				if (kernel.ScriptID(80, 0) tstFlag: 710 2048):
					0
				else:
					(global91 say: noun param1 21)
				#endif
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class roomConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class prince(Prop):
	#property vars (may be empty)
	x = 255
	y = 180
	view = 7020
	loop = 1
	priority = 15
	signal = 26640
	detailLevel = 2
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super cue:)
		match local1.post('++')
			case 1:
				(pTimer setReal: self 5)
			#end:case
			case 2:
				(self setCycle: Beg self)
			#end:case
			case 3:
				(self addToPic:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class beauty(Prop):
	#property vars (may be empty)
	x = 242
	y = 188
	view = 7020
	loop = 2
	priority = 14
	signal = 26640
	detailLevel = 2
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super cue:)
		match local2.post('++')
			case 1:
				(bTimer setCycle: self 5)
			#end:case
			case 2:
				(self cel: 2)
				(bTimer setCycle: self 5)
			#end:case
			case 3:
				(self cel: 3)
				(bTimer setCycle: self 5)
			#end:case
			case 4:
				(self setCycle: Beg self)
			#end:case
			case 5:
				(bTimer setReal: self 3)
			#end:case
			case 6:
				local2 = 0
				(self setCycle: End self)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class azure(View):
	#property vars (may be empty)
	x = 20
	y = 185
	view = 747
	loop = 2
	signal = 26624
	
#end:class or instance

@SCI.instance
class aeriel(View):
	#property vars (may be empty)
	x = 31
	y = 176
	view = 747
	loop = 2
	cel = 1
	signal = 26624
	
#end:class or instance

@SCI.instance
class celeste(View):
	#property vars (may be empty)
	x = 55
	y = 170
	view = 747
	loop = 2
	cel = 2
	signal = 26624
	
#end:class or instance

@SCI.instance
class druid1(Prop):
	#property vars (may be empty)
	x = 94
	y = 189
	view = 747
	loop = 3
	signal = 26624
	detailLevel = 2
	
#end:class or instance

@SCI.instance
class druid2(Prop):
	#property vars (may be empty)
	x = 69
	y = 189
	view = 747
	loop = 3
	cel = 1
	signal = 26624
	detailLevel = 2
	
#end:class or instance

@SCI.instance
class druid3(Prop):
	#property vars (may be empty)
	x = 120
	y = 179
	view = 747
	loop = 3
	cel = 2
	signal = 26624
	detailLevel = 2
	
#end:class or instance

@SCI.instance
class caliphimallaria(Prop):
	#property vars (may be empty)
	x = 128
	y = 147
	view = 7450
	loop = 2
	signal = 26624
	detailLevel = 2
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super cue:)
		match local5.post('++')
			case 1:
				(self setCycle: Beg self)
			#end:case
			case 2:
				(cTimer setReal: self kernel.Random(2, 4))
			#end:case
			case 3:
				local5 = 0
				(self setCycle: End self)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class grahamvalanice(Prop):
	#property vars (may be empty)
	x = 216
	y = 144
	view = 745
	loop = 4
	cel = 1
	signal = 26624
	detailLevel = 2
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self stopUpd:)
	#end:method

#end:class or instance

@SCI.instance
class rosella(Prop):
	#property vars (may be empty)
	x = 235
	y = 145
	view = 745
	loop = 4
	cel = 2
	signal = 26624
	detailLevel = 2
	
#end:class or instance

@SCI.instance
class leftGuard(Prop):
	#property vars (may be empty)
	x = 148
	y = 189
	view = 7473
	loop = 1
	signal = 26624
	
	@classmethod
	def cue(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super cue:)
		if (param1 == 99):
			local4 = param1
		#endif
		param1 = 0
		match local4.post('++')
			case 1:
				(lgTimer setReal: self kernel.Random(1, 2))
			#end:case
			case 2:
				(self cel: 2)
				(lgTimer setReal: self kernel.Random(1, 2))
			#end:case
			case 3:
				(self cel: 3)
				(lgTimer setReal: self kernel.Random(1, 2))
			#end:case
			case 4:
				(self setCycle: Beg self)
			#end:case
			case 5:
				(lgTimer setReal: self kernel.Random(2, 3))
			#end:case
			case 6:
				local4 = 0
				(self setCycle: End self)
			#end:case
			case 100:
				local4 = 0
				(lgTimer dispose:)
				(self cel: 0 setCycle: 0 stopUpd:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class rightGuard(Prop):
	#property vars (may be empty)
	x = 174
	y = 189
	view = 7473
	signal = 26624
	
	@classmethod
	def cue(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super cue:)
		if (param1 == 99):
			local3 = param1
		#endif
		param1 = 0
		match local3.post('++')
			case 1:
				(rgTimer setReal: self kernel.Random(1, 2))
			#end:case
			case 2:
				(self cel: 1)
				(rgTimer setReal: self kernel.Random(1, 2))
			#end:case
			case 3:
				(self cel: 2)
				(rgTimer setReal: self kernel.Random(1, 2))
			#end:case
			case 4:
				(self setCycle: Beg self)
			#end:case
			case 5:
				(rgTimer setReal: self kernel.Random(2, 3))
			#end:case
			case 6:
				local3 = 0
				(self setCycle: End self)
			#end:case
			case 100:
				local3 = 0
				(rgTimer dispose:)
				(self cel: 0 setCycle: 0 stopUpd:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class redQueen(Prop):
	#property vars (may be empty)
	x = 287
	y = 172
	view = 7471
	priority = 15
	signal = 26640
	detailLevel = 2
	
#end:class or instance

@SCI.instance
class redQBody(View):
	#property vars (may be empty)
	x = 286
	y = 181
	view = 747
	signal = 26624
	
#end:class or instance

@SCI.instance
class whiteQBody(View):
	#property vars (may be empty)
	x = 296
	y = 175
	view = 747
	cel = 1
	signal = 26624
	
#end:class or instance

@SCI.instance
class whiteQueen(Prop):
	#property vars (may be empty)
	x = 296
	y = 159
	view = 7471
	loop = 1
	priority = 14
	signal = 26640
	detailLevel = 2
	
#end:class or instance

@SCI.instance
class guard3(Actor):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class guardsActions(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 1
		temp1 = (22 if (kernel.ScriptID(80, 0) tstFlag: 710 2048) else 21)
		(= temp2
			if (((CueObj client:) modNum:) == -1):
				global11
			else:
				((CueObj client:) modNum:)
			#endif
		)
		if kernel.Message(0, temp2, ((CueObj client:) noun:), param1, temp1, 1):
			(global91 say: ((CueObj client:) noun:) param1 temp1)
		else:
			temp0 = 0
		#endif
		return temp0
	#end:method

#end:class or instance

@SCI.instance
class bTimer(Timer):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class pTimer(Timer):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class lgTimer(Timer):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class rgTimer(Timer):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class cTimer(Timer):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class theGreatEscape(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global69 disable: 6)
				(global102 number: 742 loop: -1 play:)
				(vizier cycleSpeed: 6 setCycle: CT 9 1 self)
			#end:case
			case 1:
				(door hide:)
				(door approachVerbs: 5)
				(vizier setCycle: End self)
			#end:case
			case 2:
				(door show: cel: 1 stopUpd:)
				(vizier dispose:)
				cycles = 3
			#end:case
			case 3:
				kernel.UnLoad(128, 7413)
				(global69 enable: 6)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

