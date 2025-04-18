#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 900
import sci_sh
import kernel
import Main
import KQ6Print
import n913
import Game
import User
import System

# Public Export Declarations
SCI.public_exports(
	KQ6Room = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


@SCI.procedure
def localproc_0():
	(return
		match global11
			case 160: 160#end:case
			case 290: 34#end:case
			case 320: 64#end:case
			case 390: 134#end:case
			case 410: 154#end:case
			case 420: 164#end:case
			case 440: 184#end:case
			case 461: 5#end:case
			case 740: 228#end:case
			case 750: 238#end:case
			case 790: 22#end:case
			else: 0#end:else
		#end:match
	)
#end:procedure

class NewRoomCue(Cue):
	#property vars (may be empty)
	@classmethod
	def doit():
		global18._send('delete:', self)
		if global18._send('isEmpty:'):
			global18._send('dispose:')
			global18 = 0
		#endif
		cuee._send('newRoomCue:', register)
		self._send('dispose:')
	#end:method

#end:class or instance

class KQ6Room(Rm):
	#property vars (may be empty)
	horizon = 80
	walkOffEdge = 0
	autoLoad = 1
	
	@classmethod
	def translateVerb(param1 = None, *rest):
		if (not proc999_5(param1, 3, 1, 4, 2)):
			return 0
		else:
			return 0
		#endif
	#end:method

	@classmethod
	def init():
		local0 = 0
		super._send('init:', &rest)
		if ((global90 & 0x0001) and autoLoad):
			if (modNum == -1):
				modNum = global11
			#endif
			kernel.Load(143, modNum)
			kernel.Lock(143, modNum, 1)
		#endif
		if proc913_0(103):
			global1._send('handsOff:')
			proc913_2(103)
			self._send('setScript:', kernel.ScriptID(89, 0))
		#endif
	#end:method

	@classmethod
	def doit():
		if 
			(and
				(not script)
				(not walkOffEdge)
				temp0 = User._send('alterEgo:')._send('edgeHit:')
				(not self._send('edgeToRoom:', temp0))
			)
			User._send('alterEgo:')._send('edgeHit:', 0, 'setMotion:', 0)
			match temp0
				case 3:
					global0._send('y:', 188)
				#end:case
				case 1:
					global0._send('y:', (horizon + 1))
				#end:case
				case 4:
					global0._send('x:', 1)
				#end:case
				case 2:
					global0._send('x:', 318)
				#end:case
			#end:match
		#endif
		(cond
			case script:
				script._send('doit:')
			#end:case
			case local0: 0#end:case
			case temp0 = self._send('edgeToRoom:', User._send('alterEgo:')._send('edgeHit:')):
				self._send('newRoom:', temp0)
			#end:case
		)
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		if global25:
			global25._send('dispose:')
		#endif
		if (not local0):
			global1._send('handsOff:')
			kernel.Lock(143, modNum, 0)
			if global25:
				global25._send('dispose:')
			#endif
			if (not global18):
				global18 = Set._send('new:')
			#endif
			global18._send(
				'add:', NewRoomCue._send('new:')._send(
						'cuee:', self,
						'cuer:', self,
						'register:', param1,
						'yourself:'
					)
			)
			local0 = 1
		#endif
	#end:method

	@classmethod
	def newRoomCue():
		super._send('newRoom:', &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		if (modNum == -1):
			modNum = global11
		#endif
		(return
			if 
				(and
					(global66._send('doit:', param1) == -32768)
					kernel.Message(0, modNum, noun, 0, 0, 1)
				)
				global91._send('say:', noun, 0, 0, 0, 0, modNum)
				1
			else:
				super._send('doVerb:', param1)
			#endif
		)
	#end:method

	@classmethod
	def setScript(param1 = None, *rest):
		(cond
			case kernel.IsObject(param1):
				super._send('setScript:', param1, &rest)
			#end:case
			case (global0._send('view:') != 900):
				KQ6Print._send(
					'font:', global22,
					'posn:', -1, 10,
					'say:', 0, 7, 0, 16, 1, 0, 0, 0,
					'init:'
				)
			#end:case
			case 
				(or
					(global0._send('script:') and (param1 == 905))
					(self._send('script:') and (param1 == 905))
					((param1 == 905) and (global11 == 480) and global0._send('script:'))
				):
				KQ6Print._send(
					'font:', global22,
					'posn:', -1, 10,
					'say:', 0, 7, 0, 16, 1, 0, 0, 0,
					'init:'
				)
			#end:case
			case proc999_5(param1, 87, 85, 88, 90, 190, 915, 92, 93, 97, 96, 905):
				(cond
					case 
						proc999_5(global11, 160, 290, 320, 390, 410, 420, 440, 600, 630, 640, 650, 660, 670, 680, 690, 740, 750, 790, 461):
						(cond
							case 
								proc999_5(global11, 600, 630, 640, 650, 660, 670, 680, 690):
								KQ6Print._send(
									'font:', global22,
									'posn:', -1, 10,
									'say:', 0, 0, 0, 88, 1, 0, 0, 899,
									'init:'
								)
							#end:case
							case (global11 == 461):
								KQ6Print._send(
									'font:', global22,
									'posn:', -1, 10,
									'say:', 0, 0, 0, 5, 1, 0, 0, 899,
									'init:'
								)
							#end:case
							case temp0 = localproc_0():
								KQ6Print._send(
									'font:', global22,
									'posn:', -1, 10,
									'say:', 0, 0, 0, global11, 1, 0, 0, 899,
									'init:'
								)
							#end:case
						)
					#end:case
					case self._send('scriptCheck:', param1):
						super._send('setScript:', kernel.ScriptID(param1), &rest)
					#end:case
				)
			#end:case
			else:
				super._send('setScript:', kernel.ScriptID(param1), &rest)
			#end:else
		)
	#end:method

	@classmethod
	def scriptCheck():
		return 1
	#end:method

#end:class or instance

