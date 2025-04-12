#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 470
import sci_sh
import kernel
import Main
import KQ6Room
import n913
import Conversation
import Osc
import PolyPath
import Polygon
import Feature
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm470 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = [5, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
local37
local49
local55 = None
local56 = None
local57 = None
local58 = None
local59 = None
local60 = None
local61 = 3
local62 = None
local63
local73 = [276, 280, 284, 283, 195, 210, 213, 232]
local81 = [181, 182, 185, 181, 165, 158, 158, 170]
local89 = [4701, 4701, 4701, 4701, 4701, 4701, 4701, 4701]
local97 = [1, 2, 5, 4, 6, 7, 8, 10]
local105
local110 = [273, 279, 230]
local113 = [179, 179, 168]
local116 = [4703, 4703, 4703]
local119 = [0, 2, 9]
local122 = [135, 177, 146, 136]
local126 = [169, 179, 184, 157]
local130 = [57, 30, 149, 103, 220]
local135 = [147, 165, 156, 135, 163]
local140 = None
local141 = None
local142 = None


@SCI.procedure
def localproc_0():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	temp0 = 0
	while (temp0 < 8): # inline for
		(local63[temp0] = (aCat new:)
			view: local89[temp0]
			loop: local97[temp0]
			x: local73[temp0]
			y: local81[temp0]
			signal: 20480
			addToPic:
		)
		# for:reinit
		temp0.post('++')
	#end:loop
#end:procedure

@SCI.procedure
def localproc_1():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	temp0 = 0
	while (temp0 < 3): # inline for
		(local105[temp0] = (aCat new:)
			view: local116[temp0]
			loop: local119[temp0]
			x: local110[temp0]
			y: local113[temp0]
			signal: 20480 9
			init:
			stopUpd:
		)
		# for:reinit
		temp0.post('++')
	#end:loop
#end:procedure

@SCI.procedure
def localproc_2():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(global103 number: 473 setLoop: -1 play:)
	temp0 = 0
	while (temp0 < 3): # inline for
		(local105[temp0] setCycle: Fwd)
		# for:reinit
		temp0.post('++')
	#end:loop
#end:procedure

@SCI.procedure
def localproc_3():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(global103 stop:)
	temp0 = 0
	while (temp0 < 3): # inline for
		(local105[temp0] setCycle: Beg)
		# for:reinit
		temp0.post('++')
	#end:loop
#end:procedure

@SCI.procedure
def localproc_4():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	temp0 = 0
	while (temp0 < 3): # inline for
		(local105[temp0] stopUpd:)
		# for:reinit
		temp0.post('++')
	#end:loop
#end:procedure

@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class rm470(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 470
	horizon = 0
	walkOffEdge = 1
	autoLoad = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (and global100 (global12 == 99) kernel.FileIO(10, r"""g""")):
			(global0 get: 49 get: 46 get: 19 get: 11 get: 8)
		#endif
		(super init: &rest)
		(global1 handsOn:)
		(self
			addObstacle:
				((Polygon new:)
					type: 2
					init: 223 189 129 165 141 151 213 151 319 170 319 189
					yourself:
				)
				((Polygon new:)
					type: 2
					init:
						0
						189
						0
						140
						85
						161
						88
						167
						53
						170
						54
						174
						121
						174
						137
						181
						131
						189
					yourself:
				)
				((Polygon new:)
					type: 2
					init:
						319
						129
						124
						129
						172
						148
						89
						148
						52
						132
						70
						126
						67
						124
						44
						126
						39
						135
						0
						131
						0
						0
						319
						0
					yourself:
				)
		)
		(global102 number: 470 setLoop: -1 play:)
		(global32
			add: swamp1 swamp2 farTrees pathage milkers dogTree log
			eachElementDo: #init
		)
		localproc_0()
		localproc_1()
		(bump init: stopUpd:)
		(cond
			case 
				(and
					(not proc913_0(127))
					(((global9 at: 49) owner:) == global11)
				):
				(mater
					view: 475
					z: 60
					posn: 274 189
					setLoop: 5
					cel: 6
					setPri: 5
					init:
					stopUpd:
				)
				(local37[0] = (slimeBall new:)
					x: 31
					y: 148
					setLoop: 0
					cel: 3
					setPri: 15
					init:
					addToPic:
				)
				(local37[1] = (slimeBall new:)
					x: 32
					y: 154
					setLoop: 1
					cel: 3
					setPri: 15
					init:
					addToPic:
				)
				global167 = 5
				global168 = 5
				(stick init: cue: 1)
				local55 = 2
			#end:case
			case (proc913_0(127) and (((global9 at: 49) owner:) == global11)):
				global167 = 5
				global168 = 5
				(stick init: cue: 1)
				local55 = 2
			#end:case
			case proc913_0(134):
				(stick init: cue: 0)
				local55 = 1
			#end:case
			else:
				(stick init: cue: 1)
				local55 = 0
			#end:else
		)
		(doggy init: stopUpd:)
		(global0 init: scaleSignal: 4 scaleX: 128 scaleY: 128 maxScale: 128)
		(global2 setScript: egoEnters)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super doit:)
		(cond
			case (global2 script:):#end:case
			case ((global0 edgeHit:) == 3):
				(global2 setScript: walkOut 0 1)
			#end:case
			case ((global0 x:) <= 8):
				(global2 setScript: walkOut 0 0)
			#end:case
			case ((global0 onControl: 1) == 2):
				(global2 setScript: quagmire)
			#end:case
			case ((global0 inRect: 104 142 190 167) and (not local2)):
				local2 = 1
				kernel.Load(128, 4731)
				kernel.Load(143, 470)
			#end:case
			case ((local0 == 5) and (local1 == 5)):
				local0 = 6
				local1 = 6
				(global1 handsOff:)
				(local140 = (Prop new:) view: 476 init: setScript: stepOnFrog)
			#end:case
		)
		kernel.Palette(6, 64, 68, -10)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		kernel.DisposeScript(939)
		(super dispose:)
	#end:method

#end:class or instance

@SCI.instance
class log(Feature):
	#property vars (may be empty)
	x = 30
	y = 165
	noun = 14
	onMeCheck = 128
	
#end:class or instance

@SCI.instance
class farTrees(Feature):
	#property vars (may be empty)
	x = 168
	y = 10
	noun = 12
	onMeCheck = 8
	
#end:class or instance

@SCI.instance
class pathage(Feature):
	#property vars (may be empty)
	noun = 13
	onMeCheck = 64
	
#end:class or instance

@SCI.instance
class dogTree(Feature):
	#property vars (may be empty)
	x = 40
	y = 17
	noun = 5
	onMeCheck = 16
	approachX = 80
	approachY = 146
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self approachVerbs: 5)
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				local0.post('++')
				(global91 say: 5 1 0 1)
			#end:case
			case 0:
				(global91 say: 5 0 0 1)
			#end:case
			case 2:
				(global2 setScript: bowWow 0 param1)
			#end:case
			case 5:
				(global2 setScript: bowWow 0 param1)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class swamp1(Feature):
	#property vars (may be empty)
	x = 180
	y = 10
	noun = 6
	onMeCheck = 4
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 44:
				(global91 say: 6 44 10 1)
			#end:case
			case 0:
				(global91 say: 6 0 0 1)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class swamp2(Feature):
	#property vars (may be empty)
	x = 180
	y = 10
	noun = 6
	onMeCheck = 2
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 44:
				(cond
					case proc913_0(68):
						(global91 say: 6 44 12 1)
					#end:case
					case (local55 == 2):
						(global91 say: 6 44 11)
					#end:case
					case local55 = 1:
						(global2 setScript: teaParty)
					#end:case
				)
			#end:case
			case 0:
				(global91 say: 6 0 0 1)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class milkers(Feature):
	#property vars (may be empty)
	x = 60
	y = 120
	noun = 9
	nsTop = 96
	nsLeft = 47
	nsBottom = 117
	nsRight = 89
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				if (global0 has: 22):
					local1.post('++')
					(global91 say: 9 5 20 1)
				else:
					(global2 setScript: getMilk)
				#endif
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class mater(Actor):
	#property vars (may be empty)
	noun = 11
	view = 475
	loop = 6
	priority = 15
	signal = 16400
	
#end:class or instance

@SCI.instance
class milkWeed(View):
	#property vars (may be empty)
	x = 9
	y = 117
	noun = 9
	view = 4701
	loop = 5
	signal = 16384
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				if (global0 has: 22):
					(global91 say: 9 5 20 1)
				else:
					(global91 say: 9 5 19 1)
				#endif
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class bump(Prop):
	#property vars (may be empty)
	x = 28
	y = 178
	z = 25
	noun = 7
	approachX = 88
	approachY = 177
	approachDist = 20
	view = 4700
	loop = 1
	signal = 20480
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self approachVerbs: 2 setPri: 15)
		(super init:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 44:
				match local55
					case 0:
						(global91 say: 7 44 13 1)
					#end:case
					case 1:
						(global91 say: 7 44 14 1)
					#end:case
					else:
						(global91 say: 7 44 15 1)
					#end:else
				#end:match
			#end:case
			case 1:
				match local55
					case 0:
						(global91 say: 7 1 13 1)
					#end:case
					case 1:
						(global91 say: 7 1 14 1)
					#end:case
					else:
						(global91 say: 7 1 15 1)
					#end:else
				#end:match
			#end:case
			case 5:
				match local55
					case 0:
						(global91 say: 7 5 13 1)
					#end:case
					case 1:
						(global91 say: 7 5 14 1)
					#end:case
					else:
						(global91 say: 7 5 15 1)
					#end:else
				#end:match
			#end:case
			case 2:
				(cond
					case (local55 == 2):
						(global91 say: 7 5 15 1)
					#end:case
					case (local55 == 0):
						(global91 say: 7 2 13 1)
					#end:case
					case (global167.post('++') == 1):
						(self setScript: fightTalk self)
					#end:case
					case (global167 == 2):
						(global91 say: 7 2 26 0 stick)
					#end:case
					else:
						(global91 say: 7 2 17 0 stick)
					#end:else
				)
			#end:case
			case 34:
				if (kernel.ScriptID(40, 0) stickTalk:):
					global168 = 3
					(global0 put: 49 bump)
					(global2 setScript: bumpMaterToss)
				else:
					(global91 say: 7 34 18 1)
				#endif
			#end:case
			case 34:
				if (local55 == 1):
					(global91 say: 7 8 14 1)
				else:
					(global91 say: 7 0 13 1)
				#endif
			#end:case
			else:
				match local55
					case 0:
						(global91 say: 7 0 13 1)
					#end:case
					case 1:
						(global91 say: 7 0 14 0)
					#end:case
					else:
						(global91 say: 7 5 15 1)
					#end:else
				#end:match
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class bumpArm(Prop):
	#property vars (may be empty)
	x = 30
	y = 150
	view = 474
	loop = 5
	priority = 15
	signal = 16400
	
#end:class or instance

@SCI.instance
class stick(Prop):
	#property vars (may be empty)
	x = 287
	y = 189
	z = 66
	noun = 10
	approachDist = 300
	view = 4700
	loop = 2
	priority = 4
	signal = 20496
	cycleSpeed = 8
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if 
			(and
				(kernel.ScriptID(40, 0) stickTalk:)
				(((global9 at: 49) owner:) != global11)
			)
			(self view: 475 setLoop: 1)
			local55 = 1
		else:
			(self cue:)
		#endif
		(super init:)
	#end:method

	@classmethod
	def cue(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self view: 4700 setLoop: 2 cel: param1 stopUpd:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				match local55
					case 0:
						(global91 say: 10 5 13 1)
					#end:case
					case 1:
						(global91 say: 10 5 14 1)
					#end:case
					else:
						(global91 say: 10 5 15 1)
					#end:else
				#end:match
			#end:case
			case 1:
				match local55
					case 0:
						(global91 say: 10 1 13 1)
					#end:case
					case 1:
						(global91 say: 10 1 14 1)
					#end:case
					else:
						(global91 say: 10 1 15 1)
					#end:else
				#end:match
			#end:case
			case 2:
				(global2 setScript: sTalkToStick)
			#end:case
			case 34:
				(cond
					case (local55 == 0):
						(global91 say: 10 0 13 1)
					#end:case
					case local56:
						(global0 put: 49 470)
						(global2 setScript: egoMaterThrowAway)
					#end:case
					else:
						(global2 setScript: egoMaterToss)
					#end:else
				)
			#end:case
			case 44:
				match local55
					case 0:
						(global91 say: 10 44 13 1)
					#end:case
					case 1:
						(global91 say: 10 44 14 1)
					#end:case
					else:
						(global91 say: 10 44 15 1)
					#end:else
				#end:match
			#end:case
			else:
				match local55
					case 0:
						(global91 say: 10 0 13 1)
					#end:case
					case 1:
						(global91 say: 10 0 14 0)
					#end:case
					else:
						(global91 say: 10 0 15 1)
					#end:else
				#end:match
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class fightTalk(Script):
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
				(myConv add: -1 7 2 16 1 add: -1 7 2 16 2 init: self)
			#end:case
			case 2:
				(global0 cel: 2)
				cycles = 2
			#end:case
			case 3:
				(global91 say: 7 2 16 3 self)
			#end:case
			case 4:
				cycles = 2
			#end:case
			case 5:
				(global91 say: 7 2 16 4 self)
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				(global91 say: 7 2 16 5 self)
			#end:case
			case 8:
				cycles = 2
			#end:case
			case 9:
				(global91 say: 7 2 16 6 self)
			#end:case
			case 10:
				cycles = 2
			#end:case
			case 11:
				(global91 say: 7 2 16 7 self)
			#end:case
			case 12:
				cycles = 2
			#end:case
			case 13:
				(global91 say: 7 2 16 8 self)
			#end:case
			case 14:
				(global0 reset:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class stickTalking(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(myConv add: -1 10 2 22 1 add: -1 10 2 22 2 init: self)
			#end:case
			case 1:
				(global0 cel: 2)
				cycles = 2
			#end:case
			case 2:
				(global91 say: 10 2 22 3 self)
			#end:case
			case 3:
				(global1 handsOn:)
				(global0 reset:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class slimeBall(Prop):
	#property vars (may be empty)
	noun = 8
	approachX = 87
	approachY = 181
	approachDist = 20
	view = 4702
	loop = 1
	signal = 22544
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(self approachVerbs: 5 9)
		(super init: &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 44:
				if (not proc913_0(68)):
					(global2 setScript: getOoze)
				else:
					(global91 say: 6 44 12 1)
				#endif
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class aCat(Prop):
	#property vars (may be empty)
	noun = 4
	cycleSpeed = 4
	
	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 2:
				(global2 setScript: doPussy 0 2)
			#end:case
			case 5:
				(global2 setScript: doPussy 0 5)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class doggy(Prop):
	#property vars (may be empty)
	x = 25
	y = 19
	noun = 5
	view = 4700
	priority = 1
	signal = 16400
	cycleSpeed = 1
	
#end:class or instance

@SCI.instance
class slime(Actor):
	#property vars (may be empty)
	yStep = 36
	view = 474
	loop = 4
	signal = 16384
	xStep = 68
	
#end:class or instance

@SCI.instance
class materSlime(Actor):
	#property vars (may be empty)
	yStep = 36
	view = 475
	signal = 20496
	xStep = 68
	
#end:class or instance

@SCI.instance
class egoEnters(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				match global12
					case 450:
						(global0
							setLoop: 3
							posn: 162 249
							setMotion: MoveTo 165 185 self
						)
						if (not kernel.Random(0, 1)):
							(local142 = (Prop new:)
								view: 476
								init:
								setScript: kernel.Clone(sFrogX)
							)
						#endif
					#end:case
					else:
						(global0
							setLoop: 0
							posn: -10 135
							setMotion: MoveTo 10 139 self
						)
						if (not kernel.Random(0, 1)):
							(local141 = (Prop new:)
								view: 476
								init:
								setScript: kernel.Clone(sFrogY)
							)
						#endif
						if (not kernel.Random(0, 1)):
							(local142 = (Prop new:)
								view: 476
								init:
								setScript: kernel.Clone(sFrogX)
							)
						#endif
					#end:else
				#end:match
			#end:case
			case 1:
				(global1 handsOn:)
				(global0 reset:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walkOut(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				if register:
					(global0 setMotion: MoveTo (global0 x:) 255 self)
				else:
					(global0 setMotion: MoveTo -25 (global0 y:) self)
				#endif
			#end:case
			case 1:
				if register:
					(global2 newRoom: 450)
				else:
					(global2 newRoom: 480)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getMilk(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(stick stopUpd:)
				(bump stopUpd:)
				(global0 setMotion: PolyPath 64 141 self)
			#end:case
			case 1:
				(global0 setHeading: 0)
				kernel.UnLoad(128, 474)
				kernel.UnLoad(128, 475)
				ticks = 6
			#end:case
			case 2:
				(global0
					view: 472
					normal: 0
					loop: 1
					cel: 0
					posn: 64 141
					setCycle: End self
				)
			#end:case
			case 3:
				(global91 say: 9 5 19 1 self)
			#end:case
			case 4:
				if (not proc913_0(130)):
					proc913_1(130)
					(global1 givePoints: 1)
				#endif
				(global0
					reset: 6
					posn: 53 133
					get: 22
					setMotion: PolyPath 79 145 self
				)
			#end:case
			case 5:
				(global0 setHeading: 335)
				cycles = 8
			#end:case
			case 6:
				(self setScript: bowWow self 99)
			#end:case
			case 7:
				(global91 say: 9 5 19 2 self)
			#end:case
			case 8:
				(global1 handsOn:)
				(global0 reset: 3)
				kernel.UnLoad(128, 472)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getOoze(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setHeading: 270 self)
			#end:case
			case 1:
				if (not proc913_0(68)):
					proc913_1(68)
					(global1 givePoints: 1)
				#endif
				(global0
					view: 474
					setLoop: 10
					posn: 71 189
					cel: 0
					normal: 0
					setCycle: End self
				)
			#end:case
			case 2:
				(global91 say: 8 44 0 1 self)
			#end:case
			case 3:
				(global0 setCycle: Beg self)
			#end:case
			case 4:
				(global0 posn: 87 181 reset: 1 setMotion: MoveTo 107 167 self)
			#end:case
			case 5:
				(global1 handsOn:)
				(global0 setHeading: 180)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class doPussy(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				if (register == 5):
					(global91 say: 4 5 0 1 self)
				else:
					(global91 say: 4 2 0 1 self)
				#endif
			#end:case
			case 1:
				if (register == 5):
					(global0 setMotion: PolyPath 205 186 self)
				else:
					(self cue:)
				#endif
			#end:case
			case 2:
				if (register == 5):
					(global0 setHeading: 135)
					ticks = 6
				else:
					(self cue:)
				#endif
			#end:case
			case 3:
				(global103 number: 473 setLoop: 1 play:)
				(local105[0] view: 4701 startUpd: setCycle: End self)
			#end:case
			case 4:
				(global103 number: 473 setLoop: 1 play:)
				(local105[0] setCycle: Beg)
				(local105[1] view: 4701 startUpd: setCycle: End self)
			#end:case
			case 5:
				(global103 number: 473 setLoop: 1 play:)
				(local105[1] setCycle: Beg)
				(local105[2] view: 4701 startUpd: setCycle: End self)
			#end:case
			case 6:
				if (local62 < 3):
					local62.post('++')
					(local105[2] setCycle: Beg)
					(state -= 4)
					(self cue:)
				else:
					(local105[2] setCycle: Beg self)
				#endif
			#end:case
			case 7:
				localproc_4()
				if (register == 5):
					(global0 setHeading: 315)
				#endif
				cycles = 10
			#end:case
			case 8:
				if (register == 5):
					(self setScript: bowWow self 99)
				else:
					(self cue:)
				#endif
			#end:case
			case 9:
				if (register == 5):
					(global91 say: 4 5 0 2 self)
				else:
					(self cue:)
				#endif
			#end:case
			case 10:
				(global1 handsOn:)
				local62 = 0
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class teaParty(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(kernel.ScriptID(40, 0) stickTalk: 1)
				(cond
					case (local57 >= 3):
						(global91 say: 6 44 11 1)
						(self dispose:)
					#end:case
					case proc913_0(68):
						(global91 say: 6 44 12 1)
						(self dispose:)
					#end:case
					else:
						(global1 handsOff:)
						ticks = 4
					#end:else
				)
			#end:case
			case 1:
				(global0 setMotion: PolyPath 132 155 self)
			#end:case
			case 2:
				(global0
					view: 472
					setLoop: 0
					normal: 0
					cel: 0
					posn: ((global0 x:) + 6) ((global0 y:) + 4)
					cycleSpeed: 6
					setCycle: CT 2 1 self
				)
			#end:case
			case 3:
				(global103 number: 924 setLoop: 1 play:)
				(global0 setCycle: End self)
			#end:case
			case 4:
				(global0 posn: ((global0 x:) - 11) ((global0 y:) - 8) reset: 4)
				ticks = 4
			#end:case
			case 5:
				(global0
					setLoop: 4
					setMotion: MoveTo ((global0 x:) - 6) ((global0 y:) - 4)
				)
				(stick view: 475 setLoop: 1 setCycle: End self)
			#end:case
			case 6:
				(stick setCycle: Beg self)
			#end:case
			case 7:
				if (local57 == 0):
					(myConv
						add: -1 6 44 4 1
						add: -1 6 44 4 2
						add: -1 6 44 4 3
						init: self
					)
				else:
					(self cue:)
				#endif
			#end:case
			case 8:
				match temp0 = kernel.Random(0, 2)
					case 0:
						(global91 say: 6 44 8 1 self)
					#end:case
					case 1:
						(global91 say: 6 44 9 1 self)
					#end:case
					case 2:
						(global91 say: 6 44 7 1 self)
					#end:case
				#end:match
			#end:case
			case 9:
				match local57
					case 0:
						(self setScript: teaTalk self 1)
					#end:case
					case 1:
						(self setScript: teaTalk self 2)
					#end:case
					case 2:
						(self setScript: teaTalk self 3)
					#end:case
				#end:match
			#end:case
			case 10:
				local57.post('++')
				(global0 reset:)
				(stick setLoop: 2 setCycle: Osc 1 self)
				cycles = 1
			#end:case
			case 11:
				(global103 number: 478 setLoop: 1 play:)
			#end:case
			case 12:
				(global1 handsOn:)
				(stick cue: 0)
				proc913_1(134)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class teaTalk(Script):
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
				match register
					case 1:
						(global91 say: 6 44 4 4 self)
					#end:case
					case 2:
						(global91 say: 6 44 5 1 self)
					#end:case
					case 3:
						(global91 say: 6 44 28 1 self)
					#end:case
				#end:match
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				match register
					case 1:
						(global91 say: 6 44 4 5 self)
					#end:case
					case 2:
						(global91 say: 6 44 5 2 self)
					#end:case
					case 3:
						(global91 say: 6 44 28 2 self)
					#end:case
				#end:match
			#end:case
			case 4:
				cycles = 2
			#end:case
			case 5:
				match register
					case 1:
						(global91 say: 6 44 4 6 self)
					#end:case
					case 2:
						(global91 say: 6 44 5 3 self)
					#end:case
					case 3:
						(global91 say: 6 44 28 3 self)
					#end:case
				#end:match
			#end:case
			case 6:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class backOut(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global0 setMotion: PolyPath 155 186 self)
			#end:case
			case 1:
				(global0 setHeading: 0)
				cycles = 2
			#end:case
			case 2:
				(global0 view: 4702 setLoop: 2 normal: 0 setCycle: 0)
				cycles = 2
			#end:case
			case 3:
				kernel.Load(128, 475)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class materTossSlime(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				kernel.UnLoad(128, 474)
				(mater setLoop: 8 cel: 0 z: 0 posn: 275 129 setCycle: End self)
			#end:case
			case 1:
				(mater cel: 0)
				(global103 number: 0 stop:)
				ticks = 4
			#end:case
			case 2:
				(global103 number: 476 setLoop: 1 play:)
				(materSlime
					view: 475
					posn: 217 111
					ignoreActors:
					init:
					setLoop: 10
					cel: 0
					setPri: 15
				)
				ticks = 4
			#end:case
			case 3:
				(materSlime posn: 172 109 forceUpd:)
				ticks = 2
			#end:case
			case 4:
				(materSlime
					view: 4702
					setLoop: 1
					cel: 0
					posn: 121 108
					forceUpd:
				)
				ticks = 2
			#end:case
			case 5:
				(materSlime posn: 87 119 forceUpd:)
				ticks = 2
			#end:case
			case 6:
				(materSlime cel: 0 posn: 87 119 forceUpd:)
				ticks = 4
			#end:case
			case 7:
				(local49[local59] = (slimeBall new:)
					x: 31
					y: 189
					z: 41
					setLoop: 0
					priority: 15
					init:
					setCycle: End self
				)
				(materSlime setCycle: 0 hide: dispose:)
			#end:case
			case 8:
				(local49[local59] addToPic:)
				if (local59 < 2):
					local59.post('++')
					(state -= 9)
				#endif
				(self cue:)
			#end:case
			case 9:
				(mater
					view: 475
					setLoop: 5
					cel: 6
					x: 274
					y: 189
					z: 60
					setPri: 5
					stopUpd:
				)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoMaterToss(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: PolyPath 55 172 self)
			#end:case
			case 1:
				(global0 setHeading: 225)
				cycles = 8
			#end:case
			case 2:
				(global91 say: 10 34 24 0 self)
			#end:case
			case 3:
				(global1 handsOn:)
				local56 = 1
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoMaterThrowAway(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				proc913_1(127)
				(global91 say: 10 34 25 1 self)
			#end:case
			case 1:
				(global0 setMotion: PolyPath 108 149 self)
			#end:case
			case 2:
				(global0 view: 472 normal: 0 setLoop: 2 setCycle: End self)
				(global103 number: 0 stop:)
				(global103 number: 474 setLoop: 1 play:)
			#end:case
			case 3:
				(global0 posn: 108 149 reset: 0)
				(self setScript: egoMaterFlight self)
			#end:case
			case 4:
				cycles = 8
			#end:case
			case 5:
				(myConv
					add: -1 10 34 25 3
					add: -1 10 34 25 4
					add: -1 10 34 25 5
					add: -1 10 34 25 6
					add: -1 10 34 25 7
					add: -1 10 34 25 8
					add: -1 10 34 25 9
					add: -1 10 34 25 10
					add: -1 10 34 25 11
					init: self
				)
			#end:case
			case 6:
				(global1 handsOn:)
				local55 = 2
				(stick cue: 1)
				global168 = 2
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoMaterFlight(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(mater posn: ((global0 x:) + 36) ((global0 y:) - 61) init:)
				ticks = 4
			#end:case
			case 1:
				(mater posn: ((mater x:) + 31) ((mater y:) - 10))
				ticks = 4
			#end:case
			case 2:
				(mater posn: ((mater x:) + 31) ((mater y:) + 2))
				ticks = 4
			#end:case
			case 3:
				(mater posn: ((mater x:) + 28) ((mater y:) + 10))
				ticks = 4
			#end:case
			case 4:
				(mater posn: ((mater x:) + 18) ((mater y:) + 13))
				ticks = 4
			#end:case
			case 5:
				(mater posn: ((mater x:) + 6) ((mater y:) + 16))
				ticks = 4
			#end:case
			case 6:
				(global103 number: 0 stop:)
				(global103 number: 475 setLoop: 1 play:)
				(mater posn: 266 131)
				ticks = 12
			#end:case
			case 7:
				(mater setLoop: 5 posn: 274 130 cel: 0 setCycle: End self)
			#end:case
			case 8:
				(mater setLoop: 6 posn: 266 131 startUpd: forceUpd:)
				cycles = 4
			#end:case
			case 9:
				(global91 say: 10 34 25 2 self)
			#end:case
			case 10:
				(mater setLoop: 6 setMotion: MoveTo 270 140 self)
			#end:case
			case 11:
				(mater setLoop: 9 posn: 279 139 cel: 0 setCycle: End self)
				(global103 number: 477 setLoop: 1 play:)
			#end:case
			case 12:
				(mater dispose:)
				ticks = 4
			#end:case
			case 13:
				(global103 number: 0 stop:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class bowWow(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				match register
					case 2:
						(global91 say: 5 2 0 1 self)
					#end:case
					case 5:
						(global91 say: 5 5 0 1 self)
					#end:case
					else:
						(self cue:)
					#end:else
				#end:match
			#end:case
			case 1:
				(doggy setCycle: End self)
			#end:case
			case 2:
				(global103 number: 0 stop:)
				(global103 number: 472 setLoop: 1 play:)
				ticks = 30
			#end:case
			case 3:
				(doggy setCel: 1)
				if local61.post('--'):
					(state -= 3)
				else:
					(doggy setCycle: Beg)
				#endif
				ticks = 30
			#end:case
			case 4:
				if (register == 5):
					(global91 say: 5 5 0 2 self)
				else:
					(self cue:)
				#endif
			#end:case
			case 5:
				(global1 handsOn:)
				(doggy stopUpd:)
				local61 = 3
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class theBattle(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				local58.post('++')
				(stick view: 475 setLoop: 4 cel: 0 setCycle: End self)
			#end:case
			case 1:
				(global103 number: 0 stop:)
				(global103 number: 476 setLoop: 1 play:)
				(slime
					posn: kernel.Random(248, 252) kernel.Random(88, 92)
					illegalBits: 0
					ignoreActors:
					init:
					setLoop: 3
					cel: 0
					setPri: 15
					setCycle: Fwd
					setMotion: MoveTo kernel.Random(180, 185) kernel.Random(60, 65) self
				)
			#end:case
			case 2:
				(slime setMotion: MoveTo kernel.Random(115, 122) kernel.Random(75, 82) self)
			#end:case
			case 3:
				(slime
					cel: 1
					setMotion: MoveTo kernel.Random(68, 74) kernel.Random(110, 115) self
				)
			#end:case
			case 4:
				if (mod local58 2):
					temp0 = 0
				else:
					temp0 = 1
				#endif
				(local37[local58] = (slimeBall new:)
					view: 474
					x: (31 if temp0 else 28)
					y: (189 if temp0 else 188)
					z: (41 if temp0 else 35)
					setLoop: (0 if temp0 else 1)
					priority: 15
					init:
				)
				if temp0:
					(local37[local58] setCycle: End self)
				else:
					cycles = 4
				#endif
				(slime setCycle: 0 dispose:)
				(stick cel: 0)
			#end:case
			case 5:
				if (local58 < 2):
					(local37[local58] ignoreActors: 1 addToPic:)
					(self init:)
				else:
					(global103 stop:)
					(global0 reset: 3)
					(stick cue: 0)
					local60 = 1
					local55 = 2
					(self dispose:)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class bumpMaterToss(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				if (not proc913_0(139)):
					proc913_1(139)
					(global1 givePoints: 3)
				#endif
				(global0 setMotion: PolyPath 87 177 self)
			#end:case
			case 1:
				(global0
					view: 474
					setLoop: 4
					cel: 0
					posn: 70 185
					normal: 0
					cycleSpeed: 8
					setCycle: End self
				)
			#end:case
			case 2:
				(bumpArm
					init:
					view: 474
					setLoop: 5
					setCel: 0
					cycleSpeed: 6
					setCycle: CT 2 1 self
				)
			#end:case
			case 3:
				(global0 reset: 1)
				(bumpArm setCycle: End self)
			#end:case
			case 4:
				cycles = 2
			#end:case
			case 5:
				(myConv
					add: -1 7 34 14 1
					add: -1 7 34 14 2
					add: -1 7 34 14 3
					add: -1 7 34 14 4
					add: -1 7 34 14 5
					add: -1 7 34 14 6
					init: self
				)
			#end:case
			case 6:
				(global0 setScript: backOut self)
			#end:case
			case 7:
				(self setScript: bumpMaterFlight self)
			#end:case
			case 8:
				(mater setScript: materTossSlime self)
				(self setScript: theBattle self)
			#end:case
			case 9:#end:case
			case 10:
				(stick cue: 0)
				kernel.UnLoad(128, 474)
				kernel.UnLoad(128, 475)
				(myConv
					add: -1 7 34 14 7
					add: -1 7 34 14 8
					add: -1 7 34 14 9
					add: -1 7 34 14 10
					add: -1 7 34 14 11
					init: self
				)
			#end:case
			case 11:
				((global9 at: 49) owner: global11)
				(global103 number: 961 setLoop: 1 play:)
				(mater init: view: 4700 setLoop: 1 cel: 2)
				(slimeBall addToPic:)
				ticks = 120
			#end:case
			case 12:
				(global1 handsOn:)
				(mater cel: 1 forceUpd:)
				(stick cue: 1)
				global168 = 2
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class bumpMaterFlight(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(bump hide:)
				(bumpArm
					view: 4741
					init:
					posn: 29 154
					setLoop: 0
					cel: 0
					setPri: 15
					ignoreActors: 1
					setCycle: End self
				)
			#end:case
			case 1:
				ticks = 30
			#end:case
			case 2:
				(bumpArm setLoop: 1 setCycle: Fwd)
				seconds = 3
			#end:case
			case 3:
				(bumpArm setLoop: 2 cel: 0 setCycle: End self)
			#end:case
			case 4:
				(global103 number: 474 setLoop: 1 play:)
				(mater view: 475 loop: 6 posn: 61 145 init:)
				(bump show:)
				(bumpArm dispose:)
				ticks = 4
			#end:case
			case 5:
				(mater posn: 85 118)
				ticks = 4
			#end:case
			case 6:
				(mater posn: 121 97)
				ticks = 4
			#end:case
			case 7:
				(mater posn: 153 82)
				ticks = 4
			#end:case
			case 8:
				(mater posn: 193 78)
				ticks = 4
			#end:case
			case 9:
				(mater posn: 230 83)
				ticks = 4
			#end:case
			case 10:
				(mater posn: 260 90)
				ticks = 4
			#end:case
			case 11:
				(global103 number: 0 stop:)
				(global103 number: 475 setLoop: 1 play:)
				(stick view: 475 setLoop: 11 cel: 0 setCycle: Fwd)
				(mater posn: 280 97)
				ticks = 4
			#end:case
			case 12:
				(mater posn: 270 108)
				ticks = 4
			#end:case
			case 13:
				(mater posn: 263 131)
				ticks = 4
			#end:case
			case 14:
				(stick view: 475 setLoop: 1 cel: 0 stopUpd:)
				(mater setLoop: 5 posn: 274 129 setCycle: End self)
			#end:case
			case 15:
				(mater
					view: 475
					setLoop: 5
					cel: 6
					x: 274
					y: 189
					z: 60
					setPri: 5
				)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class sTalkToStick(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				if (((global0 x:) != 121) and ((global0 y:) != 147)):
					(global0 setMotion: PolyPath 121 147 self)
				else:
					cycles = 2
				#endif
			#end:case
			case 1:
				register = kernel.GetAngle((global0 x:), (global0 y:), 292, 135)
				cycles = 2
			#end:case
			case 2:
				if ((global0 heading:) != register):
					proc913_4(global0, 292, 135, self)
				else:
					cycles = 2
				#endif
			#end:case
			case 3:
				cycles = 4
			#end:case
			case 4:
				global168.post('++')
				(cond
					case (local55 == 0):
						global168.post('--')
						(global91 say: 10 2 13 1 self)
					#end:case
					case (global168 == 1):
						(self setScript: stickTalking self)
					#end:case
					case (global168 == 2):
						(global91 say: 10 2 27 0 self)
					#end:case
					case (((global9 at: 49) owner:) != global11):
						(global91 say: 10 2 23 0 self)
					#end:case
					else:
						(global91 say: 10 2 15 1 self)
					#end:else
				)
			#end:case
			case 5:
				if (local55 == 1):
					(stick cue: 0)
				else:
					(stick cue: 1)
				#endif
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class quagmire(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 view: 4731 normal: 0 setLoop: 0 cel: 0 posn: 151 160)
				ticks = 10
			#end:case
			case 1:
				(global0
					cycleSpeed: 8
					moveSpeed: 15
					setCycle: End self
					setMotion: MoveTo 211 131
				)
				cycles = 2
			#end:case
			case 2:#end:case
			case 3:
				(global91 say: 6 3 0 1 self)
			#end:case
			case 4:
				(global103 number: 0 stop:)
				(global103 number: 477 setLoop: -1 play:)
				(global0
					view: 473
					setMotion: 0
					setLoop: 0
					cel: 0
					cycleSpeed: 12
				)
				cycles = 2
			#end:case
			case 5:
				(global0 setCycle: End self)
			#end:case
			case 6:
				(global0 setLoop: 1 cel: 0 cycleSpeed: 15 setCycle: End self)
			#end:case
			case 7:
				(global91 say: 6 3 0 2 self)
			#end:case
			case 8:
				proc0_1(36)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class sFrogY(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				register = kernel.Random(0, 3)
				(client
					loop: 2
					cel: 0
					x: local122[register]
					y: local126[register]
					signal: 26640
				)
				cycles = 1
			#end:case
			case 1:
				cycles = kernel.Random(4, 8)
			#end:case
			case 2:
				(client setCycle: CT 3 1 self)
			#end:case
			case 3:
				(client posn: (client x:) ((client y:) + 15) setCycle: End self)
			#end:case
			case 4:
				if ((client y:) < 195):
					state = 0
					cycles = 1
				else:
					(client dispose:)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class sFrogX(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				register = kernel.Random(0, 4)
				(client
					loop: 1
					cel: 0
					x: local130[register]
					y: local135[register]
					signal: 26640
				)
				cycles = 1
			#end:case
			case 1:
				cycles = kernel.Random(4, 8)
			#end:case
			case 2:
				if proc999_5(register, 0, 1):
					(client setCycle: CT 9 1 self)
				else:
					(state += 2)
					(client setCycle: End self)
				#endif
			#end:case
			case 3:
				(client posn: ((client x:) + 66) ((client y:) - 8) cel: 0)
				cycles = kernel.Random(2, 4)
			#end:case
			case 4:
				(client setCycle: End self)
			#end:case
			case 5:
				(client dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class stepOnFrog(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(client posn: 46 168 cel: 0 setLoop: 1 setCycle: CT 9 1 self)
			#end:case
			case 1:
				(global1 handsOff:)
				(global0 setMotion: PolyPath 103 160 self)
			#end:case
			case 2:
				(global103 number: 475 setLoop: 1 play:)
				(client
					setLoop: 3
					posn: 109 164
					setPri: 1
					ignoreActors: 1
					addToPic:
				)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

