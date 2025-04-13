#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 300
import sci_sh
import kernel
import Main
import rCliffs
import KQ6Print
import n301
import n913
import Conversation
import PolyPath
import Polygon
import Feature
import LoadMany
import Motion
import User
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm300 = 0,
	stepDownToBeach = 1,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 108, 142, 200, 219, 170, 156, 170, 166, 188, 46, 53, 90, 25, 258, 223, 245, 122, 112, 106, 111, 113, 109, 117]
local37 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4]
local65 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 6, 7]
local93 = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 3, 0, 0, 0, 4, 0, 4, 0, 0, 0, 4, 0]
local121 = [105, 111, 124, 137, 152, 166, 177, 191, 204, 134, 146, 153, 163, 172, 115, 134, 141, 153, 166, 181, 116, 126, 135, 146, 158, 170, 180, 190]
local149 = [56, 56, 56, 56, 56, 56, 56, 56, 56, 73, 73, 73, 73, 73, 89, 89, 89, 89, 89, 89, 105, 105, 105, 105, 105, 105, 105, 105]
local177 = [49, 49, 49, 49, 49, 49, 49, 49, 49, 66, 66, 66, 66, 66, 82, 82, 82, 82, 82, 82, 98, 98, 98, 98, 98, 98, 98, 98]
local205 = [102, 108, 121, 134, 149, 163, 174, 188, 201, 131, 143, 150, 160, 169, 112, 131, 138, 150, 163, 178, 113, 123, 132, 143, 155, 167, 177, 187]
local233 = [108, 121, 134, 149, 163, 174, 188, 201, 214, 143, 150, 160, 169, 183, 131, 138, 150, 163, 178, 188, 123, 132, 143, 155, 167, 177, 187, 200]
local261 = [65, 65, 65, 65, 65, 65, 65, 65, 65, 81, 81, 81, 81, 81, 98, 98, 98, 98, 98, 98, 113, 113, 113, 113, 113, 113, 113, 113]
local289 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 1, 2, 6, 0, 0]
local323 = None
local324 = None
local325 = None
local326 = None
local327 = None


class WalkFeature(Feature):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		global93._send('add:', self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global93._send('delete:', self)
		super._send('dispose:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = global80._send('curEvent:')
		if (param1 == 3):
			(cond
				case ((global0._send('view:') == 301) and (global0._send('loop:') == 3)): 0#end:case
				case (global0._send('y:') < 38):
					global2._send('setScript:', splatterDie, 0, 1)
				#end:case
				case (global0._send('y:') < 95):
					global2._send('setScript:', splatterDie, 0, 0)
				#end:case
				case (global0._send('y:') <= 105):
					kernel.ScriptID(21, 0)._send('cue:')
					global2._send('setScript:', stepDownToBeach)
				#end:case
				case proc999_5((== global0._send('view:') 301 301)): 0#end:case
				else:
					if ((temp0._send('y:') > 160) and (global0._send('onControl:', 1) == 64)):
						temp0._send('y:', 160)
					#endif
					global0._send('setScript:', walkThere, 0, temp0)
				#end:else
			)
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class rm300(CliffRoom):
	#property vars (may be empty)
	noun = 8
	picture = 300
	horizon = 0
	walkOffEdge = 1
	
	@classmethod
	def notify():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global2._send('setScript:', rockStair)
	#end:method

	@classmethod
	def cue():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case (global0._send('y:') < 38):
				global2._send('setScript:', splatterDie, 0, 1)
			#end:case
			case (global0._send('y:') < 95):
				global2._send('setScript:', splatterDie, 0, 0)
			#end:case
		)
	#end:method

	@classmethod
	def makeARock():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		local324 = 1
		super._send('makeARock:')
	#end:method

	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global2._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 319, 189, 253, 189, 241, 181, 238, 175, 233, 159, 230, 149, 223, 114, 211, 113, 209, 111, 190, 116, 103, 115, 88, 124, 73, 122, 72, 125, 66, 135, 70, 155, 90, 189, 6, 189, 0, 189, 0, 0, 319, 0,
					'yourself:'
				)
		)
		if (global12 != 380):
			global102._send('number:', 915, 'setLoop:', -1, 'play:')
		#endif
		global105._send('number:', 916, 'setLoop:', -1, 'play:')
		if proc913_0(157):
			self._send('north:', 340)
		else:
			self._send('north:', 320)
		#endif
		if (global12 == 320):
			self._send('style:', 13)
		else:
			self._send('style:', -32758)
		#endif
		super._send('init:')
		global32._send('add:', cliffs, ocean, rock, stone, beach, 'eachElementDo:', #init)
		if proc913_0(5):
			self._send('allRocksOut:')
		#endif
		proc958_0(128, 320, 321, 308, 3081, 3082)
		wave._send('init:', 'hide:', 'setScript:', waveScr)
		sanScript._send('init:')
		shimmer1._send('init:')
		shimmer2._send('init:')
		if (global9._send('at:', 12)._send('owner:') == global11):
			feather._send('init:', 'stopUpd:')
		#endif
		if (global9._send('at:', 13)._send('owner:') == global11):
			stench._send('init:', 'stopUpd:')
		#endif
		global0._send('actions:', egoDoVerb)
		(cond
			case proc999_5(global12, 370, 380):
				global0._send('init:', 'reset:', 'posn:', 340, -10)
				proc301_0()
			#end:case
			case proc999_5(global12, 320, 340):
				if (global12 == 320):
					kernel.UnLoad(128, 322)
				#endif
				kernel.Load(128, 321)
				global0._send('view:', 301, 'setLoop:', 1, 'cel:', 0, 'init:', 'posn:', 70, 4)
				global2._send('setScript:', stepDownFromCliff)
			#end:case
		)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(cond
			case 
				(and
					(global0._send('onControl:', 1) == 64)
					(global0._send('view:') == 308)
					(global0._send('view:') != 900)
				):
				local325 = 0
				global103._send('fade:', 0, 10, 15, 1)
				global0._send('view:', 900)
			#end:case
			case 
				(and
					(global0._send('onControl:', 1) == 32)
					((global0._send('view:') == 900) or (global0._send('view:') == 3081))
					(global0._send('view:') != 308)
				):
				global103._send('number:', 922, 'setLoop:', -1, 'play:')
				(cond
					case (global0._send('view:') != 900): 0#end:case
					case (global0._send('heading:') < 135):
						global0._send('loop:', 0)
					#end:case
					case (global0._send('heading:') > 225):
						global0._send('loop:', 1)
					#end:case
					else:
						global0._send('loop:', 2)
					#end:else
				)
				global0._send('view:', 308)
			#end:case
			case 
				(and
					(or
						(global0._send('onControl:', 1) == 512)
						(global0._send('onControl:', 1) == 1024)
					)
					(global0._send('view:') != 3081)
				):
				global0._send('view:', 3081)
			#end:case
			case 
				(and
					(or
						(global0._send('onControl:', 1) == 4096)
						(global0._send('onControl:', 1) == 2048)
					)
					(global0._send('view:') != 3082)
					(not local323)
				):
				global0._send('view:', 3082)
			#end:case
		)
		super._send('doit:')
	#end:method

	@classmethod
	def newRoom(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 != 320):
			global102._send('fade:', 0, 5, 5)
			global105._send('fade:', 0, 5, 5)
		#endif
		super._send('newRoom:', param1)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		kernel.DisposeScript(301)
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class myConv(Conversation):
	#property vars (may be empty)
#end:class or instance

@SCI.instance
class puzzle(PuzzleInset):
	#property vars (may be empty)
	x = 157
	y = 39
	z = -45
	view = 320
	signal = 16384
	maxButtons = 4
	buttNumber = 28
	buttView = 321
	lookMsg = 8
	puzzNumber = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send(
			'buttTop:', @local177,
			'buttLeft:', @local205,
			'buttRight:', @local233,
			'buttBottom:', @local261,
			'buttLoop:', @local37,
			'buttCel:', @local65,
			'buttX:', @local121,
			'buttY:', @local149,
			'buttVal:', @local93,
			'buttKill:', @local289
		)
		global0._send('hide:', 'view:', 300)
		kernel.UnLoad(128, 900)
		words._send('init:')
		super._send('init:')
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		words._send('dispose:')
		global0._send('view:', 900, 'loop:', 3, 'show:')
		super._send('dispose:')
	#end:method

#end:class or instance

@SCI.instance
class words(View):
	#property vars (may be empty)
	x = 209
	y = 71
	z = -40
	view = 321
	priority = 13
	signal = 16400
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		puzzle._send('doVerb:', param1, &rest)
	#end:method

#end:class or instance

@SCI.instance
class stench(View):
	#property vars (may be empty)
	x = 68
	y = 127
	noun = 12
	view = 300
	loop = 4
	signal = 16384
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 5):
			(cond
				case (global0._send('y:') < 105):
					global91._send('say:', 6, 12, 14, 1)
				#end:case
				case (global9._send('at:', 13)._send('owner:') == global11):
					global2._send('setScript:', pickItem, 0, self)
				#end:case
			)
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class feather(View):
	#property vars (may be empty)
	x = 210
	y = 128
	noun = 11
	view = 310
	loop = 4
	signal = 16384
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 5):
			if (global0._send('y:') < 105):
				global91._send('say:', 6, 12, 14, 1)
			else:
				global2._send('setScript:', pickItem, 0, self)
			#endif
		else:
			super._send('doVerb:', param1, &rest)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class wave(Prop):
	#property vars (may be empty)
	x = 162
	y = 159
	noun = 7
	view = 300
	priority = 1
	signal = 16
	
#end:class or instance

@SCI.instance
class shimmer1(Prop):
	#property vars (may be empty)
	x = 24
	y = 177
	noun = 7
	view = 300
	loop = 1
	priority = 1
	signal = 16400
	cycleSpeed = 30
	detailLevel = 3
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('setCycle:', Fwd)
		super._send('init:')
	#end:method

#end:class or instance

@SCI.instance
class shimmer2(Prop):
	#property vars (may be empty)
	x = 261
	y = 182
	noun = 7
	view = 300
	loop = 2
	priority = 1
	signal = 16400
	cycleSpeed = 30
	detailLevel = 3
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send('setCycle:', Fwd)
		super._send('init:')
	#end:method

#end:class or instance

@SCI.instance
class sanScript(View):
	#property vars (may be empty)
	x = 138
	y = 189
	z = 124
	noun = 3
	sightAngle = 180
	view = 326
	signal = 16400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		global72._send('add:', self)
		global73._send('add:', self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global72._send('delete:', self)
		global73._send('delete:', self)
		super._send('dispose:')
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				User._send('canInput:')
				(param1._send('type:') != 16384)
				(not param1._send('modifiers:'))
				self._send('onMe:', param1)
				(not kernel.ScriptID(21, 0)._send('puzzleIsUp:'))
				(or
					(global69._send('curIcon:') == global69._send('at:', 1))
					(global69._send('curIcon:') == global69._send('at:', 2))
				)
				((param1._send('message:') == 13) or (param1._send('type:') == 1))
				User._send('canInput:')
				(param1._send('type:') != 16384)
				(not param1._send('modifiers:'))
			)
			param1._send('claimed:', 1)
			(cond
				case (global0._send('y:') <= 105):
					if global25:
						if global25:
							global25._send('dispose:')
						#endif
					else:
						global91._send('say:', 3, 1, 14, 1)
					#endif
				#end:case
				case (proc913_0(6) or proc913_0(5)):
					puzzle._send('puzzSolved:')
				#end:case
				else:
					global0._send('setScript:', goToInset)
				#end:else
			)
		else:
			super._send('handleEvent:', param1)
		#endif
	#end:method

#end:class or instance

@SCI.instance
class stone(WalkFeature):
	#property vars (may be empty)
	noun = 9
	onMeCheck = 256
	
#end:class or instance

@SCI.instance
class rock(WalkFeature):
	#property vars (may be empty)
	noun = 9
	onMeCheck = 3072
	
#end:class or instance

@SCI.instance
class ocean(WalkFeature):
	#property vars (may be empty)
	noun = 7
	onMeCheck = 4640
	
#end:class or instance

@SCI.instance
class cliffs(WalkFeature):
	#property vars (may be empty)
	noun = 8
	onMeCheck = 128
	
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 1:
				if local324:
					global91._send('say:', 8, 1, 22, 0)
				else:
					global91._send('say:', 8, 1, 5, 0)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class beach(Feature):
	#property vars (may be empty)
	noun = 2
	onMeCheck = 64
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		global93._send('add:', self)
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global93._send('delete:', self)
		super._send('dispose:')
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = global80._send('curEvent:')
		match param1
			case 3:
				(cond
					case ((global0._send('view:') == 301) and (global0._send('loop:') == 3)): 0#end:case
					case (global0._send('y:') < 38):
						global2._send('setScript:', splatterDie, 0, 1)
					#end:case
					case (global0._send('y:') < 95):
						global2._send('setScript:', splatterDie, 0, 0)
					#end:case
					case (global0._send('y:') <= 105):
						kernel.ScriptID(21, 0)._send('cue:')
						global2._send('setScript:', stepDownToBeach)
					#end:case
					case ((global0._send('view:') == 301) or (global0._send('view:') == 301)): 0#end:case
					else:
						if 
							(and
								(temp0._send('y:') > 160)
								(global0._send('onControl:', 1) == 64)
							)
							temp0._send('y:', 160)
						#endif
						global0._send('setScript:', walkThere, 0, temp0)
					#end:else
				)
			#end:case
			case 1:
				if proc913_0(5):
					global91._send('say:', 2, 1, 22, 1)
				else:
					global91._send('say:', 2, 1, 5, 1)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class waveScr(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if (global1._send('detailLevel:') > wave._send('detailLevel:')):
					wave._send('show:', 'cel:', 0, 'setCycle:', End, self)
				else:
					(state += 1)
					self._send('cue:')
				#endif
			#end:case
			case 1:
				wave._send('setCycle:', Beg, self)
			#end:case
			case 2:
				state = -1
				wave._send('hide:')
				seconds = kernel.Random(1, 7)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walkThere(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				if 
					(or
						(global0._send('onControl:', 1) == 32)
						(global0._send('onControl:', 1) == 512)
						(global0._send('onControl:', 1) == 1024)
					)
					local325 = 1
				else:
					local325 = 0
				#endif
				global0._send('setMotion:', PolyPath, register._send('x:'), register._send('y:'), self)
			#end:case
			case 1:
				cycles = 2
			#end:case
			case 2:
				(cond
					case 
						(and
							(not local325)
							(or
								(global0._send('onControl:', 1) == 32)
								(global0._send('onControl:', 1) == 512)
								(global0._send('onControl:', 1) == 1024)
							)
						):
						global91._send('say:', 7, 3, 24, 1, self)
					#end:case
					case 
						(or
							(global0._send('onControl:', 1) == 4096)
							(global0._send('onControl:', 1) == 2048)
						):
						myConv._send('add:', -1, 7, 3, 26, 1, 'add:', -1, 7, 3, 26, 2, 'init:', self)
					#end:case
					else:
						self._send('cue:')
					#end:else
				)
			#end:case
			case 3:
				if 
					(or
						(global0._send('onControl:', 1) == 4096)
						(global0._send('onControl:', 1) == 2048)
					)
					self._send('cue:')
				else:
					self._send('dispose:')
				#endif
			#end:case
			case 4:
				global1._send('handsOff:')
				local323 = 1
				global103._send('number:', 921, 'setLoop:', 1, 'play:')
				global0._send(
					'view:', 309,
					'cel:', 0,
					'normal:', 0,
					'cycleSpeed:', 6,
					'setCycle:', End, self
				)
			#end:case
			case 5:
				global2._send('newRoom:', 135)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class splatterDie(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				rCliffs._send('cheatCount:', 0)
				if (register == 0):
					kernel.Load(128, 201)
				#endif
				kernel.ScriptID(21, 0)._send('cue:')
				global91._send('say:', 4, 3, 8, 1, self)
			#end:case
			case 1:
				if (global0._send('loop:') < 6):
					global0._send(
						'setLoop:', 4,
						'posn:', (global0._send('x:') - 19), (global0._send('y:') + 6),
						'cel:', 2
					)
					ticks = 2
				else:
					self._send('cue:')
				#endif
			#end:case
			case 2:
				global104._send('number:', 305, 'setLoop:', 1, 'play:')
				if (global0._send('loop:') == 6):
					global0._send(
						'view:', 3011,
						'posn:', (global0._send('x:') + 18), (global0._send('y:') + 10),
						'cycleSpeed:', 6,
						'setLoop:', 1
					)
				else:
					global0._send(
						'view:', 301,
						'posn:', global0._send('x:'), (global0._send('y:') + 2),
						'cycleSpeed:', 6,
						'setLoop:', 3
					)
				#endif
				global0._send('cel:', 0, 'setCycle:', End, self)
			#end:case
			case 3:
				if (global0._send('view:') == 301):
					global0._send('setCycle:', Beg, self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 4:
				if (global0._send('view:') == 301):
					global0._send(
						'posn:', (global0._send('x:') + 18), (global0._send('y:') - 7),
						'setLoop:', kernel.Random(1, 2)
					)
				else:
					global0._send(
						'posn:', (global0._send('x:') - 18), (global0._send('y:') - 10),
						'setLoop:', 6
					)
				#endif
				global0._send('view:', 301, 'cycleSpeed:', 6, 'cel:', 0)
				cycles = 10
			#end:case
			case 5:
				if (global0._send('loop:') == 4):
					global0._send('posn:', (global0._send('x:') - 1), (global0._send('y:') - 9))
				else:
					global0._send('posn:', (global0._send('x:') - 1), (global0._send('y:') - 3))
				#endif
				global0._send('view:', 307, 'cycleSpeed:', 1, 'setLoop:', 0)
				proc913_1(59)
				if (global90 & 0x0002):
					KQ6Print._send('modeless:', 1, 'posn:', -1, 10, 'say:', 0, 4, 3, 8, 2, 'init:')
				#endif
				cycles = 4
			#end:case
			case 6:
				global0._send('setCycle:', End, self)
			#end:case
			case 7:
				proc913_2(59)
				global104._send('number:', 306, 'setLoop:', 1, 'play:')
				global0._send('setLoop:', 1, 'yStep:', 35)
				if (register == 0):
					temp0 = 15
				else:
					temp0 = 0
				#endif
				global0._send(
					'setStep:', 10, 12,
					'setMotion:', PolyPath, (global0._send('x:') + temp0), 116, self
				)
			#end:case
			case 8:
				if (register == 0):
					self._send('setScript:', bounceButt, self)
				else:
					global0._send('setLoop:', 2, 'setCycle:', End, self)
				#endif
				global104._send('stop:')
				global103._send('number:', 307, 'setLoop:', 1, 'play:')
			#end:case
			case 9:
				if (register == 0):
					global0._send(
						'setLoop:', 4,
						'cel:', 0,
						'posn:', (global0._send('x:') - 55), (global0._send('y:') + 19),
						'setCycle:', End, self
					)
				else:
					global91._send('say:', 4, 3, 9, 1, self)
				#endif
			#end:case
			case 10:
				if (register == 0):
					global0._send(
						'posn:', (global0._send('x:') + 33), (global0._send('y:') + 4),
						'reset:', 5
					)
					cycles = 8
				else:
					self._send('cue:')
				#endif
			#end:case
			case 11:
				if (register == 0):
					if (local326 == 3):
						global91._send('say:', 1, 0, 15, 1, self)
					else:
						global91._send('say:', 4, 3, 8, 3, self)
					#endif
				else:
					self._send('cue:')
				#endif
			#end:case
			case 12:
				if (register == 0):
					global1._send('handsOn:')
					global0._send('actions:', egoDoVerb)
					self._send('dispose:')
				else:
					global105._send('fade:', 0, 5, 5)
					proc0_1(8)
				#endif
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class bounceButt(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				local326.post('++')
				global0._send(
					'view:', 307,
					'setLoop:', 3,
					'cel:', 0,
					'normal:', 0,
					'setSpeed:', 6,
					'posn:', global0._send('x:'), global0._send('y:')
				)
				ticks = 4
			#end:case
			case 1:
				global0._send('cel:', 1, 'posn:', (global0._send('x:') + 4), (global0._send('y:') - 1))
				ticks = 4
			#end:case
			case 2:
				global0._send('cel:', 2, 'posn:', global0._send('x:'), (global0._send('y:') - 1))
				ticks = 4
			#end:case
			case 3:
				global0._send('cel:', 3, 'posn:', global0._send('x:'), (global0._send('y:') - 5))
				ticks = 4
			#end:case
			case 4:
				global0._send('cel:', 4, 'posn:', global0._send('x:'), (global0._send('y:') - 1))
				ticks = 4
			#end:case
			case 5:
				global0._send('cel:', 5, 'posn:', global0._send('x:'), (global0._send('y:') - 1))
				ticks = 4
			#end:case
			case 6:
				global0._send('cel:', 6, 'posn:', global0._send('x:'), (global0._send('y:') - 1))
				ticks = 4
			#end:case
			case 7:
				global74._send('delete:', global2)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class stepDownFromCliff(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				rCliffs._send('cue:', 'cheatCount:', 8, 'stepDirection:', 1)
				global0._send(
					'view:', 301,
					'setLoop:', 8,
					'cel:', 0,
					'cycleSpeed:', 16,
					'posn:', (global0._send('x:') + 1), global0._send('y:')
				)
				cycles = 8
			#end:case
			case 1:
				if (local327 == 0):
					if (global12 == 340):
						global91._send('say:', 1, 0, 6, 1, self)
					else:
						cycles = 1
					#endif
				else:
					self._send('cue:')
				#endif
			#end:case
			case 2:
				proc21_1()
				global0._send('cel:', 1, 'posn:', global0._send('x:'), global0._send('y:'))
				cycles = 8
			#end:case
			case 3:
				global0._send('cel:', 2, 'posn:', global0._send('x:'), global0._send('y:'))
				cycles = 8
			#end:case
			case 4:
				global0._send('cel:', 3, 'posn:', global0._send('x:'), global0._send('y:'))
				cycles = 8
			#end:case
			case 5:
				global0._send('cel:', 4, 'posn:', (global0._send('x:') + 1), global0._send('y:'))
				cycles = 8
			#end:case
			case 6:
				global0._send('cel:', 5, 'posn:', (global0._send('x:') - 1), global0._send('y:'))
				cycles = 8
			#end:case
			case 7:
				global0._send('cel:', 6, 'posn:', (global0._send('x:') + 2), global0._send('y:'))
				cycles = 8
			#end:case
			case 8:
				if (local327 == 3):
					self._send('cue:')
				else:
					global0._send(
						'view:', 301,
						'setLoop:', 8,
						'cel:', 0,
						'posn:', (global0._send('x:') + 27), (global0._send('y:') + 12)
					)
					cycles = 8
				#endif
			#end:case
			case 9:
				if (local327 < 3):
					local327.post('++')
					(state -= 9)
				else:
					local327 = 0
					global0._send('setLoop:', 2, 'cel:', 0, 'posn:', 188, 50)
				#endif
				self._send('cue:')
			#end:case
			case 10:
				global1._send('handsOn:')
				kernel.ScriptID(21, 0)._send('notify:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class stepDownToBeach(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				if (rCliffs._send('stepDirection:') == 2):
					global0._send(
						'view:', 301,
						'setLoop:', 5,
						'cel:', 0,
						'posn:', (global0._send('x:') + 18), (global0._send('y:') + 7),
						'setCycle:', End, self
					)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 1:
				if (rCliffs._send('stepDirection:') == 2):
					rCliffs._send('stepDirection:', 3)
					global0._send(
						'view:', 301,
						'setLoop:', 1,
						'cel:', 0,
						'posn:', (global0._send('x:') + 16), (global0._send('y:') - 6)
					)
					cycles = 8
				else:
					self._send('cue:')
				#endif
			#end:case
			case 2:
				global0._send(
					'view:', 301,
					'x:', (global0._send('x:') - 20),
					'y:', (global0._send('y:') + 11),
					'setLoop:', 0,
					'cel:', 5,
					'setCycle:', Beg, self
				)
			#end:case
			case 3:
				if (global12 == 340):
					global91._send('say:', 1, 0, 6, 1, self)
				else:
					self._send('cue:')
				#endif
			#end:case
			case 4:
				global0._send('posn:', 110, 112, 'actions:', egoDoVerb, 'reset:', 3)
				cycles = 8
			#end:case
			case 5:
				global0._send('setHeading:', 180)
				cycles = 14
			#end:case
			case 6:
				global1._send('handsOn:')
				global74._send('delete:', global2)
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class goToInset(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				if proc913_0(5):
					self._send('cue:')
				else:
					global91._send('say:', 3, 1, 0, 1, self)
				#endif
			#end:case
			case 1:
				if global0._send('inRect:', 140, 110, 180, 125):
					self._send('cue:')
				else:
					global0._send('setMotion:', PolyPath, 146, 127, self)
				#endif
			#end:case
			case 2:
				global0._send('setHeading:', 0)
				ticks = 18
			#end:case
			case 3:
				global1._send('handsOn:')
				puzzle._send('init:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class pickItem(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				if (register == stench):
					global0._send(
						'setMotion:', PolyPath, (register._send('x:') + 34), (+
								register._send('y:')
								2
							), self
					)
				else:
					global0._send(
						'setMotion:', PolyPath, (register._send('x:') + 7), (-
								register._send('y:')
								12
							), self
					)
				#endif
			#end:case
			case 1:
				if (register == stench):
					global0._send('setHeading:', 315)
				else:
					global0._send('setHeading:', 180)
				#endif
				ticks = 18
			#end:case
			case 2:
				if (register == stench):
					global0._send(
						'view:', 302,
						'setLoop:', 0,
						'normal:', 0,
						'cel:', 0,
						'setPri:', global0._send('priority:'),
						'posn:', 89, 135,
						'cycleSpeed:', 6,
						'setCycle:', CT, 2, 1, self
					)
				else:
					global0._send(
						'view:', 311,
						'setLoop:', 0,
						'normal:', 0,
						'cel:', 0,
						'setPri:', global0._send('priority:'),
						'posn:', (global0._send('x:') - 2), (global0._send('y:') + 11),
						'cycleSpeed:', 6,
						'setCycle:', CT, 3, 1, self
					)
				#endif
				global1._send('givePoints:', 1)
			#end:case
			case 3:
				if (register == feather):
					feather._send('dispose:')
				else:
					stench._send('dispose:')
				#endif
				global0._send('setCycle:', End, self)
			#end:case
			case 4:
				if (register == feather):
					global0._send('get:', 12)
					global91._send('say:', 11, 5, 0, 1, self)
				else:
					global0._send('get:', 13)
					global91._send('say:', 12, 5, 0, 1, self)
				#endif
			#end:case
			case 5:
				if (register == stench):
					global0._send(
						'reset:', 7,
						'posn:', (global0._send('x:') + 11), (global0._send('y:') - 5)
					)
					kernel.UnLoad(128, 302)
				else:
					global0._send(
						'reset:', 2,
						'posn:', (global0._send('x:') + 2), (global0._send('y:') - 9)
					)
					kernel.UnLoad(128, 311)
				#endif
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class rockStair(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				proc913_1(5)
				seconds = 2
			#end:case
			case 1:
				global2._send('flipRocks:', 0, 'callForRocks:')
			#end:case
			case 2:
				global1._send('handsOn:')
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class egoDoVerb(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (param1 == 12):
			if (global0._send('onControl:', 1) == 64):
				global2._send('setScript:', 130)
				return 1
			else:
				global2._send('setScript:', 130)
				return 1
			#endif
		else:
			return 0
		#endif
	#end:method

#end:class or instance

