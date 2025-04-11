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
	argc = sum(v is not None for v in locals().values())

	(kernel.ScriptID(480, 5) register: 1)
	(global0 setScript: takeBottleAway 0 kernel.ScriptID(480, 6))
#end:procedure

@SCI.procedure
def proc481_1(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(kernel.ScriptID(480, 5) register: 1)
	if (not proc913_0(118)):
		proc913_1(118)
		(global1 givePoints: 2)
	#endif
	match param1
		case 1:
			local2 = 0
			local3 = 12
			(kernel.ScriptID(40, 0) bottleSucker: 1)
			(global0 setScript: giveBabyBottle 0 babyFace1)
		#end:case
		case 2:
			local2 = 1
			local3 = 11
			(kernel.ScriptID(40, 0) bottleSucker: 2)
			(global0 setScript: giveBabyBottle 0 babyFace2)
		#end:case
		case 3:
			local2 = 0
			local3 = 9
			(kernel.ScriptID(40, 0) bottleSucker: 3)
			(global0 setScript: giveBabyBottle 0 babyFace3)
		#end:case
		case 4:
			local2 = 0
			local3 = 7
			(kernel.ScriptID(40, 0) bottleSucker: 4)
			(global2 setScript: giveBabyBottle 0 babyFace4)
		#end:case
	#end:match
#end:procedure

@SCI.procedure
def proc481_3(param1 = None):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(kernel.ScriptID(480, 5) register: 1)
	match param1
		case 1:
			(global0 setScript: getBabyTears 0 babyFace1)
		#end:case
		case 2:
			(global0 setScript: getBabyTears 0 babyFace2)
		#end:case
		case 3:
			(global0 setScript: getBabyTears 0 babyFace3)
		#end:case
		case 4:
			(global0 setScript: getBabyTears 0 babyFace4)
		#end:case
	#end:match
#end:procedure

@SCI.procedure
def proc481_6():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(cryMusic stop: dispose:)
	(suckMusic stop: dispose:)
	if (global5 contains: babyFace1):
		(babyFace1 setCycle: 0 dispose: delete:)
	#endif
	if (global5 contains: babyFace2):
		(babyFace2 setCycle: 0 dispose: delete:)
	#endif
	if (global5 contains: babyFace3):
		(babyFace3 setCycle: 0 dispose: delete:)
	#endif
	if (global5 contains: babyFace4):
		(babyFace4 setCycle: 0 dispose: delete:)
	#endif
	kernel.DisposeScript(481)
#end:procedure

@SCI.procedure
def proc481_7():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	if ((babyFace1 bottleNum:) != (kernel.ScriptID(40, 0) bottleSucker:)):
		(babyFace1 init: setCycle: Fwd)
	#endif
	if ((babyFace2 bottleNum:) != (kernel.ScriptID(40, 0) bottleSucker:)):
		(babyFace2 init: setCycle: Fwd)
	#endif
	if ((babyFace3 bottleNum:) != (kernel.ScriptID(40, 0) bottleSucker:)):
		(babyFace3 init: setCycle: Fwd)
	#endif
	if ((babyFace4 bottleNum:) != (kernel.ScriptID(40, 0) bottleSucker:)):
		(babyFace4 init: setCycle: Fwd)
	#endif
	(cryMusic setLoop: -1 play:)
	(suckMusic setLoop: -1 play:)
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
		argc = sum(v is not None for v in locals().values())

		(cryMusic stop: dispose:)
		(suckMusic stop: dispose:)
		(super dispose:)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if proc999_5(param1, 57, 58, 59, 60, 96):
			if ((kernel.ScriptID(40, 0) bottleSucker:) == (self bottleNum:)):
				(global91 say: 9 56 17 0 0 480)
			else:
				(global91 say: 9 56 (kernel.ScriptID(40, 0) lampMsg:) 0 0 480)
			#endif
		else:
			match param1
				case 14:
					(global91 say: 9 14 0 1 0 480)
				#end:case
				case 5:
					(cond
						case 
							(==
								(kernel.ScriptID(40, 0) bottleSucker:)
								(self bottleNum:)
							):
							(global2
								setScript: takeBottleAway 0 kernel.ScriptID(480, 6)
							)
						#end:case
						case ((kernel.ScriptID(40, 0) lampMsg:) == 15):
							(global91 say: 9 5 15 1 0 480)
						#end:case
						else:
							(global91 say: 9 5 18 1 0 480)
						#end:else
					)
				#end:case
				case 43:
					(cond
						case 
							(==
								(kernel.ScriptID(40, 0) bottleSucker:)
								(self bottleNum:)
							):
							(global91 say: 9 43 17 1 0 480)
						#end:case
						case (not proc913_0(77)):
							(global91 say: 9 43 21 1 0 480)
						#end:case
						case ((global161 & 0x0004) or proc913_0(144)):
							(global91 say: 9 43 20 1 0 480)
						#end:case
						case (global161 & 0x0001):
							(global91 say: 9 43 13 1 0 480)
						#end:case
						case (global161 & 0x0002):
							(global2 setScript: getBabyTears 0 self)
						#end:case
						case ((kernel.ScriptID(40, 0) lampMsg:) == 15):
							(global91 say: 9 43 15 1 0 480)
						#end:case
						else:
							(global2 setScript: getBabyTears 0 self)
						#end:else
					)
				#end:case
				case 1:
					if ((kernel.ScriptID(40, 0) lampMsg:) == 15):
						(global91 say: 9 1 (kernel.ScriptID(40, 0) lampMsg:) 1 0 480)
					else:
						(global91 say: 9 1 16 1 0 480)
					#endif
				#end:case
				case 2:
					if ((kernel.ScriptID(40, 0) lampMsg:) == 15):
						(global91 say: 9 2 (kernel.ScriptID(40, 0) lampMsg:) 0 0 480)
					else:
						(global91 say: 9 2 16 1 0 480)
					#endif
				#end:case
				case 44:
					(cond
						case 
							(==
								(kernel.ScriptID(40, 0) bottleSucker:)
								(self bottleNum:)
							):
							(global91 say: 9 44 17 1 0 480)
						#end:case
						case (not proc913_0(77)):
							(global91 say: 9 44 21 1 0 480)
						#end:case
						else:
							(global91 say: 9 44 22 1 0 480)
						#end:else
					)
				#end:case
				case 24:
					if ((kernel.ScriptID(40, 0) lampMsg:) == 15):
						(global91 say: 9 24 15 1 0 480)
					else:
						(global91 say: 9 24 16 1 0 480)
					#endif
				#end:case
				else:
					(self setScript: inventOnBaby 0 self)
				#end:else
			#end:match
		#endif
	#end:method

#end:class or instance

@SCI.instance
class inventOnBaby(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					setMotion:
						PolyPath
						(register walkToX:)
						(register walkToY:)
						self
				)
			#end:case
			case 1:
				(= temp0
					kernel.GetAngle((global0 x:), (global0 y:), (register x:), (register
						y:
					))
				)
				(global0 setHeading: temp0 self)
			#end:case
			case 2:
				cycles = 6
			#end:case
			case 3:
				(global91 say: 9 0 16 0 self 480)
			#end:case
			case 4:
				(global1 handsOn:)
				(self dispose:)
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
		argc = sum(v is not None for v in locals().values())

		if (and local0 kernel.DoAudio(4) (kernel.DoAudio(6) == -1) (not global84)):
			(self play:)
		#endif
		(super check:)
	#end:method

	@classmethod
	def stop():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		local0 = 0
		(super stop:)
	#end:method

	@classmethod
	def play():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		local0 = 1
		(super play:)
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
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				if (register != babyFace2):
					proc913_1(59)
				#endif
				(global0
					setMotion:
						PolyPath
						(register walkToX:)
						(register walkToY:)
						self
				)
			#end:case
			case 1:
				(global0
					view: 4811
					setLoop: 1
					cel: 0
					posn: (register stoopX:) (register stoopY:)
					normal: 0
					cycleSpeed: 12
					setCycle: End self
				)
				kernel.UnLoad(128, 900)
			#end:case
			case 2:
				(global91 say: 9 62 0 1 self 480)
			#end:case
			case 3:
				(cryMusic setLoop: -1 play:)
				(suckMusic setLoop: -1 play:)
				(kernel.ScriptID(480, 6)
					setLoop:
						if ((register == babyFace1) or (register == babyFace2)):
							1
						else:
							0
						#endif
					x: ((global0 x:) - 24)
					y: ((global0 y:) - 10)
					z: 5
					setPri: local3
					init:
				)
				if proc913_0(77):
					(kernel.ScriptID(40, 0) lampMsg: 22)
				else:
					(kernel.ScriptID(40, 0) lampMsg: 21)
				#endif
				if (register != babyFace1):
					(babyFace1 init: setCycle: Fwd)
				#endif
				if (register != babyFace2):
					(babyFace2 init: setCycle: Fwd)
				#endif
				if (register != babyFace3):
					(babyFace3 init: setCycle: Fwd)
				#endif
				if (register != babyFace4):
					(babyFace4 init: setCycle: Fwd)
				#endif
				(global0 setLoop: 3 cycleSpeed: 3 setCycle: Beg self)
				kernel.UnLoad(128, 4811)
			#end:case
			case 4:
				(global0 posn: (register walkToX:) (register walkToY:) reset: 1)
				ticks = 8
			#end:case
			case 5:
				(global91 say: 9 62 0 2 self 480)
			#end:case
			case 6:
				(global0 setMotion: PolyPath 135 170 self)
			#end:case
			case 7:
				(global91 say: 9 62 0 3 self 480)
			#end:case
			case 8:
				(cryMusic setLoop: -1 play:)
				(global1 handsOn:)
				proc913_2(59)
				(register hide:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getBabyTears(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					setMotion:
						PolyPath
						(register walkToX:)
						(register walkToY:)
						self
				)
			#end:case
			case 1:
				(global0
					view: 4811
					setLoop: 0
					cel: 0
					posn: (register stoopX:) (register stoopY:)
					normal: 0
					cycleSpeed: 6
					setCycle: End self
				)
				kernel.UnLoad(128, 900)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				(global0 setCycle: Beg self)
			#end:case
			case 4:
				(global161 |= 0x0004)
				(global1 givePoints: 1)
				(global0 reset: 1 posn: (register walkToX:) (register walkToY:))
				kernel.UnLoad(128, 4811)
				ticks = 8
			#end:case
			case 5:
				if (global161 & 0x0002):
					(global91 say: 9 43 14 1 self 480)
				else:
					(global91 say: 9 43 19 1 self 480)
				#endif
			#end:case
			case 6:
				(global0 setMotion: PolyPath 135 170 self)
			#end:case
			case 7:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class takeBottleAway(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0
					setMotion:
						PolyPath
						((kernel.ScriptID(480, 6) x:) + 45)
						((kernel.ScriptID(480, 6) y:) + 1)
						self
				)
			#end:case
			case 1:
				(global0
					view: 4811
					setLoop: 3
					setPri:
						if local2:
							-1
						else:
							((kernel.ScriptID(480, 6) priority:) + 1)
						#endif
					cel: 0
					posn:
						((kernel.ScriptID(480, 6) x:) + 21)
						((kernel.ScriptID(480, 6) y:) + 6)
					normal: 0
					cycleSpeed: 12
					setCycle: End self
				)
				kernel.UnLoad(128, 900)
			#end:case
			case 2:
				(global91 say: 9 5 17 1 self 480)
			#end:case
			case 3:
				(global0 setCycle: Beg self)
			#end:case
			case 4:
				if ((kernel.ScriptID(40, 0) bottleSucker:) == 3):
					temp0 = 10
				else:
					temp0 = 1
				#endif
				(global0
					reset: 1
					setPri: 15
					posn:
						((kernel.ScriptID(480, 6) x:) + 45)
						((kernel.ScriptID(480, 6) y:) + temp0)
					setMotion: PolyPath 135 170 self
				)
				kernel.UnLoad(128, 4811)
			#end:case
			case 5:
				(global1 handsOn:)
				(global0 setPri: -1)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

