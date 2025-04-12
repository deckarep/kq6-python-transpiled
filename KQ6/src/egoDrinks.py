#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 87
import sci_sh
import kernel
import Main
import n913
import LoadMany
import Sound
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	egoDrinks = 0,
	drinkMeScript = 1,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None
local4 = None
local5 = None
local6 = None
local7 = None


@SCI.instance
class egoDrinks(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff: killSound: 1)
				(global69 disable:)
				(global91 say: 1 14 0 1 self 0)
			#end:case
			case 1:
				(global0
					cycleSpeed: 10
					view: 935
					setPri: 14
					cel: 0
					setLoop: 0
					setCycle: End self
				)
				(localMusic number: 925 play: loop: 1)
			#end:case
			case 2:
				seconds = 2
			#end:case
			case 3:
				(global0 setCycle: Beg self)
			#end:case
			case 4:
				cycles = 15
			#end:case
			case 5:
				(global91 say: 1 14 0 2 self 0)
			#end:case
			case 6:
				(client setScript: kernel.ScriptID(87, 1))
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class drinkMeScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				local0 = global5
				local1 = global32
				local2 = global10
				local3 = global73
				local4 = global72
				local5 = global74
				local6 = global93
				local7 = (global2 obstacles:)
				(global2 obstacles: ((List new:) add: yourself:))
				(global5 = (EventHandler new:) name: r"""newCast""" add:)
				(global32 = (EventHandler new:)
					name: r"""newFeatures"""
					add: self
				)
				(global10 = (EventHandler new:) name: r"""newATPs""" add:)
				(global73 = (EventHandler new:) name: r"""newMH""" add: self)
				(global72 = (EventHandler new:) name: r"""newKH""" add: self)
				(global74 = (EventHandler new:) name: r"""newDH""" add: self)
				(global93 = (EventHandler new:) name: r"""newWH""" add:)
				kernel.DrawPic(981, 9)
				cycles = 2
			#end:case
			case 1:
				(global91 say: 1 14 0 3 self 0)
			#end:case
			case 2:
				(localMusic number: 926 play: self)
				(newEgo
					init:
					posn: 147 118
					setLoop: 1
					cel: 0
					setPri: 14
					cycleSpeed: 12
					setCycle: End self
				)
			#end:case
			case 3:
				kernel.Palette(1, 981)
			#end:case
			case 4:
				kernel.Palette(1, 97)
				if ((localMusic prevSignal:) == -1):
					cycles = 1
				#endif
			#end:case
			case 5:
				if ((localMusic prevSignal:) == 10):
					(state -= 3)
				#endif
				cycles = 1
			#end:case
			case 6:
				kernel.Palette(1, 981)
				cycles = 1
			#end:case
			case 7:
				seconds = 4
			#end:case
			case 8:
				(global91 say: 1 14 0 4 self 0)
			#end:case
			case 9:
				seconds = 5
			#end:case
			case 10:
				(global91 say: 1 14 0 5 self 0)
			#end:case
			case 11:
				(localMusic number: 927 play: self)
			#end:case
			case 12:
				(global91 say: 1 14 0 6 self 0)
			#end:case
			case 13:
				(newEgo cel: 0 setLoop: 2 setCycle: End self)
			#end:case
			case 14:
				(newEgo cel: 0 setLoop: 3 setCycle: End self)
			#end:case
			case 15:
				(global5
					eachElementDo: #dispose
					eachElementDo: #delete
					release:
					dispose:
				)
				(global10 dispose:)
				(global32 delete: self dispose:)
				(global73 delete: self dispose:)
				(global72 delete: self dispose:)
				(global74 delete: self dispose:)
				(global93 delete: self dispose:)
				((global2 obstacles:) dispose:)
				(global2 obstacles: local7)
				global5 = local0
				global32 = local1
				global73 = local3
				global72 = local4
				global74 = local5
				global93 = local6
				global10 = local2
				kernel.DrawPic((global2 picture:), 9)
				(global0 reset: 2)
				cycles = 3
			#end:case
			case 16:
				cycles = 3
			#end:case
			case 17:
				(global91 say: 1 14 0 7 self 0)
			#end:case
			case 18:
				(global91 say: 1 14 0 8 self 0)
			#end:case
			case 19:
				(global69 enable:)
				(global1 handsOn: killSound: 0)
				proc913_1(153)
				(localMusic stop: dispose:)
				(self dispose:)
				proc958_0(0, 87)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class localMusic(Sound):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class newEgo(Prop):
	#property vars (may be empty)
	view = 935
	
#end:class or instance

