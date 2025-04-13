#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 770
import sci_sh
import kernel
import Main
import rgCastle
import n913
import Conversation
import Scaler
import Polygon
import Feature
import LoadMany
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm770 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None


@SCI.procedure
def localproc_0():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	if 
		(and
			kernel.ScriptID(80, 0)._send('tstFlag:', 710, 4096)
			kernel.ScriptID(80, 0)._send('tstFlag:', 710, 8192)
			kernel.ScriptID(80, 0)._send('tstFlag:', 710, 16384)
			kernel.ScriptID(80, 0)._send('tstFlag:', 710, -32768)
			(not kernel.ScriptID(80, 0)._send('tstFlag:', 710, 16))
		)
		kernel.ScriptID(80, 0)._send('setFlag:', 710, 16)
		return 1
	else:
		return 0
	#endif
#end:procedure

class StolenItem(Feature):
	#property vars (may be empty)
	look1stSeq = 0
	handLookedMsg = 0
	flagNum = 0
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		x = param1._send('x:')
		return super._send('onMe:', param1)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				roomConv._send(
					'add:', -1, noun, param1, (+
							look1stSeq
							kernel.ScriptID(80, 0)._send('tstFlag:', 710, flagNum)
						)
				)
				kernel.ScriptID(80, 0)._send('setFlag:', 710, flagNum)
				if localproc_0():
					global1._send('givePoints:', 2)
					roomConv._send('add:', -1, 1, 0, 1)
				#endif
				roomConv._send('init:')
			#end:case
			case 5:
				global91._send(
					'say:', noun, param1, (+
							handLookedMsg
							(not kernel.ScriptID(80, 0)._send('tstFlag:', 710, flagNum))
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
class rm770(CastleRoom):
	#property vars (may be empty)
	noun = 3
	picture = 770
	style = 10
	south = 710
	vanishingX = 110
	vanishingY = 98
	minScaleSize = 55
	maxScaleSize = 107
	minScaleY = 126
	maxScaleY = 154
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		proc958_0(128, 771, 770)
		kernel.ScriptID(81, 0)._send('clrFlag:', 709, 1, 2)
		if global5._send('contains:', kernel.ScriptID(80, 5)):
			kernel.ScriptID(80, 5)._send('dispose:')
		#endif
		if global5._send('contains:', kernel.ScriptID(80, 6)):
			kernel.ScriptID(80, 6)._send('dispose:')
		#endif
		self._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 15, 179, 6, 189, 0, 189, 0, -10, 319, -10, 319, 189, 307, 189, 285, 179, 263, 179, 213, 151, 225, 151, 202, 141, 187, 141, 163, 128, 82, 128, 71, 139, 55, 139, 48, 148, 66, 148, 37, 179,
					'yourself:'
				), Polygon._send('new:')._send(
					'type:', 2,
					'init:', 172, 144, 160, 150, 132, 153, 106, 151, 90, 143, 106, 137, 155, 137,
					'yourself:'
				)
		)
		global32._send(
			'add:', coatOfArms, goldenFleece, oakTree, singingStone, table, roomFeatures, skyLight,
			'eachElementDo:', #init
		)
		if kernel.ScriptID(80, 0)._send('tstFlag:', 711, 512):
			kernel.ScriptID(80, 0)._send('weddingRemind:', 0)
		#endif
		if (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 8)):
			drape._send('cel:', 0, 'posn:', 136, 145, 14, 'init:', 'stopUpd:')
		else:
			drape._send('cel:', 1, 'posn:', 95, 141, 0, 'init:', 'stopUpd:')
		#endif
		global0._send(
			'init:',
			'posn:', 148, 184,
			'setScale:', Scaler, maxScaleSize, minScaleSize, maxScaleY, minScaleY
		)
		global0._send('scaler:')._send('doit:')
		if (not proc913_1(85)):
			global1._send('givePoints:', 2)
		#endif
		global102._send('fadeTo:', 770, -1)
		self._send('setScript:', entryScript)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if kernel.ScriptID(80, 0)._send('tstFlag:', 711, 512):
			kernel.ScriptID(80, 0)._send('weddingRemind:', 1)
		#endif
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class removeDrape(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 710, 1024)):
					kernel.ScriptID(80, 0)._send('setFlag:', 710, 1024)
					global91._send('say:', 4, 5, 6, 0, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				global0._send(
					'normal:', 0,
					'setScale:', 0,
					'view:', 771,
					'loop:', 0,
					'cel:', 0,
					'cycleSpeed:', 10,
					'posn:', 105, 148,
					'setCycle:', End, self
				)
			#end:case
			case 2:
				seconds = 3
			#end:case
			case 3:
				drape._send('hide:')
				global0._send('loop:', 1, 'cel:', 0, 'posn:', 104, 148, 'setCycle:', End, self)
			#end:case
			case 4:
				drape._send('posn:', 95, 141, 0, 'cel:', 1, 'show:', 'stopUpd:')
				global0._send('loop:', 2, 'cel:', 0, 'posn:', 92, 150, 'setCycle:', End, self)
			#end:case
			case 5:
				seconds = 2
			#end:case
			case 6:
				global0._send('setCycle:', Beg, self)
			#end:case
			case 7:
				global0._send('posn:', drape._send('approachX:'), drape._send('approachY:'), 'reset:', 6)
				kernel.ScriptID(80, 0)._send('setFlag:', 709, 8)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class replaceDrape(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				kernel.ScriptID(80, 0)._send('clrFlag:', 709, 8)
				drape._send('hide:', 'posn:', 136, 145, 14, 'cel:', 0)
				global0._send(
					'normal:', 0,
					'view:', 771,
					'setScale:', 0,
					'loop:', 3,
					'cel:', 0,
					'cycleSpeed:', 8,
					'posn:', 104, 148,
					'setCycle:', End, self
				)
			#end:case
			case 1:
				drape._send('show:', 'stopUpd:')
				global0._send('posn:', drape._send('approachX:'), drape._send('approachY:'), 'reset:', 6)
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class drape(Prop):
	#property vars (may be empty)
	x = 136
	y = 145
	z = 14
	noun = 4
	approachX = 95
	approachY = 148
	view = 770
	priority = 11
	signal = 4112
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('approachVerbs:', 5, 'ignoreActors:', 1)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 8)):
					roomConv._send('add:', -1, noun, param1, 2)
				else:
					roomConv._send('add:', -1, noun, param1, 3)
				#endif
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 256)):
					kernel.ScriptID(80, 0)._send('setFlag:', 709, 256)
					roomConv._send('add:', -1, noun, param1, 4)
				#endif
				roomConv._send('init:')
			#end:case
			case 5:
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 709, 8)):
					global2._send('setScript:', removeDrape)
				else:
					global2._send('setScript:', replaceDrape)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class coatOfArms(StolenItem):
	#property vars (may be empty)
	y = 144
	noun = 8
	onMeCheck = 2
	look1stSeq = 19
	handLookedMsg = 21
	flagNum = 4096
	
#end:class or instance

@SCI.instance
class goldenFleece(StolenItem):
	#property vars (may be empty)
	y = 144
	noun = 6
	onMeCheck = 4
	look1stSeq = 11
	handLookedMsg = 13
	flagNum = 8192
	
#end:class or instance

@SCI.instance
class oakTree(StolenItem):
	#property vars (may be empty)
	y = 144
	noun = 5
	onMeCheck = 8
	look1stSeq = 7
	handLookedMsg = 9
	flagNum = 16384
	
#end:class or instance

@SCI.instance
class singingStone(StolenItem):
	#property vars (may be empty)
	y = 144
	noun = 7
	onMeCheck = 16
	look1stSeq = 15
	handLookedMsg = 17
	flagNum = -32768
	
#end:class or instance

@SCI.instance
class table(Feature):
	#property vars (may be empty)
	y = 144
	noun = 9
	onMeCheck = 32
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		x = param1._send('x:')
		return super._send('onMe:', param1)
	#end:method

#end:class or instance

@SCI.instance
class skyLight(Feature):
	#property vars (may be empty)
	x = 160
	y = 144
	noun = 14
	onMeCheck = 1024
	
#end:class or instance

@SCI.instance
class roomFeatures(Feature):
	#property vars (may be empty)
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = kernel.OnControl(4, param1._send('x:'), param1._send('y:'))
		x = param1._send('x:')
		(return
			(or
				((temp0 & 0x0200) and noun = 11 and y = 161)
				((temp0 & 0x0100) and noun = 13 and y = 177)
				(and
					(temp0 & 0x0080)
					noun = 10
					(((x > 190) and y = 145) or y = 125)
				)
				((temp0 & 0x0040) and noun = 12 and y = 138)
				0
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class roomConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class entryScript(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				cycles = 15
			#end:case
			case 1:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

