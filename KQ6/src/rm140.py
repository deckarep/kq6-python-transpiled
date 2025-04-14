#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 140
import sci_sh
import kernel
import Main
import AnimatePrint
import KQ6Room
import Kq6Talker
import CartoonScript
import n913
import Messager
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm140 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = [285, 48, 0, 262, 60, 1, 238, 73, 2, 222, 83, 3, 201, 92, 4, 177, 105, 5, -99, 159, 109, 0, 146, 114, 1, 139, 116, 2, -99, 139, 116, 0, -1, -1, -1]
local38 = [139, 116, 0, 139, 116, 1, 146, 114, 2, -99, 159, 109, 0, 177, 105, 1, 201, 92, 2, 222, 83, 3, 238, 73, 4, 262, 60, 5, -1, -1, -1]
local69 = -1
local70 = None
local71 = None
local72 = None


@SCI.instance
class rm140(KQ6Room):
	#property vars (may be empty)
	picture = 140
	horizon = 0
	
	@classmethod
	def init():
		super._send('init:', &rest)
		local72 = global91
		global91 = localMessager
		global69._send('disable:')
		proc913_1(59)
		singSing._send('init:')
		leftArm._send('init:')
		local0 = global9._send('at:', 47)._send('owner:')
		local1 = global9._send('at:', 39)._send('owner:')
		local2 = global9._send('at:', 38)._send('owner:')
		(cond
			case (local0 == global11):
				self._send('setScript:', poemSegueScr)
			#end:case
			case (local2 == global11):
				self._send('setScript:', roseSegueScr)
			#end:case
			case (local1 == global11):
				self._send('setScript:', ringSegueScr)
			#end:case
		)
		global105._send('fade:')
		global104._send('number:', 140, 'loop:', -1, 'play:')
	#end:method

	@classmethod
	def dispose():
		global91 = local72
		proc913_2(59)
		kernel.DisposeScript(371)
		super._send('dispose:', &rest)
		global69._send('enable:')
	#end:method

#end:class or instance

@SCI.instance
class cassyPrint(AnimatePrint):
	#property vars (may be empty)
	@classmethod
	def init():
		myMouth = cassyMouth
		x = -1
		y = 15
		super._send('init:')
	#end:method

#end:class or instance

@SCI.instance
class singSingEnterScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				match register
					case 0:
						followItem._send('view:', 1412)
					#end:case
					case 2:
						followItem._send('view:', 1411)
					#end:case
					case 1:
						followItem._send('view:', 1414)
					#end:case
				#end:match
				leftArm._send('setCycle:', End)
				state.post('++')
				followItem._send('init:')
				self._send('cue:')
			#end:case
			case 1:
				ticks = 15
			#end:case
			case 2:
				if (local3[local69.post('++')] != -1):
					(state -= 2)
					if (local3[local69] == -99):
						singSing._send('loop:', (singSing._send('loop:') + 1))
						followItem._send('loop:', (followItem._send('loop:') + 1))
						local69.post('++')
					#endif
					temp40 = local3[local69]
					temp41 = local3[local69.post('++')]
					temp42 = local3[local69.post('++')]
					singSing._send('posn:', temp40, temp41, 'cel:', temp42)
					followItem._send('posn:', temp40, temp41, 'cel:', temp42)
				#endif
				self._send('cue:')
			#end:case
			case 3:
				cHead._send('init:', 0)
				seconds = 2
			#end:case
			case 4:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class singSingLeaveScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if (not local71):
					leftArm._send('view:', 1401, 'loop:', 0, 'cel:', 2)
					rightArm._send('dispose:')
				#endif
				match register
					case 1:
						followItem._send('init:', 'loop:', 1, 'view:', 1413)
					#end:case
					case 2:
						followItem._send('init:', 'view:', 1411, 'loop:', 3)
					#end:case
					else:
						register = 0
					#end:else
				#end:match
				local69 = -1
				singSing._send('loop:', 3)
				state.post('++')
				self._send('cue:')
			#end:case
			case 1:
				ticks = 20
			#end:case
			case 2:
				if (local38[local69.post('++')] != -1):
					(state -= 2)
					if (local38[local69] == -99):
						singSing._send('loop:', (singSing._send('loop:') + 1))
						if register:
							followItem._send('loop:', (followItem._send('loop:') + 1))
						#endif
						local69.post('++')
					#endif
					temp0 = local38[local69]
					temp1 = local38[local69.post('++')]
					temp2 = local38[local69.post('++')]
					singSing._send('posn:', temp0, temp1, 'cel:', temp2)
					if register:
						followItem._send('posn:', temp0, temp1, 'cel:', temp2)
					#endif
				#endif
				self._send('cue:')
			#end:case
			case 3:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class ringSegueScr(CartoonScript):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		if script:
			script._send('dispose:')
		#endif
		match state = param1
			case 0:
				self._send('setScript:', singSingEnterScr, self, 0)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				global91._send('say:', 1, 0, 1, 1, self)
			#end:case
			case 3:
				ticks = 12
			#end:case
			case 4:
				rightArm._send('init:')
				followItem._send('dispose:')
				leftArm._send('view:', 1422, 'loop:', 0, 'cel:', 0, 'setCycle:', CT, 1, 1, self)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				global91._send('say:', 1, 0, 1, 2, self)
			#end:case
			case 8:
				cycles = 2
			#end:case
			case 9:
				global91._send('say:', 1, 0, 1, 3, self)
			#end:case
			case 10:
				cHead._send('dispose:')
				ticks = 12
			#end:case
			case 11:
				leftArm._send('loop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 12:
				ticks = 30
			#end:case
			case 13:
				global91._send('say:', 1, 0, 1, 4, self)
			#end:case
			case 14:
				ticks = 12
			#end:case
			case 15:
				leftArm._send('view:', 1423, 'loop:', 0, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 16:
				cycles = 2
			#end:case
			case 17:
				if ((local2 == 210) and (local0 == 210)):
					global91._send('say:', 1, 0, 8, 1, self)
				else:
					global91._send('say:', 1, 0, 1, 5, self)
				#endif
			#end:case
			case 18:
				self._send('setScript:', singSingLeaveScr, self, 1)
			#end:case
			case 19:
				global2._send('newRoom:', 210)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class roseSegueScr(CartoonScript):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				self._send('setScript:', singSingEnterScr, self, 1)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				(= register
					(cond
						case ((local1 != 210) and (local0 != 210)): 5#end:case
						case ((local1 != 210) and (local0 == 210)): 6#end:case
						else: 4#end:else
					)
				)
				self._send('cue:')
			#end:case
			case 3:
				rightArm._send('init:')
				followItem._send('dispose:')
				leftArm._send('view:', 1424, 'loop:', 0, 'cel:', 0)
				if (register == 4):
					cHead._send('init:', 0)
					leftArm._send('setCycle:', End, self)
				else:
					cHead._send('init:', 1)
					local71 = 1
					leftArm._send('setCycle:', CT, 1, 1, self)
				#endif
			#end:case
			case 4:
				ticks = 30
			#end:case
			case 5:
				if (register != 4):
					state = 10
					global91._send('say:', 1, 0, register, 1, self)
				else:
					leftArm._send('setPri:', 15)
					leftArm._send('setCycle:', Beg, self)
				#endif
			#end:case
			case 6:
				global91._send('say:', 1, 0, register, 1, self)
			#end:case
			case 7:
				if (register == 4):
					cHead._send('init:', 0)
				#endif
				cycles = 2
			#end:case
			case 8:
				if (local0 != 210):
					state = 10
					global91._send('say:', 1, 0, 9, 1, self)
				else:
					global91._send('say:', 1, 0, register, 2, self)
				#endif
			#end:case
			case 9:
				cycles = 2
			#end:case
			case 10:
				global91._send('say:', 1, 0, register, 3, self)
			#end:case
			case 11:
				if global5._send('contains:', cHead):
					cHead._send('dispose:')
				#endif
				self._send('setScript:', singSingLeaveScr, self)
			#end:case
			case 12:
				global2._send('newRoom:', 210)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class poemSegueScr(CartoonScript):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				self._send('setScript:', singSingEnterScr, self, 2)
			#end:case
			case 1:
				register = (3 if (local1 != 210) else 2)
				cycles = 2
			#end:case
			case 2:
				global91._send('say:', 1, 0, register, 1, self)
			#end:case
			case 3:
				ticks = 25
			#end:case
			case 4:
				leftArm._send('view:', 1421, 'loop:', 0, 'cel:', 0, 'setCycle:', End, self)
				followItem._send('dispose:')
				rightArm._send('init:')
				if (local1 != 210):
					cHead._send('init:', 1)
				#endif
			#end:case
			case 5:
				global91._send('say:', 1, 0, register, 2, self)
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				global91._send('say:', 1, 0, register, 3, self)
				if (register == 3):
					(state += 9)
				#endif
			#end:case
			case 8:
				cycles = 2
			#end:case
			case 9:
				cHead._send('init:', 2)
				global91._send('say:', 1, 0, register, 4, self, 140)
			#end:case
			case 10:
				cycles = 2
			#end:case
			case 11:
				if (local2 == 210):
					global91._send('say:', 1, 0, 7, 1, self)
				else:
					global91._send('say:', 1, 0, register, 5, self)
				#endif
			#end:case
			case 12:
				leftArm._send('loop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 13:
				ticks = 20
			#end:case
			case 14:
				leftArm._send('setCycle:', Beg, self)
			#end:case
			case 15:
				cycles = 2
			#end:case
			case 16:
				leftArm._send('loop:', 0, 'cel:', 0)
				ticks = 30
			#end:case
			case 17:
				cHead._send('dispose:')
				self._send(
					'setScript:', singSingLeaveScr, self, if 
							proc999_5(register, 7, 2)
							2
						else:
							0
						#endif
				)
			#end:case
			case 18:
				global2._send('newRoom:', 210)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class singSing(Actor):
	#property vars (may be empty)
	x = 285
	y = 48
	view = 141
	loop = 1
	signal = 16384
	illegalBits = 0
	
	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('loop:', 0, 'setPri:', 14)
	#end:method

#end:class or instance

@SCI.instance
class leftArm(Prop):
	#property vars (may be empty)
	x = 87
	y = 161
	view = 1401
	signal = 16384
	
#end:class or instance

@SCI.instance
class rightArm(Prop):
	#property vars (may be empty)
	x = 142
	y = 157
	view = 1401
	loop = 1
	signal = 16384
	
#end:class or instance

@SCI.instance
class followItem(Actor):
	#property vars (may be empty)
	view = 1412
	priority = 15
	signal = 16400
	illegalBits = 0
	
#end:class or instance

@SCI.instance
class cassyMouth(Prop):
	#property vars (may be empty)
	x = 106
	y = 97
	view = 142
	loop = 3
	signal = 16384
	
#end:class or instance

@SCI.instance
class cassyMouth2(Prop):
	#property vars (may be empty)
	x = 122
	y = 82
	view = 140
	loop = 1
	signal = 16384
	
#end:class or instance

@SCI.instance
class cHead(Prop):
	#property vars (may be empty)
	x = 91
	y = 55
	view = 142
	loop = 2
	
	@classmethod
	def init(param1 = None, *rest):
		(= loop
			match param1
				case 0: 0#end:case
				case 1: 1#end:case
				case 2: 2#end:case
			#end:match
		)
		super._send('init:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class localMessager(Messager):
	#property vars (may be empty)
	@classmethod
	def findTalker(param1 = None, *rest):
		(= temp0
			match param1
				case 28: Cassima#end:case
				case 99: global89#end:case
			#end:match
		)
	#end:method

#end:class or instance

@SCI.instance
class Cassima(Kq6Talker):
	#property vars (may be empty)
	x = 5
	y = 5
	view = 891
	talkWidth = 213
	textX = 79
	textY = 8
	
	@classmethod
	def init():
		if global5._send('contains:', cHead):
			cel = 1
			self._send('x:', 94, 'y:', 87, 'textX:', -60, 'textY:', 30)
			super._send('init:', 0, 0, cassyMouth, &rest)
		else:
			cel = 1
			self._send('x:', 97, 'y:', 85, 'textX:', -60, 'textY:', 30)
			super._send('init:', 0, 0, cassyMouth2, &rest)
		#endif
	#end:method

#end:class or instance

