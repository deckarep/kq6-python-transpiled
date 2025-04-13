#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 860
import sci_sh
import kernel
import Main
import rgCastle
import NewFeature
import KQ6Print
import n913
import Scaler
import PolyPath
import Polygon
import Feature
import Motion
import User
import System

# Public Export Declarations
SCI.public_exports(
	rm860 = 0,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = 1
local2 = None
local3 = None
local4 = None
local5 = None
local6 = None
local7 = None
local8 = None


@SCI.procedure
def localproc_0(param1 = None, *rest):
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values()) + len(rest)

	if (global0._send('y:') > 137):
		(= temp1
			if (kernel.ScriptID(80, 5)._send('y:') >= kernel.ScriptID(80, 6)._send('y:')):
				kernel.ScriptID(80, 5)
			else:
				kernel.ScriptID(80, 6)
			#endif
		)
	else:
		(= temp1
			if (kernel.ScriptID(80, 5)._send('y:') <= kernel.ScriptID(80, 6)._send('y:')):
				kernel.ScriptID(80, 5)
			else:
				kernel.ScriptID(80, 6)
			#endif
		)
	#endif
	match temp1
		case kernel.ScriptID(80, 5):
			temp0 = kernel.ScriptID(80, 6)
		#end:case
		case kernel.ScriptID(80, 6):
			temp0 = kernel.ScriptID(80, 5)
		#end:case
	#end:match
	if (global0._send('y:') < 137):
		if (temp0 == kernel.ScriptID(80, 5)):
			temp2 = (local6 >> 0x0008)
		else:
			temp2 = (local7 >> 0x0008)
		#endif
	else:
		temp2 = temp0._send('x:')
	#endif
	temp3 = temp1._send('y:')
	temp0._send('cycleSpeed:', 5, 'moveSpeed:', 5, 'setMotion:', PolyPath, temp2, temp3, param1)
#end:procedure

@SCI.instance
class rm860(CastleRoom):
	#property vars (may be empty)
	noun = 2
	picture = 860
	style = 10
	south = 730
	vanishingX = 198
	vanishingY = 90
	minScaleSize = 37
	minScaleY = 111
	maxScaleY = 177
	moveOtherGuard = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		self._send(
			'addObstacle:', Polygon._send('new:')._send(
					'type:', 2,
					'init:', 141, 117, 170, 117, 113, 153, 128, 153, 116, 165, 98, 165, 75, 179, 63, 182, 45, 182, 36, 178, 13, 178, 0, 186, 0, -10, 319, -10, 319, 180, 221, 112, 141, 112,
					'yourself:'
				)
		)
		global32._send(
			'add:', eastDoors, roomFeatures, floor, chairs, hideFeature,
			'eachElementDo:', #init
		)
		super._send('init:', &rest)
		kernel.ScriptID(80, 0)._send('guard1Code:', guardsCode, 'guard2Code:', guardsCode)
		kernel.ScriptID(1015, 6)._send('talkWidth:', 150, 'x:', 15, 'y:', 20)
		kernel.ScriptID(1015, 7)._send('talkWidth:', 135, 'x:', 160, 'y:', 20)
		kernel.ScriptID(80, 5)._send(
			'setScript:', kernel.Clone(guardPatrol), 0, 1,
			'init:',
			'noun:', 5,
			'actions:', guardDoVerb,
			'okToCheck:', guardCheck,
			'ignoreActors:',
			'sightAngle:', 45
		)
		kernel.ScriptID(80, 6)._send(
			'setScript:', guardPatrol,
			'init:',
			'noun:', 5,
			'actions:', guardDoVerb,
			'okToCheck:', guardCheck,
			'ignoreActors:',
			'sightAngle:', 45
		)
		kernel.ScriptID(80, 0)._send('setupGuards:')
		global0._send(
			'init:',
			'setScale:', Scaler, maxScaleSize, minScaleSize, maxScaleY, minScaleY
		)
		match global12
			case 870:
				global0._send('posn:', 173, 114)
				kernel.ScriptID(80, 5)._send('okToCheck:', 0)
				kernel.ScriptID(80, 6)._send('okToCheck:', 0)
				self._send('setScript:', getCaught)
			#end:case
			else:
				global0._send('loop:', 1, 'setSpeed:', 6, 'posn:', 79, 188)
				self._send('setScript:', hideEgo)
			#end:else
		#end:match
		spotEgoScr = captureEgo
		if global0._send('scaler:'):
			global0._send('scaler:')._send('doit:')
		#endif
		if (not script):
			global1._send('handsOn:')
		#endif
		global105._send('number:', 702, 'loop:', 1, 'play:')
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		local0 = global0._send('onControl:', 1)
		local1 = ((global0._send('view:') == 881) or (local0 & 0x0004))
		(cond
			case script: 0#end:case
			case proc999_4(0, 0, 165, 117, global0):
				global2._send('newRoom:', 870)
			#end:case
		)
		super._send('doit:', &rest)
	#end:method

#end:class or instance

@SCI.instance
class hideEgo(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		global73._send('addToFront:', self)
		global72._send('addToFront:', self)
		kernel.ScriptID(80, 5)._send('sightAngle:', 180)
		kernel.ScriptID(80, 6)._send('sightAngle:', 180)
		super._send('init:', &rest)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if (global0._send('mover:') and (state == 4)):
			global1._send('handsOff:')
			if (not local2):
				local2 = User._send('curEvent:')._send('x:')
				local3 = User._send('curEvent:')._send('y:')
				cycles = 3
			#endif
			global0._send('setMotion:', 0)
		#endif
		super._send('doit:')
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				User._send('canInput:')
				(not param1._send('modifiers:'))
				(global69._send('curIcon:') == global69._send('at:', 3))
				(or
					kernel.ScriptID(80, 5)._send('onMe:', param1)
					kernel.ScriptID(80, 6)._send('onMe:', param1)
				)
			)
			global1._send('handsOff:')
			CueObj._send('state:', 0, 'cycles:', 0, 'client:', kernel.ScriptID(80, 5), 'theVerb:', 2)
			CueObj._send('client:')._send('approachX:', 111, 'approachY:', 172)
			kernel.ScriptID(80, 5)._send('okToCheck:', 0)
			kernel.ScriptID(80, 6)._send('okToCheck:', 0)
			local5 = 1
			global91._send('say:', 5, 2, 0, 1, self)
			next = talkToGuards
			param1._send('claimed:', 1)
		#endif
		param1._send('claimed:')
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				global0._send('setMotion:', PolyPath, 60, 180, self)
			#end:case
			case 1:
				global0._send('setHeading:', 135, self)
			#end:case
			case 2:
				global0._send(
					'normal:', 0,
					'view:', 881,
					'setLoop:', 3,
					'cel:', 0,
					'x:', 78,
					'y:', 188,
					'setScale:',
					'scaleX:', 142,
					'scaleY:', 142,
					'cycleSpeed:', 8,
					'setCycle:', End, self
				)
			#end:case
			case 3:
				if (not kernel.ScriptID(80, 0)._send('tstFlag:', 711, 2048)):
					kernel.ScriptID(80, 0)._send('setFlag:', 711, 2048)
					global91._send('say:', 1, 0, 6, 0, self)
				else:
					global91._send('say:', 1, 0, 7, 0, self)
				#endif
			#end:case
			case 4:
				global1._send('handsOn:')
			#end:case
			case 5:
				global73._send('delete:', self)
				global72._send('delete:', self)
				kernel.ScriptID(80, 5)._send('sightAngle:', 40)
				kernel.ScriptID(80, 6)._send('sightAngle:', 40)
				global0._send('setCycle:', Beg, self)
			#end:case
			case 6:
				global0._send(
					'reset:', 5, 900,
					'posn:', hideFeature._send('approachX:'), hideFeature._send('approachY:')
				)
				if 
					(and
						CueObj._send('client:')
						CueObj._send('client:')._send('approachX:')
						(&
							CueObj._send('client:')._send('_approachVerbs:')
							global66._send('doit:', global69._send('curIcon:')._send('message:'))
						)
					)
					if (CueObj._send('client:') == hideFeature):
						local8 = 1
						CueObj._send('client:')._send('doVerb:', CueObj._send('theVerb:'))
					else:
						global0._send(
							'setMotion:', PolyPath, CueObj._send('client:')._send(
									'approachX:'
								), (+
									global0._send('z:')
									CueObj._send('client:')._send('approachY:')
								), CueObj
						)
					#endif
				else:
					global0._send('setMotion:', PolyPath, local2, local3)
				#endif
				global1._send('handsOn:')
				local2 = local3 = register = 0
				self._send('dispose:')
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class guardPatrol(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		start = -1
		super._send('init:', &rest)
		if register:
			register = 0
			register = (| (register & 0x00ff) 0xc400)
			register = (| (register & 0xff00) 0x00b3)
			client._send('posn:', (register & 0x00ff), 147)
			state = 0
		else:
			register = (| (register & 0x00ff) 0xce00)
			register = (| (register & 0xff00) 0x00df)
			client._send('posn:', (register >> 0x0008), 114)
		#endif
		cycles = 1
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		register = 0
		super._send('dispose:')
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				client._send('setMotion:', MoveTo, (register & 0x00ff), 147, self)
			#end:case
			case 1:
				client._send('setMotion:', MoveTo, (register >> 0x0008), 114, self)
			#end:case
			case 2:
				client._send('setHeading:', 270, self)
			#end:case
			case 3:
				state = -1
				seconds = 2
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class getCaught(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				cycles = 3
			#end:case
			case 1:
				global91._send('say:', 1, 0, 2, 0, self)
			#end:case
			case 2:
				global2._send('spotEgo:', proc80_7())
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class captureEgo(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		register = 0
		super._send('dispose:', &rest)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				local6 = kernel.ScriptID(80, 5)._send('script:')._send('register:')
				local7 = kernel.ScriptID(80, 6)._send('script:')._send('register:')
				kernel.ScriptID(80, 5)._send('setScript:', 0, 'setMotion:', 0, 'okToCheck:', 0)
				kernel.ScriptID(80, 6)._send('setScript:', 0, 'setMotion:', 0, 'okToCheck:', 0)
				proc913_4(register, global0, self)
			#end:case
			case 1:
				global91._send('say:', 1, 0, 3, 1, self)
			#end:case
			case 2:
				(cond
					case (not global0._send('facingMe:', kernel.ScriptID(80, 5))):
						proc913_4(kernel.ScriptID(80, 5), global0, self)
					#end:case
					case (not global0._send('facingMe:', kernel.ScriptID(80, 6))):
						proc913_4(kernel.ScriptID(80, 6), global0, self)
					#end:case
					else:
						cycles = 1
					#end:else
				)
			#end:case
			case 3:
				localproc_0(self)
			#end:case
			case 4:
				cycles = 2
			#end:case
			case 5:
				global91._send('say:', 1, 0, 3, 2, self)
			#end:case
			case 6:
				global91._send('say:', 1, 0, 3, 3, self)
			#end:case
			case 7:
				global91._send('say:', 1, 0, 3, 4, self)
			#end:case
			case 8:
				proc80_7()._send('setScript:', kernel.ScriptID(80, 4), self, 1)
			#end:case
			case 9:
				global91._send('say:', 1, 0, 3, 5, self, 'oneOnly:', 0)
			#end:case
			case 10:
				global2._send('newRoom:', 820)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class talkToGuards(Script):
	#property vars (may be empty)
	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		register = 0
		super._send('dispose:', &rest)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				global1._send('handsOff:')
				kernel.ScriptID(80, 5)._send('okToCheck:', 0)
				kernel.ScriptID(80, 6)._send('okToCheck:', 0)
				kernel.ScriptID(80, 5)._send('approachX:', 0, 'approachY:', 0)
				if (not local5):
					global91._send('say:', 5, 2, 0, 1, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				if local1:
					global0._send('setMotion:', PolyPath, 111, 172, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				if (not global0._send('facingMe:', kernel.ScriptID(80, 5))):
					proc913_4(kernel.ScriptID(80, 5), global0, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 3:
				cycles = 1
			#end:case
			case 4:
				global91._send('say:', 5, 2, 0, 2, self, 'oneOnly:', 0)
			#end:case
			case 5:
				global2._send('spotEgo:', proc80_7())
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class eastDoors(NewFeature):
	#property vars (may be empty)
	heading = 270
	noun = 3
	sightAngle = 90
	onMeCheck = 2
	approachX = 237
	approachY = 139
	normal = 0
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('approachVerbs:', 5)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global2._send('spotEgo:', proc80_7())
			#end:case
			case 1:
				if (not local4):
					local4.post('++')
					global91._send('say:', noun, param1, 8)
				else:
					global91._send('say:', noun, param1, 9)
				#endif
			#end:case
			else:
				super._send('doVerb:', param1, &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def doSpecial(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				global91._send('say:', noun, param1, 0, 0, NewFeature)
			#end:case
			else:
				super._send('doSpecial:')
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class chairs(Feature):
	#property vars (may be empty)
	noun = 10
	onMeCheck = 8
	
	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		x = param1._send('x:')
		y = param1._send('y:')
		sightAngle = 26505
		return super._send('onMe:', param1)
	#end:method

#end:class or instance

@SCI.instance
class hideFeature(Feature):
	#property vars (may be empty)
	nsTop = 64
	nsBottom = 176
	nsRight = 73
	approachX = 60
	approachY = 180
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		self._send('approachVerbs:', 5)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				(cond
					case local8:
						local8 = 0
					#end:case
					case (global2._send('script:') != hideEgo):
						global2._send('setScript:', hideEgo)
					#end:case
					else:
						super._send('doVerb:', param1)
					#end:else
				)
			#end:case
			else:
				super._send('doVerb:', param1)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class guardDoVerb(Actions):
	#property vars (may be empty)
	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = 1
		(cond
			case (param1 == 2):
				global2._send('setScript:', talkToGuards)
			#end:case
			case (param1 == 37):
				KQ6Print._send('posn:', -1, 10, 'say:', 0, 5, 37, 0, 1, 'init:')
				global0._send(
					'setMotion:', PolyPath, CueObj._send('client:')._send('x:'), CueObj._send(
								'client:'
							)._send(
							'y:'
						)
				)
			#end:case
			else:
				temp0 = 0
			#end:else
		)
	#end:method

#end:class or instance

@SCI.instance
class guardsCode(Code):
	#property vars (may be empty)
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return ((not local1) and (global2._send('script:') != hideEgo))
	#end:method

#end:class or instance

@SCI.instance
class guardCheck(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return ((< 90 param1._send('heading:') 270) or (global0._send('y:') <= param1._send('y:')))
	#end:method

#end:class or instance

@SCI.instance
class roomFeatures(Feature):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		sightAngle = 26505
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = kernel.OnControl(4, param1._send('x:'), param1._send('y:'))
		(return
			(or
				((0x0200 & temp0) and noun = 6)
				((0x0100 & temp0) and noun = 7)
			)
		)
	#end:method

#end:class or instance

@SCI.instance
class floor(NewFeature):
	#property vars (may be empty)
	noun = 8
	onMeCheck = 128
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		super._send('init:', &rest)
		normal = 0
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(and
				super._send('onMe:', param1)
				(or
					(and
						(global69._send('curIcon:') == global69._send('useIconItem:'))
						(global69._send('curInvIcon:') == global9._send('at:', 27))
						_approachVerbs = -32768
						approachX = 154
						approachY = 141
					)
					(and
						(not _approachVerbs = 0)
						(not approachX = 0)
						(not approachY = 0)
					)
				)
			)
		)
	#end:method

	@classmethod
	def doSpecial(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 37:
				global91._send('say:', 8, 37, 0, 0, self)
			#end:case
			else:
				super._send('doSpecial:')
			#end:else
		#end:match
	#end:method

#end:class or instance

