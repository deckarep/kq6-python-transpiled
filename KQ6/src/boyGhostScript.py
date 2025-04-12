#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 822
import sci_sh
import kernel
import Main
import KQ6Print
import n913
import RandCycle
import PolyPath
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	boyGhostScript = 0,
	boyGhost = 1,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None
local4 = None


@SCI.procedure
def localproc_0():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	if (kernel.ScriptID(820, 4) cycler:):
		(kernel.ScriptID(820, 4) setCycle: 0 stopUpd:)
		(kernel.ScriptID(820, 5) setCycle: 0 stopUpd:)
	#endif
#end:procedure

@SCI.procedure
def localproc_1():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	if (not (kernel.ScriptID(820, 4) cycler:)):
		(kernel.ScriptID(820, 4) startUpd: setCycle: Fwd)
		(kernel.ScriptID(820, 5) startUpd: setCycle: RandCycle)
	#endif
#end:procedure

@SCI.instance
class boyGhostScript(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global1 handsOn:)
		(super dispose:)
		(boyGhost delete:)
		kernel.DisposeScript(822)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				kernel.Load(128, 763)
				cycles = 5
			#end:case
			case 1:
				(global1 handsOff:)
				(boyGhost
					view: 763
					setLoop: 0
					cel: 7
					x: 260
					y: 118
					cycleSpeed: 10
					show:
					setCycle: End self
				)
			#end:case
			case 2:
				(boyGhost setLoop: 1 cel: 7 posn: 258 117)
				(self setScript: cryBaby self)
			#end:case
			case 3:
				if (global0 has: 17):
					(global1 handsOn:)
				else:
					state = 5
					cycles = 1
				#endif
			#end:case
			case 4:
				(global1 handsOff:)
				(global91 say: 6 2 16 1 self)
			#end:case
			case 5:
				localproc_1()
				(cryBaby
					next: (showNonHanky register: 1 caller: self yourself:)
				)
			#end:case
			case 6:
				if (local0 or (global0 has: 17)):
					localproc_0()
					state = 7
					if local0:
						cycles = 3
					else:
						(global1 handsOn:)
					#endif
				else:
					(self setScript: noHanky self)
				#endif
			#end:case
			case 7:
				(global2 setScript: kernel.ScriptID(820, 1))
			#end:case
			case 8:
				(global1 handsOff:)
				(kernel.ScriptID(80, 0) setFlag: 709 -32768)
				(global91 say: 6 50 0 1 self)
			#end:case
			case 9:
				localproc_1()
				if (script == cryBaby):
					(cryBaby next: (showNonHanky caller: self yourself:))
				else:
					cycles = 1
				#endif
			#end:case
			case 10:
				(global0
					normal: 0
					setScale: 0
					view: 763
					setLoop: 7
					cel: 0
					setCycle: End self
				)
			#end:case
			case 11:
				(boyGhost setCycle: End self)
			#end:case
			case 12:
				(boyGhost setLoop: 3 cel: 0 posn: 229 70 setCycle: Fwd)
				seconds = 5
			#end:case
			case 13:
				localproc_0()
				cycles = 4
			#end:case
			case 14:
				(kernel.ScriptID(820, 2)
					add: -1 6 50 0 2
					add: -1 6 50 0 3
					add: -1 6 50 0 4
					init: self
				)
			#end:case
			case 15:
				localproc_1()
				(boyGhost setCycle: Beg self)
			#end:case
			case 16:
				(boyGhost setLoop: 4 cel: 0 posn: 155 88 setCycle: CT 10 1 self)
			#end:case
			case 17:
				(global0 reset: 0)
				(boyGhost setCycle: End self)
			#end:case
			case 18:
				(boyGhost setLoop: 5 cel: 0 posn: 229 88 setCycle: End self)
			#end:case
			case 19:
				(boyGhost hide:)
				seconds = 2
			#end:case
			case 20:
				(boyGhost
					setLoop: 6
					setPri: ((global0 priority:) - 1)
					cel: 0
					posn: 85 151
					show:
					setCycle: End self
				)
			#end:case
			case 21:
				(global91 say: 6 50 0 5 self)
			#end:case
			case 22:
				(global102 fadeTo: 824 -1)
				(boyGhost setCycle: 0 setMotion: 0 dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class showNonHanky(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				localproc_1()
				if (((boyGhost loop:) == 1) and (boyGhost cel:)):
					(boyGhost setCycle: Beg self)
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				(boyGhost setLoop: 2 cel: 0 posn: 241 96 setCycle: CT 4 1 self)
			#end:case
			case 2:
				if register:
					localproc_0()
					cycles = 4
				else:
					(self cue:)
				#endif
			#end:case
			case 3:
				if register:
					(kernel.ScriptID(820, 2)
						add: -1 6 2 16 2
						add: -1 6 2 16 3
						init: self
					)
				else:
					ticks = 1
				#endif
			#end:case
			case 4:
				if register:
					localproc_1()
				#endif
				if local0:
					(self dispose:)
				else:
					seconds = 3
				#endif
			#end:case
			case 5:
				(boyGhost setCycle: CT 0 -1 self)
			#end:case
			case 6:
				(boyGhost setLoop: 1 cel: 0 posn: 258 117)
				local1 = 0
				if (not register):
					(global1 handsOn:)
					(client setScript: cryBaby)
				else:
					register = 0
					(client setScript: cryBaby 0 1)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class cryBaby(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		local2 = 30
		(super init: &rest)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		local3 = kernel.GetTime(1)
		if ((not local1) and (local4 != local3) and (global11 == global13)):
			local4 = local3
			if (local2 < 30):
				local2.post('++')
			#endif
		#endif
		(super doit:)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not next):
			match state = param1
				case 0:
					(boyGhost view: 763 setLoop: 1 x: 258 y: 117)
					if (boyGhost cel:):
						(boyGhost setCycle: Beg self)
					else:
						cycles = 1
					#endif
				#end:case
				case 1:
					(cond
						case (register == -32768):
							(global91 say: 6 0 0 2 self oneOnly: 0)
						#end:case
						case register:
							(global91 say: 6 2 16 4 self)
						#end:case
						case (not local1):
							(global91 say: 1 0 4 0 self)
						#end:case
						else:
							ticks = 1
						#end:else
					)
					register = 0
				#end:case
				case 2:
					localproc_1()
					if ((not local1) and (local2 == 30)):
						local2 = 0
					#endif
					if caller:
						(caller cue:)
						caller = 0
					#endif
					(boyGhost setCycle: End self)
				#end:case
				case 3:
					(boyGhost setCycle: CT 2 -1 self)
				#end:case
				case 4:
					if ((not local1) and (local2 == 30)):
						state = -1
						cycles = 1
					else:
						state = 1
						cycles = kernel.Random(1, 15)
					#endif
				#end:case
			#end:match
		else:
			(self dispose:)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class noHanky(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(KQ6Print posn: -1 10 say: 0 1 0 5 1 init: self)
			#end:case
			case 1:
				(self setScript: justCryToMama self 2)
			#end:case
			case 2:
				localproc_0()
				cycles = 2
			#end:case
			case 3:
				(kernel.ScriptID(820, 2)
					add: -1 1 0 5 3 -1 10
					add: -1 1 0 5 4 -1 10
					init: self
				)
			#end:case
			case 4:
				localproc_1()
				(self setScript: justCryToMama self 5)
			#end:case
			case 5:
				proc913_4(global0, kernel.ScriptID(820, 3), self)
			#end:case
			case 6:
				localproc_0()
				cycles = 4
			#end:case
			case 7:
				(global91 say: 1 0 5 6 self)
			#end:case
			case 8:
				(global91 say: 1 0 5 7 self)
			#end:case
			case 9:
				localproc_1()
				(boyGhost setLoop: 0 cel: 7 x: 260 y: 118 setCycle: Beg self)
			#end:case
			case 10:
				if ((global0 x:) <= (kernel.ScriptID(820, 3) approachX:)):
					(global0
						setMotion:
							PolyPath
							(kernel.ScriptID(820, 3) approachX:)
							(kernel.ScriptID(820, 3) approachY:)
							self
					)
				else:
					state.post('++')
					cycles = 1
				#endif
			#end:case
			case 11:
				proc913_4(global0, kernel.ScriptID(820, 3), self)
			#end:case
			case 12:
				(global0 setPri: 9)
				(global105 number: 821 loop: 1 play:)
				(kernel.ScriptID(820, 3) setPri: 10 setCycle: End self)
			#end:case
			case 13:
				localproc_0()
				(kernel.ScriptID(820, 3) stopUpd:)
				cycles = 4
			#end:case
			case 14:
				(global91 say: 1 0 5 8 self)
			#end:case
			case 15:
				(global105 stop:)
				(kernel.ScriptID(820, 2)
					add: -1 1 0 5 9
					add: -1 1 0 5 10
					add: -1 1 0 5 11
					add: -1 1 0 5 12
					add: -1 1 0 5 13
					init: self
				)
			#end:case
			case 16:
				localproc_1()
				(kernel.ScriptID(820, 3) setCycle: Beg self)
				(global105 number: 822 loop: 1 play:)
			#end:case
			case 17:
				(global105 stop:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class justCryToMama(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(boyGhost view: 763 setLoop: 1 x: 258 y: 117)
				if (boyGhost cel:):
					(boyGhost setCycle: Beg self)
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				(KQ6Print posn: -1 10 say: 0 1 0 5 register init: self)
			#end:case
			case 2:
				(boyGhost setCycle: End self)
			#end:case
			case 3:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class boyGhost(Actor):
	#property vars (may be empty)
	x = 260
	y = 118
	noun = 6
	approachX = 98
	approachY = 149
	view = 763
	cycleSpeed = 8
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		(self hide: setScript: boyGhostScript approachVerbs: 50)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 2:
				if ((boyGhostScript state:) == 3):
					local1 = 1
					(boyGhostScript cue:)
				else:
					localproc_0()
					(global91 say: noun param1 17)
					localproc_1()
				#endif
			#end:case
			case 50:
				localproc_0()
				local0 = 1
				(global0 put: 17 820)
				(global1 givePoints: 3)
				local1 = 1
				if ((boyGhostScript state:) == 3):
					(boyGhostScript cue:)
				else:
					(boyGhostScript changeState: 8)
				#endif
			#end:case
			else:
				if ((global66 doit: param1) == -32768):
					localproc_0()
					(global91 say: noun 0 0 1)
					local1 = 1
					if ((script script:) != showNonHanky):
						((script script:) register: -32768 next: showNonHanky)
					#endif
				else:
					(super doVerb: param1)
				#endif
			#end:else
		#end:match
	#end:method

#end:class or instance

