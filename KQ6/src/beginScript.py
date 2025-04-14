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
		match state = param1
			case 0:
				global1._send('handsOff:')
				global69._send('disable:', 6)
				if (not proc913_0(129)):
					proc913_1(129)
					global1._send('givePoints:', 1)
				#endif
				global91._send('say:', 1, 27, 0, 1, self, 0)
			#end:case
			case 1:
				seconds = 2
			#end:case
			case 2:
				global0._send(
					'normal:', 0,
					'view:', 903,
					'cel:', 0,
					'setLoop:', 2,
					'cycleSpeed:', 5,
					'setCycle:', End, self
				)
			#end:case
			case 3:
				global0._send('cel:', 0, 'setLoop:', 0, 'setCycle:', End, self)
			#end:case
			case 4:
				global0._send('setLoop:', 1, 'setCycle:', Fwd)
				seconds = 4
			#end:case
			case 5:
				client._send('setScript:', kernel.ScriptID(90, 1))
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class riddleBookScript(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		local9 = global91
		global91 = rBookMessager
		local0 = global5
		local1 = global32
		local2 = global10
		local3 = global73
		local4 = global72
		local5 = global74
		local6 = global93
		local7 = global2._send('obstacles:')
		global2._send('obstacles:', List._send('new:')._send('add:', 'yourself:'))
		global5 = EventHandler._send('new:')._send('name:', r"""newCast""", 'add:')
		global32 = EventHandler._send('new:')._send('name:', r"""newFeatures""", 'add:', self)
		global10 = EventHandler._send('new:')._send('name:', r"""newATPs""", 'add:')
		global73 = EventHandler._send('new:')._send('name:', r"""newMH""", 'add:', self)
		global72 = EventHandler._send('new:')._send('name:', r"""newKH""", 'add:', self)
		global74 = EventHandler._send('new:')._send('name:', r"""newDH""", 'add:', self)
		global93 = EventHandler._send('new:')._send('name:', r"""newWH""", 'add:')
		if register:
			global9._send('hide:')
			register = 0
		#endif
		kernel.DrawPic(98)
		super._send('init:', &rest)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				background._send('init:')
				bookView._send('init:', 'stopUpd:')
				seconds = 2
			#end:case
			case 1:
				global91._send('say:', 1, 27, 0, 2, self, 0)
			#end:case
			case 2:
				global91._send('say:', 1, 27, 0, 3, self, 0)
			#end:case
			case 3:
				global1._send('handsOn:')
				global32._send('delete:', self)
				User._send('controls:', 0)
				global69._send('disable:', 0, 3, 4, 5)
			#end:case
			case 4:
				global1._send('handsOff:')
				if global25:
					global25._send('dispose:')
				#endif
				global1._send('setCursor:', global21)
				global5._send(
					'eachElementDo:', #dispose,
					'eachElementDo:', #delete,
					'release:',
					'dispose:'
				)
				global10._send('dispose:')
				global32._send('delete:', background, self, 'dispose:')
				global73._send('delete:', self, 'dispose:')
				global72._send('delete:', self, 'dispose:')
				global74._send('delete:', self, 'dispose:')
				global93._send('delete:', self, 'dispose:')
				global2._send('obstacles:')._send('dispose:')
				global2._send('obstacles:', local7)
				global5 = local0
				global32 = local1
				global73 = local3
				global72 = local4
				global74 = local5
				global93 = local6
				global10 = local2
				kernel.UnLoad(128, 904)
				kernel.DrawPic(global2._send('picture:'), 100)
				if global10:
					global10._send('doit:')
				#endif
				seconds = 2
			#end:case
			case 5:
				global0._send('setLoop:', 2, 'cycleSpeed:', 10, 'lastCel:', 'setCycle:', Beg, self)
			#end:case
			case 6:
				global0._send('reset:', 2)
				global69._send('enable:', 6)
				global1._send('handsOn:')
				self._send('dispose:')
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
		riddleBookScript._send('cue:')
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
		if (param1 == 1):
			riddleBookScript._send('state:', (riddleBookScript._send('state:') - 3), 'cue:')
		else:
			background._send('doVerb:', param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class rBookMessager(Kq6Messager):
	#property vars (may be empty)
	@classmethod
	def findTalker(param1 = None, *rest):
		if (param1 == 99):
			temp0 = localNarrator
			return
		else:
			super._send('findTalker:', param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class localNarrator(Kq6Narrator):
	#property vars (may be empty)
	y = 135
	
	@classmethod
	def init():
		talkWidth = 280
		super._send('init:', &rest)
	#end:method

#end:class or instance

