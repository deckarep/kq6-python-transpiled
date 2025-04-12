#!/usr/bin/env python3

### Sierra Script 1.0 - (do not remove this comment)
### Decompiled by sluicebox
### Transpiled by deckarep (python3.10+)
# script# 810
import sci_sh
import kernel
import Main
import rgCastle
import Scaler
import Polygon
import Feature
import MoveFwd
import Motion
import Actor
import System

# Public Export Declarations
SCI.public_exports(
	rm810 = 0,
	proc810_1 = 1,
	beam = 3,
)

# script local declarations
# NOTE: notice how locals are incremented by how many slots the previous local used?
# This doesn't really matter in Python-land, but we will preserve it so everything matches up.
local0 = None
local1 = [0, 189, 0, -10, 319, -10, 319, 189, 254, 189, 222, 132, 126, 132, 126, 137, 179, 137, 142, 189]
local21 = [0, 189, 0, -10, 319, -10, 319, 189, 256, 189, 207, 106, 199, 106, 142, 189]
local37 = [0, 189, 0, -10, 319, -10, 319, 189, 254, 189, 222, 132, 183, 132, 142, 189]
local53 = None
local54 = None
local55 = None


@SCI.procedure
def localproc_0():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	if (global2 obstacles:):
		((global2 obstacles:) dispose:)
	#endif
	match local0
		case 1:
			(global2 addObstacle: (mainPoly points: @local37 size: 8 yourself:))
		#end:case
		case 2:
			(global2 addObstacle: (mainPoly points: @local21 size: 8 yourself:))
		#end:case
		else:
			(global2 addObstacle: (mainPoly points: @local1 size: 10 yourself:))
		#end:else
	#end:match
#end:procedure

@SCI.procedure
def proc810_1():
	# Python3 magic, for those function which use argc.
	argc = sum(v is not None for v in locals().values())

	(global2 drawPic: (global2 picture:))
	(endHallway init: addToPic:)
	(global0 init: show:)
	(beam cel: 0 show:)
	(chink show:)
	localproc_0()
#end:procedure

@SCI.instance
class rm810(CastleRoom):
	#property vars (may be empty)
	noun = 3
	picture = 810
	style = 10
	horizon = 129
	walkOffEdge = 1
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match global12
			case 781:
				local0 = 1
				local53 = 1
				(global102 fadeTo: 810 -1)
			#end:case
			else:
				(global0 posn: 200 186)
				local0 = 3
			#end:else
		#end:match
		localproc_0()
		(super init: &rest)
		(walls init:)
		(global0 init: reset:)
		if (global12 == 800):
			(global0 loop: 9 cel: 3)
		#endif
		(global0 setScale: Scaler 100 70 190 129)
		((global0 scaler:) doit:)
		(secretDoor init: hide:)
		match global12
			case 781:
				(secretDoor cel: 3 show: stopUpd:)
				(global0
					normal: 0
					view: 781
					setScale: 0
					scaleX: 128
					scaleY: 128
					loop: 3
					cel: 9
					posn: 193 134
				)
				(self setScript: enterBedroom)
			#end:case
			else:
				(global0 posn: 200 186)
			#end:else
		#end:match
		(chink init: hide:)
		(beam init: hide:)
		(endHallway addToPic:)
		if (not script):
			(global1 handsOn:)
		#endif
	#end:method

	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		temp0 = (global0 onControl: 1)
		(cond
			case script: 0#end:case
			case (temp0 & 0x4000):
				if (local0 != 1):
					(self setScript: changeHallways 0 270)
				#endif
			#end:case
			case temp1 = (global0 edgeHit:):
				match temp1
					case 3:
						if (local0 == 3):
							(global2 newRoom: 800)
						else:
							(self setScript: changeHallways 0 180)
						#endif
					#end:case
					case 1:
						(self setScript: changeHallways 0 0)
					#end:case
				#end:match
			#end:case
		)
		(super doit: &rest)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

	@classmethod
	def dispose():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super dispose: &rest)
		kernel.DisposeScript(951)
		kernel.DisposeScript(969)
	#end:method

#end:class or instance

@SCI.instance
class changeHallways(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				(global0 setHeading: register self)
			#end:case
			case 1:
				(secretDoor startUpd:)
				if register:
					(global0 setMotion: MoveFwd 15 self)
				else:
					cycles = 1
				#endif
			#end:case
			case 2:
				(beam setScript: 0)
				if ((global0 heading:) == 180):
					(global0 posn: 200 133)
					local0.post('++')
				else:
					(global0 posn: 200 188 setHeading: 0)
					local0.post('--')
				#endif
				state.post('++')
				if register = (local0 == 3):
					state.post('--')
					(global0 posn: 156 135 hide: normal: 0)
				#endif
				localproc_0()
				(chink hide:)
				(beam hide:)
				(secretDoor startUpd: hide:)
				(global2 drawPic: 810 10)
				(endHallway addToPic:)
				match local0
					case 2:
						(chink show:)
						(beam show:)
					#end:case
					case 1:
						(secretDoor show: stopUpd:)
					#end:case
				#end:match
				((global0 scaler:) doit:)
				cycles = 10
			#end:case
			case 3:
				(global0 show: normal: 1 setMotion: MoveTo 184 135 self)
			#end:case
			case 4:
				ticks = 30
			#end:case
			case 5:
				if ((local0 == 2) and (not (kernel.ScriptID(80, 0) tstFlag: 711 16))):
					(global91 say: 1 0 4 0 self)
				else:
					cycles = 2
				#endif
			#end:case
			case 6:
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class enterBedroom(Script):
	#property vars (may be empty)
	@classmethod
	def changeState(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match state = param1
			case 0:
				(global1 handsOff:)
				if local53:
					(secretDoor cel: 3)
					cycles = 1
				else:
					(secretDoor setCycle: End self)
				#endif
			#end:case
			case 1:
				(global0
					normal: 0
					view: 781
					setScale: 0
					scaleX: 128
					scaleY: 128
					loop: 3
					cycleSpeed: 8
					posn: 193 134
				)
				if local53:
					state.post('++')
					(global0 cel: 9 setCycle: Beg self)
				else:
					(global0 cel: 0 setCycle: End self)
				#endif
			#end:case
			case 2:
				if (not (kernel.ScriptID(80, 0) tstFlag: 711 1024)):
					(kernel.ScriptID(80, 0) setFlag: 711 1024)
					(global91 say: 6 5 13 0 self)
				else:
					cycles = 1
				#endif
			#end:case
			case 3:
				if local53:
					(global0
						posn: (secretDoor approachX:) (secretDoor approachY:)
						oldScaleSignal: 0
						setScale: Scaler 100 70 190 129
						reset: 1
					)
					((global0 scaler:) doit:)
					local53 = 0
					(secretDoor setCycle: Beg self)
				else:
					(global2 newRoom: 781)
				#endif
			#end:case
			case 4:
				(secretDoor stopUpd:)
				(global1 handsOn:)
				(self dispose:)
			#end:case
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class walls(Feature):
	#property vars (may be empty)
	noun = 5
	
	@classmethod
	def onMe(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		local54 = (proc999_4(142, 64, 157, 156, param1) and (local0 == 2))
		return (not (0x0002 & kernel.OnControl(4, (param1 x:), (param1 y:))))
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				if local54:
					temp0 = 11
				else:
					temp0 = 12
				#endif
				(global91 say: noun param1 temp0)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class endHallway(View):
	#property vars (may be empty)
	onMeCheck = 0
	view = 810
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		cel = (0 if (local0 == 3) else local0)
		match cel
			case 1:
				x = 203
				y = 101
			#end:case
			case 2:
				x = 200
				y = 106
			#end:case
		#end:match
		priority = 0
		(signal |= 0x6010)
		(super init: &rest)
	#end:method

#end:class or instance

@SCI.instance
class chink(View):
	#property vars (may be empty)
	x = 148
	y = 167
	z = 42
	noun = 4
	approachX = 164
	approachY = 169
	view = 810
	loop = 1
	priority = 10
	signal = 16400
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 1 5)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 1:
				(global2 setScript: kernel.ScriptID(811))
			#end:case
			case 5:
				(global2 setScript: kernel.ScriptID(811))
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class beam(Prop):
	#property vars (may be empty)
	x = 148
	y = 167
	z = 42
	onMeCheck = 0
	view = 810
	loop = 2
	cel = 8
	signal = 16400
	
	@classmethod
	def doit():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		if (not (signal & 0x0008)):
			if (((global0 x:) <= 216) and (>= 169 (global0 y:) 165)):
				cel = ((((global0 x:) - x) / 7) - 1)
				priority = ((global0 priority:) - 1)
			else:
				priority = kernel.CoordPri(y)
				cel = 8
			#endif
		#endif
		(super doit:)
	#end:method

	@classmethod
	def setScript(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super setScript: param1 &rest)
	#end:method

#end:class or instance

@SCI.instance
class secretDoor(Prop):
	#property vars (may be empty)
	x = 175
	y = 127
	noun = 6
	approachX = 192
	approachY = 134
	view = 781
	loop = 2
	signal = 24592
	
	@classmethod
	def init():
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		(super init: &rest)
		(self approachVerbs: 5)
	#end:method

	@classmethod
	def doVerb(param1 = None):
		# Python3 magic, for those function which use argc.
		argc = sum(v is not None for v in locals().values())

		match param1
			case 5:
				(global2 setScript: enterBedroom)
			#end:case
			else:
				(super doVerb: param1 &rest)
			#end:else
		#end:match
	#end:method

#end:class or instance

@SCI.instance
class mainPoly(Polygon):
	#property vars (may be empty)
	type = 2
	
#end:class or instance

