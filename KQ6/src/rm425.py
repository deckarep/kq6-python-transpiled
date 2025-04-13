#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 425
import sci_sh
import kernel
import Main
import rLab
import n402
import n913
import PolyPath
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm425 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


@SCI.instance
class rm425(LabRoom):
	#property vars (may be empty)
	style = 10
	east = 400
	west = 411
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		proc402_1()
		super._send('init:', &rest)
		westDoor._send('addToPic:')
		westWing._send('addToPic:')
		kernel.ScriptID(30, 3)._send('init:')
		kernel.ScriptID(30, 0)._send('initCrypt:', 1)
		kernel.ScriptID(30, 6)._send('addToPic:')
		kernel.ScriptID(30, 10)._send('addToPic:')
		kernel.ScriptID(30, 8)._send('addToPic:')
		global2._send('setScript:', kernel.ScriptID(30, 1), self)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (not proc913_0(1)):
			match kernel.ScriptID(30, 0)._send('timesGenieHasAppeared:')
				case 0:
					genie._send('init:', 'setScript:', genieMeeting)
					kernel.ScriptID(30, 0)._send('geniePresent:', 1)
				#end:case
				case 1:
					genieMeeting._send('start:', 12)
					genie._send('init:', 'setScript:', genieMeeting)
					kernel.ScriptID(30, 0)._send('geniePresent:', 1)
				#end:case
				case 2:
					genieMeeting._send('start:', 22)
					genie._send('init:', 'setScript:', genieMeeting)
					kernel.ScriptID(30, 0)._send('geniePresent:', 1)
				#end:case
				else:
					kernel.ScriptID(30, 0)._send(
						'timesGenieHasAppeared:', (+
								kernel.ScriptID(30, 0)._send('timesGenieHasAppeared:')
								1
							)
					)
				#end:else
			#end:match
		#endif
	#end:method

	@classmethod
	def notify():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		westDoor._send('addToPic:')
		westWing._send('addToPic:')
		kernel.ScriptID(30, 6)._send('addToPic:')
		kernel.ScriptID(30, 10)._send('addToPic:')
		kernel.ScriptID(30, 8)._send('addToPic:')
		kernel.ScriptID(30, 3)._send('show:')
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.ScriptID(30, 0)._send('geniePresent:', 0)
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class genieMeeting(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				seconds = 3
			#end:case
			case 1:
				if (global0._send('x:') < 130):
					global0._send('setMotion:', PolyPath, 130, global0._send('y:'), self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 2:
				kernel.ScriptID(30, 0)._send(
					'timesGenieHasAppeared:', (+
							kernel.ScriptID(30, 0)._send('timesGenieHasAppeared:')
							1
						)
				)
				temp1 = kernel.GetAngle(global0._send('x:'), global0._send('y:'), 85, 158)
				global0._send('setHeading:', temp1)
				local0 = 1
				genie._send(
					'posn:', 26, 158,
					'init:',
					'setCycle:', Walk,
					'setMotion:', PolyPath, 85, 158, self
				)
			#end:case
			case 3:
				glint._send('init:')
			#end:case
			case 4:
				genie._send('view:', 442, 'setLoop:', 6, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 5:
				seconds = 2
			#end:case
			case 6:
				genie._send('setCycle:', Beg, self)
			#end:case
			case 7:
				global91._send('say:', 1, 0, 20, 0, self, 400)
			#end:case
			case 8:
				genie._send('view:', 442, 'setLoop:', 3, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 9:
				genie._send('view:', 442, 'setLoop:', 4, 'cel:', 0)
				cycles = 2
			#end:case
			case 10:
				genie._send(
					'view:', 364,
					'setLoop:', -1,
					'setCycle:', Walk,
					'setMotion:', PolyPath, 26, 164, self
				)
			#end:case
			case 11:
				global1._send('handsOn:')
				seconds = 30
			#end:case
			case 12:
				global1._send('handsOff:')
				seconds = 3
			#end:case
			case 13:
				genie._send('posn:', 26, 158)
				cycles = 2
			#end:case
			case 14:
				if (global0._send('x:') < 130):
					global0._send('setMotion:', PolyPath, 130, global0._send('y:'), self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 15:
				kernel.ScriptID(30, 0)._send(
					'timesGenieHasAppeared:', (+
							kernel.ScriptID(30, 0)._send('timesGenieHasAppeared:')
							1
						)
				)
				temp1 = kernel.GetAngle(global0._send('x:'), global0._send('y:'), 85, 158)
				global0._send('setHeading:', temp1)
				local0 = 1
				genie._send('setCycle:', Walk, 'setMotion:', PolyPath, 85, 158, self)
			#end:case
			case 16:
				glint._send('init:')
			#end:case
			case 17:
				genie._send('view:', 442, 'setLoop:', 6, 'cel:', 0)
				cycles = 10
			#end:case
			case 18:
				global91._send('say:', 1, 0, 21, 1, self, 400)
			#end:case
			case 19:
				genie._send(
					'view:', 442,
					'setLoop:', 2,
					'cel:', 0,
					'cycleSpeed:', 10,
					'setCycle:', End, self
				)
			#end:case
			case 20:
				genie._send(
					'view:', 364,
					'setLoop:', -1,
					'setCycle:', Walk,
					'setMotion:', PolyPath, 26, 164, self
				)
			#end:case
			case 21:
				global1._send('handsOn:')
				seconds = 30
			#end:case
			case 22:
				global1._send('handsOff:')
				seconds = 3
			#end:case
			case 23:
				genie._send('posn:', 26, 164)
				cycles = 2
			#end:case
			case 24:
				if (global0._send('x:') < 130):
					global0._send('setMotion:', PolyPath, 130, global0._send('y:'), self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 25:
				kernel.ScriptID(30, 0)._send(
					'timesGenieHasAppeared:', (+
							kernel.ScriptID(30, 0)._send('timesGenieHasAppeared:')
							1
						)
				)
				temp1 = kernel.GetAngle(global0._send('x:'), global0._send('y:'), 85, 158)
				global0._send('setHeading:', temp1)
				local0 = 1
				genie._send('setCycle:', Walk, 'setMotion:', PolyPath, 85, 158, self)
			#end:case
			case 26:
				glint._send('init:')
			#end:case
			case 27:
				genie._send('view:', 442, 'setLoop:', 6, 'cel:', 0)
				cycles = 10
			#end:case
			case 28:
				global91._send('say:', 1, 0, 22, 1, self, 400)
			#end:case
			case 29:
				genie._send(
					'view:', 442,
					'setLoop:', 5,
					'cel:', 0,
					'cycleSpeed:', 10,
					'setCycle:', End, self
				)
			#end:case
			case 30:
				genie._send('setCycle:', Beg, self)
			#end:case
			case 31:
				genie._send(
					'view:', 442,
					'setLoop:', 2,
					'cel:', 0,
					'cycleSpeed:', 10,
					'setCycle:', End, self
				)
			#end:case
			case 32:
				genie._send(
					'view:', 364,
					'setLoop:', -1,
					'cycleSpeed:', 6,
					'setCycle:', Walk,
					'setMotion:', PolyPath, 26, 164, self
				)
			#end:case
			case 33:
				global1._send('handsOn:')
				genie._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class backOut(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global0._send('setHeading:', 270, self)
			#end:case
			case 1:
				global0._send(
					'setLoop:', 1,
					'setCycle:', Walk,
					'setMotion:', MoveTo, (global0._send('x:') + 20), global0._send('y:'), self
				)
			#end:case
			case 2:
				global0._send('reset:', 1)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genie(Actor):
	#property vars (may be empty)
	modNum = 400
	view = 364
	
#end:class or instance

@SCI.instance
class glint(Prop):
	#property vars (may be empty)
	view = 902
	cycleSpeed = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send(
			'posn:', (genie._send('x:') + 3), (genie._send('y:') - 44),
			'setPri:', 15,
			'setCycle:', End, self
		)
		super._send('init:')
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (cel > 0):
			self._send('setCycle:', Beg, self)
		else:
			self._send('dispose:')
			genieMeeting._send('cue:')
		#endif
	#end:method

#end:class or instance

@SCI.instance
class exitSouth(View):
	#property vars (may be empty)
	x = 176
	y = 166
	noun = 6
	modNum = 400
	view = 408
	priority = 15
	signal = 16
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				global91._send('say:', 6, 1, 9, 0, 0, 400)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class westDoor(View):
	#property vars (may be empty)
	x = 63
	y = 155
	modNum = 400
	view = 405
	cel = 1
	priority = 11
	signal = 16400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('stopUpd:')
		westWing._send('init:', 'stopUpd:')
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				if local0:
					global91._send('say:', 14, 1, 25, 1, 0, 400)
				else:
					global91._send('say:', 4, 1, 0, 1, 0, 400)
				#endif
			#end:case
			case 5:
				if local0:
					global91._send('say:', 14, 5, 25, 1, 0, 400)
				else:
					global91._send('say:', 4, 5, 0, 1, 0, 400)
				#endif
			#end:case
			case 2:
				if local0:
					global91._send('say:', 14, 2, 25, 0, 0, 400)
				else:
					global91._send('say:', 4, 2, 0, 1, 0, 400)
				#endif
			#end:case
			else:
				global91._send('say:', 4, 0, 0, 1, 0, 400)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class westWing(View):
	#property vars (may be empty)
	x = 43
	y = 168
	noun = 14
	modNum = 400
	view = 405
	priority = 13
	signal = 16400
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		westDoor._send('doVerb:', param1, &rest)
	#end:method

#end:class or instance

