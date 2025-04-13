#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 800
import sci_sh
import kernel
import Main
import rgCastle
import Conversation
import PolyPath
import Polygon
import Feature
import Motion
import User
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm800 = 0,
	proc800_1 = 1,
	roomConv = 2,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = [0, 189, 0, 0, 319, 0, 319, 189, 207, 189, 207, 186, 285, 186, 212, 143, 75, 143, 16, 186, 161, 186, 161, 189]
local25 = [75, 152, 99, 152, 99, 159, 75, 159]
local33 = [197, 147, 197, 149, 165, 149, 165, 158, 205, 158, 205, 160, 113, 160, 113, 147]
local49 = [288, 187, 212, 143, 77, 143, 22, 187]
local57 = [0, -10, 319, -10, 319, 189, 295, 189, 0, 189, 0, 186, 287, 186, 211, 143, 119, 143, 119, 147, 201, 147, 201, 152, 99, 152, 99, 144, 74, 144, 52, 161, 0, 161]
local91 = [79, 82, 98, 82, 192, 155, 192, 151, 99, 78, 88, 78, 88, 76, 110, 76, 238, -10, 231, -10, 108, 73, 63, 73]
local115 = None
local116 = None
local117 = [0, 0, 198, 155, 79, 77, 211, 5]
local125 = [188, 185, 188, 189, 110, 189]
local131 = None
local132 = None
local133 = None
local134 = None
local135 = None


@SCI.procedure
def localproc_0(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	if (argc == 1):
		local0 = param1[0]
	#endif
	if global2._send('obstacles:'):
		global2._send('obstacles:')._send('dispose:')
		global2._send('obstacles:', 0)
	#endif
	mainPoly._send('type:', 2)
	match local0
		case 1:
			global2._send(
				'addObstacle:', mainPoly._send(
						'type:', 3,
						'points:', @local49,
						'size:', 4,
						'yourself:'
					), Poly1._send('type:', 2, 'points:', @local25, 'size:', 4, 'yourself:'), Poly2._send(
						'type:', 2,
						'points:', @local33,
						'size:', 8,
						'yourself:'
					)
			)
		#end:case
		case 2:
			backPost._send('setPri:', 0, 'stopUpd:')
			global2._send(
				'addObstacle:', mainPoly._send(
						'type:', 3,
						'points:', @local91,
						'size:', 12,
						'yourself:'
					)
			)
		#end:case
		case 3:
			global2._send('addObstacle:', mainPoly._send('points:', @local57, 'size:', 17, 'yourself:'))
		#end:case
	#end:match
#end:procedure

@SCI.procedure
def proc800_1():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	global2._send('drawPic:', global2._send('picture:'))
	if (local0 == 3):
		upHallleft._send('addToPic:')
		upHalleft2._send('addToPic:')
		upStairs._send('addToPic:')
		upStairs2._send('addToPic:')
	else:
		downStairs._send('addToPic:')
		downUpperHalf._send('addToPic:')
		downFloor._send('addToPic:')
		backPost._send('show:', 'stopUpd:')
	#endif
	stoneDoor._send('show:', 'stopUpd:')
	beam._send('show:')
	chink._send('show:', 'stopUpd:')
	global0._send('show:')
	localproc_0()
#end:procedure

@SCI.instance
class rm800(CastleRoom):
	#property vars (may be empty)
	noun = 3
	picture = 800
	style = 10
	horizon = 17
	west = 810
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match global12
			case 810:
				local0 = 3
			#end:case
			else:
				local0 = 1
			#end:else
		#end:match
		localproc_0()
		walls._send('init:')
		super._send('init:', &rest)
		stoneDoor._send('init:')
		match global12
			case 810:
				upHallleft._send('addToPic:')
				upHalleft2._send('addToPic:')
				upStairs._send('addToPic:')
				upStairs2._send('addToPic:')
				climbStairs._send('register:', 3)
				global0._send('posn:', 30, 165)
				self._send('setScript:', firstTimeOnSecondLevel)
			#end:case
			else:
				downStairs._send('addToPic:')
				downUpperHalf._send('addToPic:')
				downFloor._send('addToPic:')
				backPost._send('init:', 'stopUpd:')
				local131 = 2
				secretDoorMove._send('register:', 1)
				stoneDoor._send('posn:', 110, 189)
				self._send('setScript:', secretDoorMove)
				global0._send('reset:', 3, 'posn:', 183, 184)
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 32)):
					kernel.ScriptID(80, 0)._send('setFlag:', 711, 4)
					if (not script):
						self._send('setScript:', firstEntry)
					else:
						script._send('next:', firstEntry)
					#endif
				#endif
			#end:else
		#end:match
		chink._send('init:', 'show:', 'stopUpd:')
		beam._send('init:', 'addToPic:')
		global0._send('init:', 'reset:')
		if (global12 == 810):
			global0._send('loop:', 9, 'cel:', 0)
		#endif
		global0._send('setScale:', 0, 'scaleX:', 128, 'scaleY:', 128, 'ignoreHorizon:')
		if (not script):
			global1._send('handsOn:')
		#endif
		if (global102._send('number:') != 810):
			global102._send('fadeTo:', 810, -1)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		local135 = global0._send('onControl:', 1)
		(cond
			case script: 0#end:case
			case ((local0 == 1) and (local135 & 0x4000)):
				self._send('setScript:', getOnStairs, 0, 1)
				localproc_0(2)
			#end:case
			case ((local0 == 3) and (global0._send('y:') <= 149) and (local135 & 0x1000)):
				self._send('setScript:', changeLandings)
			#end:case
		)
		super._send('doit:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			match param1
				case 1:
					global91._send('say:', noun, param1, (14 + (local0 == 3)))
					1
				#end:case
				else:
					super._send('doVerb:', param1, &rest)
				#end:else
			#end:match
		)
	#end:method

#end:class or instance

@SCI.instance
class firstEntry(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				cycles = 2
			#end:case
			case 1:
				global91._send('say:', 1, 0, 1, 0, self)
			#end:case
			case 2:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class firstTimeOnSecondLevel(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				cycles = 10
			#end:case
			case 1:
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 711, 8)):
					kernel.ScriptID(80, 0)._send('setFlag:', 711, 8)
					roomConv._send('add:', -1, 1, 0, 3)
				#endif
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 710, 256)):
					roomConv._send('add:', -1, 1, 0, 6)
				#endif
				if roomConv._send('size:'):
					roomConv._send('init:', self)
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class changeLandings(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				match local0
					case 2:
						backPost._send('startUpd:')
						global0._send('setMotion:', MoveTo, 207, 9, self)
					#end:case
					case 3:
						global0._send(
							'setPri:', 1,
							'setLoop:', 1,
							'setMotion:', MoveTo, 157, 164, self
						)
					#end:case
				#end:match
			#end:case
			case 1:
				if (local0 == 3):
					localproc_0(2)
				else:
					backPost._send('dispose:')
					chink._send('startUpd:')
					localproc_0(3)
				#endif
				global10._send('eachElementDo:', #dispose, 'release:')
				global2._send('drawPic:', 800, 10)
				match local0
					case 3:
						upHallleft._send('addToPic:')
						upHalleft2._send('addToPic:')
						upStairs._send('addToPic:')
						upStairs2._send('addToPic:')
						global0._send('setPri:', 1, 'posn:', 157, 164)
					#end:case
					else:
						downStairs._send('addToPic:')
						downUpperHalf._send('addToPic:')
						downFloor._send('addToPic:')
						backPost._send('init:', 'stopUpd:')
						global0._send('posn:', 207, 9)
					#end:else
				#end:match
				stoneDoor._send('init:', 'stopUpd:')
				beam._send('addToPic:')
				chink._send('show:', 'stopUpd:')
				cycles = 3
			#end:case
			case 2:
				match local0
					case 3:
						next = firstTimeOnSecondLevel
						global0._send('setMotion:', MoveTo, 191, 145, self)
					#end:case
					else:
						global0._send('setLoop:', -1)
						next = climbStairs._send('register:', 3, 'yourself:')
						global0._send('setMotion:', MoveTo, 168, 34, self)
					#end:else
				#end:match
			#end:case
			case 3:
				if (local0 != 3):
					if (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 32)):
						global91._send('say:', 1, 0, 1, 0, self)
					else:
						cycles = 1
					#endif
				else:
					cycles = 1
				#endif
			#end:case
			case 4:
				if (local0 != 3):
					global1._send('handsOn:')
				#endif
				global0._send('reset:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getOnStairs(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				if register:
					global0._send('setMotion:', MoveTo, 167, 136, self)
				else:
					global0._send('setMotion:', MoveTo, 198, 155, self)
				#endif
			#end:case
			case 1:
				global1._send('handsOn:')
				if register:
					client._send('setScript:', climbStairs)
				else:
					backPost._send('setPri:', -1, 'stopUpd:')
					self._send('dispose:')
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class climbStairs(Script):
	#property vars (may be empty)
	register = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global74._send('addToFront:', self)
		global73._send('addToFront:', self)
		super._send('init:', &rest)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global74._send('delete:', self)
		global73._send('delete:', self)
		super._send('dispose:')
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return 0
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case ((local0 == 2) and (local135 & 0x1000)):
				client._send('setScript:', getOnStairs, 0, 0)
				localproc_0(1)
			#end:case
			case (global0._send('edgeHit:') == 1):
				client._send('setScript:', changeLandings)
			#end:case
		)
		super._send('doit:')
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((param1._send('type:') != 16384) and (not param1._send('modifiers:'))):
			if (param1._send('type:') & 0x0001):
				local134 = 1
			#endif
			if (param1._send('type:') & 0x0040):
				param1._send('claimed:', 1)
				if local134:
					local134 = 0
					register = (2 + (((global0._send('y:') <= 77) * 2) - 1))
				#endif
				(cond
					case proc999_5(param1._send('message:'), 1, 5):
						match param1._send('message:')
							case 1:
								if (register < 3):
									register.post('++')
								#endif
							#end:case
							case 5:
								if (register > 1):
									register.post('--')
								#endif
							#end:case
						#end:match
						global0._send(
							'setMotion:', PolyPath, local117[(register * 2)], [local117
									((register * 2) + 1)
								]
						)
					#end:case
					case (not proc999_5(param1._send('message:'), 8, 2, 6, 4)):
						param1._send('claimed:', 0)
					#end:case
				)
			#endif
		#endif
		param1._send('claimed:')
	#end:method

#end:class or instance

@SCI.instance
class secretDoorMove(Script):
	#property vars (may be empty)
	register = -1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		register = (((register == -1) * 2) - 1)
		if (register == -1):
			global2._send('south:', 0)
			global2._send('obstacles:')._send(
				'delete:', mainPoly,
				'add:', mainPoly._send('type:', 3, 'points:', @local49, 'size:', 4, 'yourself:')
			)
		else:
			global1._send('handsOff:')
		#endif
		super._send('init:', &rest)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (register == 1):
			global2._send('south:', 720)
			next = exitRoom
		#endif
		if (not next):
			global1._send('handsOn:')
		#endif
		super._send('dispose:')
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				cycles = 1
			#end:case
			case 1:
				global105._send('number:', 909, 'loop:', 1, 'play:')
				ticks = 1
			#end:case
			case 2:
				if (<= 0 (local131 += register) 2):
					state.post('--')
					local132 = local125[(local131 * 2)]
					local133 = local125[((local131 * 2) + 1)]
					stoneDoor._send(
						'moveSpeed:', 4,
						'setMotion:', MoveTo, local132, local133, self
					)
				else:
					cycles = 1
				#endif
			#end:case
			case 3:
				global105._send('stop:')
				stoneDoor._send('stopUpd:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class exitRoom(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global0._send('setMotion:', MoveTo, global0._send('x:'), 200, self)
			#end:case
			case 1:
				global2._send('newRoom:', 720)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class stoneDoor(Actor):
	#property vars (may be empty)
	x = 188
	y = 185
	noun = 8
	view = 801
	loop = 2
	cel = 4
	priority = 14
	signal = 18448
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('approachX:', 188, 'approachY:', 183, 'approachVerbs:', 5, 'stopUpd:')
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(and
				(local131 != 3)
				(local0 != 3)
				super._send('onMe:', param1)
				(param1._send('x:') > 115)
			)
		)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				if (not script):
					self._send('setScript:', secretDoorMove)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class chink(View):
	#property vars (may be empty)
	x = 289
	y = 128
	view = 801
	loop = 3
	
	@classmethod
	def show():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (local0 != 3):
			self._send('posn:', 289, 128)
		else:
			self._send('posn:', 258, 122)
		#endif
		super._send('show:', &rest)
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('approachVerbs:', 5, 1)
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(and
				super._send('onMe:', param1)
				(or
					(and
						(local0 == 3)
						approachX = 228
						approachY = 157
						noun = 4
					)
					(approachX = 258 and approachY = 166 and noun = 6)
				)
			)
		)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case ((global66._send('doit:', param1) == -32768) and (not param1 = 0)):
				global91._send('say:', 7, param1)
			#end:case
			case proc999_5(param1, 5, 1):
				match noun
					case 4:
						global2._send('setScript:', kernel.ScriptID(801))
					#end:case
					else:
						global2._send('setScript:', kernel.ScriptID(802))
					#end:else
				#end:match
			#end:case
			else:
				super._send('doVerb:', param1)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class beam(View):
	#property vars (may be empty)
	onMeCheck = 0
	view = 801
	loop = 4
	signal = 16400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		cel = (kernel.NumCels(self) - 1)
		super._send('init:', &rest)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((not (signal & 0x0008)) and (global0._send('view:') != 802)):
			if 
				(and
					(global0._send('x:') >= local115)
					(>= (y + 2) global0._send('y:') (y - 2))
				)
				cel = (((x - global0._send('x:')) / 7) - 1)
				priority = (global0._send('priority:') - 1)
			else:
				priority = kernel.CoordPri(y)
				cel = local116
			#endif
		#endif
		super._send('doit:')
	#end:method

	@classmethod
	def addToPic():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (local0 != 3):
			self._send('posn:', 289, 128, 0, 'loop:', 4)
		else:
			self._send('posn:', 258, 122, 0, 'loop:', 6)
		#endif
		cel = (kernel.NumCels(self) - 1)
		local116 = cel
		priority = kernel.CoordPri(y)
		kernel.SetNowSeen(self)
		local115 = nsLeft
		temp0 = y
		y = (nsBottom - 2)
		z = (y - temp0)
	#end:method

#end:class or instance

class Stair(View):
	#property vars (may be empty)
	noun = 10
	view = 801
	loop = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		global93._send('add:', self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global93._send('delete:', self)
		super._send('dispose:')
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				(local0 != 2)
				(param1._send('type:') != 16384)
				(not param1._send('modifiers:'))
				(param1._send('type:') & 0x1000)
				self._send('onMe:', param1)
			)
			param1._send('claimed:', 1)
			global0._send('setMotion:', PolyPath, 188, 151)
		#endif
		param1._send('claimed:')
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(and
				super._send('onMe:', param1)
				(or
					((global69._send('curIcon:') == global69._send('at:', 2)) and noun = 10)
					noun = 11
				)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class downStairs(Stair):
	#property vars (may be empty)
	x = 106
	y = 158
	signal = 20480
	
#end:class or instance

@SCI.instance
class downUpperHalf(Stair):
	#property vars (may be empty)
	x = 106
	y = 78
	cel = 1
	signal = 20480
	
#end:class or instance

@SCI.instance
class downFloor(Stair):
	#property vars (may be empty)
	x = 106
	y = 77
	cel = 2
	signal = 20496
	
#end:class or instance

@SCI.instance
class backPost(Stair):
	#property vars (may be empty)
	x = 181
	y = 158
	z = 15
	cel = 3
	signal = 20480
	
#end:class or instance

@SCI.instance
class upHallleft(View):
	#property vars (may be empty)
	x = 25
	y = 114
	noun = 9
	view = 801
	loop = 2
	priority = 15
	signal = 20496
	
#end:class or instance

@SCI.instance
class upHalleft2(View):
	#property vars (may be empty)
	x = 25
	y = 114
	noun = 9
	view = 801
	loop = 2
	cel = 1
	signal = 16400
	
#end:class or instance

@SCI.instance
class upStairs(View):
	#property vars (may be empty)
	x = 154
	y = 148
	noun = 11
	view = 801
	loop = 2
	cel = 3
	signal = 20496
	
#end:class or instance

@SCI.instance
class upStairs2(View):
	#property vars (may be empty)
	x = 154
	y = 151
	noun = 11
	view = 801
	loop = 2
	cel = 2
	signal = 20480
	
#end:class or instance

@SCI.instance
class walls(Feature):
	#property vars (may be empty)
	noun = 7
	onMeCheck = 2
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				roomConv._send('add:', -1, noun, param1, 26)
				if (User._send('curEvent:')._send('x:') >= 214):
					roomConv._send('add:', -1, noun, param1, 27)
				#endif
				roomConv._send('init:')
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
class mainPoly(Polygon):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class Poly1(Polygon):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class Poly2(Polygon):
	#property vars (may be empty)
#end:class or instance

