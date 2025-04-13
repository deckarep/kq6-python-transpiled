#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 210
import sci_sh
import kernel
import Main
import rgCrown
import walkEgoInScr
import KQ6Print
import KQ6Room
import CartoonScript
import n913
import Print
import Scaler
import PolyPath
import Polygon
import Feature
import LoadMany
import StopWalk
import DPath
import Path
import Motion
import Game
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm210 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = [295, 71, 283, 65, 277, 64, -32768, -32768]
local9 = [292, 71, 280, 65, 268, 61, 262, 61, 258, 56, 270, 55, 285, 55, 290, 53, 298, 47, -32768, -32768]
local29 = None
local30 = None
local31 = None
local32 = None
local33 = 4660
local34 = None
local35 = -1


@SCI.procedure
def localproc_0(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	if singSing._send('script:'):
		local29 = param1
		if proc999_5(singSingScr._send('state:'), 3, 9):
			singSing._send('setScript:', 0)
		#endif
	else:
		param1._send('cue:')
	#endif
#end:procedure

@SCI.instance
class rm210(KQ6Room):
	#property vars (may be empty)
	noun = 3
	picture = 210
	horizon = 0
	south = 200
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global2._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 39, -10, 263, -10, 250, 78, 232, 104, 139, 139, 76, 113, 39, 82,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 0,
					'init:', 0, 189, 0, 120, 65, 120, 117, 148, 68, 189,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 29, 138, 94, 138, 94, 156, 31, 162,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 0, -10, 27, -10, 27, 84, 64, 119, 0, 119,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 115, 189, 151, 145, 244, 108, 266, 79, 319, 79, 319, 189,
					'yourself:'
				)
		)
		super._send('init:', &rest)
		global0._send('init:', 'setScale:', Scaler, 100, 84, 134, 81)
		global32._send('add:', genericFeatures, tree, holeInTree, 'eachElementDo:', #init)
		kernel.ScriptID(10, 4)._send('onMeCheck:', 2, 'setOnMeCheck:', 1, 2, 'init:')
		proc958_0(132, 214, 215, 216)
		match global12
			case 220:
				global2._send('setScript:', enterFromCastleScr, 0, global0)
			#end:case
			case 240:
				global2._send('setScript:', enterFromVillageScr)
			#end:case
			case 140:
				global104._send('fade:', 0, 30, 8, 1)
				global0._send(
					'posn:', singSing._send('approachX:'), singSing._send('approachY:'),
					'loop:', 6
				)
			#end:case
			else:
				if (global12 != 200):
					kernel.ScriptID(10, 0)._send('setIt:', 2)
				#endif
				local34 = 1
				proc12_1(91, 185, 30)
			#end:else
		#end:match
		temp2 = global9._send('at:', 39)._send('owner:')
		temp3 = global9._send('at:', 38)._send('owner:')
		if (proc913_0(94) and (temp3 != 140)):
			temp3 = global11
		#endif
		temp1 = global9._send('at:', 47)._send('owner:')
		if (global9._send('at:', 35)._send('owner:') == -1):
			theRibbon._send('init:')
		#endif
		if (global9._send('at:', 32)._send('owner:') == -1):
			letter._send('init:')
		#endif
		if (temp2 == 140):
			global9._send('at:', 39)._send('owner:', global11)
		#endif
		if (temp3 == 140):
			global9._send('at:', 38)._send('owner:', global11)
		#endif
		if (temp1 == 140):
			global9._send('at:', 47)._send('owner:', global11)
		#endif
		(= temp0
			(not
				(and
					proc999_5(temp1, global11, 140)
					proc999_5(temp2, global11, 140)
					proc999_5(temp3, global11, 140)
				)
			)
		)
		if kernel.ScriptID(10, 0)._send('isSet:', 2):
			kernel.ScriptID(10, 0)._send('clrIt:', 2)
			clown._send('init:')
		#endif
		(cond
			case 
				(and
					(global12 == 140)
					(temp3 == 140)
					(not ((temp1 == global11) and (temp2 == global11)))
				):
				proc10_2(returnToBranch, 18)
			#end:case
			case 
				(and
					(global12 == 140)
					(temp3 == 140)
					(temp1 == global11)
					(temp2 == global11)
				):
				proc10_2(notReturnScr, 20)
			#end:case
			case ((global12 == 140) and (temp1 == 140) and (temp2 != global11)):
				proc10_2(returnToBranch, 12)
			#end:case
			case 
				(and
					(global12 == 140)
					((temp2 == 140) or ((temp1 == 140) and (temp2 == global11)))
				):
				local32 = 1
				proc10_2(deliveryScr, 13)
			#end:case
			case proc913_0(62):
				proc10_2(deliveryScr, 5)
			#end:case
			case proc913_0(63):
				proc10_2(deliveryScr, 6)
			#end:case
			else:
				if (global0._send('has:', 0) and temp0):
					if proc913_0(21):
						singSing._send('init:', 0)
					else:
						singSing._send('init:', 1)
					#endif
					global103._send('number:', 210, 'loop:', -1, 'play:')
					musicScr._send('client:', musicScr, 'cue:')
				#endif
				proc913_2(62)
				proc913_2(63)
			#end:else
		)
		(= temp5
			(or
				proc999_5(global2._send('script:'), enterFromCastleScr, enterFromVillageScr)
				local34
			)
		)
		if 
			(and
				global5._send('contains:', singSing)
				(or
					(temp5 and (not global2._send('script:')._send('script:')))
					((not temp5) and (not global2._send('script:')))
				)
			)
			singSing._send('setScript:', singSingScr)
		#endif
		if (global12 != 220):
			global102._send('number:', 917, 'loop:', -1, 'play:')
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = global0._send('onControl:', 1)
		(cond
			case script: 0#end:case
			case (temp0 & 0x4000):
				global0._send('setSpeed:', 6)
				global2._send('setScript:', kernel.Clone(exitToCastleScr), 0, global0)
			#end:case
			case (temp0 & 0x2000):
				global2._send('setScript:', exitToVillageScr)
			#end:case
		)
		super._send('doit:', &rest)
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((param1 == 220) and global5._send('contains:', clown)):
			kernel.ScriptID(10, 0)._send('setIt:', 2)
		#endif
		if global5._send('contains:', singSing):
			global103._send('fade:')
			if global78._send('contains:', musicScr):
				musicScr._send('dispose:')
			#endif
		#endif
		super._send('newRoom:', param1, &rest)
	#end:method

	@classmethod
	def scriptCheck(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 85:
				if (not global5._send('contains:', singSing)):
					temp0 = 1
				else:
					self._send('setScript:', fluteScr)
					temp0 = 0
				#endif
			#end:case
			case 93:
				if (not global5._send('contains:', singSing)):
					temp0 = 1
				else:
					singSing._send('doVerb:', 37)
					temp0 = 0
				#endif
			#end:case
		#end:match
		return temp0
	#end:method

	@classmethod
	def edgeToRoom(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (param1 == 3):
				proc12_0(param1, 30)
				return 0
			#end:case
			case argc:
				super._send('edgeToRoom:', param1, &rest)
			#end:case
			else:
				super._send('edgeToRoom:')
			#end:else
		)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global102._send('fade:')
		super._send('dispose:')
		kernel.DisposeScript(983)
		kernel.DisposeScript(964)
	#end:method

#end:class or instance

@SCI.instance
class exitPath(Path):
	#property vars (may be empty)
	@classmethod
	def at(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (client == global0):
			return local1[param1]
		else:
			return local9[param1]
		#endif
	#end:method

#end:class or instance

@SCI.instance
class musicScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if (not register):
					global104._send('stop:')
				#endif
				register = 1
				global78._send('add:', self)
				while True: #repeat
					(breakif (register = kernel.Random(0, 2) != local33))
				#end:loop
				global104._send(
					'number:', match register
							case 0: 214#end:case
							case 1: 215#end:case
							case 2: 216#end:case
						#end:match,
					'loop:', 1,
					'play:', self
				)
			#end:case
			case 1:
				state = -1
				ticks = kernel.Random(60, 300)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('dispose:')
		if register:
			global78._send('delete:', self)
		#endif
		register = 0
	#end:method

#end:class or instance

@SCI.instance
class fluteScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				localproc_0(self)
			#end:case
			case 1:
				if global5._send('contains:', singSing):
					global103._send('fade:')
					musicScr._send('dispose:')
				#endif
				global102._send('fade:')
				self._send('setScript:', kernel.ScriptID(85), self)
			#end:case
			case 2:
				global91._send('say:', 14, 31, 9, 0, self)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				global102._send('play:')
				if global5._send('contains:', singSing):
					global103._send('play:')
					musicScr._send('state:', -1, 'client:', musicScr, 'cue:')
				#endif
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class enterFromVillageScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global0._send(
					'setSpeed:', 6,
					'posn:', 23, 70,
					'setScale:', Scaler, 86, 20, 88, 70,
					'setMotion:', MoveTo, 38, 88, self
				)
			#end:case
			case 1:
				global0._send('reset:', 2, 'setScale:', Scaler, 100, 84, 134, 81)
				cycles = 1
			#end:case
			case 2:
				if (not script):
					cycles = 1
				#endif
			#end:case
			case 3:
				if (not global5._send('contains:', clown)):
					global1._send('handsOn:')
				#endif
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class exitToVillageScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send(
					'setSpeed:', 6,
					'setScale:', Scaler, 90, 20, 88, 70,
					'setMotion:', MoveTo, 23, 70, self
				)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				global2._send('newRoom:', 240)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class enterFromCastleScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global0._send(
					'setSpeed:', 6,
					'posn:', 277, 64,
					'setScale:', Scaler, 30, 5, 75, 15,
					'setMotion:', DPath, 283, 65, 295, 71, 300, 79, self
				)
			#end:case
			case 1:
				global0._send('hide:')
				ticks = 150
			#end:case
			case 2:
				global0._send(
					'show:',
					'setPri:', 3,
					'posn:', 271, 130,
					'setLoop:', 2,
					'scaleX:', 108,
					'scaleY:', 108,
					'setScale:',
					'setMotion:', MoveTo, 263, 81, self
				)
			#end:case
			case 3:
				global0._send('setPri:', -1, 'setScale:', Scaler, 100, 84, 134, 81)
				cycles = 1
			#end:case
			case 4:
				global0._send('setMotion:', MoveTo, 260, 85, self)
			#end:case
			case 5:
				global0._send('reset:', 2)
				if register:
					register._send('cue:')
				#endif
				if (not script):
					cycles = 1
				#endif
			#end:case
			case 6:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class exitToCastleScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if (register == global0):
					global1._send('handsOff:')
				#endif
				register._send(
					'setLoop:', 3,
					'setPri:', 3,
					'setScale:',
					'setMotion:', MoveTo, 267, 131, self
				)
			#end:case
			case 1:
				register._send('hide:')
				ticks = 150
				if (register != global0):
					global1._send('handsOn:')
				#endif
			#end:case
			case 2:
				register._send(
					'show:',
					'setLoop:', -1,
					'setPri:', -1,
					'setScale:', Scaler, 30, 5, 75, 15,
					'posn:', 300, 79
				)
				register._send('setMotion:', kernel.Clone(exitPath), self)
			#end:case
			case 3:
				cycles = 2
			#end:case
			case 4:
				if (register == global0):
					global2._send('newRoom:', 220)
				else:
					self._send('dispose:')
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class clownScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				clown._send('setMotion:', PolyPath, 138, 144, self)
			#end:case
			case 1:
				clown._send('view:', 718, 'setLoop:', 5, 'setMotion:', PolyPath, 247, 104, self)
			#end:case
			case 2:
				clown._send('view:', 717, 'setLoop:', -1, 'setMotion:', PolyPath, 261, 85, self)
			#end:case
			case 3:
				self._send('setScript:', kernel.Clone(exitToCastleScr), self, clown)
			#end:case
			case 4:
				clown._send('hide:')
				seconds = 10
			#end:case
			case 5:
				clown._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class returnToBranch(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				singSing._send(
					'init:',
					'z:', 0,
					'setPri:', 1,
					'posn:', 305, 30,
					'setScale:', Scaler, 100, 5, 51, 30,
					'setLoop:', 0,
					'setCycle:', Fwd,
					'setMotion:', MoveTo, 272, 52, self
				)
			#end:case
			case 1:
				singSing._send(
					'setStep:', 4, 3,
					'setScale:', 0,
					'setMotion:', MoveTo, 226, 55, self
				)
			#end:case
			case 2:
				singSing._send('setLoop:', 3, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 3:
				singSing._send('loop:', 2, 'cel:', 8, 'posn:', 252, 125, 97, 'setPri:', 14)
				cycles = 2
			#end:case
			case 4:
				global91._send('say:', 1, 0, register, 0, self)
			#end:case
			case 5:
				global103._send('number:', 210, 'loop:', -1, 'play:')
				musicScr._send('client:', musicScr, 'cue:')
				proc913_2(62)
				proc913_2(63)
				singSing._send('setScript:', singSingScr)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class notReturnScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				seconds = 5
			#end:case
			case 1:
				global91._send('say:', 1, 0, register, 0, self)
			#end:case
			case 2:
				proc913_2(62)
				proc913_2(63)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class deliveryScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if proc999_5(register, 5, 6):
					singSing._send('init:', 0)
					(cond
						case clown._send('script:'):
							seconds = 6
						#end:case
						case (client == enterFromCastleScr):
							client._send('register:', self)
						#end:case
						else:
							seconds = 3
						#end:else
					)
				else:
					state = 2
					singSing._send(
						'init:',
						'z:', 0,
						'posn:', 305, 30,
						'setScale:', Scaler, 100, 5, 51, 30
					)
					cycles = 2
				#endif
			#end:case
			case 1:
				singSing._send('z:', 0, 'loop:', 4, 'cel:', 0, 'posn:', 225, 56, 'setCycle:', End, self)
			#end:case
			case 2:
				singSing._send('posn:', 201, 56)
				self._send('cue:')
			#end:case
			case 3:
				singSing._send(
					'view:', 214,
					'setLoop:', (0 if proc913_0(62) else 1),
					'setCycle:', Fwd
				)
				if proc999_5(register, 5, 6):
					state = 4
				#endif
				self._send('cue:')
			#end:case
			case 4:
				singSing._send('setMotion:', MoveTo, 272, 52, self)
			#end:case
			case 5:
				singSing._send('setScale:', 0, 'setStep:', 4, 3)
				if proc913_0(62):
					singSing._send('setMotion:', MoveTo, 156, 79, self)
				else:
					singSing._send('setMotion:', MoveTo, 111, 81, self)
				#endif
			#end:case
			case 6:
				if proc913_0(62):
					theRibbon._send('init:')
				else:
					letter._send('init:')
				#endif
				if 
					(and
						(global9._send('at:', 39)._send('owner:') == global11)
						(global9._send('at:', 38)._send('owner:') == global11)
						(global9._send('at:', 47)._send('owner:') == global11)
					)
					singSing._send(
						'view:', 213,
						'setLoop:', 0,
						'setMotion:', MoveTo, -10, 79, self
					)
				else:
					state.post('++')
					self._send('cue:')
				#endif
			#end:case
			case 7:
				singSing._send('dispose:')
				cycles = 2
				state = 10
			#end:case
			case 8:
				if proc913_0(62):
					singSing._send('posn:', 156, 79)
				else:
					singSing._send('posn:', 111, 81)
				#endif
				singSing._send('view:', 213, 'setLoop:', 5, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 9:
				if proc913_0(62):
					singSing._send('posn:', 185, 69)
				else:
					singSing._send('posn:', 141, 72)
				#endif
				singSing._send(
					'setLoop:', 1,
					'setCycle:', Fwd,
					'setMotion:', MoveTo, 220, 49, self
				)
			#end:case
			case 10:
				singSing._send(
					'setLoop:', -1,
					'loop:', 6,
					'cel:', 0,
					'posn:', 225, 56,
					'setCycle:', End, self
				)
			#end:case
			case 11:
				if global5._send('contains:', singSing):
					global103._send('number:', 210, 'loop:', -1, 'play:')
					musicScr._send('state:', -1, 'client:', musicScr, 'cue:')
				#endif
				global91._send('say:', 1, 0, register, 0, self)
			#end:case
			case 12:
				if global5._send('contains:', singSing):
					singSing._send(
						'loop:', 2,
						'cel:', 8,
						'posn:', 252, 125, 97,
						'setPri:', 14,
						'setScript:', singSingScr
					)
				#endif
				if local32:
					global1._send('handsOn:')
				#endif
				proc913_2(62)
				proc913_2(63)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class giveItemToBirdScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global0._send('setMotion:', MoveTo, 138, 142, self)
			#end:case
			case 1:
				global0._send('setHeading:', 90, self)
			#end:case
			case 2:
				localproc_0(self)
			#end:case
			case 3:
				global0._send(
					'view:', 211,
					'posn:', 147, 143,
					'loop:', 0,
					'cel:', 0,
					'normal:', 0,
					'setCycle:', End, self
				)
				if local31:
					genieSnake._send('init:')
				#endif
			#end:case
			case 4:
				if 
					(and
						global5._send('contains:', genieSnake)
						(genieSnake._send('script:')._send('state:') <= 0)
					)
					state.post('--')
					ticks = 15
				else:
					self._send('cue:')
				#endif
			#end:case
			case 5:
				client._send('cue:')
			#end:case
			case 6:
				global103._send('fade:')
				musicScr._send('dispose:')
				singSing._send('z:', 0, 'loop:', 4, 'posn:', 225, 56, 'setCycle:', End, self)
			#end:case
			case 7:
				singSing._send(
					'setLoop:', 0,
					'posn:', 201, 56,
					'setCycle:', Fwd, self,
					'setMotion:', MoveTo, 158, 95, self
				)
			#end:case
			case 8:
				if (global103._send('prevSignal:') != -1):
					global103._send('stop:')
				#endif
				global105._send('number:', 212, 'play:')
				if proc913_0(10):
					global105._send('hold:', 10)
				#endif
				singSing._send('setLoop:', 5, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 9:
				client._send('cue:')
			#end:case
			case 10:
				global0._send('setCycle:', Beg, self)
				self._send('cue:')
				register = 0
			#end:case
			case 11:
				singSing._send(
					'view:', 214,
					'setLoop:', match register
							case 2: 2#end:case
							case 1: 3#end:case
							case 0: 4#end:case
						#end:match,
					'posn:', 187, 85,
					'setCycle:', Fwd,
					'setMotion:', MoveTo, 272, 52, self
				)
			#end:case
			case 12:
				global0._send('posn:', (global0._send('x:') - 10), (global0._send('y:') - 3), 'reset:', 4)
			#end:case
			case 13:
				client._send('cue:')
			#end:case
			case 14:
				singSing._send(
					'setScale:', Scaler, 100, 5, 51, 30,
					'setMotion:', MoveTo, 305, 30, self
				)
			#end:case
			case 15:
				singSing._send('dispose:')
				if global5._send('contains:', genieSnake):
					genieSnake._send('script:')._send('caller:', self, 'ticks:', 0, 'state:', 2, 'cue:')
				else:
					self._send('cue:')
				#endif
			#end:case
			case 16:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class givePoemScr(CartoonScript):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global0._send('put:', 47, 140)
				global1._send('handsOff:')
				if (temp0 = global9._send('at:', 39)._send('owner:') == 210):
					global1._send('givePoints:', 1)
				#endif
				temp1 = global9._send('at:', 38)._send('owner:')
				(= register
					(cond
						case 
							(and
								(temp0 != global11)
								(temp1 != global11)
								(global9._send('at:', 47)._send('owner:') != global11)
							):
							local31 = 1
							(25 if proc913_0(10) else 26)
						#end:case
						case ((temp0 != global11) and (temp1 == global11)): 32#end:case
						case (temp0 == global11):
							proc913_1(63)
							14
						#end:case
					)
				)
				self._send('setScript:', giveItemToBirdScr, self, 2)
			#end:case
			case 1:
				if proc999_5(register, 14, 32, 25):
					KQ6Print._send('posn:', -1, 80)
				else:
					KQ6Print._send('posn:', -1, 100)
				#endif
				KQ6Print._send(
					'font:', global22,
					'say:', 0, 4, 32, register, 1,
					'init:', giveItemToBirdScr
				)
			#end:case
			case 2:
				if proc999_5(register, 25, 26):
					KQ6Print._send(
						'font:', global22,
						'posn:', -1, 100,
						'say:', 0, 4, 32, register, 2,
						'init:', giveItemToBirdScr
					)
				else:
					giveItemToBirdScr._send('cue:')
				#endif
			#end:case
			case 3:
				KQ6Print._send(
					'font:', global22,
					'posn:', -1, 100,
					'modeless:', 1,
					'ticks:', 0,
					'say:', 0, 4, 32, register, if proc999_5(register, 25, 26):
							3
						else:
							2
						#endif,
					'init:'
				)
				giveItemToBirdScr._send('cue:')
			#end:case
			case 4:
				if global25:
					if (global90 & 0x0002):
						self._send('cue:')
					else:
						state.post('++')
						KQ6Print._send('caller:', self)
					#endif
				else:
					state.post('++')
					self._send('cue:')
				#endif
			#end:case
			case 5:
				if (not (kernel.DoAudio(6) == -1)):
					state.post('--')
				#endif
				ticks = 10
			#end:case
			case 6:
				if proc913_0(10):
					global2._send('newRoom:', 140)
				else:
					global1._send('handsOn:')
					self._send('dispose:')
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class giveRingScr(CartoonScript):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global0._send('put:', 39, 140)
				global1._send('handsOff:')
				if proc913_0(10):
					global1._send('givePoints:', 3)
				else:
					global1._send('givePoints:', 1)
				#endif
				proc913_1(62)
				temp0 = global9._send('at:', 47)._send('owner:')
				temp1 = global9._send('at:', 38)._send('owner:')
				(= register
					(cond
						case 
							(and
								(temp0 != global11)
								(temp1 != global11)
								(global9._send('at:', 39)._send('owner:') != global11)
							):
							local31 = 1
							(25 if proc913_0(10) else 26)
						#end:case
						case ((temp0 == global11) and (temp1 != global11)): 36#end:case
						case ((temp0 == global11) and (temp1 == global11)): 38#end:case
						case ((temp1 == global11) and (temp0 != global11)): 34#end:case
						else:
							proc921_0(r"""Problem! In else state of giveRoseScr conditional.""")
						#end:else
					)
				)
				self._send('setScript:', giveItemToBirdScr, self, 0)
			#end:case
			case 1:
				(cond
					case (register == 25):
						KQ6Print._send('posn:', -1, 100)
					#end:case
					case proc999_5(register, 36, 34):
						KQ6Print._send('posn:', -1, 100)
					#end:case
					case (register == 38):
						KQ6Print._send('posn:', -1, 100)
					#end:case
					else:
						KQ6Print._send('posn:', -1, 100)
					#end:else
				)
				KQ6Print._send(
					'font:', global22,
					'say:', 0, 4, 70, register, 1,
					'init:', giveItemToBirdScr
				)
			#end:case
			case 2:
				if proc999_5(register, 25, 26):
					KQ6Print._send(
						'font:', global22,
						'posn:', -1, 100,
						'say:', 0, 4, 70, register, 2,
						'init:', giveItemToBirdScr
					)
				else:
					giveItemToBirdScr._send('cue:')
				#endif
			#end:case
			case 3:
				if proc999_5(register, 36, 38):
					register = 34
				#endif
				KQ6Print._send(
					'font:', global22,
					'posn:', -1, 100,
					'modeless:', 1,
					'ticks:', 0,
					'say:', 0, 4, 70, register, if proc999_5(register, 25, 26):
							3
						else:
							2
						#endif,
					'init:'
				)
				giveItemToBirdScr._send('cue:')
			#end:case
			case 4:
				if global25:
					if (global90 & 0x0002):
						self._send('cue:')
					else:
						state.post('++')
						KQ6Print._send('caller:', self)
					#endif
				else:
					state.post('++')
					self._send('cue:')
				#endif
			#end:case
			case 5:
				if (not (kernel.DoAudio(6) == -1)):
					state.post('--')
				#endif
				ticks = 10
			#end:case
			case 6:
				if proc913_0(10):
					global2._send('newRoom:', 140)
				else:
					global1._send('handsOn:')
					self._send('dispose:')
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class giveRoseScr(CartoonScript):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global0._send('put:', 38, 140)
				global1._send('handsOff:')
				temp0 = global9._send('at:', 39)._send('owner:')
				temp1 = global9._send('at:', 47)._send('owner:')
				if (temp0 == global11):
					global1._send('givePoints:', 1)
				#endif
				(= register
					(cond
						case 
							(and
								(temp0 != global11)
								(temp1 != global11)
								(global9._send('at:', 38)._send('owner:') != global11)
							):
							local31 = 1
							(25 if proc913_0(10) else 26)
						#end:case
						case ((temp0 != global11) and (temp1 == global11)): 41#end:case
						case ((temp0 == global11) and (temp1 != global11)): 23#end:case
						case ((temp0 == global11) and (temp1 == global11)): 24#end:case
						else:
							proc921_0(r"""Problem! In else state of giveRoseScr conditional.""")
						#end:else
					)
				)
				self._send('setScript:', giveItemToBirdScr, self, 1)
			#end:case
			case 1:
				(cond
					case (register == 25):
						KQ6Print._send('posn:', -1, 80)
					#end:case
					case proc999_5(register, 23, 41):
						KQ6Print._send('posn:', -1, 80)
					#end:case
					else:
						KQ6Print._send('posn:', -1, 100)
					#end:else
				)
				KQ6Print._send(
					'font:', global22,
					'say:', 0, 4, 71, register, 1,
					'init:', giveItemToBirdScr
				)
			#end:case
			case 2:
				if proc999_5(register, 25, 26):
					KQ6Print._send(
						'font:', global22,
						'posn:', -1, 100,
						'say:', 0, 4, 71, register, 2,
						'init:', giveItemToBirdScr
					)
				else:
					giveItemToBirdScr._send('cue:')
				#endif
			#end:case
			case 3:
				if proc999_5(register, 41):
					register = 23
				#endif
				KQ6Print._send(
					'font:', global22,
					'posn:', -1, 100,
					'modeless:', 1,
					'ticks:', 0,
					'say:', 0, 4, 71, register, if proc999_5(register, 25, 26):
							3
						else:
							2
						#endif,
					'init:'
				)
				giveItemToBirdScr._send('cue:')
			#end:case
			case 4:
				if global25:
					if (global90 & 0x0002):
						self._send('cue:')
					else:
						state.post('++')
						KQ6Print._send('caller:', self)
					#endif
				else:
					state.post('++')
					self._send('cue:')
				#endif
			#end:case
			case 5:
				if (not (kernel.DoAudio(6) == -1)):
					state.post('--')
				#endif
				ticks = 10
			#end:case
			case 6:
				if proc913_0(10):
					global2._send('newRoom:', 140)
				else:
					global1._send('handsOn:')
					self._send('dispose:')
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class windBirdHeader(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 120, 141, self)
			#end:case
			case 1:
				global0._send('setHeading:', 90, self)
			#end:case
			case 2:
				localproc_0(self)
			#end:case
			case 3:
				KQ6Print._send(
					'font:', global22,
					'posn:', 10, 10,
					'say:', 0, 4, 37, register, 1,
					'init:', self
				)
			#end:case
			case 4:
				cycles = 2
			#end:case
			case 5:
				global103._send('fade:')
				musicScr._send('dispose:')
				global0._send(
					'setSpeed:', 6,
					'view:', 883,
					'loop:', 1,
					'cel:', 0,
					'posn:', 120, 142,
					'normal:', 0,
					'setCycle:', Fwd,
					'scaleX:', 128,
					'scaleY:', 128,
					'setScale:'
				)
				global105._send('number:', 930, 'loop:', -1, 'play:')
				ticks = 180
			#end:case
			case 6:
				global105._send('stop:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class windUpBirdScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				self._send('setScript:', windBirdHeader, self, 10)
			#end:case
			case 1:
				global105._send('number:', 931, 'loop:', -1, 'play:')
				global0._send('loop:', 7, 'cycleSpeed:', 9, 'setCycle:', Fwd)
				ticks = 180
			#end:case
			case 2:
				KQ6Print._send(
					'font:', global22,
					'posn:', 10, 10,
					'say:', 0, 4, 37, 10, 2,
					'init:', self
				)
			#end:case
			case 3:
				KQ6Print._send(
					'font:', global22,
					'posn:', 10, 10,
					'say:', 0, 4, 37, 10, 3,
					'init:', self
				)
			#end:case
			case 4:
				ticks = 30
			#end:case
			case 5:
				global105._send('fade:')
				global103._send('play:', 0, 'fade:', 127, 25, 10, 0)
				musicScr._send('state:', -1, 'client:', musicScr, 'cue:')
				global0._send('reset:', 0, 'posn:', 126, 139)
				cycles = 2
			#end:case
			case 6:
				singSing._send('setScript:', singSingScr)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class befriendSSScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('givePoints:', 4)
				self._send('setScript:', windBirdHeader, self, 11)
			#end:case
			case 1:
				global0._send('loop:', 3, 'cel:', 0, 'posn:', 119, 142, 'setCycle:', End, self)
			#end:case
			case 2:
				windUpBird._send('init:')
				global105._send('number:', 931, 'loop:', -1, 'play:')
				global0._send('posn:', 120, 141, 'reset:', 0)
				cycles = 2
			#end:case
			case 3:
				ticks = 180
			#end:case
			case 4:
				KQ6Print._send(
					'font:', global22,
					'posn:', 10, 10,
					'say:', 0, 4, 37, 11, 2,
					'init:', self
				)
			#end:case
			case 5:
				singSing._send('posn:', 252, 125, 97, 'loop:', 2, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				KQ6Print._send(
					'font:', global22,
					'posn:', 10, 10,
					'say:', 0, 4, 37, 11, 3,
					'init:', self
				)
			#end:case
			case 8:
				ticks = 48
			#end:case
			case 9:
				global105._send('fade:')
				windUpBird._send('dispose:')
				global0._send(
					'setSpeed:', 6,
					'posn:', 119, 143,
					'view:', 883,
					'loop:', 3,
					'cel:', 7,
					'normal:', 0,
					'setCycle:', CT, 1, -1, self
				)
			#end:case
			case 10:
				global103._send('play:', 0, 'fade:', 127, 25, 10, 0)
				musicScr._send('state:', -1, 'client:', musicScr, 'cue:')
				global0._send('reset:', 0, 'posn:', 120, 141, 'setScale:', Scaler, 100, 84, 134, 81)
				proc913_1(21)
				singSing._send('setScript:', singSingScr)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class snakeScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				client._send('setCycle:', End, self)
			#end:case
			case 1:
				client._send('loop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 2:
				if (local35.post('++') < 2):
					global104._send('number:', 211, 'loop:', 1, 'play:')
				#endif
				if ((not kernel.Random(0, 1)) and (not local30)):
					local30 = 1
					state = 5
					self._send('cue:')
				else:
					state = 0
					ticks = kernel.Random(60, 150)
				#endif
			#end:case
			case 3:
				if (not local30):
					local30 = register = 1
					state = 5
					self._send('cue:')
				else:
					register = 0
					if global5._send('contains:', eye):
						eye._send('dispose:')
					#endif
					genieSnake._send('loop:', 2, 'cel:', 0, 'setCycle:', End, self)
				#endif
			#end:case
			case 4:
				genieSnake._send('dispose:')
			#end:case
			case 5:
				if (genieSnake._send('cel:') != 6):
					genieSnake._send('setCycle:', End, self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 6:
				eye._send('init:', 'setCycle:', End, self)
			#end:case
			case 7:
				ticks = 45
			#end:case
			case 8:
				eye._send('setCycle:', Beg, self)
			#end:case
			case 9:
				eye._send('dispose:')
				state = ((3 if register else 2) - 1)
				self._send('cue:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class showItemScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send(
					'setMotion:', MoveTo, singSing._send('approachX:'), singSing._send(
							'approachY:'
						), self
				)
			#end:case
			case 1:
				global0._send(
					'view:', 211,
					'posn:', 147, 145,
					'loop:', 0,
					'cel:', 0,
					'normal:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				ticks = 30
			#end:case
			case 3:
				global91._send('say:', 4, 0, 11, 1, self)
			#end:case
			case 4:
				if proc913_0(21):
					global91._send('say:', 4, register, 10, 1, self)
				else:
					global91._send('say:', 4, register, 11, 2, self)
				#endif
			#end:case
			case 5:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				global0._send(
					'reset:', 4,
					'posn:', singSing._send('approachX:'), singSing._send('approachY:')
				)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class singSingScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				register = proc913_0(21)
				cycles = 1
			#end:case
			case 1:
				(= state
					match kernel.Random(0, 1)
						case 0: 4#end:case
						case 1: 10#end:case
					#end:match
				)
				state.post('--')
				if local29:
					self._send('dispose:')
				else:
					seconds = kernel.Random(3, 12)
				#endif
			#end:case
			case 2:
				if register:
					singSing._send('posn:', 225, 105, 49)
				else:
					singSing._send('posn:', 268, 96, 85)
				#endif
				cycles = 2
			#end:case
			case 3: 0#end:case
			case 4:
				singSing._send('loop:', 7, 'cel:', 0)
				self._send('changeState:', 2)
				state = 4
			#end:case
			case 5:
				singSing._send('setCycle:', End, self)
			#end:case
			case 6:
				cycles = 2
			#end:case
			case 7:
				singSing._send('setCycle:', Beg, self)
			#end:case
			case 8:
				state = 0
				ticks = 1
			#end:case
			case 9: 0#end:case
			case 10:
				singSing._send('loop:', 8, 'cel:', 0)
				self._send('changeState:', 2)
				state = 10
			#end:case
			case 11:
				singSing._send('cycleSpeed:', 8, 'setCycle:', End, self)
			#end:case
			case 12:
				singSing._send('cycleSpeed:', 6, 'cel:', 0)
				cycles = 2
			#end:case
			case 13:
				self._send('changeState:', 8)
			#end:case
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (local29 and (local29 != -1)):
			if (not global18):
				global18 = Set._send('new:')
			#endif
			global18._send('add:', Cue._send('new:')._send('cuee:', local29, 'cuer:', self, 'yourself:'))
		#endif
		singSing._send('cycleSpeed:', 6)
		local29 = seconds = 0
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class getRibbonScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global1._send('givePoints:', 1)
				cycles = 2
			#end:case
			case 1:
				global0._send('get:', 35, 'setHeading:', 90, self)
			#end:case
			case 2:
				if (not proc913_0(112)):
					proc913_1(93)
				#endif
				cycles = 2
			#end:case
			case 3:
				global0._send(
					'normal:', 0,
					'setSpeed:', 6,
					'posn:', 142, 149,
					'view:', 215,
					'loop:', 1,
					'cel:', 0
				)
				cycles = 2
			#end:case
			case 4:
				global0._send('setCycle:', CT, 3, 1, self)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				theRibbon._send('dispose:')
				global0._send('setCycle:', End, self)
			#end:case
			case 7:
				cycles = 2
			#end:case
			case 8:
				global0._send('reset:', 6, 'posn:', 129, 144)
				cycles = 2
			#end:case
			case 9:
				kernel.UnLoad(128, 215)
				global91._send('say:', 6, 5, (22 if proc913_0(10) else 21), 0, self)
			#end:case
			case 10:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getLetterScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global1._send('givePoints:', 1)
				cycles = 2
			#end:case
			case 1:
				global0._send('get:', 32, 'setHeading:', 270, self)
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				global0._send(
					'normal:', 0,
					'setSpeed:', 6,
					'posn:', 138, 147,
					'view:', 215,
					'loop:', 0,
					'cel:', 0
				)
				cycles = 2
			#end:case
			case 4:
				global0._send('setCycle:', CT, 3, 1, self)
			#end:case
			case 5:
				cycles = 2
			#end:case
			case 6:
				letter._send('dispose:')
				global0._send('setCycle:', End, self)
			#end:case
			case 7:
				cycles = 2
			#end:case
			case 8:
				global0._send('reset:', 7, 'posn:', 149, 142)
				cycles = 2
			#end:case
			case 9:
				if global5._send('contains:', singSing):
					global103._send('fade:', 0, 15, 20, 1)
					musicScr._send('dispose:')
				else:
					state.post('++')
				#endif
				global91._send('say:', 5, 5, 0, 1, self)
			#end:case
			case 10:
				if (global103._send('prevSignal:') != -1):
					state.post('--')
				#endif
				cycles = 2
			#end:case
			case 11:
				global105._send('number:', 213, 'loop:', -1, 'play:')
				if (global90 & 0x0002):
					global91._send('say:', 5, 5, 0, 2, self)
				else:
					KQ6Print._send(
						'addText:', r"""Dearest Alexander:\n\nI cannot believe you are here, my friend! Please, please be careful! Abdul isn't about to let anyone interfere with his plans. Watch out for Abdul's genie, Alexander, and do not do anything rash.""",
						'init:', self
					)
				#endif
			#end:case
			case 12:
				if (global90 & 0x0002):
					cycles = 1
				else:
					KQ6Print._send(
						'addText:', r"""I am not without resources, and I will prevail if I can only find some small means of defense. Do nothing to try to get to me. You must not be endangered again for my sake.\n\nGreatly in your family's debt,\n\nCassima""",
						'init:', self
					)
				#endif
			#end:case
			case 13:
				global91._send('say:', 5, 5, 0, 3, self, 'oneOnly:', 0)
			#end:case
			case 14:
				global105._send('client:', self, 'fade:', 0, 15, 20, 1)
			#end:case
			case 15:
				if global5._send('contains:', singSing):
					global103._send('play:')
					musicScr._send('state:', -1, 'client:', musicScr, 'cue:')
				#endif
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class eye(Prop):
	#property vars (may be empty)
	x = 128
	y = 24
	view = 902
	priority = 14
	signal = 16
	
#end:class or instance

@SCI.instance
class singSing(Actor):
	#property vars (may be empty)
	x = 252
	y = 125
	z = 97
	noun = 4
	approachX = 138
	approachY = 142
	view = 213
	loop = 2
	priority = 14
	signal = 8208
	
	@classmethod
	def init(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send(
			'setScale:', 0,
			'setStep:', 4, 3,
			'ignoreActors:',
			'cel:', (8 if (not param1) else 0)
		)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case proc999_5(param1, 1, 5):
				global91._send('say:', noun, param1, (10 if proc913_0(21) else 11))
			#end:case
			case (proc999_5(param1, 29, 46, 44, 66) and proc913_0(21)):
				global91._send('say:', noun, 29, 10)
			#end:case
			case (param1 == 37):
				if proc913_0(21):
					global2._send('setScript:', windUpBirdScr)
				else:
					global2._send('setScript:', befriendSSScr)
				#endif
			#end:case
			case (param1 == 2):
				global91._send(
					'say:', noun, param1, (cond
							case (not proc913_0(21)): 11#end:case
							case global0._send('has:', 32): 19#end:case
							else: 43#end:else
						)
				)
			#end:case
			case (param1 == 31):
				global2._send('setScript:', fluteScr)
			#end:case
			case (not proc913_0(21)):
				global2._send('setScript:', showItemScr, 0, 0)
			#end:case
			case proc999_5(param1, 15, 18):
				global91._send('say:', noun, 15, 10)
			#end:case
			case (param1 == 32):
				global2._send('setScript:', givePoemScr)
			#end:case
			case (param1 == 71):
				if proc913_0(94):
					global91._send('say:', noun, param1, 27)
				else:
					proc913_1(94)
					global2._send('setScript:', giveRoseScr)
				#endif
			#end:case
			case (param1 == 70):
				global2._send('setScript:', giveRingScr)
			#end:case
			case proc999_5(param1, 42, 27, 28, 45, 8):
				global91._send('say:', noun, 42, 10)
			#end:case
			case proc999_5(param1, 33, 65):
				global91._send('say:', noun, 33)
			#end:case
			case proc999_5(param1, 63, 67):
				global2._send('setScript:', showItemScr, 0, 63)
			#end:case
			case proc999_5(param1, 35, 47, 68, 72):
				global2._send('setScript:', showItemScr, 0, param1)
			#end:case
			else:
				global2._send('setScript:', showItemScr, 0, 0)
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class letter(Actor):
	#property vars (may be empty)
	x = 119
	y = 89
	noun = 5
	sightAngle = 45
	approachX = 146
	approachY = 142
	yStep = 4
	view = 214
	loop = 7
	cel = 1
	priority = 1
	signal = 18448
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('posn:', 112, 136, 'setLoop:', 8, 'cel:', 0, 'stopUpd:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global2._send('setScript:', getLetterScr)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('approachVerbs:', 5)
		if (global9._send('at:', 32)._send('owner:') != -1):
			global9._send('at:', 32)._send('owner:', -1)
			self._send('setMotion:', MoveTo, 120, 137, self)
		else:
			self._send('cue:')
		#endif
	#end:method

#end:class or instance

@SCI.instance
class theRibbon(Actor):
	#property vars (may be empty)
	x = 155
	y = 87
	noun = 6
	sightAngle = 45
	approachX = 133
	approachY = 143
	yStep = 4
	view = 214
	loop = 5
	priority = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('approachVerbs:', 5, 'signal:', 18448)
		if (global9._send('at:', 35)._send('owner:') != -1):
			global9._send('at:', 35)._send('owner:', -1)
			self._send('setMotion:', MoveTo, 155, 138, self)
		else:
			self._send('cue:')
		#endif
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('posn:', 153, 138, 'setLoop:', 6, 'cel:', 0, 'stopUpd:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global2._send('setScript:', getRibbonScr)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genieSnake(Prop):
	#property vars (may be empty)
	x = 109
	y = 5
	view = 212
	
	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('dispose:')
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('setScript:', snakeScr, 'setPri:', 14)
	#end:method

#end:class or instance

@SCI.instance
class clown(Actor):
	#property vars (may be empty)
	x = 62
	y = 102
	view = 717
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send(
			'setScale:', Scaler, 100, 84, 134, 81,
			'setScript:', clownScr,
			'ignoreActors:',
			'setStep:', 4, 3,
			'moveSpeed:', 7,
			'cycleSpeed:', 7,
			'setCycle:', StopWalk, 2741
		)
	#end:method

#end:class or instance

@SCI.instance
class windUpBird(Prop):
	#property vars (may be empty)
	x = 141
	y = 142
	view = 883
	loop = 5
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('setCycle:', Fwd)
	#end:method

#end:class or instance

@SCI.instance
class tree(Feature):
	#property vars (may be empty)
	x = 160
	y = 30
	noun = 11
	sightAngle = 40
	onMeCheck = 32
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global91._send(
					'say:', noun, param1, (cond
							case 
								(and
									global5._send('contains:', singSing)
									proc913_0(21)
								):
								10
							#end:case
							case global5._send('contains:', singSing): 11#end:case
							else: 8#end:else
						)
				)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class holeInTree(Feature):
	#property vars (may be empty)
	x = 147
	y = 111
	noun = 12
	sightAngle = 40
	onMeCheck = 128
	approachX = 136
	approachY = 139
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('approachVerbs:', 5, 2)
	#end:method

#end:class or instance

@SCI.instance
class genericFeatures(Feature):
	#property vars (may be empty)
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(= noun
				match temp0 = kernel.OnControl(4, param1._send('x:'), param1._send('y:'))
					case 4: 8#end:case
					case 8: 9#end:case
					case 16: 10#end:case
					case 64: 13#end:case
					else:
						(13 if proc999_5(temp0, 64, 16384) else 0)
					#end:else
				#end:match
			)
		)
	#end:method

#end:class or instance

