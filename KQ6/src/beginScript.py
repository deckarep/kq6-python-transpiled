#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 90
import sci_sh
import kernel
import Main
import Kq6Talker
import n913
import Feature
import Motion
import User
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	beginScript = 0,
	riddleBookScript = 1,
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
local8 = None
local9 = None


@SCI.instance
class beginScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global69 disable: 6)
				if (not proc913_0(129)):
					proc913_1(129)
					(global1 givePoints: 1)
				#endif
				(global91 say: 1 27 0 1 self 0)
			#end:case
			case 1:
				seconds = 2
			#end:case
			case 2:
				(global0
					normal: 0
					view: 903
					cel: 0
					setLoop: 2
					cycleSpeed: 5
					setCycle: End self
				)
			#end:case
			case 3:
				(global0 cel: 0 setLoop: 0 setCycle: End self)
			#end:case
			case 4:
				(global0 setLoop: 1 setCycle: Fwd)
				seconds = 4
			#end:case
			case 5:
				(client setScript: kernel.ScriptID(90, 1))
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class riddleBookScript(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		local9 = global91
		global91 = rBookMessager
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
		(global32 = (EventHandler new:) name: r"""newFeatures""" add: self)
		(global10 = (EventHandler new:) name: r"""newATPs""" add:)
		(global73 = (EventHandler new:) name: r"""newMH""" add: self)
		(global72 = (EventHandler new:) name: r"""newKH""" add: self)
		(global74 = (EventHandler new:) name: r"""newDH""" add: self)
		(global93 = (EventHandler new:) name: r"""newWH""" add:)
		if register:
			(global9 hide:)
			register = 0
		#endif
		kernel.DrawPic(98)
		(super init: &rest)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(background init:)
				(bookView init: stopUpd:)
				seconds = 2
			#end:case
			case 1:
				(global91 say: 1 27 0 2 self 0)
			#end:case
			case 2:
				(global91 say: 1 27 0 3 self 0)
			#end:case
			case 3:
				(global1 handsOn:)
				(global32 delete: self)
				(User controls: 0)
				(global69 disable: 0 3 4 5)
			#end:case
			case 4:
				(global1 handsOff:)
				if global25:
					(global25 dispose:)
				#endif
				(global1 setCursor: global21)
				(global5
					eachElementDo: #dispose
					eachElementDo: #delete
					release:
					dispose:
				)
				(global10 dispose:)
				(global32 delete: background self dispose:)
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
				kernel.UnLoad(128, 904)
				kernel.DrawPic((global2 picture:), 100)
				if global10:
					(global10 doit:)
				#endif
				seconds = 2
			#end:case
			case 5:
				(global0 setLoop: 2 cycleSpeed: 10 lastCel: setCycle: Beg self)
			#end:case
			case 6:
				(global0 reset: 2)
				(global69 enable: 6)
				(global1 handsOn:)
				(self dispose:)
				global91 = local9
				kernel.DisposeScript(90)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class background(Feature):
	#property vars (may be empty)
	nsBottom = 200
	nsRight = 320
	
	@classmethod
	def doVerb():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(riddleBookScript cue:)
	#end:method

#end:class or instance

@SCI.instance
class bookView(Prop):
	#property vars (may be empty)
	x = 149
	y = 86
	view = 904
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 1):
			(riddleBookScript state: ((riddleBookScript state:) - 3) cue:)
		else:
			(background doVerb: param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class rBookMessager(Kq6Messager):
	#property vars (may be empty)
	@classmethod
	def findTalker(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 99):
			temp0 = localNarrator
			return
		else:
			(super findTalker: param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class localNarrator(Kq6Narrator):
	#property vars (may be empty)
	y = 135
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		talkWidth = 280
		(super init: &rest)
	#end:method

#end:class or instance

