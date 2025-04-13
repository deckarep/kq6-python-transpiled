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
				global1._send('handsOff:', 'killSound:', 1)
				global69._send('disable:')
				global91._send('say:', 1, 14, 0, 1, self, 0)
			#end:case
			case 1:
				global0._send(
					'cycleSpeed:', 10,
					'view:', 935,
					'setPri:', 14,
					'cel:', 0,
					'setLoop:', 0,
					'setCycle:', End, self
				)
				localMusic._send('number:', 925, 'play:', 'loop:', 1)
			#end:case
			case 2:
				seconds = 2
			#end:case
			case 3:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 4:
				cycles = 15
			#end:case
			case 5:
				global91._send('say:', 1, 14, 0, 2, self, 0)
			#end:case
			case 6:
				client._send('setScript:', kernel.ScriptID(87, 1))
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
				local7 = global2._send('obstacles:')
				global2._send('obstacles:', List._send('new:')._send('add:', 'yourself:'))
				global5 = EventHandler._send('new:')._send('name:', r"""newCast""", 'add:')
				global32 = EventHandler._send('new:')._send(
					'name:', r"""newFeatures""",
					'add:', self
				)
				global10 = EventHandler._send('new:')._send('name:', r"""newATPs""", 'add:')
				global73 = EventHandler._send('new:')._send('name:', r"""newMH""", 'add:', self)
				global72 = EventHandler._send('new:')._send('name:', r"""newKH""", 'add:', self)
				global74 = EventHandler._send('new:')._send('name:', r"""newDH""", 'add:', self)
				global93 = EventHandler._send('new:')._send('name:', r"""newWH""", 'add:')
				kernel.DrawPic(981, 9)
				cycles = 2
			#end:case
			case 1:
				global91._send('say:', 1, 14, 0, 3, self, 0)
			#end:case
			case 2:
				localMusic._send('number:', 926, 'play:', self)
				newEgo._send(
					'init:',
					'posn:', 147, 118,
					'setLoop:', 1,
					'cel:', 0,
					'setPri:', 14,
					'cycleSpeed:', 12,
					'setCycle:', End, self
				)
			#end:case
			case 3:
				kernel.Palette(1, 981)
			#end:case
			case 4:
				kernel.Palette(1, 97)
				if (localMusic._send('prevSignal:') == -1):
					cycles = 1
				#endif
			#end:case
			case 5:
				if (localMusic._send('prevSignal:') == 10):
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
				global91._send('say:', 1, 14, 0, 4, self, 0)
			#end:case
			case 9:
				seconds = 5
			#end:case
			case 10:
				global91._send('say:', 1, 14, 0, 5, self, 0)
			#end:case
			case 11:
				localMusic._send('number:', 927, 'play:', self)
			#end:case
			case 12:
				global91._send('say:', 1, 14, 0, 6, self, 0)
			#end:case
			case 13:
				newEgo._send('cel:', 0, 'setLoop:', 2, 'setCycle:', End, self)
			#end:case
			case 14:
				newEgo._send('cel:', 0, 'setLoop:', 3, 'setCycle:', End, self)
			#end:case
			case 15:
				global5._send(
					'eachElementDo:', #dispose,
					'eachElementDo:', #delete,
					'release:',
					'dispose:'
				)
				global10._send('dispose:')
				global32._send('delete:', self, 'dispose:')
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
				kernel.DrawPic(global2._send('picture:'), 9)
				global0._send('reset:', 2)
				cycles = 3
			#end:case
			case 16:
				cycles = 3
			#end:case
			case 17:
				global91._send('say:', 1, 14, 0, 7, self, 0)
			#end:case
			case 18:
				global91._send('say:', 1, 14, 0, 8, self, 0)
			#end:case
			case 19:
				global69._send('enable:')
				global1._send('handsOn:', 'killSound:', 0)
				proc913_1(153)
				localMusic._send('stop:', 'dispose:')
				self._send('dispose:')
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

