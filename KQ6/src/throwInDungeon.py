#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 821
import sci_sh
import kernel
import Main
import n913
import DPath
import Jump
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	throwInDungeon = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.instance
class throwInDungeon(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super dispose:)
		kernel.DisposeScript(821)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(kernel.ScriptID(80, 0) dungeonEntered: 3)
				(global0
					normal: 0
					view: 825
					setLoop: 0
					cel: 0
					posn: 100 144
					setPri: 9
					setCycle: 0
					cycleSpeed: 8
					moveSpeed: 0
					setScale:
					scaleX: 121
					scaleY: 121
					setMotion: JumpTo 150 154 self
				)
			#end:case
			case 1:
				(global0 setCycle: End self)
			#end:case
			case 2:
				(global105 number: 960 setLoop: 1 play: self)
			#end:case
			case 3:
				if (not (kernel.ScriptID(80, 0) tstFlag: 711 64)):
					(global91 say: 1 0 8 0 self)
				else:
					cycles = 1
				#endif
			#end:case
			case 4:
				if (not (kernel.ScriptID(80, 0) tstFlag: 711 64)):
					(global105 number: 902 loop: 1 play:)
					(kernel.ScriptID(820, 3) setCycle: Beg self)
				else:
					(state += 2)
					cycles = 1
				#endif
			#end:case
			case 5:
				(global105 number: 822 loop: 1 play: self)
			#end:case
			case 6:
				cycles = 1
			#end:case
			case 7:
				local0 = 0
				(cond
					case (kernel.ScriptID(80, 0) tstFlag: 709 128):
						state = 9
						(self setScript: beautyEntrance self)
					#end:case
					case (kernel.ScriptID(80, 0) tstFlag: 709 4096):
						(kernel.ScriptID(80, 0) clrFlag: 709 4096)
						(self setScript: searchEgo self)
					#end:case
					case (kernel.ScriptID(80, 0) tstFlag: 711 32):
						(kernel.ScriptID(80, 0) clrFlag: 711 32)
						local0 = (global0 has: 44)
						(kernel.ScriptID(820, 3) setPri: -1 stopUpd:)
						(self setScript: afterClownHelpedEgoEscape self)
					#end:case
					case 
						(and
							proc913_0(10)
							(not (kernel.ScriptID(80, 0) tstFlag: 709 16384))
						):
						(kernel.ScriptID(80, 0) setFlag: 709 16384 1)
						(kernel.ScriptID(80, 0) setFlag: 711 32)
						(self register: jolloHelpsEgo setScript: jolloHelpsEgo)
					#end:case
					case (global0 has: 44):
						local0 = 1
						cycles = 1
					#end:case
					else:
						cycles = 1
					#end:else
				)
			#end:case
			case 8:
				(kernel.ScriptID(80, 0) setFlag: 711 64)
				if (not register):
					register = self
				#endif
				(global0 loop: 1 cel: 0 setCycle: End self)
			#end:case
			case 9:
				if local0:
					state = 11
				#endif
				(global0 reset: 7 posn: 132 149)
				if (register != self):
					(register cycles: 1)
				else:
					cycles = 1
				#endif
			#end:case
			case 10:
				cycles = 3
			#end:case
			case 11:
				(global2 setScript: kernel.ScriptID(820, 1))
			#end:case
			case 12:
				(global1 handsOn:)
				(kernel.ScriptID(820, 3) setPri: -1 stopUpd:)
				(global0 reset: 1)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class searchEgo(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global0 put: 44 820)
				(global91 say: 1 0 13 0 self)
			#end:case
			case 1:
				(kernel.ScriptID(820, 3) setCycle: Beg self)
			#end:case
			case 2:
				(global105 number: 822 loop: 1 play:)
				(kernel.ScriptID(820, 3) setPri: -1 stopUpd:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class beautyEntrance(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global91 say: 1 0 1 2 self)
			#end:case
			case 1:
				(global0 loop: 1 cel: 0 setCycle: End self)
			#end:case
			case 2:
				(global0 reset: 7 posn: 132 149)
				cycles = 4
			#end:case
			case 3:
				(global91 say: 1 0 1 3 self oneOnly: 0)
			#end:case
			case 4:
				cycles = 4
			#end:case
			case 5:
				(kernel.ScriptID(820, 3) setPri: -1 stopUpd:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class afterClownHelpedEgoEscape(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global91 say: 1 0 11 0 self)
			#end:case
			case 1:
				(kernel.ScriptID(820, 3) setCycle: Beg self)
			#end:case
			case 2:
				(global105 number: 822 loop: 1 play:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class jolloHelpsEgo(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global91 say: 1 0 9 1 self)
			#end:case
			case 1:
				(client cue:)
			#end:case
			case 2:
				seconds = 5
			#end:case
			case 3:
				(global105 number: 821 loop: 1 play: self)
			#end:case
			case 4:
				(global105 number: 821 loop: 1 play:)
				(kernel.ScriptID(820, 3) setCycle: End self)
			#end:case
			case 5:
				(global105 stop:)
				(jollo
					ignoreActors:
					init:
					cel: 0
					cycleSpeed: 8
					setLoop: 0
					setCycle: End self
				)
			#end:case
			case 6:
				(jollo posn: 87 148 setLoop: 1 cel: 0 setCycle: End self)
			#end:case
			case 7:
				(global91 say: 1 0 9 2 self)
			#end:case
			case 8:
				proc913_4(global0, jollo, self)
			#end:case
			case 9:
				cycles = 5
			#end:case
			case 10:
				(global91 say: 1 0 9 3 self oneOnly: 0)
			#end:case
			case 11:
				(jollo
					posn: 100 150
					setLoop: 2
					cel: 0
					cycleSpeed: 12
					setCycle: End self
				)
			#end:case
			case 12:
				(global0 reset: 1 setPri: 1 setMotion: DPath 93 142 34 142 self)
			#end:case
			case 13:
				(jollo setCycle: 0)
				(global2 newRoom: 710)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class jollo(Prop):
	#property vars (may be empty)
	x = 89
	y = 147
	view = 822
	priority = 9
	signal = 16
	
#end:class or instance

