#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 802
import sci_sh
import kernel
import Main
import rm800
import Print
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	guardsScript = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None


@SCI.instance
class guardsScript(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		global1._send('handsOn:')
		super._send('dispose:')
		kernel.DisposeScript(802)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				global91._send(
					'say:', 6, 1, (24 + kernel.ScriptID(80, 0)._send('tstFlag:', 709, 32)), 1, self
				)
			#end:case
			case 1:
				local0 = global0._send('x:')
				local1 = global0._send('y:')
				global0._send(
					'normal:', 0,
					'view:', 802,
					'loop:', 0,
					'cel:', 0,
					'posn:', 297, 173,
					'setScale:', 0,
					'scaleX:', 128,
					'scaleY:', 128,
					'cycleSpeed:', 8,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				global5._send('eachElementDo:', #startUpd)
				cycles = 4
			#end:case
			case 3:
				global69._send('disable:')
				global5._send('eachElementDo:', #hide)
				global2._send('drawPic:', 802, 10)
				background._send('addToPic:')
				guard1._send('init:', 'stopUpd:')
				guard2._send('init:', 'stopUpd:')
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 32)):
					global1._send('givePoints:', 2)
					saladin._send('init:', 'stopUpd:')
				#endif
				cycles = 4
			#end:case
			case 4:
				global69._send('enable:')
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 32)):
					self._send('setScript:', overHearGuards, self)
				else:
					self._send('setScript:', guardsNotHere, self)
				#endif
			#end:case
			case 5:
				background._send('dispose:')
				guard1._send('dispose:', 'delete:')
				guard2._send('dispose:', 'delete:')
				saladin._send('dispose:', 'delete:')
				proc800_1()
				global0._send('setCycle:', Beg, self)
			#end:case
			case 6:
				global69._send('enable:')
				global0._send('posn:', local0, local1, 'reset:', 0)
				cycles = 2
			#end:case
			case 7:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class overHearGuards(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				kernel.ScriptID(80, 0)._send('setFlag:', 709, 32)
				cycles = 3
			#end:case
			case 1:
				global91._send('say:', 6, 1, 24, 2, self, 'oneOnly:', 0)
			#end:case
			case 2:
				Print._send(
					'font:', global22,
					'width:', 250,
					'posn:', 20, 139,
					'addText:', r"""He was speakin' to that door--black magic, is what I say! I heard him say 'Ali', but then Bay came up and started yappin at me.""",
					'modeless:', 1,
					'init:'
				)
				seconds = 10
			#end:case
			case 3:
				if global25:
					global25._send('dispose:')
				#endif
				cycles = 10
			#end:case
			case 4:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class guardsNotHere(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				cycles = 3
			#end:case
			case 1:
				global91._send('say:', 6, 1, 25, 2, self, 'oneOnly:', 0)
			#end:case
			case 2:
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class background(View):
	#property vars (may be empty)
	x = 77
	y = 54
	view = 803
	signal = 16400
	
#end:class or instance

@SCI.instance
class guard1(View):
	#property vars (may be empty)
	x = 144
	y = 125
	view = 724
	loop = 4
	cel = 3
	scaleSignal = 1
	scaleX = 147
	scaleY = 147
	
#end:class or instance

@SCI.instance
class guard2(View):
	#property vars (may be empty)
	x = 127
	y = 110
	view = 726
	loop = 4
	scaleSignal = 1
	scaleX = 121
	scaleY = 121
	
#end:class or instance

@SCI.instance
class saladin(View):
	#property vars (may be empty)
	x = 167
	y = 110
	view = 736
	loop = 4
	cel = 2
	scaleSignal = 1
	scaleX = 112
	scaleY = 112
	
#end:class or instance

