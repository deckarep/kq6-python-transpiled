#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 822
import sci_sh
import kernel
import Main
import KQ6Print
import n913
import RandCycle
import PolyPath
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	boyGhostScript = 0,
	boyGhost = 1,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None
local3 = None
local4 = None


@SCI.procedure
def localproc_0():
	if kernel.ScriptID(820, 4)._send('cycler:'):
		kernel.ScriptID(820, 4)._send('setCycle:', 0, 'stopUpd:')
		kernel.ScriptID(820, 5)._send('setCycle:', 0, 'stopUpd:')
	#endif
#end:procedure

@SCI.procedure
def localproc_1():
	if (not kernel.ScriptID(820, 4)._send('cycler:')):
		kernel.ScriptID(820, 4)._send('startUpd:', 'setCycle:', Fwd)
		kernel.ScriptID(820, 5)._send('startUpd:', 'setCycle:', RandCycle)
	#endif
#end:procedure

@SCI.instance
class boyGhostScript(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		global1._send('handsOn:')
		super._send('dispose:')
		boyGhost._send('delete:')
		kernel.DisposeScript(822)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				kernel.Load(128, 763)
				cycles = 5
			#end:case
			case 1:
				global1._send('handsOff:')
				boyGhost._send(
					'view:', 763,
					'setLoop:', 0,
					'cel:', 7,
					'x:', 260,
					'y:', 118,
					'cycleSpeed:', 10,
					'show:',
					'setCycle:', End, self
				)
			#end:case
			case 2:
				boyGhost._send('setLoop:', 1, 'cel:', 7, 'posn:', 258, 117)
				self._send('setScript:', cryBaby, self)
			#end:case
			case 3:
				if global0._send('has:', 17):
					global1._send('handsOn:')
				else:
					state = 5
					cycles = 1
				#endif
			#end:case
			case 4:
				global1._send('handsOff:')
				global91._send('say:', 6, 2, 16, 1, self)
			#end:case
			case 5:
				localproc_1()
				cryBaby._send(
					'next:', showNonHanky._send('register:', 1, 'caller:', self, 'yourself:')
				)
			#end:case
			case 6:
				if (local0 or global0._send('has:', 17)):
					localproc_0()
					state = 7
					if local0:
						cycles = 3
					else:
						global1._send('handsOn:')
					#endif
				else:
					self._send('setScript:', noHanky, self)
				#endif
			#end:case
			case 7:
				global2._send('setScript:', kernel.ScriptID(820, 1))
			#end:case
			case 8:
				global1._send('handsOff:')
				kernel.ScriptID(80, 0)._send('setFlag:', 709, -32768)
				global91._send('say:', 6, 50, 0, 1, self)
			#end:case
			case 9:
				localproc_1()
				if (script == cryBaby):
					cryBaby._send('next:', showNonHanky._send('caller:', self, 'yourself:'))
				else:
					cycles = 1
				#endif
			#end:case
			case 10:
				global0._send(
					'normal:', 0,
					'setScale:', 0,
					'view:', 763,
					'setLoop:', 7,
					'cel:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 11:
				boyGhost._send('setCycle:', End, self)
			#end:case
			case 12:
				boyGhost._send('setLoop:', 3, 'cel:', 0, 'posn:', 229, 70, 'setCycle:', Fwd)
				seconds = 5
			#end:case
			case 13:
				localproc_0()
				cycles = 4
			#end:case
			case 14:
				kernel.ScriptID(820, 2)._send(
					'add:', -1, 6, 50, 0, 2,
					'add:', -1, 6, 50, 0, 3,
					'add:', -1, 6, 50, 0, 4,
					'init:', self
				)
			#end:case
			case 15:
				localproc_1()
				boyGhost._send('setCycle:', Beg, self)
			#end:case
			case 16:
				boyGhost._send('setLoop:', 4, 'cel:', 0, 'posn:', 155, 88, 'setCycle:', CT, 10, 1, self)
			#end:case
			case 17:
				global0._send('reset:', 0)
				boyGhost._send('setCycle:', End, self)
			#end:case
			case 18:
				boyGhost._send('setLoop:', 5, 'cel:', 0, 'posn:', 229, 88, 'setCycle:', End, self)
			#end:case
			case 19:
				boyGhost._send('hide:')
				seconds = 2
			#end:case
			case 20:
				boyGhost._send(
					'setLoop:', 6,
					'setPri:', (global0._send('priority:') - 1),
					'cel:', 0,
					'posn:', 85, 151,
					'show:',
					'setCycle:', End, self
				)
			#end:case
			case 21:
				global91._send('say:', 6, 50, 0, 5, self)
			#end:case
			case 22:
				global102._send('fadeTo:', 824, -1)
				boyGhost._send('setCycle:', 0, 'setMotion:', 0, 'dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class showNonHanky(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				localproc_1()
				if ((boyGhost._send('loop:') == 1) and boyGhost._send('cel:')):
					boyGhost._send('setCycle:', Beg, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				boyGhost._send('setLoop:', 2, 'cel:', 0, 'posn:', 241, 96, 'setCycle:', CT, 4, 1, self)
			#end:case
			case 2:
				if register:
					localproc_0()
					cycles = 4
				else:
					self._send('cue:')
				#endif
			#end:case
			case 3:
				if register:
					kernel.ScriptID(820, 2)._send(
						'add:', -1, 6, 2, 16, 2,
						'add:', -1, 6, 2, 16, 3,
						'init:', self
					)
				else:
					ticks = 1
				#endif
			#end:case
			case 4:
				if register:
					localproc_1()
				#endif
				if local0:
					self._send('dispose:')
				else:
					seconds = 3
				#endif
			#end:case
			case 5:
				boyGhost._send('setCycle:', CT, 0, -1, self)
			#end:case
			case 6:
				boyGhost._send('setLoop:', 1, 'cel:', 0, 'posn:', 258, 117)
				local1 = 0
				if (not register):
					global1._send('handsOn:')
					client._send('setScript:', cryBaby)
				else:
					register = 0
					client._send('setScript:', cryBaby, 0, 1)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class cryBaby(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		local2 = 30
		super._send('init:', &rest)
	#end:method

	@classmethod
	def doit():
		local3 = kernel.GetTime(1)
		if ((not local1) and (local4 != local3) and (global11 == global13)):
			local4 = local3
			if (local2 < 30):
				local2.post('++')
			#endif
		#endif
		super._send('doit:')
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		if (not next):
			match state = param1
				case 0:
					boyGhost._send('view:', 763, 'setLoop:', 1, 'x:', 258, 'y:', 117)
					if boyGhost._send('cel:'):
						boyGhost._send('setCycle:', Beg, self)
					else:
						cycles = 1
					#endif
				#end:case
				case 1:
					(cond
						case (register == -32768):
							global91._send('say:', 6, 0, 0, 2, self, 'oneOnly:', 0)
						#end:case
						case register:
							global91._send('say:', 6, 2, 16, 4, self)
						#end:case
						case (not local1):
							global91._send('say:', 1, 0, 4, 0, self)
						#end:case
						else:
							ticks = 1
						#end:else
					)
					register = 0
				#end:case
				case 2:
					localproc_1()
					if ((not local1) and (local2 == 30)):
						local2 = 0
					#endif
					if caller:
						caller._send('cue:')
						caller = 0
					#endif
					boyGhost._send('setCycle:', End, self)
				#end:case
				case 3:
					boyGhost._send('setCycle:', CT, 2, -1, self)
				#end:case
				case 4:
					if ((not local1) and (local2 == 30)):
						state = -1
						cycles = 1
					else:
						state = 1
						cycles = kernel.Random(1, 15)
					#endif
				#end:case
			#end:match
		else:
			self._send('dispose:')
		#endif
	#end:method

#end:class or instance

@SCI.instance
class noHanky(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				KQ6Print._send('posn:', -1, 10, 'say:', 0, 1, 0, 5, 1, 'init:', self)
			#end:case
			case 1:
				self._send('setScript:', justCryToMama, self, 2)
			#end:case
			case 2:
				localproc_0()
				cycles = 2
			#end:case
			case 3:
				kernel.ScriptID(820, 2)._send(
					'add:', -1, 1, 0, 5, 3, -1, 10,
					'add:', -1, 1, 0, 5, 4, -1, 10,
					'init:', self
				)
			#end:case
			case 4:
				localproc_1()
				self._send('setScript:', justCryToMama, self, 5)
			#end:case
			case 5:
				proc913_4(global0, kernel.ScriptID(820, 3), self)
			#end:case
			case 6:
				localproc_0()
				cycles = 4
			#end:case
			case 7:
				global91._send('say:', 1, 0, 5, 6, self)
			#end:case
			case 8:
				global91._send('say:', 1, 0, 5, 7, self)
			#end:case
			case 9:
				localproc_1()
				boyGhost._send('setLoop:', 0, 'cel:', 7, 'x:', 260, 'y:', 118, 'setCycle:', Beg, self)
			#end:case
			case 10:
				if (global0._send('x:') <= kernel.ScriptID(820, 3)._send('approachX:')):
					global0._send(
						'setMotion:', PolyPath, kernel.ScriptID(820, 3)._send('approachX:'), kernel.ScriptID(820, 3)._send(
								'approachY:'
							), self
					)
				else:
					state.post('++')
					cycles = 1
				#endif
			#end:case
			case 11:
				proc913_4(global0, kernel.ScriptID(820, 3), self)
			#end:case
			case 12:
				global0._send('setPri:', 9)
				global105._send('number:', 821, 'loop:', 1, 'play:')
				kernel.ScriptID(820, 3)._send('setPri:', 10, 'setCycle:', End, self)
			#end:case
			case 13:
				localproc_0()
				kernel.ScriptID(820, 3)._send('stopUpd:')
				cycles = 4
			#end:case
			case 14:
				global91._send('say:', 1, 0, 5, 8, self)
			#end:case
			case 15:
				global105._send('stop:')
				kernel.ScriptID(820, 2)._send(
					'add:', -1, 1, 0, 5, 9,
					'add:', -1, 1, 0, 5, 10,
					'add:', -1, 1, 0, 5, 11,
					'add:', -1, 1, 0, 5, 12,
					'add:', -1, 1, 0, 5, 13,
					'init:', self
				)
			#end:case
			case 16:
				localproc_1()
				kernel.ScriptID(820, 3)._send('setCycle:', Beg, self)
				global105._send('number:', 822, 'loop:', 1, 'play:')
			#end:case
			case 17:
				global105._send('stop:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class justCryToMama(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				boyGhost._send('view:', 763, 'setLoop:', 1, 'x:', 258, 'y:', 117)
				if boyGhost._send('cel:'):
					boyGhost._send('setCycle:', Beg, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				KQ6Print._send('posn:', -1, 10, 'say:', 0, 1, 0, 5, register, 'init:', self)
			#end:case
			case 2:
				boyGhost._send('setCycle:', End, self)
			#end:case
			case 3:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class boyGhost(Actor):
	#property vars (may be empty)
	x = 260
	y = 118
	noun = 6
	approachX = 98
	approachY = 149
	view = 763
	cycleSpeed = 8
	
	@classmethod
	def init():
		super._send('init:', &rest)
		self._send('hide:', 'setScript:', boyGhostScript, 'approachVerbs:', 50)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 2:
				if (boyGhostScript._send('state:') == 3):
					local1 = 1
					boyGhostScript._send('cue:')
				else:
					localproc_0()
					global91._send('say:', noun, param1, 17)
					localproc_1()
				#endif
			#end:case
			case 50:
				localproc_0()
				local0 = 1
				global0._send('put:', 17, 820)
				global1._send('givePoints:', 3)
				local1 = 1
				if (boyGhostScript._send('state:') == 3):
					boyGhostScript._send('cue:')
				else:
					boyGhostScript._send('changeState:', 8)
				#endif
			#end:case
			else:
				if (global66._send('doit:', param1) == -32768):
					localproc_0()
					global91._send('say:', noun, 0, 0, 1)
					local1 = 1
					if (script._send('script:') != showNonHanky):
						script._send('script:')._send('register:', -32768, 'next:', showNonHanky)
					#endif
				else:
					super._send('doVerb:', param1)
				#endif
			#end:else
		#end:match
	#end:method

#end:class or instance

