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
		super._send('dispose:')
		kernel.DisposeScript(821)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				kernel.ScriptID(80, 0)._send('dungeonEntered:', 3)
				global0._send(
					'normal:', 0,
					'view:', 825,
					'setLoop:', 0,
					'cel:', 0,
					'posn:', 100, 144,
					'setPri:', 9,
					'setCycle:', 0,
					'cycleSpeed:', 8,
					'moveSpeed:', 0,
					'setScale:',
					'scaleX:', 121,
					'scaleY:', 121,
					'setMotion:', JumpTo, 150, 154, self
				)
			#end:case
			case 1:
				global0._send('setCycle:', End, self)
			#end:case
			case 2:
				global105._send('number:', 960, 'setLoop:', 1, 'play:', self)
			#end:case
			case 3:
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 711, 64)):
					global91._send('say:', 1, 0, 8, 0, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 4:
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 711, 64)):
					global105._send('number:', 902, 'loop:', 1, 'play:')
					kernel.ScriptID(820, 3)._send('setCycle:', Beg, self)
				else:
					(state += 2)
					cycles = 1
				#endif
			#end:case
			case 5:
				global105._send('number:', 822, 'loop:', 1, 'play:', self)
			#end:case
			case 6:
				cycles = 1
			#end:case
			case 7:
				local0 = 0
				(cond
					case kernel.ScriptID(80, 0)._send('tstFlag:', 709, 128):
						state = 9
						self._send('setScript:', beautyEntrance, self)
					#end:case
					case kernel.ScriptID(80, 0)._send('tstFlag:', 709, 4096):
						kernel.ScriptID(80, 0)._send('clrFlag:', 709, 4096)
						self._send('setScript:', searchEgo, self)
					#end:case
					case kernel.ScriptID(80, 0)._send('tstFlag:', 711, 32):
						kernel.ScriptID(80, 0)._send('clrFlag:', 711, 32)
						local0 = global0._send('has:', 44)
						kernel.ScriptID(820, 3)._send('setPri:', -1, 'stopUpd:')
						self._send('setScript:', afterClownHelpedEgoEscape, self)
					#end:case
					case 
						(and
							proc913_0(10)
							(not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 16384))
						):
						kernel.ScriptID(80, 0)._send('setFlag:', 709, 16384, 1)
						kernel.ScriptID(80, 0)._send('setFlag:', 711, 32)
						self._send('register:', jolloHelpsEgo, 'setScript:', jolloHelpsEgo)
					#end:case
					case global0._send('has:', 44):
						local0 = 1
						cycles = 1
					#end:case
					else:
						cycles = 1
					#end:else
				)
			#end:case
			case 8:
				kernel.ScriptID(80, 0)._send('setFlag:', 711, 64)
				if (not register):
					register = self
				#endif
				global0._send('loop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 9:
				if local0:
					state = 11
				#endif
				global0._send('reset:', 7, 'posn:', 132, 149)
				if (register != self):
					register._send('cycles:', 1)
				else:
					cycles = 1
				#endif
			#end:case
			case 10:
				cycles = 3
			#end:case
			case 11:
				global2._send('setScript:', kernel.ScriptID(820, 1))
			#end:case
			case 12:
				global1._send('handsOn:')
				kernel.ScriptID(820, 3)._send('setPri:', -1, 'stopUpd:')
				global0._send('reset:', 1)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class searchEgo(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('put:', 44, 820)
				global91._send('say:', 1, 0, 13, 0, self)
			#end:case
			case 1:
				kernel.ScriptID(820, 3)._send('setCycle:', Beg, self)
			#end:case
			case 2:
				global105._send('number:', 822, 'loop:', 1, 'play:')
				kernel.ScriptID(820, 3)._send('setPri:', -1, 'stopUpd:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class beautyEntrance(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global91._send('say:', 1, 0, 1, 2, self)
			#end:case
			case 1:
				global0._send('loop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 2:
				global0._send('reset:', 7, 'posn:', 132, 149)
				cycles = 4
			#end:case
			case 3:
				global91._send('say:', 1, 0, 1, 3, self, 'oneOnly:', 0)
			#end:case
			case 4:
				cycles = 4
			#end:case
			case 5:
				kernel.ScriptID(820, 3)._send('setPri:', -1, 'stopUpd:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class afterClownHelpedEgoEscape(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global91._send('say:', 1, 0, 11, 0, self)
			#end:case
			case 1:
				kernel.ScriptID(820, 3)._send('setCycle:', Beg, self)
			#end:case
			case 2:
				global105._send('number:', 822, 'loop:', 1, 'play:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class jolloHelpsEgo(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global91._send('say:', 1, 0, 9, 1, self)
			#end:case
			case 1:
				client._send('cue:')
			#end:case
			case 2:
				seconds = 5
			#end:case
			case 3:
				global105._send('number:', 821, 'loop:', 1, 'play:', self)
			#end:case
			case 4:
				global105._send('number:', 821, 'loop:', 1, 'play:')
				kernel.ScriptID(820, 3)._send('setCycle:', End, self)
			#end:case
			case 5:
				global105._send('stop:')
				jollo._send(
					'ignoreActors:',
					'init:',
					'cel:', 0,
					'cycleSpeed:', 8,
					'setLoop:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 6:
				jollo._send('posn:', 87, 148, 'setLoop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 7:
				global91._send('say:', 1, 0, 9, 2, self)
			#end:case
			case 8:
				proc913_4(global0, jollo, self)
			#end:case
			case 9:
				cycles = 5
			#end:case
			case 10:
				global91._send('say:', 1, 0, 9, 3, self, 'oneOnly:', 0)
			#end:case
			case 11:
				jollo._send(
					'posn:', 100, 150,
					'setLoop:', 2,
					'cel:', 0,
					'cycleSpeed:', 12,
					'setCycle:', End, self
				)
			#end:case
			case 12:
				global0._send('reset:', 1, 'setPri:', 1, 'setMotion:', DPath, 93, 142, 34, 142, self)
			#end:case
			case 13:
				jollo._send('setCycle:', 0)
				global2._send('newRoom:', 710)
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

