#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 752
import sci_sh
import kernel
import Main
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	throwDazzle = 0,
	geniePoofIn = 1,
	geniePoofOut = 2,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = [9, 10, 11, -1, 11, 12, 13, 14]
local8 = [85, 85, 85, 85, 85, 85, 85, 88]
local16 = [1, 0, -1, 0, 1, 0, 1, 0]


@SCI.instance
class throwDazzle(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if (not global106):
					global106 = global0
				#endif
				if (global106 == global0):
					(global1 handsOff:)
				#endif
				kernel.Load(132, 708)
				kernel.Load(132, 707)
				cycles = 4
			#end:case
			case 1:
				(= temp2
					kernel.GetAngle((register x:), (register y:), (global106 x:), (global106
						y:
					), 60)
				)
				(register
					loop:
						(cond
							case (<= 338 temp2 23): 3#end:case
							case (<= 23 temp2 75): 6#end:case
							case (<= 75 temp2 105): 0#end:case
							case (<= 105 temp2 158): 4#end:case
							case (<= 158 temp2 203): 2#end:case
							case (<= 203 temp2 255): 5#end:case
							case (<= 255 temp2 285): 1#end:case
							else: 7#end:else
						)
				)
				kernel.UnLoad(128, (register view:))
				temp0 = (kernel.NumCels(register) - 1)
				(register cel: temp0)
				kernel.SetNowSeen(register)
				if ((register loop:) != 3):
					(projectile
						priority: (register priority:)
						y:
							(-
								(register nsBottom:)
								(/
									(*
										local8[(register loop:)]
										(-
											(register nsBottom:)
											(register nsTop:)
										)
									)
									100
								)
							)
						setLoop: local0[(register loop:)]
					)
					(projectile
						x:
							if (local16[(register loop:)] >= 0):
								if local16[(register loop:)]:
									(register nsRight:)
								else:
									(register nsLeft:)
								#endif
							else:
								(register x:)
							#endif
					)
				#endif
				(register cel: 0 setCycle: End self)
				if ((global103 number:) != 707):
					(global103 number: 0 stop:)
					(global103 number: 707 setLoop: 1 play:)
				#endif
			#end:case
			case 2:
				(global106 setMotion: 0 stopUpd:)
				(global103 number: 0 stop:)
				(global103 number: 708 setLoop: 1 play:)
				if ((register loop:) != 3):
					(= temp1
						(-
							(global106 y:)
							((75 * ((global106 y:) - (global106 nsTop:))) / 100)
						)
					)
					temp0 = (global106 x:)
					(projectile
						init:
						setCycle: Fwd
						setMotion: MoveTo temp0 temp1 self
					)
				else:
					cycles = 1
				#endif
			#end:case
			case 3:
				if ((register loop:) != 3):
					(global103 number: 0 stop:)
					(global103 number: 709 setLoop: 1 play:)
					(projectile loop: 15 cel: 0 setCycle: End self)
				else:
					cycles = 1
				#endif
			#end:case
			case 4:
				if (global106 == global0):
					(global103 number: 0 stop:)
					(global102 number: 705 setLoop: 1 play:)
				#endif
				(projectile dispose:)
				(cond
					case kernel.IsObject(global156):
						(self setScript: global156 self)
						global156 = 0
					#end:case
					case (global106 == global0):
						(global102 client: self)
						(self setScript: getEgo 0 caller)
					#end:case
					else:
						cycles = 1
					#end:else
				)
			#end:case
			case 5:
				(register setCycle: Beg self)
			#end:case
			case 6:
				cycles = 3
			#end:case
			case 7:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getEgo(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global0
					view: 749
					normal: 0
					cel: 0
					loop: (mod (global0 cel:) 4)
					cycleSpeed: 8
					setCycle: CT 2 1 self
				)
			#end:case
			case 1:
				(global0
					loop:
						match (global0 loop:)
							case 0: 3#end:case
							case 1: 2#end:case
							case 2: 1#end:case
							case 3: 0#end:case
						#end:match
				)
				(global0 setCycle: End self)
			#end:case
			case 2:
				if ((global0 loop:) > 2):
					(global0
						loop: (4 + ((global0 loop:) == 3))
						cycleSpeed: 10
						setCycle: End self
					)
				else:
					cycles = 1
				#endif
			#end:case
			case 3:
				if register:
					(self dispose:)
				else:
					proc0_1(18)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class geniePoofIn(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				kernel.Load(132, 943)
				cycles = 2
			#end:case
			case 1:
				(global103 number: 0 stop:)
				(global103 number: 943 setLoop: 1 play:)
				(smoke
					scaleSignal: 1
					scaleX: (register scaleX:)
					scaleY: (register scaleY:)
					priority: (register priority:)
					posn: (register x:) ((register y:) + 1) 1
					init:
					cycleSpeed: 8
					setCycle: CT 2 1 self
				)
			#end:case
			case 2:
				(register init: show:)
				(smoke cycleSpeed: 10 setCycle: End self)
			#end:case
			case 3:
				(smoke dispose:)
				cycles = 2
			#end:case
			case 4:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class geniePoofOut(Script):
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
				(global103 number: 0 stop:)
				(global103 number: 943 setLoop: 1 play:)
				(smoke
					scaleSignal: 1
					scaleX: (register scaleX:)
					scaleY: (register scaleY:)
					priority: (register priority:)
					posn: (register x:) ((register y:) + 1) 1
					init:
					setCycle: CT 2 1 self
				)
			#end:case
			case 2:
				(register hide:)
				(smoke setCycle: End self)
			#end:case
			case 3:
				(smoke dispose:)
				cycles = 2
			#end:case
			case 4:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class smoke(Prop):
	#property vars (may be empty)
	view = 7501
	signal = 16400
	cycleSpeed = 8
	
#end:class or instance

@SCI.instance
class projectile(Actor):
	#property vars (may be empty)
	yStep = 7
	loop = 9
	signal = 24592
	cycleSpeed = 3
	xStep = 7
	moveSpeed = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (global11 == 740):
			view = 7021
		else:
			view = 702
		#endif
		(super init: &rest)
	#end:method

#end:class or instance

