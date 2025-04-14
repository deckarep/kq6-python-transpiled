#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 190
import sci_sh
import kernel
import Main
import KQ6Print
import n913
import Sound
import Motion
import User
import System

# Public Export Declarations
SCI.public_exports(
	openBook = 0,
	spellBookScr = 1,
	makeRainScript = 2,
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
local10
local14 = 110
local15 = 1
local16
local216
local416
local616 = None


@SCI.instance
class openBook(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				local616 = global0._send('cel:')
				seconds = 2
			#end:case
			case 1:
				global0._send(
					'normal:', 0,
					'view:', 903,
					'cel:', 0,
					'setLoop:', 2,
					'cycleSpeed:', 5,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				global0._send('cel:', 0, 'setLoop:', 0, 'setCycle:', End, self)
			#end:case
			case 3:
				client._send('setScript:', kernel.ScriptID(190, 1))
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class spellBookScr(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		global1._send('handsOff:')
		User._send('canInput:', 1)
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
		global69._send('disable:')
		kernel.DrawPic(98, 10)
		super._send('init:', &rest)
	#end:method

	@classmethod
	def doit():
		super._send('doit:', &rest)
		if local15:
			return
		#endif
		(cond
			case 
				(and
					(&
						(= temp0
							kernel.OnControl(4, User._send('curEvent:')._send('x:'), User._send(
									'curEvent:'
								)._send(
								'y:'
							))
						)
						0x0002
					)
					(local8 != 2)
				):
				local8 = 2
				kernel.SetCursor(190, 0, 1)
			#end:case
			case ((temp0 & 0x0004) and (local8 != 3)):
				local8 = 3
				kernel.SetCursor(190, 0, 2)
			#end:case
			case ((temp0 & 0x0008) and (local8 != 4)):
				if (local8 != 4):
					local8 = 4
					kernel.SetCursor(190, 0, 0)
				#endif
			#end:case
			case ((temp0 & 0x4000) and (local8 != 1)):
				local8 = 1
				global1._send('setCursor:', global69._send('at:', 2)._send('cursor:'))
			#end:case
			case ((not (temp0 & 0x400e)) and (local8 != 5)):
				local8 = 5
				global69._send('curIcon:', global69._send('at:', 0))
				global1._send('setCursor:', global69._send('curIcon:')._send('cursor:'))
			#end:case
		)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		if 
			(and
				(not param1._send('modifiers:'))
				(or
					(param1._send('type:') & 0x0001)
					((param1._send('type:') == 4) and (param1._send('message:') == 13))
				)
				(not param1._send('claimed:'))
			)
			match local8
				case 1:
					global91._send(
						'say:', match local9
								case 0: 4#end:case
								case 1: 5#end:case
								case 2: 6#end:case
							#end:match, 1, 0, 0, 0, 190
					)
				#end:case
				case 2:
					if (local9 > 0):
						global1._send('handsOff:')
						local9.post('--')
						state = -1
						self._send('cue:')
					else:
						global91._send('say:', 2, 5, 0, 0, 0, 190)
					#endif
				#end:case
				case 3:
					if (local9 < 2):
						global1._send('handsOff:')
						local9.post('++')
						state = -1
						self._send('cue:')
					else:
						global91._send('say:', 1, 5, 0, 0, 0, 190)
					#endif
				#end:case
				case 4:
					self._send('cue:')
				#end:case
				case 5:
					self._send('dispose:')
				#end:case
			#end:match
			local8 = -1
			param1._send('claimed:', 1)
		#endif
		param1._send('claimed:')
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				match local9
					case 0:
						1
						register = 12
					#end:case
					case 1:
						0
						register = 16
					#end:case
					case 2:
						2
						register = 18
					#end:case
				#end:match
				kernel.Message(0, 190, 3, 0, register, 1, @local16)
				cycles = 1
			#end:case
			case 1:
				match local9
					case 0:
						1
						register = 13
					#end:case
					case 1:
						0
						register = 17
					#end:case
					case 2:
						2
						register = 19
					#end:case
				#end:match
				kernel.Message(0, 190, 3, 0, register, 1, @local216)
				cycles = 1
			#end:case
			case 2:
				match local9
					case 0:
						1
						register = 14
					#end:case
					case 1:
						0
						register = 20
					#end:case
					case 2:
						2
						register = 21
					#end:case
				#end:match
				kernel.Message(0, 190, 3, 0, register, 1, @local416)
				register = 0
				cycles = 1
			#end:case
			case 3:
				kernel.DrawPic(190, 10)
				self._send('cue:')
			#end:case
			case 4:
				kernel.Display(@local416, 100, 45, 30, 106, local14, 102, 98, 105, 1111)
				if (local9 == 2):
					temp1 = 49
				else:
					temp1 = 40
				#endif
				kernel.Display(@local16, 100, 45, temp1, 106, local14, 102, 98, 105, 1111)
				kernel.Display(r"""INCANTATION:""", 100, 178, 27, 106, 100, 102, 98, 105, 1111)
				kernel.Display(@local216, 100, 178, 37, 106, 100, 102, 98, 105, 1111)
				User._send('canInput:', 1, 'canControl:', 1)
				local8 = 999
				local15 = 0
			#end:case
			case 5:
				state.post('--')
				match local9
					case 0:
						if 
							(or
								(global11 != 230)
								(not proc913_0(23))
								(proc913_0(23) and proc913_0(24))
							)
							global91._send('say:', 4, 2, 5, 0, 0, 190)
						else:
							register = 1
							self._send('dispose:')
						#endif
					#end:case
					case 2:
						temp0 = global9._send('at:', 11)._send('state:')
						(cond
							case 
								(and
									proc999_5(temp0, 15, 7)
									(or
										(global11 != 340)
										(and
											(global11 == 340)
											(not
												local0._send(
													'contains:', kernel.ScriptID(344, 2)
												)
											)
										)
									)
								):
								global91._send('say:', 6, 2, 2, 0, 0, 190)
							#end:case
							case 
								(and
									proc999_5(temp0, 15, 7)
									(global11 == 340)
									local0._send('contains:', kernel.ScriptID(344, 2))
								):
								register = 1
								self._send('dispose:')
							#end:case
							else:
								global91._send('say:', 6, 2, 11, 0, 0, 190)
							#end:else
						)
					#end:case
					case 1:
						(cond
							case (global0._send('has:', 19) and (global161 == 15)):
								global91._send('say:', 5, 2, 23, 0, 0, 190)
							#end:case
							case (global161 == 7):
								(global161 |= 0x0008)
								register = 4660
								proc913_1(31)
								self._send('dispose:')
							#end:case
							else:
								global91._send('say:', 5, 2, 11, 0, 0, 190)
							#end:else
						)
					#end:case
				#end:match
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		global1._send('setCursor:', global21)
		super._send('dispose:')
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
		global0._send('reset:', 2)
		if (global11 == 781):
			global0._send('setPri:', 13)
		#endif
		kernel.DrawPic(global2._send('picture:'), 100)
		if global10:
			global10._send('doit:')
		#endif
		global69._send('enable:')
		global1._send('handsOn:')
		match register
			case 1:
				kernel.Animate(global5._send('elements:'), 1)
				if 
					(not
						(and
							(local9 == 2)
							(not (global9._send('at:', 11)._send('state:') & 0x0008))
						)
					)
					global1._send('givePoints:', 3)
				#endif
				global2._send('notify:')
			#end:case
			case 4660:
				global1._send('givePoints:', 3)
				kernel.Animate(global5._send('elements:'), 1)
				global2._send('setScript:', kernel.ScriptID(190, 2))
			#end:case
		#end:match
		if (global2._send('script:') != makeRainScript):
			kernel.DisposeScript(190)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class localSound(Sound):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class makeRainScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				proc913_1(59)
				global91._send('say:', 3, 0, 9, 1, self, 0)
			#end:case
			case 1:
				KQ6Print._send('say:', 0, 3, 0, 9, 2, 0, 0, 0, 'posn:', 10, 10, 'width:', 289, 'init:')
				global0._send(
					'normal:', 0,
					'view:', 586,
					'cel:', 0,
					'setLoop:', 0,
					'cycleSpeed:', 5,
					'setCycle:', Fwd
				)
				seconds = 13
			#end:case
			case 2:
				if global25:
					global25._send('dispose:')
				#endif
				localSound._send('number:', 945, 'loop:', 1, 'play:')
				global0._send('cel:', 0, 'setLoop:', 1, 'setCycle:', CT, 2, 1, self)
			#end:case
			case 3:
				global0._send('setCycle:', CT, 0, -1, self)
			#end:case
			case 4:
				global0._send('setCycle:', CT, 2, 1, self)
			#end:case
			case 5:
				global0._send('setCycle:', CT, 0, -1, self)
			#end:case
			case 6:
				global0._send('setCycle:', End, self)
			#end:case
			case 7:
				global91._send('say:', 3, 0, 9, 3, self, 0)
			#end:case
			case 8:
				proc913_2(59)
				global0._send('reset:', local616)
				if (global11 == 781):
					global0._send('setPri:', 13)
				#endif
				localSound._send('stop:', 'dispose:')
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(190)
	#end:method

#end:class or instance

