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
		argc = sum(v is not None for v in locals().values())

		if (((global9 at: 11) owner:) == global11):
			(theSkull init: stopUpd:)
			(global2
				addObstacle:
					((Polygon new:)
						type: 2
						init:
							0
							189
							0
							0
							319
							0
							319
							189
							190
							189
							190
							185
							276
							185
							264
							172
							261
							178
							237
							178
							198
							155
							206
							152
							240
							151
							205
							151
							190
							143
							117
							143
							117
							153
							90
							164
							72
							157
							38
							185
							130
							185
							130
							189
						yourself:
					)
					((Polygon new:)
						type: 2
						init: 196 152 180 152 176 149 181 146 195 146 200 149
						yourself:
					)
			)
		else:
			(global2
				addObstacle:
					((Polygon new:)
						type: 2
						init:
							0
							189
							0
							0
							319
							0
							319
							189
							190
							189
							190
							185
							276
							185
							264
							172
							261
							178
							237
							178
							198
							155
							206
							152
							240
							151
							205
							151
							190
							143
							117
							143
							117
							153
							90
							164
							72
							157
							38
							185
							130
							185
							130
							189
						yourself:
					)
			)
		#endif
		(skelton1 init: stopUpd:)
		(skelton2 init: stopUpd:)
		(skelton3 init: stopUpd:)
		(super init: &rest)
		(global2 setScript: kernel.ScriptID(30, 1))
		(kernel.ScriptID(30, 0) initCrypt: 1)
	#end:method

	@classmethod
	def notify():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(kernel.ScriptID(30, 3) show:)
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
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global2 setScript: getSkull)
			#end:case
			else:
				(super doVerb: param1 &rest)
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
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 == 0):
			(global91 say: 10 5 0 1)
		else:
			(super doVerb: param1 &rest)
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
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 == 0):
			(global91 say: 10 5 0 1)
		else:
			(super doVerb: param1 &rest)
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
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (param1 == 0):
			(global91 say: 10 5 0 1)
		else:
			(super doVerb: param1 &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class getSkull(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: PolyPath 204 151 self)
			#end:case
			case 1:
				(global0 setHeading: 270)
				cycles = 8
			#end:case
			case 2:
				(global0
					normal: 0
					view: 401
					setLoop: 1
					cycleSpeed: 6
					posn: 193 153
					setCycle: CT 3 1 self
				)
			#end:case
			case 3:
				(global91 say: 12 5 0 1 self 400)
			#end:case
			case 4:
				(global1 givePoints: 1)
				(theSkull dispose:)
				(global0 setCycle: End self)
			#end:case
			case 5:
				((global2 obstacles:) dispose:)
				(global1 handsOn:)
				(global0 posn: 204 151 get: 11 reset: 1)
				(global2
					addObstacle:
						((Polygon new:)
							type: 2
							init:
								0
								189
								0
								0
								319
								0
								319
								189
								190
								189
								190
								185
								276
								185
								264
								172
								261
								178
								237
								178
								198
								155
								206
								152
								240
								151
								205
								151
								190
								143
								117
								143
								117
								153
								90
								164
								72
								157
								38
								185
								130
								185
								130
								189
							yourself:
						)
				)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

