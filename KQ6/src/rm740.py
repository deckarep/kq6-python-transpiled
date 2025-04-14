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
	if (global2._send('curPic:') != 740):
		global69._send('disable:')
		global2._send('drawPic:', 740, 10)
	#endif
	priest._send(
		'view:', 748,
		'init:',
		'setLoop:', 0,
		'posn:', 178, 139,
		'setCycle:', 0,
		'cel:', 0,
		'setScale:', 0,
		'signal:', 26624
	)
	saladin._send(
		'view:', 7411,
		'init:',
		'setLoop:', 0,
		'cel:', 0,
		'posn:', 183, 129,
		'signal:', 26624,
		'addToPic:'
	)
	if proc913_0(15):
		caliphimallaria._send('init:', 'stopUpd:')
		global164 = 105
		global165 = 155
	else:
		global164 = 116
		global165 = 143
	#endif
	if (global9._send('at:', 25)._send('owner:') == global11):
		genie._send(
			'view:', 7020,
			'init:',
			'setLoop:', 0,
			'cel:', 0,
			'posn:', 274, 160,
			'scaleSignal:', 1,
			'scaleX:', 115,
			'scaleY:', 115,
			'signal:', 26624,
			'stopUpd:'
		)
		grahamvalanice._send('init:', 'stopUpd:')
		rosella._send('init:', 'stopUpd:')
		if kernel.ScriptID(80, 0)._send('tstFlag:', 710, 16):
			druid1._send('init:', 'stopUpd:')
			druid2._send('init:', 'stopUpd:')
			druid3._send('init:', 'stopUpd:')
			celeste._send('init:', 'addToPic:')
			aeriel._send('init:', 'addToPic:')
			azure._send('init:', 'addToPic:')
			beauty._send('init:', 'setPri:', 15, 'stopUpd:')
			prince._send('init:', 'setPri:', 14, 'stopUpd:')
			redQBody._send('init:', 'addToPic:')
			whiteQBody._send('init:', 'addToPic:')
			redQueen._send('init:', 'stopUpd:')
			whiteQueen._send('init:', 'stopUpd:')
		#endif
	#endif
	leftGuard._send('init:', 'stopUpd:')
	rightGuard._send('init:', 'stopUpd:')
	jollo._send(
		'init:',
		'view:', 7463,
		'loop:', 1,
		'cel:', 0,
		'posn:', 116, 143,
		'scaleSignal:', 1,
		'scaleX:', 115,
		'scaleY:', 115,
		'posn:', global164, global165,
		'signal:', 26624,
		'stopUpd:'
	)
	door._send('init:', 'addToPic:')
	global69._send('enable:')
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
		self._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 0, -10, 319, -10, 319, 189, 228, 121, 221, 121, 221, 134, 120, 134, 0, 179,
					'yourself:'
				)
		)
		global32._send('add:', roomFeatures, 'eachElementDo:', #init)
		if ((global12 == 99) and global100 and kernel.FileIO(10, r"""g""")):
			match
				Print._send(
					'addText:', r"""select:""",
					'addButton:', 1, r"""V wedding""", 0, 12,
					'addButton:', 2, r"""A wedding""", 0, 26,
					'init:'
				)
				case 1:
					if 
						Print._send(
							'addText:', r"""Are Cassima's parents alive?""",
							'addButton:', 1, r"""No""", 0, 12,
							'addButton:', 0, r"""Yes""", 0, 26,
							'init:'
						)
						kernel.ScriptID(80, 0)._send('setFlag:', 709, 128)
					#endif
					global102._send('number:', 701, 'setLoop:', -1, 'play:')
					kernel.ScriptID(80, 0)._send('setFlag:', 709, 2)
					global0._send('get:', 24, 'get:', 31)
					global9._send('at:', 25)._send('owner:', 750)
					global9._send('at:', 8)._send('owner:', 870)
					global12 = 730
				#end:case
				case 2:
					global12 = 180
				#end:case
			#end:match
		#endif
		if (global12 == 180):
			if (global100 and kernel.FileIO(10, r"""g""") and (not global102._send('handle:'))):
				global102._send('number:', 743, 'setLoop:', -1, 'play:')
			#endif
			if 
				(and
					global100
					kernel.FileIO(10, r"""g""")
					Print._send(
						'addText:', r"""Are Cassima's parents alive?""",
						'addButton:', 0, r"""No""", 0, 12,
						'addButton:', 1, r"""Yes""", 0, 26,
						'init:'
					)
				)
				proc913_1(15)
			#endif
			if 
				(and
					global100
					kernel.FileIO(10, r"""g""")
					Print._send(
						'addText:', r"""genie status?""",
						'addButton:', 0, r"""Killed with peppermint""", 0, 12,
						'addButton:', 1, r"""Saved""", 0, 26,
						'init:'
					)
				)
				global9._send('at:', 25)._send('owner:', global11)
			#endif
			if 
				(and
					global100
					kernel.FileIO(10, r"""g""")
					Print._send(
						'addText:', r"""Found missing treasure?""",
						'addButton:', 0, r"""No""", 0, 12,
						'addButton:', 1, r"""Yes""", 0, 26,
						'init:'
					)
				)
				kernel.ScriptID(80, 0)._send('setFlag:', 710, 16)
			#endif
			if 
				(and
					global100
					kernel.FileIO(10, r"""g""")
					Print._send(
						'addText:', r"""Befriended Court Clown?""",
						'addButton:', 0, r"""No""", 0, 12,
						'addButton:', 1, r"""Yes""", 0, 26,
						'init:'
					)
				)
				proc913_1(10)
			#endif
			if (global100 and kernel.FileIO(10, r"""g""")):
				while True: #repeat
					match
						(= temp1
							Print._send(
								'addText:', r"""Which ring?""",
								'addButton:', 1, r"""Cassima has a ring""", 0, 12,
								'addButton:', 2, r"""Alex has a ring """, 0, 26,
								'addButton:', 3, r"""Left ring at pawn shop""", 0, 40,
								'init:'
							)
						)
						case 1:
							global9._send('at:', 39)._send('owner:', 140)
						#end:case
						case 2:
							global0._send('get:', 39)
						#end:case
						case 3:#end:case
					#end:match
					if temp1:
						(break)
					#endif
				#end:loop
			#endif
			super._send('init:', &rest)
			proc740_10()
			self._send('setScript:', kernel.ScriptID(743, 0))
		else:
			super._send('init:', &rest)
			global0._send(
				'init:',
				'reset:', 3,
				'setScale:', Scaler, maxScaleSize, minScaleSize, maxScaleY, minScaleY
			)
			door._send('init:')
			match global12
				case 790:
					global0._send('posn:', 222, 126)
				#end:case
				else:
					if kernel.ScriptID(80, 0)._send('tstFlag:', 709, 2):
						global0._send('posn:', 131, 180)
						saladin._send(
							'posn:', 147, 187,
							'init:',
							'setStep:', 5, 3,
							'setCycle:', StopWalk, -1,
							'setScale:', Scaler, 110, 93, 189, 141
						)
						if (not proc913_0(10)):
							jollo._send('init:', 'stopUpd:')
						#endif
						kernel.ScriptID(80, 5)._send('actions:', guardsActions)
						kernel.ScriptID(80, 6)._send('actions:', guardsActions)
						guard3._send('actions:', guardsActions)
						self._send('setScript:', kernel.ScriptID(742, 0))
					else:
						global0._send('posn:', 128, 185)
						self._send('setScript:', kernel.ScriptID(741, 0))
					#endif
				#end:else
			#end:match
			global0._send('scaler:')._send('doit:')
		#endif
		if (not script):
			global1._send('handsOn:')
		#endif
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		if 
			(and
				(global69._send('curIcon:') == global69._send('at:', 3))
				(param1._send('type:') != 16384)
				(not param1._send('modifiers:'))
				(not vizier._send('onMe:', param1))
				(not jollo._send('onMe:', param1))
				(or
					((param1._send('type:') & 0x0004) and (param1._send('message:') == 13))
					(param1._send('type:') & 0x0001)
				)
			)
			global1._send('handsOff:')
			kernel.ScriptID(740, 7)._send('add:', -1, 3, 2, 21, 0)
			global2._send('setScript:', kernel.ScriptID(742, 1))
			param1._send('claimed:', 1)
			param1._send('claimed:')
			return
		else:
			super._send('handleEvent:', param1)
		#endif
	#end:method

	@classmethod
	def doit():
		temp0 = global0._send('onControl:', 1)
		(cond
			case script: 0#end:case
			case (temp0 & 0x4000):
				if global5._send('contains:', genie):
					genie._send('setScript:', 0)
				#endif
				global2._send('newRoom:', 790)
			#end:case
		)
		if global0._send('scaler:'):
			(cond
				case (global0._send('y:') < 142):
					if local0:
						local0 = 0
						global0._send('setScale:', Scaler, 83, 43, 142, 120)
					#endif
				#end:case
				case (not local0):
					local0 = 1
					global0._send(
						'setScale:', Scaler, maxScaleSize, minScaleSize, maxScaleY, minScaleY
					)
				#end:case
			)
		#endif
		super._send('doit:', &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		temp0 = (22 if kernel.ScriptID(80, 0)._send('tstFlag:', 710, 2048) else 21)
		(return
			match param1
				case 1:
					global91._send('say:', noun, param1, temp0)
					1
				#end:case
				case 2:
					kernel.ScriptID(80, 0)._send('setFlag:', 710, 2048)
					global91._send('say:', noun, param1, temp0)
					1
				#end:case
				else:
					super._send('doVerb:', param1)
					1
				#end:else
			#end:match
		)
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(741)
		kernel.DisposeScript(742)
		kernel.DisposeScript(743)
		kernel.DisposeScript(964)
		kernel.DisposeScript(939)
		kernel.DisposeScript(752)
	#end:method

	@classmethod
	def cue():
		if (global90 == 2):
			global2._send('setScript:', kernel.ScriptID(52))
		else:
			global2._send('newRoom:', 94)
		#endif
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		bTimer._send('dispose:', 'delete:')
		pTimer._send('dispose:', 'delete:')
		lgTimer._send('dispose:', 'delete:')
		rgTimer._send('dispose:', 'delete:')
		super._send('newRoom:', param1)
	#end:method

#end:class or instance

@SCI.instance
class roomFeatures(Feature):
	#property vars (may be empty)
	@classmethod
	def init():
		super._send('init:', &rest)
		y = 1
		sightAngle = 26505
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		if (global2._send('curPic:') == 740):
			(return
				(or
					(and
						(&
							temp0 = kernel.OnControl(4, param1._send('x:'), param1._send('y:'))
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
		(return
			(and
				super._send('onMe:', param1)
				(or
					(and
						(view == 741)
						(loop == 2)
						((param1._send('x:') - nsLeft) < 15)
						noun = 6
					)
					noun = 4
				)
			)
		)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		if proc999_5(param1, 5, 2):
			roomConv._send('add:', -1, noun, param1, 0, 1)
			global2._send('setScript:', kernel.ScriptID(742, 1))
		else:
			super._send('doVerb:', param1, &rest)
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
		if (global66._send('doit:', param1) == -32768):
			param1 = 0
		#endif
		temp0 = (22 if kernel.ScriptID(80, 0)._send('tstFlag:', 710, 2048) else 21)
		global91._send('say:', noun, param1, temp0)
	#end:method

	@classmethod
	def cue():
		self._send('setHeading:', 0)
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
		self._send('view:', 7464, 'loop:', 0, 'cel:', 0, 'stopUpd:')
		super._send('cue:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				global91._send('say:', 19, 1, 0, 1)
			#end:case
			case 2:
				if kernel.ScriptID(80, 0)._send('tstFlag:', 710, 2048):
					global91._send('say:', 19, 2, 22, 1)
				else:
					global91._send('say:', 19, 2, 21, 1)
				#endif
			#end:case
			case 5:
				if kernel.ScriptID(80, 0)._send('tstFlag:', 710, 2048):
					global91._send('say:', 19, 5, 22, 1)
				else:
					global91._send('say:', 19, 5, 21, 1)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
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
		match param1
			case 5:
				if kernel.ScriptID(80, 0)._send('tstFlag:', 710, 2048):
					0
				else:
					global91._send('say:', noun, param1, 21)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
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
		super._send('cue:')
		match local1.post('++')
			case 1:
				pTimer._send('setReal:', self, 5)
			#end:case
			case 2:
				self._send('setCycle:', Beg, self)
			#end:case
			case 3:
				self._send('addToPic:')
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
		super._send('cue:')
		match local2.post('++')
			case 1:
				bTimer._send('setCycle:', self, 5)
			#end:case
			case 2:
				self._send('cel:', 2)
				bTimer._send('setCycle:', self, 5)
			#end:case
			case 3:
				self._send('cel:', 3)
				bTimer._send('setCycle:', self, 5)
			#end:case
			case 4:
				self._send('setCycle:', Beg, self)
			#end:case
			case 5:
				bTimer._send('setReal:', self, 3)
			#end:case
			case 6:
				local2 = 0
				self._send('setCycle:', End, self)
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
		super._send('cue:')
		match local5.post('++')
			case 1:
				self._send('setCycle:', Beg, self)
			#end:case
			case 2:
				cTimer._send('setReal:', self, kernel.Random(2, 4))
			#end:case
			case 3:
				local5 = 0
				self._send('setCycle:', End, self)
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
		self._send('stopUpd:')
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
		super._send('cue:')
		if (param1 == 99):
			local4 = param1
		#endif
		param1 = 0
		match local4.post('++')
			case 1:
				lgTimer._send('setReal:', self, kernel.Random(1, 2))
			#end:case
			case 2:
				self._send('cel:', 2)
				lgTimer._send('setReal:', self, kernel.Random(1, 2))
			#end:case
			case 3:
				self._send('cel:', 3)
				lgTimer._send('setReal:', self, kernel.Random(1, 2))
			#end:case
			case 4:
				self._send('setCycle:', Beg, self)
			#end:case
			case 5:
				lgTimer._send('setReal:', self, kernel.Random(2, 3))
			#end:case
			case 6:
				local4 = 0
				self._send('setCycle:', End, self)
			#end:case
			case 100:
				local4 = 0
				lgTimer._send('dispose:')
				self._send('cel:', 0, 'setCycle:', 0, 'stopUpd:')
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
		super._send('cue:')
		if (param1 == 99):
			local3 = param1
		#endif
		param1 = 0
		match local3.post('++')
			case 1:
				rgTimer._send('setReal:', self, kernel.Random(1, 2))
			#end:case
			case 2:
				self._send('cel:', 1)
				rgTimer._send('setReal:', self, kernel.Random(1, 2))
			#end:case
			case 3:
				self._send('cel:', 2)
				rgTimer._send('setReal:', self, kernel.Random(1, 2))
			#end:case
			case 4:
				self._send('setCycle:', Beg, self)
			#end:case
			case 5:
				rgTimer._send('setReal:', self, kernel.Random(2, 3))
			#end:case
			case 6:
				local3 = 0
				self._send('setCycle:', End, self)
			#end:case
			case 100:
				local3 = 0
				rgTimer._send('dispose:')
				self._send('cel:', 0, 'setCycle:', 0, 'stopUpd:')
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
		temp0 = 1
		temp1 = (22 if kernel.ScriptID(80, 0)._send('tstFlag:', 710, 2048) else 21)
		(= temp2
			if (CueObj._send('client:')._send('modNum:') == -1):
				global11
			else:
				CueObj._send('client:')._send('modNum:')
			#endif
		)
		if kernel.Message(0, temp2, CueObj._send('client:')._send('noun:'), param1, temp1, 1):
			global91._send('say:', CueObj._send('client:')._send('noun:'), param1, temp1)
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
		match state = param1
			case 0:
				global69._send('disable:', 6)
				global102._send('number:', 742, 'loop:', -1, 'play:')
				vizier._send('cycleSpeed:', 6, 'setCycle:', CT, 9, 1, self)
			#end:case
			case 1:
				door._send('hide:')
				door._send('approachVerbs:', 5)
				vizier._send('setCycle:', End, self)
			#end:case
			case 2:
				door._send('show:', 'cel:', 1, 'stopUpd:')
				vizier._send('dispose:')
				cycles = 3
			#end:case
			case 3:
				kernel.UnLoad(128, 7413)
				global69._send('enable:', 6)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

