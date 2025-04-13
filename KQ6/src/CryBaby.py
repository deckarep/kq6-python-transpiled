#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 481
import sci_sh
import kernel
import Main
import Kq6Sound
import n913
import PolyPath
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	proc481_0 = 0,
	proc481_1 = 1,
	takeBottleAway = 2,
	proc481_3 = 3,
	cryMusic = 4,
	suckMusic = 5,
	proc481_6 = 6,
	proc481_7 = 7,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None


@SCI.procedure
def proc481_0():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	kernel.ScriptID(480, 5)._send('register:', 1)
	global0._send('setScript:', takeBottleAway, 0, kernel.ScriptID(480, 6))
#end:procedure

@SCI.procedure
def proc481_1(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	kernel.ScriptID(480, 5)._send('register:', 1)
	if (not proc913_0(118)):
		proc913_1(118)
		global1._send('givePoints:', 2)
	#endif
	match param1
		case 1:
			local2 = 0
			local3 = 12
			kernel.ScriptID(40, 0)._send('bottleSucker:', 1)
			global0._send('setScript:', giveBabyBottle, 0, babyFace1)
		#end:case
		case 2:
			local2 = 1
			local3 = 11
			kernel.ScriptID(40, 0)._send('bottleSucker:', 2)
			global0._send('setScript:', giveBabyBottle, 0, babyFace2)
		#end:case
		case 3:
			local2 = 0
			local3 = 9
			kernel.ScriptID(40, 0)._send('bottleSucker:', 3)
			global0._send('setScript:', giveBabyBottle, 0, babyFace3)
		#end:case
		case 4:
			local2 = 0
			local3 = 7
			kernel.ScriptID(40, 0)._send('bottleSucker:', 4)
			global2._send('setScript:', giveBabyBottle, 0, babyFace4)
		#end:case
	#end:match
#end:procedure

@SCI.procedure
def proc481_3(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	kernel.ScriptID(480, 5)._send('register:', 1)
	match param1
		case 1:
			global0._send('setScript:', getBabyTears, 0, babyFace1)
		#end:case
		case 2:
			global0._send('setScript:', getBabyTears, 0, babyFace2)
		#end:case
		case 3:
			global0._send('setScript:', getBabyTears, 0, babyFace3)
		#end:case
		case 4:
			global0._send('setScript:', getBabyTears, 0, babyFace4)
		#end:case
	#end:match
#end:procedure

@SCI.procedure
def proc481_6():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	cryMusic._send('stop:', 'dispose:')
	suckMusic._send('stop:', 'dispose:')
	if global5._send('contains:', babyFace1):
		babyFace1._send('setCycle:', 0, 'dispose:', 'delete:')
	#endif
	if global5._send('contains:', babyFace2):
		babyFace2._send('setCycle:', 0, 'dispose:', 'delete:')
	#endif
	if global5._send('contains:', babyFace3):
		babyFace3._send('setCycle:', 0, 'dispose:', 'delete:')
	#endif
	if global5._send('contains:', babyFace4):
		babyFace4._send('setCycle:', 0, 'dispose:', 'delete:')
	#endif
	kernel.DisposeScript(481)
#end:procedure

@SCI.procedure
def proc481_7():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	if (babyFace1._send('bottleNum:') != kernel.ScriptID(40, 0)._send('bottleSucker:')):
		babyFace1._send('init:', 'setCycle:', Fwd)
	#endif
	if (babyFace2._send('bottleNum:') != kernel.ScriptID(40, 0)._send('bottleSucker:')):
		babyFace2._send('init:', 'setCycle:', Fwd)
	#endif
	if (babyFace3._send('bottleNum:') != kernel.ScriptID(40, 0)._send('bottleSucker:')):
		babyFace3._send('init:', 'setCycle:', Fwd)
	#endif
	if (babyFace4._send('bottleNum:') != kernel.ScriptID(40, 0)._send('bottleSucker:')):
		babyFace4._send('init:', 'setCycle:', Fwd)
	#endif
	cryMusic._send('setLoop:', -1, 'play:')
	suckMusic._send('setLoop:', -1, 'play:')
#end:procedure

class CryBaby(Prop):
	#property vars (may be empty)
	walkToX = 0
	walkToY = 0
	stoopX = 0
	stoopY = 0
	bottleNum = 0
	
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		cryMusic._send('stop:', 'dispose:')
		suckMusic._send('stop:', 'dispose:')
		super._send('dispose:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if proc999_5(param1, 57, 58, 59, 60, 96):
			if (kernel.ScriptID(40, 0)._send('bottleSucker:') == self._send('bottleNum:')):
				global91._send('say:', 9, 56, 17, 0, 0, 480)
			else:
				global91._send('say:', 9, 56, kernel.ScriptID(40, 0)._send('lampMsg:'), 0, 0, 480)
			#endif
		else:
			match param1
				case 14:
					global91._send('say:', 9, 14, 0, 1, 0, 480)
				#end:case
				case 5:
					(cond
						case 
							(==
								kernel.ScriptID(40, 0)._send('bottleSucker:')
								self._send('bottleNum:')
							):
							global2._send(
								'setScript:', takeBottleAway, 0, kernel.ScriptID(480, 6)
							)
						#end:case
						case (kernel.ScriptID(40, 0)._send('lampMsg:') == 15):
							global91._send('say:', 9, 5, 15, 1, 0, 480)
						#end:case
						else:
							global91._send('say:', 9, 5, 18, 1, 0, 480)
						#end:else
					)
				#end:case
				case 43:
					(cond
						case 
							(==
								kernel.ScriptID(40, 0)._send('bottleSucker:')
								self._send('bottleNum:')
							):
							global91._send('say:', 9, 43, 17, 1, 0, 480)
						#end:case
						case (not proc913_0(77)):
							global91._send('say:', 9, 43, 21, 1, 0, 480)
						#end:case
						case ((global161 & 0x0004) or proc913_0(144)):
							global91._send('say:', 9, 43, 20, 1, 0, 480)
						#end:case
						case (global161 & 0x0001):
							global91._send('say:', 9, 43, 13, 1, 0, 480)
						#end:case
						case (global161 & 0x0002):
							global2._send('setScript:', getBabyTears, 0, self)
						#end:case
						case (kernel.ScriptID(40, 0)._send('lampMsg:') == 15):
							global91._send('say:', 9, 43, 15, 1, 0, 480)
						#end:case
						else:
							global2._send('setScript:', getBabyTears, 0, self)
						#end:else
					)
				#end:case
				case 1:
					if (kernel.ScriptID(40, 0)._send('lampMsg:') == 15):
						global91._send('say:', 9, 1, kernel.ScriptID(40, 0)._send('lampMsg:'), 1, 0, 480)
					else:
						global91._send('say:', 9, 1, 16, 1, 0, 480)
					#endif
				#end:case
				case 2:
					if (kernel.ScriptID(40, 0)._send('lampMsg:') == 15):
						global91._send('say:', 9, 2, kernel.ScriptID(40, 0)._send('lampMsg:'), 0, 0, 480)
					else:
						global91._send('say:', 9, 2, 16, 1, 0, 480)
					#endif
				#end:case
				case 44:
					(cond
						case 
							(==
								kernel.ScriptID(40, 0)._send('bottleSucker:')
								self._send('bottleNum:')
							):
							global91._send('say:', 9, 44, 17, 1, 0, 480)
						#end:case
						case (not proc913_0(77)):
							global91._send('say:', 9, 44, 21, 1, 0, 480)
						#end:case
						else:
							global91._send('say:', 9, 44, 22, 1, 0, 480)
						#end:else
					)
				#end:case
				case 24:
					if (kernel.ScriptID(40, 0)._send('lampMsg:') == 15):
						global91._send('say:', 9, 24, 15, 1, 0, 480)
					else:
						global91._send('say:', 9, 24, 16, 1, 0, 480)
					#endif
				#end:case
				else:
					self._send('setScript:', inventOnBaby, 0, self)
				#end:else
			#end:match
		#endif
	#end:method

#end:class or instance

@SCI.instance
class inventOnBaby(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send(
					'setMotion:', PolyPath, register._send('walkToX:'), register._send(
							'walkToY:'
						), self
				)
			#end:case
			case 1:
				(= temp0
					kernel.GetAngle(global0._send('x:'), global0._send('y:'), register._send(
						'x:'
					), register._send('y:'))
				)
				global0._send('setHeading:', temp0, self)
			#end:case
			case 2:
				cycles = 6
			#end:case
			case 3:
				global91._send('say:', 9, 0, 16, 0, self, 480)
			#end:case
			case 4:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class babyFace1(CryBaby):
	#property vars (may be empty)
	x = 51
	y = 152
	noun = 9
	modNum = 480
	view = 4803
	priority = 12
	signal = 16400
	walkToX = 95
	walkToY = 159
	stoopX = 83
	stoopY = 162
	bottleNum = 1
	
#end:class or instance

@SCI.instance
class babyFace2(CryBaby):
	#property vars (may be empty)
	x = 6
	y = 147
	noun = 9
	modNum = 480
	view = 4803
	loop = 1
	priority = 11
	signal = 16400
	walkToX = 55
	walkToY = 153
	stoopX = 36
	stoopY = 157
	bottleNum = 2
	
#end:class or instance

@SCI.instance
class babyFace3(CryBaby):
	#property vars (may be empty)
	x = 35
	y = 122
	noun = 9
	modNum = 480
	view = 4803
	loop = 2
	priority = 9
	signal = 16400
	walkToX = 81
	walkToY = 131
	stoopX = 63
	stoopY = 135
	bottleNum = 3
	
#end:class or instance

@SCI.instance
class babyFace4(CryBaby):
	#property vars (may be empty)
	x = 15
	y = 107
	noun = 9
	modNum = 480
	view = 4803
	loop = 3
	priority = 7
	signal = 16400
	walkToX = 62
	walkToY = 116
	stoopX = 43
	stoopY = 119
	bottleNum = 4
	
#end:class or instance

@SCI.instance
class cryMusic(Kq6Sound):
	#property vars (may be empty)
	number = 481
	loop = -1
	
	@classmethod
	def check():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (local0 and kernel.DoAudio(4) and (kernel.DoAudio(6) == -1) and (not global84)):
			self._send('play:')
		#endif
		super._send('check:')
	#end:method

	@classmethod
	def stop():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		local0 = 0
		super._send('stop:')
	#end:method

	@classmethod
	def play():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		local0 = 1
		super._send('play:')
	#end:method

#end:class or instance

@SCI.instance
class suckMusic(Kq6Sound):
	#property vars (may be empty)
	number = 485
	loop = -1
	
#end:class or instance

@SCI.instance
class giveBabyBottle(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				if (register != babyFace2):
					proc913_1(59)
				#endif
				global0._send(
					'setMotion:', PolyPath, register._send('walkToX:'), register._send(
							'walkToY:'
						), self
				)
			#end:case
			case 1:
				global0._send(
					'view:', 4811,
					'setLoop:', 1,
					'cel:', 0,
					'posn:', register._send('stoopX:'), register._send('stoopY:'),
					'normal:', 0,
					'cycleSpeed:', 12,
					'setCycle:', End, self
				)
				kernel.UnLoad(128, 900)
			#end:case
			case 2:
				global91._send('say:', 9, 62, 0, 1, self, 480)
			#end:case
			case 3:
				cryMusic._send('setLoop:', -1, 'play:')
				suckMusic._send('setLoop:', -1, 'play:')
				kernel.ScriptID(480, 6)._send(
					'setLoop:', if 
							((register == babyFace1) or (register == babyFace2))
							1
						else:
							0
						#endif,
					'x:', (global0._send('x:') - 24),
					'y:', (global0._send('y:') - 10),
					'z:', 5,
					'setPri:', local3,
					'init:'
				)
				if proc913_0(77):
					kernel.ScriptID(40, 0)._send('lampMsg:', 22)
				else:
					kernel.ScriptID(40, 0)._send('lampMsg:', 21)
				#endif
				if (register != babyFace1):
					babyFace1._send('init:', 'setCycle:', Fwd)
				#endif
				if (register != babyFace2):
					babyFace2._send('init:', 'setCycle:', Fwd)
				#endif
				if (register != babyFace3):
					babyFace3._send('init:', 'setCycle:', Fwd)
				#endif
				if (register != babyFace4):
					babyFace4._send('init:', 'setCycle:', Fwd)
				#endif
				global0._send('setLoop:', 3, 'cycleSpeed:', 3, 'setCycle:', Beg, self)
				kernel.UnLoad(128, 4811)
			#end:case
			case 4:
				global0._send('posn:', register._send('walkToX:'), register._send('walkToY:'), 'reset:', 1)
				ticks = 8
			#end:case
			case 5:
				global91._send('say:', 9, 62, 0, 2, self, 480)
			#end:case
			case 6:
				global0._send('setMotion:', PolyPath, 135, 170, self)
			#end:case
			case 7:
				global91._send('say:', 9, 62, 0, 3, self, 480)
			#end:case
			case 8:
				cryMusic._send('setLoop:', -1, 'play:')
				global1._send('handsOn:')
				proc913_2(59)
				register._send('hide:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getBabyTears(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send(
					'setMotion:', PolyPath, register._send('walkToX:'), register._send(
							'walkToY:'
						), self
				)
			#end:case
			case 1:
				global0._send(
					'view:', 4811,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', register._send('stoopX:'), register._send('stoopY:'),
					'normal:', 0,
					'cycleSpeed:', 6,
					'setCycle:', End, self
				)
				kernel.UnLoad(128, 900)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 4:
				(global161 |= 0x0004)
				global1._send('givePoints:', 1)
				global0._send('reset:', 1, 'posn:', register._send('walkToX:'), register._send('walkToY:'))
				kernel.UnLoad(128, 4811)
				ticks = 8
			#end:case
			case 5:
				if (global161 & 0x0002):
					global91._send('say:', 9, 43, 14, 1, self, 480)
				else:
					global91._send('say:', 9, 43, 19, 1, self, 480)
				#endif
			#end:case
			case 6:
				global0._send('setMotion:', PolyPath, 135, 170, self)
			#end:case
			case 7:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class takeBottleAway(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send(
					'setMotion:', PolyPath, (kernel.ScriptID(480, 6)._send('x:') + 45), (+
							kernel.ScriptID(480, 6)._send('y:')
							1
						), self
				)
			#end:case
			case 1:
				global0._send(
					'view:', 4811,
					'setLoop:', 3,
					'setPri:', if local2:
							-1
						else:
							(kernel.ScriptID(480, 6)._send('priority:') + 1)
						#endif,
					'cel:', 0,
					'posn:', (kernel.ScriptID(480, 6)._send('x:') + 21), (+
							kernel.ScriptID(480, 6)._send('y:')
							6
						),
					'normal:', 0,
					'cycleSpeed:', 12,
					'setCycle:', End, self
				)
				kernel.UnLoad(128, 900)
			#end:case
			case 2:
				global91._send('say:', 9, 5, 17, 1, self, 480)
			#end:case
			case 3:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 4:
				if (kernel.ScriptID(40, 0)._send('bottleSucker:') == 3):
					temp0 = 10
				else:
					temp0 = 1
				#endif
				global0._send(
					'reset:', 1,
					'setPri:', 15,
					'posn:', (kernel.ScriptID(480, 6)._send('x:') + 45), (+
							kernel.ScriptID(480, 6)._send('y:')
							temp0
						),
					'setMotion:', PolyPath, 135, 170, self
				)
				kernel.UnLoad(128, 4811)
			#end:case
			case 5:
				global1._send('handsOn:')
				global0._send('setPri:', -1)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

