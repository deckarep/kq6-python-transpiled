#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 415
import sci_sh
import kernel
import Main
import rLab
import PolyPath
import Polygon
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm415 = 0,
)

@SCI.instance
class rm415(LabRoom):
	#property vars (may be empty)
	south = 400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (global9._send('at:', 11)._send('owner:') == global11):
			theSkull._send('init:', 'stopUpd:')
			global2._send(
				'addObstacle:', Polygon._send('new:')._send(
						'type:', 2,
						'init:', 0, 189, 0, 0, 319, 0, 319, 189, 190, 189, 190, 185, 276, 185, 264, 172, 261, 178, 237, 178, 198, 155, 206, 152, 240, 151, 205, 151, 190, 143, 117, 143, 117, 153, 90, 164, 72, 157, 38, 185, 130, 185, 130, 189,
						'yourself:'
					), Polygon._send('new:')._send(
						'type:', 2,
						'init:', 196, 152, 180, 152, 176, 149, 181, 146, 195, 146, 200, 149,
						'yourself:'
					)
			)
		else:
			global2._send(
				'addObstacle:', Polygon._send('new:')._send(
						'type:', 2,
						'init:', 0, 189, 0, 0, 319, 0, 319, 189, 190, 189, 190, 185, 276, 185, 264, 172, 261, 178, 237, 178, 198, 155, 206, 152, 240, 151, 205, 151, 190, 143, 117, 143, 117, 153, 90, 164, 72, 157, 38, 185, 130, 185, 130, 189,
						'yourself:'
					)
			)
		#endif
		skelton1._send('init:', 'stopUpd:')
		skelton2._send('init:', 'stopUpd:')
		skelton3._send('init:', 'stopUpd:')
		super._send('init:', &rest)
		global2._send('setScript:', kernel.ScriptID(30, 1))
		kernel.ScriptID(30, 0)._send('initCrypt:', 1)
	#end:method

	@classmethod
	def notify():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.ScriptID(30, 3)._send('show:')
	#end:method

#end:class or instance

@SCI.instance
class theSkull(View):
	#property vars (may be empty)
	x = 189
	y = 151
	noun = 12
	modNum = 400
	view = 403
	loop = 6
	cel = 3
	signal = 16384
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global2._send('setScript:', getSkull)
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class skelton1(View):
	#property vars (may be empty)
	x = 87
	y = 138
	noun = 10
	modNum = 400
	view = 403
	loop = 6
	signal = 16384
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 0):
			global91._send('say:', 10, 5, 0, 1)
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class skelton2(View):
	#property vars (may be empty)
	x = 239
	y = 163
	noun = 10
	modNum = 400
	view = 403
	loop = 6
	cel = 1
	signal = 16384
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 0):
			global91._send('say:', 10, 5, 0, 1)
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class skelton3(View):
	#property vars (may be empty)
	x = 227
	y = 143
	noun = 10
	modNum = 400
	view = 403
	loop = 6
	cel = 2
	signal = 16384
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 0):
			global91._send('say:', 10, 5, 0, 1)
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class getSkull(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 204, 151, self)
			#end:case
			case 1:
				global0._send('setHeading:', 270)
				cycles = 8
			#end:case
			case 2:
				global0._send(
					'normal:', 0,
					'view:', 401,
					'setLoop:', 1,
					'cycleSpeed:', 6,
					'posn:', 193, 153,
					'setCycle:', CT, 3, 1, self
				)
			#end:case
			case 3:
				global91._send('say:', 12, 5, 0, 1, self, 400)
			#end:case
			case 4:
				global1._send('givePoints:', 1)
				theSkull._send('dispose:')
				global0._send('setCycle:', End, self)
			#end:case
			case 5:
				global2._send('obstacles:')._send('dispose:')
				global1._send('handsOn:')
				global0._send('posn:', 204, 151, 'get:', 11, 'reset:', 1)
				global2._send(
					'addObstacle:', Polygon._send('new:')._send(
							'type:', 2,
							'init:', 0, 189, 0, 0, 319, 0, 319, 189, 190, 189, 190, 185, 276, 185, 264, 172, 261, 178, 237, 178, 198, 155, 206, 152, 240, 151, 205, 151, 190, 143, 117, 143, 117, 153, 90, 164, 72, 157, 38, 185, 130, 185, 130, 189,
							'yourself:'
						)
				)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

