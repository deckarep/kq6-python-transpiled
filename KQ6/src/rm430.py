#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 430
import sci_sh
import kernel
import Main
import rLab
import n401
import PolyPath
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm430 = 0,
)

@SCI.instance
class rm430(LabRoom):
	#property vars (may be empty)
	east = 400
	
	@classmethod
	def init():
		proc401_3()
		super._send('init:', &rest)
		theCorpseNorth._send('init:', 'stopUpd:')
		if (global9._send('at:', 7)._send('owner:') == global11):
			theGlint._send('init:')
		#endif
		global2._send('setScript:', kernel.ScriptID(30, 1))
		kernel.ScriptID(30, 0)._send('initCrypt:', 4)
		kernel.ScriptID(30, 6)._send('addToPic:')
		kernel.ScriptID(30, 10)._send('addToPic:')
		kernel.ScriptID(30, 8)._send('addToPic:')
	#end:method

	@classmethod
	def notify():
		kernel.ScriptID(30, 6)._send('addToPic:')
		kernel.ScriptID(30, 10)._send('addToPic:')
		kernel.ScriptID(30, 8)._send('addToPic:')
		kernel.ScriptID(30, 3)._send('show:')
	#end:method

#end:class or instance

@SCI.instance
class theGlint(Prop):
	#property vars (may be empty)
	x = 132
	y = 111
	modNum = 400
	view = 902
	priority = 9
	signal = 16400
	cycleSpeed = 3
	
	@classmethod
	def init():
		theDeadMansCoin._send('init:')
		self._send('setScript:', glintCoinEyes)
		super._send('init:', &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				global0._send('setScript:', getCoins)
			#end:case
			else:
				kernel.ScriptID(30, 4)._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class theDeadMansCoin(Prop):
	#property vars (may be empty)
	x = 133
	y = 170
	z = 58
	noun = 13
	modNum = 400
	view = 431
	loop = 6
	priority = 8
	signal = 16400
	cycleSpeed = 15
	
	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 5:
				global0._send('setScript:', getCoins)
			#end:case
			case 1:
				global91._send('say:', 13, 1, 0, 0, 0, 400)
			#end:case
			else:
				kernel.ScriptID(30, 4)._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class theCorpseNorth(View):
	#property vars (may be empty)
	x = 132
	y = 122
	z = 10
	approachX = 132
	approachY = 112
	view = 400
	loop = 1
	cel = 2
	priority = 7
	signal = 16400
	
	@classmethod
	def init():
		if global5._send('contains:', theDeadMansCoin):
			self._send('noun:', 13)
		else:
			self._send('noun:', 8)
		#endif
		super._send('init:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 7:
				global91._send('say:', 13, 7, 0, 1, 0, 400)
			#end:case
			case 5:
				if global5._send('contains:', theDeadMansCoin):
					global0._send('setScript:', getCoins)
				else:
					global2._send('setScript:', kernel.ScriptID(30, 11), 0, self)
				#endif
			#end:case
			else:
				if global5._send('contains:', theDeadMansCoin):
					theDeadMansCoin._send('doVerb:', param1, &rest)
				else:
					kernel.ScriptID(30, 4)._send('doVerb:', param1, &rest)
				#endif
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getCoins(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 127, 149, self)
			#end:case
			case 1:
				global0._send(
					'view:', 431,
					'normal:', 0,
					'setLoop:', 5,
					'cel:', 0,
					'cycleSpeed:', 10,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				global0._send('setLoop:', 4, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 3:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 4:
				if (global9._send('at:', 7)._send('owner:') != global11):
					global91._send('say:', 8, 5, 0, 1, self, 400)
				else:
					global91._send('say:', 13, 5, 0, 1, self, 400)
				#endif
			#end:case
			case 5:
				global0._send('reset:', 3)
				if (global9._send('at:', 7)._send('owner:') == global11):
					global1._send('givePoints:', 1)
					global0._send('get:', 7)
					theDeadMansCoin._send('dispose:')
					theGlint._send('dispose:')
				#endif
				seconds = 1
			#end:case
			case 6:
				global1._send('handsOn:')
				global0._send('setHeading:', 180)
				theCorpseNorth._send('noun:', 8)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class glintCoinEyes(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				theGlint._send('setCycle:', Beg, self)
			#end:case
			case 1:
				theGlint._send('hide:')
				seconds = 10
			#end:case
			case 2:
				(state -= 3)
				theGlint._send('show:')
				self._send('cue:')
			#end:case
		#end:match
	#end:method

#end:class or instance

