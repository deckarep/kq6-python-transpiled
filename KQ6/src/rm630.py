#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 630
import sci_sh
import kernel
import Main
import KQ6Room
import Conversation
import Scaler
import MCyc
import PolyPath
import Polygon
import Feature
import LoadMany
import DPath
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm630 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = [1, 0, 183, 156, 1, 1, 184, 152, 1, 2, 185, 141, 1, 3, 184, 128, 1, 4, 183, 113, 1, 5, 182, 102, 1, 6, 182, 88, 1, 7, 183, 83, 1, 8, 184, 78, 1, 9, 184, 77, 1, 10, 183, 78, 1, 11, 183, 78, 1, 12, 183, 79, 1, 13, 183, 76, 1, 14, 183, 74, 1, 15, 183, 71, 2, 0, 181, 66, 2, 1, 180, 60, -32768]
local73 = None
local74 = None
local75 = None
local76 = None
local77 = None
local78 = None
local79 = [136, 132, 126, 133, 110, 144, 131, 150, 139, 168, 152, 189, 319, 189, 217, 140, 171, 159, 165, 156, 183, 134, 172, 132, 181, 126, 227, 124, 219, 112, 199, 109, 193, 103, 155, 101, 154, 7, 114, 7, 114, 105, 187, 113, 133, 122]
local125 = [105, 149, 145, 189, 303, 189, 164, 134, 173, 125, 196, 121, 216, 123, 223, 117, 204, 113, 191, 107, 147, 101, 187, 89, 187, 2, 182, 2, 182, 88, 125, 103, 163, 108, 196, 113, 157, 119, 134, 131]
local165 = [0, 189, 0, -10, 319, -10, 319, 189, 196, 141, 167, 149, 174, 134, 163, 133, 167, 128, 215, 116, 188, 107, 145, 101, 145, 10, 131, 10, 131, 103, 181, 110, 199, 115, 144, 126, 137, 133, 122, 148, 157, 162, 162, 189]
local209 = [0, 0, 7, 38, 0, 1, 0, 38, 0, 2, 2, 40, 0, 3, 0, 39, 1, 0, 0, 41, 1, 1, 6, 38, 1, 2, 17, 38, 2, 0, 27, 38, 2, 1, 38, 40, 2, 2, 47, 39, 3, 0, 54, 41, 3, 1, 66, 38, 3, 2, 77, 38, 4, 0, 87, 38, 4, 1, 98, 40, 4, 2, 107, 39, 5, 0, 114, 41, 5, 1, 126, 38, 5, 2, 137, 38, 6, 0, 147, 38, 6, 1, 158, 40, 6, 2, 167, 39, 7, 0, 174, 41, 7, 1, 186, 38, 7, 2, 197, 38, 8, 0, 207, 38, 8, 1, 218, 40, 8, 2, 227, 39, -32768]
local322 = [1, 0, 114, 79, 1, 1, 116, 79, 1, 2, 120, 69, 1, 3, 130, 62, 1, 4, 140, 53, 1, 5, 152, 48, 1, 6, 182, 52, 1, 7, 175, 73, 1, 8, 165, 82, 1, 9, 156, 97, 1, 10, 134, 111, 1, 11, 121, 110, 1, 12, 111, 98, -32768]
local375 = [0, 0, 109, 82, 0, 1, 108, 84, 0, 2, 108, 82, 0, 3, 108, 82, 1, 0, 114, 79, 1, 1, 116, 79, 1, 2, 120, 69, 1, 3, 130, 62, 1, 4, 140, 53, 1, 5, 153, 48, 1, 6, 182, 52, 1, 7, 175, 73, 1, 8, 165, 82, 1, 9, 156, 97, 1, 10, 134, 111, 1, 11, 121, 110, 1, 12, 111, 98, -32768, 2, 0, 138, 69, 2, 1, 159, 87, 2, 2, 163, 106, -32768]
local457 = [2, 3, 175, 104, 3, 0, 187, 76, 3, 1, 191, 71, 3, 2, 193, 64, 3, 3, 207, 54, 3, 4, 220, 50, 3, 5, 231, 22, 3, 6, 253, 14, 3, 7, 284, 44, 3, 8, 262, 60, 3, 9, 248, 55, 3, 10, 241, 44, 4, 0, 243, 26, -32768]


@SCI.procedure
def localproc_0(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	if global2._send('obstacles:'):
		global2._send('obstacles:')._send('dispose:')
	#endif
	global2._send(
		'addObstacle:', match (local73 if (not argc) else param1)
				case 0:
					roomPoly._send('type:', 2, 'points:', @local165, 'size:', 22, 'yourself:')
				#end:case
				case 1:
					roomPoly._send('type:', 3, 'points:', @local79, 'size:', 23, 'yourself:')
				#end:case
				case 2:
					roomPoly._send('type:', 3, 'points:', @local125, 'size:', 20, 'yourself:')
				#end:case
			#end:match
	)
#end:procedure

@SCI.instance
class rm630(KQ6Room):
	#property vars (may be empty)
	noun = 5
	picture = 630
	north = 640
	south = 600
	
	@classmethod
	def init():
		global1._send('handsOff:')
		super._send('init:', &rest)
		if (global12 == 640):
			local73 = 2
			global0._send(
				'init:',
				'reset:', 5,
				'setScale:', Scaler, 40, 20, 140, 80,
				'posn:', 178, 92,
				'setPri:', 8
			)
			global2._send('setScript:', fromEntranceScr)
		else:
			local73 = 0
			global0._send('init:', 'reset:', 3, 'posn:', 225, 188, 'setScale:', FixedScaler, 100)
			global1._send('handsOn:')
		#endif
		localproc_0()
		bats._send(
			'init:',
			'illegalBits:', 0,
			'ignoreActors:', 1,
			'ignoreHorizon:', 1,
			'setCycle:', MCyc, @local209, bats
		)
		zombie._send(
			'init:',
			'illegalBits:', 0,
			'ignoreActors:', 1,
			'ignoreHorizon:', 1,
			'setCycle:', Walk,
			'hide:',
			'setScript:', zombieScript, 0, 600
		)
		global32._send('add:', moon, sky, uWorldEntrance, myPath, 'eachElementDo:', #init)
		if (not global0._send('has:', 17)):
			motherGhost._send(
				'init:',
				'ignoreActors:', 1,
				'illegalBits:', 0,
				'ignoreHorizon:', 1,
				'setScript:', motherGhostScript
			)
			global102._send('number:', 630, 'loop:', -1, 'play:')
		#endif
	#end:method

	@classmethod
	def doit():
		super._send('doit:', &rest)
		if (not script):
			match temp0 = global0._send('onControl:', 1)
				case 16384:
					self._send('setScript:', toEntranceScr)
				#end:case
				case 8192:
					if (local73 == 0):
						self._send('setScript:', downToMidScr)
					#endif
				#end:case
				case 4096:
					if (local73 == 1):
						self._send('setScript:', downToBottomScr)
					#endif
				#end:case
				case 2048:
					if (local73 == 1):
						self._send('setScript:', upToTopScr)
					#endif
				#end:case
				case 1024:
					if (local73 == 2):
						self._send('setScript:', upToMidScr)
					#endif
				#end:case
			#end:match
		#endif
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		if (global102._send('number:') == 630):
			global102._send('fade:')
		#endif
		super._send('newRoom:', param1)
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		proc958_0(0, 942, 964)
	#end:method

#end:class or instance

@SCI.instance
class roomPoly(Polygon):
	#property vars (may be empty)
#end:class or instance

class FixedScaler(Code):
	#property vars (may be empty)
	frontSize = 0
	backSize = 0
	frontY = 0
	backY = 0
	
	@classmethod
	def init(param1 = None, param2 = None, *rest):
		backSize = (frontSize = param2 - 1)
		param2 = ((param2 * 128) / 100)
		param1._send('scaleX:', param2, 'scaleY:', param2)
	#end:method

#end:class or instance

@SCI.instance
class downToMidScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if (global0._send('mover:') and global0._send('mover:')._send('isKindOf:', PolyPath)):
					local74 = global0._send('mover:')._send('finalX:')
					local75 = global0._send('mover:')._send('finalY:')
					local76 = global0._send('mover:')._send('caller:')
				#endif
				global1._send('handsOff:')
				global0._send('setMotion:', 0)
				cycles = 1
			#end:case
			case 1:
				global0._send(
					'setScale:', Scaler, ((global0._send('scaleX:') * 100) / 128), (-
							((global0._send('scaleX:') * 100) / 128)
							1
						), global0._send('x:'), (global0._send('x:') - 1),
					'setPri:', 9,
					'setLoop:', 7,
					'setMotion:', MoveTo, (global0._send('x:') - 20), (+
							global0._send('y:')
							50
						), self
				)
			#end:case
			case 2:
				global0._send('setLoop:', -1, 'setScale:', FixedScaler, 65)
				localproc_0(1)
				seconds = 2
			#end:case
			case 3:
				global0._send('posn:', 136, 175, 'setMotion:', MoveTo, 139, 151, self)
			#end:case
			case 4:
				local73 = 1
				if (not local76):
					global1._send('handsOn:')
				#endif
				if local74:
					if 
						(>
							kernel.GetDistance(global0._send('x:'), global0._send('y:'), local74, local75)
							15
						)
						global0._send('setMotion:', PolyPath, local74, local75, local76)
					#endif
					local74 = 0
					local76 = 0
				#endif
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class downToBottomScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if (global0._send('mover:') and global0._send('mover:')._send('isKindOf:', PolyPath)):
					local74 = global0._send('mover:')._send('finalX:')
					local75 = global0._send('mover:')._send('finalY:')
					local76 = global0._send('mover:')._send('caller:')
				#endif
				global1._send('handsOff:')
				global0._send('setMotion:', 0)
				cycles = 1
			#end:case
			case 1:
				global0._send(
					'setScale:', Scaler, ((global0._send('scaleX:') * 100) / 128), (-
							((global0._send('scaleX:') * 100) / 128)
							1
						), global0._send('x:'), (global0._send('x:') - 1),
					'setPri:', 8,
					'setLoop:', 3,
					'setMotion:', MoveTo, 160, 167, self
				)
			#end:case
			case 2:
				global0._send('setLoop:', -1, 'setScale:', Scaler, 40, 20, 140, 80)
				localproc_0(2)
				seconds = 2
			#end:case
			case 3:
				global0._send('posn:', 161, 151, 'setMotion:', MoveTo, 160, 134, self)
			#end:case
			case 4:
				local73 = 2
				if (not local76):
					global1._send('handsOn:')
				#endif
				if local74:
					if 
						(>
							kernel.GetDistance(global0._send('x:'), global0._send('y:'), local74, local75)
							10
						)
						global0._send('setMotion:', PolyPath, local74, local75, local76)
					#endif
					local74 = 0
					local76 = 0
				#endif
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class upToTopScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if (global0._send('mover:') and global0._send('mover:')._send('isKindOf:', PolyPath)):
					local74 = global0._send('mover:')._send('finalX:')
					local75 = global0._send('mover:')._send('finalY:')
					local76 = global0._send('mover:')._send('caller:')
				#endif
				global1._send('handsOff:')
				global0._send('setMotion:', 0)
				cycles = 1
			#end:case
			case 1:
				global0._send(
					'setMotion:', MoveTo, (global0._send('x:') - 10), (+
							global0._send('y:')
							35
						), self
				)
			#end:case
			case 2:
				localproc_0(0)
				seconds = 2
			#end:case
			case 3:
				global0._send(
					'setScale:', FixedScaler, 100,
					'setLoop:', 2,
					'posn:', 133, 191,
					'setMotion:', MoveTo, 167, 151, self
				)
			#end:case
			case 4:
				global0._send('setPri:', -1, 'setLoop:', -1, 'setMotion:', MoveTo, 175, 156, self)
			#end:case
			case 5:
				local73 = 0
				if (not local76):
					global1._send('handsOn:')
				#endif
				if local74:
					if 
						(>
							kernel.GetDistance(global0._send('x:'), global0._send('y:'), local74, local75)
							20
						)
						global0._send('setMotion:', PolyPath, local74, local75, local76)
					#endif
					local74 = 0
					local76 = 0
				#endif
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class upToMidScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if (global0._send('mover:') and global0._send('mover:')._send('isKindOf:', PolyPath)):
					local74 = global0._send('mover:')._send('finalX:')
					local75 = global0._send('mover:')._send('finalY:')
					local76 = global0._send('mover:')._send('caller:')
				#endif
				global1._send('handsOff:')
				global0._send('setMotion:', 0)
				cycles = 1
			#end:case
			case 1:
				global0._send(
					'setMotion:', MoveTo, (global0._send('x:') + 3), (+
							global0._send('y:')
							24
						), self
				)
			#end:case
			case 2:
				seconds = 2
			#end:case
			case 3:
				global0._send(
					'setScale:', FixedScaler, 65,
					'setLoop:', 2,
					'posn:', 172, 165,
					'setMotion:', MoveTo, 162, 136, self
				)
			#end:case
			case 4:
				global0._send(
					'setLoop:', -1,
					'setPri:', (global0._send('priority:') + 1),
					'setMotion:', MoveTo, 154, 141, self
				)
			#end:case
			case 5:
				local73 = 1
				localproc_0()
				if (not local76):
					global1._send('handsOn:')
				#endif
				if local74:
					if 
						(>
							kernel.GetDistance(global0._send('x:'), global0._send('y:'), local74, local75)
							15
						)
						global0._send('setMotion:', PolyPath, local74, local75, local76)
					#endif
					local74 = 0
					local76 = 0
				#endif
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class fromEntranceScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('setMotion:', DPath, 176, 91, 140, 103, 176, 108, self)
			#end:case
			case 1:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class toEntranceScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', DPath, 140, 103, 176, 91, self)
			#end:case
			case 1:
				global0._send('setMotion:', 0)
				cycles = 2
			#end:case
			case 2:
				global2._send('newRoom:', global2._send('north:'))
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class zombie(Actor):
	#property vars (may be empty)
	x = 343
	y = 258
	noun = 11
	view = 600
	
	@classmethod
	def doVerb(param1 = None, *rest):
		if (param1 == 5):
			if local73:
				global91._send('say:', noun, param1, 7, 1)
			else:
				global1._send('handsOff:')
				global2._send('setScript:', egoDeadScript, 0, self)
			#endif
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

	@classmethod
	def doit():
		if 
			(and
				(not global2._send('script:'))
				(motherGhost._send('script:') != getHankyScript)
				(global0._send('distanceTo:', self) <= 10)
				(not local73)
			)
			global1._send('handsOff:')
			local78 = 1
			global2._send('setScript:', egoDeadScript, 0, self)
		#endif
		super._send('doit:')
	#end:method

#end:class or instance

@SCI.instance
class ghoul1(Actor):
	#property vars (may be empty)
	x = 183
	y = 156
	noun = 8
	view = 631
	loop = 1
	
#end:class or instance

@SCI.instance
class zombieScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				seconds = kernel.Random(20, 30)
			#end:case
			case 1:
				client._send(
					'view:', register,
					'show:',
					'setMotion:', DPath, 343, 258, 299, 187, 234, 183, 165, 186, 165, 242, self
				)
				register.post('++')
				if (register == 602):
					register = 603
				#endif
				if (register > 603):
					register = 600
				#endif
			#end:case
			case 2:
				client._send('hide:')
				self._send('init:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoDeadScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				zombie._send('setMotion:', 0)
				if local78:
					global91._send('say:', 9, 0, 5, 1, self)
				else:
					global91._send('say:', 11, 5, 0, 1, self)
				#endif
			#end:case
			case 1:
				(cond
					case local78:
						cycles = 1
					#end:case
					case (global0._send('x:') > register._send('x:')):
						global0._send(
							'setMotion:', PolyPath, (register._send('x:') + 20), register._send(
									'y:'
								), self
						)
					#end:case
					else:
						global0._send(
							'setMotion:', PolyPath, (register._send('x:') - 20), register._send(
									'y:'
								), self
						)
					#end:else
				)
				global102._send('stop:')
				global103._send('number:', 601, 'loop:', 1, 'play:')
			#end:case
			case 2:
				if local78:
					global91._send('say:', 9, 0, 5, 2, self)
				else:
					global91._send('say:', 11, 5, 0, 2, self)
				#endif
			#end:case
			case 3:
				global0._send(
					'view:', 606,
					'normal:', 0,
					'setLoop:', 0,
					'cel:', 0,
					'cycleSpeed:', 15,
					'setCycle:', End, self
				)
			#end:case
			case 4:
				proc0_1(38)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class ghoul1Scr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				client._send('show:', 'setCycle:', MCyc, @local0, self)
			#end:case
			case 1:
				client._send('hide:')
				seconds = kernel.Random(20, 30)
			#end:case
			case 2:
				self._send('init:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class myPath(Feature):
	#property vars (may be empty)
	noun = 4
	onMeCheck = 31746
	
#end:class or instance

@SCI.instance
class uWorldEntrance(Feature):
	#property vars (may be empty)
	noun = 10
	onMeCheck = 4
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 2:
				super._send('doVerb:', param1, &rest)
			#end:case
			case 1:
				super._send('doVerb:', param1, &rest)
			#end:case
			else:
				super._send('doVerb:', 5, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class sky(Feature):
	#property vars (may be empty)
	noun = 7
	onMeCheck = 16
	
#end:class or instance

@SCI.instance
class moon(Feature):
	#property vars (may be empty)
	noun = 3
	onMeCheck = 32
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 2:
				super._send('doVerb:', param1, &rest)
			#end:case
			case 1:
				super._send('doVerb:', param1, &rest)
			#end:case
			case 5:
				super._send('doVerb:', param1, &rest)
			#end:case
			else:
				global91._send('say:', noun, 0, 0, 0)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class bats(Actor):
	#property vars (may be empty)
	x = 7
	y = 38
	noun = 8
	view = 630
	
	@classmethod
	def cue():
		ghoul1._send(
			'init:',
			'setPri:', 10,
			'cycleSpeed:', 15,
			'ignoreActors:', 1,
			'ignoreHorizon:', 1,
			'setScript:', ghoul1Scr
		)
		self._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class motherGhost(Actor):
	#property vars (may be empty)
	x = 109
	y = 82
	noun = 2
	view = 633
	cycleSpeed = 10
	
	@classmethod
	def doit():
		super._send('doit:')
		if 
			(and
				(not global2._send('script:'))
				(script._send('state:') == 0)
				script._send('register:')
			)
			global1._send('handsOff:')
			self._send('setScript:', getHankyScript)
		#endif
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 2:
				(cond
					case global0._send('has:', 17):
						global91._send('say:', 2, 2, 1)
					#end:case
					case (script._send('state:') != 0):
						global1._send('handsOff:')
						script._send('register:', 1)
					#end:case
					else:
						global1._send('handsOff:')
						self._send('setScript:', getHankyScript)
					#end:else
				)
			#end:case
			case 1:
				if global0._send('has:', 17):
					global91._send('say:', noun, param1, 1)
				else:
					global91._send('say:', noun, param1, 2)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class motherGhostScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				client._send('loop:', 0, 'posn:', 109, 82, 'cycleSpeed:', 20, 'setCycle:', Fwd)
				seconds = kernel.Random(5, 15)
			#end:case
			case 1:
				global91._send('say:', 9, 0, 4, 1, self)
			#end:case
			case 2:
				client._send('cycleSpeed:', 5, 'setCycle:', MCyc, @local322, self)
			#end:case
			case 3:
				self._send('init:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getHankyScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				local77 = zombie._send('mover:')
				zombie._send('mover:', 0)
				global0._send('setMotion:', PolyPath, 205, 162, self)
			#end:case
			case 1:
				global0._send('setHeading:', 315, self)
			#end:case
			case 2:
				theConv._send(
					'add:', -1, 2, 2, 2, 1,
					'add:', -1, 2, 2, 2, 2,
					'add:', -1, 2, 2, 2, 3,
					'add:', -1, 2, 2, 2, 4,
					'add:', -1, 2, 2, 2, 5,
					'add:', -1, 2, 2, 2, 6,
					'add:', -1, 2, 2, 2, 7,
					'init:', self
				)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				global91._send('say:', 2, 2, 2, 8, self)
			#end:case
			case 5:
				global91._send('say:', 2, 2, 2, 9, self)
			#end:case
			case 6:
				motherGhost._send('cycleSpeed:', 15, 'setCycle:', MCyc, @local375, self)
			#end:case
			case 7:
				motherGhost._send('setLoop:', 2, 'cel:', 0, 'posn:', 138, 69)
				global0._send(
					'normal:', 0,
					'view:', 633,
					'setLoop:', 5,
					'cel:', 0,
					'posn:', (global0._send('x:') - 11), (global0._send('y:') - 1)
				)
				cycles = 10
			#end:case
			case 8:
				motherGhost._send('cel:', 1, 'posn:', 159, 87)
				global0._send('cel:', 1)
				cycles = 10
			#end:case
			case 9:
				motherGhost._send('cel:', 2, 'posn:', 163, 106)
				global0._send('cel:', 2)
				cycles = 10
			#end:case
			case 10:
				motherGhost._send('setCycle:', MCyc, @local457, self)
				global0._send('cel:', 3)
				cycles = 3
			#end:case
			case 11:
				global1._send('givePoints:', 1)
				global0._send(
					'get:', 17,
					'oldScaleSignal:', 0,
					'reset:', 7,
					'setScale:', FixedScaler, 100,
					'posn:', 210, 167
				)
			#end:case
			case 12:
				motherGhost._send('view:', 632, 'setLoop:', 0, 'cel:', 0, 'setCycle:', End, self)
				global102._send('fade:')
			#end:case
			case 13:
				global102._send('number:', 600, 'loop:', -1, 'play:')
				global1._send('handsOn:')
				motherGhost._send('dispose:')
				if local77:
					zombie._send('mover:', local77)
				#endif
				local77 = 0
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class theConv(Conversation):
	#property vars (may be empty)
#end:class or instance

