#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 801
import sci_sh
import kernel
import Main
import rm800
import n913
import Scaler
import Feature
import StopWalk
import Motion
import User
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	cassimaScript = 0,
)

@SCI.instance
class cassimaScript(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		super._send('dispose:')
		kernel.DisposeScript(801)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		if 
			(and
				User._send('input:')
				(not param1._send('modifiers:'))
				(global69._send('curIcon:') == global69._send('at:', 2))
				(or
					(param1._send('type:') & 0x0001)
					((param1._send('type:') & 0x0004) and (param1._send('message:') == 13))
				)
				(not cassimaFeature._send('onMe:', param1))
			)
			global91._send('say:', 1, 1)
			param1._send('claimed:', 1)
		#endif
		param1._send('claimed:')
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global5._send('eachElementDo:', #startUpd)
				global10._send('eachElementDo:', #dispose)
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 710, 256)):
					global1._send('givePoints:', 1)
				#endif
				cycles = 2
			#end:case
			case 1:
				(cond
					case (not kernel.ScriptID(80, 0)._send('tstFlag:', 710, 256)):
						global91._send('say:', 1, 0, 7, 1, self)
					#end:case
					case kernel.ScriptID(80, 0)._send('tstFlag:', 711, 16384):
						global91._send('say:', 4, 1, 21, 1, self)
					#end:case
					else:
						global91._send('say:', 4, 1, 20, 1, self)
					#end:else
				)
			#end:case
			case 2:
				global0._send(
					'normal:', 0,
					'view:', 802,
					'loop:', 0,
					'cel:', 0,
					'setScale:', 0,
					'scaleX:', 128,
					'scaleY:', 128,
					'posn:', 267, 165,
					'cycleSpeed:', 8,
					'setCycle:', End, self
				)
			#end:case
			case 3:
				global69._send('disable:')
				global5._send('eachElementDo:', #hide)
				global2._send('drawPic:', 802, 10)
				chinkOverlay._send('addToPic:')
				background._send('addToPic:')
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 710, 256)):
					global102._send('fadeTo:', 703, -1)
					cassima._send('init:', 'stopUpd:')
				#endif
				global73._send('addToFront:', self)
				global72._send('addToFront:', self)
				cycles = 4
			#end:case
			case 4:
				global69._send('enable:')
				(cond
					case (not kernel.ScriptID(80, 0)._send('tstFlag:', 710, 256)):
						global32._send('add:', cassimaFeature)
						if proc999_5(global9._send('at:', 39)._send('owner:'), 140, 210):
							self._send(
								'setScript:', sentRing._send(
										'start:', -1,
										'next:', endDialog._send('caller:', self, 'yourself:'),
										'yourself:'
									), 0
							)
						else:
							self._send(
								'setScript:', noRing._send(
										'start:', -1,
										'next:', endDialog._send('caller:', self, 'yourself:'),
										'yourself:'
									), 0
							)
						#endif
						kernel.ScriptID(800, 2)._send(
							'add:', -1, 1, 0, 7, 2,
							'add:', convScr,
							'add:', -1, 1, 0, 7, 3,
							'add:', -1, 1, 0, 7, 4,
							'add:', -1, 1, 0, 7, 5,
							'add:', -1, 1, 0, 7, 6,
							'init:', script
						)
					#end:case
					case kernel.ScriptID(80, 0)._send('tstFlag:', 711, 16384):
						global91._send('say:', 4, 1, 21, 2, self, 'oneOnly:', 0)
					#end:case
					else:
						kernel.ScriptID(80, 0)._send('setFlag:', 711, 16384)
						global91._send('say:', 4, 1, 20, 2, self, 'oneOnly:', 0)
					#end:else
				)
			#end:case
			case 5:
				chinkOverlay._send('dispose:')
				background._send('dispose:')
				cassArm._send('dispose:', 'delete:')
				alexArm._send('dispose:', 'delete:')
				cassimaInset._send('dispose:', 'delete:')
				alexHead._send('dispose:', 'delete:')
				cassHead._send('dispose:', 'delete:')
				if (global102._send('number:') != 810):
					global102._send('fadeTo:', 810, -1)
				#endif
				global73._send('delete:', self)
				global72._send('delete:', self)
				proc800_1()
				cycles = 2
			#end:case
			case 6:
				global69._send('enable:')
				global0._send('setCycle:', Beg, self)
			#end:case
			case 7:
				global0._send('posn:', 228, 157, 'reset:', 0)
				cycles = 4
			#end:case
			case 8:
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 710, 256)):
					kernel.ScriptID(80, 0)._send('setFlag:', 710, 256)
					global91._send('say:', 1, 0, 13, 4, self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 9:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class sentRing(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global91._send('say:', 1, 0, 8, 1, self)
			#end:case
			case 1:
				self._send('setScript:', cassimaStands, self)
			#end:case
			case 2:
				self._send('setScript:', ringScr, self, 1)
			#end:case
			case 3:
				kernel.ScriptID(800, 2)._send('add:', -1, 1, 0, 8, 2, 'add:', -1, 1, 0, 8, 3, 'init:', self)
			#end:case
			case 4:
				self._send('setScript:', ringScr, self)
			#end:case
			case 5:
				kernel.ScriptID(800, 2)._send('add:', -1, 1, 0, 8, 4, 'add:', -1, 1, 0, 8, 5, 'init:', self)
			#end:case
			case 6:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class noRing(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				kernel.ScriptID(800, 2)._send('add:', -1, 1, 0, 9, 1, 'add:', -1, 1, 0, 9, 2, 'init:', self)
			#end:case
			case 1:
				self._send('setScript:', cassimaStands, self)
			#end:case
			case 2:
				self._send('setScript:', ringScr, self, 0)
			#end:case
			case 3:
				kernel.ScriptID(800, 2)._send('add:', -1, 1, 0, 9, 3, 'add:', -1, 1, 0, 9, 4, 'init:', self)
			#end:case
			case 4:
				self._send('setScript:', ringScr, self)
			#end:case
			case 5:
				kernel.ScriptID(800, 2)._send(
					'add:', -1, 1, 0, 9, 5,
					'add:', -1, 1, 0, 9, 6,
					'add:', -1, 1, 0, 9, 7,
					'add:', -1, 1, 0, 9, 8,
					'init:', self
				)
			#end:case
			case 6:
				global91._send('say:', 1, 0, 9, 9, self)
			#end:case
			case 7:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class endDialog(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		proc913_2(102)
		super._send('dispose:')
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				if kernel.ScriptID(80, 0)._send('tstFlag:', 711, 16):
					self._send('setScript:', watchedVizInStudy, self)
				else:
					self._send('setScript:', didn_tWatchVizInStudy, self)
				#endif
			#end:case
			case 1:
				global91._send('say:', 1, 0, 12, 0, self)
			#end:case
			case 2:
				global1._send('handsOn:')
				global69._send('disable:', 0, 1, 3)
				if (not global69._send('curInvIcon:')):
					global69._send('disable:', 4)
				#endif
				seconds = 11
			#end:case
			case 3:
				global1._send('handsOff:')
				global32._send('delete:', cassimaFeature)
				cassHead._send(
					'view:', 7833,
					'loop:', 5,
					'cel:', 0,
					'posn:', 133, 79,
					'show:',
					'cycleSpeed:', 2,
					'setCycle:', End, self
				)
			#end:case
			case 4:
				cycles = 30
			#end:case
			case 5:
				cassHead._send('cycleSpeed:', 6, 'setCycle:', Beg, self)
			#end:case
			case 6:
				cassHead._send('hide:')
				cycles = 2
			#end:case
			case 7:
				global91._send('say:', 1, 0, 13, 1, self)
			#end:case
			case 8:
				global91._send('say:', 1, 0, 13, 2, self)
			#end:case
			case 9:
				global91._send('say:', 1, 0, 13, 3, self)
			#end:case
			case 10:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class watchedVizInStudy(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				kernel.ScriptID(800, 2)._send(
					'add:', -1, 1, 0, 10, 1,
					'add:', -1, 1, 0, 10, 2,
					'add:', -1, 1, 0, 10, 3,
					'add:', -1, 1, 0, 10, 4,
					'add:', -1, 1, 0, 10, 5,
					'add:', -1, 1, 0, 10, 6,
					'add:', -1, 1, 0, 10, 7,
					'init:', self
				)
			#end:case
			case 1:
				self._send('setScript:', ringScr._send('start:', 8, 'yourself:'), self)
			#end:case
			case 2:
				global91._send('say:', 1, 0, 10, 8, self)
			#end:case
			case 3:
				self._send('setScript:', ringScr, self)
			#end:case
			case 4:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class didn_tWatchVizInStudy(Script):
	#property vars (may be empty)
	name = r"""didn'tWatchVizInStudy"""
	
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				kernel.ScriptID(800, 2)._send(
					'add:', -1, 1, 0, 11, 1,
					'add:', -1, 1, 0, 11, 2,
					'add:', -1, 1, 0, 11, 3,
					'init:', self
				)
			#end:case
			case 1:
				self._send('setScript:', ringScr._send('start:', 5, 'yourself:'), self)
			#end:case
			case 2:
				global91._send('say:', 1, 0, 11, 4, self)
			#end:case
			case 3:
				self._send('setScript:', ringScr, self)
			#end:case
			case 4:
				global91._send('say:', 1, 0, 11, 5, self, 'oneOnly:', 0)
			#end:case
			case 5:
				self._send('setScript:', ringScr, self)
			#end:case
			case 6:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class giveLetter(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				client._send('seconds:', 0)
				alexArm._send(
					'view:', 7832,
					'loop:', 5,
					'cel:', 0,
					'posn:', 173, 83,
					'show:',
					'setCycle:', CT, 1, 1, self
				)
			#end:case
			case 1:
				global91._send('say:', 5, 61, 22, 1, self)
			#end:case
			case 2:
				alexArm._send('cel:', 2)
				cassArm._send(
					'view:', 7832,
					'loop:', 4,
					'cel:', 0,
					'posn:', 113, 86,
					'setCycle:', CT, 2, 1, self
				)
			#end:case
			case 3:
				cassArm._send('setCycle:', End, self)
				alexArm._send('setCycle:', End)
			#end:case
			case 4:
				cassHead._send(
					'init:',
					'show:',
					'view:', 7832,
					'setPri:', 15,
					'loop:', 7,
					'cel:', 0,
					'x:', 137,
					'y:', 59
				)
				seconds = 5
			#end:case
			case 5:
				cassHead._send('view:', 7832, 'loop:', 8, 'cel:', 0, 'x:', 136, 'y:', 60)
				cycles = 40
			#end:case
			case 6:
				cassHead._send('hide:')
				cycles = 2
			#end:case
			case 7:
				global91._send('say:', 5, 61, 22, 2, self)
			#end:case
			case 8:
				cassArm._send('setCycle:', CT, 2, -1, self)
				alexArm._send('setCycle:', CT, 2, -1, self)
			#end:case
			case 9: 0#end:case
			case 10:
				alexArm._send('setCycle:', Beg, self)
				cassArm._send('setCycle:', Beg, self)
			#end:case
			case 11: 0#end:case
			case 12:
				alexArm._send('hide:')
				cassArm._send('loop:', 1, 'cel:', 0, 'stopUpd:')
				global1._send('handsOn:')
				global69._send('disable:', 0, 1, 3)
				if (not global69._send('curInvIcon:')):
					global69._send('disable:', 4)
				#endif
				client._send('seconds:', 8)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class giveDagger(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global0._send('put:', 8, 870)
				global1._send('givePoints:', 3)
				global1._send('handsOff:')
				client._send('seconds:', 0)
				alexArm._send(
					'view:', 7832,
					'loop:', 3,
					'cel:', 0,
					'x:', 172,
					'y:', 84,
					'show:',
					'setCycle:', CT, 1, 1, self
				)
			#end:case
			case 1:
				global91._send('say:', 5, 8, 0, 1, self)
			#end:case
			case 2:
				alexArm._send('cel:', 2)
				cassArm._send(
					'view:', 7832,
					'loop:', 2,
					'cel:', 0,
					'x:', 113,
					'y:', 86,
					'setCycle:', CT, 2, 1, self
				)
			#end:case
			case 3:
				cassArm._send('cel:', 3)
				alexArm._send('setCycle:', End, self)
			#end:case
			case 4:
				alexArm._send('hide:')
				cycles = 2
			#end:case
			case 5:
				global91._send('say:', 5, 8, 0, 2, self)
			#end:case
			case 6:
				cassArm._send('setCycle:', End, self)
			#end:case
			case 7:
				cassArm._send('loop:', 1, 'cel:', 0, 'stopUpd:')
				global1._send('handsOn:')
				global69._send('disable:', 0, 1, 3)
				if (not global69._send('curInvIcon:')):
					global69._send('disable:', 4)
				#endif
				client._send('seconds:', 8)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class convScr(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		start = (state + 1)
		super._send('dispose:')
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cassima._send('cycleSpeed:', 8, 'setCycle:', End, self)
			#end:case
			case 1:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class cassimaStands(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cassima._send(
					'setLoop:', 1,
					'cel:', 0,
					'posn:', 140, 108,
					'setPri:', 13,
					'setCycle:', End, self
				)
			#end:case
			case 1:
				cassima._send(
					'setLoop:', -1,
					'setScale:', Scaler, 150, 100, 171, 108,
					'view:', 784,
					'setCycle:', StopWalk, -1
				)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class ringScr(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		start = (state + 1)
		register = 0
		super._send('dispose:')
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cassima._send('setMotion:', MoveTo, 140, 146, self)
			#end:case
			case 1:
				if (not register):
					self._send('dispose:')
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				cassima._send('setMotion:', MoveTo, 136, 185, self)
			#end:case
			case 3:
				cassimaInset._send('addToPic:')
				cassima._send('dispose:')
				cassArm._send('init:', 'stopUpd:')
				alexArm._send('init:', 'hide:')
				proc913_1(102)
				cycles = 4
			#end:case
			case 4:
				kernel.UnLoad(128, 783)
				kernel.UnLoad(128, 784)
				self._send('dispose:')
			#end:case
			case 5:
				cassHead._send('init:', 'view:', 7833, 'loop:', 1, 'cel:', 0)
				seconds = 3
			#end:case
			case 6:
				cassHead._send('hide:', 'view:', 7832)
				cycles = 3
			#end:case
			case 7:
				self._send('dispose:')
			#end:case
			case 8:
				alexArm._send(
					'view:', 7833,
					'loop:', 0,
					'cel:', 0,
					'posn:', 172, 84,
					'show:',
					'cycleSpeed:', 0,
					'setCycle:', End, self
				)
			#end:case
			case 9:
				self._send('dispose:')
			#end:case
			case 10:
				alexArm._send('cel:', 1, 'cycleSpeed:', 8, 'setCycle:', Beg, self)
			#end:case
			case 11:
				alexArm._send('view:', 7832, 'hide:')
				cycles = 2
			#end:case
			case 12:
				state = 0
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class chinkOverlay(View):
	#property vars (may be empty)
	x = 251
	y = 118
	view = 7801
	priority = 14
	signal = 16400
	
#end:class or instance

@SCI.instance
class background(View):
	#property vars (may be empty)
	x = 175
	y = 82
	view = 780
	signal = 24592
	
#end:class or instance

@SCI.instance
class cassima(Actor):
	#property vars (may be empty)
	x = 155
	y = 103
	view = 783
	signal = 24576
	illegalBits = 0
	
#end:class or instance

@SCI.instance
class cassimaInset(View):
	#property vars (may be empty)
	x = 161
	y = 190
	z = 101
	sightAngle = 180
	view = 7832
	priority = 14
	signal = 16
	
	@classmethod
	def doVerb(param1 = None, *rest):
		if ((global2._send('script:') == endDialog) and (endDialog._send('seconds:') < 2)):
			endDialog._send('seconds:', 4)
		#endif
		match param1
			case 8:
				endDialog._send('setScript:', giveDagger)
			#end:case
			case 61:
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 710, 8)):
					kernel.ScriptID(80, 0)._send('setFlag:', 710, 8)
					endDialog._send('setScript:', giveLetter)
				else:
					global91._send('say:', 5, param1, 28)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class cassArm(Prop):
	#property vars (may be empty)
	x = 113
	y = 86
	view = 7832
	loop = 1
	priority = 15
	signal = 16400
	cycleSpeed = 8
	
#end:class or instance

@SCI.instance
class alexArm(Prop):
	#property vars (may be empty)
	x = 113
	y = 86
	view = 7832
	loop = 3
	priority = 15
	signal = 16400
	cycleSpeed = 8
	
#end:class or instance

@SCI.instance
class alexHead(View):
	#property vars (may be empty)
	x = 194
	y = 68
	view = 7832
	loop = 6
	priority = 15
	signal = 16
	
#end:class or instance

@SCI.instance
class cassHead(Prop):
	#property vars (may be empty)
	x = 137
	y = 59
	view = 7832
	loop = 7
	priority = 15
	signal = 16400
	
#end:class or instance

@SCI.instance
class cassimaFeature(Feature):
	#property vars (may be empty)
	x = 121
	y = 191
	noun = 5
	nsTop = 46
	nsLeft = 92
	nsBottom = 135
	nsRight = 151
	sightAngle = 180
	
	@classmethod
	def doVerb(param1 = None, *rest):
		if proc999_5(param1, 8, 61):
			cassimaInset._send('doVerb:', param1)
		else:
			super._send('doVerb:', param1)
		#endif
	#end:method

#end:class or instance

