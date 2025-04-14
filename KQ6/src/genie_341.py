#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 341
import sci_sh
import kernel
import Main
import rSacred
import n913
import Conversation
import PolyPath
import Polygon
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	proc341_0 = 0,
	proc341_1 = 1,
	proc341_2 = 2,
	proc341_3 = 3,
	genie = 4,
	poofAwayScript = 5,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = None
local2 = None


@SCI.procedure
def proc341_0():
	genie._send('init:')
#end:procedure

@SCI.procedure
def proc341_1():
	genie._send('setScript:', genieTrap)
#end:procedure

@SCI.procedure
def proc341_2():
	genie._send('dispose:')
#end:procedure

@SCI.procedure
def proc341_3():
	genie._send('addToPic:')
#end:procedure

@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class geniePoly(Polygon):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class eyeGlint(Prop):
	#property vars (may be empty)
	view = 902
	cycleSpeed = 15
	
	@classmethod
	def init():
		self._send('setPri:', 15, 'setCycle:', End, self)
		super._send('init:')
	#end:method

	@classmethod
	def cue():
		if (cel == 2):
			self._send('setPri:', 15, 'setCycle:', Beg, self)
		else:
			genie._send('script:')._send('cue:')
			self._send('dispose:')
		#endif
	#end:method

#end:class or instance

@SCI.instance
class genie(Actor):
	#property vars (may be empty)
	x = 260
	y = 116
	noun = 8
	modNum = 340
	yStep = 8
	view = 334
	signal = 24576
	xStep = 12
	
	@classmethod
	def init():
		global2._send(
			'addObstacle:', geniePoly._send(
					'type:', 2,
					'init:', 279, 120, 239, 120, 234, 116, 239, 113, 279, 113, 283, 116,
					'yourself:'
				)
		)
		rSacred._send('geniePresent:', 1)
		super._send('init:')
	#end:method

	@classmethod
	def dispose():
		global104._send('fade:', 0, 6, 6)
		eyeGlint._send('dispose:')
		global2._send('obstacles:')._send('delete:', geniePoly)
		geniePoly._send('dispose:')
		rSacred._send('geniePresent:', 0)
		super._send('dispose:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		match param1
			case 2:
				if local0:
					myConv._send('add:', 340, 8, 2, 26, 1, 'add:', 340, 8, 2, 26, 2, 'init:')
				else:
					local0 = 1
					myConv._send('add:', 340, 8, 2, 25, 1, 'add:', 340, 8, 2, 25, 2, 'init:')
				#endif
			#end:case
			case 63:
				global0._send('setScript:', 0)
				global1._send('handsOff:')
				global2._send('setScript:', genieAsMintJunkie)
			#end:case
			case 43:
				global91._send('say:', noun, param1, 0, 0)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class poofAwayScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				genie._send('setScript:', 0, 'setCycle:', 0, 'setMotion:', 0)
				eyeGlint._send('dispose:')
				cycles = 1
			#end:case
			case 1:
				global91._send('say:', 1, 0, 7, 1, self, 340)
			#end:case
			case 2:
				global105._send('number:', 943, 'setLoop:', 1, 'play:')
				genie._send('setLoop:', 2, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 3:
				global91._send('say:', 1, 0, 7, 2, self, 340)
			#end:case
			case 4:
				rSacred._send('geniePresent:', 0)
				self._send('dispose:')
				genie._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genieAsMintJunkie(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				global1._send('handsOff:')
				if (global0._send('x:') > genie._send('x:')):
					global0._send('setMotion:', PolyPath, 249, 118, self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 1:
				global0._send('setHeading:', 45)
				cycles = 8
			#end:case
			case 2:
				myConv._send('add:', 340, 8, 63, 0, 1, 'add:', 340, 8, 63, 0, 2, 'init:', self)
			#end:case
			case 3:
				genie._send(
					'setLoop:', 3,
					'posn:', (genie._send('x:') - 1), (genie._send('y:') - 25),
					'setCycle:', End, self
				)
			#end:case
			case 4:
				genie._send(
					'setCycle:', 0,
					'setMotion:', MoveTo, (global0._send('x:') + 12), (-
							global0._send('y:')
							27
						), self
				)
			#end:case
			case 5:
				genie._send('setCycle:', Beg, self)
			#end:case
			case 6:
				genie._send(
					'setLoop:', 5,
					'cel:', 0,
					'posn:', (global0._send('x:') + 13), (global0._send('y:') - 3)
				)
				global0._send(
					'view:', 334,
					'normal:', 0,
					'setLoop:', 6,
					'cel:', 0,
					'setCycle:', CT, 2, 1, self
				)
			#end:case
			case 7:
				genie._send('setCycle:', End, self)
				global0._send('cel:', 3)
			#end:case
			case 8:
				myConv._send('add:', 340, 8, 63, 0, 3, 'add:', 340, 8, 63, 0, 4, 'init:', self)
			#end:case
			case 9:
				global0._send('reset:', 6, 'put:', 23, 340)
				global105._send('number:', 943, 'setLoop:', 1, 'play:')
				genie._send(
					'setLoop:', 2,
					'cel:', 0,
					'posn:', (global0._send('x:') + 13), (global0._send('y:') - 2),
					'setCycle:', End, self
				)
			#end:case
			case 10:
				local1 = 1
				genie._send('dispose:')
				cycles = 4
			#end:case
			case 11:
				global91._send('say:', 8, 63, 0, 5, self, 340)
			#end:case
			case 12:
				global1._send('handsOn:')
				self._send('dispose:')
				kernel.DisposeScript(341)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class genieTrap(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		match state = param1
			case 0:
				proc913_1(4)
				seconds = 2
				global0._send('setHeading:', 30)
			#end:case
			case 1:
				eyeGlint._send('posn:', genie._send('x:'), (genie._send('y:') - 44), 'init:')
			#end:case
			case 2:
				cycles = 2
			#end:case
			case 3:
				global91._send('say:', 1, 0, 1, 2, 0, 340)
				seconds = 1
			#end:case
			case 4:
				genie._send('setLoop:', 1, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 5:
				genie._send('setCycle:', Beg, self)
			#end:case
			case 6:
				genie._send('setCycle:', End, self)
			#end:case
			case 7:
				genie._send('setCycle:', Beg, self)
			#end:case
			case 8:
				seconds = 2
			#end:case
			case 9:
				global91._send('say:', 1, 0, 1, 3, 0, 340)
				seconds = 1
			#end:case
			case 10:
				seconds = 2
			#end:case
			case 11:
				genie._send('setLoop:', 1, 'cel:', 0)
				cycles = 6
			#end:case
			case 12:
				genie._send('setLoop:', 5, 'cel:', 0, 'setCycle:', End, self)
				global105._send('number:', 348, 'setLoop:', 1, 'play:')
			#end:case
			case 13:
				genie._send('setCycle:', Beg, self)
			#end:case
			case 14:
				genie._send('setLoop:', 0, 'posn:', 260, 116)
				seconds = 2
			#end:case
			case 15:
				eyeGlint._send('posn:', genie._send('x:'), (genie._send('y:') - 44), 'init:')
			#end:case
			case 16:
				cycles = 2
			#end:case
			case 17:
				genie._send('setLoop:', 3, 'cel:', 0, 'posn:', 259, 89, 'setCycle:', End, self)
			#end:case
			case 18:
				global105._send('number:', 347, 'setLoop:', -1, 'play:')
				genie._send('setCycle:', Beg, self)
			#end:case
			case 19:
				genie._send(
					'setLoop:', 4,
					'cel:', 0,
					'setCycle:', Fwd,
					'setMotion:', MoveTo, (genie._send('x:') - 30), (genie._send('y:') - 20), self
				)
			#end:case
			case 20:
				genie._send(
					'setMotion:', MoveTo, (genie._send('x:') + 60), (genie._send('y:') - 20), self
				)
			#end:case
			case 21:
				genie._send(
					'setMotion:', MoveTo, (genie._send('x:') - 60), (genie._send('y:') - 20), self
				)
			#end:case
			case 22:
				genie._send(
					'setMotion:', MoveTo, (genie._send('x:') + 60), (genie._send('y:') - 20), self
				)
			#end:case
			case 23:
				genie._send(
					'setMotion:', MoveTo, (genie._send('x:') - 60), (genie._send('y:') + 20), self
				)
			#end:case
			case 24:
				genie._send(
					'setMotion:', MoveTo, (genie._send('x:') + 60), (genie._send('y:') + 20), self
				)
			#end:case
			case 25:
				genie._send(
					'setMotion:', MoveTo, (genie._send('x:') - 30), (genie._send('y:') + 20), self
				)
			#end:case
			case 26:
				genie._send('setLoop:', 3, 'cel:', 3, 'posn:', 259, 89, 'setCycle:', Beg, self)
			#end:case
			case 27:
				global105._send('stop:')
				genie._send('setLoop:', 0, 'posn:', 260, 116)
				seconds = 2
			#end:case
			case 28:
				eyeGlint._send('posn:', genie._send('x:'), (genie._send('y:') - 44), 'init:')
			#end:case
			case 29:
				cycles = 2
			#end:case
			case 30:
				global1._send('handsOn:')
				global91._send('say:', 1, 0, 1, 4, 0, 340)
				seconds = 1
			#end:case
			case 31:
				eyeGlint._send('posn:', genie._send('x:'), (genie._send('y:') - 44), 'init:')
			#end:case
			case 32:
				seconds = 10
			#end:case
			case 33:
				if ((not global2._send('script:')) and (not global25)):
					global91._send('say:', 1, 0, 5, 1, 0, 340)
					seconds = 1
				else:
					self._send('cue:')
				#endif
			#end:case
			case 34:
				eyeGlint._send('posn:', genie._send('x:'), (genie._send('y:') - 44), 'init:')
			#end:case
			case 35:
				seconds = 10
			#end:case
			case 36:
				if ((not global2._send('script:')) and (not global25)):
					global91._send('say:', 1, 0, 6, 1, 0, 340)
					seconds = 1
				else:
					self._send('cue:')
				#endif
			#end:case
			case 37:
				eyeGlint._send('posn:', genie._send('x:'), (genie._send('y:') - 44), 'init:')
			#end:case
			case 38:
				seconds = 10
			#end:case
			case 39:
				if ((not global2._send('script:')) and (not global25)):
					global91._send('say:', 1, 0, 7, 1, 0, 340)
					seconds = 1
				else:
					self._send('cue:')
				#endif
			#end:case
			case 40:
				global1._send('handsOff:')
				if (not global2._send('script:')):
					proc913_4(global0, genie)
				#endif
				global105._send('number:', 943, 'setLoop:', 1, 'play:')
				genie._send('setLoop:', 2, 'cel:', 0, 'setCycle:', End, self)
			#end:case
			case 41:
				global91._send('say:', 1, 0, 7, 2, 0, 340)
				seconds = 1
			#end:case
			case 42:
				global1._send('handsOn:')
				genie._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

