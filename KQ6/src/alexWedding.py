#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 743
import sci_sh
import Main
import rm740
import n913
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	alexWedding = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.instance
class alexWedding(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global69 disable: 6)
				register = ((MemoryInfo 4) >> 0x0006)
				local0 = (((global9 at: 25) owner:) == global11)
				ticks = 30
			#end:case
			case 1:
				(global91 say: 1 0 16 1 self 743)
			#end:case
			case 2:
				ticks = 60
			#end:case
			case 3:
				(global91 say: 1 0 16 2 self 743)
			#end:case
			case 4:
				(global5 eachElementDo: #dispose)
				(global69
					enable:
					disable: 0 1 2 3 4 5 6
					height: -100
					activateHeight: -100
				)
				(Cursor showCursor: 0)
				(global2 drawPic: 165 10)
				cycles = 3
			#end:case
			case 5:
				(global91 say: 1 0 7 0 self 165)
			#end:case
			case 6:
				(cond
					case (proc999_5 ((global9 at: 39) owner:) 140 210):
						state = 10
						(global91 say: 1 0 3 0 self 165)
					#end:case
					case (global0 has: 39):
						state = 10
						(global91 say: 1 0 4 0 self 165)
					#end:case
					else:
						(global91 say: 1 0 2 1 self 165)
					#end:else
				)
			#end:case
			case 7:
				(extraProp
					view: 165
					init:
					setLoop: 4
					cel: 0
					cycleSpeed: 4
					posn: 167 62
					setCycle: End self
				)
			#end:case
			case 8:
				cycles = 5
			#end:case
			case 9:
				((ScriptID 740 7) add: 165 1 0 2 2 add: 165 1 0 2 3 init: self)
			#end:case
			case 10:
				state = 12
				(global91 say: 1 0 2 4 self 165)
			#end:case
			case 11:
				(global2 drawPic: 166 10)
				(extraProp
					view: 166
					init:
					setLoop: 0
					cel: 0
					cycleSpeed: 12
					posn: 82 127
				)
				seconds = 3
			#end:case
			case 12:
				(extraProp setCycle: End self)
			#end:case
			case 13:
				(extraProp dispose:)
				(proc740_10)
				cycles = 3
			#end:case
			case 14:
				(global69 height: 0 activateHeight: 0)
				(Cursor showCursor: 1)
				(global69 enable:)
				cycles = 2
			#end:case
			case 15:
				(UnLoad 128 7411)
				if (not (proc913_0 15)):
					state = 18
					ticks = 30
				else:
					(global91 say: 1 0 13 1 self 743)
				#endif
			#end:case
			case 16:
				((ScriptID 740 11)
					setLoop: 0
					cel: 0
					posn: 135 144
					cycleSpeed: 8
					setCycle: End
				)
				((ScriptID 740 1) setLoop: 2 cel: 0 cycleSpeed: 8 setCycle: End)
				seconds = 3
			#end:case
			case 17:
				(global91 say: 1 0 13 2 self 743)
			#end:case
			case 18:
				state = 24
				((ScriptID 740 11) cel: 0)
				ticks = 60
			#end:case
			case 19:
				((ScriptID 740 11) setLoop: 2 cel: 0 posn: 128 147 stopUpd:)
				cycles = 2
			#end:case
			case 20:
				(global91 say: 1 0 14 1 self 743)
			#end:case
			case 21:
				((ScriptID 740 4)
					view: 7465
					posn: (global164 + 32) (global165 - 4)
					setCel: 255
					setLoop: 0
					scaleSignal: 1
					scaleX: 117
					scaleY: 117
					setCycle: Beg self
				)
			#end:case
			case 22:
				((ScriptID 740 7)
					add: 743 1 0 14 2
					add: 743 1 0 14 3
					init: self
				)
			#end:case
			case 23:
				((ScriptID 740 4) setCycle: End self)
			#end:case
			case 24:
				((ScriptID 740 4)
					view: 746
					setLoop: 0
					cel: 0
					posn: global164 global165
					scaleSignal: 1
					scaleX: 115
					scaleY: 115
					stopUpd:
				)
				ticks = 30
			#end:case
			case 25:
				if local0:
					(global91 say: 1 0 12 1 self 743)
				else:
					state = 28
					((ScriptID 740 1) setLoop: 0 cel: 0 cycleSpeed: 8)
					ticks = 30
				#endif
			#end:case
			case 26:
				((ScriptID 740 12) setLoop: 2 cel: 0 setCycle: End self)
			#end:case
			case 27:
				(global91 say: 1 0 12 2 self 743)
			#end:case
			case 28:
				state++
				((ScriptID 740 12) setCycle: Beg self)
			#end:case
			case 29:
				((ScriptID 740 7)
					add: 743 1 0 11 1
					add: 743 1 0 11 2
					add: 743 1 0 11 3
					init: self
				)
			#end:case
			case 30:
				(global91 say: 1 0 15 1 self 743)
			#end:case
			case 31:
				((ScriptID 740 1)
					setLoop: 1
					cel: 0
					cycleSpeed: 8
					setCycle: End self
				)
				if local0:
					((ScriptID 740 12)
						setLoop: 3
						cel: 0
						setCycle: End (ScriptID 740 12)
					)
				#endif
				if (proc913_0 15):
					((ScriptID 740 11) setLoop: 2 cel: 0 setCycle: Fwd)
				#endif
				(global102
					number: (1744 if global169 else 744)
					setLoop: -1
					play:
				)
			#end:case
			case 32:
				(global91 say: 1 0 15 2 self 743)
			#end:case
			case 33:
				(cond
					case (not (proc913_0 10)):
						((ScriptID 740 4)
							view: 746
							setLoop: 0
							cel: 0
							setCycle: End self
						)
					#end:case
					case ((not (proc913_0 15)) and (not local0)):
						((ScriptID 740 4)
							view: 7461
							setLoop: 0
							cel: 0
							setCycle: End self
						)
					#end:case
					else:
						((ScriptID 740 4)
							view: 7463
							setLoop: 0
							cel: 0
							scaleSignal: 1
							scaleX: 115
							scaleY: 115
							setCycle: End self
						)
					#end:else
				)
				((ScriptID 740 21) setCycle: End (ScriptID 740 21))
				((ScriptID 740 22) setCycle: End (ScriptID 740 22))
				((ScriptID 740 11) cel: 0 stopUpd:)
			#end:case
			case 34:
				if (proc913_0 10):
					((ScriptID 740 4)
						view: 746
						setLoop: 0
						cel: 0
						setCycle: 0
						scaleSignal: 1
						scaleX: 115
						scaleY: 115
					)
				#endif
				seconds = 3
			#end:case
			case 35:
				((ScriptID 740 1) setCycle: Beg self)
			#end:case
			case 36:
				if (not (proc913_0 15)):
					((ScriptID 740 1) setLoop: 0 cel: 0)
				else:
					((ScriptID 740 1) setLoop: 2 setCycle: End)
				#endif
				((ScriptID 740 21) cue: 99)
				((ScriptID 740 22) cue: 99)
				seconds = 3
			#end:case
			case 37:
				if (proc913_0 15):
					((ScriptID 740 7)
						add: 743 1 0 6 1
						add: 743 1 0 6 2
						add: 743 1 0 6 3
						add: 743 1 0 6 4
						add: 743 1 0 6 5
						add: 743 1 0 6 6
					)
				else:
					((ScriptID 740 7)
						add: 743 1 0 7 1
						add: 743 1 0 7 2
						add: 743 1 0 7 3
						add: 743 1 0 7 4
						add: 743 1 0 7 5
						add: 743 1 0 7 6
					)
				#endif
				((ScriptID 740 7) init: self)
			#end:case
			case 38:
				((ScriptID 740 7) add: 743 1 0 8 1 add: 743 1 0 8 3 init: self)
			#end:case
			case 39:
				if local0:
					(self setScript: hugStuff self)
				else:
					((ScriptID 740 7)
						add: 743 1 0 10 1
						add: 743 1 0 10 2
						add: 743 1 0 10 3
						add: 743 1 0 10 4
						init: self
					)
				#endif
			#end:case
			case 40:
				if (proc913_0 15):
					((ScriptID 740 7) add: 743 1 0 2 1 add: 743 1 0 2 2)
				else:
					((ScriptID 740 7) add: 743 1 0 1 1 add: 743 1 0 1 2)
				#endif
				((ScriptID 740 7) init: self)
			#end:case
			case 41:
				if local0:
					(Portrait 2 r"""CASSIMA""")
					((ScriptID 740 7)
						add: 743 1 0 19 1
						add: 743 1 0 19 2
						add: 743 1 0 19 3
						init: self
					)
					(Portrait 2 r"""VALANICE""")
				else:
					cycles = 2
				#endif
			#end:case
			case 42:
				if (((ScriptID 740 1) loop:) == 2):
					((ScriptID 740 1) setCycle: Beg self)
				else:
					cycles = 2
				#endif
			#end:case
			case 43:
				((ScriptID 740 1) setLoop: 0 cel: 0)
				ticks = 30
			#end:case
			case 44:
				if local0:
					(global91 say: 1 0 5 1 self 743)
				else:
					(global91 say: 1 0 4 1 self 743)
				#endif
			#end:case
			case 45:
				if ((ScriptID 80 0) tstFlag: 710 16):
					(Portrait 2 r"""JOLLO""")
					(Portrait 2 r"""VALANICE""")
					(Portrait 0 r"""CASSIMA""")
					(Portrait 0 r"""SALADIN""")
					((ScriptID 740 7)
						add: 743 1 0 17 1
						add: 743 1 0 17 2
						init: self
					)
				else:
					((ScriptID 740 7)
						add: 743 1 0 18 1
						add: 743 1 0 18 2
						init: self
					)
				#endif
			#end:case
			case 46:
				(global91 say: 1 0 3 1 self 743)
			#end:case
			case 47:
				((ScriptID 740 1) setLoop: 2 cel: 0 setCycle: End self)
			#end:case
			case 48:
				(global89 keepWindow: 1 modeless: 0)
				(global91 say: 1 0 3 2 self 743)
			#end:case
			case 49:
				(DisposeScript 1001)
				(DisposeScript 1005)
				(DisposeScript 1026)
				(DisposeScript 1004)
				if (local0 and ((ScriptID 80 0) tstFlag: 710 16)):
					((ScriptID 740 16) setCycle: Fwd)
					((ScriptID 740 17) setCycle: Fwd)
					((ScriptID 740 19) view: 7472 setLoop: 1 setCycle: Fwd)
					((ScriptID 740 18) view: 7472 setLoop: 0 setCycle: Fwd)
					((ScriptID 740 20) view: 7472 setLoop: 2 setCycle: Fwd)
					(clap1 init: setCycle: Fwd)
					(clap2 init: setCycle: Fwd)
					((ScriptID 740 14)
						view: 7471
						setLoop: 2
						cel: 0
						posn: 236 189
						setPri: 15
						setCycle: End (ScriptID 740 14)
					)
					((ScriptID 740 15)
						view: 7471
						setLoop: 3
						cel: 0
						posn: 248 186
						setPri: 14
						setCycle: End (ScriptID 740 15)
					)
				#endif
				(cond
					case (not (proc913_0 10)):
						((ScriptID 740 4)
							view: 746
							setLoop: 0
							cel: 0
							setCycle: End
						)
					#end:case
					case (not (proc913_0 15)):
						((ScriptID 740 4) setScript: clap 0 0)
					#end:case
					case (not (global5 contains: (ScriptID 740 3))):
						((ScriptID 740 4) setScript: clap 0 1)
					#end:case
					else:
						((ScriptID 740 4)
							view: 7460
							setLoop: 0
							scaleSignal: 1
							scaleX: 115
							scaleY: 115
							setCycle: Fwd
						)
					#end:else
				)
				if (proc913_0 15):
					((ScriptID 740 11)
						setLoop: 2
						setCycle: End (ScriptID 740 11)
					)
				#endif
				((ScriptID 740 21) setCycle: End (ScriptID 740 21))
				((ScriptID 740 22) setCycle: End (ScriptID 740 22))
				if (((global9 at: 25) owner:) == 740):
					(self setScript: (ScriptID 752 2) self (ScriptID 740 3))
				else:
					state = 51
					cycles = 2
				#endif
			#end:case
			case 50:
				((ScriptID 740 3) posn: 195 152)
				(self setScript: (ScriptID 752 1) self (ScriptID 740 3))
			#end:case
			case 51:
				((ScriptID 740 3) view: 7481 setLoop: 0 cel: 0)
				ticks = 30
			#end:case
			case 52:
				(global89 keepWindow: 1 modeless: 0)
				((ScriptID 740 7)
					add: 743 1 0 3 3
					add: 743 1 0 3 4
					add: 743 1 0 3 5
					init: self
				)
			#end:case
			case 53:
				if (((global9 at: 25) owner:) == 740):
					cycles = 2
				else:
					((ScriptID 740 1) setLoop: 1 cel: 0 setCycle: End)
				#endif
				(global102 number: 747 setLoop: 1 play: global2)
			#end:case
			case 54:
				((ScriptID 740 3) cycleSpeed: 10 setCycle: End self)
			#end:case
			case 55:
				((ScriptID 740 1)
					view: 7481
					setLoop: 1
					cel: 0
					cycleSpeed: 8
					setCycle: End self
				)
				((ScriptID 740 3) cel: 0)
			#end:case
			case 56:
				((ScriptID 740 3) setCycle: End self)
			#end:case
			case 57:
				((ScriptID 740 1) setLoop: 2 cel: 0 setCycle: End)
				((ScriptID 740 3) view: 7020 setLoop: 0 cel: 0 stopUpd:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class hugStuff(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				if (((ScriptID 740 1) loop:) != 2):
					((ScriptID 740 1) setLoop: 2 cel: 0 setCycle: End self)
				else:
					cycles = 2
				#endif
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				(global91 say: 1 0 9 1 self 743)
			#end:case
			case 3:
				((ScriptID 740 12)
					view: 7451
					setLoop: 0
					cel: 0
					setCycle: End self
				)
			#end:case
			case 4:
				(global91 say: 1 0 9 2 self 743)
			#end:case
			case 5:
				((ScriptID 740 1) hide:)
				((ScriptID 740 12)
					setLoop: 1
					cel: 0
					posn: 221 145
					setCycle: End self
				)
			#end:case
			case 6:
				(global91 say: 1 0 9 3 self 743)
			#end:case
			case 7:
				((ScriptID 740 12) setLoop: 2 cel: 0 setCycle: End self)
			#end:case
			case 8:
				(Portrait 2 r"""CASSIMA""")
				(global91 say: 1 0 9 4 self 743)
				(Portrait 2 r"""VALANICE""")
			#end:case
			case 9:
				((ScriptID 740 1) show:)
				((ScriptID 740 12)
					setLoop: 0
					setCel: 255
					posn: 216 144
					cycleSpeed: 10
					setCycle: Beg self
				)
			#end:case
			case 10:
				(global91 say: 1 0 9 5 self 743)
			#end:case
			case 11:
				((ScriptID 740 12) addToPic:)
				(DisposeScript 1065)
				(DisposeScript 1066)
				cycles = 2
			#end:case
			case 12:
				((ScriptID 740 1) setPri: 8)
				((ScriptID 740 13)
					view: 7452
					setPri: 9
					setLoop: 0
					cel: 0
					posn: 228 145
					cycleSpeed: 12
					setCycle: End self
				)
			#end:case
			case 13:
				((ScriptID 740 1) hide:)
				((ScriptID 740 13)
					setLoop: 1
					cel: 0
					posn: 178 139
					setCycle: End self
				)
			#end:case
			case 14:
				(global91 say: 1 0 9 6 self 743)
			#end:case
			case 15:
				(global91 say: 1 0 9 7 self 743)
			#end:case
			case 16:
				((ScriptID 740 1) show: setPri: -1)
				((ScriptID 740 13)
					setLoop: 2
					cel: 0
					posn: 227 146
					setCycle: End self
				)
			#end:case
			case 17:
				((ScriptID 740 13)
					view: 745
					setLoop: 4
					cel: 2
					posn: 235 145
					signal: 26624
				)
				ticks = 30
			#end:case
			case 18:
				((ScriptID 740 13) addToPic:)
				(DisposeScript 1067)
				cycles = 2
			#end:case
			case 19:
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class extraProp(Prop):
	#property vars (may be empty)
	view = 165
	loop = 4
	signal = 26624
	detailLevel = 2
	
#end:class or instance

@SCI.instance
class clap1(Prop):
	#property vars (may be empty)
	x = 30
	y = 145
	view = 7471
	loop = 5
	priority = 15
	signal = 18448
	cycleSpeed = 4
	detailLevel = 2
	
#end:class or instance

@SCI.instance
class clap2(Prop):
	#property vars (may be empty)
	x = 54
	y = 141
	view = 7471
	loop = 6
	priority = 15
	signal = 18448
	cycleSpeed = 4
	detailLevel = 2
	
#end:class or instance

@SCI.instance
class clap(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				((ScriptID 740 4)
					view: 7462
					setLoop: 0
					cel: 0
					scaleSignal: 1
					scaleX: 105
					scaleY: 105
					setCycle: End self
				)
			#end:case
			case 1:
				((ScriptID 740 4) setLoop: 1 setCycle: Fwd)
				if register:
					seconds = 3
				#endif
			#end:case
			case 2:
				((ScriptID 740 4) setLoop: 0 setCel: 255 setCycle: Beg self)
			#end:case
			case 3:
				((ScriptID 740 4)
					view: 7463
					cel: 0
					setLoop: 0
					setScale: 0
					setCycle: End self
				)
			#end:case
			case 4:
				(self init:)
			#end:case
		#end:match
	#end:method

#end:class or instance

