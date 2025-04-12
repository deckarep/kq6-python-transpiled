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

	if ((global0 y:) > 137):
		(= temp1
			if ((kernel.ScriptID(80, 5) y:) >= (kernel.ScriptID(80, 6) y:)):
				kernel.ScriptID(80, 5)
			else:
				kernel.ScriptID(80, 6)
			#endif
		)
	else:
		(= temp1
			if ((kernel.ScriptID(80, 5) y:) <= (kernel.ScriptID(80, 6) y:)):
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
	if ((global0 y:) < 137):
		if (temp0 == kernel.ScriptID(80, 5)):
			temp2 = (local6 >> 0x0008)
		else:
			temp2 = (local7 >> 0x0008)
		#endif
	else:
		temp2 = (temp0 x:)
	#endif
	temp3 = (temp1 y:)
	(temp0 cycleSpeed: 5 moveSpeed: 5 setMotion: PolyPath temp2 temp3 param1)
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

		(self
			addObstacle:
				((Polygon new:)
					type: 2
					init:
						141
						117
						170
						117
						113
						153
						128
						153
						116
						165
						98
						165
						75
						179
						63
						182
						45
						182
						36
						178
						13
						178
						0
						186
						0
						-10
						319
						-10
						319
						180
						221
						112
						141
						112
					yourself:
				)
		)
		(global32
			add: eastDoors roomFeatures floor chairs hideFeature
			eachElementDo: #init
		)
		(super init: &rest)
		(kernel.ScriptID(80, 0) guard1Code: guardsCode guard2Code: guardsCode)
		(kernel.ScriptID(1015, 6) talkWidth: 150 x: 15 y: 20)
		(kernel.ScriptID(1015, 7) talkWidth: 135 x: 160 y: 20)
		(kernel.ScriptID(80, 5)
			setScript: kernel.Clone(guardPatrol) 0 1
			init:
			noun: 5
			actions: guardDoVerb
			okToCheck: guardCheck
			ignoreActors:
			sightAngle: 45
		)
		(kernel.ScriptID(80, 6)
			setScript: guardPatrol
			init:
			noun: 5
			actions: guardDoVerb
			okToCheck: guardCheck
			ignoreActors:
			sightAngle: 45
		)
		(kernel.ScriptID(80, 0) setupGuards:)
		(global0
			init:
			setScale: Scaler maxScaleSize minScaleSize maxScaleY minScaleY
		)
		match global12
			case 870:
				(global0 posn: 173 114)
				(kernel.ScriptID(80, 5) okToCheck: 0)
				(kernel.ScriptID(80, 6) okToCheck: 0)
				(self setScript: getCaught)
			#end:case
			else:
				(global0 loop: 1 setSpeed: 6 posn: 79 188)
				(self setScript: hideEgo)
			#end:else
		#end:match
		spotEgoScr = captureEgo
		if (global0 scaler:):
			((global0 scaler:) doit:)
		#endif
		if (not script):
			(global1 handsOn:)
		#endif
		(global105 number: 702 loop: 1 play:)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		local0 = (global0 onControl: 1)
		local1 = (((global0 view:) == 881) or (local0 & 0x0004))
		(cond
			case script: 0#end:case
			case proc999_4(0, 0, 165, 117, global0):
				(global2 newRoom: 870)
			#end:case
		)
		(super doit: &rest)
	#end:method

#end:class or instance

@SCI.instance
class hideEgo(Script):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(global73 addToFront: self)
		(global72 addToFront: self)
		(kernel.ScriptID(80, 5) sightAngle: 180)
		(kernel.ScriptID(80, 6) sightAngle: 180)
		(super init: &rest)
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if ((global0 mover:) and (state == 4)):
			(global1 handsOff:)
			if (not local2):
				local2 = ((User curEvent:) x:)
				local3 = ((User curEvent:) y:)
				cycles = 3
			#endif
			(global0 setMotion: 0)
		#endif
		(super doit:)
	#end:method

	@classmethod
	def handleEvent(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		if 
			(and
				(User canInput:)
				(not (param1 modifiers:))
				((global69 curIcon:) == (global69 at: 3))
				(or
					(kernel.ScriptID(80, 5) onMe: param1)
					(kernel.ScriptID(80, 6) onMe: param1)
				)
			)
			(global1 handsOff:)
			(CueObj state: 0 cycles: 0 client: kernel.ScriptID(80, 5) theVerb: 2)
			((CueObj client:) approachX: 111 approachY: 172)
			(kernel.ScriptID(80, 5) okToCheck: 0)
			(kernel.ScriptID(80, 6) okToCheck: 0)
			local5 = 1
			(global91 say: 5 2 0 1 self)
			next = talkToGuards
			(param1 claimed: 1)
		#endif
		(param1 claimed:)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setMotion: PolyPath 60 180 self)
			#end:case
			case 1:
				(global0 setHeading: 135 self)
			#end:case
			case 2:
				(global0
					normal: 0
					view: 881
					setLoop: 3
					cel: 0
					x: 78
					y: 188
					setScale:
					scaleX: 142
					scaleY: 142
					cycleSpeed: 8
					setCycle: End self
				)
			#end:case
			case 3:
				if (not (kernel.ScriptID(80, 0) tstFlag: 711 2048)):
					(kernel.ScriptID(80, 0) setFlag: 711 2048)
					(global91 say: 1 0 6 0 self)
				else:
					(global91 say: 1 0 7 0 self)
				#endif
			#end:case
			case 4:
				(global1 handsOn:)
			#end:case
			case 5:
				(global73 delete: self)
				(global72 delete: self)
				(kernel.ScriptID(80, 5) sightAngle: 40)
				(kernel.ScriptID(80, 6) sightAngle: 40)
				(global0 setCycle: Beg self)
			#end:case
			case 6:
				(global0
					reset: 5 900
					posn: (hideFeature approachX:) (hideFeature approachY:)
				)
				if 
					(and
						(CueObj client:)
						((CueObj client:) approachX:)
						(&
							((CueObj client:) _approachVerbs:)
							(global66 doit: ((global69 curIcon:) message:))
						)
					)
					if ((CueObj client:) == hideFeature):
						local8 = 1
						((CueObj client:) doVerb: (CueObj theVerb:))
					else:
						(global0
							setMotion:
								PolyPath
								((CueObj client:) approachX:)
								((global0 z:) + ((CueObj client:) approachY:))
								CueObj
						)
					#endif
				else:
					(global0 setMotion: PolyPath local2 local3)
				#endif
				(global1 handsOn:)
				local2 = local3 = register = 0
				(self dispose:)
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
		(super init: &rest)
		if register:
			register = 0
			register = (| (register & 0x00ff) 0xc400)
			register = (| (register & 0xff00) 0x00b3)
			(client posn: (register & 0x00ff) 147)
			state = 0
		else:
			register = (| (register & 0x00ff) 0xce00)
			register = (| (register & 0xff00) 0x00df)
			(client posn: (register >> 0x0008) 114)
		#endif
		cycles = 1
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		register = 0
		(super dispose:)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(client setMotion: MoveTo (register & 0x00ff) 147 self)
			#end:case
			case 1:
				(client setMotion: MoveTo (register >> 0x0008) 114 self)
			#end:case
			case 2:
				(client setHeading: 270 self)
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
				(global91 say: 1 0 2 0 self)
			#end:case
			case 2:
				(global2 spotEgo: proc80_7())
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
		(super dispose: &rest)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				local6 = ((kernel.ScriptID(80, 5) script:) register:)
				local7 = ((kernel.ScriptID(80, 6) script:) register:)
				(kernel.ScriptID(80, 5) setScript: 0 setMotion: 0 okToCheck: 0)
				(kernel.ScriptID(80, 6) setScript: 0 setMotion: 0 okToCheck: 0)
				proc913_4(register, global0, self)
			#end:case
			case 1:
				(global91 say: 1 0 3 1 self)
			#end:case
			case 2:
				(cond
					case (not (global0 facingMe: kernel.ScriptID(80, 5))):
						proc913_4(kernel.ScriptID(80, 5), global0, self)
					#end:case
					case (not (global0 facingMe: kernel.ScriptID(80, 6))):
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
				(global91 say: 1 0 3 2 self)
			#end:case
			case 6:
				(global91 say: 1 0 3 3 self)
			#end:case
			case 7:
				(global91 say: 1 0 3 4 self)
			#end:case
			case 8:
				(proc80_7() setScript: kernel.ScriptID(80, 4) self 1)
			#end:case
			case 9:
				(global91 say: 1 0 3 5 self oneOnly: 0)
			#end:case
			case 10:
				(global2 newRoom: 820)
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
		(super dispose: &rest)
	#end:method

	@classmethod
	def changeState(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match state = param1
			case 0:
				(global1 handsOff:)
				(kernel.ScriptID(80, 5) okToCheck: 0)
				(kernel.ScriptID(80, 6) okToCheck: 0)
				(kernel.ScriptID(80, 5) approachX: 0 approachY: 0)
				if (not local5):
					(global91 say: 5 2 0 1 self)
				else:
					cycles = 1
				#endif
			#end:case
			case 1:
				if local1:
					(global0 setMotion: PolyPath 111 172 self)
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				if (not (global0 facingMe: kernel.ScriptID(80, 5))):
					proc913_4(kernel.ScriptID(80, 5), global0, self)
				else:
					cycles = 1
				#endif
			#end:case
			case 3:
				cycles = 1
			#end:case
			case 4:
				(global91 say: 5 2 0 2 self oneOnly: 0)
			#end:case
			case 5:
				(global2 spotEgo: proc80_7())
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

		(super init: &rest)
		(self approachVerbs: 5)
	#end:method

	@classmethod
	def doVerb(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				(global2 spotEgo: proc80_7())
			#end:case
			case 1:
				if (not local4):
					local4.post('++')
					(global91 say: noun param1 8)
				else:
					(global91 say: noun param1 9)
				#endif
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def doSpecial(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		match param1
			case 5:
				(global91 say: noun param1 0 0 NewFeature)
			#end:case
			else:
				(super doSpecial:)
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

		x = (param1 x:)
		y = (param1 y:)
		sightAngle = 26505
		return (super onMe: param1)
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

		(super init: &rest)
		(self approachVerbs: 5)
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
					case ((global2 script:) != hideEgo):
						(global2 setScript: hideEgo)
					#end:case
					else:
						(super doVerb: param1)
					#end:else
				)
			#end:case
			else:
				(super doVerb: param1)
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
				(global2 setScript: talkToGuards)
			#end:case
			case (param1 == 37):
				(KQ6Print posn: -1 10 say: 0 5 37 0 1 init:)
				(global0
					setMotion:
						PolyPath
						((CueObj client:) x:)
						((CueObj client:) y:)
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

		return ((not local1) and ((global2 script:) != hideEgo))
	#end:method

#end:class or instance

@SCI.instance
class guardCheck(Code):
	#property vars (may be empty)
	@classmethod
	def doit(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		return ((< 90 (param1 heading:) 270) or ((global0 y:) <= (param1 y:)))
	#end:method

#end:class or instance

@SCI.instance
class roomFeatures(Feature):
	#property vars (may be empty)
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(super init: &rest)
		sightAngle = 26505
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		temp0 = kernel.OnControl(4, (param1 x:), (param1 y:))
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

		(super init: &rest)
		normal = 0
	#end:method

	@classmethod
	def onMe(param1 = None, *rest):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values()) + len(rest)

		(return
			(and
				(super onMe: param1)
				(or
					(and
						((global69 curIcon:) == (global69 useIconItem:))
						((global69 curInvIcon:) == (global9 at: 27))
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
				(global91 say: 8 37 0 0 self)
			#end:case
			else:
				(super doSpecial:)
			#end:else
		#end:match
	#end:method

#end:class or instance

