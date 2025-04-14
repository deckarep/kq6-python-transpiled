#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 810
import sci_sh
import kernel
import Main
import rgCastle
import Scaler
import Polygon
import Feature
import MoveFwd
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm810 = 0,
	proc810_1 = 1,
	beam = 3,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = [0, 189, 0, -10, 319, -10, 319, 189, 254, 189, 222, 132, 126, 132, 126, 137, 179, 137, 142, 189]
local21 = [0, 189, 0, -10, 319, -10, 319, 189, 256, 189, 207, 106, 199, 106, 142, 189]
local37 = [0, 189, 0, -10, 319, -10, 319, 189, 254, 189, 222, 132, 183, 132, 142, 189]
local53 = None
local54 = None
local55 = None


@SCI.procedure
def localproc_0():
	if global2._send('obstacles:'):
		global2._send('obstacles:')._send('dispose:')
	#endif
	match local0
		case 1:
			global2._send('addObstacle:', mainPoly._send('points:', @local37, 'size:', 8, 'yourself:'))
		#end:case
		case 2:
			global2._send('addObstacle:', mainPoly._send('points:', @local21, 'size:', 8, 'yourself:'))
		#end:case
		else:
			global2._send('addObstacle:', mainPoly._send('points:', @local1, 'size:', 10, 'yourself:'))
		#end:else
	#end:match
#end:procedure

@SCI.procedure
def proc810_1():
	global2._send('drawPic:', global2._send('picture:'))
	endHallway._send('init:', 'addToPic:')
	global0._send('init:', 'show:')
	beam._send('cel:', 0, 'show:')
	chink._send('show:')
	localproc_0()
#end:procedure

@SCI.instance
class rm810(CastleRoom):
	#property vars (may be empty)
	noun = 3
	picture = 810
	style = 10
	horizon = 129
	walkOffEdge = 1
	
	@classmethod
	def init():
		match global12
			case 781:
				local0 = 1
				local53 = 1
				global102._send('fadeTo:', 810, -1)
			#end:case
			else:
				global0._send('posn:', 200, 186)
				local0 = 3
			#end:else
		#end:match
		localproc_0()
		super._send('init:', &rest)
		walls._send('init:')
		global0._send('init:', 'reset:')
		if (global12 == 800):
			global0._send('loop:', 9, 'cel:', 3)
		#endif
		global0._send('setScale:', Scaler, 100, 70, 190, 129)
		global0._send('scaler:')._send('doit:')
		secretDoor._send('init:', 'hide:')
		match global12
			case 781:
				secretDoor._send('cel:', 3, 'show:', 'stopUpd:')
				global0._send(
					'normal:', 0,
					'view:', 781,
					'setScale:', 0,
					'scaleX:', 128,
					'scaleY:', 128,
					'loop:', 3,
					'cel:', 9,
					'posn:', 193, 134
				)
				self._send('setScript:', enterBedroom)
			#end:case
			else:
				global0._send('posn:', 200, 186)
			#end:else
		#end:match
		chink._send('init:', 'hide:')
		beam._send('init:', 'hide:')
		endHallway._send('addToPic:')
		if (not script):
			global1._send('handsOn:')
		#endif
	#end:method

	@classmethod
	def doit():
		temp0 = global0._send('onControl:', 1)
		(cond
			case script: 0#end:case
			case (temp0 & 0x4000):
				if (local0 != 1):
					self._send('setScript:', changeHallways, 0, 270)
				#endif
			#end:case
			case temp1 = global0._send('edgeHit:'):
				match temp1
					case 3:
						if (local0 == 3):
							global2._send('newRoom:', 800)
						else:
							self._send('setScript:', changeHallways, 0, 180)
						#endif
					#end:case
					case 1:
						self._send('setScript:', changeHallways, 0, 0)
					#end:case
				#end:match
			#end:case
		)
		super._send('doit:', &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:', &rest)
		kernel.DisposeScript(951)
		kernel.DisposeScript(969)
	#end:method

#end:class or instance

@SCI.instance
class changeHallways(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setHeading:', register, self)
			#end:case
			case 1:
				secretDoor._send('startUpd:')
				if register:
					global0._send('setMotion:', MoveFwd, 15, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				beam._send('setScript:', 0)
				if (global0._send('heading:') == 180):
					global0._send('posn:', 200, 133)
					local0.post('++')
				else:
					global0._send('posn:', 200, 188, 'setHeading:', 0)
					local0.post('--')
				#endif
				state.post('++')
				if register = (local0 == 3):
					state.post('--')
					global0._send('posn:', 156, 135, 'hide:', 'normal:', 0)
				#endif
				localproc_0()
				chink._send('hide:')
				beam._send('hide:')
				secretDoor._send('startUpd:', 'hide:')
				global2._send('drawPic:', 810, 10)
				endHallway._send('addToPic:')
				match local0
					case 2:
						chink._send('show:')
						beam._send('show:')
					#end:case
					case 1:
						secretDoor._send('show:', 'stopUpd:')
					#end:case
				#end:match
				global0._send('scaler:')._send('doit:')
				cycles = 10
			#end:case
			case 3:
				global0._send('show:', 'normal:', 1, 'setMotion:', MoveTo, 184, 135, self)
			#end:case
			case 4:
				ticks = 30
			#end:case
			case 5:
				if ((local0 == 2) and (not kernel.ScriptID(80, 0)._send('tstFlag:', 711, 16))):
					global91._send('say:', 1, 0, 4, 0, self)
				else:
					cycles = 2
				#endif
			#end:case
			case 6:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class enterBedroom(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				if local53:
					secretDoor._send('cel:', 3)
					cycles = 1
				else:
					secretDoor._send('setCycle:', End, self)
				#endif
			#end:case
			case 1:
				global0._send(
					'normal:', 0,
					'view:', 781,
					'setScale:', 0,
					'scaleX:', 128,
					'scaleY:', 128,
					'loop:', 3,
					'cycleSpeed:', 8,
					'posn:', 193, 134
				)
				if local53:
					state.post('++')
					global0._send('cel:', 9, 'setCycle:', Beg, self)
				else:
					global0._send('cel:', 0, 'setCycle:', End, self)
				#endif
			#end:case
			case 2:
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 711, 1024)):
					kernel.ScriptID(80, 0)._send('setFlag:', 711, 1024)
					global91._send('say:', 6, 5, 13, 0, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 3:
				if local53:
					global0._send(
						'posn:', secretDoor._send('approachX:'), secretDoor._send('approachY:'),
						'oldScaleSignal:', 0,
						'setScale:', Scaler, 100, 70, 190, 129,
						'reset:', 1
					)
					global0._send('scaler:')._send('doit:')
					local53 = 0
					secretDoor._send('setCycle:', Beg, self)
				else:
					global2._send('newRoom:', 781)
				#endif
			#end:case
			case 4:
				secretDoor._send('stopUpd:')
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walls(Feature):
	#property vars (may be empty)
	noun = 5
	
	@classmethod
	def onMe(param1 = None, *rest):
		local54 = (proc999_4(142, 64, 157, 156, param1) and (local0 == 2))
		return (not (0x0002 & kernel.OnControl(4, param1._send('x:'), param1._send('y:'))))
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				if local54:
					temp0 = 11
				else:
					temp0 = 12
				#endif
				global91._send('say:', noun, param1, temp0)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class endHallway(View):
	#property vars (may be empty)
	onMeCheck = 0
	view = 810
	
	@classmethod
	def init():
		cel = (0 if (local0 == 3) else local0)
		match cel
			case 1:
				x = 203
				y = 101
			#end:case
			case 2:
				x = 200
				y = 106
			#end:case
		#end:match
		priority = 0
		(signal |= 0x6010)
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class chink(View):
	#property vars (may be empty)
	x = 148
	y = 167
	z = 42
	noun = 4
	approachX = 164
	approachY = 169
	view = 810
	loop = 1
	priority = 10
	signal = 16400
	
	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('approachVerbs:', 1, 5)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 1:
				global2._send('setScript:', kernel.ScriptID(811))
			#end:case
			case 5:
				global2._send('setScript:', kernel.ScriptID(811))
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class beam(Prop):
	#property vars (may be empty)
	x = 148
	y = 167
	z = 42
	onMeCheck = 0
	view = 810
	loop = 2
	cel = 8
	signal = 16400
	
	@classmethod
	def doit():
		if (not (signal & 0x0008)):
			if ((global0._send('x:') <= 216) and (>= 169 global0._send('y:') 165)):
				cel = (((global0._send('x:') - x) / 7) - 1)
				priority = (global0._send('priority:') - 1)
			else:
				priority = kernel.CoordPri(y)
				cel = 8
			#endif
		#endif
		super._send('doit:')
	#end:method

	@classmethod
	def setScript(param1 = None, *rest):
		super._send('setScript:', param1, &rest)
	#end:method

#end:class or instance

@SCI.instance
class secretDoor(Prop):
	#property vars (may be empty)
	x = 175
	y = 127
	noun = 6
	approachX = 192
	approachY = 134
	view = 781
	loop = 2
	signal = 24592
	
	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('approachVerbs:', 5)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				global2._send('setScript:', enterBedroom)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class mainPoly(Polygon):
	#property vars (may be empty)
	type = 2
	
#end:class or instance

