#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 80
import sci_sh
import kernel
import Main
import KQ6Room
import n913
import Scaler
import PolyPath
import StopWalk
import Grooper
import Motion
import Game
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rgCastle = 0,
	proc80_2 = 2,
	guardsGetEgo = 4,
	guard1 = 5,
	guard2 = 6,
	proc80_7 = 7,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None


@SCI.procedure
def proc80_2(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	(global1 handsOff:)
	match param1
		case 4:
			temp0 = -40
			temp1 = 0
		#end:case
		case 2:
			temp0 = 40
			temp1 = 0
		#end:case
		case 1:
			temp0 = 0
			temp1 = -40
		#end:case
	#end:match
	(global0
		ignoreActors: 1
		setMotion: MoveTo ((global0 x:) + temp0) ((global0 y:) + temp1)
	)
#end:procedure

@SCI.procedure
def localproc_0(param1 = None, param2 = None, param3 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	temp2 = ((global0 brLeft:) - param2)
	temp0 = ((global0 brTop:) - param3)
	temp3 = ((global0 brRight:) + param2)
	temp1 = ((global0 brBottom:) + param3)
	if (not local2):
		if (global2 moveOtherGuard:):
			local2.post('++')
		#endif
		local0 = proc999_3(temp2, proc999_2(temp3, (param1 x:)))
		local1 = proc999_3(temp0, proc999_2(temp1, (param1 y:)))
	else:
		local2 = 0
		temp4 = ((((global0 x:) <= (param1 x:)) * 2) - 1)
		(= local0
			(+
				(global0 x:)
				(*
					((((global0 brRight:) - (global0 brLeft:)) / 2) + param2)
					temp4
				)
			)
		)
		local1 = proc999_3(temp0, proc999_2(temp1, (param1 y:)))
	#endif
#end:procedure

@SCI.procedure
def proc80_7():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	temp0 = localproc_1(kernel.ScriptID(80, 5))
	temp1 = localproc_1(kernel.ScriptID(80, 6))
	if (temp0 <= temp1):
		kernel.ScriptID(80, 5)
	else:
		kernel.ScriptID(80, 6)
	#endif
#end:procedure

@SCI.procedure
def localproc_1(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	if (global5 contains: param1):
		(= temp0
			kernel.GetDistance((param1 x:), (param1 y:), (global0 x:), (global0 y:), 60)
		)
	else:
		temp0 = 500
	#endif
	return temp0
#end:procedure

class CastleRoom(KQ6Room):
	#property vars (may be empty)
	spotEgoScr = 0
	minScaleSize = 10
	maxScaleSize = 100
	minScaleY = 0
	maxScaleY = 190
	moveOtherGuard = 0
	scalerCode = 0
	
	@classmethod
	def doLoiter():#end:method

	@classmethod
	def warnUser():#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		scalerCode = spotEgoScr = 0
		(super dispose:)
	#end:method

	@classmethod
	def newRoom():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (((global103 prevSignal:) != -1) and ((global103 number:) == 710)):
			(global103 fade:)
		#endif
		(super newRoom: &rest)
	#end:method

	@classmethod
	def spotEgo(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global102 stop:)
		(global103 number: 710 loop: -1 play:)
		if spotEgoScr:
			(global2 setScript: spotEgoScr 0 param1)
		else:
			(param1 setScript: guardsGetEgo &rest)
		#endif
	#end:method

	@classmethod
	def scriptCheck(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 0
		if 
			(and
				proc999_5(param1, 85, 87, 93)
				proc999_5(global11, 710, 720, 730, 770, 780, 781, 800, 810, 820, 840, 850, 860, 870, 880)
			)
			match param1
				case 85:
					(global91 say: 0 0 199 0 0 899)
				#end:case
				case 87:
					(global91 say: 0 0 198 0 0 899)
				#end:case
				case 93:
					(global91 say: 0 0 3 0 0 899)
				#end:case
			#end:match
		else:
			temp0 = 1
		#endif
		return temp0
	#end:method

#end:class or instance

class GuardDog(Actor):
	#property vars (may be empty)
	sightAngle = 95
	cycleSpeed = 10
	moveSpeed = 10
	okToCheck = 0
	checkCode = 0
	regPathID = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(self setScale:)
		(super init: &rest)
		(self
			setCycle: StopWalk -1
			setLoop: Grooper
			setStep: 4 2
			ignoreHorizon:
			illegalBits: 0
			ignoreActors: 1
			signal: (| signal 0x1000)
		)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super doit:)
		if 
			(and
				okToCheck
				((not kernel.IsObject(okToCheck)) or (self perform: okToCheck))
				kernel.IsObject(checkCode)
				(self perform: checkCode)
			)
			checkCode = 0
			(global1 handsOff:)
			(self setMotion: 0)
			(global2 spotEgo: self)
		#endif
		if (kernel.IsObject(global2) and (global2 scalerCode:)):
			(self perform: (global2 scalerCode:))
		#endif
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		regPathID = checkCode = okToCheck = 0
		if kernel.IsObject(scaler):
			(scaler dispose:)
		#endif
		scaler = 0
		(super dispose:)
	#end:method

#end:class or instance

class rgCastle(Rgn):
	#property vars (may be empty)
	rFlag1 = 0
	rFlag2 = 0
	rFlag3 = 0
	dungeonEntered = 0
	lastSeconds = 0
	loiterTimer = -1
	weddingRemind = 0
	guardTimer = 0
	guard2Timer = 0
	guard1Code = 0
	guard2Code = 0
	stopTimers = 0
	weddingMusicCount = -1
	
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = kernel.GetTime(1)
		(cond
			case 
				(and
					(not global84)
					(not ((global69 state:) & 0x0020))
					(lastSeconds != temp0)
					(global11 == global13)
					(not stopTimers)
				):
				lastSeconds = temp0
				if 
					(and
						(loiterTimer > 0)
						(not (global2 script:))
						(loiterTimer.post('--') == 0)
					)
					(self doLoiter:)
				#endif
				if ((weddingRemind > 0) and (weddingRemind.post('--') == 0)):
					if 
						(or
							weddingMusicCount
							(and
								((global6 size:) == 3)
								(not (kernel.ScriptID(81, 0) tstFlag: 709 1))
								(not (kernel.ScriptID(81, 0) tstFlag: 709 2))
							)
							1
						)
						if ((global102 number:) != 701):
							(global102 fadeTo: 701 -1)
						#endif
						(rFlag1 |= 0x0002)
						weddingMusicCount.post('++')
						(global2 warnUser: 1)
					else:
						weddingRemind = 5
					#endif
				#endif
				if ((guardTimer > 0) and (guardTimer.post('--') == 0)):
					(cond
						case (not (rFlag2 & 0x0001)):
							(rFlag2 |= 0x0001)
							if proc999_5(global11, 850, 880, 781):
								(global2 warnUser: 2)
							#endif
						#end:case
						case (global11 == 850):
							(global1 handsOff:)
							(global2 spotEgo: kernel.ScriptID(80, 5))
						#end:case
					)
				#endif
				if ((guard2Timer > 0) and (guard2Timer.post('--') == 0)):
					(cond
						case (not (rFlag2 & 0x0020)):
							(rFlag2 |= 0x0020)
							if (global11 == 870):
								(global2 warnUser: 3 0)
							#endif
						#end:case
						case (global11 == 870):
							(global1 handsOff:)
							(global2 warnUser: 3 1)
						#end:case
					)
				#endif
			#end:case
			case ((global69 state:) & 0x0020):
				lastSeconds = temp0
			#end:case
		)
		(super doit:)
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(kernel.ScriptID(80, 0)
			keep:
				proc999_5(param1, 700, 710, 720, 730, 740, 750, 760, 770, 780, 781, 790, 800, 810, 820, 840, 850, 860, 870, 880, 180, 743)
		)
		initialized = 0
		loiterTimer = -1
		(super newRoom: param1 &rest)
		guard1Code = guard2Code = 0
	#end:method

	@classmethod
	def doLoiter():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		loiterTimer = 0
		(global2 doLoiter:)
	#end:method

	@classmethod
	def setupGuards():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (global5 contains: guard1):
			(guard1 checkCode: guard1Code)
			if (not kernel.IsObject((guard1 scaler:))):
				(guard1
					setScale:
						Scaler
						(global2 maxScaleSize:)
						(global2 minScaleSize:)
						(global2 maxScaleY:)
						(global2 minScaleY:)
				)
				((guard1 scaler:) doit:)
			#endif
		#endif
		if (global5 contains: guard2):
			(guard2 checkCode: guard2Code)
			if (not kernel.IsObject((guard2 scaler:))):
				(guard2
					setScale:
						Scaler
						(global2 maxScaleSize:)
						(global2 minScaleSize:)
						(global2 maxScaleY:)
						(global2 minScaleY:)
				)
				((guard2 scaler:) doit:)
			#endif
		#endif
	#end:method

	@classmethod
	def setFlag(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			temp0 = param1[0]
		#endif
		temp1 = 1
		while (temp1 < argc): # inline for
			(self temp0: (| (self temp0:) param1[temp1]))
			# for:reinit
			temp1.post('++')
		#end:loop
	#end:method

	@classmethod
	def clrFlag(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if argc:
			temp0 = param1[0]
		#endif
		temp1 = 1
		while (temp1 < argc): # inline for
			(self temp0: ((self temp0:) & ~param1[temp1]))
			# for:reinit
			temp1.post('++')
		#end:loop
	#end:method

	@classmethod
	def tstFlag(param1 = None, param2 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return (1 if ((self param1:) & param2) else 0)
	#end:method

#end:class or instance

@SCI.instance
class guardsGetEgo(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(rgCastle rFlag1: (| (rgCastle rFlag1:) 0x2000) dungeonEntered: 3)
		register = 0
		(super dispose:)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 ignoreActors: setMotion: 0)
				if 
					(and
						(not ((global0 signal:) & 0x0800))
						(not (global0 facingMe: client))
					)
					proc913_4(global0, client, self)
				else:
					cycles = 2
				#endif
			#end:case
			case 1:
				cycles = 4
			#end:case
			case 2:
				localproc_0(client, 8, 5)
				(client
					setSpeed: 3
					ignoreHorizon: 1
					ignoreActors: 1
					setMotion: PolyPath local0 local1 self
				)
				if (global2 moveOtherGuard:):
					match client
						case guard1:
							temp0 = guard2
						#end:case
						case guard2:
							temp0 = guard1
						#end:case
					#end:match
					localproc_0(temp0, 25, 0)
					(temp0
						setSpeed: 3
						ignoreHorizon: 1
						ignoreActors: 1
						setMotion: PolyPath local0 local1 self
					)
				#endif
			#end:case
			case 3:
				if (global2 moveOtherGuard:):
					0
				else:
					ticks = 1
				#endif
			#end:case
			case 4:
				if (global2 moveOtherGuard:):
					match client
						case guard1:
							temp0 = guard2
						#end:case
						case guard2:
							temp0 = guard1
						#end:case
					#end:match
					proc913_4(temp0, global0, self)
				else:
					(self cue:)
				#endif
			#end:case
			case 5:
				if register:
					(self dispose:)
				else:
					cycles = 1
				#endif
			#end:case
			case 6:
				(global103 fade:)
				(global2 newRoom: 820)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class guard1(GuardDog):
	#property vars (may be empty)
	view = 724
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		if ((global6 size:) == 3):
			checkCode = (kernel.ScriptID(81, 0) guard1Code:)
		#endif
	#end:method

	@classmethod
	def cue(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case argc:
				temp0 = okToCheck
				okToCheck = (>= 10 param1[0] 4)
				if (temp0 and (param1 > 10)):
					(global2 warnUser: 4 (regPathID currentRoom:))
				#endif
			#end:case
			case ((global6 size:) == 3):
				(kernel.ScriptID(81, 0) clrFlag: 709 1 loiterTimer: 36)
			#end:case
		)
	#end:method

#end:class or instance

@SCI.instance
class guard2(GuardDog):
	#property vars (may be empty)
	x = 99
	y = 181
	view = 726
	loop = 3
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		if ((global6 size:) == 3):
			checkCode = (kernel.ScriptID(81, 0) guard2Code:)
		#endif
	#end:method

	@classmethod
	def cue(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case argc:
				temp0 = okToCheck
				okToCheck = (>= 13 param1[0] 3)
				if 
					(and
						temp0
						(not okToCheck)
						((regPathID currentRoom:) == 840)
					)
					(global2 warnUser: 4 (regPathID currentRoom:))
				#endif
			#end:case
			case ((global6 size:) == 3):
				(kernel.ScriptID(81, 0)
					rFlag1: ((kernel.ScriptID(81, 0) rFlag1:) & 0xfffd)
					loiterTimer: 36
				)
			#end:case
		)
	#end:method

#end:class or instance

